import csv, json, sys, random, statistics as S, collections, os
ws = sys.argv[1]; fps = 24; LASTF = 14635
st = list(csv.DictReader(open(f'{ws}/visual_states.csv'))); sh = list(csv.DictReader(open(f'{ws}/shot_ledger.csv')))
man = json.load(open(f'{ws}/source_manifest.json')); I = set(man['iframe_indices'])
fm = {int(r['frame']): int(float(r['fullres_changed_px_thr25'])) for r in csv.DictReader(open(f'{ws}/tables/frame_metrics.csv'))}
zm = [x for x in csv.DictReader(open(f'{ws}/tables/zoom_measure.csv')) if x['scale_b_over_a'] not in ('', None)]
ep = list(csv.DictReader(open(f'{ws}/tables/episodes.csv')))
pal = json.load(open(f'{ws}/tables/palette.json'))['colors']
pairs = json.load(open(f'{ws}/build/phrase_pairs.json'))
asr = json.load(open(f'{ws}/audio/WCS1bK3KB3U_small_en.json'))
W = [(x['start'], x['end'], x['word'].strip()) for s in asr['segments'] for x in s['words']]; WS_ = sorted(x[0] for x in W)
sid = lambda f: next(r['visual_state_id'] for r in st if int(r['start_frame']) <= f <= int(r['end_frame']))
lab = lambda r: r['label'].lower()
base = collections.Counter(r['entering_class'].split('+')[0] for r in st)
cuts = [int(r['start_frame']) for r in st if r['entering_class'].startswith('CUT')]; non = [c for c in cuts if c not in I]
L = [int(s['end_frame']) - int(s['start_frame']) + 1 for s in sh]; q = S.quantiles(L, n=4)
mn = min(sh, key=lambda s: int(s['end_frame']) - int(s['start_frame'])); mx = max(sh, key=lambda s: int(s['end_frame']) - int(s['start_frame']))
longs = [s for s in sh if int(s['end_frame']) - int(s['start_frame']) + 1 > 192]
longtxt = '; '.join(f"{s['shot_id']} f{s['start_frame']}-f{s['end_frame']} ({(int(s['end_frame'])-int(s['start_frame'])+1)/fps:.1f} s)" for s in longs)
shorts = [s for s in sh if int(s['end_frame']) - int(s['start_frame']) + 1 <= 10]
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
c1 = cad(3130, 4338); gtxt = lambda c: ', '.join(f'{k} frame{"s" if k > 1 else ""} x{v}' for k, v in c[2])
ev = [int(r['start_frame']) / fps for r in st]; near = lambda t: min(abs(t - w) for w in WS_); e3 = sum(near(t) <= 0.3 for t in ev)
random.seed(7); rnd = [random.uniform(0, 603) for _ in range(20000)]
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
 (0, "Hook: April 7th post and the platform stock", "stick man, handwritten date April 7th, 5:32 PM, president caricature at a desk beside a long social post, numeral cards 1. and 2., blue app-logo character dancing (I'm SO good omg!!!) with rival social-app characters, falling stock chart (who's gonna tell him?), investor with briefcase"),
 (417, "The next day: ceasefire relief rally", "TradingView charts with red arrow and green circle, article text on index gains with highlights and red circle, green arrow with a presenter image, A few weeks later..., deal-book caricature, angry caricature with a CNBC headline, Breaking News newspaper, relief-rally article screenshots, two figures at a rising chart, Relief rally! crossed out"),
 (1153, "What is going on? War and selling", "chalkboard What is going on?, map characters in boxing gloves, Wall St sign, reporter, On February 28th..., country silhouettes, targeting laptop, portrait with Iran flag, Strait of Hormuz map crossed out, CBS correction headline, heatmap and burning-office gif, 401K character, Panik, Goldman Sachs/Yahoo Finance article, Investopedia prime broker definition, Goldman telescope character, Prime Book chart, Hedgeweek leverage note, chalkboard Macro ETFs / SPY / QQQ, March 19th"),
 (3130, "Interview clip: oil shock warning", "third-party interview clip (guest, interviewer, split screen) with burned-in word-highlighted subtitles and a source line, ending in a teal and yellow bar wipe"),
 (4349, "Six weeks later: the rally", "Six weeks later..., stick man with cash, bear and SELL button, caricature with giant post bubble, money-gun photo, green heatmap, stonks tiles, TradingView charts, Relief rally newspaper reader, torn newspaper, Windward logo, robot with GPS tablets and satellite, Windward vessel map, chalkboard 96% decrease and 130 daily transits, dove with fallen olive branch, green heatmap with ???"),
 (6005, "Short squeeze explained", "meme-stock collage (GameStop, sketch-show orange-slices clip, Doge coin), chalkboard What the heck is a short squeeze?, Shorting a stock = with share boxes and banknotes, bought initially for / bought back for, share-and-dollar icon with a green arrow drawing on, phone call Do something about this or else!, or abort the mission!, crowd of buyers raising banknotes"),
 (7124, "CTAs and mechanical trading", "orange-slices clip, chalkboard April 8th and HIGHEST since 2020, V-shaped TradingView chart, domino video clip, flowchart icon and robot, chalkboard CTAs / Commodity Trading Advisors, animated sitcom courtroom clip with a pitcher mascot labelled CTAs, Rules scroll, Earth crossed out, Short! and Long! bubbles, chalkboard Mechanical trading, Goldman Sachs CTAs $30 BILLION (right before ceasefire), S&P 500 with warning sign, $40 billion will do"),
 (8652, "Hedge fund buying and the options market", "dark article Historic scale of hedge fund buying with $86 billion circled, briefcases, money-throwing clip, single domino, THE OPTIONS MARKET, Investopedia delta-neutral list, phone man, hoodie trader, SpotGamma logo and negative gamma chart, chalkboard Stabilizing / Pro-cyclical, share icon arrows, dominoes falling, Omg relief rally!!!"),
 (9760, "History rhymes: 2018 and 2024", "Goldman popcorn character and film still, red cycle arrows, scrolling timeline of years, December 2018..., not stonks meme, Federal Reserve with percent and arrow, photo with patient bubble, Dow Jones Industrial Average, starburst, Dow soars article, August 2024..., Bank of Japan with 17 years, channel community post (Japan character, yen), Nikkei 225 -12% / +10%"),
 (10737, "Market structure then and now", "cycle arrows, 20 years ago..., office traders, A technology startup? / five cents and some gum, ICI fund table with circled values, robot beep boop, chalkboard Market cap, BIG BUSINESS tower, Magnificent Seven chart with company logos and 33%, chalkboard Hedge funds / Few funds, top-hat tycoon with strings, fund logos and AUM chart, Millennium risk excerpt, round table So uh..., Federal Reserve with knife, strait map with question marks, film clip Sell it all / Today, Cboe options volume text, $2 TRILLION meme, banknote exchange arrows"),
 (13071, "Conclusion: no thinking", "hoodie trader, share boxes and banknote hands, chalkboard no thinking / BUY SELL BUY SELL BUY!, dollar sign, TV host SELL / BUY photo, chalkboard April 8th, Efficient Market Hypothesis card crossed out, photo of two men at a laptop, NEWS reader, Markets explained for dum dums!!!, SUBSCRIBE!, newspaper with eyes, heart (Market my beloved), quote card attributed to Warren Buffett... probably, crossed-out heart, cycle arrows, two puzzled figures"),
 (14483, "End card", "white card: Subscribe for more Casual Finance with a YouTube mark and crossed-out social icons"),
]
rows = ['| Part | Frames | Seconds | States | OBSERVED content |', '|---|---|---|---|---|']
for i, (f0, name, desc) in enumerate(parts):
    f1 = (parts[i + 1][0] - 1) if i + 1 < len(parts) else LASTF
    rows.append(f'| {name} | f{f0}-f{f1} | {f0/fps:.1f}-{(f1+1)/fps:.1f} | {sid(f0)}-{sid(f1)} | {desc} |')
D = lambda r: r['literal_description'].lower()
board = sum('chalkboard' in lab(r) or lab(r).startswith('board text') for r in st)
writes = sum('writes on' in lab(r) for r in st); bn = sum('breaking news' in lab(r) for r in st)
shareico = sum('share icon' in lab(r) for r in st); anim_states = sum('+ANIM' in r['entering_class'] for r in st)
clipcuts = [int(r['start_frame']) for r in st if 3130 <= int(r['start_frame']) <= 4338 and r['entering_class'].startswith('CUT')]
anim = 'f1827-f1974 (burning-office gif), f3130-f4338 (interview clip, then a bar wipe f4339-f4348), f6005-f6037, f7124-f7157 and f9581-f9603 (sketch-show orange-slices clip), f7295-f7351 (domino video), f7536-f7794 (animated sitcom courtroom clip), f8862-f8941 (money-throwing clip), f9882-f9973, f10803-f10918 and f14196-f14302 (rotating cycle arrows), f10247-f10262 (starburst flashing every third frame), f6438, f6630, f6994, f9484 and f9526 (green arrow draws on, about 10-20 frames each)'
c2 = cad(7536, 7794); c3 = cad(8862, 8941); c4 = cad(10247, 10262, 100000)
zsig_lab = '; '.join(f"f{z[1]['state_start']} {sid(int(z[1]['state_start']))} {lab(next(r for r in st if r['start_frame']==z[1]['state_start']))}" for z in zsig)
body = '## 2. Structure (MEASURED frames; part boundaries are INFERRED from visuals plus ASR narration)\n' + '\n'.join(rows) + f"""

Reading: a {LASTF+1}-frame, {(LASTF+1)/fps:.1f} s explainer on why stocks rallied during a war, delivered as a stick-figure explainer with handwritten captions, a recurring green chalkboard and many inserted screenshots, memes and video clips. There are no chapter cards; date captions written on in white (April 7th, A few weeks later..., On February 28th..., March 19th, Six weeks later..., December 2018..., August 2024..., 20 years ago...) mark the time jumps. A third-party interview clip runs {(4339-3130)/fps:.1f} s (f3130-f4338). No sponsor segment was seen and the ASR has no sponsor read. The file ends on a {(LASTF-14483+1)/fps:.1f} s end card.

## 3. Shots and cut rhythm (MEASURED)
- {len(st)} visual states and {len(sh)} shots from {len(cuts)} hard cuts plus the opening shot; mean state {S.mean(sds):.2f} s, median {S.median(sds):.2f} s.
- Shot length: median {S.median(L)/fps:.2f} s, mean {S.mean(L)/fps:.2f} s, interquartile range {q[0]/fps:.2f}-{q[2]/fps:.2f} s; shortest {min(L)/fps:.2f} s ({mn['shot_id']}, f{mn['start_frame']}-f{mn['end_frame']}), longest {max(L)/fps:.2f} s ({mx['shot_id']}, f{mx['start_frame']}-f{mx['end_frame']}); {len(longs)} shots exceed 8 s ({longtxt}); {sum(l>=120 for l in L)} shots last 5 s or more; {len(shorts)} shots last 10 frames or less.
- Encoder alignment: {len(cuts)-len(non)} of the {len(cuts)} hard cuts start on an I-frame ({100*(len(cuts)-len(non))/len(cuts):.1f} percent; {len(I)} I-frames in total, mean gap {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.2f} s). The {len(non)} that do not (f{', f'.join(map(str,non))}) were each viewed on native frames (sheets hid1-hid4): all are one-frame replacements with no dissolve.
- The interview clip contains its own camera cuts, counted as states: f{', f'.join(map(str, clipcuts))}.
- State classes (base class): CUT {base['CUT']}, POP_IN {base['POP_IN']}, POSE {base['POSE']}, START {base['START']}; {anim_states} states carry an ANIM suffix for animation inside the state.
- Hard-cut size: grayscale changes above 25 levels at the cut frame run from {cutpx[0]:,} px to {cutpx[-1]:,} px (median {cutpx[len(cutpx)//2]:,}); small values are cuts between two mostly white drawings.
- Recurring scene types (states, from labels): chalkboard states {board}, write-on captions {writes}, Breaking News newspaper {bn}, share-and-dollar icon with a rising arrow {shareico}.
- Cuts hidden on the last frame of multi-frame episodes, found by the gap check and confirmed on native frames: f279 (pop-in), f768, f1907, f1975, f2092, f2787, f3029, f4349, f4815, f5142, f5432, f6038, f6405, f7158, f7352, f7555, f7607, f7795, f8942, f9604, f9882, f9974, f10263, f11103, f12720, f13488, f13618, f13727, f14059, f14303, f14360.

## 4. Motion and animation (MEASURED + OBSERVED)
- Episodes: {len(ep)} candidate change episodes, of which {n1} last one frame ({100*n1/len(n):.1f} percent), {n23} last two or three frames and {n4} last four frames or more (longest {max(n)} frames at f{bigeps[0][1]}). The ten longest start at f{', f'.join(str(b[1]) for b in bigeps)}.
- Pop-in rule: drawings, labels, bubbles, logos, circles, X marks and arrows appear in one frame; lists and groups build one item per step (stonks tiles every 4-8 frames f4885-f4933; banknote hands f6949-f6975 and f13177-f13203; company logos f11729-f11751).
- Write-on: dates and time captions are written stroke by stroke over 8-45 frames (for example f6-f39, f768 onward, f1493 onward).
- Camera scale (MEASURED, ORB feature matching with RANSAC between start+4 and end-3): {len(zm)} states of at least 25 frames measured. {len(zsig)} change scale by more than 0.002 at 100 inliers or more ({zsigtxt or 'none'}), {len(zflat)} are flat and {len(zlow)} have fewer than 100 inliers and are not reliable ({zlowtxt or 'none'}). The scale changes sit on the Wall St sign (f1315), the reporter (f1370), the cash close-up (f4492) and the money-gun photo (f4739, f4778); elsewhere the camera is locked off.
- In-state animation (OBSERVED, ranges from frame_metrics): {anim}. Inside the interview clip {c1[0]} of {c1[1]} frames change by 3,000 px or more; the sitcom clip {c2[0]} of {c2[1]}; the money-throwing clip {c3[0]} of {c3[1]}. The starburst flashes on every third frame (gaps {gtxt(c4)}).
- Loops: the president caricature waves its arms and the app-logo character dances in an 8-frame loop (f67-f115, f197-f279).
- Transition: one graphic wipe (teal then yellow horizontal bars, f4339-f4348) ends the interview clip; no dissolve was seen at any hard cut viewed natively.
- 24 fps constant frame rate ({LASTF+1} frames).

## 5. Art direction and graphics
- Palette (k-means, 8 colours over one frame per state, {len(st)} frames): """ + ', '.join(f"{c['hex']} {c['share_pct']} percent" for c in pal) + f""". Colour names are INFERRED from the swatches: white canvas dominant, near-black line, beige, dark brown-grey, olive grey and accent colours.
- Style: black-outlined stick figures and flat props on white with hand-lettered captions; a green chalkboard with a brown frame for terms; red for falling arrows, circles and X marks; green for rising arrows and banknotes; a recurring cast (stick man, investor with glasses and briefcase, short seller with green tie, man on a corded phone, hoodie trader in sunglasses, grey robot, Goldman Sachs card character with telescope or popcorn).
- Third-party material, OBSERVED: social post and stock chart screenshots, TradingView charts, news and article screenshots (sources named on screen include CNBC, CBS, Goldman Sachs/Yahoo Finance, GuruFocus, Hedgeweek, Windward, Bloomberg, ICI, Cboe, MacroMicro, Investopedia and Quant Enthusiasts Substack), company logos, a portrait photo with flag, photos and memes (Panik, stonks, not stonks, money-gun photo, man on cash, TV host), a burning-office gif, a domino video, an interview clip, an animated sitcom clip, a sketch-show clip, a film clip and a channel community post. They belong to third parties; people in photographs are not identified except by on-screen text.
- Text: captions, board text, labels and headlines were read from decoded frames; body text inside articles, tables and charts is only partly legible and quoted only in part.

## 6. Object lifecycles (OBSERVED)
- Chalkboard: What is going on? f1153, We're NOT guessing! f2215, Macro ETFs / SPY / QQQ f2879-f2949, 96% decrease / 130 daily transits f5538-f5659, short squeeze f6067, April 8th / HIGHEST since 2020 f7158-f7224, CTAs f7430-f7467, Mechanical trading f8135, Stabilizing / Pro-cyclical f9390-f9465 and f9604-f9623, Market cap f11577, Hedge funds / Few funds f12050-f12102, no thinking / BUY SELL f13275-f13386, April 8th f13488.
- Share-and-dollar icon with green arrow and banknote pile: f6438, f6630, f6994, f9484, f9526.
- Hoodie trader with red chart: f9177, f9505, f9637, f13100.
- Breaking News newspaper: f928, f1108 (crossed f1128), f5210 (torn f5222), f5771, f7887 (crossed f7901), f9738, f13801.
- Orange-slices clip: f6005 (collage), f7124, f9581.

## 7. Attention hypotheses (INFERRED, no retention or CTR data)
1. A new visual state appears every {S.mean(sds):.1f} s on average and a hard cut every {S.mean(L)/fps:.1f} s; {n1} of {len(ep)} change episodes are single frames. ASR counts {nw:,} words over {span:.0f} s (about {nw/span*60:.0f} words per minute).
2. In {early} of {len(pairs)} phrase pairs the picture changes before the spoken word (median lead {abs(S.median(lags)):.2f} s); pairs match on-screen words to the same spoken word, and the lead may partly reflect ASR timing.
3. ASR gaps of 3 s or more: {agtxt}. The single gap falls inside the animated sitcom clip (f7536-f7794); what is heard there is UNAVAILABLE because audio was not heard.
4. Date write-on captions act as signposts for the time jumps in the story; the chalkboard returns for each new term.
5. Third-party clips and memes recur through the video (see section 4) and may work as comic resets; their purpose is INFERRED.

## 8. Uncertainties and limits
- Audio was never heard; ASR (openai-whisper small.en) is provisional, so AV sign-off is BLOCKED. Phrase pairs ({len(pairs)} kept) were selected by a script that matches content words of each state's visible text to the nearest same spoken word within 2.5 s; 8 matches with a lag beyond 1.5 s were dropped and states with no match are not counted as unpaired.
- ASR event-to-nearest-word offsets ({e3} of {len(ev)} state starts within 0.3 s) are not evidence of sync: random times fall within 0.3 s of some word start {r3:.1f} percent of the time and within 0.1 s {r1:.1f} percent of the time in the random control.
- The 1 fps overview sheet set (53 sheets) was generated but not viewed. Coverage rests on the 53 episode change-crop sheets (all viewed), the gap check against frame_metrics, native-frame windows (hid1-hid4) and 22 state sheets (all viewed). Inside the interview clip only frames of 300,000 px or more were checked for camera cuts; inside the other clips and loops, per-frame changes are left to the ANIM class.
- People in photographs and clips are not identified; names come from on-screen text only.
- Article, chart, table and UI body text is only partly transcribed.
- Changed-pixel counts are frame_metrics.csv full-resolution grayscale differences above 25 levels; episodes.csv and sheet-header counts use a different colour-difference measure.
- Camera scale values are net scale between two decoded frames; states with fewer than 100 inliers ({len(zlow)}) are reported as unreliable, not as zoom.
- Whether the file is an original upload, re-encode or edit export is not known. Part boundaries, pace claims and attention hypotheses are INFERRED.
"""
open(f'{ws}/build/report_body.md', 'w').write(body)
mods = f"""## Modules (original rebuild; derived from measured patterns)
1. **Cast and prop kit**: stick man, investor with glasses and briefcase, short seller with green tie, phone man, hoodie trader, grey robot, card character with telescope, newspaper, share boxes, banknotes, dominoes, chalkboard. Redraw as new original assets; do not trace the source.
2. **Hard-cut scene chain**: {len(cuts)} hard cuts, median shot {S.median(L)/fps:.1f} s ({min(L)/fps:.2f}-{max(L)/fps:.1f} s); {len(cuts)-len(non)} land on I-frames and {len(non)} do not, so author cuts as true edits.
3. **Chalkboard term frame**: pointer-stick figure beside a green board whose text swaps in place; {board} chalkboard states.
4. **Date write-on captions**: dates and time jumps written stroke by stroke on white; {writes} write-on states.
5. **One-frame pop-in vocabulary**: bubbles, labels, circles, X marks, arrows and logos in a single frame; {n1} of {len(ep)} episodes are one frame.
6. **Recurring diagram**: share-and-dollar icon, banknote and a green arrow that draws on, then a banknote pile.
7. **Third-party insert slot**: screenshots, charts, memes, photos and clips are replaced with licensed or self-made equivalents; never copy the source items.
8. **Clip handling**: long interview clip with burned-in subtitles ended by a bar wipe; short loops for meme clips.
9. **Locked-off camera with rare moves**: scale changes only on a few close-ups (street sign, reporter, cash, photo).
10. **End card**: white card with Subscribe for more, channel name, YouTube mark and crossed-out social icons held {(LASTF-14483+1)/fps:.1f} s.
11. **Codec note**: 24 fps constant frame rate, {len(I)} I-frames about every {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.1f} s on average.
"""
open(f'{ws}/build/modules.md', 'w').write(mods)
views = {
 "native_windows": [
  "hid1 rows: f278-f280, f767-f769, f1906-f1908, f1974-f1976, f2091-f2093, f2412-f2414, f2786-f2788, f3028-f3030, f3399-f3401, f3530-f3532, f3566-f3568, f3681-f3683, f3737-f3739, f3866-f3868, f4235-f4237, f4338-f4350",
  "hid2 rows: f4814-f4816, f5141-f5143, f5431-f5433, f6037-f6039, f6404-f6406, f7157-f7159, f7351-f7353, f7408-f7410, f7554-f7556, f7606-f7608, f7794-f7796, f8941-f8943, f9603-f9605, f9881-f9883, f9973-f9975, f10262-f10264, f10918-f10920, f11102-f11104, f12304-f12306, f12719-f12721, f13439-f13441, f13487-f13489, f13617-f13619, f13726-f13728, f14058-f14060, f14302-f14304, f14359-f14361",
  "hid3 rows: f175-f177, f478-f480, f1195-f1197, f1492-f1494, f6004-f6006, f7626-f7628, f7997-f7999, f8413-f8415, f9737-f9739, f10025-f10027, f10384-f10386, f11484-f11486, f12343-f12345, f12748-f12750, f12798-f12800, f13993-f13995; hid4 rows: f446-f447, f463-f466, f474-f476"
 ],
 "stepped_sheets": [
  "overview 1 fps (53 sheets generated by sheets.py; NOT viewed, so they are not counted as visual coverage)",
  f"episode change-crop sheets epc_01-53 ({len(ep)} episodes: context frame with changed-pixel bbox, crop at start-1, crop at start; all 53 sheets viewed)",
  f"state_rep ({len(st)} states, 22 sheets, all viewed)"
 ],
 "episode_view": f"per episode: context frame at its first changed frame with the changed-pixel bbox, plus bbox crops at start-1 and start (adjacent decoded frames); every frame of 8,000 changed px or more outside the interview clip was compared with the state starts (gap check) and frames of 100,000 px or more inside long episodes were viewed natively, which found {31} hidden boundaries; {len(st)} states were placed in total",
 "text_gate": "PARTIAL_OPEN_LIMITATION (captions, board text, labels, headlines and logo names read from decoded frames; body text inside articles, tables, charts and UI screenshots flagged not transcribed or quoted only in part; people in photographs and clips not identified)"
}
json.dump(views, open(f'{ws}/build/views.json', 'w'), indent=1)
print('written', len(body), len(mods)); print('zsig', len(zsig), 'zflat', len(zflat), 'zlow', len(zlow))
print('board', board, 'writes', writes, 'bn', bn, 'share', shareico, 'anim', anim_states, 'clipcuts', clipcuts)
print('longs', longtxt, 'agaps', agtxt, 'control', r1, r3, 'e3', e3, len(ev), 'early', early, len(pairs), c1[:2], c2[:2], c3[:2], c4)
