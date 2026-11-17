import csv, json, sys, random, statistics as S, collections, os
ws = sys.argv[1]; fps = 30; LASTF = 19010
st = list(csv.DictReader(open(f'{ws}/visual_states.csv'))); sh = list(csv.DictReader(open(f'{ws}/shot_ledger.csv')))
man = json.load(open(f'{ws}/source_manifest.json')); I = set(man['iframe_indices'])
fm = {int(r['frame']): int(float(r['fullres_changed_px_thr25'])) for r in csv.DictReader(open(f'{ws}/tables/frame_metrics.csv'))}
zm = [x for x in csv.DictReader(open(f'{ws}/tables/zoom_measure.csv')) if x['scale_b_over_a'] not in ('', None)]
ep = list(csv.DictReader(open(f'{ws}/tables/episodes.csv')))
pal = json.load(open(f'{ws}/tables/palette.json'))['colors']
pairs = json.load(open(f'{ws}/build/phrase_pairs.json'))
asr = json.load(open(f'{ws}/audio/KTnp2OlQJHA_small_en.json'))
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
c1 = cad(800, 847); gtxt = lambda c: ', '.join(f'{k} frame{"s" if k > 1 else ""} x{v}' for k, v in c[2])
ev = [int(r['start_frame']) / fps for r in st]; near = lambda t: min(abs(t - w) for w in WS_); e3 = sum(near(t) <= 0.3 for t in ev)
random.seed(7); rnd = [random.uniform(0, 628) for _ in range(20000)]
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
 (0, "Hook: back in the day on Wall Street", "Back in the day..., Wall St sign, three office workers, ME flag on an island, two film stills of traders, rising and falling arrows, office trader with phone and chart, Trust me, boss!, crying trader with flying money, slumped figure"),
 (938, "Stories versus standards", "chalkboard Story, thinking figure with group, document, banknote and stonks checks, zodiac wheel and crystal ball, chalkboard Stories = Standard, turtle carrying money, rising arrow and money bags, figure with glasses, film stills, diploma and university crest, medal, bell-curve chart in a thought bubble"),
 (2052, "In the late 1980s: the quant idea", "In the late 1980s..., three men thinking, chalkboard Random? / Statistical, Patterns cycle with a turtle, Quantitative Investing, Is this a good company?, What's the expected outcome?, Rules scroll, letter P, MATH > gut feelings, And it worked!, money bags and banknotes, worried curly-haired man with mirror"),
 (3025, "Renaissance and the Medallion Fund", "Renaissance logo, Medallion Fund medal, THE MOST SUCCESSFUL IN HISTORY!, a medallion what?, sailboat, portrait photo, Hear me out..., 2 + 2 = 4, price chart, Adobe and Alphabet arrows, CNBC news clip, computer with genie, formula meme clip, For more than 20 YEARS, 60% returns (before fees) / 39% returns (after fees), portrait with 19% return, $10,000 over 20 years to $324,000 and $7,000,000"),
 (4931, "It transformed the industry", "Medallion fund = SUCCESS!!!, It transformed the industry built word by word, office workers and computer (Now I decide!), arrows equal money, ORDER boxes, And much more!, speedster clip, medal with good job star, BIG BUSINESS, crowd of figures crossed out with two checks"),
 (6120, "By the early 2000s: active managers underperform", "By the early 2000s..., magnifier and paper stack, trader, slumped figure, just bad luck that one time! / this wasn't my year... crossed out, REPORT and STUDY papers with 90%, underperformance bar chart, FEE you BETTER PAY papers, investor asks Why am I paying extra to underperform?"),
 (7041, "Index investing", "chalkboard Index investing, red arrow with banknote and chart, index fund infographic, headband man with check, quote card attributed to John C. Bogle, investor with workers crossed out, BIG BUSINESS with banknotes, medal and briefcase, trader zooming and greying, FEE paper, faded woman"),
 (8338, "Robo advisors arrive", "briefcase, balance scale with TAX papers, chalkboard Robo Advisors, robot with flowchart bubble crossed out, medal with flowchart, Renaissance and Two Sigma logos, clock and backtest charts, + other strats / ALPHA, chefs (best I can do is canned), robot = computer + banknotes, advisors crossed out, robot boxing a Two Sigma character, Forget those lads / I can do it for you!, 1% a year crossed out, Wealthfront and Betterment, DOWNLOADS counter, 10 years ago... $2B / $80B, Earth and robot, $187 billion in 2017 / $2.8 TRILLION / $4.7 TRILLION!, block tower, grinning robot"),
 (11953, "Sponsor segment (Surfshark)", "yellow progress bar along the bottom edge; door Who is it?, Surfshark logo and chalkboard, laptop accidentally gave all my data, sleeping mascot wakes ready!, browser history crossed out and IP blurred, phones and laptops, key one account / go mad!, email screenshot, data thief, hey boss!, all in one!, caged YOUR DATA box, 30 day money back guarantee, surfshark.com/casualfinance and code CASUALFINANCE for 4 extra months!"),
 (14023, "Robo advisors: how they work and their limits", "chalkboard Robo advisors, grinning robot trust me I'm ok, robot with FOR SALE! sign, expectation: muscular robot vs reality: small robot, QUESTIONNAIRE with age? / income? / time horizon? / goals?, Sweet! / But in reality..., robot at chart board This could work for you!, CATEGORY buckets and briefcase, video clip of a man speaking, round table with What is BETA???, ACCESS with computer, orders and papers, flat-pack furniture with ?, excited man with globe, DOWNLOADS counter, door, 1% a year, airplane, BUY / SELL buttons, papers equal FREE!, Robo advisors = good or bad? / different!, COMMENT!, robot beside a cracking bank"),
 (18857, "End card", "white card: Subscribe for more Casual Finance with a YouTube mark and crossed-out social icons"),
]
rows = ['| Part | Frames | Seconds | States | OBSERVED content |', '|---|---|---|---|---|']
for i, (f0, name, desc) in enumerate(parts):
    f1 = (parts[i + 1][0] - 1) if i + 1 < len(parts) else LASTF
    rows.append(f'| {name} | f{f0}-f{f1} | {f0/fps:.1f}-{(f1+1)/fps:.1f} | {sid(f0)}-{sid(f1)} | {desc} |')
board = sum('chalkboard' in lab(r) or lab(r).startswith('board ') for r in st)
caps = sum(lab(r).startswith('caption') for r in st)
anim_states = sum('+ANIM' in r['entering_class'] for r in st)
spon = [r for r in st if 11953 <= int(r['start_frame']) <= 14022]
c2 = cad(15519, 15604); c3 = cad(3807, 3855)
anim = 'f800-f847 (crying trader with flying money), f1435-f1593 (walking turtle), f2097-f2185 (slow push-in on three men), f3807-f3855 (TV news clip), f3856-f3938 (genie fades in), f3939-f4032 (formula meme clip), f4685-f4735 and f4877-f4930 (money clips with flying banknotes), f5495-f5563 (speedster clip), f8040-f8193 (push-in and fade to grey), f10778-f10834 and f16746-f16806 (download counters climbing), f15519-f15604 (video clip of a man speaking), f16390-f16413 (chart darkens), f18753-f18856 (bank building cracks)'
body = '## 2. Structure (MEASURED frames; part boundaries are INFERRED from visuals plus ASR narration)\n' + '\n'.join(rows) + f"""

Reading: a {LASTF+1}-frame, {(LASTF+1)/fps:.1f} s explainer on quantitative investing and robo advisors, delivered as a stick-figure explainer with a recurring green chalkboard, handwritten captions and short inserted clips and photos. There are no chapter cards; captions such as Back in the day..., In the late 1980s..., By the early 2000s... and 10 years ago... mark time jumps. A sponsor segment (Surfshark) runs f11953-f14022 ({(14023-11953)/fps:.1f} s) with a yellow progress bar along the bottom edge; the ASR sponsor read starts at about 395 s and the return line is at about 466 s. The file ends on a {(LASTF-18857+1)/fps:.1f} s end card.

## 3. Shots and cut rhythm (MEASURED)
- {len(st)} visual states and {len(sh)} shots from {len(cuts)} hard cuts plus the opening shot; mean state {S.mean(sds):.2f} s, median {S.median(sds):.2f} s.
- Shot length: median {S.median(L)/fps:.2f} s, mean {S.mean(L)/fps:.2f} s, interquartile range {q[0]/fps:.2f}-{q[2]/fps:.2f} s; shortest {min(L)/fps:.2f} s ({mn['shot_id']}, f{mn['start_frame']}-f{mn['end_frame']}), longest {max(L)/fps:.2f} s ({mx['shot_id']}, f{mx['start_frame']}-f{mx['end_frame']}); {len(longs)} shots exceed 8 s ({longtxt}); {sum(l>=150 for l in L)} shots last 5 s or more; {len(shorts)} shots last 0.4 s or less.
- Encoder alignment: {len(cuts)-len(non)} of the {len(cuts)} hard cuts start on an I-frame ({100*(len(cuts)-len(non))/len(cuts):.1f} percent; {len(I)} I-frames in total, mean gap {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.2f} s). The {len(non)} that do not (f{', f'.join(map(str,non))}) were each viewed on native frames (sheets hid1 and hid2): all are one-frame replacements except f12087, where the dark door shape turns into the sponsor logo over a few frames.
- State classes (base class): CUT {base['CUT']}, POP_IN {base['POP_IN']}, POSE {base['POSE']}, START {base['START']}; {anim_states} states carry an ANIM suffix.
- Hard-cut size: grayscale changes above 25 levels at the cut frame run from {cutpx[0]:,} px to {cutpx[-1]:,} px (median {cutpx[len(cutpx)//2]:,}).
- Recurring scene types (states, from labels): chalkboard states {board}, caption states {caps}; {len(spon)} states fall inside the sponsor segment.
- Boundaries hidden on the last frame of multi-frame episodes, found by printing frames of 100,000 px or more inside long episodes and confirmed on native frames: f2274, f2352, f2449, f2688, f3856, f3939, f4033, f4736, f4931, f5564, f7165, f9367, f10835, f11953, f14023, f14025, f14810, f15605, f16639, f16807.

## 4. Motion and animation (MEASURED + OBSERVED)
- Episodes: {len(ep)} candidate change episodes, of which {n1} last one frame ({100*n1/len(n):.1f} percent), {n23} last two or three frames and {n4} last four frames or more (longest {max(n)} frames at f{bigeps[0][1]}). The ten longest start at f{', f'.join(str(b[1]) for b in bigeps)}.
- Pop-in rule: drawings, labels, bubbles, logos, checks, X marks and banknotes appear in one frame; groups build one item per step (banknotes every 4-10 frames, money bags, papers, logos), and words of a caption can appear one at a time (It transformed the industry, f5030-f5056).
- Camera scale (MEASURED, ORB feature matching with RANSAC between start+4 and end-3): {len(zm)} states of at least 25 frames measured. {len(zsig)} change scale by more than 0.002 at 100 inliers or more ({zsigtxt or 'none'}), {len(zflat)} are flat and {len(zlow)} have fewer than 100 inliers and are not reliable ({zlowtxt or 'none'}).
- Sponsor progress bar (MEASURED from decoded frames, rows 1068-1079, yellow pixels): 4 px wide at f11953, 518 px at f12500, 988 px at f13000, 1,458 px at f13500 and the full 1,920 px by f14000, so it grows about 0.94 px per frame.
- In-state animation (OBSERVED, ranges from frame_metrics): {anim}. The crying-trader shot has {c1[0]} of {c1[1]} frames changing by 3,000 px or more; the speaking-man clip {c2[0]} of {c2[1]}; the TV news clip {c3[0]} of {c3[1]}.
- Blinks: checks and arrows blink off and on for 4-5 frames (f5913-f5918, f7293-f7298, f8996, f18350-f18354).
- 30 fps constant frame rate ({LASTF+1} frames).

## 5. Art direction and graphics
- Palette (k-means, 8 colours over one frame per state, {len(st)} frames): """ + ', '.join(f"{c['hex']} {c['share_pct']} percent" for c in pal) + f""". Colour names are INFERRED from the swatches: white canvas dominant, beige office wall, near-black line, brown, sage green, dark grey and khaki.
- Style: black-outlined stick figures and flat props on white with hand-lettered captions; green chalkboard with a brown frame for terms; red for falling arrows and X marks, green for rising arrows, checks and banknotes; recurring cast (stick man, figure with orange tie, glasses figure, office workers, trader at a desk, investor with briefcase, grey robot, Surfshark mascot in the sponsor segment).
- Third-party material, OBSERVED: film stills, a TV news clip (CNBC), meme images and clips (stonks, formula meme), portrait photos, a speedster clip, a video clip of a man speaking outdoors, an underperformance bar chart, an index fund infographic (Personal Finance Club), a quote card (AZ Quotes), an investment calculator screenshot, backtest charts, an email screenshot and logos (Renaissance, Two Sigma, Adobe, Alphabet, Harvard crest, Wealthfront, Betterment, Surfshark). They belong to third parties; people in photographs and clips are not identified except by on-screen text.
- Text: captions, board text, labels and logo names were read from decoded frames; small body text in screenshots is only partly legible.

## 6. Object lifecycles (OBSERVED)
- Chalkboard: Story f991, Stories = Standard f1355, Random? / Statistical f2186-f2273, Quantitative Investing f2480, MATH > gut feelings f2825, THE MOST SUCCESSFUL IN HISTORY! f3324, Medallion fund = SUCCESS!!! f4931-f4986, And much more! f5381, Index investing f7041-f7063, Robo Advisors f8662-f8706, + other strats / ALPHA f9419-f9513, $187 billion to $4.7 TRILLION! f11279-f11586, Surfshark f12114 / f12694 / f13161 / f13527, Robo advisors f14025 / f15373 / f17715, good or bad? / different! f17902-f18008, ACCESS f16126-f16143.
- Grey robot: f8866, f9624, f9800, f10042 (boxing), f10263, f11220, f11809, f11911, f14085, f14199, f15079, f15605, f17010, f17682, f17797, f18279, f18542, f18681.
- Medal: f3151 (Medallion Fund), f4153, f4793, f5564 (good job), f9052, f9548.
- Download counters: f10778 (0 to 27,541), f16746 (0 to 29,508).

## 7. Attention hypotheses (INFERRED, no retention or CTR data)
1. A new visual state appears every {S.mean(sds):.1f} s on average and a hard cut every {S.mean(L)/fps:.1f} s; {n1} of {len(ep)} change episodes are single frames. ASR counts {nw:,} words over {span:.0f} s (about {nw/span*60:.0f} words per minute).
2. In {early} of {len(pairs)} phrase pairs the picture changes before the spoken word (median lead {abs(S.median(lags)):.2f} s); pairs match on-screen words to the same spoken word, and the lead may partly reflect ASR timing.
3. ASR gaps of 3 s or more: {agtxt}. The narration is continuous.
4. The progress bar shows the viewer how long the sponsor read lasts; whether it changes viewing behaviour is INFERRED and not measured.
5. The chalkboard returns for every new term and acts as a signpost for the argument.

## 8. Uncertainties and limits
- Audio was never heard; ASR (openai-whisper small.en) is provisional, so AV sign-off is BLOCKED. Phrase pairs ({len(pairs)} kept) were selected by a script that matches content words of each state's visible text to the nearest same spoken word within 2.5 s; 6 matches with a lag beyond 1.5 s were dropped and states with no match are not counted as unpaired.
- ASR event-to-nearest-word offsets ({e3} of {len(ev)} state starts within 0.3 s) are not evidence of sync: random times fall within 0.3 s of some word start {r3:.1f} percent of the time and within 0.1 s {r1:.1f} percent of the time in the random control.
- The 1 fps overview sheet set (36 sheets) was generated but not viewed. Coverage rests on the 60 episode change-crop sheets (all viewed), the gap check against frame_metrics, native-frame windows (hid1 and hid2) and 27 state sheets (all viewed). Inside clips and other animated states, per-frame changes are left to the ANIM class.
- People in photographs and clips are not identified; names come from on-screen text only.
- Screenshot body text is only partly transcribed.
- Changed-pixel counts are frame_metrics.csv full-resolution grayscale differences above 25 levels; episodes.csv and sheet-header counts use a different colour-difference measure.
- Camera scale values are net scale between two decoded frames; states with fewer than 100 inliers ({len(zlow)}) are reported as unreliable, not as zoom.
- Whether the file is an original upload, re-encode or edit export is not known. Part boundaries, pace claims and attention hypotheses are INFERRED.
"""
open(f'{ws}/build/report_body.md', 'w').write(body)
mods = f"""## Modules (original rebuild; derived from measured patterns)
1. **Cast and prop kit**: stick man, figure with orange tie, glasses figure, office workers, trader at desk, investor with briefcase, grey robot, chalkboard, medal, money bags, papers, ORDER boxes. Redraw as new original assets; do not trace the source.
2. **Hard-cut scene chain**: {len(cuts)} hard cuts, median shot {S.median(L)/fps:.1f} s ({min(L)/fps:.2f}-{max(L)/fps:.1f} s); {len(cuts)-len(non)} land on I-frames and {len(non)} do not.
3. **Chalkboard term frame**: {board} chalkboard states; swap the board text in place.
4. **One-frame pop-in builds**: {n1} of {len(ep)} episodes are one frame; build groups one item per step.
5. **Caption time jumps**: short handwritten captions for each era.
6. **Sponsor block with progress bar**: a yellow bar along the bottom edge that grows about 0.94 px per frame across the {(14023-11953)/fps:.0f} s segment; use your own sponsor and mascot.
7. **Third-party insert slot**: photos, clips, charts, logos and screenshots are replaced with licensed or self-made equivalents.
8. **Counters and blinks**: animated number counters and 4-5 frame blinks for emphasis.
9. **Mostly locked-off camera**: only a few scale changes ({len(zsig)} measured).
10. **End card**: white card with Subscribe for more, channel name, YouTube mark and crossed-out social icons held {(LASTF-18857+1)/fps:.1f} s.
11. **Codec note**: 30 fps constant frame rate, {len(I)} I-frames about every {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.1f} s on average.
"""
open(f'{ws}/build/modules.md', 'w').write(mods)
views = {
 "native_windows": [
  "hid1 rows: f2096-f2098, f2273-f2276, f2350-f2354, f2447-f2450, f2687-f2689, f3855-f3857, f3938-f3940, f4032-f4034, f4735-f4737, f4930-f4932, f5288-f5290, f5563-f5565, f7164-f7166, f9366-f9368, f10834-f10836, f11952-f11954, f14022-f14026, f14809-f14811, f15542-f15544, f15555-f15557, f15604-f15606, f15637-f15639, f16638-f16640, f16806-f16808",
  "hid2 rows: f1593-f1595, f2777-f2779, f3064-f3066, f3323-f3325, f7112-f7114, f10625-f10627, f11910-f11912, f12030-f12032, f12086-f12088, f15235-f15237, f17175-f17177"
 ],
 "stepped_sheets": [
  "overview 1 fps (36 sheets generated by sheets.py; NOT viewed, so they are not counted as visual coverage)",
  f"episode change-crop sheets epc_01-60 ({len(ep)} episodes: context frame with changed-pixel bbox, crop at start-1, crop at start; all 60 sheets viewed)",
  f"state_rep ({len(st)} states, 27 sheets, all viewed)"
 ],
 "episode_view": f"per episode: context frame at its first changed frame with the changed-pixel bbox, plus bbox crops at start-1 and start (adjacent decoded frames); every frame of 8,000 changed px or more outside animated states was compared with the state starts (gap check) and frames of 100,000 px or more inside long episodes were viewed natively, which found 20 hidden boundaries; {len(st)} states were placed in total",
 "text_gate": "PARTIAL_OPEN_LIMITATION (captions, board text, labels and logo names read from decoded frames; body text inside screenshots flagged not transcribed or quoted only in part; people in photographs and clips not identified)"
}
json.dump(views, open(f'{ws}/build/views.json', 'w'), indent=1)
print('written', len(body), len(mods)); print('zsig', len(zsig), zsigtxt); print('zlow', len(zlow), 'board', board, 'caps', caps, 'anim', anim_states, 'spon', len(spon))
print('longs', longtxt, 'agaps', agtxt, 'control', r1, r3, 'e3', e3, len(ev), 'early', early, len(pairs), c1[:2], c2[:2], c3[:2])
