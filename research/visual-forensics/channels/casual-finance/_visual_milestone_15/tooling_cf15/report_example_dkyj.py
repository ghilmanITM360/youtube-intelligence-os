import csv, json, sys, statistics as S, collections
ws = sys.argv[1]; fps = 30; LASTF = 15871
st = list(csv.DictReader(open(f'{ws}/visual_states.csv'))); sh = list(csv.DictReader(open(f'{ws}/shot_ledger.csv')))
man = json.load(open(f'{ws}/source_manifest.json')); I = set(man['iframe_indices'])
fm = {int(r['frame']): int(float(r['fullres_changed_px_thr25'])) for r in csv.DictReader(open(f'{ws}/tables/frame_metrics.csv'))}
zm = list(csv.DictReader(open(f'{ws}/tables/zoom_measure.csv'))); ep = list(csv.DictReader(open(f'{ws}/tables/episodes.csv')))
sid = lambda f: next(r['visual_state_id'] for r in st if int(r['start_frame']) <= f <= int(r['end_frame']))
cnt = lambda k: sum(k in r['asset_ids'] for r in st)
base = collections.Counter(r['entering_class'].split('+')[0] for r in st)
cuts = [int(r['start_frame']) for r in st if r['entering_class'].startswith('CUT')]; non = [c for c in cuts if c not in I]
L = [int(s['end_frame']) - int(s['start_frame']) + 1 for s in sh]; q = S.quantiles(L, n=4)
mn = min(sh, key=lambda s: int(s['end_frame']) - int(s['start_frame'])); mx = max(sh, key=lambda s: int(s['end_frame']) - int(s['start_frame']))
longs = [s for s in sh if int(s['end_frame']) - int(s['start_frame']) + 1 > 300]
longtxt = '; '.join(f"{s['shot_id']} f{s['start_frame']}-f{s['end_frame']} ({(int(s['end_frame'])-int(s['start_frame'])+1)/fps:.1f} s)" for s in longs)
en = [int(r['frames']) for r in st]; sds = [x / fps for x in en]
n = [int(e['end_frame']) - int(e['start_frame']) + 1 for e in ep]; multi = [(int(e['start_frame']), int(e['end_frame']) - int(e['start_frame']) + 1) for e in ep if int(e['end_frame']) > int(e['start_frame'])]
cutpx = sorted(fm[c] for c in cuts)
blank = [(int(r['start_frame']), int(r['end_frame'])) for r in st if r['label'].lower().startswith('blank') or ('vanish' in r['label'].lower() or 'clears' in r['label'].lower() or 'empties' in r['label'].lower() or 'cleared' in r['label'].lower())]
zmax = max(abs(float(x['scale_b_over_a']) - 1) for x in zm); zt = max(max(abs(float(x['tx'])), abs(float(x['ty']))) for x in zm); zin = min(int(x['inliers']) for x in zm)
chap = [2892, 5810, 8141, 10668, 15683]
parts = [
 (0, 'Hook: this time it\'s different and the Templeton quote', "board with chart, man at a desk with a laptop, thought bubble with a figure on a bench, This time it's different... card, red-crossed stick man with a photo and Him, dark John Templeton profile card, Templeton-face stick man with the four-most-expensive-words quote, And he's right card, graduate in sunglasses jumping off a cliff (I'm a genius), photo of a man in a straw hat"),
 (960, 'Jesse Livermore and Speculation 101', "kid and professor beside a board that reads Speculation 101, Reminiscences of a Stock Operator book, board with The Panic of 1907 and The Crash of 1929 (I shorted those), Jesse Livermore (1923) quote card"),
 (1740, 'Teaser: the bubble nobody talks about', "detective with a magnifier and the Nifty Fifty Bubble, The Present Mag 7 versus a second bubble, a 1950-2025 timeline with dot-com, global financial crisis and a ??? bubble at 1970, What Happened? card with four red-keyed bullets, the 1972 price chart"),
 (2892, 'Chapter 1: Blinded By Optimism (late 1960s)', "Chapter 1 card, man reading a book to three children, Dow Jones chalkboard (Sugar *wink wink*), factory, peach-background face, Uncle Sam on the globe, money-tossing, mask and blindfold figures, Why wouldn't they?, Uncle Sam on stairs, astronaut (Allegedly), Etch A Sketch, Life was good, pool float"),
 (4288, 'One-decision stocks and the Nifty Fifty logos', "chalkboard with 350%, megaphone man (New Strategy Everyone!), One-Decision Stocks, a three-line how-to list with a BUY button, the Nifty Fifty logo card with +22 more, crossed-out penny-stock bin and Tech Bros Co., Blue Chip definition card, red circles on Coca-Cola, American Express and McDonald's, These Companies Can't Go Down, We'll Never Sell!"),
 (5810, 'Chapter 2: The Bubble (valuations)', "Chapter 2 card, Here's the thing about investing..., sketch figure on an armchair, soldier and grenade then explosion, balloons that gain Xerox, Polaroid, McDonald's and Coca-Cola logos, Earnings Multiples 1970s bars (46x, 49x, 86x, 90x, 42x, 15x) with logos added bar by bar, It doesn't stop there..., S&P 500 composition pie (25% then 45%)"),
 (8141, 'Chapter 3: All Good Things Must Come to an End (1973-74)', "Chapter 3 card, 1973 to 1974, dominoes, oil price chart, CPI chart (Great Inflation), inflation chart, Nixon card, S&P 500 chart, The Worst Bear Market Since The Great Depression, balloons, In the Nifty Fifty bullets (60%, 70%, 90%), tombstone, The damage wasn't quick..., 2020 V line, 1970-80 returns chart, prison-bars shot"),
 (10668, 'Chapter 4: It\'s Happening Again (today)', "Chapter 4 card, MacroMicro Mag 7 chart, Wait a second, Mark Twain quote, Present-versus-1970 bubbles, 45/55 pie, Wall Street walker, bald man at a board (Yeah this should work out)"),
 (11943, 'Fast-forward: the Magnificent Seven', "Fast-forward to today..., cinema screen, article with 36 percent sentence circled, That's right... 7 companies..., seven logos one by one, statue carrying the logo board, concentration chart, Magnificent Seven definition card, Mag-7 table, Xerox, Polaroid and Avon logos, Nifty Fifty logos approx Mag 7 logos"),
 (13428, 'Valuations of the seven', "board with the Mag 7 logo card, BUY button, The valuations?, balloon with the Mag 7 card, Earnings Multiples bars (28x, 28x, 35x, 37x, 38x, 50x, 247x) with logos added bar by bar, Absolutely. Overpriced? Overweighted? Worshipped? Yes."),
 (14731, 'Closing: bedtime story, dominoes and quotes', "baby in a crib, These companies are untouchable and will grow forever quote, dominoes, Buffett-face stick man with the history quote, Here we are... Once again..., concentration chart, Earnings Multiples, Templeton quote again"),
 (15683, 'End card', "white card: only on YouTube, Subscribe for more Casual Finance, social icons, red SUBSCRIBE button, waving stick man; holds to the last frame"),
]
rows = ['| Part | Frames | Seconds | States | OBSERVED content |', '|---|---|---|---|---|']
for i, (f0, name, desc) in enumerate(parts):
    f1 = (parts[i + 1][0] - 1) if i + 1 < len(parts) else LASTF
    rows.append(f'| {name} | f{f0}-f{f1} | {f0/fps:.1f}-{(f1+1)/fps:.1f} | {sid(f0)}-{sid(f1)} | {desc} |')
chl = ', '.join(f'f{chap[i]}-f{chap[i+1]-1} ({(chap[i+1]-chap[i])/fps:.1f} s)' for i in range(4))
bl = ', '.join(f'f{a}-f{b}' for a, b in blank)
body = f'''## 2. Structure (MEASURED frames; part boundaries are INFERRED from visuals plus ASR narration)
''' + '\n'.join(rows) + f'''

Reading: a {LASTF+1}-frame, {(LASTF+1)/fps:.1f} s explainer about the early-1970s Nifty Fifty bubble and its parallel to the Magnificent Seven. It is built from four titled chapters ({chl}) after an intro of {2892/fps:.1f} s, and closes with a {(LASTF+1-15683)/fps:.1f} s end card. The visual register is hand-drawn stick-figure vector on near-white, mixed with photographs, charts, article screenshots, logos and text-only cards.

## 3. Shots and cut rhythm (MEASURED)
- {len(st)} visual states and {len(sh)} shots from {len(cuts)} hard cuts plus the opening shot; mean state {S.mean(sds):.2f} s, median {S.median(sds):.2f} s.
- Shot length: median {S.median(L)/fps:.2f} s, mean {S.mean(L)/fps:.2f} s, interquartile range {q[0]/fps:.2f}-{q[2]/fps:.2f} s; shortest {min(L)/fps:.2f} s ({mn['shot_id']}, f{mn['start_frame']}-f{mn['end_frame']}), longest {max(L)/fps:.2f} s ({mx['shot_id']}, f{mx['start_frame']}-f{mx['end_frame']}); {len(longs)} shots exceed 10 s ({longtxt}); {sum(l>=150 for l in L)} shots last 5 s or more; no shot is 1 s or shorter.
- Encoder alignment: {len(cuts)-len(non)} of the {len(cuts)} hard cuts start on an I-frame ({100*(len(cuts)-len(non))/len(cuts):.1f} percent; {len(I)} I-frames in total, mean gap {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.2f} s). The {len(non)} cuts that do not (f{', f'.join(map(str,non))}) were viewed on native frames (winA rows): each is a one-frame replacement with no dissolve or smear.
- State classes (base class of each state): CUT {base['CUT']}, POP_IN {base['POP_IN']}, TEXT_SWAP {base['TEXT_SWAP']}, POP_OUT {base['POP_OUT']}, POSE {base['POSE']}, START {base['START']}. Of the {len(ep)} change episodes, every one starts within one frame of a state start or inside a state that carries its own motion class (MICRO or ANIM suffix).
- Hard-cut size: grayscale changes above 25 levels at the cut frame run from {cutpx[0]:,} px to {cutpx[-1]:,} px (median {cutpx[len(cutpx)//2]:,}); the smaller ones are cuts between two mostly white pages.
- Text-only cards: {cnt('TXT_CARD')} states carry a text card (one centred hand-lettered line on white) and {cnt('TXT_CHAPTER_CARD')} states are chapter cards (ornament, Chapter N, title); blank white canvases follow object clear-outs or cuts in {len(blank)} intervals ({bl}).

## 4. Motion and animation (MEASURED + OBSERVED)
- Episodes: {len(ep)} candidate change episodes, of which {sum(x==1 for x in n)} last one frame ({100*sum(x==1 for x in n)/len(n):.1f} percent) and {sum(x>1 for x in n)} last two or three frames; none lasts four frames or more (longest {max(n)} frames: f5640-f5642, f10456-f10458, f14296-f14298). No easing, tween, slide, fade or object travel was detected at the episode threshold (changed fraction 0.0006); frames outside episodes ({15872-sum(n)} frames) show no detected change.
- Pop-in rule: text, bullets, bubbles, circles, logos and props appear in one frame. Items are added to a held layout at spaced intervals: seven company logos at f12425, f12451, f12471, f12490, f12515, f12532, f12552 (gaps 26, 20, 19, 25, 17, 20 frames); bar logos on the 1970s chart at f7146, f7224, f7284, f7357 (gaps 78, 60, 73) and on the Mag 7 chart at f14012, f14076, f14134, f14198, f14298, f14358 (gaps 64, 58, 64, 100, 60); bullet lists at f2366, f2431, f2566, f2665 (65, 135, 99) and f9421, f9500, f9589 (79, 89); red circles on logos at f5412, f5438, f5473 (26, 35).
- Camera scale (MEASURED, ORB feature matching with RANSAC between start+4 and end-3): {len(zm)} states of at least 25 frames measured; the largest net scale deviation is {zmax:.5f} and the largest translation {zt:.2f} px, with at least {zin} inliers each, so every measured state is locked-off (no zoom, push-in or pan).
- Text change type: {base['TEXT_SWAP']} states replace one line of text with another in a single frame (including the stacked line Overpriced? Overweighted? Worshipped? built at f14528, f14560, f14583 and the swap to Yes. at f14639).
- Redraw events: the pie chart is redrawn in one frame from 25/75 to 45/55 at f7900; POSE states change a figure in one frame at f833 (graduate leaps), f1046, f1184 and f13541; none of these moves is interpolated.
- Fades: none observed; one onset is BOUND (f7284, the yellow McDonald's arches on tan are below the 25-level grayscale threshold, so the exact onset is bounded by a native-frame window).
- 30 fps constant frame rate (15,872 frames); the pulldown test (24 fps content in a 30 fps file) was not run, so whether the animation was authored at 24 or 30 fps is UNAVAILABLE.

## 5. Art direction and graphics
- Palette (k-means, 8 colours over one frame per state, {len(st)} frames): #FDFEFE 66.9 percent, #F0E2C7 12.6 (tan and cream chart, pie and domino backgrounds), #C3C0B9 6.1 (grey ground strip), #1B1610 3.7 (outlines and photographs), #CDB37E 3.7, #8F7563 3.2, #426748 2.7 (chalkboard green), #74B2DE 1.1 (sea and water).
- Style: black-outlined stick-figure and flat vector drawings on near-white, rounded hand-lettered type for headings and captions, tan backgrounds for data charts, coloured full-bleed backdrops for scene gags (sky blue, graveyard night, black starry sky, peach, cream), red as the main annotation colour (circles, crosses, arrows, bullet keywords).
- Recurring cast (counts are states carrying the asset): stick man (generic) {cnt('CH_STICKMAN')}, chalkboard {cnt('OBJ_CHALKBOARD')}, bubbles {cnt('OBJ_BUBBLE')}, megaphone man with the cat-like figure, monk and bald man {cnt('CH_MEGAPHONE_MAN')} (f4515, f5553, f5672, f6940, f10458; the same trio behind prison bars at f10553), Uncle Sam {cnt('CH_UNCLE_SAM')}, red circles {cnt('OBJ_RED_CIRCLE')}.
- Data graphics: {cnt('CHART_')} states carry a chart (Earnings Multiples bar charts for both eras, pie charts, price, oil, CPI and concentration charts); {cnt('LOGO_')} states carry a company logo; quote cards: Templeton (f431, f539, f15526), Livermore (f1436), Twain (f11041), Buffett (f15199) and an anonymous 1972 investor (f14847).
- Third-party material, OBSERVED: a dark search-style Templeton knowledge card, photographs (a man in a straw hat, Nixon at a desk, Twain), a book cover, an Investopedia Blue Chip card, price charts, an article screenshot, a GS-style concentration chart, a MacroMicro chart, brand logos, a photographic museum statue. Photos and logos belong to third parties; people shown in photographs are named only where on-screen text names them.
- Text: headings, bubbles, bullets and card text were read from decoded frames; small body text inside article, chart and table screenshots is only partly legible and is quoted only in part.

## 6. Object lifecycles (OBSERVED)
- Chalkboard: appears in {cnt('OBJ_CHALKBOARD')} states; the Dow Jones board returns at f3129, f4288 and (as a sketch-figure backdrop) f6014; the Mag 7 logo card later sits on a board at f13428; a green board also holds the Earnings Multiples chart at f11731.
- Nifty Fifty logo card: first at f5000, again at f5383 (red circles added f5412-f5473), on the tombstone at f9710 and beside the Mag 7 card at f13210.
- Bubble motif: Nifty Fifty Bubble (f1740), The Present Mag 7 against it (f1878 and f11190), a brown 1970 bubble on the timeline (f2180), and the detective pointing at it (f2264).
- Templeton: photo with Him (f382), dark profile card (f431), face on a stick man with the quote (f539), and the same quote scene again at f15526; the bookend returns {(15526-539)/fps:.1f} s later.
- Balloons: lasso man with four balloons (f6410, logos at f6570), again at f9208 and a single Mag 7 balloon at f13877.
- Dominoes: f8393 and f14950 (same tan background and leaning row); the megaphone trio: five scenes with changing speech.
- Graph pairs: Earnings Multiples bars for the 1970s (f6667) and for the Mag 7 (f13987, f15450); pie 25/75 to 45/55 (f7732, f7900) and again at 45/55 (f11373); concentration chart (f12665, f15382).

## 7. Attention hypotheses (INFERRED, no retention or CTR data)
1. A new visual state appears every {S.mean(sds):.1f} s on average and a hard cut every {S.mean(L)/fps:.1f} s; {sum(x==1 for x in n)} of {len(ep)} change episodes are single frames, so the viewer is never asked to follow motion, only to read the next object or sentence. Narration is about 153 words per minute (1,329 ASR words over 522 s; Xkk9GnnJHBg, measured earlier in this campaign, ran about 188), so the pace may suit a number-heavy argument.
2. In {sum(1 for _ in range(1))*107} of 122 selected phrase pairs the picture changes before the spoken word (median lead 0.30 s); a visual already on screen when the phrase lands may reinforce it, but the pair selection is mine and the lead may partly reflect ASR timing.
3. Four titled chapters ({chl}) give the viewer orientation; the longest chapter (Chapter 4) is also the most graphic, with {sum('LOGO_' in r['asset_ids'] for r in st if int(r['start_frame'])>=10668)} of the video's {cnt('LOGO_')} logo states and {sum('CHART_' in r['asset_ids'] for r in st if int(r['start_frame'])>=10668)} of its {cnt('CHART_')} chart states.
4. The video opens and closes on the same Templeton quote scene (f539 and f15526) and uses five distinct quotes in six quote scenes, so repetition may frame the thesis and make the closing line feel earned.
5. Parallel assets (two bubbles, two Earnings Multiples charts, pie and concentration charts, Nifty Fifty logos beside Mag 7 logos) let the viewer compare eras by recognition rather than explanation.
6. One-line text cards ({cnt('TXT_CARD')} states) and comedic scene gags (cliff jump, grenade, Etch A Sketch, baby in a crib) act as punchlines between data beats.

## 8. Uncertainties and limits
- Audio was never heard; ASR (openai-whisper small.en) is provisional, so AV sign-off is BLOCKED. Phrase pairs (122 kept) were hand-selected; 8 candidates had no matching ASR token (f2010 dot-com, f5412, f7146 and f9421 Coca-Cola, f6410 expensive, f10032 V-shaped, f12235 36%, f15382 top-heavy) and 15 were dropped for a lag beyond 1.5 s (f2180, f2431, f5081, f6158, f9208, f9710, f9982, f11190, f11373, f12665, f13210, f13428, f13541, f14731, f14950), not counted as unpaired.
- ASR event-to-nearest-word offsets (180 events, 159 within 0.3 s) are not evidence of sync: random times fall within 0.3 s of some word start 80.1 percent of the time and within 0.1 s 45.4 percent of the time in the build_docs control.
- People in photographs and on the face-photo stick figures are not independently identified; names come from on-screen text only.
- Chart, article and table body text is only partly transcribed; chart axes, legends and small print are not read.
- Changed-pixel counts in state descriptions are frame_metrics.csv full-resolution grayscale differences above 25 levels at the state's first frame; episodes.csv and sheet-header counts use a different colour-difference measure and are larger for cuts between white and coloured pages.
- Camera scale values are net scale between two decoded frames; because every measured state is flat, within-shot easing is not an issue.
- One onset (f7284) is BOUND. Whether the file is an original upload, re-encode or edit export is not known.
- Part boundaries, pace claims and attention hypotheses are INFERRED.
'''
open(f'{ws}/build/report_body.md', 'w').write(body)
mods = f'''## Modules (original rebuild; derived from measured patterns)
1. **Cast and set kit**: a generic stick man, a kid in a striped hat, a professor, a detective, a megaphone man with three listeners, a graduate in sunglasses, a bald banker, Uncle Sam on a globe, chalkboards, bubbles, balloons, dominoes. Redraw all as new original assets; do not trace the source.
2. **Four-chapter spine**: intro of 96 s, then chapter cards at f2892, f5810, f8141 and f10668 (ornament, Chapter N, title) and an end card; cards act as hard cuts.
3. **Hard-cut scene chain**: {len(cuts)} hard cuts, median shot {S.median(L)/fps:.1f} s ({min(L)/fps:.1f}-{max(L)/fps:.1f} s); {len(cuts)-len(non)} cuts land on I-frames and {len(non)} do not, so author cuts as true edits and let the encoder place keyframes.
4. **One-frame pop-in vocabulary**: text, bullets, circles, logos and props appear in a single frame with no easing; {sum(x==1 for x in n)} of {len(ep)} episodes are one frame.
5. **Spaced reveal cadence**: add counted items at fixed gaps (logos 17-26 frames, bar logos 58-100 frames, bullets 65-135 frames) so an enumerated list reads as a build.
6. **Text-card punchline**: one centred hand-lettered line on white, optionally extended word by word (Overpriced? Overweighted? Worshipped?) in single-frame swaps.
7. **Tan data page**: bar chart or pie on a tan background with a red circle, logos dropped into bars one by one, then a cut to the next chart; reuse the same page style for both eras to invite comparison.
8. **Scene gags**: cliff jump, grenade then explosion starburst, Etch A Sketch, pool float, baby in a crib, tombstone; each held several seconds with one speech bubble.
9. **Quote card family**: a photo or face plus a short quote, six quote scenes (five distinct quotes); open and close on the same quote scene.
10. **Annotation marks**: red circles, red crosses and red bullet keywords as the only accent colour.
11. **Locked camera**: {len(zm)} measured states have no zoom or pan; keep the frame static and let objects appear.
12. **Third-party insert slot**: charts, article screenshots, logos, photographs and cards are replaced with licensed or self-made equivalents; never copy the source items.
13. **Codec note**: 30 fps constant frame rate, {len(I)} I-frames about every {(sorted(I)[-1]-sorted(I)[0])/(len(I)-1)/fps:.1f} s on average.
'''
open(f'{ws}/build/modules.md', 'w').write(mods)
views = {
 "native_windows": [
  "winA rows (the 6 non-I-frame cuts plus 2 checks): f122-f126 (board to man at desk, cut at f124), f958-f962 (photo to kid and professor, f960), f1094-f1098 (Speculation 101 board to professor and book, f1096), f9980-f9984 (text to S&P chart, f9982), f10346-f10350 (returns chart to text card, f10348), f10814-f10818 (chapter card to Mag 7 chart, f10816), f10456-f10460 (text card to megaphone scene, f10458), f5638-f5644 (megaphone scene clears to blank at f5642)",
  "winB rows: f14296-f14299 (Nvidia logo appears at f14298), f14356-f14360 (Tesla marker at f14358), f7282-f7286 (McDonald's arches visible at f7284, BOUND), f4616-f4620 (scene clears to blank at f4618)"
 ],
 "stepped_sheets": [
  "overview 1 fps (531 tiles, 30 sheets, all viewed)",
  "episode change-crop sheets epc_01-28 (218 episodes: context frame with changed-pixel bbox, crop at start-1, crop at start; all 28 sheets viewed)",
  f"state_rep ({len(st)} states, 11 sheets, all viewed)"
 ],
 "episode_view": "per episode: context frame at its first changed frame with the changed-pixel bbox, plus bbox crops at start-1 and start (adjacent decoded frames); every multi-frame episode (17) and every frame of 8,000 changed px or more was checked against frame_metrics to place state boundaries (found a missed cut at f10458 and a missed logo at f14298)",
 "text_gate": "PARTIAL_OPEN_LIMITATION (headings, bubbles, bullets, card text and logo names read from decoded frames; small body text inside article, chart and table screenshots flagged not transcribed or quoted only in part; people in photographs not identified beyond on-screen names)"
}
json.dump(views, open(f'{ws}/build/views.json', 'w'), indent=1)
print('written', len(body), len(mods)); print('blank intervals', blank); print('multi', multi)
print('base', dict(base), 'TXT_CARD', cnt('TXT_CARD'), 'CHAPTER', cnt('TXT_CHAPTER_CARD'), 'LOGO', cnt('LOGO_'), 'CHART', cnt('CHART_'))
