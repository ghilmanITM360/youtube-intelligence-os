import csv, json, sys, random, statistics as S, collections, os
ws = sys.argv[1]; fps = 24; LASTF = 14260
st = list(csv.DictReader(open(f'{ws}/visual_states.csv'))); sh = list(csv.DictReader(open(f'{ws}/shot_ledger.csv')))
man = json.load(open(f'{ws}/source_manifest.json')); I = set(man['iframe_indices'])
fm = {int(r['frame']): int(float(r['fullres_changed_px_thr25'])) for r in csv.DictReader(open(f'{ws}/tables/frame_metrics.csv'))}
zm = [x for x in csv.DictReader(open(f'{ws}/tables/zoom_measure.csv')) if x['scale_b_over_a'] not in ('', None)]
ep = list(csv.DictReader(open(f'{ws}/tables/episodes.csv')))
pal = json.load(open(f'{ws}/tables/palette.json'))['colors']
pairs = json.load(open(f'{ws}/build/phrase_pairs.json'))
asr = json.load(open(f'{ws}/audio/dPoDyl9Ys38_small_en.json'))
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
c1 = cad(950, 994); gtxt = lambda c: ', '.join(f'{k} frame{"s" if k > 1 else ""} x{v}' for k, v in c[2])
ev = [int(r['start_frame']) / fps for r in st]; near = lambda t: min(abs(t - w) for w in WS_); e3 = sum(near(t) <= 0.3 for t in ev)
random.seed(7); rnd = [random.uniform(0, 585) for _ in range(20000)]
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
 (0, "Hook: the crypto hater returns; MicroStrategy and industry recaps", "stick figure, Ethereum and Bitcoin coins with a prohibition ring, YouTube channel card and Trojan-horse video thumbnail, MicroStrategy logo cards, bills, dynamite with a 00:30 timer, comment-card stacks (several with Editor's note captions), price charts with red arrows, Panik meme, finish-line ribbon, pointer-stick figure, thumbnails, cap figure (Trust me, bro!), Bitcoin character with a cane, rug, chalkboard (So... What about Bitcoin?), block chain on a bar"),
 (2449, "Jenga tower and the three narratives", "tower of wooden blocks with a Bitcoin block, equals signs with gold bars, curly-haired figure and Dollar is out, Bitcoin is in!, rising arrows, smirk-figure row, Only dumb people don't buy Bitcoin!, But here's the problem card, magnifying glass, REPORT and STUDY papers, cycle diagram of the narrative loop"),
 (3365, "What was Bitcoin supposed to do: chalkboard and the 2008 paper", "chalkboard Bitcoin's value, What's the purpose?, photo and paper page, The idea?, quoted peer-to-peer electronic cash system, coin equals bill, glowing cyan bill, bank buildings, Bank of Japan crossed out, If Bitcoin succeeded... THE FUTURE!!!"),
 (4259, "Three tests of money (exchange, store, account)", "numbered list 1 to 3 with icons, hoodie and ponytail exchange scene, treasure chest, today and in a month phone-for-bill lines, equation card, bills-to-teddy-bear, car and house price lines"),
 (5058, "Test 1, medium of exchange: slow turtle, VISA, energy", "turtle with a Bitcoin coin, transactions-per-day chart, VISA with 65,000 transactions and a clock, 1.5 MILLION transactions, energy chart, four-stat footprint card with a red circle, Earth with Bitcoin icons crossed out"),
 (6137, "Test 2, store of value: gold, volatility, ownership", "running coin, top-hat figure with gold bars, chest, Two reasons chalkboard, 1. stability with price chart and 20% in ONE month!, SPECULATIVE investment, 2. ownership with PROPERTY OF sign, office scene, coin heap, article page with a highlight, Jane Street news article, Terraform text, dollar-bill wallpaper"),
 (8132, "Test 3, unit of account: priced in dollars", "3. equation card, BUSINESS tower, We accept Bitcoin bubble, 15,000 and 0,000014 lines, How many for a car? crossed out, Bitcoin character passing through"),
 (8893, "El Salvador experiment: Chivo and remittances", "WELL ACTUALLY cap figure, In 2021 card, country outline that becomes a character, Chivo logo, restaurant, phone figure and $30 FREE! lines, IMF-style report page, 98% chose traditional with a row of people, report page and survey excerpts, replayed recap scene"),
 (11500, "Recap of the three tests", "replay of the exchange-arrows, chest and equation-card list scenes (hoodie figure and car; today phone-for-bill lines; bills-to-teddy-bear lines)"),
 (11688, "Where does the value come from? Greater fool theory", "chalkboards (To be or not to be, Where does the VALUE come from?, It's just..., The Greater Fool Theory), big block chain network, It works bro!, become a MILLIONAIRE!, film still, Fool Theory article, stonks meme, truck and machine, price chart, cap figure, cycle diagram, framed chart, Bitcoin good? chalkboard, Are you the next greater fool?, closing cap-figure bubbles"),
 (14150, "End card", "white card: Subscribe for more Casual Finance with a YouTube mark and three crossed-out social icons"),
]
rows = ['| Part | Frames | Seconds | States | OBSERVED content |', '|---|---|---|---|---|']
for i, (f0, name, desc) in enumerate(parts):
    f1 = (parts[i + 1][0] - 1) if i + 1 < len(parts) else LASTF
    rows.append(f'| {name} | f{f0}-f{f1} | {f0/fps:.1f}-{(f1+1)/fps:.1f} | {sid(f0)}-{sid(f1)} | {desc} |')
anim = 'f949-f995 (burning-office clip), f1066-f1119 (two thumbnails slide in), f1182-f1214 (Earth globe), f2111-f2152 (rug lifts), f2478-f2539 (block tower wobbles), f3190-f3365 (cycle diagram builds), f8653-f8723 (coin passes through), f10464-f10599 (globe scene), f11813-f11878 (block chain zoom out), f11973-f12004 (film still), f13089-f13138 (cycle diagram assembles), f13501-f13541 (boxy machine)'
body = '## 2. Structure (MEASURED frames; part boundaries are INFERRED from visuals plus ASR narration)\n' + '\n'.join(rows) + f'''

Reading: a {LASTF+1}-frame, {(LASTF+1)/fps:.1f} s essay arguing that Bitcoin is not money, delivered as a hand-drawn stick-figure explainer. Unlike hbsYaLaN_F8 it has no chapter cards; the argument is a chalkboard list (three tests of money, then the greater-fool theory). It reuses the same scene set twice: the exchange-arrows and equation-card list scenes at f4347-f4772 return at f11500-f11675 as a recap. No sponsor segment was seen and no sponsor read was found in the ASR. The file ends on a {(LASTF-14150+1)/fps:.1f} s end card.

## 3. Shots and cut rhythm (MEASURED)
- {len(st)} visual states and {len(sh)} shots from {len(cuts)} hard cuts plus the opening shot; mean state {S.mean(sds):.2f} s, median {S.median(sds):.2f} s.
- Shot length: median {S.median(L)/fps:.2f} s, mean {S.mean(L)/fps:.2f} s, interquartile range {q[0]/fps:.2f}-{q[2]/fps:.2f} s; shortest {min(L)/fps:.2f} s ({mn['shot_id']}, f{mn['start_frame']}-f{mn['end_frame']}), longest {max(L)/fps:.2f} s ({mx['shot_id']}, f{mx['start_frame']}-f{mx['end_frame']}); {len(longs)} shots exceed 10 s ({longtxt}); {sum(l>=120 for l in L)} shots last 5 s or more; {len(shorts)} shots last 0.5 s or less.
- Encoder alignment: {len(cuts)-len(non)} of the {len(cuts)} hard cuts start on an I-frame ({100*(len(cuts)-len(non))/len(cuts):.1f} percent; {len(I)} I-frames in total, mean gap {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.2f} s). The {len(non)} that do not (f{', f'.join(map(str,non))}) were not individually viewed on native frames, so a dissolve there is not excluded by a native-frame view; every cut frame is a single frame in frame_metrics.csv with a large changed-pixel count.
- State classes (base class): CUT {base['CUT']}, POP_IN {base['POP_IN']}, POSE {base['POSE']}, TEXT_SWAP {base['TEXT_SWAP']}, FADE_IN {base['FADE_IN']}, START {base['START']}.
- Hard-cut size: grayscale changes above 25 levels at the cut frame run from {cutpx[0]:,} px to {cutpx[-1]:,} px (median {cutpx[len(cutpx)//2]:,}); small values are cuts between two mostly white pages.
- Recurring scene types (states, from labels): chalkboard {cnt('chalkboard')}, YouTube comment card {cnt('comment card')}, speech bubble {cnt('speech bubble')}, red X over an item {cnt('red x')}, Bitcoin coin character {cnt('bitcoin character')+cnt('bitcoin coin character')+cnt('character')}, list-label cards (1., 2., 3.) {cnt('list label')}.
- Cuts that sat on the last frame of a multi-frame animation range were found by the gap check and native-frame windows: f995, f1661, f3365, f5132, f8723, f10599, f12004 and f13138 (all one-frame replacements in frames viewed at start-1, start and start+1).

## 4. Motion and animation (MEASURED + OBSERVED)
- Episodes: {len(ep)} candidate change episodes, of which {n1} last one frame ({100*n1/len(n):.1f} percent), {n23} last two or three frames and {n4} last four frames or more (longest {max(n)} frames at f{bigeps[0][1]}). The long ones are animation inside a state or build-up of a diagram, not cuts: the ten longest start at f{', f'.join(str(b[1]) for b in bigeps)}.
- Pop-in rule: text lines, labels, speech bubbles, X marks, arrows and logos appear in one frame; sequences add one item per step (coins at f7400, f7408, f7415, f7420 and f7427 in single-frame steps, comment cards 11-18 frames apart, gold bars f2715, f2722, f2729).
- Camera scale (MEASURED, ORB feature matching with RANSAC between start+4 and end-3): {len(zm)} states of at least 25 frames measured. {len(zsig)} change scale by more than 0.002 at 100 inliers or more ({zsigtxt or 'none'}), {len(zflat)} are flat (|scale-1| at most 0.002) and {len(zlow)} have fewer than 100 inliers and are not reliable ({zlowtxt or 'none'}). The camera is locked off apart from the listed states.
- In-state animation (OBSERVED, ranges from frame_metrics): {anim}. The first clip (f949-f995) has {c1[0]} of {c1[1]} frames changing by 3,000 px or more; gaps between changing frames are {gtxt(c1)}.
- Third-party clip: the burning-office image at f945-f995 animates (flames and small figures) and is not a stick-figure drawing; its origin is not identified.
- Fades: one FADE_IN state (f4520, a faint translucent bill over the chest; 110 px at the first frame, onset EXACT because it is at least 20 px). No dissolve was seen at any hard cut that was viewed.
- Character redraws: expression and pose changes (POSE states) are single-frame swaps; small arm wobbles of 2,000-6,000 px recur on the standing figure and are left to the POSE class.
- 24 fps constant frame rate ({LASTF+1} frames); the pulldown test does not apply.

## 5. Art direction and graphics
- Palette (k-means, 8 colours over one frame per state, {len(st)} frames): ''' + ', '.join(f"{c['hex']} {c['share_pct']} percent" for c in pal) + f'''. Colour names are INFERRED from the swatches: white canvas, cream, near-black, brown, grey, orange, green, blue.
- Style: black-outlined stick-figure and flat vector drawings on white with hand-lettered type; orange Bitcoin coin, green bill and gold bar icons; red as the annotation colour (X marks, arrows, circles); dark cards for quoted screenshots; green chalkboard with a pointer stick for the argument headings.
- Third-party material, OBSERVED: YouTube channel and video thumbnails, comment screenshots, price-chart screenshots, web articles, a report page of an international financial institution and a survey excerpt, news articles, photographs (a seated man, an older man, a film still of a man in a tuxedo, a pile of coin tokens), meme images (a muscular Shiba, a small Shiba, a stonks image, a Panik image) and logos (MicroStrategy, VISA, Chivo, YouTube). Photos, memes and logos belong to third parties; people shown in photographs are not identified.
- Text: headings, labels, quotes and card text were read from decoded frames; small body text inside articles, charts and UI screenshots is only partly legible and quoted only in part (survey digits at f9991 are not legible on the sheet).

## 6. Object lifecycles (OBSERVED)
- Exchange-arrows list scene: f4347 arrows and two figures, f4383 car and cash stack, f4422-f4455 shift; replay f11500, f11525-f11558.
- Chest line: chest f4512, faint bill f4520, figure with money bag f4536, today f4571, in a month f4593; replay f11573, f11595.
- Equation-card line: card f4685, 10 bills = teddy bear f4709, 15,000 = car f4736, 100,000 = house f4772; replay f11622, f11639, f11675.
- Coins on a globe: icons f6050, f6054, f6061, f6067, red X f6089.
- Coin row: coins f7400, f7408, f7415, f7420, f7427, then the figure on a coin heap f7444.
- Ending run: Bitcoin good? chalkboard f13759 (text crossed out by f13820), It's just... f13852, Are you the next greater fool? f13905, cap figure bubbles f14075-f14125, end card f14150.

## 7. Attention hypotheses (INFERRED, no retention or CTR data)
1. A new visual state appears every {S.mean(sds):.1f} s on average and a hard cut every {S.mean(L)/fps:.1f} s; {n1} of {len(ep)} change episodes are single frames, so the viewer follows the next card or sentence, not motion. ASR counts {nw:,} words over {span:.0f} s (about {nw/span*60:.0f} words per minute).
2. In {early} of {len(pairs)} selected phrase pairs the picture changes before the spoken word (median lead {abs(S.median(lags)):.2f} s); the pair selection is mine and the lead may partly reflect ASR timing.
3. ASR gaps of 3 s or more: {agtxt}; whether those are silence, music or clip audio is UNAVAILABLE because audio was not heard.
4. Recurring set pieces (chalkboard with pointer, comment cards, coin character, equation-card list) may help the viewer follow a long argument; the recap replay at f11500 repeats earlier scenes.
5. Comment-card runs (f581-f627, f1357-f1410, f1764-f1811) put audience reactions on screen next to the host's reply captions; whether they were chosen for comedic or credibility effect is INFERRED.

## 8. Uncertainties and limits
- Audio was never heard; ASR (openai-whisper small.en) is provisional, so AV sign-off is BLOCKED. Phrase pairs ({len(pairs)} kept of 105 candidates) were hand-selected; 5 were dropped for a lag beyond 1.5 s (f1357 popular, f4685 third, f5658 carbon, f6033 widely, f14150 fools) and are not counted as unpaired.
- ASR event-to-nearest-word offsets ({e3} of {len(ev)} state starts within 0.3 s) are not evidence of sync: random times fall within 0.3 s of some word start {r3:.1f} percent of the time and within 0.1 s {r1:.1f} percent of the time in the random control.
- The 1 fps overview sheet set (34 sheets) was generated but not viewed for this video; coverage rests on the 52 episode change-crop sheets (all viewed), the gap check against frame_metrics, 12 native-frame windows (hid1 and hid2) and 24 state sheets (all viewed). Small in-state changes below the episode threshold are not individually recorded.
- People in photographs and clips are not independently identified; names come from on-screen text only.
- Article, chart, UI and report-page body text is only partly transcribed; axes, legends and small print are not read.
- Changed-pixel counts in state descriptions are frame_metrics.csv full-resolution grayscale differences above 25 levels at the state's first frame; episodes.csv and sheet-header counts use a different colour-difference measure.
- Camera scale values are net scale between two decoded frames; states with fewer than 100 inliers ({len(zlow)}) are reported as unreliable, not as zoom.
- Whether the file is an original upload, re-encode or edit export is not known. Part boundaries, pace claims and attention hypotheses are INFERRED.
'''
open(f'{ws}/build/report_body.md', 'w').write(body)
mods = f'''## Modules (original rebuild; derived from measured patterns)
1. **Cast and prop kit**: a generic stick man, a cap figure, a coin character with legs and a cane, a top-hat figure, a hoodie figure, ponytail figure and props (chalkboard, treasure chest, gold bars, bills, block tower, turtle, truck, machine). Redraw all as new original assets; do not trace the source.
2. **Hard-cut scene chain**: {len(cuts)} hard cuts, median shot {S.median(L)/fps:.1f} s ({min(L)/fps:.2f}-{max(L)/fps:.1f} s); {len(cuts)-len(non)} cuts land on I-frames and {len(non)} do not, so author cuts as true edits and let the encoder place keyframes.
3. **One-frame pop-in vocabulary**: text lines, bubbles, X marks, arrows, coins and logos appear in a single frame with no easing; {n1} of {len(ep)} episodes are one frame.
4. **Chalkboard argument frame**: pointer-stick figure beside a green board whose text is swapped in place for each step of the argument.
5. **Comment-card runs**: dark cards added one per 15-20 frames with short handwritten reply captions.
6. **Recap replay**: reuse earlier scene sets as a late recap instead of building new ones.
7. **Locked-off camera**: no push-ins; put motion in redraws and diagram build-ups (cycle diagram, block tower, rug lift).
8. **Third-party insert slot**: charts, articles, screenshots, photographs, memes, clip and logos are replaced with licensed or self-made equivalents; never copy the source items.
9. **Annotation marks**: red X marks, arrows and circles, yellow highlight bars as the accent system.
10. **End card**: white card with Subscribe for more, channel name, YouTube mark and crossed-out social icons held {(LASTF-14150+1)/fps:.0f} s.
11. **Codec note**: 24 fps constant frame rate, {len(I)} I-frames about every {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.1f} s on average.
'''
open(f'{ws}/build/modules.md', 'w').write(mods)
views = {
 "native_windows": [
  "hid1 rows: f994-f996 (burning clip to price chart, f995), f1660-f1662 (Panik scene to figure, f1661), f3364-f3366 (cycle diagram to chalkboard, f3365), f3411-f3413 (chalkboard held), f5131-f5133 (turtle to transactions chart, f5132), f8722-f8724 (coin character to list, f8723)",
  "hid2 rows: f10598-f10600 (globe scene to phone figure, f10599), f12003-f12005 (film still to cane character, f12004), f13137-f13139 (cycle diagram to reading figure, f13138), f5081-f5083 (bills appear around turtle, f5082), f3127-f3129 (magnifier sweep), f12341-f12343 (cap figure entering)"
 ],
 "stepped_sheets": [
  "overview 1 fps (34 sheets generated by sheets.py; NOT viewed for this video, so they are not counted as visual coverage)",
  f"episode change-crop sheets epc_01-52 ({len(ep)} episodes: context frame with changed-pixel bbox, crop at start-1, crop at start; all 52 sheets viewed)",
  f"state_rep ({len(st)} states, 24 sheets, all viewed)"
 ],
 "episode_view": f"per episode: context frame at its first changed frame with the changed-pixel bbox, plus bbox crops at start-1 and start (adjacent decoded frames); every frame of 8,000 changed px or more was compared with the state starts (gap check, all remaining frames fall inside listed animation ranges) and the last frames of multi-frame ranges were viewed natively, which found cuts at f995, f1661, f3365, f5132, f8723, f10599, f12004 and f13138; {len(st)} states were placed in total",
 "text_gate": "PARTIAL_OPEN_LIMITATION (headings, labels, quotes, card text and logo names read from decoded frames; small body text inside articles, charts, report pages and UI screenshots flagged not transcribed or quoted only in part; people in photographs not identified)"
}
json.dump(views, open(f'{ws}/build/views.json', 'w'), indent=1)
print('written', len(body), len(mods)); print('zsig', len(zsig), 'zflat', len(zflat), 'zlow', len(zlow)); print('cnt', cnt('chalkboard'), cnt('comment card'), cnt('speech bubble'), cnt('red x'), cnt('character'), cnt('list label'))
print('longs', longtxt, 'agaps', agtxt, 'control', r1, r3, 'e3', e3, len(ev), 'early', early, len(pairs), 'c1', c1)
