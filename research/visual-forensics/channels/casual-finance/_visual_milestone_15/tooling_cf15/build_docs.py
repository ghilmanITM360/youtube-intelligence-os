# usage: build_docs.py (cwd = workspace). Needs build/phrase_pairs.json, build/report_body.md, build/modules.md, build/views.json (all authored per video)
import csv, json, random, statistics as S, hashlib, os, glob, datetime
man = json.load(open('source_manifest.json')); VID = man['video_id']; N = man['decoded_frames_pts_listed']; FPS = round(1 / (man['pts_last'] / (N - 1))); pts = lambda f: round(f / FPS, 4)
st = list(csv.DictReader(open('visual_states.csv'))); ev = list(csv.DictReader(open('visual_event_ledger.csv'))); kf = json.load(open('tables/key_facts.json')); asum = json.load(open('tables/asr_alignment_summary.json'))
asr = json.load(open(glob.glob('audio/*_small_en.json')[0])); words = [(x['start'], x['end'], x['word'].strip()) for sg in asr['segments'] for x in sg['words']]
M = json.load(open('build/phrase_pairs.json')); views = json.load(open('build/views.json')); byf = {int(e['start_frame']): e for e in ev}; rows = []
for f, wd, t0 in M:
    cands = [k for k, x in enumerate(words) if x[2].lower().strip('.,?!') == wd.lower().strip('.,?!')]; assert cands, (f, wd)
    j = min(cands, key=lambda k: abs(words[k][0] - t0)); e = byf.get(f); vt = float(e['start_pts_seconds']) if e else pts(f)
    rows.append(dict(video_id=VID, event_id=(e['event_id'] if e else f'E-f{f}'), audio_source='local ASR openai-whisper small.en word timestamps', audio_listening_status='ASR_UNCERTIFIED - NO HUMAN LISTENING',
        phrase_or_sound=f"[{words[j][2]}] …{' '.join(x[2] for x in words[max(0,j-3):j+4])}…", audio_start_pts=round(words[j][0], 3), audio_end_pts=round(words[j][1], 3), visual_start_pts=vt, visual_end_pts=(e['end_pts_seconds'] if e else vt),
        lead_lag_seconds=round(vt - words[j][0], 3), timestamp_method='semantically chosen word (phrase the graphic illustrates) vs visual PTS (frame-exact where onset EXACT)', confidence='MEDIUM', limitations='ASR word timing +/-0.1-0.3 s; chosen pairing is my reading (INFERRED), not heard'))
with open('audio_visual_alignment_phrase.csv', 'w', newline='') as fh:
    q = csv.DictWriter(fh, fieldnames=list(rows[0])); q.writeheader(); q.writerows(rows)
lags = [r['lead_lag_seconds'] for r in rows]; random.seed(1); starts = sorted(x[0] for x in words); dur_s = N / FPS
base = [min(abs(t - s) for s in starts) for t in (random.uniform(0, dur_s) for _ in range(5000))]
phr = dict(n=len(lags), median=S.median(lags), p10=sorted(lags)[len(lags)//10], p90=sorted(lags)[9*len(lags)//10], within_0_1=sum(abs(x) <= 0.1 for x in lags), within_0_3=sum(abs(x) <= 0.3 for x in lags), visual_early=sum(x < 0 for x in lags), visual_late=sum(x > 0 for x in lags),
           random_within_0_1=round(sum(b <= 0.1 for b in base) / len(base), 3), random_within_0_3=round(sum(b <= 0.3 for b in base) / len(base), 3))
json.dump(phr, open('tables/phrase_alignment_summary.json', 'w'), indent=1)
v = man['video']
head = f"""# Visual CT scan report - {VID} (Casual Finance) - visual-only scope
Reader: Claude Sonnet 5.5, Machine A, {datetime.date.today()}. Mode CT_SCAN (visual). Audio: ASR only, never heard. See `quality_gate.json` (visual-only, declared coverage; AV sign-off BLOCKED).

## 1. Source and coverage (MEASURED, generated)
- File `{os.path.basename(man['source_path'])}`; SHA-256 `{man['source_sha256']}`; {man['bytes']:,} bytes. Identity: filename `[ID]` and roster/queue EXACT_ID_MATCH where stated; live YouTube not re-checked.
- {v['codec']} {v['w']}x{v['h']} {v['pix_fmt']}, {v['avg_frame_rate']} fps, {man['cfr_assessment']}: {N} frames, delta {man['frame_delta_distinct']} s, PTS = frame/{FPS}, last PTS {man['pts_last']:.3f}; {man['iframes']} I-frames.
- Pass 1 (MEASURED): all {N} frames decoded once; 320 px changed-fraction, mean abs difference, luma, 4x4 grid, full-res changed pixels -> `tables/frame_metrics.csv`; {kf['episodes']} candidate episodes -> `tables/episodes.csv`.
- Pass 2 (OBSERVED): 1 fps overview, all {kf['episodes']} episodes viewed ({views.get('episode_view', 'decoded frames start-1/start/mid/end/end+1')}), {len(views['native_windows'])} native consecutive-frame windows, {len(views['stepped_sheets'])} stepped sheets, one representative decoded frame per state ({kf['states']}) compared with the ledger. No interpolated frames.
- Result: {kf['states']} states contiguous f0-f{N-1}; {kf['shots']} shots; {kf['hard_cuts']} hard cuts + start; {kf['events']} events; onset precision {kf['exact_onsets']} EXACT, {kf['bound_onsets']} BOUND (<= 6-frame windows), rest MEAS (activity edge).
"""
tail = f"""
## Audio alignment (generated; ASR_UNCERTIFIED - nobody listened)
- Whisper small.en text: {asr['text'].strip()}
- Phrase-level pairs ({phr['n']}, `audio_visual_alignment_phrase.csv`): median visual-minus-word lag {phr['median']:.3f} s, p10 {phr['p10']:.3f}, p90 {phr['p90']:.3f}; {phr['within_0_1']}/{phr['n']} within 0.1 s, {phr['within_0_3']}/{phr['n']} within 0.3 s; visual leads in {phr['visual_early']}, trails in {phr['visual_late']}. Control: random times lie within 0.1 s of some word start {phr['random_within_0_1']:.0%} and within 0.3 s {phr['random_within_0_3']:.0%} of the time, so closeness alone is weak evidence; the pairing of the right word is the evidence.
- Nearest-word table for all non-hold events: `audio_visual_alignment.csv` ({asum['events']} rows, median lag {asum['median_lag']:.3f} s). Music, SFX, tone: UNAVAILABLE.
"""
open('visual_ct_scan_report.md', 'w').write(head + '\n' + open('build/report_body.md').read() + '\n' + tail)
timeline = '\n'.join(f"- {s['visual_state_id']} f{s['start_frame']}-f{s['end_frame']} ({s['frames']} fr): {s['entering_class']} - {s['label']}" for s in st)
open('reconstruction_blueprint.md', 'w').write(f"""# Reconstruction blueprint - original asset system derived from {VID}
New ORIGINAL assets and motion only. No source screenshot, footage, logo or character drawing is copied; third-party items (`IMG_*`, `ICON_*`) are replaced with licensed or self-made equivalents and your own data. Timings at {FPS} fps, {v['w']}x{v['h']}.

{open('build/modules.md').read()}

## Editor timeline (frames)
{timeline}

## Per-state prompts
All {kf['states']} image and animation prompts with static anchors and nearest-frame QA: `PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json`.

## Acceptance tests
1. Cut frames equal the ledger exactly ({', '.join(str(f) for f in kf['cut_frames'])}).
2. EXACT onsets match to the frame; BOUND onsets fall inside their window.
3. Static anchors are pixel-still between events.
4. Total length {N} frames.
5. Sound unspecified (nobody listened); ASR lines are timing reference only.
""")
json.dump(dict(video_id=VID, source_sha256=man['source_sha256'], mode='CT_SCAN (visual-only)', frames_total=N, frames_measured=N, frames_measured_fraction=1.0, episodes_total=kf['episodes'], episodes_viewed=kf['episodes'], states=kf['states'],
  native_windows_viewed=views['native_windows'], stepped_sheets=views['stepped_sheets'], representative_state_frames_viewed=kf['states'], onset_precision=dict(EXACT=kf['exact_onsets'], BOUND=kf['bound_onsets']),
  unseen='quiet frames inside holds measured unchanged (thr 0.06 % / 300 px) but not individually viewed', resolution_floor='~35 px at 320 px scale; 300 changed full-res px', audio='ASR only (small.en); never listened; AV not signed off'), open('coverage.json', 'w'), indent=1)
json.dump(dict(video_id=VID, source_sha256=man['source_sha256'], requested_mode='CT_SCAN', scope='visual-only; audio/AV tracked separately', reviewer=f'Claude Sonnet 5.5, Machine A, {datetime.date.today()}',
  gates=dict(source_identity='PASS (hash computed; filename ID/registry attribution; live YouTube not re-checked)', full_temporal_overview=f'PASS (all {N} frames measured; 1 fps overview)', candidate_shots_verified=f"PASS ({kf['hard_cuts']} hard cuts verified on adjacent decoded frames; {kf['episodes']}/{kf['episodes']} episodes viewed)",
    meaningful_state_timing=f"PASS_WITH_DECLARED_BOUNDS ({kf['exact_onsets']} EXACT, {kf['bound_onsets']} BOUND, rest measured activity edges)", motion_design_review='PASS (classified; easing UNAVAILABLE)', creative_design_review='PASS (palette measured; typography labelled)',
    on_screen_text=views.get('text_gate', 'PARTIAL_OPEN_LIMITATION (small text flagged not guessed)'), visual_script_mapping=f"PROVISIONAL_ASR_ONLY ({phr['n']} semantic pairs, control baseline reported)", production_blueprint=f"PASS ({kf['states']} per-state prompts, modules, timeline, acceptance tests)",
    audio_human_listening='NOT_COMPLETED', final_av_signoff='BLOCKED', ct_scan_complete='PASS_VISUAL_ONLY'), final_video_status='VISUAL_CT_SCAN_COMPLETE_WITH_EVIDENCE (visual-only, declared coverage)', full_av_signoff='NO',
  limitations=['no human listening', 'ASR unverified', 'quiet-frame interiors not individually viewed', 'sub-threshold changes undetectable', 'pan/ease curves and typefaces not measured', 'live thumbnail/title not re-fetched', 'on-screen figures not fact-checked'], next_step='counts only if validate.py exits 0'), open('quality_gate.json', 'w'), indent=1)
open('continuation_handoff.md', 'w').write(f"""# Handoff - {VID} ({datetime.date.today()})
Visual-only CT scan built; validator `build/validate.py`. Pending outside scope: human listening (AV BLOCKED), live thumbnail/title identity. Source SHA-256 {man['source_sha256']}. Workspace {os.getcwd()} (local only; media never in Git).
Tools: ~/YIOS-local-audits/tooling/cf15/*.py (ingest, measure, episodes, sheets, windows, stepsheet, repsheets, build_all, build_docs, validate) + tooling/visual-ct-scan-venv; ASR with system python3 -E whisper small.en. Machine A; writer lock claude-cf15-20261108.
""")
files = sorted(f for f in glob.glob('**/*', recursive=True) if os.path.isfile(f) and f != 'EVIDENCE_SHA256SUMS' and '__pycache__' not in f)
open('EVIDENCE_SHA256SUMS', 'w').write(''.join(f"{hashlib.sha256(open(f,'rb').read()).hexdigest()}  {f}\n" for f in files)); print(len(files), 'files sealed;', json.dumps(phr))
