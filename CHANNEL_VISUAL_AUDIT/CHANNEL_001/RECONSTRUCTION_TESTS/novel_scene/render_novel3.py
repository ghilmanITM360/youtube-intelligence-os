"""CH001 novel NS5: family B panel-fill (original art/topic, no source pixels). Targets from 33NV/zLv/xdF8 T3:
full-width flat colour panel (green #309050 / orange #F09010) in band y~750-1160, black ink 11-44%, in-art dialogue text, NO bottom caption, ~1.8 s/state."""
import importlib.util, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('rn', os.path.join(HERE, 'render_novel.py')); N = importlib.util.module_from_spec(sp); sp.loader.exec_module(N)
stick, hand, qmark, burger, BLK, RED = (getattr(N, k) for k in 'stick hand qmark burger BLK RED'.split())
GRN, ORG, WHT = (48, 144, 80), (240, 144, 16), (253, 253, 253)
def panel(c, col, y0=750, y1=1160, x0=0, x1=1080, k=0.45):
    # T3 re-read: ref green/orange regions are ~2-4% of frame (ink_frac 0.017-0.047), not full-width panels -> shrink about centre
    cx, cy, hw, hh = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) * k / 2, (y1 - y0) * k / 2
    c.rect(cx - hw, cy - hh, cx + hw, cy + hh, fill=col, outline=None, w=0)
def dark(c, x0=120, x1=960, y0=720, y1=1200):
    cx, cy, hw, hh = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) * .25, (y1 - y0) * .25
    c.rect(cx - hw, cy - hh, cx + hw, cy + hh, fill=(24, 24, 24), outline=BLK, w=10, r=24)
def say(c, x, y, txt, sz=64): c.text(x, y, txt, hand(int(sz * 0.6)))  # ref dark-ink share 0.21-0.37
def ns5(c, f):
    s = f // 52
    if s == 0: say(c, 540, 900, 'Retire at 30?', 90)
    elif s == 1: panel(c, GRN); stick(c, 330, 880, 'neutral', 'shrug'); say(c, 740, 900, 'easy, right?')
    elif s == 2: panel(c, GRN, 800, 1100, 120, 960); stick(c, 330, 880, 'neutral', 'shrug', sweat=True); say(c, 740, 900, 'wait...')
    elif s == 3: panel(c, GRN); say(c, 540, 900, 'LET\'S GOOO!', 100)
    elif s == 4: panel(c, ORG); stick(c, 300, 900, 'neutral', 'point'); say(c, 720, 880, 'my plan:')
    elif s == 5: dark(c); burger(c, 540, 930, 2.4)
    elif s == 6: panel(c, ORG); say(c, 540, 900, 'save 70%', 110)
    elif s == 7: dark(c, 200, 880, 760, 1160); c.text(540, 960, 'Reality check', hand(84), WHT)
    elif s == 8: panel(c, GRN); say(c, 540, 860, 'rent + food', 80); say(c, 540, 990, '= 90%', 100)
    elif s == 9: panel(c, GRN, 720, 1200, 0, 700); stick(c, 700, 900, 'neutral', 'shrug', sweat=True); say(c, 300, 900, 'oh no...')
    elif s == 10: dark(c, 0, 1080, 700, 1220); qmark(c, 540, 900, 150)
    elif s == 11: panel(c, ORG, 700, 900); say(c, 540, 900, 'start small', 100)
    elif s == 12: stick(c, 540, 900, 'happy', 'point'); say(c, 540, 760, 'consistency wins', 70)
    else: panel(c, GRN); say(c, 540, 900, 'your move', 110)
if __name__ == '__main__':
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    N.render('NS5_retire_early_panelfill', ns5, [], 728, out)
