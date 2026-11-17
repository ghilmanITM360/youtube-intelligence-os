import cv2, numpy as np, subprocess, json
rng = np.random.default_rng(7)
S = 2; W, H = 1920*S, 1080*S
def P(x, y): return (int(x*S), int(y*S))
def jit(pts, a=2.0):
    return np.array([[x+rng.normal(0,a), y+rng.normal(0,a)] for x, y in pts])
def poly(c, pts, fill, th=9, closed=True):
    p = (jit(pts)*S).astype(np.int32)
    if fill is not None: cv2.fillPoly(c, [p], fill, cv2.LINE_AA)
    cv2.polylines(c, [p], closed, (35,30,30), th*S, cv2.LINE_AA)
def circ(n, cx, cy, r): return [(cx+r*np.cos(t), cy+r*np.sin(t)) for t in np.linspace(0, 2*np.pi, n, endpoint=False)]
c = np.full((H, W, 3), (232,240,245), np.uint8)  # BGR off-white
# grass tufts
for _ in range(260):
    x, y = rng.uniform(0,1920), rng.uniform(0,1080); 
    for k in range(3):
        cv2.line(c, P(x+k*4,y), P(x+k*4+rng.uniform(-5,5), y-rng.uniform(8,18)), (90,140,80), 2*S, cv2.LINE_AA)
# ground line
poly(c, [(0,905),(480,898),(960,908),(1440,900),(1920,906)], None, 6, False)
# pot (right)
poly(c, circ(40,1150,760,170)[:0] or [(1030,640),(1270,640),(1310,760),(1280,900),(1020,900),(990,760)], (60,120,190))
poly(c, [(1010,620),(1290,620),(1290,665),(1010,665)], (50,100,170))
poly(c, circ(30,1150,780,55), (45,85,140), 6)
# stick figure: head near (627,700), feet at y~905
poly(c, circ(36,627,700,70), (200,215,235))
poly(c, [(627,770),(627,850)], None, 9, False)
poly(c, [(627,800),(560,840)], None, 9, False); poly(c, [(627,800),(710,780)], None, 9, False)
poly(c, [(627,850),(590,905)], None, 9, False); poly(c, [(627,850),(670,905)], None, 9, False)
for ex in (605,650): cv2.circle(c, P(ex,692), 5*S, (35,30,30), -1, cv2.LINE_AA)
poly(c, [(610,725),(627,735),(645,725)], None, 5, False)
# paper grain on canvas (static artwork)
g = rng.normal(0, 7, (H, W, 1)).astype(np.float32)
g = cv2.GaussianBlur(g, (0,0), 0.8)[..., None] * 1.6
c = np.clip(c.astype(np.float32)+g, 0, 255).astype(np.uint8)
# framings
wide = cv2.resize(c, (1920,1080), interpolation=cv2.INTER_AREA)
fx, fy, k = 627, 818, 2.14
M = np.float32([[k,0,2*fx*(1-k)],[0,k,2*fy*(1-k)]])  # canvas2x -> 2x screen
big = cv2.warpAffine(c, M, (W,H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
punch = cv2.resize(big, (1920,1080), interpolation=cv2.INTER_AREA)
ff = subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24','-s','1920x1080',
    '-r','30000/1001','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','12','-r','30000/1001','rt.mp4'], stdin=subprocess.PIPE)
for i in range(90): ff.stdin.write((wide if i < 45 else punch).tobytes())
ff.stdin.close(); ff.wait()
json.dump({"test":"RT-V1-P01","fps":"30000/1001","frames":90,"segments":[
 {"frames":"0-44","framing":"wide","static":True},
 {"frames":"45-89","framing":"punch_in","scale":k,"fixed_point":[fx,fy],"hard_cut_at":45,"static":True}]},
 open('timeline.json','w'), indent=1)
cv2.imwrite('/tmp/_f44.png', wide); cv2.imwrite('/tmp/_f45.png', punch)
