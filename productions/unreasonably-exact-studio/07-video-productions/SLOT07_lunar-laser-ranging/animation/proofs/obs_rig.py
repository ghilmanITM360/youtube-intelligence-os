"""RIG_002 observatory: Codex layers (B4P plate, B4L/B4L2 building, telescope, leaves, ridge) on one 1024x1536 canvas,
assembled and animated by Claude. Telescope is clipped to the slit (it sits INSIDE the dome); leaves slide open; plate and
Moon sit on far parallax planes. Coordinates: 'layer px' = the shared Codex canvas; LAYER_TO_WORLD maps it to design units."""
import json, math, os
import numpy as np, cv2
from PIL import Image
from uemotion import space as S, tokens as T
from uemotion.camera import T3, S3, R3
from uemotion.easing import *      # noqa

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(ROOT, 'assets/rigs/observatory')
RIG = json.load(open(os.path.join(D, 'RIG_002_observatory.json')))
def _a(k): return np.asarray(Image.open(os.path.join(D, RIG['layers'][k]['file'])).convert('RGBA'), np.float32)
L = {k: _a(k) for k in RIG['layers']}
# grade (Claude, compositing, source file untouched): the Codex tube is near-black inside a near-black slit; lift it so it reads at phone size
L['telescope'][..., :3] = np.clip(L['telescope'][..., :3] * 1.55 + 12, 0, 255)
H_, W_ = 1536, 1024
TEL = RIG['layers']['telescope']; TP, TA = np.array(TEL['pivot_altitude'], float), np.array(TEL['aperture'], float)
TEL_AT, TEL_S, TEL_LEAN0 = np.array(TEL['placed_at'], float), TEL['scale'], TEL['tube_lean_deg_in_file']
SLIT_X = RIG['slit']['centre_x']

# slit mask = rows of the dark interior of the open building, filled between the leftmost and rightmost dark pixel, feathered
def _slit_mask():
    b = L['building_open']; dark = (b[..., :3].mean(2) < 40) & (b[..., 3] > 128); m = np.zeros((H_, W_), np.float32)
    for y in range(*RIG['slit']['rows']):
        xs = np.where(dark[y])[0]
        if len(xs) > 4: m[y, xs.min():xs.max() + 1] = 1
    return cv2.GaussianBlur(m, (5, 5), 1.2)
SLIT = _slit_mask()

# design placement of the shared canvas (world units, parallax 1)
K = 1.20; O = (540 - 512 * K, 260.0)
LAYER_TO_WORLD = T3(*O) @ S3(K)
PLATE_K = 1.40; PLATE_Y = 1190 * 1.20 + 260.0 - 1190 * 1.40; PLATE_M = T3(540 - 512 * PLATE_K, PLATE_Y) @ S3(PLATE_K)        # plate on a far plane: mountains line up with the ridge at rest
PLATE_EXTENT = (540 - 512 * PLATE_K, PLATE_Y, 540 + 512 * PLATE_K, PLATE_Y + 1536 * PLATE_K)

def to_world(p): v = LAYER_TO_WORLD @ np.array([p[0], p[1], 1.0]); return (float(v[0]), float(v[1]))

def tel_matrix(lean_deg):
    """layer-space matrix placing the telescope with the tube leaning lean_deg right of vertical (rotation about the altitude bearing)."""
    return T3(*TEL_AT) @ R3(math.radians(lean_deg - TEL_LEAN0)) @ S3(TEL_S) @ T3(-TP[0], -TP[1])

def aperture_layer(lean_deg):
    v = tel_matrix(lean_deg) @ np.array([TA[0], TA[1], 1.0]); return (float(v[0]), float(v[1]))

def _over(dst, src):
    a = src[..., 3:4] / 255; dst[..., :3] = src[..., :3] * a + dst[..., :3] * (1 - a); dst[..., 3:4] = src[..., 3:4] + dst[..., 3:4] * (1 - a)

def compose(open_u=1.0, lean=8.0, ridge=True):
    """the observatory (building + telescope + leaves + ridge) as one RGBA uint8 image in layer space."""
    # V2 seam fix (D07): the closed/open plates differ in texture everywhere (Codex re-render), so blending a full-height
    # vertical band printed a seam down the wall. Base = the OPEN plate everywhere; the CLOSED plate appears only inside the
    # slit area of the dome (rows 633-1000, |x - slit| < 140, feathered) where the shutter has not yet slid away.
    xx = np.arange(W_, dtype=np.float32)[None, :]; yy = np.arange(H_, dtype=np.float32)[:, None]
    band = np.clip((110 * open_u - np.abs(xx - SLIT_X)) / 6 + 0.5, 0, 1) * min(1.0, open_u / 0.02)
    region = np.clip((yy - 625) / 8, 0, 1) * np.clip((1004 - yy) / 8, 0, 1) * np.clip((140 - np.abs(xx - SLIT_X)) / 10, 0, 1)
    w = (region * (1 - band))[..., None]
    out = L['building_open'] * (1 - w) + L['building_closed'] * w
    if open_u > 0.05:
        tel = cv2.warpAffine(L['telescope'], tel_matrix(lean)[:2], (W_, H_), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
        xx = np.arange(W_, dtype=np.float32); band = np.clip((110 * open_u - np.abs(xx - SLIT_X)) / 6 + 0.5, 0, 1)[None, :]
        tel[..., 3] *= SLIT * band; _over(out, tel)
    lv = smoothstep(seg(open_u, 0.0, 0.45))
    for k in ('leaf_left', 'leaf_right'):
        if lv <= 0: continue
        dx = (1 - open_u) * RIG['layers'][k]['closed_dx']
        src = L[k] if abs(dx) < 0.5 else cv2.warpAffine(L[k], np.float32([[1, 0, dx], [0, 1, 0]]), (W_, H_), borderMode=cv2.BORDER_CONSTANT)
        if lv < 1: src = src.copy(); src[..., 3] *= lv
        _over(out, src)
    if ridge: _over(out, L['ridge'])
    return np.clip(out, 0, 255).astype(np.uint8)

PLATE_IMG = Image.fromarray(L['plate'].astype(np.uint8), 'RGBA')

def draw_plate(cv, ctx=None):
    top = tuple(int(v) for v in L['plate'][2, 512, :3]); cv.rect((-800, -1200, 1900, 10), fill=top)   # sky continues above the plate
    with cv.xf(PLATE_M): cv.blit_image(PLATE_IMG)

def draw_observatory(cv, open_u=1.0, lean=8.0):
    with cv.xf(LAYER_TO_WORLD): cv.blit_image(Image.fromarray(compose(open_u, lean), 'RGBA'))
