"""V1 Rent R8 tail (122.3-286.06 s on the EDITED Take 2 master): BLS vacancy/age, Zillow, level vs change, "what we checked", close.
  python3 tools/v1r8_tail.py --still 125,131 | --storyboard | --seg 3 --out out_r8/x.mp4   (seg 3 122.3-147.6, 4 147.6-199.5, 5 199.5-257.0, 6 257.0-286.06)
Audio: audio/take2_edited/v1_rent_take2_edited_cut124-254.8.wav (sha gated). Timeline = new (post-cut) times from t2e_words.json.
Claims: SEGMENT_122_286_CLAIM_REGISTER.md. Graphics are character-free for vacancy/age. Same grammar/engine as R4/R5/R7 (v1r4_render)."""
import os, sys, math, hashlib, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import v1r4_render as r
from v1r4_render import *
from v1r5_seg2 import mini_house, paper, chip
r.BEATS = []
EWAV = HERE + '/audio/take2_edited/v1_rent_take2_edited_cut124-254.8.wav'
EWAV_SHA = '9709ad340795a5b285657e31936121dc2e663e4e43f03b692fb634102dfa857c'
END = 286.06
SEGS = {3: (122.3, 147.6), 4: (147.6, 199.5), 5: (199.5, 257.0), 6: (257.0, END)}
BL = (70, 140, 190)
BSRC = ["Source: BLS factsheet:", "Owners' equivalent rent and rent"]
BCPI = ['Source: BLS, CPI release Oct 14, 2026, Table 1']
ZSEP = ['Source: Zillow Group release Oct 6, 2026 (typical U.S. rent)']
ZOCT = ['Source: Zillow Research, ZORI (smoothed, U.S.), data through Oct 2026']

def build():
    PRE = -1.0
    # ---- seg 3: BLS vacancy + age adjustment (character-free graphics) ----
    b = B(122.3, 124.32, 'Host smile; "Two more details"', 'Two more details.')
    b.add(host([(122.3, 'shrug', 'smile')], 470, 1010, 0.46), txt('Two more', 1330, 380, 150, INK, 122.7, 'wide'), txt('details', 1330, 560, 170, RED, 123.0, 'wide'), *source(BSRC, 122.7, False))
    b = B(124.32, 127.3, 'A house with no tenant: dashed "vacant" when the BLS checks', 'If a unit is vacant when the BLS checks it,')
    b.add(mini_house(780, 470, 400, PAPER, 124.4, 31), *chip(780, 770, 380, 110, 'vacant', GREYF, 124.8, 74, INK, 32), txt('when the BLS checks it', 1470, 420, 90, INK, 125.6, 'wide'),  *source(BSRC, 124.6))
    b = B(127.3, 131.2, 'Arrow from vacant house to three newly rented houses: estimated from them', 'the BLS estimates its change using units that were newly rented,')
    b.add(mini_house(450, 470, 300, PAPER, 127.3, 31, mode='static'), *chip(450, 720, 300, 100, 'vacant', GREYF, 127.3, 66, INK, 32, mode='static'),
          arrow(680, 470, 960, 470, 128.2), *[mini_house(1180 + i * 260, 470, 220, BL, 129.4 + i * 0.25, 40 + i) for i in range(3)],
          txt('newly rented', 1440, 700, 110, BL, 129.9, 'wide'), txt('its change is estimated from these', 1300, 830, 70, GREYT, 128.6), *source(BSRC, 127.6))
    b = B(131.2, 135.2, 'Each new price + "age adjustment" chip; "age of the unit"', 'and each new price carries an adjustment for the age of the unit.')
    b.add(*chip(620, 470, 300, 120, 'new price', ORANGE, 131.4, 72, INK, 41), txt('+', 880, 480, 120, INK, 132.3, 'wide'), *chip(1240, 470, 480, 120, 'age adjustment', BL, 132.5, 72, INK, 42),
          txt('for the age of the unit', 1240, 690, 100, RED, 133.6, 'wide'), *source(BSRC, 131.6))
    b = B(135.2, 137.0, 'Host point; "Notice what this means"', 'Notice what this means.')
    b.add(host([(135.2, 'point', 'neutral')], 470, 1010, 0.46), txt('Notice what', 1330, 380, 130, INK, 135.7, 'wide'), txt('this means', 1330, 540, 150, RED, 136.0, 'wide'))
    fx = [(780 + c * 300, 430 + rr * 250) for rr in range(2) for c in range(3)]
    b = B(137.0, 141.9, 'Six blue houses, same ones: "a fixed set of homes"', 'The BLS number is a measure of price change for a fixed set of homes,')
    b.add(*[mini_house(x, y, 220, BL, 137.4 + 0.08 * i, 50 + i) for i, (x, y) in enumerate(fx)], txt('price change', 1500, 200, 100, RED, 139.2, 'wide'), txt('for a fixed set of homes', 1380, 860, 100, INK, 140.3, 'wide'), *source(BSRC, 137.6))
    b = B(141.9, 144.0, 'Same houses; Jan -> Jul "six-month steps"', 'observed at six-month steps.')
    b.add(*[mini_house(x, y - 40, 180, BL, PRE, 50 + i, mode='static') for i, (x, y) in enumerate(fx[:3])], *chip(660, 760, 240, 110, 'Jan', ORANGE, 142.1, 68, INK, 51), arrow(800, 760, 1100, 760, 142.5), *chip(1240, 760, 240, 110, 'Jul', ORANGE, 142.9, 68, INK, 52), txt('six-month steps', 960, 640, 100, RED, 142.6, 'wide'), *source(BSRC, PRE))
    b = B(144.0, 147.6, 'Struck-through "average price on the market this week"', 'It is not the average price of a home on the market this week.')
    b.add(txt('average price of a home', 960, 400, 120, INK, 144.2, 'wide'), txt('on the market this week', 960, 560, 110, GREYT, 145.4, 'wide'), stroke_item([(380, 480), (1540, 470)], 146.3, RED, 14, 0.3, 5, 71, 3), txt('not this', 960, 760, 130, RED, 146.6, 'wide'), *source(BSRC, 144.4))

    # ---- seg 4: Zillow + level vs change ----
    b = B(147.6, 150.1, 'Host point; "Zillow\'s index"', "Now take Zillow's index.")
    b.add(host([(147.6, 'point', 'neutral')], 470, 1010, 0.46), txt("Now Zillow's", 1330, 380, 130, INK, 148.0, 'wide'), txt('index', 1330, 560, 170, BL, 148.8, 'wide'))
    b = B(150.1, 157.3, '"$1,913" big, labelled Zillow smoothed U.S. rent index, Oct 2026', "In October 2026, Zillow's smoothed U.S. rent index stood at $1,913.")
    b.add(txt('Oct 2026', 960, 230, 100, GREYT, 150.4, 'wide'), txt("Zillow's smoothed U.S. rent index", 960, 360, 90, INK, 151.8), txt('$1,913', 960, 640, 300, RED, 155.3, 'num'), *source(ZOCT, 150.6))
    b = B(157.3, 161.5, '"$1,859" with "Oct 2025" and "ZORI data file" label', 'A year earlier, it was $1,859.')
    b.add(txt('Oct 2025', 960, 230, 100, GREYT, 157.7, 'wide'), txt('a year earlier', 960, 360, 90, INK, 158.0), txt('$1,859', 960, 640, 300, ORANGE, 159.2, 'num'), txt('from the Zillow data file (ZORI)', 960, 840, 62, GREYT, 159.8), *source(ZOCT, 157.9))
    b = B(161.5, 164.3, '"+2.9%" big, $1,913 vs $1,859', 'That is a rise of 2.9%.')
    b.add(txt('$1,859  →  $1,913', 960, 320, 120, INK, 161.8, 'num'), txt('+2.9%', 960, 640, 330, RED, 162.7, 'num'), txt('Oct 2026 vs Oct 2025', 960, 860, 70, GREYT, 163.2), *source(ZOCT, 162.0))
    b = B(164.3, 167.0, '"+2.7%" Sep with source', 'In September, it was 2.7%.')
    b.add(txt('September 2026', 960, 280, 110, INK, 164.5, 'wide'), txt('+2.7%', 960, 620, 330, BL, 166.0, 'num'), txt('same measure, month earlier', 960, 850, 70, GREYT, 166.3), *source(ZSEP, 164.6))
    b = B(167.0, 169.7, 'Host smirk; "The takeaway"', 'Here is the thing to take away.')
    b.add(host([(167.0, 'point', 'smirk')], 470, 1010, 0.46), txt('The', 1330, 380, 110, INK, 167.2), txt('takeaway', 1330, 540, 170, RED, 167.6, 'wide'))
    b = B(169.7, 174.8, 'Zillow: $1,913 = level (dollars), +2.9% = change in that level', "Zillow's figure is a level, a dollar amount, and a change in that level.")
    b.add(txt('Zillow', 960, 190, 110, BL, 169.9, 'wide'), *chip(640, 520, 520, 220, '$1,913', GREYF, 171.4, 130, INK, 61, kind='num'), txt('a level (dollars)', 640, 700, 80, INK, 171.8), *chip(1280, 520, 520, 220, '+2.9%', ORANGE, 172.8, 130, INK, 62, kind='num'), txt('a change in that level', 1280, 700, 80, RED, 173.4), *source(ZOCT, 170.2))
    b = B(174.8, 177.4, 'BLS: "+2.8%" = change only', 'The BLS figure is a change only.')
    b.add(txt('BLS', 960, 190, 110, INK, 174.9, 'wide'), *chip(960, 520, 520, 220, '+2.8%', ORANGE, 175.7, 130, INK, 63, kind='num'), txt('a change only', 960, 720, 110, RED, 176.3, 'wide'), txt('12 months to September 2026', 960, 810, 56, GREYT, 175.9), *source(BCPI, 175.0))
    b = B(177.4, 180.6, 'Host shrug; "typical rent = ?"', 'The CPI does not say what the typical rent is.')
    b.add(host([(177.4, 'shrug', 'smirk')], 470, 1010, 0.46), txt('CPI: typical rent', 1330, 380, 100, INK, 177.9, 'wide'), txt('?', 1330, 600, 330, RED, 179.7, 'wide'))
    b = B(180.6, 183.9, 'Group of six houses + "how fast" arrow', 'It says how fast prices moved for a group of homes.')
    b.add(*[mini_house(x, y, 200, BL, 180.8 + 0.08 * i, 50 + i) for i, (x, y) in enumerate(fx)], arrow(1640, 700, 1820, 470, 181.3, RED, 14), txt('how fast', 1720, 800, 110, RED, 181.6, 'wide'), txt('for a group of homes', 1100, 880, 90, INK, 182.5), *source(BSRC, 181.0))
    b = B(183.9, 189.2, '"rent is high" != "rent is rising fast"', 'That is why rent is high and rent is rising fast are two different claims.')
    b.add(*chip(620, 500, 560, 200, 'rent is high', GREYF, 184.5, 80, INK, 64, kind='wide'), txt('≠', 960, 500, 220, RED, 187.7, 'wide'), *chip(1330, 500, 640, 200, 'rent is rising fast', ORANGE, 186.2, 80, INK, 65, kind='wide'), txt('two different claims', 960, 800, 120, INK, 188.4, 'wide'))
    b = B(189.2, 193.9, 'Host worried; "$ level" high even if change is 2.8%', 'A dollar amount can be uncomfortable even when its yearly change is 2.8%.')
    b.add(host([(189.2, 'shrug', 'worried')], 470, 1010, 0.46), txt('a dollar amount', 1330, 330, 100, INK, 189.8, 'wide'), txt('can be uncomfortable', 1330, 470, 100, RED, 190.6, 'wide'), txt('even when the yearly change is 2.8%', 1330, 620, 70, GREYT, 192.1))
    b = B(193.9, 199.5, 'Stacked bar: rent "already stretched" + small +2.8% slice (illustrative)', 'A 2.8% rise on a rent that is already stretched is still a bigger monthly bill.')
    b.add(rect(820, 330, 420, 480, GREYF, 194.0, 8, 91), txt('rent', 1030, 560, 110, INK, 195.2, 'wide'), rect(820, 290, 420, 40, ORANGE, 197.7, 8, 92), txt('+2.8%', 1560, 305, 90, RED, 197.7, 'num'), txt('still a bigger monthly bill', 1210, 900, 100, INK, 198.2, 'wide'), txt('illustration, not to scale', 1500, 975, 50, GREYT, 194.4))

    # ---- seg 5: what we checked ----
    b = B(199.5, 205.8, 'Host smirk then "stuck behind the market?" -> red "we did not find it"', 'We went looking for a clean story ... We did not find it.')
    b.add(host([(199.5, 'shrug', 'smirk'), (204.6, 'shrug', 'worried')], 470, 1010, 0.46), txt('the clean story:', 1330, 330, 90, GREYT, 200.1), txt('official number\nstuck behind the market', 1330, 520, 90, INK, 201.7), txt('not found', 1330, 800, 190, RED, 205.0, 'wide', rot=-4))
    b = B(205.8, 210.4, 'Chip "BLS collection cycle: six months"', 'First, the BLS explanation tells you the collection cycle, six months.')
    b.add(txt('First', 700, 190, 110, GREYT, 206.7, 'wide'), txt('the BLS collection cycle', 960, 360, 100, INK, 207.2), *chip(960, 640, 560, 200, 'six months', ORANGE, 209.9, 110, INK, 66, kind='wide'), *source(BSRC, 207.3))
    b = B(210.4, 216.9, 'Document with line "CPI rent trails market rents" -> struck, "not found"', 'We looked for a BLS sentence that says the CPI rent trails market rents. We did not find one.')
    b.add(paper(720, 560, 520, 640, 'BLS', 210.6, INK, 100, seed=75), txt('"CPI rent trails\nmarket rents"', 1370, 440, 90, INK, 212.8), stroke_item([(1050, 360), (1700, 510)], 214.9, RED, 12, 0.3, 5, 72, 3), txt('no such sentence', 1450, 800, 120, RED, 215.8, 'wide'), *source(BSRC, 210.9))
    b = B(216.9, 225.9, 'Two bars: BLS 2.8% vs Zillow 2.7% (Sep, 12 months)', 'Second, on the numbers we could read, the two measures sit close together. 2.8% for BLS in September, 2.7% for Zillow.')
    b.add(axis(217.6), txt('Second: the two measures sit close', 960, 150, 80, GREYT, 217.7), bar(0, 2.8, ORANGE, 221.6), numtxt(0, 2.8, ORANGE, 221.8), txt('BLS', CX[0], BASE + 70, 90, INK, 222.4, 'wide'),
          bar(1, 2.7, BL, 223.6), numtxt(1, 2.7, BL, 223.8), txt('Zillow', CX[1], BASE + 70, 90, INK, 224.6, 'wide'), txt('12 months to September 2026', 960, 228, 52, GREYT, 221.7), *source(BCPI + ZSEP, 221.7, True))
    b = B(225.9, 232.9, 'October one-month: BLS rent +0.2%, Zillow almost flat', 'In October, the BLS rent index rose 0.2% for the month. Zillow\'s index was almost flat that month.')
    K = 400
    b.add(txt('October 2026, one month', 960, 150, 80, GREYT, 226.1), stroke_item([(800, BASE + 4), (1790, BASE + 4)], 226.1, INK, 9, 0.25, 4, 5, 2), rect(CX[0] - 120, BASE - int(0.2 * K), 240, int(0.2 * K), ORANGE, 228.0, 8, 93, mode='static'), txt('+0.2%', CX[0], BASE - 190, 120, ORANGE, 228.0, 'num'), txt('BLS rent', CX[0], BASE + 70, 90, INK, 226.8, 'wide'),
          rect(CX[1] - 120, BASE - 10, 240, 10, BL, 231.3, 6, 94, mode='static'), txt('almost flat', CX[1], BASE - 100, 90, BL, 231.3, 'wide'), txt('Zillow', CX[1], BASE + 70, 90, INK, 230.5, 'wide'), *source(['Source: BLS CPI release Nov 10, 2026;', 'Zillow Research October Rent Report'], 226.4, True))
    b = B(232.9, 243.5, 'BLS: 12-month rent change Oct 2026 = not published; empty dashed box vs Zillow +2.9%', "Third, the BLS did not print a 12-month rent change in its October release, so there was no October-to-October comparison from the BLS to put next to Zillow's 2.9%.")
    b.add(txt('Third', 700, 190, 110, GREYT, 233.2, 'wide'), txt('BLS 12-month rent change, Oct 2026', 960, 330, 80, INK, 234.3), rect(520, 440, 560, 300, PAPER, 236.4, 8, 95, dash=True), txt('not printed', 800, 590, 110, RED, 236.9, 'wide'),
          txt('vs', 1160, 590, 90, GREYT, 241.0), *chip(1420, 590, 420, 300, '+2.9%', ORANGE, 242.6, 130, INK, 67, kind='num'), txt('Zillow', 1420, 790, 80, INK, 242.8), txt('no October 2025 BLS data was collected', 960, 900, 62, GREYT, 237.8), *source(['Source: BLS CPI release Nov 10, 2026'], 236.6))
    b = B(243.5, 257.0, 'Summary: honest answer is narrower; moves in six-month steps; close in Sept; no dollar price', 'So, the honest answer is narrower than a headline. The official rent number moves in six-month steps. It matches the market measure today within a fraction of a point, and it cannot tell you the dollar price of renting.')
    b.add(txt('The honest answer is narrower', 960, 170, 100, RED, 243.8, 'wide'), *chip(960, 400, 1500, 130, 'moves in six-month steps', GREYF, 247.9, 80, INK, 68),
          *chip(960, 590, 1500, 130, 'close to the market measure (Sept: 2.8% vs 2.7%)', ORANGE, 251.0, 62, INK, 69), *chip(960, 780, 1500, 130, 'cannot tell you the dollar price of renting', GREYF, 254.4, 68, INK, 70), *source(BCPI + ZSEP, 251.4, True))

    # ---- seg 6: three questions + close ----
    b = B(257.0, 260.4, 'Host point; "three questions for any rent headline"', 'If you read a rent headline, ask three questions.')
    b.add(host([(257.0, 'point', 'neutral')], 470, 1010, 0.46), txt('A rent headline?', 1330, 330, 110, INK, 257.4, 'wide'), txt('ask three questions', 1330, 500, 120, RED, 258.7, 'wide'))
    b = B(260.4, 262.9, 'Q1 "Is it a level or a change?"', 'Is it a level or a change?')
    b.add(txt('1', 360, 400, 220, RED, 260.6, 'num'), txt('level', 800, 400, 160, INK, 260.9, 'wide'), txt('or', 1100, 400, 100, GREYT, 261.4, 'wide'), txt('change?', 1450, 400, 160, ORANGE, 261.5, 'wide'))
    b = B(262.9, 265.9, 'Q2 "same homes or new listings?"', 'Is it measured on the same homes or on new listings?')
    b.add(txt('2', 360, 400, 220, RED, 263.0, 'num'), *[mini_house(720 + i * 170, 380, 130, BL, 263.5 + 0.06 * i, 80 + i) for i in range(3)], txt('same homes', 890, 560, 80, INK, 263.9), txt('or', 1330, 400, 90, GREYT, 264.2, 'wide'), *chip(1560, 400, 340, 120, 'new listings', ORANGE, 264.6, 62, INK, 81))
    b = B(265.9, 268.7, 'Q3 "how often is each home priced?"', 'How often is each home priced?')
    b.add(txt('3', 360, 400, 220, RED, 266.0, 'num'), txt('how often', 960, 330, 130, INK, 266.3, 'wide'), txt('is each home priced?', 960, 500, 110, INK, 266.9, 'wide'), *chip(960, 760, 760, 130, 'every six months (BLS)', GREYF, 267.3, 62, INK, 82), *source(BSRC, 267.4))
    b = B(268.7, 274.8, 'Host; your own rent paper vs "change in an average"', 'If you are comparing your own rent with any of these numbers, a change in an average does not say what you will be asked to pay.')
    b.add(host([(268.7, 'down', 'neutral'), (272.4, 'shrug', 'smirk')], 470, 1010, 0.46), paper(1100, 520, 360, 460, 'YOUR RENT', 269.5, INK, 70, seed=76), txt('≠', 1480, 520, 200, RED, 272.7, 'wide'), txt('an average\nchange', 1700, 500, 80, INK, 271.5))
    b = B(274.8, 277.5, 'Big text "the market, not your lease"', 'It describes the market, not your lease.')
    b.add(txt('describes the market', 960, 380, 150, INK, 275.4, 'wide'), txt('not your lease', 960, 620, 190, RED, 276.3, 'wide'))
    b = B(277.5, END, 'Disclaimer + source-tag note; host smile', 'This is not financial advice. It describes how two published measures are built. Sources are in the description, and every number on screen carries its source tag.')
    b.add(host([(277.5, 'down', 'smile')], 470, 1010, 0.46), txt('Not financial advice', 1330, 330, 120, INK, 277.9, 'wide'), txt('how two published measures are built', 1330, 480, 66, GREYT, 279.6), txt('Sources in the description', 1330, 680, 90, RED, 282.3, 'wide'), txt('every number carries its source tag', 1330, 800, 62, GREYT, 283.5))
    return r.BEATS

def main():
    a = sys.argv; beats = build()
    if '--storyboard' in a:
        t = r.storyboard(beats).replace('V1 Rent R4 storyboard (long-form grammar re-block of the 0-75 s Take 2 narration)', 'V1 Rent R8 storyboard, tail (122.3-286.06 s on the edited Take 2 master)'); open(HERE + '/STORYBOARD_R8_122-286s.md', 'w').write(t + '\n'); print('ok'); return
    od = HERE + '/out_r8'; os.makedirs(od + '/stills', exist_ok=True)
    if '--still' in a:
        for ts in a[a.index('--still') + 1].split(','): render(beats, math.floor(float(ts) * CFPS + 1e-6) / CFPS).save('%s/stills/r8_%s.png' % (od, ts))
        return
    sg = int(a[a.index('--seg') + 1]); T0, T1 = SEGS[sg]
    out = a[a.index('--out') + 1] if '--out' in a else od + '/V1_RENT_R8_seg%d_%d-%ds.mp4' % (sg, T0, round(T1)); out = out if os.path.isabs(out) else HERE + '/' + out
    assert hashlib.sha256(open(EWAV, 'rb').read()).hexdigest() == EWAV_SHA, 'edited wav checksum mismatch'; n = round((T1 - T0) * FPS)
    cmd = ['/opt/homebrew/bin/ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1920x1080', '-r', str(FPS), '-i', '-', '-ss', '%.3f' % T0, '-t', '%.3f' % (n / FPS), '-i', EWAV,
           '-map', '0:v', '-map', '1:a', '-vf', 'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p', '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
           '-af', 'aresample=48000' + (',afade=t=out:st=%.3f:d=0.3' % max(0, n / FPS - 0.3) if sg == 6 else ''), '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE); last = None
    for f in range(n):
        tq = math.floor((T0 + f / FPS) * CFPS + 1e-6) / CFPS
        if tq != last: im = render(beats, tq).tobytes(); last = tq
        p.stdin.write(im)
    p.stdin.close(); p.wait(); print('rendered', n, 'frames ->', out)
if __name__ == '__main__': main()
