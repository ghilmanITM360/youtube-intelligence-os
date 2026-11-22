"""R9 video-only segment renderer. python3 tools/v1r9_render_all.py SEG   (1: 0-75 s, 2: 75-122.3, 3..6 tail). Writes out_r9/seg{N}_video.mp4 (libx264 crf17 bt709, no audio).
Same engine, same scenes as R7/R8; R9 differences: OFL numerals/source-tag font, descender padding, tail fixes (v1r9_tail.py). Audio is muxed later from the single edited WAV."""
import os, sys, math, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v1r9_tail as T          # sets r.NUMFONT / r.PLAINFONT
import v1r4_render as r
import v1r5_seg2 as S
HERE = r.HERE
seg = int(sys.argv[1]); r.BEATS = []
if seg == 1: beats = r.build(); T0, T1 = 0.0, 75.0
elif seg == 2: beats = S.build(); T0, T1 = S.T0, S.T1
else:
    beats = T.build(); T0, T1 = T.SEGS[seg]
os.makedirs(HERE + '/out_r9b', exist_ok=True); out = HERE + '/out_r9b/seg%d_video.mp4' % seg
n = round((T1 - T0) * r.FPS)
cmd = ['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1920x1080', '-r', str(r.FPS), '-i', '-', '-vf', 'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p',
       '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-an', out]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE); last = None
for f in range(n):
    tq = math.floor((T0 + f / r.FPS) * r.CFPS + 1e-6) / r.CFPS
    if tq != last: im = r.render(beats, tq).tobytes(); last = tq
    p.stdin.write(im)
p.stdin.close(); p.wait(); print('seg', seg, n, 'frames ->', out)
