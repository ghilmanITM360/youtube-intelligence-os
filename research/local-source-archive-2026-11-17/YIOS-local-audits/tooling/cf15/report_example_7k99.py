import csv, json, sys, random, statistics as S, collections, os
ws = sys.argv[1]; fps = 30; LASTF = 18149
st = list(csv.DictReader(open(f'{ws}/visual_states.csv'))); sh = list(csv.DictReader(open(f'{ws}/shot_ledger.csv')))
man = json.load(open(f'{ws}/source_manifest.json')); I = set(man['iframe_indices'])
fm = {int(r['frame']): int(float(r['fullres_changed_px_thr25'])) for r in csv.DictReader(open(f'{ws}/tables/frame_metrics.csv'))}
zm = [x for x in csv.DictReader(open(f'{ws}/tables/zoom_measure.csv')) if x['scale_b_over_a'] not in ('', None)]
ep = list(csv.DictReader(open(f'{ws}/tables/episodes.csv')))
pal = json.load(open(f'{ws}/tables/palette.json'))['colors']
pairs = json.load(open(f'{ws}/build/phrase_pairs.json'))
asr = json.load(open(f'{ws}/audio/7K991LgY3tc_small_en.json'))
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
c1 = cad(436, 479); gtxt = lambda c: ', '.join(f'{k} frame{"s" if k > 1 else ""} x{v}' for k, v in c[2])
ev = [int(r['start_frame']) / fps for r in st]; near = lambda t: min(abs(t - w) for w in WS_); e3 = sum(near(t) <= 0.3 for t in ev)
random.seed(7); rnd = [random.uniform(0, 598) for _ in range(20000)]
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
 (0, "Hook: on the surface vs underneath", "Uncle Sam flexing on a globe with fireworks, S&P 500 and inflation screenshots, a fast-food social post, three text cards (On the surface... / Life is good. / But underneath...), burning-room dog meme clip, podium and nightclub scenes, credit crisis kettle, a social post listing record household debts built line by line, detective at an evidence board, Uncle Sam slumped in a restroom stall"),
 (1793, "Chapter 1: The Big Picture, America's Debt Mountain", "chapter card over a money mountain, debt list post, government debt infographic, spending-by-category bar chart with red marks, interest expense chart, article excerpt, White House cash-stack scene, hedge meme clip, average debt by generation card, total debt balance chart with ~60% and $18.6 trillion marks, national debt counter, drowning man, taped Capitol, western poster recut into a Good / Bad / Ugly icon frame"),
 (4687, "Chapter 2: The Good, Housing Debt", "chapter card over a suburban house, debt tree diagram (Housing / Non-Housing, Mortgage / Home Equity), mortgage bullets, closed-end and HELOC icon flows on cream, NY Fed breakdown chart with $13.1 Trillion, sitcom clip, HELOC balances chart (30%, $411 bn), family portrait annotations, a documentary poster for the non-housing branch, the tree reduced to Student Debt and CC Debt"),
 (8661, "Chapter 3: The Bad, Student Loan Debt", "chapter card over a university on a floating cliff, graduates on a conveyor with a ball and chain, rocket scene, three-panel No Credit History / No Collateral / No Financial Literacy, CPI and tuition charts with lines drawing in, cause-and-effect text flow, NY Fed chart with $1.7 Trillion and ~9%, borrowers by age and average balance charts, delinquency chart with <1% and >9% marks, Secured / Unsecured Loan tree, graveyard of debt tombstones, beach scene"),
 (11692, "Chapter 4: The Ugly, Credit Card Debt", "chapter card over a shopkeeper holding a burning card, poster icon frame with red marks, three text cards, NY Fed chart with $1.2 Trillion, 50% and 9%, banker desk scene with FEES, accounts and population charts, circus clown juggling cards, delinquency chart with 12.41%, inflation, house price, wage and card-rate charts, drowning man reprise"),
 (14562, "BNPL segment", "game-style challenger banner reading BNPL, pink canvas, phone checkout screens, BNPL company logos crossed out, mirror disguise scene, BNPL use by generation card, Federal Reserve statistic card, key points card"),
 (15977, "Consumer-spending paradox and conclusion", "phone user (This is awesome!), news headline screenshots, instalment food order, debt list post reprise, ECONOMY BOOMING! podium, men passing a lit bomb to Uncle Sam, White House cash-stack reprise, national debt counter reprise, stacked text lines (It's not loud / sudden / dramatic; It's quiet / gradual / happening in plain sight), S&P 500, inflation and unemployment screenshots, opening Uncle Sam scene as a bookend, closing text card"),
 (17970, "End card", "white card: Subscribe for more Casual Finance with a YouTube mark, crossed-out social icons and a stick figure beside a SUBSCRIBE button; last frame black"),
]
rows = ['| Part | Frames | Seconds | States | OBSERVED content |', '|---|---|---|---|---|']
for i, (f0, name, desc) in enumerate(parts):
    f1 = (parts[i + 1][0] - 1) if i + 1 < len(parts) else LASTF
    rows.append(f'| {name} | f{f0}-f{f1} | {f0/fps:.1f}-{(f1+1)/fps:.1f} | {sid(f0)}-{sid(f1)} | {desc} |')
chap = frames('chapter'); cc = [round(f / fps, 1) for f in chap]
agap_list = [(round(W[i][1], 1), round(W[i + 1][0], 1)) for i in range(len(W) - 1) if W[i + 1][0] - W[i][1] >= 3.0]
ch_in_gap = sum(any(a - 0.5 <= t <= b + 0.5 for a, b in agap_list) for t in cc)
hl = sum('highest level' in r['visible_text'].lower() for r in st)
poster = sum('poster' in lab(r) and 'documentary' not in lab(r) for r in st); tree = sum('tree' in lab(r) for r in st)
tcard = sum(lab(r).startswith('text card') for r in st); tswap = sum(lab(r).startswith(('text swaps', 'line ', 'lines ', 'word ')) for r in st)
chart = sum('chart' in lab(r) for r in st); anno = sum(any(k in lab(r) for k in ('annotation', 'circle', 'red x', 'ellipse', 'arrow', 'bracket', 'label')) for r in st)
anim = 'f436-f480 (burning-room dog meme clip), f3082-f3143 (hedge meme clip), f7176-f7223 (two-character sitcom clip), f9529-f9581 (chart lines draw in)'
c2 = cad(3082, 3142); c3 = cad(7180, 7222); c4 = cad(9529, 9581, 200)
body = '## 2. Structure (MEASURED frames; part boundaries are INFERRED from visuals plus ASR narration)\n' + '\n'.join(rows) + f"""

Reading: a {LASTF+1}-frame, {(LASTF+1)/fps:.1f} s explainer on US household debt built as a Good / Bad / Ugly argument. Four chapter cards (f{', f'.join(map(str, chap))}) split housing, student loan and credit card debt; a western movie poster recut into three icon panels (house, cap, card) appears in {poster} states as the map of the argument. No sponsor segment was seen and the ASR has no sponsor read. The opening Uncle Sam scene returns at f17843 as a bookend, and the file ends on a {(LASTF-17970)/fps:.1f} s end card plus one black frame.

## 3. Shots and cut rhythm (MEASURED)
- {len(st)} visual states and {len(sh)} shots from {len(cuts)} hard cuts plus the opening shot; mean state {S.mean(sds):.2f} s, median {S.median(sds):.2f} s.
- Shot length: median {S.median(L)/fps:.2f} s, mean {S.mean(L)/fps:.2f} s, interquartile range {q[0]/fps:.2f}-{q[2]/fps:.2f} s; shortest {min(L)/fps:.2f} s ({mn['shot_id']}, f{mn['start_frame']}-f{mn['end_frame']}), longest {max(L)/fps:.2f} s ({mx['shot_id']}, f{mx['start_frame']}-f{mx['end_frame']}); {len(longs)} shots exceed 8 s ({longtxt}); {sum(l>=150 for l in L)} shots last 5 s or more; {len(shorts)} shots last 0.4 s or less.
- Encoder alignment: {len(cuts)-len(non)} of the {len(cuts)} hard cuts start on an I-frame ({100*(len(cuts)-len(non))/len(cuts):.1f} percent; {len(I)} I-frames in total, mean gap {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.2f} s). The {len(non)} that do not (f{', f'.join(map(str,non))}) were each viewed on native frames (start-2 to start+2, sheets hid1 and hid2): all are one-frame replacements with no dissolve.
- State classes (base class): CUT {base['CUT']}, POP_IN {base['POP_IN']}, POSE {base['POSE']}, START {base['START']}.
- Hard-cut size: grayscale changes above 25 levels at the cut frame run from {cutpx[0]:,} px to {cutpx[-1]:,} px (median {cutpx[len(cutpx)//2]:,}); small values are cuts between two mostly white text cards or between two grey-backed screenshots.
- Recurring scene types (states, from labels): white text cards {tcard} plus {tswap} in-place text or line swaps, states whose label names a chart {chart}, debt tree diagram {tree}, poster icon frame {poster}, The highest level ever recorded. card {hl} times, annotation marks (circles, X marks, arrows, brackets, handwritten values) {anno}.
- One cut sat on the last frame of a two-frame episode: f11116 (And the worst part? card to the Secured Loan tree; 919 px at f11115, {fm[11116]:,} px at f11116), found by the gap check and confirmed on native frames.

## 4. Motion and animation (MEASURED + OBSERVED)
- Episodes: {len(ep)} candidate change episodes, of which {n1} last one frame ({100*n1/len(n):.1f} percent), {n23} last two or three frames and {n4} last four frames or more (longest {max(n)} frames at f{bigeps[0][1]}). The ten longest start at f{', f'.join(str(b[1]) for b in bigeps)}.
- Pop-in rule: text lines, list items, icons, logos, circles, X marks and handwritten values appear in one frame with no easing; list builds add one item per step (debt list lines f1274, f1304, f1327, f1366, f1397; tree leaves f8213, f8244, f8269, f8299).
- Camera scale (MEASURED, ORB feature matching with RANSAC between start+4 and end-3): {len(zm)} states of at least 25 frames measured. {len(zsig)} change scale by more than 0.002 at 100 inliers or more ({zsigtxt or 'none'}), {len(zflat)} are flat (|scale-1| at most 0.002) and {len(zlow)} have fewer than 100 inliers and are not reliable ({zlowtxt or 'none'}). The camera is locked off; no push-in or pan was measured.
- In-state animation (OBSERVED, ranges from frame_metrics): {anim}. The first meme clip has {c1[0]} of {c1[1]} frames changing by 3,000 px or more (gaps {gtxt(c1)}); the hedge clip {c2[0]} of {c2[1]} (gaps {gtxt(c2)}); the sitcom clip {c3[0]} of {c3[1]} (gaps {gtxt(c3)}). These clips update about every third frame, about 10 updates per second inside a 30 fps file. The chart draw-in has {c4[0]} of {c4[1]} frames changing by 200 px or more (gaps {gtxt(c4)}).
- Fades: none seen; every hard cut viewed natively is a one-frame replacement.
- 30 fps constant frame rate ({LASTF+1} frames).

## 5. Art direction and graphics
- Palette (k-means, 8 colours over one frame per state, {len(st)} frames): """ + ', '.join(f"{c['hex']} {c['share_pct']} percent" for c in pal) + f""". Colour names are INFERRED from the swatches: white canvas, mid grey (screenshot backdrop), pale pink-grey, dark green-grey, near-black, khaki, light blue, orange.
- Style: flat outlined cartoon characters (an Uncle Sam figure, a detective, bankers, a man in a vest, graduates) on white, with handwritten-style type on white text cards; cream backgrounds for icon flows; screenshots and charts are placed on a mid-grey backdrop; annotation colours change by chapter (red and orange for housing, red and black for student loans, blue and black for credit cards).
- Third-party material, OBSERVED: search-result and financial chart screenshots (S&P 500, inflation, unemployment, population), New York Fed and FRED charts, a government-debt infographic, a spending-by-category chart, article and news screenshots, social posts, a fast-food promotion post, a TV host photograph, a western movie poster, a documentary poster, meme clips and a two-character sitcom clip, BNPL company logos and a phone checkout screen. They belong to third parties; people in photographs are not identified.
- Text: headings, labels, card text and handwritten values were read from decoded frames; small body text inside articles, charts and UI screenshots is only partly legible and quoted only in part.

## 6. Object lifecycles (OBSERVED)
- Poster icon frame: poster f4223, arrow to debt post f4358, blank panels with house f4555, cap f4584, card f4619; returns f5102 (house circled f5147), f8783 (cap circled f8835), f11824 (card circled f11870, arrow f11907), f13391, f17201, f17752.
- Debt tree: heading f4953, two branches f5022, housing sub-branches f5201, mortgage circled f5420; returns f6677 (home equity circled f6739), f7994, f8134 (four leaves f8213-f8299, two crossed f8330-f8375, removed f8501, circled f8578-f8616).
- NY Fed breakdown chart: mortgage f6200-f6486 ($13.1 Trillion), student loan f10003-f10241 ($1.7 Trillion, ~9%), credit card f12105-f12588 ($1.2 Trillion, 50%, 9%).
- Delinquency chart: f10670 (student loan marks to f11006), f13465 (12.41% f13625, peak circle f13688), f14337.
- Bookend: Uncle Sam on the globe at f0 and f58 returns at f17843 with fireworks and We're the best.

## 7. Attention hypotheses (INFERRED, no retention or CTR data)
1. A new visual state appears every {S.mean(sds):.1f} s on average and a hard cut every {S.mean(L)/fps:.1f} s; {n1} of {len(ep)} change episodes are single frames, so the viewer follows the next card or chart, not motion. ASR counts {nw:,} words over {span:.0f} s (about {nw/span*60:.0f} words per minute).
2. In {early} of {len(pairs)} phrase pairs the picture changes before the spoken word (median lead {abs(S.median(lags)):.2f} s); pairs match on-screen words to the same spoken word, and the lead may partly reflect ASR timing.
3. ASR gaps of 3 s or more: {agtxt}. {ch_in_gap} of the {len(chap)} chapter cards ({', '.join(f'{t} s' for t in cc)}) fall inside one of these gaps, so the chapter cards sit in pauses in the narration (what is heard there is UNAVAILABLE because audio was not heard).
4. The poster icon frame and the debt tree return across chapters and may work as a map of the argument; the repeated The highest level ever recorded. card ({hl} times) is a verbal and visual refrain.
5. Reaction meme and sitcom clips (f436, f3082, f7176) are the only moving footage; their comic purpose is INFERRED.

## 8. Uncertainties and limits
- Audio was never heard; ASR (openai-whisper small.en) is provisional, so AV sign-off is BLOCKED. Phrase pairs ({len(pairs)} kept) were selected by a script that matches content words of each state's visible text to the nearest same spoken word within 2.5 s; 13 matches with a lag beyond 1.5 s were dropped and states with no match are not counted as unpaired.
- ASR event-to-nearest-word offsets ({e3} of {len(ev)} state starts within 0.3 s) are not evidence of sync: random times fall within 0.3 s of some word start {r3:.1f} percent of the time and within 0.1 s {r1:.1f} percent of the time in the random control.
- The 1 fps overview sheet set (34 sheets) was generated; only sheet 1 was viewed. Coverage rests on the 34 episode change-crop sheets (all viewed), the gap check against frame_metrics, 12 native-frame windows (hid1 and hid2) and 13 state sheets (all viewed). Small in-state changes below the episode threshold are not individually recorded.
- People in photographs and clips are not identified; names come from on-screen text only.
- Article, chart, UI and report body text is only partly transcribed; axes, legends and small print are not read.
- Changed-pixel counts are frame_metrics.csv full-resolution grayscale differences above 25 levels; episodes.csv and sheet-header counts use a different colour-difference measure.
- Camera scale values are net scale between two decoded frames; states with fewer than 100 inliers ({len(zlow)}) are reported as unreliable, not as zoom.
- Whether the file is an original upload, re-encode or edit export is not known. Part boundaries, pace claims and attention hypotheses are INFERRED.
"""
open(f'{ws}/build/report_body.md', 'w').write(body)
mods = f"""## Modules (original rebuild; derived from measured patterns)
1. **Cast and prop kit**: an Uncle Sam style figure, detective, bankers, graduates, a man in a vest, a shopkeeper; props (globe, podium, kettle, cork board, cash stack, piggy banks, tombstones, rocket). Redraw all as new original assets; do not trace the source.
2. **Hard-cut scene chain**: {len(cuts)} hard cuts, median shot {S.median(L)/fps:.1f} s ({min(L)/fps:.2f}-{max(L)/fps:.1f} s); {len(cuts)-len(non)} land on I-frames and {len(non)} do not, so author cuts as true edits and let the encoder place keyframes.
3. **White text-card beats**: one handwritten-style line on white, swapped in place for two- and three-step phrases; {tcard} text-card states.
4. **Argument map**: a three-panel Good / Bad / Ugly frame with one icon per chapter, revisited and circled before each chapter.
5. **Chapter cards**: four illustrated title cards placed in pauses in the narration.
6. **Chart on grey with handwritten value**: screenshot chart on a grey backdrop, then a coloured circle, bracket and handwritten value as a separate one-frame pop-in.
7. **Tree and icon flows**: diagram built one leaf per pop-in; cream-background three-icon flows with arrows.
8. **Third-party insert slot**: charts, articles, posts, posters, memes and clips are replaced with licensed or self-made equivalents; never copy the source items.
9. **Locked-off camera**: no zoom or pan; motion comes only from short meme or sitcom clips and one chart draw-in.
10. **Bookend and end card**: return to the opening scene before the closing line, then a {(LASTF-17970)/fps:.0f} s subscribe end card.
11. **Codec note**: 30 fps constant frame rate, {len(I)} I-frames about every {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.1f} s on average.
"""
open(f'{ws}/build/modules.md', 'w').write(mods)
views = {
 "native_windows": [
  "hid1 rows: f117-f121 (f119), f2884-f2888 (f2886), f5697-f5701 (f5699), f6602-f6606 (f6604), f9138-f9142 (f9140), f11113-f11118 (f11116 hidden last-frame cut)",
  "hid2 rows: f11952-f11956 (f11954), f12445-f12449 (f12447), f14004-f14008 (f14006), f17706-f17710 (f17708), f17841-f17845 (f17843), f18146-f18149 (f18149 black frame)"
 ],
 "stepped_sheets": [
  "overview 1 fps (34 sheets generated by sheets.py; only sheet 1 viewed, so they are not counted as visual coverage)",
  f"episode change-crop sheets epc_01-34 ({len(ep)} episodes: context frame with changed-pixel bbox, crop at start-1, crop at start; all 34 sheets viewed)",
  f"state_rep ({len(st)} states, 13 sheets, all viewed)"
 ],
 "episode_view": f"per episode: context frame at its first changed frame with the changed-pixel bbox, plus bbox crops at start-1 and start (adjacent decoded frames); every frame of 8,000 changed px or more was compared with the state starts (gap check; all remaining frames fall inside the three listed clip ranges) and the hidden cut at f11116 was viewed natively; {len(st)} states were placed in total",
 "text_gate": "PARTIAL_OPEN_LIMITATION (headings, labels, card text, handwritten values and logo names read from decoded frames; small body text inside articles, charts and UI screenshots flagged not transcribed or quoted only in part; people in photographs not identified)"
}
json.dump(views, open(f'{ws}/build/views.json', 'w'), indent=1)
print('written', len(body), len(mods)); print('zsig', len(zsig), 'zflat', len(zflat), 'zlow', len(zlow))
print('chap', chap, cc, 'in gap', ch_in_gap, 'hl', hl, 'poster', poster, 'tree', tree, 'tcard', tcard, 'tswap', tswap, 'chart', chart, 'anno', anno)
print('longs', longtxt, 'agaps', agtxt, 'control', r1, r3, 'e3', e3, len(ev), 'early', early, len(pairs), c1, c2, c3, c4)
