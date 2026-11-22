"""CH001 novel round 2: family-conditional tests (original art/topics, no source pixels).
NS3 family B 'uncaptioned slow' (target from 33NV/zLv: ~1.8 s/state, 0.4-0.8 cuts/10 s, no bottom caption, in-band labels, art y670-1150).
NS4 family A 'captioned busy' (target from 10nE/1eTw: ~0.7-0.9 s/state, bottom caption block).
Usage: render_novel2.py OUT_DIR"""
import importlib.util, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('rn', os.path.join(HERE, 'render_novel.py')); N = importlib.util.module_from_spec(sp); sp.loader.exec_module(N)
ease, stick, bag, qmark, hand, comic, BLK, RED, burger, words = (getattr(N, k) for k in 'ease stick bag qmark hand comic BLK RED burger words'.split())
GRN = (60, 140, 70); ORG = (240, 145, 15)
def piggy(c, x, y, s=1.0):
    c.ell(x, y, 110 * s, 80 * s, fill=(245, 170, 175), outline=BLK, w=7)
    c.ell(x + 105 * s, y + 5 * s, 34 * s, 28 * s, fill=(240, 150, 160), outline=BLK, w=6)
    c.rect(x - 30 * s, y - 85 * s, x + 30 * s, y - 70 * s, fill=BLK, outline=None, w=0)
    for dx in (-60, 50): c.rect(x + dx * s, y + 60 * s, x + (dx + 28) * s, y + 110 * s, fill=(245, 170, 175), outline=BLK, w=6)
# ---- NS3: 24 s = 720 frames, 13 states of ~1.8 s, no caption ----
def ns3(c, f):
    s = f // 42
    if s == 0: c.text(540, 760, 'Emergency fund?', hand(84)); 
    elif s == 1: stick(c, 300, 800, 'neutral', 'shrug'); c.text(760, 800, 'rent', hand(90))
    elif s == 2: stick(c, 780, 800, 'neutral', 'shrug'); c.text(300, 880, 'car', hand(90))
    elif s == 3: stick(c, 300, 800, 'neutral', 'shrug', sweat=True); c.text(760, 1000, 'vet', hand(90))
    elif s == 4: piggy(c, 540, 930, 2.6)
    elif s == 5: piggy(c, 540, 930, 2.6); c.text(540, 720, '$0', hand(90), RED)
    elif s == 6: piggy(c, 400, 930, 1.1); c.text(780, 930, '3 months', hand(70), GRN)
    elif s == 7: burger(c, 540, 930, 3.4)
    elif s == 8: burger(c, 540, 930, 3.4); c.text(540, 740, 'saved', hand(80), GRN)
    elif s == 9: stick(c, 800, 800, 'neutral', 'point'); c.text(300, 700, 'start small', hand(70))
    elif s == 10: c.text(340, 760, '$20', hand(160), GRN); c.text(700, 1000, 'a week', hand(70))
    elif s == 11: piggy(c, 540, 930, 1.5); c.text(540, 720, 'keep going', hand(70), ORG)
    else: stick(c, 540, 800, 'happy', 'point')
    # beats beyond s==12 repeat the last one
# ---- NS4: 18 s = 540 frames, ~0.7 s states, captioned ----
NS4_W = words("A flat tire. A vet bill. A broken phone. Emergencies are not rare, so plan for them.", 6, per=6)
def ns4(c, f):
    s = f // 28
    k = ease((f % 28) / 5)
    items = [lambda: c.text(540, 800, 'flat tire', hand(90)),
             lambda: (stick(c, 400, 800, 'neutral', 'shrug'), c.text(760, 800, '$400', hand(80), RED)),
             lambda: (piggy(c, 540, 930, 2.8 * k + .01)),
             lambda: c.text(540, 800, 'vet bill', hand(90)),
             lambda: (stick(c, 400, 800, 'neutral', 'shrug', sweat=True), c.text(760, 800, '$900', hand(80), RED)),
             lambda: burger(c, 540, 930, 3.4 * k + .01),
             lambda: c.text(540, 800, 'broken phone', hand(80)),
             lambda: (stick(c, 400, 800, 'neutral', 'shrug'), c.text(760, 800, '$600', hand(80), RED)),
             lambda: qmark(c, 540, 820, int(30 + 70 * k))]
    items[s % len(items)]()
if __name__ == '__main__':
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    N.W_ = None
    # NS3 without caption: pass empty word list
    N.render('NS3_emergency_fund_uncaptioned', ns3, [], 720, out)
    N.render('NS4_emergencies_captioned', ns4, NS4_W, 540, out)
