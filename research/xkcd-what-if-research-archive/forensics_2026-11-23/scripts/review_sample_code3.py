"""Appends coding for cells 61-108 (review batch 3, 48 shots) to review_sample/REVIEWED_SAMPLE.csv (cells 1-60 already there) and prints tallies.
Same rules as review_sample_code2.py. Viewer: main session, three stills per cell (0.25 s before start, keyframe, 0.25 s after start), no playback.
PAN= camera move inferred from stills (zoomed or motion-blurred map views of the same background)."""
import csv, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); O = R + '/review_sample'
T, F, B = 'TRUE_CUT', 'FALSE_PROGRESSIVE', 'BORDERLINE'; PAN = 'PAN_OR_ZOOM_INFERRED_FROM_STILLS'
C = {
61: (T, 'car chasing a yellow sun over a Scandinavia map, "~95 min"', 'white, grey map', 'full-frame', '"~95 min"', 'QUANTITY_COMPARISON', 'before: figure at a laptop beside an Arctic Circle map'),
62: (T, 'Earth ringed with tiny people and a nutrition-facts label', 'white', 'full-frame', '"EARTH", "500,000,000,000"', 'QUANTITY_SCALE', 'before: red series title card; after: the label is gone, same Earth'),
63: (T, 'house at night with lightning at the chimney, "BZZZ..."', 'dark grey', 'full-frame', '"BZZZ...", "WHIRR"', 'EXPLAIN_CONSEQUENCE', 'before: figure with a lightning rod and thought bubble'),
64: (T, 'tiny moon beside a huge starfield sphere, equal sign, energy labels', 'white', 'full-frame', '"93 BILLION LIGHTYEARS", "3,475 km", E labels', 'QUANTITY_COMPARISON', 'before: two gravity wells on a grid'),
65: (T, 'whale-shaped splash with white rays above a black ground, red line', 'grey, black ground', 'full-frame', 'none', 'EXPLAIN_SCENE', 'before: basketball court with a red 20 m circle'),
66: (F, 'three glasses labelled VACUUM / WATER', 'white, hand line', 'full-frame', '"VACUUM", "WATER"', 'EXPLAIN_BUILDUP', 'same table line; the single glass is joined by two more'),
67: (T, '"NOT A SUNSET": two figures watching a red and yellow sky', 'red and yellow gradient', 'full-frame', '"NOT A SUNSET", "NOT TOUCHING THE HORIZON (YET)"', 'GAG_VISUAL', 'before: sun path diagram with check and crosses'),
68: (T, 'grey stormscape, "CATATUMBO LIGHTNING"', 'grey photographic style', 'full-frame', '"CATATUMBO LIGHTNING"', 'CONTEXT_PLACE', 'before: figure and a map with a red circle on Lake Maracaibo'),
69: (F, 'silhouette town with a charged lightning column, flames spreading', 'black, white glow', 'full-frame', '+ and - signs on the column', 'EXPLAIN_MECH', 'same column and silhouette; glow and flames added, strength 0.475'),
70: (T, 'sun and lightning side by side, "1,000,000 : 1"', 'grey split', 'full-frame split', '"1,000,000 : 1"', 'QUANTITY_COMPARISON', 'before: world map with two red circles'),
71: (B, 'figure at a PROS / CONS board with two pictures', 'white, board', 'full-frame', '"PROS", "CONS"', 'GAG_BOARD', 'same figure and board; board contents replaced (before: worked calculation); after: board emptied'),
72: (T, 'newspaper, phone and TV clips ("UHM, ACTUALLY...")', 'white', 'full-frame', 'headline "3.5 EARTHQUAKE STRIKES FEAR IN OHIO CORN FIELD"', 'GAG_CONTEXT', 'before: RICHTER SCALE struck out for "MOMENT MAGNITUDE" scale beside a seismograph'),
73: (T, 'figure with a huge pile of pennies, "I\'LL NEED A BIGGER PIGGY BANK..."', 'white', 'full-frame', '"200 BILLION PENNIES"', 'QUANTITY_GAG', 'before: "ALL THE MONEY" coin hill beside landmarks'),
74: (T, 'red end card with credits and four book covers', 'red', 'full-frame', 'credits, "GET THE BOOKS: xkcd.com/books"', 'END_CARD_PROMO', 'before: dark planet with "PROBLEMS BIGGER THAN YOU CAN POSSIBLY IMAGINE"; no ASR in this shot'),
75: (T, 'frozen Miami sign and palm, dark sun in a starry sky', 'dark grey', 'full-frame', '"MIAMI"', 'GAG_VISUAL', 'before: dark space, star with field lines, "2025"'),
76: (T, 'figure on a thick stack of pages, "ROB MATTHEWS"', 'white', 'full-frame', '"5000+ PAGES", "400+ ARTICLES"', 'QUANTITY_SCALE', 'before: printers on a table, "WIKIPRINTIA"'),
77: (F, 'figure and baby under an umbrella with a grey shadow', 'white', 'full-frame', 'none', 'EXPLAIN_BUILDUP', 'same sun and figure; umbrella and shadow added'),
78: (T, 'figure at a desk, "I FOUND ANOTHER MISTAKE!"', 'white', 'full-frame', '"I FOUND ANOTHER MISTAKE!"', 'GAG_REACTION', 'before: library signs with shelves; bubble leaves in the after frame'),
79: (T, 'figure typing under a cloud of "TAP" words, squirrel on the desk', 'white', 'full-frame', '"TAP" x many', 'EXPLAIN_SCENE', 'before: "1.5 MILLIJOULES", droplet and squirrel'),
80: (F, 'house scene with "470 m/s (1040 mph)" and a running figure', 'white, grey ground', 'full-frame', '"470 m/s (1040 mph)"', 'QUANTITY_SCALEREF', 'same house and ground band; the scene scrolls and a sub-label is added (PAN)'),
81: (F, 'split screen BEFORE ANDREW / AFTER ANDREW with a Moon and chained ball', 'white, vertical divider', 'full-frame', '"BEFORE ANDREW", "AFTER ANDREW"', 'COMPARISON', 'before: only the BEFORE panel; right panel added'),
82: (F, 'printers feeding stacks of pages, "ARCHIVE"', 'white', 'full-frame', '"ARCHIVE"', 'EXPLAIN_BUILDUP', 'same page stacks; printers added on top'),
83: (T, 'figure in a window with a red cross, then a sun-and-moon diagram', 'white', 'full-frame', 'none', 'GAG_VISUAL', 'before: "NOT A SUNSET" scene'),
84: (T, 'blazing explosion over a figure and board', 'grey', 'full-frame', 'question card faintly visible', 'EXPLAIN_CONSEQUENCE', 'before: figure at a board with the Earth and Moon fields; question card above'),
85: (T, 'grey world map with wind bands, "470 m/s"', 'white, grey map', 'portrait', '"470 m/s"', 'QUANTITY_MAP', 'before: pink-red hurricane scene with swim text'),
86: (T, 'row of dinosaurs and palms on hills', 'white', 'portrait, art in a band', 'none', 'GAG_CONTEXT', 'before: board with two globes and the question card'),
87: (T, 'tombstone "R.I.P. HUMANITY 200,000 BCE - 2025"', 'white', 'portrait', 'tombstone text', 'GAG_PAYOFF', 'before: grid of stick people with red infection lines'),
88: (T, 'ship, "1 GRAM" mound and a drip, "NEEDED: 574 MEGAWATTS"', 'white', 'portrait, art low', '"NEEDED: 574 MEGAWATTS", "1 GRAM"', 'QUANTITY_SCALEREF', 'before: four-panel storyboard with a flamethrower'),
89: (T, 'phone ad "NEW: TELEPORTATION FUNCTION!"', 'white', 'portrait', 'ad text and small print', 'GAG_VISUAL', 'before: black gradient with a figure and an IEEE standard note'),
90: (T, 'sun with three satellites and a dish, "IMPROVED SATELLITE SERVICE"', 'white', 'portrait', '"IMPROVED SATELLITE SERVICE"', 'GAG_LIST', 'before: dark observatory with a black sun'),
91: (T, 'black gradient with a figure and an IEEE standard note, "DON\'T DO THIS"', 'black gradient', 'portrait', 'IEEE standard text, small figures', 'QUANTITY_GAG', 'before: snow scene with "30 cm / nanosecond"'),
92: (T, 'coloured map zoomed on Greenland and Antarctica, circle insets', 'colour map', 'portrait', 'caption about ice sheets', 'EXPLAIN_MAP', f'{PAN}: after frame is a blurred zoom of the same map; before shows an inset-circle version'),
93: (T, 'figure with a flamethrower aimed at a snowman', 'white, sun', 'portrait', 'none', 'GAG_VISUAL', 'before: figure at a board with a car and flamethrower'),
94: (T, 'panel of a figure with a microwave on a cliff, then a glass of water with waves', 'white', 'portrait', 'none', 'EXPLAIN_MECH', 'before: snowman scene, "!" added; strength 0.088 is low but the scene changes'),
95: (T, 'black skyline silhouette with debris lines', 'black and white', 'portrait', 'none', 'EXPLAIN_SCENE', 'before: oval grey map "470 m/s"'),
96: (T, 'small plane, "A-A-CHOO!", then "SAFER PILOTS"', 'white, sun', 'portrait', '"A-A-CHOO!", "SAFER PILOTS"', 'GAG_LIST', 'before: dark scene with two figures, one sneezing'),
97: (F, 'coloured world map with a pyramid inset', 'colour map', 'portrait', 'none', 'EXPLAIN_MAP', f'{PAN}: before is the same map seen smaller'),
98: (F, 'coloured map with a hurricane symbol and insets', 'colour map', 'portrait', 'none', 'EXPLAIN_MAP', f'{PAN}: same map, insets added'),
99: (T, 'figure holding a baby under a sun, then "SAFER CHILDREN"', 'white', 'portrait', '"SAFER CHILDREN"', 'GAG_LIST', 'before: grey office with a figure at a desk'),
100: (F, 'coloured map with a Taj Mahal inset and a pink region', 'colour map', 'portrait', 'none', 'EXPLAIN_MAP', f'{PAN}: after frame is a blurred zoom'),
101: (F, 'map zooming between North America views with a hurricane symbol', 'colour map', 'portrait', 'none', 'EXPLAIN_MAP', f'{PAN}: three stills of one map at different zoom'),
102: (F, 'device with a red laser on a grey background, "WATER DROPLET"', 'grey', 'portrait', '"WATER DROPLET", "ARE YOU SURE?"', 'EXPLAIN_DIM', 'same device and figure on white before; whole frame dims and a laser is added, strength 0.997'),
103: (F, 'map re-centred from Australia to Antarctica then a blurred pan', 'colour map', 'portrait', '"AUSTRALIA", "ANTARCTICA"', 'EXPLAIN_MAP', f'{PAN}: motion blur visible'),
104: (F, 'map of Europe with Iceland and insets', 'colour map', 'portrait', '"ICELAND"', 'EXPLAIN_MAP', f'{PAN}: same background, insets and zoom change'),
105: (T, 'grid of stick people with red infection lines', 'white', 'portrait', 'none', 'EXPLAIN_MECH', 'before: freezer scene "IT\'LL BE FIIINE"'),
106: (F, 'coloured map with insets, then shifted', 'colour map', 'portrait', 'none', 'EXPLAIN_MAP', f'{PAN}: same map across the three stills'),
107: (T, 'grey scene with a red beam on a figure, "9.17 kW/m2"', 'grey', 'portrait', '"9.17 kW/m2", "1.36 kW/m2"', 'QUANTITY_COMPARISON', 'before: WolframAlpha result card'),
108: (T, 'black skyline silhouette with debris', 'black and white', 'portrait', 'small sign', 'EXPLAIN_SCENE', 'before: oval map "470 m/s"'),
}
old = [r for r in csv.DictReader(open(O + '/REVIEWED_SAMPLE.csv')) if int(r['n']) <= 60]
new = []
for r in csv.DictReader(open(O + '/SAMPLE3.csv')):
    c = C[int(r['n'])]; cm = PAN if PAN in c[6] else 'NOT_ASSESSED_STILLS'
    new.append(dict(r, boundary_check=c[0], subject=c[1], setting=c[2], framing=c[3], camera_motion=cm, graphics_text=c[4], narrative_function=c[5], note=c[6], interpretation_status='VIEWED_SELF_REVIEW_3_STILLS'))
rows = old + new
w = csv.DictWriter(open(O + '/REVIEWED_SAMPLE.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
def cnt(rs): return {k: sum(r['boundary_check'] == k for r in rs) for k in (T, F, B)}
print('all', len(rows), cnt(rows), 'batch3', cnt(new)); print('videos', len({r['video_id'] for r in rows}))
for f in ('LONG', 'SHORT'): print(f, cnt([r for r in rows if r['fmt'] == f]), 'batch3', cnt([r for r in new if r['fmt'] == f]))
for lab, fn in (('<0.3', lambda s: s < .3), ('>=0.3', lambda s: s >= .3)): print(lab, cnt([r for r in rows if fn(float(r['boundary_strength']))]), len([r for r in rows if fn(float(r['boundary_strength']))]))
print('b3 false strengths', sorted(float(r['boundary_strength']) for r in new if r['boundary_check'] != T))
print('pan flagged', sum(r['camera_motion'] != 'NOT_ASSESSED_STILLS' for r in new), sorted({r['video_id'] for r in new if r['camera_motion'] != 'NOT_ASSESSED_STILLS'}))
