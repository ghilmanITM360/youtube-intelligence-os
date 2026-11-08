import csv, json, bisect, random, statistics as S, hashlib, os, glob, datetime
VID = 'CFrVTZBYa3Q'; FPS = 24; pts = lambda f: round(f / FPS, 4)
man = json.load(open('source_manifest.json')); st = list(csv.DictReader(open('visual_states.csv'))); ev = list(csv.DictReader(open('visual_event_ledger.csv'))); kf = json.load(open('tables/key_facts.json'))
asr = json.load(open('audio/CFrV_small_en.json')); words = [(x['start'], x['end'], x['word'].strip()) for sg in asr['segments'] for x in sg['words']]
pal = json.load(open('tables/palette.json')); asum = json.load(open('tables/asr_alignment_summary.json'))
# ---- phrase-level (semantic) alignment: (state_start_frame, word, approx_word_time)
M = [(63,'since',2.64),(99,'The',4.12),(164,'since',6.76),(203,'while',8.56),(268,'since',10.94),(296,'And',12.36),(375,'since',15.38),(423,'30',17.54),(484,'So',20.22),(585,'of',24.32),(612,'Elon',25.70),(644,'raises',26.92),(659,'very',27.48),(704,'the',29.40),(746,'Because',31.06),(777,'boring,',32.58),(801,"it's",33.42),(816,'predictable,',34.04),(839,'uneventful,',35.00),(862,'something',35.98),(889,'asleep',37.12),(923,"that's",38.54),(1005,'But',41.80),(1012,'now,',42.12),(1020,'while',42.52),(1048,'watching',43.60),(1068,'vertical',44.60),(1089,'the',45.40),(1117,'the',46.60),(1157,'the',48.36),(1167,'on',48.76)]
byf = {int(e['start_frame']): e for e in ev}; rows = []
for f, wd, t0 in M:
    j = min((k for k, x in enumerate(words) if x[2] == wd), key=lambda k: abs(words[k][0] - t0)); e = byf.get(f)
    vt = pts(f) if e is None or f == 1012 else float(e['start_pts_seconds'])
    rows.append(dict(video_id=VID, event_id=(e['event_id'] if e and f != 1012 else f'E-f{f}'), audio_source='local ASR openai-whisper small.en word timestamps', audio_listening_status='ASR_UNCERTIFIED - NO HUMAN LISTENING',
        phrase_or_sound=f"[{words[j][2]}] …{' '.join(x[2] for x in words[max(0,j-3):j+4])}…", audio_start_pts=round(words[j][0], 3), audio_end_pts=round(words[j][1], 3), visual_start_pts=vt, visual_end_pts=(e['end_pts_seconds'] if e and f != 1012 else vt),
        lead_lag_seconds=round(vt - words[j][0], 3), timestamp_method='semantically chosen word (phrase the graphic illustrates) vs visual PTS (frame-exact where onset EXACT)', confidence='MEDIUM', limitations='ASR word timing +/-0.1-0.3 s; chosen pairing is my reading (INFERRED), not heard'))
with open('audio_visual_alignment_phrase.csv', 'w', newline='') as fh:
    q = csv.DictWriter(fh, fieldnames=list(rows[0])); q.writeheader(); q.writerows(rows)
lags = [r['lead_lag_seconds'] for r in rows]; random.seed(1); starts = sorted(x[0] for x in words)
base = [min(abs(t - s) for s in starts) for t in (random.uniform(0, 49.5) for _ in range(5000))]
phr = dict(n=len(lags), median=S.median(lags), p10=sorted(lags)[len(lags)//10], p90=sorted(lags)[9*len(lags)//10], within_0_1=sum(abs(x) <= 0.1 for x in lags), within_0_3=sum(abs(x) <= 0.3 for x in lags), visual_early=sum(x < 0 for x in lags), visual_late=sum(x > 0 for x in lags),
           random_nearest_word_median_abs=round(S.median(base), 3), random_within_0_1=round(sum(b <= 0.1 for b in base) / len(base), 3), random_within_0_3=round(sum(b <= 0.3 for b in base) / len(base), 3))
json.dump(phr, open('tables/phrase_alignment_summary.json', 'w'), indent=1)
dur = lambda s: float(s['duration_s'])
cut = {int(s['start_frame']): s for s in st}
pan = [(1, 49), (99, 181), (203, 280), (296, 375), (423, 473)]
pd = [round((b - a + 1) / FPS, 2) for a, b in pan]
longest = max(st, key=lambda s: int(s['frames']))
T = lambda f: f"{f/FPS:.2f}s"
# ---------------- report
R = f"""# Visual CT scan report - {VID} (Casual Finance) - visual-only scope

Reader: Claude Sonnet 5.5 on Machine A, 2026-11-08. Mode: CT_SCAN (visual). Audio: ASR only, never heard. Status label: see `quality_gate.json` (visual-only, declared coverage; AV sign-off BLOCKED).

## 1. Source and coverage (MEASURED)
- File: `{os.path.basename(man['source_path'])}`; SHA-256 `{man['source_sha256']}`; {man['bytes']:,} bytes. Identity: filename carries `[{VID}]` and the roster/queue marks EXACT_ID_MATCH against registered channel metadata; not re-checked against live YouTube.
- H.264 {man['video']['w']}x{man['video']['h']} {man['video']['pix_fmt']}, {man['video']['avg_frame_rate']} fps, **CFR proven**: {man['decoded_frames_pts_listed']} frames, every frame delta {man['frame_delta_distinct'][0]} s, PTS = frame/24 (first 0.000, last {man['pts_last']:.3f}); {man['iframes']} I-frames. AAC audio present (LUFS -20.7, peak -4.7 dBFS, 4 silences below -40 dB of >=0.3 s).
- Pass 1 (MEASURED): every one of the {man['decoded_frames_pts_listed']} frames decoded once; per-frame 320 px changed-fraction, mean absolute difference, mean luma, a 4x4 localisation grid and a full-resolution changed-pixel count -> `tables/frame_metrics.csv`. {kf['episodes']} activity episodes (threshold 0.06 % or 300 full-res px, gap <= 3) -> `tables/episodes.csv` (CANDIDATES only).
- Pass 2 (OBSERVED): 1 fps overview (51 tiles), **all {kf['episodes']} episodes viewed** as decoded frames start-1 / start / middle / end / end+1, 8 + 8 + 3 native consecutive-frame windows around ambiguous cuts, overlay onsets and the type-on text, 4 stepped sheets over pans and entrances, and one representative decoded frame per state (70) viewed and compared with the ledger text. No interpolated frames are used.
- Result: **{kf['states']} visual states** contiguous from f0 to f1188 (no gaps, no overlaps), {kf['shots']} shots, {kf['hard_cuts']} hard cuts + start, {kf['events']} events. Onset precision: {kf['exact_onsets']} EXACT (adjacent decoded frames), {kf['bound_onsets']} BOUND (true onset inside a stated window of <= 6 frames), the rest MEAS (end of measured activity, interior not viewed frame-by-frame).

## 2. Macro structure (OBSERVED, timings MEASURED)
| Act | Frames | Time | What happens |
|---|---|---|---|
| A. Five bond-yield chart scenes | f0-f483 | 0.00-20.17 s | US 30y (2007 high), UK 30y (1998), Germany 30y (2011), Japan 10y (1999), Japan 30y (all-time high); each = screenshot chart panned right, then overlays |
| B. Flag recap grid | f484-f555 | 20.17-23.13 s | four flag icons + four chart thumbnails pop in one by one (US f484, UK f488, Germany f492, Japan f494) |
| C. Doge analogy | f556-f643 | 23.17-26.79 s | Doge coins fade over the flags; Dogecoin/Bitcoin chart; Elon tweet screenshot and a peeking head |
| D. Blackboard question | f644-f703 | 26.83-29.29 s | teacher at a blackboard; "One VERY important question:" |
| E. Meme and sleepy bonds | f704-f800 | 29.33-33.33 s | reaction-meme video with two "???", blank, two bond drawings, sleeping armchair figure |
| F. Blackboard "Predictable / Uneventful" | f801-f861 | 33.375-35.88 s | stern teacher, two chalk bullets typed on with pointer pops |
| G. Old man falls asleep | f862-f922 | 35.92-38.42 s | old man says a line, then dozes, three z marks added one by one |
| H. Party | f923-f1004 | 38.46-41.83 s | confetti party scene; thought bubble "These people are mad" |
| I. "But right now," | f1005-f1019 | 41.875-42.46 s | stick man, text typed on character by character |
| J. S&P 500 | f1020-f1088 | 42.5-45.33 s | dark finance screenshot, two characters hop in, chart pans right, green ellipse |
| K. AI chatter | f1089-f1116 | 45.375-46.50 s | chart grid, robot rises with thumbs up |
| L. Plug pulled | f1117-f1188 | 46.54-49.54 s | Treasury character unplugged at f1157; black from f1167 (0.917 s) |

Hard-cut frames (each verified on adjacent decoded frames, entry change MEASURED in `shot_ledger.csv`): {', '.join('f'+str(f) for f in kf['cut_frames'])}.
State length: mean {kf['mean_state_s']} s, median {kf['median_state_s']} s; longest {longest['visual_state_id']} ({longest['frames']} frames = {dur(longest):.2f} s, the four-flag grid hold). Of {kf['states']} states, {sum(1 for s in st if s['entering_class'] in ('HOLD','START'))} are pure holds.

## 3. Motion and camera findings
- **Recurring chart module (OBSERVED, n=4 full cycles + US variant):** hard cut to a wide chart screenshot already panned to its left end -> camera pans right across it for {pd[1]} s (UK, f99-f181), {pd[2]} s (Germany, f203-f280), {pd[3]} s (Japan 10y, f296-f375), {pd[4]} s (Japan 30y, f423-f473), {pd[0]} s for the US opener (f1-f49, where the yield line also draws on) -> a red arrow slides in at the right edge -> a handwritten "since YEAR" label pops in -> a country-map character rises from the bottom edge.
- **Overlay cadence (MEASURED from onsets):** UK cut f99, arrow f135 (+36 fr), label f164 (+65), character f165; Germany cut f203, arrow f227 (+24), label f268 (+65), character f269; Japan 10y cut f296, arrow f326 (+30), circle f339 (+43), label f375 (+79), character f386 (+90). Label comes about 65 frames (2.7 s) after the cut in both UK and Germany; n=2 so this is a pattern, not a rule.
- Pop-ins are single-frame (no scale/opacity easing visible on adjacent frames): "since" labels, speech/thought text, chalk bullets, flag rows, "???", armchair, z marks. Text that is *typed on* (one character per frame) appears only for "But right now," (f1006-f1012).
- Camera type: all pans are horizontal digital pans of a screenshot wider than the 1080 px frame (content moves left); easing curve not measured (ease-in/out vs linear would need per-frame offset tracking; marked UNAVAILABLE). The Doge/tweet scene uses a vertical scroll-up (f612-f627). The S&P scene pans right (f1048-f1067) while two characters stay fixed in screen space.
- Character motion: slides/rises from frame edges over 10-18 frames (UK/Germany/Japan maps, robot f1092-f1101, S&P pair f1022-f1034), a looping dancing Doge sprite (f556-f584), one idle bob (f1117-f1153), pose swaps (teacher pointer up/down at f816, f824, f838, f845; old man doze f889).
- Shot cuts: all {kf['hard_cuts']} cuts are hard cuts (no dissolves or wipes); fade-to-black is a hard cut to black at f1167.

## 4. Art direction and design
- **Medium (OBSERVED):** flat 2D hand-drawn explainer on a near-white canvas (#fcfcfc covers 52-95 % of sampled frames) mixing (a) news-outlet and data-vendor chart screenshots, (b) a reaction-meme video clip, social-post screenshot, and a dark finance-app screenshot, (c) original-looking flat characters with thick uneven black outlines. Whether characters are hand-drawn or AI-assisted cannot be determined from frames.
- **Palette (MEASURED, k-means on 12 viewed frames, `tables/palette.json`):** canvas #fcfcfc; chart hues pink #c69aa1 (UK), orange #eeab53 (Germany, Japan 30y), purple (US), black line (Japan 10y); characters' country-map green #4d9953 / #509355; blackboard green #37843e with brown frame #6a5046; skin #efd2b8 / #f5d2b7; old-man beige #cdd0b1; armchair red #b14f4d; dark app panel #212228 (42 % of f1020). Red handwritten year labels and arrows are the single saturated accent that repeats in every chart scene.
- **Typography (OBSERVED):** three registers: (1) tiny grey/black sans in screenshots, unreadable at phone size beyond headlines; (2) handwritten display for "since" (black, small) over the year (red, large); (3) chalk-style white font on the blackboard and a handwritten black type-on font for "But right now,". Exact typefaces not identified.
- **Composition:** vertical 9:16 with a full-width screenshot in the upper two thirds and characters/overlays in the lower third; characters are cropped by the frame edge, which keeps the chart readable. Static anchors: the white canvas, the chart image position (between pans) and the lower-third character slot.
- **Hierarchy (INFERRED salience hypothesis, not gaze data):** large red year label and red arrow on white are the highest-contrast marks in each chart scene, so they likely draw the eye before the chart line.

## 5. Script and audio alignment (ASR_UNCERTIFIED - nobody listened)
- ASR: local whisper small.en, 157 words; full text in `audio/CFrV_small_en.json`. The script states: US 30y highest since 2007, UK since 1998, Germany since 2011, Japan 10y since 1999, Japan 30y all-time high; "four of the largest sovereign bond markets ... Dogecoin after an Elon Musk tweet ... one very important question"; bonds are "predictable, uneventful ... grandpa falls asleep"; "But right now, while everyone's distracted watching stocks go vertical and the AI hype, the adult in the room quietly just pulled the plug on the party."
- Phrase-level sync ({phr['n']} semantically paired events, `audio_visual_alignment_phrase.csv`): median visual-minus-word lag {phr['median']:.3f} s, p10 {phr['p10']:.3f}, p90 {phr['p90']:.3f}; {phr['within_0_1']}/{phr['n']} within 0.1 s, {phr['within_0_3']}/{phr['n']} within 0.3 s; the visual leads the paired word in {phr['visual_early']} cases and trails it in {phr['visual_late']}. Control: random times fall within 0.1 s of some word start {phr['random_within_0_1']:.0%} of the time and within 0.3 s {phr['random_within_0_3']:.0%}, so closeness alone is weak evidence; the evidence is that the *right* word is hit (e.g. "since" labels pop at 2.625 s, 6.833 s, 11.167 s, 15.625 s against ASR "since" at 2.64, 6.76, 10.94, 15.38; "predictable" chalk bullet f816 = 34.00 s vs word 34.04; "uneventful" f839 = 34.958 s vs 35.00; "But" type-on ends on "now," at f1012 = 42.17 s vs 42.12; plug pull f1157 = 48.21 s right after "pulled" 48.06).
- Nearest-word table for every non-hold event: `audio_visual_alignment.csv` ({asum['events']} rows, median lag {asum['median_lag']:.3f} s). Not heard: music, SFX and tone are UNAVAILABLE.

## 6. Story and editing (INFERRED, labelled)
- The video states a thesis in 20 s with five identical-format chart "proofs", then switches visual grammar (blackboard, memes, characters) at the first rhetorical question, returns to a screenshot-plus-character grammar for the S&P/AI context, and ends on a visual pun (the Treasury character being unplugged) timed to the final clause, followed by 0.92 s of black.
- Cut rhythm: {kf['hard_cuts']} hard cuts in 49.5 s (one per {49.5/kf['hard_cuts']:.1f} s on average); chart scenes run 3.3-4.2 s each, character gag scenes 1.5-3.4 s.
- Counterexamples to the chart module: Japan 30y has no "since" label (it is "all-time high"), and its character is a different dizzy variant; the S&P scene pans but has no arrow/label; the AI chart scene has no pan.

## 7. Issues and optional improvements (all INFERRED, optional)
- Tweet screenshot, chart axes and S&P footer text are below readable size at phone width (OBSERVED unreadable); an optional fix is to crop to the one figure that matters.
- Two stills with no state change for 2.6 s (flag grid hold f494-f555) are the longest static interval; a test would be to add the Doge fade earlier or shorten the hold.
- Thumbnail/title not re-fetched; chart figures on screen not fact-checked.

## 8. Declared limitations
No listening; ASR text unverified; quiet frames inside holds were measured unchanged within threshold but not individually viewed; changes below about 0.06 % of pixels at 320 px (about 35 px) and below 300 changed full-res pixels are not detected; pan easing and exact typefaces not measured; seven overlay onsets carry a window of up to 6 frames (BOUND); shot count is exact here because every cut was a hard cut.
"""
open('visual_ct_scan_report.md', 'w').write(R)
# ---------------- blueprint
B = f"""# Reconstruction blueprint - original asset system derived from {VID}

All specifications below are for NEW ORIGINAL assets and motion. No source screenshot, meme footage, flag/logo asset or character drawing is to be copied; third-party items (`IMG_*`, `ICON_*`) are replaced with your own licensed or self-made equivalents and your own data. Derived from verified patterns; timings are for 24 fps, 1080x1920.

## Global system
- Canvas `#fcfcfc`; black outline 6-8 px, uneven hand line; flat fills; one saturated accent (red `#b0202f`-family hand-lettered labels and arrows); chart scenes use one hue per country; blackboard `#37843e` with `#6a5046` frame.
- Layers (bottom to top): canvas, chart/screenshot plate (wider than frame for pans), characters (lower third, cropped by frame edge), arrows/circles/ellipses, hand-lettered labels.
- Fonts: hand-lettered display for labels, chalk font for blackboard, handwritten black for type-on. Pick licensed equivalents.

## Reusable modules
1. **Chart module (A):** plate width ~2.5-3x frame. Hard cut onto plate panned fully left. Pan right 51-83 frames, settle. Arrow slides in from the right edge 24-36 frames after cut; "since YEAR" label pops (1 frame) about 65 frames after cut; character rises from bottom over 10-18 frames; hold >= 20 frames. QA: label onset frame equals plan +/- 0.
2. **Row pop-in grid (B):** four rows (icon + thumbnail) popping at f0, f+4, f+8, f+10 frames; hold 62 frames.
3. **Blackboard (D/F):** board top, teacher lower left, pointer poses up/down; chalk bullet appears on the same frame the pointer rises; pointer drops 8 frames later.
4. **Type-on text (I):** one character per frame, 7 frames, then hold; character gesture on the hold.
5. **Gag props (E/G/L):** sleeping armchair pop-in, z marks added one per 10 frames, plug-pull pose swap in one frame, hard cut to black held 22 frames.
6. **Dark-screenshot module (J):** plate with two bottom characters hopping in over 12 frames, plate pans right 20 frames, hand-drawn ellipse pops on the high.

## Editor timeline (frames at 24 fps)
{chr(10).join(f"- {s['visual_state_id']} f{s['start_frame']}-f{s['end_frame']} ({s['frames']} fr): {s['entering_class']} - {s['label']}" for s in st)}

## Per-state prompts
Full image and animation prompts for all {kf['states']} states, with static anchors and nearest-frame QA, are in `PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json` (generated from the verified ledger; each prompt substitutes original assets for third-party items).

## Acceptance tests
1. Cut frames equal the ledger list exactly ({', '.join(str(f) for f in kf['cut_frames'])}).
2. All EXACT onsets match to the frame; BOUND onsets fall inside their stated window.
3. Static anchors are pixel-still between events (changed fraction 0 outside event frames).
4. Total length {man['decoded_frames_pts_listed']} frames; black tail >= 22 frames.
5. Sound: not specified (nobody listened); ASR script lines may be used only as a timing reference, not as verified wording.
"""
open('reconstruction_blueprint.md', 'w').write(B)
# ---------------- coverage, gate, handoff
cov = dict(video_id=VID, source_sha256=man['source_sha256'], mode='CT_SCAN (visual-only)', frames_total=man['decoded_frames_pts_listed'], frames_measured=man['decoded_frames_pts_listed'], frames_measured_fraction=1.0,
  overview_1fps_tiles=51, episodes_total=kf['episodes'], episodes_viewed=kf['episodes'], states=kf['states'], native_windows_viewed=['0-5','97-103','176-183','200-206','279-283','293-299','384-390','421-427','135-141','159-165','165-171','227-233','263-269','326-332','338-344','374-380','1002-1013','1155-1159','1164-1168','814-818','822-826','836-841','843-847'],
  stepped_sheets=['99-183:6','203-287:6','296-380:6','423-477:4','556-585:2','612-628:1','750-766:1','923-1013:6','1020-1044:2','1048-1070:2','1089-1102:1','1117-1158:3'], representative_state_frames_viewed=kf['states'],
  onset_precision=dict(EXACT=kf['exact_onsets'], BOUND=kf['bound_onsets']), unseen='quiet frames inside holds were measured unchanged (thr 0.06 % / 300 px) but not individually viewed', resolution_floor='~35 px at 320 px scale; 300 changed full-res px', audio='ASR only (small.en); never listened; AV UNAVAILABLE for sign-off')
json.dump(cov, open('coverage.json', 'w'), indent=1)
gate = dict(video_id=VID, source_sha256=man['source_sha256'], requested_mode='CT_SCAN', scope='visual-only; audio/AV tracked separately', reviewer='Claude Sonnet 5.5, Machine A, 2026-11-08',
  gates=dict(source_identity='PASS (hash computed; filename ID + registry EXACT_ID_MATCH; live YouTube not re-checked)', full_temporal_overview='PASS (all 1189 frames measured; 1 fps overview)', candidate_shots_verified='PASS (17 hard cuts + start verified on adjacent decoded frames; 37/37 episodes viewed)',
    meaningful_state_timing='PASS_WITH_DECLARED_BOUNDS (43 EXACT, 7 BOUND windows <= 6 frames, rest measured activity edges)', motion_design_review='PASS (pans, entrances, pops, type-on classified; easing UNAVAILABLE)', creative_design_review='PASS (palette measured; typography labelled)',
    on_screen_text='PARTIAL_OPEN_LIMITATION (tweet/axis/footer text unreadable, flagged not guessed)', visual_script_mapping='PROVISIONAL_ASR_ONLY (31 semantic pairs, control baseline reported)', production_blueprint='PASS (70 per-state prompts, 6 modules, timeline, acceptance tests)',
    audio_human_listening='NOT_COMPLETED', final_av_signoff='BLOCKED', ct_scan_complete='PASS_VISUAL_ONLY'),
  final_video_status='VISUAL_CT_SCAN_COMPLETE_WITH_EVIDENCE (visual-only, declared coverage)', full_av_signoff='NO',
  limitations=['no human listening', 'ASR unverified', 'quiet-frame interiors not individually viewed', 'sub-threshold changes undetectable', 'pan easing and typefaces not measured', 'live thumbnail/title not re-fetched', 'chart figures not fact-checked'], next_step='run validate.py; add to visual_complete_ledger.json only if it exits 0')
json.dump(gate, open('quality_gate.json', 'w'), indent=1)
open('continuation_handoff.md', 'w').write(f"""# Handoff - {VID} ({datetime.date.today()})
Status: visual-only CT scan built, validator `build/validate.py`. Next frame/range: none for visual scope. Pending outside scope: human listening (AV BLOCKED), live thumbnail/title identity check.
Source SHA-256 {man['source_sha256']}. Workspace /Users/ghilmankhan/YIOS-local-audits/2026-11-08-CFrVTZBYa3Q-deep-ct-scan (local only; media never in Git). Tools: ~/YIOS-local-audits/tooling/cf15/{{ingest,measure,episodes,sheets,windows,stepsheet,repsheets}}.py with tooling/visual-ct-scan-venv; ASR via system python3 -E whisper small.en.
Rebuild: python3 -E build/build_all.py; python3 -E build/build_docs.py; python3 -E build/validate.py. Git: nothing committed from this video yet (checkpoint at the 15 milestone). Machine A; writer lock claude-cf15-20261108.
""")
# ---- checksums
files = sorted(f for f in glob.glob('**/*', recursive=True) if os.path.isfile(f) and f != 'EVIDENCE_SHA256SUMS' and '__pycache__' not in f)
open('EVIDENCE_SHA256SUMS', 'w').write(''.join(f"{hashlib.sha256(open(f,'rb').read()).hexdigest()}  {f}\n" for f in files)); print(len(files), 'files sealed;', json.dumps(phr))
