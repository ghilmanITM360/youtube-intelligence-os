"""V2 -> V3 before/after evidence frames for the defect and text audits (decoded from the delivered MP4s, captions included).
usage: v3_evidence.py   -> renders/roughcut_v3/evidence/<id>_v2_<t>.png, <id>_v3_<t>.png, <id>_pair.jpg"""
import subprocess, io, os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V2 = os.path.join(ROOT, 'renders/roughcut_v2/ROUGH_CUT_V2_PREMIUM_CAPTIONS.mp4'); V3 = os.path.join(ROOT, 'renders/roughcut_v3/SLOT07_V3_PREMIUM_CAPTIONS.mp4')
OUT = os.path.join(ROOT, 'renders/roughcut_v3/evidence'); os.makedirs(OUT, exist_ok=True)
SHOTS = [('D01_illustrative_counts', 64.0, 64.0), ('D02_widths_not_to_scale', 58.6, 58.6), ('D03_not_to_scale', 20.0, 20.0), ('D03b_not_to_scale_stopwatch', 84.0, 84.0),
         ('D04_slightly_slowed_down', 16.0, 16.0), ('D05_pulse_drawn_as_a_dot', 9.0, 9.0), ('D06_observatory_059', 59.0, 59.0), ('D06b_observatory_0597', 59.8, 59.8),
         ('D07_opening_hold_a', 2.5, 2.5), ('D07_opening_hold_b', 3.4, 3.4), ('D08_imagined_mirror', 38.6, 38.6), ('D09_measurement_space_a', 61.5, 61.5),
         ('D09_measurement_space_b', 66.8, 66.8), ('D10_ending_a', 91.0, 91.0), ('D10_ending_b', 94.8, 94.8), ('T01_conceptual', 48.0, 48.0),
         ('T02_slowdown_exaggerated', 68.5, 68.5), ('T03_illustrative', 62.0, 62.0), ('T04_orbit_illustrative', 91.0, 91.0), ('T05_g12_mirror', 37.4, 37.4)]
f = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf', 28)
def grab(v, t):
    png = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(t), '-i', v, '-frames:v', '1', '-vf', 'scale=540:960', '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True, check=True).stdout
    return Image.open(io.BytesIO(png)).convert('RGB')
for sid, t2, t3 in SHOTS:
    a, b = grab(V2, t2), grab(V3, t3); a.save(os.path.join(OUT, '%s_v2_%.1f.png' % (sid, t2))); b.save(os.path.join(OUT, '%s_v3_%.1f.png' % (sid, t3)))
    pair = Image.new('RGB', (1100, 1010), (20, 20, 20)); pair.paste(a, (0, 50)); pair.paste(b, (560, 50)); d = ImageDraw.Draw(pair)
    d.text((8, 8), 'V2  %.1f s' % t2, font=f, fill=(255, 200, 80)); d.text((568, 8), 'V3  %.1f s' % t3, font=f, fill=(120, 230, 140))
    pair.save(os.path.join(OUT, '%s_pair.jpg' % sid), quality=88)
print('wrote', len(SHOTS), 'pairs to', OUT)
