"""Appends coding for cells 25-60 to review_sample/REVIEWED_SAMPLE.csv (cells 1-24 already there) and prints tallies.
boundary_check: TRUE_CUT = composition/background replaced; FALSE_PROGRESSIVE = same scene, content added, removed, dimmed or text swapped;
BORDERLINE = same background but the main subject redrawn."""
import csv, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
O = R + '/review_sample'
T, F, B = 'TRUE_CUT', 'FALSE_PROGRESSIVE', 'BORDERLINE'
C = {
25: (T, 'figure at a board covered in huge numbers and red formulas, question card above', 'white, board', 'full-frame, figure left', 'many numerals and a power figure', 'SETUP_QUESTION', 'after: red series title card (channel own branding); before is the question scene'),
26: (T, 'cloud of dots around a ring diagram with element tiles', 'white, concentric circles', 'full-frame', 'element symbols (4 tiles)', 'EXPLAIN_MECH', 'before: grey diagram of a ball with labelled disintegrating figures and a time stamp'),
27: (T, 'moon over a curved surface with red laser beams', 'black, white and red line art', 'full-frame', '"2.10^24 W", "500 TW N.I.F. LASERS", "HARMED ATMOSPHERE"', 'QUANTITY', 'before: red series title card'),
28: (B, 'two figures splashing each other on a split white and black background', 'white left, black right', 'full-frame', 'none (citation box in the before frame)', 'EXPLAIN_SCENE', 'split background stays; figures redrawn in new poses'),
29: (T, 'open rulebook with a mushroom-cloud picture and baseball cards', 'white, desk items', 'full-frame', 'rulebook text (several lines)', 'CONTEXT_PROP', 'before: grey city map with a dense dark blast mass'),
30: (T, 'red end card with credits and four book covers', 'red background', 'full-frame', 'credit names, a URL, book titles', 'END_CARD_PROMO', 'before: presenter at a board with a physics-versus-math table; a visual book promo, see README'),
31: (T, 'black space with a bright core and beams towards a spiral galaxy', 'black, white line art', 'full-frame wide', 'none', 'CONTEXT_COSMIC', 'before: white scene with a dialog box error message joke'),
32: (T, 'two-panel jump diagram with 1 m and 2-3 m arcs and a stick figure', 'white, vertical divider', 'full-frame split', '"1 m", "2-3m"', 'COMPARISON_QUANTITY', 'before: board with a formula and Earth and Moon gravity values'),
33: (T, 'three newspapers with front-page headlines', 'white', 'full-frame', 'headlines and the paper name', 'CONTEXT_PROP', 'before: snowfall line chart for two cities'),
34: (F, 'presenter at a blank board then a globe with shading on the board', 'white, question card above', 'full-frame', 'question card text', 'EXPLAIN_BUILDUP', 'same presenter, card and board; the drawing is added'),
35: (F, 'figures and a ball inside concentric circles, background darkening', 'white then grey', 'full-frame', '"DEVELOPING FIREBALL", "T = 30 NANOSECONDS", role labels', 'EXPLAIN_MECH', 'same positions; a large grey glow is added, strength still 0.919'),
36: (T, 'figure sitting on a chair, hand to head', 'white', 'full-frame', 'none', 'GAG_REACTION', 'before: figure beside a joke safety sign'),
37: (T, 'red end card with credits and four book covers', 'red background', 'full-frame', 'credit names, a URL, book titles', 'END_CARD_PROMO', 'before: reader under a tree with a calorie comparison caption'),
38: (T, 'presenter at a board with a jump-height formula', 'white, board', 'full-frame', 'formula, Earth and Moon gravity values', 'EXPLAIN_EQUATION', 'before: a talk with a pros and cons board'),
39: (T, 'figure at a corkboard with pictures joined by red string, board then emptied', 'white', 'full-frame', '"WHAT PROCEEDS"', 'GAG_CONSPIRACY', 'before: three-panel normal versus paranormal physics with a wizard and speed figures'),
40: (T, 'ship silhouette on a flat line with a caption', 'white', 'full-frame, art low', '"NEEDED: 574 MEGAWATTS", "< 200 MW"', 'QUANTITY_SCALEREF', 'before: board with a worked calculation (car, slab)'),
41: (T, 'figure with a flamethrower and a snowman', 'white', 'full-frame', 'none', 'GAG_VISUAL', 'before: three ships with a caption (police joke)'),
42: (T, 'figure sitting under a tree, a small mound beside it', 'white, detailed tree', 'full-frame', 'none', 'CONTEXT_CALM', 'before: dark blurred mass on a hill'),
43: (T, 'tower with a sky lobby, then a catapult beside a tower', 'white', 'portrait, art in a band', 'speech balloons, "SKYLOBBY"', 'GAG_CONTEXT', 'before: elevator shaft with three figures'),
44: (T, 'house with a tree and a sleigh on the roof', 'white', 'portrait, art in a band', 'none', 'CONTEXT_SCENE', 'before: grey map with a red spiral and a pole label'),
45: (T, 'reader under a tree, runner beyond, small book', 'white, detailed tree', 'portrait', '"EQUIVALENT OF ~1/100,000 THE CALORIES OF RUNNING"', 'QUANTITY_COMPARISON', 'before: grey scene with floating tap labels and a typist'),
46: (F, 'figure at a desk with a monitor', 'white', 'portrait', 'question card and a dark thought bubble in the before frame', 'SETUP_QUESTION', 'card and bubble leave; figure and desk stay, strength 0.953'),
47: (T, 'a spinning arm in a ring, then a counterbalance arm diagram', 'white', 'portrait', '"SPEED LIMIT =", "COUNTERBALANCE"', 'EXPLAIN_MECH', 'before: board with a rocket and a figure by a bin'),
48: (T, 'blurred hillside with a large rock, dark region above', 'white, photographic blur', 'portrait', 'none', 'CONTEXT_BLUR', 'before: black ground with a cement truck and a house'),
49: (T, 'figure at a desk with a glowing laptop, grey room', 'grey', 'portrait', 'none', 'CONTEXT_SCENE', 'before: gamer figure with action counts and floating tap labels'),
50: (F, 'repeated pattern of tiny figures with a small formula label', 'white pattern', 'portrait', '"log2(8 BILLION) = 33 MONTHS" and "THIS IS FINE."', 'QUANTITY_EQUATION', 'same pattern before and after; only the overlay text swaps'),
51: (T, 'sequence of stick figures with brain icons and arrows', 'white', 'portrait, art centred', 'none', 'EXPLAIN_SEQUENCE', 'before: the repeated tile pattern with a formula label'),
52: (B, 'gradient scene with cloud top, small dots, text', 'black to grey gradient', 'portrait', '"TOO MANY NANOSECONDS" (before: "~5,800 K", "1 NANOSECOND")', 'QUANTITY_PUNCHLINE', 'same gradient and cloud; figure and labels replaced'),
53: (F, 'long table with a row of printers, then figures at the table', 'white', 'portrait, art in a band', 'price labels in the before frame', 'QUANTITY_SCALE', 'same table and printers; figures and stacks come and go'),
54: (T, 'red building drawing, then a bar chart with two building outlines', 'white', 'portrait', '"FLOORS 100", "GOAL: 1,000,000,000", "HOUSE", "SKYSCRAPER"', 'QUANTITY_COMPARISON', 'before: red hand-drawn tower with exclamations'),
55: (T, 'grey map with a red spiral and a pole label', 'grey map', 'portrait', '"NORTH POLE"', 'MAP', 'before: black ground with a dotted flight path'),
56: (T, 'skyline chart then a figure with a hard hat and a list', 'white, axis', 'portrait', '"HIGH BUILDING PROBLEMS" list (6 lines)', 'GAG_LIST', 'before: skyline chart with falling debris and red arrows'),
57: (F, 'the gamer scene dimmed with a glowing screen', 'dark grey', 'portrait', '"400+ ACTIONS PER MINUTE"', 'EXPLAIN_DIM', 'same figure and text before and after; only brightness changes, strength 0.861'),
58: (T, 'figure at a desk, "I FOUND ANOTHER MISTAKE!"', 'white', 'portrait', '"150,000 / DAY"', 'QUANTITY_GAG', 'before: row of printers over a table with a figure holding a note'),
59: (T, 'figure at a desk with a monitor; question card above', 'white', 'portrait', 'question card text', 'SETUP_QUESTION', 'new question card replaces the previous card; before: a different question with a thought bubble'),
60: (T, 'house outline on a chart axis', 'white', 'portrait', 'axis tick labels', 'QUANTITY_SCALEREF', 'before: red-arrow collapse pile drawing'),
}
old = list(csv.DictReader(open(O + '/REVIEWED_SAMPLE.csv')))
old = [r for r in old if int(r['n']) <= 24]
new = []
for r in csv.DictReader(open(O + '/SAMPLE2.csv')):
    c = C[int(r['n'])]
    new.append(dict(r, boundary_check=c[0], subject=c[1], setting=c[2], framing=c[3], camera_motion='NOT_ASSESSED_STILLS',
                    graphics_text=c[4], narrative_function=c[5], note=c[6], interpretation_status='VIEWED_SELF_REVIEW_3_STILLS'))
rows = old + new
w = csv.DictWriter(open(O + '/REVIEWED_SAMPLE.csv', 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
def cnt(rs): return {k: sum(r['boundary_check'] == k for r in rs) for k in (T, F, B)}
print('all', len(rows), cnt(rows))
for f in ('LONG', 'SHORT'): print(f, cnt([r for r in rows if r['fmt'] == f]))
lo = [r for r in rows if float(r['boundary_strength']) < 0.3]; hi = [r for r in rows if float(r['boundary_strength']) >= 0.3]
print('strength<0.3', len(lo), cnt(lo)); print('strength>=0.3', len(hi), cnt(hi))
print('videos', len({r['video_id'] for r in rows}))
print('false/borderline strengths', sorted(float(r['boundary_strength']) for r in rows if r['boundary_check'] != T))
