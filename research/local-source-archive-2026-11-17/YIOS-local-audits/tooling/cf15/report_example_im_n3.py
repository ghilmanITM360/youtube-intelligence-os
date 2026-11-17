import csv, json, sys, random, statistics as S, collections, os
ws = sys.argv[1]; fps = 30; LASTF = 20485
st = list(csv.DictReader(open(f'{ws}/visual_states.csv'))); sh = list(csv.DictReader(open(f'{ws}/shot_ledger.csv')))
man = json.load(open(f'{ws}/source_manifest.json')); I = set(man['iframe_indices'])
fm = {int(r['frame']): int(float(r['fullres_changed_px_thr25'])) for r in csv.DictReader(open(f'{ws}/tables/frame_metrics.csv'))}
zm = [x for x in csv.DictReader(open(f'{ws}/tables/zoom_measure.csv')) if x['scale_b_over_a'] not in ('', None)]
ep = list(csv.DictReader(open(f'{ws}/tables/episodes.csv')))
pal = json.load(open(f'{ws}/tables/palette.json'))['colors']
pairs = json.load(open(f'{ws}/build/phrase_pairs.json'))
asr = json.load(open(f'{ws}/audio/Im-N3K9Pnf0_small_en.json'))
W = [(x['start'], x['end'], x['word'].strip()) for s in asr['segments'] for x in s['words']]; WS_ = sorted(x[0] for x in W)
sid = lambda f: next(r['visual_state_id'] for r in st if int(r['start_frame']) <= f <= int(r['end_frame']))
lab = lambda r: r['label'].lower()
base = collections.Counter(r['entering_class'].split('+')[0] for r in st)
cuts = [int(r['start_frame']) for r in st if r['entering_class'].startswith('CUT')]; non = [c for c in cuts if c not in I]
L = [int(s['end_frame']) - int(s['start_frame']) + 1 for s in sh]; q = S.quantiles(L, n=4)
mn = min(sh, key=lambda s: int(s['end_frame']) - int(s['start_frame'])); mx = max(sh, key=lambda s: int(s['end_frame']) - int(s['start_frame']))
longs = [s for s in sh if int(s['end_frame']) - int(s['start_frame']) + 1 > 240]
longtxt = '; '.join(f"{s['shot_id']} f{s['start_frame']}-f{s['end_frame']} ({(int(s['end_frame'])-int(s['start_frame'])+1)/fps:.1f} s)" for s in longs)
shorts = [s for s in sh if int(s['end_frame']) - int(s['start_frame']) + 1 <= 12]
sds = [int(r['frames']) / fps for r in st]
n = [int(e['end_frame']) - int(e['start_frame']) + 1 for e in ep]
n1 = sum(x == 1 for x in n); n23 = sum(2 <= x <= 3 for x in n); n4 = sum(x >= 4 for x in n)
cutpx = sorted(fm[c] for c in cuts)
zr = []
for x in zm:
    d = float(x['scale_b_over_a']) - 1; zr.append((abs(d), x))
zsig = [z for z in zr if z[0] > 0.002 and int(z[1]['inliers']) >= 100]; zlow = [z for z in zr if int(z[1]['inliers']) < 100]; zflat = [z for z in zr if z[0] <= 0.002 and int(z[1]['inliers']) >= 100]
zlowtxt = '; '.join(f"f{z[1]['state_start']}-f{z[1]['state_end']} ({z[1]['inliers']} inliers, scale {float(z[1]['scale_b_over_a']):.3f})" for z in zlow)
zsigtxt = '; '.join(f"f{z[1]['state_start']}-f{z[1]['state_end']} (scale {float(z[1]['scale_b_over_a']):.3f}, {z[1]['inliers']} inliers)" for z in zsig)
def cad(a, b, thr=3000):
    ch = [f for f in range(a, b + 1) if fm[f] >= thr]; g = collections.Counter(y - x for x, y in zip(ch, ch[1:])); return len(ch), b - a + 1, sorted(g.items())
c1 = cad(13751, 13961); gtxt = lambda c: ', '.join(f'{k} frame{"s" if k > 1 else ""} x{v}' for k, v in c[2])
ev = [int(r['start_frame']) / fps for r in st]; near = lambda t: min(abs(t - w) for w in WS_); e3 = sum(near(t) <= 0.3 for t in ev)
random.seed(7); rnd = [random.uniform(0, 682.9) for _ in range(20000)]
r1 = 100 * sum(near(t) <= 0.1 for t in rnd) / len(rnd); r3 = 100 * sum(near(t) <= 0.3 for t in rnd) / len(rnd)
if os.path.exists(f'{ws}/tables/phrase_alignment_summary.json'):
    _p = json.load(open(f'{ws}/tables/phrase_alignment_summary.json')); r1 = 100 * _p['random_within_0_1']; r3 = 100 * _p['random_within_0_3']
lags = sorted(f / fps - t for f, w, t in pairs); early = sum(l < 0 for l in lags)
nw = len(W); span = max(x[1] for x in W)
agaps = [(int(W[i][1] * fps), int(W[i + 1][0] * fps), W[i + 1][0] - W[i][1]) for i in range(len(W) - 1) if W[i + 1][0] - W[i][1] >= 3.0]
agtxt = '; '.join(f'f{a}-f{b} ({g:.1f} s)' for a, b, g in agaps) or 'none'
def frames(sub, cls=''):
    return [int(r['start_frame']) for r in st if sub in lab(r) and r['entering_class'].startswith(cls)]
cnt = lambda sub: len(frames(sub))
bigeps = sorted([(int(e['end_frame']) - int(e['start_frame']) + 1, int(e['start_frame'])) for e in ep])[-10:][::-1]
parts = [
 (0, "Hook: what is coming in 2026", "chicken between two cars, bear with megaphone under a Recession cloud, bull in a game store, Over the last year..., FRED unemployment chart, bartender, slumped man before a rising chart, city street with a 2026 sign, Rate Cuts, cafe reader, All Possible, S&P 500 screenshot, sunbather with cigar, mailbox and letter, podcaster, sad man after New Year"),
 (1964, "Three doors: bearish, bullish or unknown", "To be transparent..., doors BEARISH / BULLISH / ???, man spinning a prediction wheel, cafe reader, arrow at the Bearish door"),
 (2567, "Bear case 1: Artificial Intelligence", "chip king on a throne, elephant in VR goggles, One thing is clear..., calculator with ERROR, NVIDIA, Palantir and Datadog quote pages, chalkboard Fundamentals, silver-bar basement, The problem is..., NVIDIA figure hauling a sack uphill, When NVIDIA up Then, S&P 500 PE ratio chart and statistics card with a 16x mean line, AI deals network diagram, report page, reader to people in suits"),
 (4701, "Bear case 2: Concentration", "bear waving, 2. Concentration bear bench-pressing, handshake with bear, Magnificent Seven market cap chart, narrow leadership chart, Big Tech blueprints, crossed-out film poster, That's right., Goldman Sachs Mag 7 vs 493 chart, S&P 500 YTD attribution, eleven-sector pie, stressed analysts, passive vs active chart, equal vs cap weighted bars, NVIDIA and Kraft Heinz logos, The bigger the company, rising and falling arrows with logos, dominoes, NVIDIA candlestick chart, Nasdaq Venn diagram, puppet-string skyline, bridge on pillars"),
 (8795, "Bear case 3: We're Due", "bear waving, We're Due doctor scene, S&P 500 falling arrow, man fleeing meteors, glasses man, equity returns pyramid, drawdown curve, annual returns bars, bull and bear history chart, falling candlesticks, social post I was wrong to say sell, meditating man over SELL, quote card attributed to John Maynard Keynes, And that's the uncomfortable truth, Valuations checklist, man at mirror, doors, S&P 500 and PE charts, NVIDIA climber"),
 (11119, "Bull case 1: Interest rate cuts", "charging bull, 1. Interest Rate Cuts bull pulling an arrow, chalkboard with Federal Reserve seal, official photo with Cut Rates disc, FRED federal funds chart, rate decision table, dot plot, Lower Rates, Lower Rates to Cheaper Capital flow, money bag, Liquidity Loosens checklist, S&P 500 chart, ECONOMIC UNEASE podium, red X marks"),
 (12913, "Sponsor segment (FlexiSpot)", "Sponsored by FlexiSpot card, hunched man at a bedroom desk at night, annual report page, trader with headline screens, Standing desks on the other hand, standing-desk drawings, live-action desk footage, 440lbs load capacity graphic, 30000+ lift tests, 30-day risk-free return policy, product page, code YTE730"),
 (14853, "Bull case 2: Fiscal policy and deficit spending", "chalkboard Financial Markets, book Monetary Policy / ??? then Fiscal Policy, bucket 2. Deficit Spending, Cuts? speaker before a committee, Uncle Sam signing among paper stacks, federal deficit chart, channel video grid, But the reality is... / In the short-term... / It brings some benefits., armchair man and Social Security check, FRED consumption chart, cheering executives, GDP growth chart, Fiscal Spending machine, Social Security / Medicare / Medicaid giants, Keep Spending! and Stonks Go Up rallies, Even if growth cools..., And that matters."),
 (16724, "Bull case 3: Big tech and positioning", "thinking man, charging bull, bridge on big-tech pillars, podcaster, magician card The Most Likely Outcome is the One Nobody's Positioned For, On one side..., gala guest with martini, official photo push-in, Uncle Sam in a tank, crowned chip man with bread, S&P 500 chart, On the other side..., projector The Issue, detective and Mag 7 bubble, PE ratio 16x chart, We're Due"),
 (17856, "What to do: no door is certain", "S&P 500 chart with red arrows and X, doors with red check, sideways squiggle, park bench headlines MARKET CRASH! / ALL-TIME HIGHS!, praying man, hamster wheel, C'mon, do something... / My Portfolio, Bullish and Bearish doors crossed out, Every stock feels eerie... / Every decision feels wrong..., asset cycle, outcome wheel, lost driver at night, long-nosed puppet, Trading Courses stand"),
 (19449, "Closing advice and comments", "The best thing you can do is..., student at desk, doors with a moving red arrow, man pointing at the viewer, Comments board"),
 (20193, "Sponsor reprise (FlexiSpot)", "product page scroll and zoom, code YTE730"),
 (20336, "End card", "white card: Subscribe for more Casual Finance with a YouTube mark and crossed-out social icons"),
]
rows = ['| Part | Frames | Seconds | States | OBSERVED content |', '|---|---|---|---|---|']
for i, (f0, name, desc) in enumerate(parts):
    f1 = (parts[i + 1][0] - 1) if i + 1 < len(parts) else LASTF
    rows.append(f'| {name} | f{f0}-f{f1} | {f0/fps:.1f}-{(f1+1)/fps:.1f} | {sid(f0)}-{sid(f1)} | {desc} |')
board = sum('chalkboard' in lab(r) or lab(r).startswith('board ') for r in st)
caps = sum(lab(r).startswith('caption') for r in st)
anim_states = sum('+ANIM' in r['entering_class'] for r in st)
spon = [r for r in st if 12913 <= int(r['start_frame']) <= 14852 or 20193 <= int(r['start_frame']) <= 20335]
c2 = cad(13962, 14187); c3 = cad(20206, 20269)
anim = 'f718-f799 (panicking man close-up), f1235-f1311 (S&P 500 screenshot pans), f2299-f2445 (prediction wheel spins), f13751-f13961 (video of a standing desk in a room), f13962-f14187 and f14188-f14328 (live-action desk footage with camera moves, frames of 100,000 px or more at f14128-f14153 and f14279-f14280), f17243-f17287 (slow push-in on the official photo), f20206-f20269 (product page scroll and zoom)'
body = '## 2. Structure (MEASURED frames; part boundaries are INFERRED from visuals plus ASR narration)\n' + '\n'.join(rows) + f"""

Reading: a {LASTF+1}-frame, {(LASTF+1)/fps:.1f} s market-outlook explainer for 2026, delivered as a stick-figure explainer with typed text cards, three recurring doors (Bearish / Bullish / ???), handwritten red marks and many inserted charts, quote pages and photos. Numbered title scenes mark three bear-case points (1. Artificial Intelligence f2567, 2. Concentration f4793, 3. We're Due f8880) and three bull-case points (1. Interest Rate Cuts f11227, 2. Deficit Spending f15164, then big tech and positioning). A sponsor segment (FlexiSpot) runs f12913-f14852 ({(14853-12913)/fps:.1f} s) and returns briefly at f20193-f20335 with the discount code. The file ends on a {(LASTF-20336+1)/fps:.1f} s end card.

## 3. Shots and cut rhythm (MEASURED)
- {len(st)} visual states and {len(sh)} shots from {len(cuts)} hard cuts plus the opening shot; mean state {S.mean(sds):.2f} s, median {S.median(sds):.2f} s.
- Shot length: median {S.median(L)/fps:.2f} s, mean {S.mean(L)/fps:.2f} s, interquartile range {q[0]/fps:.2f}-{q[2]/fps:.2f} s; shortest {min(L)/fps:.2f} s ({mn['shot_id']}, f{mn['start_frame']}-f{mn['end_frame']}), longest {max(L)/fps:.2f} s ({mx['shot_id']}, f{mx['start_frame']}-f{mx['end_frame']}); {len(longs)} shots exceed 8 s ({longtxt}); {sum(l>=150 for l in L)} shots last 5 s or more; {len(shorts)} shots last 0.4 s or less.
- Encoder alignment: {len(cuts)-len(non)} of the {len(cuts)} hard cuts start on an I-frame ({100*(len(cuts)-len(non))/len(cuts):.1f} percent; {len(I)} I-frames in total, mean gap {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.2f} s). The {len(non)} that do not (f{', f'.join(map(str,non))}) were each viewed on the episode change-crop sheets: f3234 and f3314 swap one stock quote page for the next, f14402 replaces the load-capacity graphic, f20206 starts the product page scroll, and the rest are one-frame scene replacements. Eleven candidate reframes first noted from the change-crop sheets were bounding-box crops, not cuts, and were removed after the validator showed no entry change at those frames.
- State classes (base class): CUT {base['CUT']}, POP_IN {base['POP_IN']}, POSE {base['POSE']}, START {base['START']}; {anim_states} states carry an ANIM suffix.
- Hard-cut size: grayscale changes above 25 levels at the cut frame run from {cutpx[0]:,} px to {cutpx[-1]:,} px (median {cutpx[len(cutpx)//2]:,}).
- Recurring scene types (states, from labels): text card states {cnt('text card')}, door states {cnt('door')}, chart states {cnt('chart')}; {len(spon)} states fall inside the two sponsor ranges.
- Boundaries hidden on the last frame of multi-frame episodes, found by printing frames of 100,000 px or more not within one frame of a state start and confirmed on native frames (gapw sheets 1-6): f5116, f5525, f5673, f5696, f5790, f5909, f11890, f13321, f13962, f14188, f14329, f15164, f16683, f17171, f17288, f17714, f17751, f17795, f17856, f19449, f20270. Runs of 100,000 px or more at f14128-f14153 and f14279-f14280 are camera moves inside live footage, not cuts.

## 4. Motion and animation (MEASURED + OBSERVED)
- Episodes: {len(ep)} candidate change episodes, of which {n1} last one frame ({100*n1/len(n):.1f} percent), {n23} last two or three frames and {n4} last four frames or more (longest {max(n)} frames at f{bigeps[0][1]}). The ten longest start at f{', f'.join(str(b[1]) for b in bigeps)}.
- Pop-in rule: arrows, labels, red X marks, checks and text lines appear in one frame; text cards add a second line in place (In the short-term... f15843, It brings some benefits. f15873, Every decision feels wrong... f18961), and the red arrow over the doors jumps between doors (f19826, f19928, f20016).
- Camera scale (MEASURED, ORB feature matching with RANSAC between start+4 and end-3): {len(zm)} states of at least 25 frames measured. {len(zsig)} change scale by more than 0.002 at 100 inliers or more ({zsigtxt or 'none'}), {len(zflat)} are flat and {len(zlow)} have fewer than 100 inliers and are not reliable ({zlowtxt or 'none'}).
- Sponsor segment: no progress bar was seen; the sponsor read is marked by a Sponsored by FlexiSpot card at f12913 and closes on the code card at f14744.
- In-state animation (OBSERVED, ranges from frame_metrics): {anim}. The crying-trader shot has {c1[0]} of {c1[1]} frames changing by 3,000 px or more; the speaking-man clip {c2[0]} of {c2[1]}; the TV news clip {c3[0]} of {c3[1]}.
- Held scenes drift: most held drawings and charts carry a slow push-in measured by camera scale (below), not separate reframe cuts.
- 30 fps constant frame rate ({LASTF+1} frames).

## 5. Art direction and graphics
- Palette (k-means, 8 colours over one frame per state, {len(st)} frames): """ + ', '.join(f"{c['hex']} {c['share_pct']} percent" for c in pal) + f""". Colour names are INFERRED from the swatches: white canvas dominant, light grey, near-black line, dark grey, olive, brown, pale blue and a small blue share.
- Style: black-outlined stick figures and flat props on white with typed text cards and hand-lettered labels; red for X marks, falling arrows and annotations, green for rising arrows; recurring cast (stick man, glasses man, bull, bear, Uncle Sam, NVIDIA climber, podcaster, detective, doctor and patient).
- Third-party material, OBSERVED: FRED and other economic charts, stock quote pages (NVIDIA, Palantir, Datadog), S&P 500 screenshots, a report page, an annual report filing page, a film poster, a social post, a quote card, a photo of a suited official, a channel page, live-action standing-desk footage and FlexiSpot product pages and graphics, plus company logos. They belong to third parties; people in photographs are not identified except by on-screen text.
- Text: text cards, labels, chart titles and logo names were read from decoded frames; small body text in charts and screenshots is only partly legible.

## 6. Object lifecycles (OBSERVED)
- Three doors (Bearish / Bullish / ???): f2000, f2524 (arrow at Bearish), f10828, f17997 (check on ???), f18756, f18814 and f18824 (Bullish and Bearish crossed out), f19566, f19826-f20016 (moving arrow).
- S&P 500 chart: f1235, f8990, f10886, f12509, f17448, f17856, f18091 (red X), f18117, f18147 (sideways squiggle), f18290, f18464.
- PE ratio chart with 16x line: f3947, f4143, f10949, f17751.
- NVIDIA climber: f3610, f4257, f7388, f11033.

## 7. Attention hypotheses (INFERRED, no retention or CTR data)
1. A new visual state appears every {S.mean(sds):.1f} s on average and a hard cut every {S.mean(L)/fps:.1f} s; {n1} of {len(ep)} change episodes are single frames. ASR counts {nw:,} words over {span:.0f} s (about {nw/span*60:.0f} words per minute).
2. In {early} of {len(pairs)} phrase pairs the picture changes before the spoken word (median lead {abs(S.median(lags)):.2f} s); pairs match on-screen words to the same spoken word, and the lead may partly reflect ASR timing.
3. ASR gaps of 3 s or more: {agtxt}. These pauses sit on the three numbered bear-case title scenes; elsewhere the narration is continuous.
4. The three doors return at each turn of the argument and act as a signpost; this is INFERRED.
5. Slow push-ins keep held drawings moving without new art; whether this holds attention is INFERRED and not measured.

## 8. Uncertainties and limits
- Audio was never heard; ASR (openai-whisper small.en) is provisional, so AV sign-off is BLOCKED. Phrase pairs ({len(pairs)} kept) were selected by a script that matches content words of each state's visible text to the nearest same spoken word within 2.5 s; 9 matches with a lag beyond 1.5 s were dropped and states with no match are not counted as unpaired.
- ASR event-to-nearest-word offsets ({e3} of {len(ev)} state starts within 0.3 s) are not evidence of sync: random times fall within 0.3 s of some word start {r3:.1f} percent of the time and within 0.1 s {r1:.1f} percent of the time in the random control.
- The 1 fps overview sheet set (38 sheets) and the 15 state representative sheets were generated but not viewed. Coverage rests on the 53 episode change-crop sheets (all viewed), the gap check against frame_metrics and native-frame windows (gapw 1-6, all viewed). Inside clips and other animated states, per-frame changes are left to the ANIM class.
- People in photographs and clips are not identified; names come from on-screen text only.
- Screenshot body text is only partly transcribed.
- Changed-pixel counts are frame_metrics.csv full-resolution grayscale differences above 25 levels; episodes.csv and sheet-header counts use a different colour-difference measure.
- Camera scale values are net scale between two decoded frames; states with fewer than 100 inliers ({len(zlow)}) are reported as unreliable, not as zoom.
- Whether the file is an original upload, re-encode or edit export is not known. Part boundaries, pace claims and attention hypotheses are INFERRED.
"""
open(f'{ws}/build/report_body.md', 'w').write(body)
mods = f"""## Modules (original rebuild; derived from measured patterns)
1. **Cast and prop kit**: stick man, glasses man, bull, bear, Uncle Sam, NVIDIA climber, doctor and patient, detective, three doors, text cards. Redraw as new original assets; do not trace the source.
2. **Hard-cut scene chain**: {len(cuts)} hard cuts, median shot {S.median(L)/fps:.1f} s ({min(L)/fps:.2f}-{max(L)/fps:.1f} s); {len(cuts)-len(non)} land on I-frames and {len(non)} do not.
3. **Three-door signpost**: {cnt('door')} door states; move a red arrow, check or X between the doors.
4. **One-frame pop-in builds**: {n1} of {len(ep)} episodes are one frame; build groups one item per step.
5. **Typed text cards**: {cnt('text card')} white cards with one or two typed lines that build in place.
6. **Sponsor block**: a {(14853-12913)/fps:.0f} s segment opened by a Sponsored by card and closed by a code card, with a short reprise before the end card; use your own sponsor.
7. **Third-party insert slot**: photos, clips, charts, logos and screenshots are replaced with licensed or self-made equivalents.
8. **Text-line builds**: add a second typed line to a card in place instead of cutting.
9. **Slow push-in on held scenes**: {len(zsig)} of {len(zm)} measured states grow in scale by about 0.2-4 percent across the state; add a gentle push-in to held drawings and charts.
10. **End card**: white card with Subscribe for more, channel name, YouTube mark and crossed-out social icons held {(LASTF-20336+1)/fps:.1f} s.
11. **Codec note**: 30 fps constant frame rate, {len(I)} I-frames about every {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.1f} s on average.
"""
open(f'{ws}/build/modules.md', 'w').write(mods)
views = {
 "native_windows": [
  "gapw rows: f5115-f5117, f5524-f5526, f5672-f5674, f5695-f5697, f5789-f5791, f5908-f5910, f11889-f11891, f13320-f13322, f13961-f13963, f14187-f14189, f14328-f14330, f15163-f15165, f16682-f16684, f17170-f17172, f17287-f17289, f17713-f17715, f17750-f17752, f17794-f17796, f17855-f17857, f19448-f19450, f20269-f20271"
 ],
 "stepped_sheets": [
  "overview 1 fps (38 sheets generated by sheets.py; NOT viewed, so they are not counted as visual coverage)",
  f"episode change-crop sheets epc_01-53 ({len(ep)} episodes: context frame with changed-pixel bbox, crop at start-1, crop at start; all 53 sheets viewed)",
  f"state_rep ({len(st)} states, 15 sheets, generated but NOT viewed)"
 ],
 "episode_view": f"per episode: context frame at its first changed frame with the changed-pixel bbox, plus bbox crops at start-1 and start (adjacent decoded frames); every frame of 100,000 changed px or more not within one frame of a state start was viewed natively (gap check), which found 21 hidden boundaries; {len(st)} states were placed in total",
 "text_gate": "PARTIAL_OPEN_LIMITATION (text cards, labels, chart titles and logo names read from decoded frames; body text inside charts and screenshots flagged not transcribed or quoted only in part; people in photographs not identified)"
}
json.dump(views, open(f'{ws}/build/views.json', 'w'), indent=1)
print('written', len(body), len(mods)); print('zsig', len(zsig), zsigtxt); print('zlow', len(zlow), 'board', board, 'caps', caps, 'anim', anim_states, 'spon', len(spon))
print('longs', longtxt, 'agaps', agtxt, 'control', r1, r3, 'e3', e3, len(ev), 'early', early, len(pairs), c1[:2], c2[:2], c3[:2])
