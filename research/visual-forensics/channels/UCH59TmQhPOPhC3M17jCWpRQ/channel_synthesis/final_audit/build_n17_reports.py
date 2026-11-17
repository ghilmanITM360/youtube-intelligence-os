# Builds matrix v3, per-video gates, audit report v3, N16 addendum, method log, R20 verification and handoff from reconciled ledgers and fresh validation.
import csv, json, re, collections
from pathlib import Path
F = Path('.').resolve(); N = F.parent / 'nonaudio_completion'; M = N / 'method_v3'; VIDS = ['uPQcyookL0Y', 'mNLNb-Z4T0M', 'GNaBxt_zIRA']
val = json.load(open('FINAL_VALIDATION_v3_pre_N17.json')); summ = json.load(open(N / 'r13_blind/BLIND_RECONCILIATION_v3_summary.json')); sens = json.load(open(M / 'METHOD_SENSITIVITY.json'))
L = {v: list(csv.DictReader(open(N / f'dense_review/DENSE_REVIEW_LEDGER_{v}_v2.csv'))) for v in VIDS}; cov = {}
for v, R in L.items():
    d = [tuple(map(int, re.match(r'(\d+)/(\d+)', r['density']).groups())) for r in R]
    cov[v] = dict(intervals=len(R), frames_measured=sum(int(r['n_frames']) for r in R), interior_seen=sum(a for a, b in d), interior_total=sum(b for a, b in d), intervals_all_viewed=sum(a >= b for a, b in d), named_tiles=sum(r['review_status'] == 'VISUALLY_NAMED_TILES' for r in R), native_crop=sum(r['review_status'] != 'VISUALLY_NAMED_TILES' for r in R), blind=sum(bool(r['blind_sample'] or r['blind2_event_class']) for r in R), orch_native=sum(r['final_basis'] == 'NATIVE_ORCH' for r in R), cam_framewide=sum(r['camera_m3'] == 'CAMERA_FRAMEWIDE' for r in R), cam_notest=sum(r['camera_m3'] in ('WHOLE_CONTENT_MOVE', 'OBJECT_MOVE', 'UNRESOLVED', 'UNRESOLVED_PARTIAL', 'UNRESOLVED_OSCILLATION') for r in R), unnamed_strict=sum(r['camera_m3'] == 'CAMERA_FRAMEWIDE' and r['event_class'] not in ('CAMERA', 'DIGITAL_ZOOM', 'MIXED') for r in R), flags=[r['interval_id'] for r in R if r['final_flag']])
claims = [(r['interval_id'], r['camera_claim_resolution_v2'][:16], r['camera_m3']) for v in VIDS for r in L[v] if r['camera_claim_resolution_v2']]
QUOTE = 'Describe actual reviewer independence accurately. Do not invent an additional human-review requirement unless the kit explicitly requires it.'
LOC = 'owner final-audit prompt, session 1e8761b1 transcript line 14, 2026-11-04T16:41:27Z (same text in session 7a28d062 line 2442); owner N15 prompt 2026-11-05T16:15:12Z asks whether independence means a separate reviewer or an explicitly different vendor/model and states same vendor is not automatically a failure'
KIT = 'visual-ct-scan 13_completion_gates_validation_handoffs.md:44 asks quality_gate.json for a reviewer locator; 10_script_and_creator_brain.md:22 warns a simulated panel is not independent validation; no kit file requires a different vendor or a human'
M0 = list(csv.DictReader(open('FINAL_AUDIT_MATRIX_v2.csv'))); fields = list(M0[0]) ; out = []
for r in M0:
    r = dict(r); q = r['req_id']; tag = 'N17 2026-11-05 (session 15f69c1b)'
    for v in VIDS:
        c = cov[v]; x = val[v]
        if q == 'R05':
            r[v] = 'PASS_WITHIN_DECLARED_COVERAGE'; r['evidence_' + v] = f"MEASURED: all {c['frames_measured']} frames of {c['intervals']} intervals (dense motion + M3 camera). VISUALLY INSPECTED: {c['interior_seen']}/{c['interior_total']} interior frames viewed by reviewers; {c['intervals_all_viewed']} intervals all frames viewed; {c['named_tiles']} named from tiles, {c['native_crop']} on native crops; {c['blind']} blind rows; {c['orch_native']} rows on orchestrator native frames. Camera: {c['cam_framewide']} CAMERA_FRAMEWIDE; {c['cam_notest']} camera not established (declared)."
        if q == 'R07':
            r[v] = 'PASS_WITHIN_DECLARED_COVERAGE'; r['evidence_' + v] = f"MEASURED: every long-state interior frame ({c['frames_measured']} frames). VISUALLY INSPECTED: only {c['interior_seen']}/{c['interior_total']} interior frames; {c['intervals_all_viewed']}/{c['intervals']} intervals fully viewed. Measured-only frames are not claimed as seen."
        if q == 'R13':
            r[v] = 'PASS'; r['evidence_' + v] = f"Criterion: \"{QUOTE}\" ({LOC}). {KIT}. Met by separate blind contexts (batch 1 69 rows, batch 2 30 rows; frozen briefs; no ledger access; image blocks present in transcripts: 24 and 11 sheet reads). LIMIT: reviewers and orchestrator are all Claude models (same vendor), adjudication is by the orchestrator who saw measurements. Optional cross-vendor review not run; not required."
        if q == 'R16': r['evidence_' + v] = 'FINAL_THREE_VIDEO_AUDIT_v3.md + CHANNEL_SYNTHESIS_v1_2.md (v1/v2 reports kept)'
        if q == 'R18': r[v] = 'PASS' if not x['seal']['mismatches'] else 'FAIL'; r['evidence_' + v] = f"{x['seal']['file']} {x['seal']['entries']} entries, {len(x['seal']['mismatches'])} mismatches (fresh, FINAL_VALIDATION_v3_pre_N17.json)"
        if q == 'R19':
            b = x['remote_readback']; r[v] = 'PASS' if not b['sha_mismatch_vs_local'] and not b['invalid_json'] else 'FAIL'; r['evidence_' + v] = f"{b['remote_files']} remote files at {val['remote_sha'][:8]}, {len(b['sha_mismatch_vs_local'])} sha mismatches, {b['remote_only_or_unmapped']} unmapped, {len(b['invalid_json'])} invalid json (fresh)"
        if q == 'R20': r[v] = 'PARTIAL'; r['evidence_' + v] = 'Package verified fresh (nonaudio_completion/portability/R20_VERIFY_N17.json). Actual off-device transfer BLOCKED: no approved destination provided. Same-device test is not backup.'
        if q == 'R22': r[v] = 'FAIL'; r['evidence_' + v] = 'VISUAL_ANALYSIS_PARTIAL. CT_SCAN_COMPLETE not awarded. Unmet: R08 PARTIAL (ASR only), R09 BLOCKED (no listening), R21 BLOCKED (no AV sign-off), R20 PARTIAL (transfer pending).'
    if q in ('R05', 'R07', 'R13', 'R16', 'R18', 'R19', 'R20', 'R22'): r['checked_this_audit'] = tag
    out.append(r)
with open('FINAL_AUDIT_MATRIX_v3.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(out)
assert all(val[v]['remote_readback']['sha_mismatch_vs_local'] == [] for v in VIDS)
tally = collections.defaultdict(list)
for r in out: tally[r['uPQcyookL0Y']].append(r['req_id'])
for v in VIDS:
    g = {m['req_id'] + ' ' + m['requirement']: dict(status=m[v], evidence=m['evidence_' + v]) for m in out}
    o = dict(video_id=v, audit='BE N17 close-out 2026-11-05 (session 15f69c1b)', status='VISUAL_ANALYSIS_PARTIAL', CT_SCAN_COMPLETE=False, FULL_AV_SIGNOFF=False, non_audio_verdict='ANALYSIS_REPORTING_COMPLETE__OFF_DEVICE_PORTABILITY_PENDING', NON_AUDIO_COMPLETE=False, remaining_non_audio=['R20 off-device transfer BLOCKED: destination not provided'], excluded_audio=['R08 PARTIAL (ASR only)', 'R09 BLOCKED', 'R21 BLOCKED'], reviewer='blind: separate Claude contexts; orchestrator: Claude Opus 5.5; same vendor', gates=g, supersedes='quality_gate_NAC.json and quality_gate_FINAL.json kept unchanged')
    json.dump(o, open(next(Path('kit_outputs').glob(f'{v}_*')) / 'quality_gate_N17.json', 'w'), indent=1)
b2 = summ['batch2']; h = summ['heldout']; mv = summ['m3_vs_native']; flags = sum((cov[v]['flags'] for v in VIDS), [])
s2 = sens['M2_chain_spread']; s3 = sens['M3']; s1 = sens['M1_chain']; s0 = sens['M0_endpoint_reapplied']; changed_m3 = sum(n for k, n in sens['M2_to_M3'].items() if k.split('->')[0] != k.split('->')[1] and k not in ('CAMERA_VERIFIED->CAMERA_FRAMEWIDE', 'CAMERA_REJECTED->NO_CAMERA'))
us = sum(cov[v]['unnamed_strict'] for v in VIDS); changed = summ['batch1']['changed_from_v2']
(N / 'method_v3/METHOD_CHANGE_LOG_N17.md').write_text(f"""# Barely Evolved: method change log (N17, 2026-11-05)

Original results are kept: `r13_blind/CAMERA_ENDPOINT_CHECK.csv` (M0), `dense/CAMERA_CHAIN_ALL_<vid>.csv` (M2), `r13_blind/BLIND_RECONCILIATION.csv` (N16 reconciliation), and every N16 column of ledger v2. `reconcile_v3.py` asserts those columns still equal the N16 commit.

| Version | Change | Status | Scope | Rows affected |
|---|---|---|---|---|
| M0 | Endpoint similarity check, frozen in `cam_endpoint.py` | Preregistered | 11 UNCERTAIN claims only | 11 |
| M1 | Chain over links of at most 10 frames | Introduced after observation, not preregistered | Then all 850 | 850 re-measured; {s1['CAMERA_VERIFIED']} verified-size moves |
| M2 | M1 plus inlier spread at least 0.5 of frame width and height | Introduced after observation, not preregistered | All 850 | {s2['NO_FRAMEWIDE_SUPPORT']} of those became NO_FRAMEWIDE_SUPPORT; {s2['CAMERA_VERIFIED']} stayed verified |
| M3 | M2 fit plus entry link, edge evidence `moved_share`, oscillation flag | Post-hoc and exploratory. Frozen by hash in `M3_RULE_FREEZE.json` before the 850-row run | All 850 | {changed_m3} rows changed category beyond renaming |
| R-v3 R1 | A cut at end+1 can no longer set the interior class; hardcoded CHARACTER removed | Post-hoc correction | 6 batch 1 rows and 6 batch 2 rows with a boundary cut | 3 classes changed: {changed}. mNLN-U0173 kept CHARACTER, now on native evidence |
| R-v3 R3 | LOW tile rows still adopt the blind label, but are flagged when M3 conflicts | Post-hoc correction | 21 rows | {len(flags)} flagged, not changed: {flags} |

M0 re-applied to all 850 for sensitivity only (it was never preregistered for them): {s0}. M1: {s1}. M2: {s2}. M3: {s3}.
The 11 original claims under M3: {claims}.

## Validation
- **Synthetic controls:** `camera_m3.py --selfcheck` passes 8 cases. The first run exposed a metric bug, fixed before the freeze; the self-check therefore also shaped the rule.
- **Sampled rows (not independent, these rows informed the design):** M3 suggestion equals the native label on {mv['agree']}/{mv['rows']}. Of {len(mv['framewide_claims'])} CAMERA_FRAMEWIDE calls, 7 matched and uPQc-U0018 did not. Disagreements: {mv['disagreements']}.
- **Held-out sample:** 24 rows, seed 20261106, 6 per label, none used before. Anonymised sheets were labelled and hashed before the key was read (`HELDOUT_LABELS_FREEZE.json`, `HELDOUT_RESULT.csv`).

| M3 label | Match | Reading |
|---|---|---|
| CAMERA_FRAMEWIDE | {h['CAMERA_FRAMEWIDE']['match']}/6 | Usable as a camera decision |
| NO_CAMERA | {h['NO_CAMERA']['match']}/6 | Usable as a no-camera decision |
| WHOLE_CONTENT_MOVE | {h['WHOLE_CONTENT_MOVE']['match']}/6 | **Not validated.** Misses {h['WHOLE_CONTENT_MOVE']['misses']} were full-frame scenes with real camera-like motion; read only as "camera not established" |
| OBJECT_MOVE | {h['OBJECT_MOVE']['match']}/6 | **Not validated.** Misses {h['OBJECT_MOVE']['misses']}; read only as "camera not established" |

Thresholds were not changed after this result, because that would spend the held-out sample. Limits: small n, one same-vendor reader, first and last frames only.
""")
(N / 'NAC_PROGRESS_N16_ADDENDUM_N17.md').write_text("""# Addendum to NAC_PROGRESS_N16.md (N17, 2026-11-05)

`NAC_PROGRESS_N16.md` is published evidence at 16bd0cc7 and stays unchanged.

**Count correction.** It says "23 where the blind label was adopted (21 LOW tile-only rows plus 1 random row)". The right count is **22** (21 + 1), as `r13_blind/BLIND_RECONCILIATION_summary.json` records (BLIND_ADOPTED_NATIVE_CROP 21, BLIND_ADOPTED 1). The batch 1 total still sums to 69: 37 + 5 + 2 + 22 + 1 + 2.

**Method wording.** `scripts/camera_all_intervals.py`, published in N16, calls the chained measure with the inlier-spread condition a "frozen rule". Only M0 was preregistered; see `method_v3/METHOD_CHANGE_LOG_N17.md`.

**Superseded class.** The N16 reconciliation set mNLN-U0284 to CHARACTER through a weak rule. N17 records CAMERA in new ledger columns. The N16 column is kept.

**Batch 2 sheets.** The batch 2 brief names sheets `<VID>_B###.jpg`, while the files are `<VID>_D###.jpg`. The reviewer read all 11.
""")
(N / 'portability/R20_VERIFY_N17.json').write_text(json.dumps(dict(utc='2026-11-05', session='15f69c1b', package_items=17, package_bytes=249052569, sha256_mismatches=0, existing_all=True, status='PARTIAL', transfer='BLOCKED: approved off-device destination not provided', same_device_test='procedure test only; not backup',
  editable_sources='render.py, spec, timeline and evaluations for all 13 RT folders are in Git; render.py draws procedurally and reads no external art asset in the strings checked',
  not_git_not_packaged='QC sheets only (.jpg/.png) in RT folders; regenerated by render or review scripts', dependencies=dict(lock_file='packaged', fonts='5 of 6 listed fonts hash-match; /Library/Fonts/Bradley Hand Bold.ttf is missing on this Mac (RT-V2-S02 references it)', runtime='recorded in manifest; not packaged', hardcoded_paths='RT-V3-S01 absolute path; several render.py use /tmp scratch paths'),
  gaps=['4 calibration extracts in style_rt/source_calibration_local_only (11.8 MB) are not in the package; regenerable from source MP4 but not byte-verified', 'manifest git base_commit still names 0c1eeaad; use the current branch head']), indent=1))
rows = lambda st: ', '.join(tally[st])
(F / 'FINAL_THREE_VIDEO_AUDIT_v3.md').write_text(f"""# Barely Evolved: three-video audit v3 (N17, 2026-11-05)

Session 15f69c1b. Kit visual-ct-scan v1.0. Supersedes `FINAL_THREE_VIDEO_AUDIT_v2.md` (kept) for the rows below.

## Decision
**Analysis/reporting complete; off-device portability pending.** `NON_AUDIO_COMPLETE` is not awarded, because R20 needs an off-device transfer. `CT_SCAN_COMPLETE` is not awarded, because audio gates are unmet.

## Matrix (`FINAL_AUDIT_MATRIX_v3.csv`)
| Status | Rows |
|---|---|
""" + ''.join(f"| {k} | {rows(k)} |\n" for k in sorted(tally)) + f"""
**R22 unmet dependencies:** R08 PARTIAL (ASR only), R09 BLOCKED (no listening), R21 BLOCKED (no AV sign-off), R20 PARTIAL (transfer pending).

## R05/R07: measured coverage and visual inspection are separate
| Video | Intervals | Frames measured | Interior frames viewed | Intervals fully viewed | Blind rows | Orchestrator native rows | CAMERA_FRAMEWIDE | Camera not established |
|---|---|---|---|---|---|---|---|---|
""" + ''.join(f"| {v} | {c['intervals']} | {c['frames_measured']} | {c['interior_seen']}/{c['interior_total']} | {c['intervals_all_viewed']} | {c['blind']} | {c['orch_native']} | {c['cam_framewide']} | {c['cam_notest']} |\n" for v, c in cov.items()) + f"""
Measured frames were not all seen. PASS applies within this declared coverage.

## Batch 2
All 30 rows were tile-only STATIC_HOLD labels that measurement contradicted, so this is a targeted sample and not a population error rate.
- Ledger STATIC_HOLD confirmed {b2['ledger_static_confirmed']}, corrected {b2['ledger_static_corrected']}.
- Blind class upheld {b2['blind_class_upheld']}, differs {b2['blind_class_differs']}.
- Final classes: {b2['final']}.
- Attribution: {b2['attribution']}. 12 rows stay unresolved on camera attribution (10 camera vs artwork slide, 2 subthreshold).

## Methods
See `nonaudio_completion/method_v3/METHOD_CHANGE_LOG_N17.md`. Only M0 was preregistered. M1, M2, M3 and R-v3 came after observation. Frame-wide moves the ledger class did not name (excluding MIXED): {us} under M3; the N16 note reported 173 under M2.

## Open evidence items
- {len(flags)} R3 rows flagged where the blind label conflicts with M3, not re-inspected: {flags}.
- Ledger CAMERA rows with M3 NO_CAMERA or OBJECT_MOVE are flagged in `camera_m3_vs_ledger`, not changed. Rows outside the samples keep their ledger class.

## R13
**PASS.** Criterion: "{QUOTE}" Location: {LOC}. {KIT}. Limit: every reviewer and the orchestrator are Claude models, so this is separate-context independence, not vendor independence. Cross-vendor review was not run and is not required.

## R18/R19
Fresh values before N17 (`FINAL_VALIDATION_v3_pre_N17.json`), remote {val['remote_sha'][:8]}:
""" + ''.join(f"- {v}: {val[v]['seal']['file']} {val[v]['seal']['entries']} entries, {len(val[v]['seal']['mismatches'])} mismatches; {val[v]['remote_readback']['remote_files']} remote files, {len(val[v]['remote_readback']['sha_mismatch_vs_local'])} sha mismatches, {val[v]['remote_readback']['remote_only_or_unmapped']} unmapped.\n" for v in VIDS) + f"""- channel_synthesis: {val['channel_synthesis']['seal']} {val['channel_synthesis']['entries']} entries; {len(val['channel_synthesis']['seal_mismatches'])} files differ: the 3 v2 ledgers (N17 columns appended) and scripts/blind_adjudicate_measure.py (edited for batch 2 after the N16 seal); all re-sealed by N17.

## R20
The 17-item package is verified fresh (249,052,569 bytes, 0 hash mismatches). See `portability/R20_VERIFY_N17.json` for sources, dependencies and gaps. Transfer BLOCKED; R20 PARTIAL.

## Remaining
1. R20: owner names an approved off-device destination; then run `scripts/stage_and_verify.sh <DEST>`.
2. Audio: R08, R09, R21 need actual listening.
""")
(N / 'NAC_HANDOFF_N17.md').write_text(f"""# Barely Evolved: handoff N17 (2026-11-05)

Session 15f69c1b. Branch research/barely-evolved-visual-forensics. Base 16bd0cc7. The N17 commit and readback are in `evidence/N17_PUBLICATION_RECEIPT.json` on Machine A and in BE_OPS_LOG.

- **Status:** Analysis/reporting complete; off-device portability pending. Report: `final_audit/FINAL_THREE_VIDEO_AUDIT_v3.md`. Gates: `kit_outputs/<vid>_*/quality_gate_N17.json`.
- **Lock:** taken over from idle session 1e8761b1 by recorded transfer (`evidence/LOCK_OWNER_at_transfer_1e8761b1_to_15f69c1b.txt`), released after N17.
- **Next, owner:** name an off-device destination for R20, or arrange listening for audio.
- **Optional, not required:** inspect flagged R3 rows {flags}; cross-vendor review needs explicit authorization.
- **Re-verify:** from `final_audit/`, `/usr/bin/python3 be_final_validate_v3.py OUT.json`. OpenCV work uses `~/YIOS-local-audits/tooling/visual-ct-scan-venv/bin/python3`.
""")
print(json.dumps({k: tally[k] for k in tally}), cov['mNLNb-Z4T0M']['interior_seen'], us, changed_m3, flags); print({v: (val[v]['seal']['file'][-4:], val[v]['seal']['entries'], val[v]['remote_readback']['remote_files']) for v in VIDS}, val['channel_synthesis']['seal'], val['channel_synthesis']['entries'], val['channel_synthesis']['seal_mismatches'][:8], val['channel_synthesis'].get('remote_readback', {}).get('remote_files'))
