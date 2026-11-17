import csv, json, sys, random, statistics as S, collections
ws = sys.argv[1]; fps = 30; LASTF = 16206
st = list(csv.DictReader(open(f'{ws}/visual_states.csv'))); sh = list(csv.DictReader(open(f'{ws}/shot_ledger.csv')))
man = json.load(open(f'{ws}/source_manifest.json')); I = set(man['iframe_indices'])
fm = {int(r['frame']): int(float(r['fullres_changed_px_thr25'])) for r in csv.DictReader(open(f'{ws}/tables/frame_metrics.csv'))}
zm = list(csv.DictReader(open(f'{ws}/tables/zoom_measure.csv'))); ep = list(csv.DictReader(open(f'{ws}/tables/episodes.csv')))
pal = json.load(open(f'{ws}/tables/palette.json'))['colors']
pairs = json.load(open(f'{ws}/build/phrase_pairs.json'))
asr = json.load(open(f'{ws}/audio/RXFBHYxyqdk_small_en.json'))
W = [(x['start'], x['end'], x['word'].strip()) for s in asr['segments'] for x in s['words']]; WS_ = sorted(x[0] for x in W)
sid = lambda f: next(r['visual_state_id'] for r in st if int(r['start_frame']) <= f <= int(r['end_frame']))
lab = lambda r: r['label'].lower()
base = collections.Counter(r['entering_class'].split('+')[0] for r in st)
cuts = [int(r['start_frame']) for r in st if r['entering_class'].startswith('CUT')]; non = [c for c in cuts if c not in I]
L = [int(s['end_frame']) - int(s['start_frame']) + 1 for s in sh]; q = S.quantiles(L, n=4)
mn = min(sh, key=lambda s: int(s['end_frame']) - int(s['start_frame'])); mx = max(sh, key=lambda s: int(s['end_frame']) - int(s['start_frame']))
longs = [s for s in sh if int(s['end_frame']) - int(s['start_frame']) + 1 > 300]
longtxt = '; '.join(f"{s['shot_id']} f{s['start_frame']}-f{s['end_frame']} ({(int(s['end_frame'])-int(s['start_frame'])+1)/fps:.1f} s)" for s in longs)
shorts = [s for s in sh if int(s['end_frame']) - int(s['start_frame']) + 1 <= 30]
en = [int(r['frames']) for r in st]; sds = [x / fps for x in en]
n = [int(e['end_frame']) - int(e['start_frame']) + 1 for e in ep]
n1 = sum(x == 1 for x in n); n23 = sum(2 <= x <= 3 for x in n); n4 = sum(x >= 4 for x in n)
cutpx = sorted(fm[c] for c in cuts)
txtc = [r for r in st if lab(r).startswith('text card') or lab(r).startswith('text swaps') or 'text swaps' in lab(r)]
txtcards = [r for r in st if lab(r).startswith('text card')]
# zoom
zr = []
for x in zm:
    d = float(x['scale_b_over_a']) - 1; dt = (int(x['frame_b']) - int(x['frame_a'])) / fps
    zr.append((abs(d), d / dt, x))
zsig = [z for z in zr if z[0] > 0.002 and int(z[2]['inliers']) >= 100]
zlow = [z for z in zr if int(z[2]['inliers']) < 100]
zflat = [z for z in zr if z[0] <= 0.002 and int(z[2]['inliers']) >= 100]
zrates = sorted(abs(z[1]) * 100 for z in zsig)
ztop = max(zsig, key=lambda z: z[0])
zlowtxt = '; '.join(f"f{z[2]['state_start']}-f{z[2]['state_end']} ({z[2]['inliers']} inliers, scale {float(z[2]['scale_b_over_a']):.3f})" for z in zlow)
# stepped footage
stepch = [f for f in range(3804, 3921) if fm[f] >= 100000]
gaps = collections.Counter(b - a for a, b in zip(stepch, stepch[1:]))
# word sync stats
ev = [int(r['start_frame']) / fps for r in st]
near = lambda t: min(abs(t - w) for w in WS_)
e3 = sum(near(t) <= 0.3 for t in ev)
random.seed(7); rnd = [random.uniform(0, 535) for _ in range(20000)]
r1 = 100 * sum(near(t) <= 0.1 for t in rnd) / len(rnd); r3 = 100 * sum(near(t) <= 0.3 for t in rnd) / len(rnd)
import os
if os.path.exists(f'{ws}/tables/phrase_alignment_summary.json'):
    _p = json.load(open(f'{ws}/tables/phrase_alignment_summary.json')); r1 = 100 * _p['random_within_0_1']; r3 = 100 * _p['random_within_0_3']
lags = sorted(f / fps - t for f, w, t in pairs); early = sum(l < 0 for l in lags)
nw = len(W); span = max(x[1] for x in W)
# sponsor
SP0, SP1 = 8981, 11078
sponsor_states = [r for r in st if SP0 <= int(r['start_frame']) <= SP1]
# lists by label
def frames(sub, cls='CUT'):
    return [int(r['start_frame']) for r in st if sub in lab(r) and r['entering_class'].startswith(cls)]
anch = [835, 903, 1643, 6624, 7290, 13053]
det = frames('detective'); rope = [2268, 5350, 13184]; vi = frames('value investing')
tl = frames('timeline'); vault = [733, 4308, 11937]; trader = [4420, 14780]
camp = frames('campsite'); server = frames('server room'); tmap = frames('treasure map'); gears = frames('gear')
ftxt = lambda a: ', '.join(f'f{x}' for x in a)
blank = [(int(r['start_frame']), int(r['end_frame'])) for r in st if lab(r).startswith('black')]
ctrl = sorted(int(r['start_frame']) for r in st if r['entering_class'].startswith('CUT'))
# scroll bursts
def burst(a, b):
    return [(int(e['start_frame']), int(e['end_frame']) - int(e['start_frame']) + 1) for e in ep if a <= int(e['start_frame']) <= b and int(e['end_frame']) > int(e['start_frame'])]
doc = [x for x in burst(9302, 9503) if x[1] >= 30]; rem = burst(10543, 10680)
bigeps = sorted([(int(e['end_frame']) - int(e['start_frame']) + 1, int(e['start_frame'])) for e in ep])[-10:][::-1]
parts = [
 (0, "Hook: game-show markets, Reddit and the three anchors", "confused figure on a 2020-2025 timeline, crossed-out ERROR calculator, letter board with logo tiles (host, then crowd), And honestly? card, figure in bed on a phone, trading-post screenshot, trader desk with a figure on the stairs, vault with THE MARKETS book (crossed out), book chained to an anchor, three anchors Earnings, Cash Flows, Economic Data, And sure... card, Vanguard bull and bear market chart"),
 (1184, "Manic phases: Large-cap, Internet stocks, Banks", "timeline with three glass bubbles added one by one (Large-cap, Internet stocks, Banks), figure with headphones, pointing figure, dot-com bubble versus A.I. meme still, Sooner or later... card, three anchors, VALUE INVESTING skyline that cracks at f1852"),
 (1958, "Prices versus fundamentals", "S&P 500 PE chart with red arrows, poker table (one player, then four), the opening confused figure again, tug-of-war rope snapping between Market Prices and Fundamentals, living room with the two sign holders, 2020 circled on a timeline, house door, DJ booth, storm with umbrella"),
 (2878, "It rewired them: the pandemic story", "text cards (It rewired them., Invest for the long-term, Buy quality companies at fair prices, The story has changed..., Now it's...) alternating with 1940-2025 timelines, STONKS ONLY meme, falling red and rising green lines through big-tech logos, glasses figure, money-bag figure, crossed-out chalkboard portrait, storm, desk with water jugs, federal funds rate chart, footage of a speaker with flying banknotes, turtle on a road, brain with two quotes"),
 (4144, "Professionals struggle: trader and Michael Burry", "red curtains, struck-through desk scene, spreadsheet figure, vault with the crossed-out book, trader at six monitors (question marks added), photos of a man and a second portrait with an $800 million label, The Big Short poster, Fundamentals figure, news headline card, Why? card, scanned investor letter (circle, then arrows), rope snap, teacher at a green board with gold, housing and S&P charts, Keynes quote card"),
 (5757, "Market can stay irrational: cliff and question marks", "cliff with the two sign holders, photos with $800 million...remember?, cracked VALUE INVESTING skyline, ??? card"),
 (6240, "Behavioral finance explained", "four-circle Behavioral Finance diagram, boardroom (Efficient, Rational), Human arrow, anchors Psychology, Emotions, Biases, detective with a Duhhh note board, school hallway, two portrait photos, 1970-circled timeline, jet window, kneeling figure with a falling chart, anchors with market excuses, detective boards with Nvidia, bitcoin, Palantir, gold, bubble infographic board, Efficient Market Hypothesis card, intrinsic value question cards, Narratives greater than Balance Sheets, Momentum greater than Valuations, Palantir stock card, chameleon, server-room box, campfire phone"),
 (8921, "Sponsor: Aura and data brokers", "thumbs-up figure, Sponsored by AURA card, creature at a night computer, Right now... card, Data Broker Market chart with a headline overlay, redacted report that scrolls in four bursts, auction scene, hooded figure and message sender, supermarket Personal Data box, blue AURA scenes, product screens, pink eraser, umbrella in rain, browser search results, video clip, app dashboard, removal list that scrolls, waving figure with the link, teacher and striped-hat figure at a link board, blue AURA card"),
 (11079, "Social media speed", "Wall Street on puppet strings, framed creatures labelled GREED, FEAR, HERD MENTALITY, RECENCY BIAS then caged, snail with an envelope, guard at a velvet rope, gears, Now? card, bedroom alarm clock, tweet with Netflix chart, figure brushing teeth, turtle crossed out then hare, vault book, four-circle diagram, server room, campsite phone with Information and Reaction signs"),
 (12320, "Institutions adapt", "reading figure, rising green line, cliff, Because of this... card, reader beside seated suits, spreadsheet figure, text list Cash Flows, Discount Rates, Trading Multiples crossed out and replaced by Online Narratives and Sentiment Analysis, figure in bed, 2020 timeline, anchors, rope snap, podcaster at a desk"),
 (13426, "Fad or structural shift", "Is this just a fad? and Is this a structural shift in markets? cards, student at a desk with floating icons, It's too early to tell. card, THE GREAT DEBATE stage, detective boards, bubble infographic board, creature crate with a red arrow and circle, astronaut, two briefcases (The AI Bubble 2023 - 2026??), crossed-out gears, campsite phone, trader desk, VALUE INVESTING skyline, If that's true... card, detective with a glass bubble, balance scale with money"),
 (15173, "Closing: the real question", "detective with ??? board, They do. and The real question is... cards, treasure map from Behavioral Finance to Alpha, fist figure, shocked figure among quote bubbles, COMMENTS card, not sure if irony or serious meme, meeting room with a bubble on the projector, figure frowning at a mirror"),
 (16057, "End card", "white card: Subscribe for more Casual Finance with a YouTube mark and social icons; holds to the last frame"),
]
rows = ['| Part | Frames | Seconds | States | OBSERVED content |', '|---|---|---|---|---|']
for i, (f0, name, desc) in enumerate(parts):
    f1 = (parts[i + 1][0] - 1) if i + 1 < len(parts) else LASTF
    rows.append(f'| {name} | f{f0}-f{f1} | {f0/fps:.1f}-{(f1+1)/fps:.1f} | {sid(f0)}-{sid(f1)} | {desc} |')
nz = sum('ZOOM' in r['entering_class'] for r in st)
body = f'''## 2. Structure (MEASURED frames; part boundaries are INFERRED from visuals plus ASR narration)
''' + '\n'.join(rows) + f'''

Reading: a {LASTF+1}-frame, {(LASTF+1)/fps:.1f} s explainer arguing that prices have loosened from fundamentals and that behavioral finance now drives them. It has no chapter cards; the parts above are my reading of narration and visuals. A sponsor block for Aura runs f{SP0}-f{SP1} ({(SP1-SP0+1)/fps:.1f} s, {100*(SP1-SP0+1)/(LASTF+1):.1f} percent of the video, INFERRED from the Sponsored by AURA card and the blue AURA card plus the ASR sponsor lines) and the video closes on a {(LASTF-16057+1)/fps:.1f} s end card. The visual register is hand-drawn stick-figure vector on near-white, mixed with full-bleed coloured scenes, meme stills, photographs, charts, screenshots and text-only cards.

## 3. Shots and cut rhythm (MEASURED)
- {len(st)} visual states and {len(sh)} shots from {len(cuts)} hard cuts plus the opening shot; mean state {S.mean(sds):.2f} s, median {S.median(sds):.2f} s.
- Shot length: median {S.median(L)/fps:.2f} s, mean {S.mean(L)/fps:.2f} s, interquartile range {q[0]/fps:.2f}-{q[2]/fps:.2f} s; shortest {min(L)/fps:.2f} s ({mn['shot_id']}, f{mn['start_frame']}-f{mn['end_frame']}), longest {max(L)/fps:.2f} s ({mx['shot_id']}, f{mx['start_frame']}-f{mx['end_frame']}); {len(longs)} shot exceeds 10 s ({longtxt}); {sum(l>=150 for l in L)} shots last 5 s or more; {len(shorts)} shots last 1 s or less (mostly one-line text cards).
- Encoder alignment: {len(cuts)-len(non)} of the {len(cuts)} hard cuts start on an I-frame ({100*(len(cuts)-len(non))/len(cuts):.1f} percent; {len(I)} I-frames in total, mean gap {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.2f} s). The {len(non)} cuts that do not (f{', f'.join(map(str,non))}) were viewed on native frames (winF, winG, winH, winI rows): each is a one-frame replacement with no dissolve or smear.
- State classes (base class of each state): CUT {base['CUT']}, POP_IN {base['POP_IN']}, TEXT_SWAP {base['TEXT_SWAP']}, POSE {base['POSE']}, FADE_IN {base['FADE_IN']}, START {base['START']}. Of the {len(ep)} change episodes, every one starts within one frame of a state start or inside a state that carries its own motion class (MICRO, ANIM or ZOOM suffix).
- Hard-cut size: grayscale changes above 25 levels at the cut frame run from {cutpx[0]:,} px to {cutpx[-1]:,} px (median {cutpx[len(cutpx)//2]:,}); the smaller ones are cuts between two mostly white pages.
- Text-only cards: {len(txtcards)} states open on a one-line card (centred hand-lettered text on white); {base['TEXT_SWAP']} states replace text in place; one black interval (f10379-f10380, {len(blank)} state) precedes the video clip in the sponsor block.
- Between f2878 and f3180 five text states (f2878, f2953, f3014 swap, f3120, f3160 swap) alternate with two timelines (f2915, f3083); the shots SH029, SH030 and SH032 last only 1.23-1.27 s.

## 4. Motion and animation (MEASURED + OBSERVED)
- Episodes: {len(ep)} candidate change episodes, of which {n1} last one frame ({100*n1/len(n):.1f} percent), {n23} last two or three frames and {n4} last four frames or more (longest {max(n)} frames at f{bigeps[0][1]}). Most of the long ones are camera pushes on held illustrations, footage, scrolling UI or small character animation: the ten longest start at f{', f'.join(str(b[1]) for b in bigeps)}.
- Pop-in rule: text, labels, circles, arrows, bubbles, logos and props appear in one frame. Items are added to a held layout at spaced intervals: bubbles on the timeline at f1184, f1267, f1335 (gaps 83, 68 frames); anchors Earnings, Cash Flows, Economic Data at f903, f937, f965 (gaps 34, 28) and Psychology, Emotions, Biases at f6624, f6659, f6689 (gaps 35, 30); text list lines at f12689, f12718, f12754 (gaps 29, 36) then crossed out at f12784 and extended at f12814, f12844 (gaps 30, 30); creature labels at f11222, f11243, f11261, f11290 (gaps 21, 18, 29).
- Camera scale (MEASURED, ORB feature matching with RANSAC between start+4 and end-3): {len(zm)} states of at least 25 frames measured. {len(zsig)} states with at least 100 inliers change scale by more than 0.002 (slow push-in on a held illustration; median rate {zrates[len(zrates)//2]:.2f} percent per second, largest net scale {1+max(float(z[2]['scale_b_over_a'])-1 for z in zsig):.4f} at f{ztop[2]['state_start']}-f{ztop[2]['state_end']}), {len(zflat)} states are flat (|scale-1| at most 0.002), and {len(zlow)} states have fewer than 100 inliers and are not reliable measurements ({zlowtxt}). All {len(zsig)} measured scale changes are positive (push-ins, none pulls out); make_states tagged {nz} states with a ZOOM_IN class suffix using its own threshold. This differs from the locked-off camera measured in DKyJABtbF2o.
- Footage cadence: in the speaker clip (f3804-f3920) {len(stepch)} frames change by 100,000 px or more (the cut frame f3804 plus {len(stepch)-1} later frames); {gaps[3]} consecutive gaps are exactly 3 frames and the one other gap is f3846 to f3852, so the clip updates about 10 times per second inside the 30 fps stream (MEASURED).
- Scrolling UI: the redacted report scrolls in {len(doc)} bursts ({', '.join(f'f{a} for {b} frames' for a, b in doc)}), and the removal list scrolls in {len(rem)} short bursts between f10543 and f10672.
- Fades: a headline overlay fades in over a dimmed page from f9176 and a clip fades up from black from f10381; no dissolve was seen at any hard cut.
- Text change type: {base['TEXT_SWAP']} states replace text, an annotation or a screenshot in one frame (for example f13464 swaps the fad question for the structural-shift question; f5558-f5627 swap the chart on the green board three times).
- Character redraws: POSE states change a figure or scene in one frame at f681, f1537, f1852 (cracks), f2464, f13609, f14451 (briefcase lid opens), f14602, f15006; small repeating wobble (about 300-500 px per episode) runs on stick figures, arrows and timelines inside many states and is left to the MICRO class.
- 30 fps constant frame rate ({LASTF+1} frames); the pulldown test (24 fps content in a 30 fps file) was not run, so whether the animation was authored at 24 or 30 fps is UNAVAILABLE.

## 5. Art direction and graphics
- Palette (k-means, 8 colours over one frame per state, {len(st)} frames): ''' + ', '.join(f"{c['hex']} {c['share_pct']} percent" for c in pal) + f'''. Colour names are INFERRED from the swatches: near-white canvas, cream and grey grounds, sky and sea blue, dark teal-grey, charcoal, wood brown, near-black outlines.
- Style: black-outlined stick-figure and flat vector drawings on near-white, rounded hand-lettered type, full-bleed coloured scenes for gags (sea floor, cliff, night bedroom, red stage curtains, brick office, jungle, blue AURA backdrop), red as the main annotation colour (circles, crosses, arrows).
- Recurring set pieces (states entering on a cut; counts from state labels): anchor scenes {len(anch)} (f{', f'.join(map(str,anch))}); rope-snap scenes {len(rope)} ({ftxt(rope)}); detective-board scenes {len(det)} ({ftxt(det)}); VALUE INVESTING skyline {len(vi)} ({ftxt(vi)}); vault book {len(vault)} ({ftxt(vault)}); six-monitor trader desk {len(trader)} ({ftxt(trader)}; a different office desk with a stair figure at f596); server room {len(server)} ({ftxt(server)}); campsite phone {len(camp)} ({ftxt(camp)}); treasure map {len(tmap)} ({ftxt(tmap)}).
- Third-party material, OBSERVED: meme stills (dot-com bubble versus A.I., STONKS ONLY, not sure if irony or serious), photographs of people (including a Big Short themed press photo, two portraits, a footage clip of a speaker with banknotes and a woman looking at a phone), a Big Short film poster, a news headline card, a scanned letter, a tweet card, charts and infographics (Vanguard, FRED, S&P 500 quote cards, a Palantir quote card, Visual Capitalist, Corporate Finance Institute, Investopedia), product screens for the sponsor, and logos (Nvidia, Microsoft, Google, Tesla, Amazon, Apple, Meta, Palantir, bitcoin, Aura, YouTube). Photos, clips and logos belong to third parties; people shown in photographs are named only where on-screen text names them.
- Text: headings, labels, quotes and card text were read from decoded frames; small body text inside letters, charts, articles and UI screenshots is only partly legible and is quoted only in part.

## 6. Object lifecycles (OBSERVED)
- Sea-floor anchors: scenes at {ftxt(anch)} (the book chained to an anchor at f835, then labels Earnings, Cash Flows, Economic Data built at f903, f937, f965; the three-anchor scene again at f1643; Psychology, Emotions, Biases at f6624-f6689; market-excuse labels at f7290; Psychology, Emotions, Biases again at f13053).
- Timelines: {len(tl)} timeline scenes ({ftxt(tl)}); the 2020 marker is circled in red and an arrow flips direction (left at f2915, right at f3083).
- Detective and note board: logo notes (Nvidia, bitcoin, Palantir, gold) around Behavioral Finance at f7411, red X at f7486 and f8606; ??? variants at f8451 and f15173.
- Value investing skyline: intact at f1712, cracked at f1852, repeated at f5983, f14845.
- Rope snap: f2268, f5350, f13184, always the same two figures labelled Market Prices and Fundamentals.
- Briefcases: closed at f14373, left case opens at f14451 showing The AI Bubble 2023 - 2026??, closes at f14602 with a red circle around the right case.
- Closing run: treasure map f15306, fist figure f15481, quote bubbles f15536, map f15669, COMMENTS card f15761, meme f15847, meeting room f15914, mirror f15973.

## 7. Attention hypotheses (INFERRED, no retention or CTR data)
1. A new visual state appears every {S.mean(sds):.1f} s on average and a hard cut every {S.mean(L)/fps:.1f} s; {n1} of {len(ep)} change episodes are single frames, so the viewer follows the next object or sentence, not motion. ASR counts {nw:,} words over {span:.0f} s (about {nw/span*60:.0f} words per minute), a dense narration that a frequent cut may be meant to match.
2. In {early} of {len(pairs)} selected phrase pairs the picture changes before the spoken word (median lead {abs(S.median(lags)):.2f} s); a visual already on screen when the phrase lands may reinforce it, but the pair selection is mine and the lead may partly reflect ASR timing.
3. Without chapter cards the video leans on recurring set pieces (anchors, rope snap, detective board, skyline, map) as visual landmarks that the viewer may use to track the argument.
4. Short text cards ({len(txtcards)} states, many under 1.3 s) work as punchlines and as pace breaks; the 70 s sponsor block shifts to screen recordings and product visuals, which may signal a change of mode.
5. The video opens on the confused figure and returns to it at f2212; the closing sequence ends on a COMMENTS card and a mirror gag, which may invite replies and end on a joke.

## 8. Uncertainties and limits
- Audio was never heard; ASR (openai-whisper small.en) is provisional, so AV sign-off is BLOCKED. Phrase pairs ({len(pairs)} kept of 177 candidates) were hand-selected; 2 candidates had no matching ASR token (f4076 sell-off, f10466 fraud) and 26 were dropped for a lag beyond 1.5 s (f123, f278, f733, f835, f1712, f2391, f2673, f3479, f4265, f5350, f5867, f7021, f7411, f7486, f7830, f7982, f8053, f8805, f8981, f9750, f9887, f10153, f10284, f10814, f11624, f11716), not counted as unpaired.
- ASR event-to-nearest-word offsets ({e3} of {len(ev)} state starts within 0.3 s) are not evidence of sync: random times fall within 0.3 s of some word start {r3:.1f} percent of the time and within 0.1 s {r1:.1f} percent of the time in the build_docs random control.
- People in photographs and clips are not independently identified; names come from on-screen text only (the headline card names Michael Burry, the labels name Keynes). ASR mentions of other people are not used to identify what is on screen.
- Letter, chart, article and UI body text is only partly transcribed; axes, legends and small print are not read.
- Changed-pixel counts in state descriptions are frame_metrics.csv full-resolution grayscale differences above 25 levels at the state's first frame; episodes.csv and sheet-header counts use a different colour-difference measure.
- Camera scale values are net scale between two decoded frames; states with fewer than 100 inliers ({len(zlow)}) are reported as unreliable, not as zoom.
- Whether the file is an original upload, re-encode or edit export is not known. Sponsor-block bounds, part boundaries, pace claims and attention hypotheses are INFERRED.
'''
open(f'{ws}/build/report_body.md', 'w').write(body)
mods = f'''## Modules (original rebuild; derived from measured patterns)
1. **Cast and set kit**: a generic stick man, a detective with a magnifier, a trader at a six-monitor desk, a podcaster, a student, a rope-snapping pair with signs, anchors, a cliff, a vault with a book, a server-room box, a crate of creatures, a treasure map, briefcases. Redraw all as new original assets; do not trace the source.
2. **Hard-cut scene chain**: {len(cuts)} hard cuts, median shot {S.median(L)/fps:.1f} s ({min(L)/fps:.1f}-{max(L)/fps:.1f} s); {len(cuts)-len(non)} cuts land on I-frames and {len(non)} do not, so author cuts as true edits and let the encoder place keyframes.
3. **One-frame pop-in vocabulary**: text, labels, circles, arrows and props appear in a single frame with no easing; {n1} of {len(ep)} episodes are one frame.
4. **Labelled-anchor build**: add one anchor and label per beat (gaps of 28-36 frames) so an enumerated list reads as a build.
5. **Text-card punchline**: one centred hand-lettered line on white, optionally swapped in place; timelines with a red circle and a direction arrow as the connective tissue.
6. **Slow push-in**: {len(zsig)} held illustrations drift in by {zrates[0]:.2f}-{zrates[-1]:.2f} percent per second; add a barely visible scale ramp to long holds.
7. **Third-party insert slot**: charts, meme stills, photographs, headline cards, letters, tweets, clips and logos are replaced with licensed or self-made equivalents; never copy the source items.
8. **Sponsor block**: a Sponsored by card, product screen recordings, a creative gag set (eraser, umbrella, auction) and a closing logo card; keep the block {(SP1-SP0+1)/fps:.0f} s and separate from the argument.
9. **Annotation marks**: red circles, red crosses and red arrows as the only accent colour.
10. **Recurring landmarks**: reuse the same few set pieces (anchors, rope snap, detective board, skyline) as visual shorthand for recurring arguments.
11. **Footage slot**: stock clips are stepped at about 10 changes per second inside the 30 fps stream; use licensed footage and decide the step rate deliberately.
12. **End card**: white card with Subscribe for more, channel name, YouTube mark and social icons, held {(LASTF-16057+1)/fps:.0f} s.
13. **Codec note**: 30 fps constant frame rate, {len(I)} I-frames about every {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.1f} s on average.
'''
open(f'{ws}/build/modules.md', 'w').write(mods)
views = {
 "native_windows": [
  "winA rows: f54-f62 (figure to calculator, f60), f118-f125 (calculator to letter board, f123), f211-f215 (board to And honestly? card, f213), f234-f238 (card to crowd board, f236), f276-f280 (crowd board to figure in bed, f278), f450-f454 (bed to phone screenshot, f452), f594-f598 (screenshot to trader desk, f596)",
  "winB rows: f679-f683 (stairs figure pose at f681), f731-f735 (trader to vault, f733), f833-f837 (vault to underwater book, f835), f1850-f1853 (skyline cracks at f1852), f2462-f2466 (living-room expressions at f2464), f1480-f1484 (timeline to headphone figure, f1482), f1535-f1539 (headphones off at f1537)",
  "winC rows: f3919-f3923 (clip to turtle, f3921), f4142-f4146 (brain to curtains, f4144), f4203-f4208 (curtains to crossed-out desk, f4206), f4262-f4266 (desk to spreadsheet figure, f4265)",
  "winD rows: f4418-f4422 (vault to trader desk, f4420), f4554-f4558 (trader to photo, f4556), f4603-f4607 (photo to two portraits, f4605), f4866-f4871 (poster to photo with arrow, f4869), f4911-f4914 (Fundamentals figure at f4913)",
  "winE rows: f9174-f9180 and f9230-f9232 (headline overlay fade from f9176), f9300-f9304 (report page at f9302), f9501-f9505 (auction scene at f9503), f8561-f8565 (chameleon to detective board, f8563), f8803-f8807 (server room to campfire, f8805), f6960-f6964 (arrow at f6962)",
  "winF rows: f10377-f10384 (black at f10379, clip fades up from f10381), f10404-f10409 (clip notification), f10464-f10468 (clip to dashboard, f10466), f10670-f10674 (list to link figure, f10672), f10541-f10545 (screen swap at f10543), f10812-f10816 (link figure to teacher board, f10814)",
  "winG rows: f11818-f11822 (bathroom to crossed-out turtle, f11820), f12157-f12161 (server room to campsite, f12159), f11893-f11897 (turtle to hare, f11895), f11222-f11224 and f11241-f11244 (creature labels)",
  "winH rows: f15479-f15483 (map to fist figure, f15481), f15667-f15671 (bubbles to map, f15669), f16055-f16059 (mirror to end card, f16057), f16203-f16206 (end card), f14001-f14005 (detective to dark-haired figure, f14003), f14371-f14375 (astronaut to briefcases, f14373), f12319-f12321 (campsite to reader, f12320)",
  "winI rows: f3118-f3122 (timeline to text card, f3120), f3477-f3481 (glasses figure to money bag, f3479), f5067-f5071 (headline card to Why?, f5069), f6238-f6242 (??? to four-circle diagram, f6240), f15249-f15253 (detective board to They do., f15251)"
 ],
 "stepped_sheets": [
  "overview 1 fps (542 tiles, 31 sheets, all viewed)",
  "episode change-crop sheets epc_01-50 (399 episodes: context frame with changed-pixel bbox, crop at start-1, crop at start; all 50 sheets viewed)",
  f"state_rep ({len(st)} states, 13 sheets, all viewed)"
 ],
 "episode_view": f"per episode: context frame at its first changed frame with the changed-pixel bbox, plus bbox crops at start-1 and start (adjacent decoded frames); every multi-frame episode and every frame of 8,000 changed px or more was checked against frame_metrics to place state boundaries (found a missed cut at f11995 hidden in the last frame of EP0301; f4144, f4420, f4556, f4605, f4869, f6932, f8563, f8805 and f9503 also sit on the last or a later frame of a multi-frame episode, and {len(st)} states were placed in total)",
 "text_gate": "PARTIAL_OPEN_LIMITATION (headings, labels, quotes, card text and logo names read from decoded frames; small body text inside letters, charts, articles and UI screenshots flagged not transcribed or quoted only in part; people in photographs and clips not identified beyond on-screen names)"
}
json.dump(views, open(f'{ws}/build/views.json', 'w'), indent=1)
print('written', len(body), len(mods))
print('zsig', len(zsig), 'zflat', len(zflat), 'zlow', len(zlow), 'rates', [round(x, 2) for x in zrates[:3]], round(zrates[-1], 2))
print('anch', anch, 'rope', rope, 'det', det, 'vi', vi, 'tl', tl[:20]); print('vault', vault, 'trader', sorted(trader), 'server', server, 'camp', camp, 'tmap', tmap)
print('txtcards', len(txtcards), 'blank', blank, 'doc', doc, 'rem', rem); print('control', r1, r3, 'e3', e3, len(ev), 'early', early, len(pairs), 'bigeps', bigeps); print('gaps', gaps)
