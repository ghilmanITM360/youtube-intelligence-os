# Barely Evolved: method change log (N17, 2026-11-05)

Original results are kept: `r13_blind/CAMERA_ENDPOINT_CHECK.csv` (M0), `dense/CAMERA_CHAIN_ALL_<vid>.csv` (M2), `r13_blind/BLIND_RECONCILIATION.csv` (N16 reconciliation), and every N16 column of ledger v2. `reconcile_v3.py` asserts those columns still equal the N16 commit.

| Version | Change | Status | Scope | Rows affected |
|---|---|---|---|---|
| M0 | Endpoint similarity check, frozen in `cam_endpoint.py` | Preregistered | 11 UNCERTAIN claims only | 11 |
| M1 | Chain over links of at most 10 frames | Introduced after observation, not preregistered | Then all 850 | 850 re-measured; 494 verified-size moves |
| M2 | M1 plus inlier spread at least 0.5 of frame width and height | Introduced after observation, not preregistered | All 850 | 256 of those became NO_FRAMEWIDE_SUPPORT; 238 stayed verified |
| M3 | M2 fit plus entry link, edge evidence `moved_share`, oscillation flag | Post-hoc and exploratory. Frozen by hash in `M3_RULE_FREEZE.json` before the 850-row run | All 850 | 368 rows changed category beyond renaming |
| R-v3 R1 | A cut at end+1 can no longer set the interior class; hardcoded CHARACTER removed | Post-hoc correction | 6 batch 1 rows and 6 batch 2 rows with a boundary cut | 3 classes changed: [['mNLN-U0039', 'CHARACTER', 'MIXED'], ['mNLN-U0283', 'CHARACTER', 'MIXED'], ['mNLN-U0284', 'CHARACTER', 'CAMERA']]. mNLN-U0173 kept CHARACTER, now on native evidence |
| R-v3 R3 | LOW tile rows still adopt the blind label, but are flagged when M3 conflicts | Post-hoc correction | 21 rows | 6 flagged, not changed: ['mNLN-U0189', 'mNLN-U0231', 'mNLN-U0254', 'GNaB-U0109', 'GNaB-U0192', 'GNaB-U0239'] |

M0 re-applied to all 850 for sensitivity only (it was never preregistered for them): {'CAMERA_VERIFIED': 368, 'CAMERA_REJECTED': 207, 'UNRESOLVED': 275}. M1: {'CAMERA_VERIFIED': 494, 'NOT_APPLICABLE': 96, 'UNRESOLVED': 86, 'CAMERA_REJECTED': 174}. M2: {'NO_FRAMEWIDE_SUPPORT': 256, 'NOT_APPLICABLE': 96, 'UNRESOLVED': 86, 'CAMERA_REJECTED': 174, 'CAMERA_VERIFIED': 238}. M3: {'WHOLE_CONTENT_MOVE': 150, 'NO_CAMERA': 232, 'UNRESOLVED_PARTIAL': 93, 'UNRESOLVED': 86, 'CAMERA_FRAMEWIDE': 231, 'OBJECT_MOVE': 39, 'NOT_APPLICABLE': 14, 'UNRESOLVED_OSCILLATION': 5}.
The 11 original claims under M3: [('uPQc-U0030', 'CAMERA_VERIFIED', 'CAMERA_FRAMEWIDE'), ('uPQc-U0066', 'CAMERA_VERIFIED_', 'UNRESOLVED_PARTIAL'), ('mNLN-U0019', 'CAMERA_VERIFIED', 'CAMERA_FRAMEWIDE'), ('mNLN-U0028', 'CAMERA_VERIFIED', 'CAMERA_FRAMEWIDE'), ('mNLN-U0029', 'CAMERA_VERIFIED', 'CAMERA_FRAMEWIDE'), ('mNLN-U0081', 'CAMERA_VERIFIED', 'CAMERA_FRAMEWIDE'), ('mNLN-U0169', 'CAMERA_VERIFIED', 'CAMERA_FRAMEWIDE'), ('mNLN-U0228', 'CAMERA_REJECTED', 'UNRESOLVED'), ('mNLN-U0258', 'CAMERA_VERIFIED', 'CAMERA_FRAMEWIDE'), ('mNLN-U0281', 'CAMERA_VERIFIED', 'CAMERA_FRAMEWIDE'), ('GNaB-U0200', 'CAMERA_REJECTED', 'NO_CAMERA')].

## Validation
- **Synthetic controls:** `camera_m3.py --selfcheck` passes 8 cases. The first run exposed a metric bug, fixed before the freeze; the self-check therefore also shaped the rule.
- **Sampled rows (not independent, these rows informed the design):** M3 suggestion equals the native label on 22/36. Of 8 CAMERA_FRAMEWIDE calls, 7 matched and uPQc-U0018 did not. Disagreements: [['uPQc-U0018', 'CHARACTER', 'MIXED', 'CAMERA_FRAMEWIDE'], ['uPQc-U0089', 'SHOT_CUT', 'UNRESOLVED', 'NOT_APPLICABLE'], ['uPQc-U0107', 'CHARACTER', 'UNRESOLVED', 'UNRESOLVED_PARTIAL'], ['uPQc-U0141', 'CHARACTER', 'WHOLE_CONTENT_MOVE', 'WHOLE_CONTENT_MOVE'], ['mNLN-U0002', 'CHARACTER', 'WHOLE_CONTENT_MOVE', 'WHOLE_CONTENT_MOVE'], ['mNLN-U0081', 'MIXED', 'CAMERA', 'CAMERA_FRAMEWIDE'], ['mNLN-U0123', 'MIXED', 'LOCAL_CHANGE', 'OBJECT_MOVE'], ['mNLN-U0214', 'MIXED', 'CAMERA', 'CAMERA_FRAMEWIDE'], ['GNaB-U0077', 'WHOLE_CONTENT_MOVE', 'UNRESOLVED', 'UNRESOLVED_PARTIAL'], ['GNaB-U0113', 'MIXED', 'WHOLE_CONTENT_MOVE', 'WHOLE_CONTENT_MOVE'], ['GNaB-U0170', 'MIXED', 'UNRESOLVED', 'UNRESOLVED_PARTIAL'], ['GNaB-U0193', 'CHARACTER', 'UNRESOLVED', 'UNRESOLVED'], ['GNaB-U0209', 'MIXED', 'UNRESOLVED', 'UNRESOLVED'], ['GNaB-U0235', 'CAMERA', 'WHOLE_CONTENT_MOVE', 'WHOLE_CONTENT_MOVE']].
- **Held-out sample:** 24 rows, seed 20261106, 6 per label, none used before. Anonymised sheets were labelled and hashed before the key was read (`HELDOUT_LABELS_FREEZE.json`, `HELDOUT_RESULT.csv`).

| M3 label | Match | Reading |
|---|---|---|
| CAMERA_FRAMEWIDE | 6/6 | Usable as a camera decision |
| NO_CAMERA | 6/6 | Usable as a no-camera decision |
| WHOLE_CONTENT_MOVE | 2/6 | **Not validated.** Misses [['H01', 'GNaB-U0105', 'CAM'], ['H18', 'mNLN-U0141', 'CAM'], ['H19', 'mNLN-U0131', 'CAM'], ['H24', 'uPQc-U0116', 'CAM']] were full-frame scenes with real camera-like motion; read only as "camera not established" |
| OBJECT_MOVE | 4/6 | **Not validated.** Misses [['H17', 'uPQc-U0022', 'WCM'], ['H23', 'GNaB-U0267', 'CAM']]; read only as "camera not established" |

Thresholds were not changed after this result, because that would spend the held-out sample. Limits: small n, one same-vendor reader, first and last frames only.
