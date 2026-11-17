"""Original primitives from SPEC only; no competitor frames or assets are loaded."""
from pathlib import Path
import hashlib
import json
import subprocess

import cv2
import numpy as np

D = Path(__file__).resolve().parent
S = json.loads((D / 'SPEC.json').read_text())
W, H = S['width'], S['height']
background, ink, accent, teal = [tuple(S[k]) for k in ['background_bgr', 'ink_bgr', 'accent_bgr', 'teal_bgr']]
master = D / 'original_opening_timing_master.mkv'
preview = D / 'original_opening_timing_preview.mp4'
assert not master.exists() and not preview.exists()

def panel(config, color):
    image = np.full((config['height'], config['width'], 3), 255, np.uint8)
    cv2.rectangle(image, (0, 0), (config['width']-1, config['height']-1), ink, 6)
    cv2.rectangle(image, (18, 16), (config['width']-19, 25), color, -1)
    cv2.putText(image, config['label'], (24, 76), cv2.FONT_HERSHEY_DUPLEX, 1.2, ink, 2, cv2.LINE_AA)
    cv2.putText(image, config['sub_label'], (24, 124), cv2.FONT_HERSHEY_SIMPLEX, .75, ink, 2, cv2.LINE_AA)
    return image

first_asset, second_asset = panel(S['first_card'], accent), panel(S['second_card'], teal)

def paste(canvas, asset, x, y):
    h, w = asset.shape[:2]
    x1, y1, x2, y2 = max(0, x), max(0, y), min(W, x+w), min(H, y+h)
    if x1 < x2 and y1 < y2:
        canvas[y1:y2, x1:x2] = asset[y1-y:y2-y, x1-x:x2-x]

process = subprocess.Popen(['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-n', '-f', 'rawvideo',
                            '-pixel_format', 'bgr24', '-video_size', f'{W}x{H}', '-framerate', '24',
                            '-i', 'pipe:0', '-an', '-c:v', 'ffv1', '-level', '3', '-pix_fmt', 'bgr0', str(master)], stdin=subprocess.PIPE)
schedule = []
for f in range(S['frames']):
    image = np.full((H, W, 3), background, np.uint8)
    body_top = None
    if f >= 1:
        t = min(1., (f-1)/11)
        body_top = round(1078 + (620-1078) * (1-(1-t)**2))
        x, y, width, height, radius = 750, body_top, 420, 600, 30
        cv2.rectangle(image, (x+radius, y), (x+width-radius, y+height), ink, -1)
        cv2.rectangle(image, (x, y+radius), (x+width, y+height-radius), ink, -1)
        for cx, cy in [(x+radius, y+radius), (x+width-radius, y+radius), (x+radius, y+height-radius), (x+width-radius, y+height-radius)]:
            cv2.circle(image, (cx, cy), radius, ink, -1)
        cv2.rectangle(image, (x+40, y+80), (x+width-40, y+220), background, -1)
        cv2.putText(image, 'POLICY CORE', (x+56, y+50), cv2.FONT_HERSHEY_DUPLEX, .85, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.rectangle(image, (x+60, y+300), (x+width-60, y+320), accent, -1)
        cv2.rectangle(image, (x+60, y+350), (x+width-100, y+370), teal, -1)
    if f >= 12:
        for point, color in zip(S['console']['light_centers'], [accent, teal]):
            cv2.circle(image, tuple(point), 24, color, -1)
    first_xy = None
    if f >= 6:
        t = min(1., (f-6)/26)
        first_xy = [round(a+(b-a)*t) for a, b in zip(S['first_card']['start_xy'], S['first_card']['end_xy'])]
        paste(image, first_asset, *first_xy)
    if f >= 32:
        paste(image, second_asset, *S['second_card']['xy'])
    schedule.append(dict(frame=f, console_top=body_top, lights_visible=f>=12,
                         first_card_xy=first_xy, second_card_visible=f>=32))
    process.stdin.write(image.tobytes())
process.stdin.close()
assert process.wait() == 0
subprocess.run(['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-n', '-i', str(master), '-an',
                '-vf', 'scale=in_range=full:out_range=tv:out_color_matrix=bt709',
                '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-pix_fmt', 'yuv420p',
                '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                '-movflags', '+faststart', str(preview)], check=True)

def decode(path):
    cap, frames = cv2.VideoCapture(str(path)), []
    while True:
        ok, image = cap.read()
        if not ok:
            break
        frames.append(image)
    cap.release()
    return frames

frames = decode(master)
assert len(frames) == 37 and frames[0].shape == (1080, 1920, 3)
assert np.all(frames[0] == np.array(background, np.uint8))
assert np.any(frames[1][1078:] != frames[0][1078:])
assert np.array_equal(frames[5][:64, :64], frames[0][:64, :64])
assert not np.array_equal(frames[6][:64, :64], frames[0][:64, :64])
assert tuple(frames[11][770, 880]) != accent and tuple(frames[12][770, 880]) == accent
assert not np.array_equal(frames[11][600:], frames[12][600:])
assert all(np.array_equal(frames[12][600:], im[600:]) for im in frames[12:])
assert cv2.minMaxLoc(cv2.matchTemplate(frames[22], first_asset, cv2.TM_SQDIFF))[0] > 1
assert cv2.minMaxLoc(cv2.matchTemplate(frames[23], first_asset, cv2.TM_SQDIFF))[0] < 1
assert np.array_equal(frames[31][70:250, 1120:1740], frames[0][70:250, 1120:1740])
assert np.array_equal(frames[32][70:250, 1120:1740], second_asset)
assert all(np.array_equal(frames[32], im) for im in frames[32:])
preview_frames = decode(preview)
assert len(preview_frames) == 37
requests = []
for f in S['checkpoints']:
    path = D / f'check_f{f:03d}.png'
    assert cv2.imwrite(str(path), preview_frames[f])
    requests.append(dict(frame=f, path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                         scale='NATIVE_RENDER_FULLFRAME1920x1080_NOT_SOURCE_EVIDENCE'))
for f, name, xywh in [(0, 'body_tip', [700, 1000, 520, 80]), (1, 'body_tip', [700, 1000, 520, 80]),
                      (5, 'card_tip', [0, 0, 64, 64]), (6, 'card_tip', [0, 0, 64, 64])]:
    x, y, w, h = xywh
    path = D / f'check_f{f:03d}_{name}_ROI.png'
    assert cv2.imwrite(str(path), preview_frames[f][y:y+h, x:x+w])
    requests.append(dict(frame=f, path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                         crop_xywh=xywh, scale='NATIVE_RENDER_ROI_NOT_SOURCE_EVIDENCE'))
probe = json.loads(subprocess.check_output(['/opt/homebrew/bin/ffprobe', '-v', 'error', '-count_frames',
                  '-show_streams', '-of', 'json', str(preview)]))
assert len(probe['streams']) == 1 and probe['streams'][0]['codec_type'] == 'video'
assert probe['streams'][0]['nb_read_frames'] == '37' and probe['streams'][0]['avg_frame_rate'] == '24/1'
result = dict(status='NUMERIC_RENDER_GATES_PASS_VISUAL_QA_PENDING', decoded_frames=37,
              resolution=[W, H], fps=24, frame_schedule=schedule, independent_media_probe=probe,
              lossless_master_sha256=hashlib.sha256(master.read_bytes()).hexdigest(),
              preview_sha256=hashlib.sha256(preview.read_bytes()).hexdigest(),
              decoded_checks=['blank0/body1', 'panel1 first6 and fully inside23', 'lights12',
                              'console anchors fixed12–36', 'panel2 first32', 'all asset hold32–36'],
              image_view_requests=requests, actual_image_views_performed_by_renderer=0,
              media_local_only=True, actual_listening_seconds=0, CT_SCAN_COMPLETE=False,
              limitations=['A bounded original timing test; not source pixel recreation or whole-video production.',
                           'Lossless master validates exact geometry; preview has declared BT709/YUV420 encoding.',
                           'Source hearing and any source music/SFX alignment remain unavailable.'])
(D / 'render_validation.json').write_text(json.dumps(result, indent=2) + '\n')
print('Rendered37frames; decoded timing/template/anchor gates PASS;15preview image requests await actual independent review')
