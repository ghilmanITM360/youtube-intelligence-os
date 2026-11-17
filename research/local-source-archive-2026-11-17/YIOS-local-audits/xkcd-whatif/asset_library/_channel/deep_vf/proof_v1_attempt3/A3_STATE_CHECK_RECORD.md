# Attempt 3 — state-change check: original vs revised result (retained separately; LOCAL ONLY)
Identified MP4s (sha256 re-computed this pass, match PROOF_RESULTS_attempt3.md):
- proof_v1_attempt3/proof_16x9.mp4 92c85f73d8397e383d8e3dd74944c6fa0886a9d94dc17a7cc023ec89769f539f
- proof_v1_attempt3/proof_9x16.mp4 aab0b65d536366eac1d3980f67520b93559f0abb51aa795c3c35a24c8e628e7e
(Attempt 2 = proof_v1/*.mp4 9be9c9e1…, 89a55d73… — not the files to review.)

| Check | 16:9 MELTING | 16:9 STEAM | 9:16 MELTING | 9:16 STEAM | Verdict |
|---|---|---|---|---|---|
| ORIGINAL exact clause (post-encode next frame changed px == 0) | 16 | 10 | 0 | 57 | **FAIL** (3 of 4 non-zero) |
| REVISED (clause dropped; changed px outside label >= 1500 on the pop frame) | 3561 | 2240 | 4306 | 2966 | PASS |
Values from VERIFY.json `next_frame_px` / `changed_px_outside_label` (the first-run VERIFY output was overwritten; the numbers are the same measurement, retained in the revised file). The revision was made **after** seeing the failure — disclosed.

## Encode tolerance for any future recheck (defined now, before any recheck)
- Pre-encode (exact): next-frame changed px == 0 (P1). Unchanged.
- Post-encode: next-frame changed px (native, any channel diff >= 12) <= 100 **and** largest 8-connected changed component <= 20 px (scattered noise), per label. Same noise rule as the per-video hold classifier (`tooling/asset_library/xkcd/closure_v1.py`).
- Not applied to attempt 3 in this pass (would be post-hoc); applies to the next render.

## P8 / P9
PENDING_HUMAN. No human playback in this pass; the model cannot play video in real time. What a reviewer should judge: (1) 9:16 opening — does `Moon made of ice?` (f6) read as a hook in the first second; (2) both formats — are the MELT_DRIPS (f150) and STEAM_WISPS (f160) readable at real size next to the labels. Record in a new file `P8_P9_HUMAN_REVIEW.md` with reviewer name and date.
