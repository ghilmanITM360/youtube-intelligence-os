import csv, json, sys, random, statistics as S, collections, os
ws = sys.argv[1]; fps = 30; LASTF = 16801
st = list(csv.DictReader(open(f'{ws}/visual_states.csv'))); sh = list(csv.DictReader(open(f'{ws}/shot_ledger.csv')))
man = json.load(open(f'{ws}/source_manifest.json')); I = set(man['iframe_indices'])
fm = {int(r['frame']): int(float(r['fullres_changed_px_thr25'])) for r in csv.DictReader(open(f'{ws}/tables/frame_metrics.csv'))}
zm = [x for x in csv.DictReader(open(f'{ws}/tables/zoom_measure.csv')) if x['scale_b_over_a'] not in ('', None)]
ep = list(csv.DictReader(open(f'{ws}/tables/episodes.csv')))
pal = json.load(open(f'{ws}/tables/palette.json'))['colors']
pairs = json.load(open(f'{ws}/build/phrase_pairs.json'))
asr = json.load(open(f'{ws}/audio/hbsYaLaN_F8_small_en.json'))
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
txtcards = [r for r in st if lab(r).startswith('text card')]
zr = []
for x in zm:
    d = float(x['scale_b_over_a']) - 1; dt = (int(x['frame_b']) - int(x['frame_a'])) / fps
    zr.append((abs(d), d / dt, x))
zsig = [z for z in zr if z[0] > 0.002 and int(z[2]['inliers']) >= 100]
zlow = [z for z in zr if int(z[2]['inliers']) < 100]
zflat = [z for z in zr if z[0] <= 0.002 and int(z[2]['inliers']) >= 100]
zlowtxt = '; '.join(f"f{z[2]['state_start']}-f{z[2]['state_end']} ({z[2]['inliers']} inliers, scale {float(z[2]['scale_b_over_a']):.3f})" for z in zlow)
def cad(a, b, thr=3000):
    ch = [f for f in range(a, b + 1) if fm[f] >= thr]
    g = collections.Counter(y - x for x, y in zip(ch, ch[1:]))
    return len(ch), b - a + 1, sorted(g.items())
c1 = cad(2470, 2564); c2 = cad(2566, 2616)
gtxt = lambda c: ', '.join(f'{k} frame{"s" if k > 1 else ""} x{v}' for k, v in c[2])
ev = [int(r['start_frame']) / fps for r in st]
near = lambda t: min(abs(t - w) for w in WS_)
e3 = sum(near(t) <= 0.3 for t in ev)
random.seed(7); rnd = [random.uniform(0, 560) for _ in range(20000)]
r1 = 100 * sum(near(t) <= 0.1 for t in rnd) / len(rnd); r3 = 100 * sum(near(t) <= 0.3 for t in rnd) / len(rnd)
if os.path.exists(f'{ws}/tables/phrase_alignment_summary.json'):
    _p = json.load(open(f'{ws}/tables/phrase_alignment_summary.json')); r1 = 100 * _p['random_within_0_1']; r3 = 100 * _p['random_within_0_3']
lags = sorted(f / fps - t for f, w, t in pairs); early = sum(l < 0 for l in lags)
nw = len(W); span = max(x[1] for x in W)
agaps = [(int(W[i][1] * fps), int(W[i + 1][0] * fps), W[i + 1][0] - W[i][1]) for i in range(len(W) - 1) if W[i + 1][0] - W[i][1] >= 3.0]
agtxt = '; '.join(f'f{a}-f{b} ({g:.1f} s)' for a, b, g in agaps)
def frames(sub, cls='CUT'):
    return [int(r['start_frame']) for r in st if sub in lab(r) and r['entering_class'].startswith(cls)]
ftxt = lambda a: ', '.join(f'f{x}' for x in a)
def burst(a, b):
    return [(int(e['start_frame']), int(e['end_frame']) - int(e['start_frame']) + 1) for e in ep if a <= int(e['start_frame']) <= b and int(e['end_frame']) > int(e['start_frame'])]
scroll = burst(12600, 12730)
bigeps = sorted([(int(e['end_frame']) - int(e['start_frame']) + 1, int(e['start_frame'])) for e in ep])[-10:][::-1]
parts = [
 (0, "Hook: Crypto card, Tinder gag and the thesis", "Crypto. card, Bitcoin over a city skyline, protest crowd, figure saying I can make you rich, restaurant host with an Applebee's sign, Tinder profile that gains the captions Entrepreneur and D2D Sales, text cards (So yeah..., If you can't tell already..., I Hate Crypto., And by the end of this video...), title Let's Expose Crypto, Jenga tower The Crypto Industry"),
 (880, "Chapter 1 (The Promise vs Reality): history and the utopia story", "chapter card, text card, Crypto History 101 chalkboard, 1983 card, newspaper portrait, eCash panel, canvasser at a grocery store, 2009 card, hooded Satoshi Nakamoto figure, Welcome to Utopia island, Statue of Liberty (torch, then rude gesture), Decentralized card that grows to three lines, At least that was the promise... and If you fast-forward to the present... cards"),
 (2353, "Bitcoin as a currency: usage claims and why it fails", "To the Moon thought bubble that turns into an angry figure by a burning bin, two third-party animated TV clips with Bitcoin overlays, sailor under a Bitcoin moon, museum case (crossed out), jeweller, map with a red circle, Rent Overdue door, business-statistics slide, dark dashboard and calculation screenshot, podium announcement, whisper gag, text cards As a currency... to The Reason: with three bullets, lawn-with-scissors, checkout at 1 percent, boardroom, rollercoaster with a gold bar, cave people with a nugget, root-beer bar, Financial Freedom Plan scroll that morphs into a 3D world-map banner, crypto casino"),
 (5349, "Chapter 2 (The Crypto Graveyard): speculative asset, volatility and expert quotes", "chapter card, text cards (So if Crypto is just a speculative asset..., Surely it's at least a good investment?, Right???, Wrong.), Annual Volatility bar chart with handwritten 60%, 15% and 4x the Volatility, boardroom with red arrows, CNBC article slide, Why? card, trophy podium World's Dumbest Investment, article cards for Buffett, Dimon and Schiff with caricatures, mound of cash, Like a gamble. card, casino, Bitcoin price history chart, sailing ship, meme-coin chart, Congratulations, Future Investors! stage (Delusional added)"),
 (7740, "Dumb Money, dead coins and rug pulls", "roulette table with a Dumb Money sign that swaps to Discord, third-party animated TV clip (Homer-style figure, forest pan to a casino hut), detective Let me prove it to you, CoinGecko logo, price table and 7 million listings card, report card (3.6 million died) with a red ellipse, courtroom with Asset Claims, dark room with a We're pivoting message, Rug Pull coin figure, ship and iceberg, Rug Pull with red arrows, How did the Crypto industry address this? card"),
 (9387, "Stablecoins: Terra and Luna", "StableCoins cards, Luna and Terra coin graphics with braces and labels, dollar bill, closed bank (Crypto Savings & Trust, 2022), balance scale, handwritten When Terra fell / rose above $1 slides, Clever in theory. / Disastrous in practice. cards, rope snap, cliff explosion, Safe and Reliable crossed out, dark Wikipedia excerpt, Regulators called it... card, report card"),
 (11391, "Exchanges: FTX, Alameda and the DraftKings analogy", "Surely the crypto exchanges are safe right? card, FTX logo, castle on a hill, NYSE approximately FTX, DON'T MISS OUT poster, press photo at a microphone, arena photo, BlackRock and Sequoia wordmarks, dark search results, portrait photo, gallery frame The Face of Trust, white-knight card, Fortune cover, Sequoia website with scrolling, All in on Sam card, bubbles of coin logos, Alameda chart and logo (BUSTED), burning office with Balance Sheet, John J. Ray III card, MoneyWatch article, family on a couch (Business Plan), DraftKings logo and app screenshot"),
 (14121, "Chapter 3 (Where Do We Go Now?): graveyard and the closing argument", "chapter card, repeats of report card, Luna and Terra, FTX logo, ship with FTX iceberg, tombstone graveyard, closed bank, man with an empty box, onion, cloaked figure with a coin and the Crypto Industry machine, No real-world utility list, ferris wheel, PUMP and DUMP chart, banquet table, shrugging figure, forum post, blockchain diagram, burning scholar with a scroll, roulette table (Discord), HOW CRYPTO WORKS chalkboard, It's the: list (Same lies, Same greed, Same blind optimism), desert mirage"),
 (16647, "End card", "white card: Subscribe for more Casual Finance with a YouTube mark, crossed-out social icons and a SUBSCRIBE button"),
 (16800, "Black frames", "two full black frames at the end of the file"),
]
rows = ['| Part | Frames | Seconds | States | OBSERVED content |', '|---|---|---|---|---|']
for i, (f0, name, desc) in enumerate(parts):
    f1 = (parts[i + 1][0] - 1) if i + 1 < len(parts) else LASTF
    rows.append(f'| {name} | f{f0}-f{f1} | {f0/fps:.1f}-{(f1+1)/fps:.1f} | {sid(f0)}-{sid(f1)} | {desc} |')
body = f'''## 2. Structure (MEASURED frames; part boundaries are INFERRED from visuals plus ASR narration)
''' + '\n'.join(rows) + f'''

Reading: a {LASTF+1}-frame, {(LASTF+1)/fps:.1f} s essay arguing that crypto is a scam. It has three chapter cards (f880, f5349, f14121); the hook before the first card and the closing run after the third are part of the same structure. No sponsor segment was seen and no sponsor read was found in the ASR. The video ends on a {(16799-16647+1)/fps:.1f} s end card and two black frames. The visual register is hand-drawn stick-figure vector on near-white, mixed with full-bleed illustrated scenes, two sets of third-party animated TV clips, photographs, article and app screenshots, charts and text-only cards.

## 3. Shots and cut rhythm (MEASURED)
- {len(st)} visual states and {len(sh)} shots from {len(cuts)} hard cuts plus the opening shot; mean state {S.mean(sds):.2f} s, median {S.median(sds):.2f} s.
- Shot length: median {S.median(L)/fps:.2f} s, mean {S.mean(L)/fps:.2f} s, interquartile range {q[0]/fps:.2f}-{q[2]/fps:.2f} s; shortest {min(L)/fps:.2f} s ({mn['shot_id']}, f{mn['start_frame']}-f{mn['end_frame']}, the two black frames), longest {max(L)/fps:.2f} s ({mx['shot_id']}, f{mx['start_frame']}-f{mx['end_frame']}); {len(longs)} shots exceed 10 s ({longtxt}), all three are runs of text swaps or a held chart in one shot; {sum(l>=150 for l in L)} shots last 5 s or more; {len(shorts)} shots last 1 s or less.
- Encoder alignment: {len(cuts)-len(non)} of the {len(cuts)} hard cuts start on an I-frame ({100*(len(cuts)-len(non))/len(cuts):.1f} percent; {len(I)} I-frames in total, mean gap {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.2f} s). The {len(non)} cuts that do not (f{', f'.join(map(str,non))}) were viewed on native frames (winE, winG rows): each is a one-frame replacement with no dissolve or smear.
- State classes (base class of each state): CUT {base['CUT']}, POP_IN {base['POP_IN']}, TEXT_SWAP {base['TEXT_SWAP']}, POSE {base['POSE']}, START {base['START']}; no FADE_IN. Of the {len(ep)} change episodes, every one starts within one frame of a state start or inside a state that carries its own motion class (MICRO or ANIM suffix).
- Hard-cut size: grayscale changes above 25 levels at the cut frame run from {cutpx[0]:,} px to {cutpx[-1]:,} px (median {cutpx[len(cutpx)//2]:,}); the smaller ones are cuts between two mostly white pages.
- Text-only cards: {len(txtcards)} states open on a one-line card (centred hand-lettered text on white); {base['TEXT_SWAP']} states replace or add text, mostly list lines and card swaps; some cards stack up to three or four lines.
- Chapter cards: f880 (Chapter 1, The Promise vs Reality, 4.6 s), f5349 (Chapter 2, The Crypto Graveyard, 4.6 s), f14121 (Chapter 3, Where Do We Go Now?, 4.7 s); each is a hard cut in and a hard cut out.

## 4. Motion and animation (MEASURED + OBSERVED)
- Episodes: {len(ep)} candidate change episodes, of which {n1} last one frame ({100*n1/len(n):.1f} percent), {n23} last two or three frames and {n4} last four frames or more (longest {max(n)} frames at f{bigeps[0][1]}). The long ones are animation inside a state, not cuts: the ten longest start at f{', f'.join(str(b[1]) for b in bigeps)}.
- Pop-in rule: text lines, labels, circles, arrows, braces and logos appear in one frame. List lines are added at spaced intervals: Decentralized, Free from government, Salvation from greedy banks at f1973, f2008, f2044 (gaps 35, 36 frames); The Reason bullets at f4013, f4058, f4109 (gaps 45, 51); No real-world utility, No intrinsic value, No trust at f15069, f15128, f15167 (gaps 59, 39); It's the: list at f16322, f16334, f16364, f16402 (gaps 12, 30, 38); Safe and Reliable then a red X at f10916, f10932, f10953 (gaps 16, 21).
- Camera scale (MEASURED, ORB feature matching with RANSAC between start+4 and end-3): {len(zm)} states of at least 25 frames measured. {len(zsig)} states change scale by more than 0.002 at 100 inliers or more, {len(zflat)} states are flat (|scale-1| at most 0.002; cards, flat illustrations and static screens), and {len(zlow)} states have fewer than 100 inliers and are not reliable measurements ({zlowtxt}); those five are the Bitcoin-moon bubble redraw, the scroll-to-banner morph, the two TV clips and the balance scale. make_states tagged no state with a ZOOM_IN suffix. Unlike RXFBHYxyqdk (slow push-ins on 54 held illustrations), the camera here is locked off.
- In-state animation (MEASURED/OBSERVED): the Bitcoin and city shot shimmers for f35-f80 (about 20,000-45,000 changed px per frame); the thought-bubble figure is redrawn into an angry figure beside a burning bin between f2407 and f2467 (60 frames, up to 155,000 px per frame); the Financial Freedom Plan doodle scroll morphs into a photoreal grey-studio banner with a blue world map between f5105 and f5243 (142 frames); the balance scale tips between f10236 and f10319; the Sequoia page scrolls in two bursts ({', '.join(f'f{a} for {b} frames' for a, b in scroll)}).
- Third-party clip cadence: in the first TV clip (f2470-f2564) {c1[0]} of {c1[1]} frames change by 3,000 px or more and the gaps between changing frames are {gtxt(c1)}; in the second (f2566-f2616) {c2[0]} of {c2[1]} change (gaps {gtxt(c2)}). The stepping is irregular; no fixed pulldown rhythm was found.
- Credit caption: the first clip carries a burned-in credit caption (Co-Executive Producer) that is absent at f2490 and present at f2518 (onset BOUND between f2491 and f2518).
- Fades: none; no dissolve was seen at any hard cut. The file ends with two black frames (f16800-f16801) cut in from the end card.
- Text change type: {base['TEXT_SWAP']} states replace or add text in one frame (for example f9899 swaps the brace label to Revolutionary Algorithmic StableCoin; f7789 swaps the neon sign from Dumb Money to Discord; f10451 clears the Terra slide and writes a new heading).
- Character redraws: POSE states change a figure or scene at f2407 (angry figure) and f16580 (mirage vanishes as the crawling figure reaches into the sand); small wobble (a few hundred px per episode) runs on stick figures and arrows inside many states and is left to the MICRO class.
- 30 fps constant frame rate ({LASTF+1} frames); the pulldown test (24 fps content in a 30 fps file) was not run, so whether the animation was authored at 24 or 30 fps is UNAVAILABLE.

## 5. Art direction and graphics
- Palette (k-means, 8 colours over one frame per state, {len(st)} frames): ''' + ', '.join(f"{c['hex']} {c['share_pct']} percent" for c in pal) + f'''. Colour names are INFERRED from the swatches: white canvas, light grey and mint grounds, charcoal and near-black, tan and wood brown, slate blue, gold.
- Style: black-outlined stick-figure and flat vector drawings on white with rounded hand-lettered type; coloured illustrated scenes for gags (casino, graveyard, desert, Titanic-style liner, castle, museum); red as the annotation colour (circles, crosses, arrows); dark cards for quoted screenshots.
- Recurring set pieces (states entering on a cut; counts from state labels): crypto casino {len(frames('casino'))} ({ftxt(frames('casino'))}); roulette table with cigar figure {len(frames('roulette'))+1} (f7740, f7789 sign swap, f16080); Rug Pull coin {len(frames('rug pull'))} ({ftxt(frames('rug pull'))}); ship and iceberg 2 (f9216, f14361); CoinGecko-style report card {len(frames('report card'))} ({ftxt(frames('report card'))}); Luna and Terra coin graphics (f9543, f9802, f10863, f14292); closed bank {len(frames('closed bank'))} ({ftxt(frames('closed bank'))}); FTX logo {len(frames('ftx logo'))} ({ftxt(frames('ftx logo'))}); dark Wikipedia excerpt {len(frames('wikipedia'))} ({ftxt(frames('wikipedia'))}); Statue of Liberty 2 (f1895, f2119).
- Third-party material, OBSERVED: four animated TV clips in two groups (f2469, f2565 and f7854, f7937) with Bitcoin overlays on the first group; photographs (a man at a microphone in front of an FTX wall, an arena exterior, a portrait of a young man, two small photos on a profile card); a magazine cover; web pages and app screenshots (Applebee's and Tinder logos, CoinGecko, a forum post, a betting app, Sequoia website, news articles, a Wikipedia excerpt, Bloomberg chart, blockchain infographic); logos (Applebee's, Tinder, CoinGecko, Discord, FTX, NYSE, BlackRock, Sequoia, DraftKings, Terra, Luna, YouTube). Photos, clips and logos belong to third parties; people shown in photographs are named only where on-screen text names them.
- Text: headings, labels, quotes and card text were read from decoded frames; small body text inside articles, charts and UI screenshots is only partly legible and is quoted only in part.

## 6. Object lifecycles (OBSERVED)
- Tinder profile: card at f325, Entrepreneur caption f420, D2D Sales caption f497.
- Annual Volatility chart: Bitcoin bar f5708, handwritten 60% f5775, U.S. Stock Market bar with 15% f5846, notes erased f5937, 4x the Volatility brace f5976.
- Terra explainer: Terra (UST) coin f10091, arrow and dollar bill f10139, Luna coin f10178, sister token label f10198, balance scale f10233, heading and lines f10321-f10367, flipped heading f10451 and lines f10501, rope snap f10717, cliff explosion f10804, Safe, Reliable and red X f10916-f10953.
- Alameda sequence: pie chart f13059, logo f13252, BUSTED stamp f13297, burning office f13358.
- Recurring callbacks: closed bank (f9698 then f14620), ship and iceberg (f9216 then f14361 with FTX and coin logos on the iceberg), report card (f8304, f11216, f14261, f14641), Luna and Terra (f14292), FTX logo (f14310), roulette with Discord (f7789, f16080), I Hate Crypto. card (f591, f16179) and So yeah... card (f533, f4159, f16147).
- Ending run: shrug f15589, forum post f15680, blockchain diagram f15861, burning scholar f15959, roulette f16080, So yeah... f16147, I Hate Crypto. f16179, HOW CRYPTO WORKS chalkboard f16227, It's the: list f16322-f16402, It's not the future of finance... f16483, desert f16544, end card f16647, black f16800.

## 7. Attention hypotheses (INFERRED, no retention or CTR data)
1. A new visual state appears every {S.mean(sds):.1f} s on average and a hard cut every {S.mean(L)/fps:.1f} s; {n1} of {len(ep)} change episodes are single frames, so the viewer follows the next card or sentence, not motion. ASR counts {nw:,} words over {span:.0f} s (about {nw/span*60:.0f} words per minute).
2. In {early} of {len(pairs)} selected phrase pairs the picture changes before the spoken word (median lead {abs(S.median(lags)):.2f} s); a visual already on screen when the phrase lands may reinforce it, but the pair selection is mine and the lead may partly reflect ASR timing.
3. Chapter cards sit in ASR gaps: no word is found for {agtxt}, which covers all three chapter-card intervals and the TV-clip stretches; whether those gaps are silence, music or clip audio is UNAVAILABLE because audio was not heard, but the pattern may mark chapter breaks as pauses.
4. Text cards ({len(txtcards)} states) work as punchlines, as pace breaks and as list builders; cards repeat the same lines (I Hate Crypto., So yeah...) as callbacks.
5. Recurring set pieces (casino, closed bank, ship and iceberg, report card, Luna and Terra, FTX logo) may help the viewer link claims across chapters.
6. The video opens on a single word card and ends on a desert mirage metaphor, a card list and an end card, which may end on a summarising image and a subscribe call.

## 8. Uncertainties and limits
- Audio was never heard; ASR (openai-whisper small.en) is provisional, so AV sign-off is BLOCKED. Phrase pairs ({len(pairs)} kept of 204 candidates) were hand-selected; none lacked a matching ASR token and 2 were dropped for a lag beyond 1.5 s (f3156 rent, f4013 high), not counted as unpaired.
- ASR event-to-nearest-word offsets ({e3} of {len(ev)} state starts within 0.3 s) are not evidence of sync: random times fall within 0.3 s of some word start {r3:.1f} percent of the time and within 0.1 s {r1:.1f} percent of the time in the build_docs random control.
- ASR reads 3.7 million where the on-screen report card reads 3.6 million; the on-screen text is the observation, ASR is provisional.
- People in photographs and clips are not independently identified; names come from on-screen text only (cards name Warren Buffett, Jamie Dimon, Peter Schiff, John J. Ray III and Sam Bankman-Fried; the caricatures beside the first three cards are drawings placed next to those names, and that they depict those people is INFERRED from placement). The TV-clip characters are third-party cartoon characters and are not named.
- Article, chart, UI and search-result body text is only partly transcribed; axes, legends and small print are not read.
- Changed-pixel counts in state descriptions are frame_metrics.csv full-resolution grayscale differences above 25 levels at the state's first frame; episodes.csv and sheet-header counts use a different colour-difference measure.
- Camera scale values are net scale between two decoded frames; states with fewer than 100 inliers ({len(zlow)}) are reported as unreliable, not as zoom.
- Whether the file is an original upload, re-encode or edit export is not known. Part boundaries, pace claims and attention hypotheses are INFERRED.
'''
open(f'{ws}/build/report_body.md', 'w').write(body)
mods = f'''## Modules (original rebuild; derived from measured patterns)
1. **Cast and set kit**: a generic stick man, a host at a desk, a canvasser, a host behind a stand, a cloaked figure, a scholar with a scroll, and set pieces (Jenga tower, casino, graveyard, desert, ship and iceberg, castle on a hill, museum case, balance scale). Redraw all as new original assets; do not trace the source.
2. **Hard-cut scene chain**: {len(cuts)} hard cuts, median shot {S.median(L)/fps:.1f} s ({min(L)/fps:.2f}-{max(L)/fps:.1f} s); {len(cuts)-len(non)} cuts land on I-frames and {len(non)} do not, so author cuts as true edits and let the encoder place keyframes.
3. **One-frame pop-in vocabulary**: text lines, labels, braces, arrows, circles and logos appear in a single frame with no easing; {n1} of {len(ep)} episodes are one frame.
4. **Text-card punchline**: one centred hand-lettered line on white, swapped in place, grown into a three-line list at 30-60 frame intervals; repeat the same lines as callbacks.
5. **Chapter-card breaks**: three white cards with doodles and a numbered title, about 4.6 s each, hard cut in and out, placed where the narration pauses.
6. **Locked-off camera**: no push-ins; keep illustrations static and put motion in redraws (a figure redrawn over 60 frames, a doodle morphing into a 3D banner over about 140 frames).
7. **Third-party insert slot**: charts, article cards, screenshots, photographs, TV clips, magazine cover and logos are replaced with licensed or self-made equivalents; never copy the source items.
8. **Dark quote cards**: a dark card with a bold lead-in and a highlighted sentence for citations (Wikipedia excerpt, white-knight persona, All in on Sam).
9. **Annotation marks**: red circles, red crosses, red arrows and a BUSTED stamp as the accent colour.
10. **Recurring landmarks**: reuse the same few set pieces (casino, closed bank, ship and iceberg, report card, Luna and Terra, FTX logo) as callbacks across chapters.
11. **Footage slot**: short stock or licensed clips with irregular frame stepping; decide the step rate deliberately.
12. **End card**: white card with Subscribe for more, channel name, YouTube mark, crossed-out social icons and a SUBSCRIBE button, held {(16799-16647+1)/fps:.0f} s, then two black frames.
13. **Codec note**: 30 fps constant frame rate, {len(I)} I-frames about every {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.1f} s on average.
'''
open(f'{ws}/build/modules.md', 'w').write(mods)
views = {
 "native_windows": [
  "winA rows: f2468-f2470 (thought-bubble figure to TV clip, f2469), f2518-f2524 (credit caption and clip motion), f2564-f2566 (clip to couch clip, f2565), f2616-f2618 (clip to Bitcoin moon, f2617)",
  "winB rows: f7870-f7872, f7926-f7928, f7936-f7938 (cut to forest, f7937), f7946-f7948, f7974-f7976, f7998-f8001 (cut to detective, f8000), f8064-f8066 (cut to CoinGecko logo, f8066)",
  "winC rows: f7957-f7966 (pan from forest to casino hut), f9471-f9472 (caption cleared, f9472), f11883-f11885 (poster to press photo, f11884), f11921-f11923 (photo to arena, f11923), f10565-f10567 and f10594-f10596 (Clever in theory. to Disastrous in practice., f10596)",
  "winD rows: f12727-f12729 (Sequoia page to dark card, f12728), f12852-f12853 (dark card to FTX logo, f12853)",
  "winE rows: f16321-f16323 (chalkboard to It's the: card, f16322), f16799-f16801 (end card to black, f16800)",
  "winF rows: f5103-f5105, f5125-f5126, f5150-f5151, f5175-f5176, f5205-f5206, f5230-f5231, f5242-f5244 (doodle scroll morphing into the 3D banner, then the casino cut at f5244)",
  "winG rows: f6378-f6380 (f6379), f6494-f6496 (f6495), f10563-f10565 (f10564), f11522-f11524 (f11523), f12927-f12929 (f12928); all five non-I cuts are one-frame replacements"
 ],
 "stepped_sheets": [
  "overview 1 fps (562 tiles, 32 sheets, all viewed)",
  "episode change-crop sheets epc_01-33 (257 episodes: context frame with changed-pixel bbox, crop at start-1, crop at start; all 33 sheets viewed)",
  f"state_rep ({len(st)} states, 13 sheets, all viewed)"
 ],
 "episode_view": f"per episode: context frame at its first changed frame with the changed-pixel bbox, plus bbox crops at start-1 and start (adjacent decoded frames); every multi-frame episode and every frame of 8,000 changed px or more was checked against frame_metrics to place state boundaries (cuts sitting on the last or a later frame of a multi-frame episode were found at f81, f2469, f2565, f2617, f2884, f5244, f7937, f8000, f10321, f10564, f11884, f12728 and f16322; {len(st)} states were placed in total)",
 "text_gate": "PARTIAL_OPEN_LIMITATION (headings, labels, quotes, card text and logo names read from decoded frames; small body text inside articles, charts, search results and UI screenshots flagged not transcribed or quoted only in part; people in photographs and clips not identified beyond on-screen names)"
}
json.dump(views, open(f'{ws}/build/views.json', 'w'), indent=1)
print('written', len(body), len(mods))
print('zsig', len(zsig), 'zflat', len(zflat), 'zlow', len(zlow)); print('casino', frames('casino'), 'rug', frames('rug pull'), 'report', frames('report card'), 'closed', frames('closed bank'), 'ftx', frames('ftx logo'), 'wiki', frames('wikipedia'))
print('txtcards', len(txtcards), 'agaps', agtxt, 'scroll', scroll); print('control', r1, r3, 'e3', e3, len(ev), 'early', early, len(pairs), 'bigeps', bigeps); print('c1', c1, 'c2', c2)
