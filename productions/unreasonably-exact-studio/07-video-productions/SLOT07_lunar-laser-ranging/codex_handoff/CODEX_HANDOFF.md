# Codex handoff: process, ownership and batches (Slot 07)

Status: see `MASTER_PRODUCTION_DASHBOARD.md` (the only status source). Claude-verified Codex progress is logged in root `CODEX_PROGRESS.csv`; Codex's own self-report is `codex_handoff/CODEX_PROGRESS.csv` (Claude never edits that one).

Entry point for Codex: `codex_handoff/START_HERE.md`. Everything Codex needs is inside `codex_handoff/` (it never needs the rest of the project).

## 1. Split of work
| Owner | Does |
|---|---|
| Owner | approves, listens (G1), signs off art and the final film |
| Claude | research, art direction, briefs, acceptance tests, code-drawn graphics, rigs, proofs, editing, audio, captions, QA |
| Codex | **independent reference research**, illustrated assets and textures, layer splits with hidden overlap, pivots, its own QA report |
Never both at once on the same file: Codex writes only inside `codex_handoff/deliveries/<batch>/`; Claude never edits a delivery in place (repairs are new files, logged "repaired by Claude" with before/after hashes).

## 2. Batches (dependency order; each ends with a Claude review before the next starts)
The chain per batch: reference verification -> candidate master -> layer decomposition -> registration -> animation proof -> approval.
| Batch | Assets | Why first | Gate to the next batch |
|---|---|---|---|
| 0 | **Calibration:** one small asset, `RETRO_002_CUBE_ARRAY` master only | tests the whole loop (references, native size, alpha, hash, QA honesty) cheaply | Claude's A+B tests pass and Codex's QA lists real failures honestly |
| 1 | Celestial: EARTH_001/002/004/006, MOON_001 (textures) | lowest risk, feeds P01/P02 | P01 and P02 rendered and reviewed |
| 2 | Retroreflector: RETRO_001/002/004/005 | the film's key reveal, needs match-cut registration | B9 registration + P06/P07 |
| 3 | Lunar surface: MOON_002/003/005/006 | environment for B15-B18 | surface layers pass the light test |
| 4 | Observatory/telescope: OBS_001-007, TEL_001-005 | most layers, depends on dome rig decisions | P03/P04 |
| 5 | Astronaut: ASTRO_001-011 | highest identity risk; small screen time; last on purpose | identity test + P05/P06 |
Between batches Codex does **not** continue generating while Claude reviews.

## 3. Evidence Codex must save (not just pictures)
- `deliveries/<batch>/ARTWORK_QA.md`: per asset, what was checked, **what failed**, departures from reference.
- `deliveries/<batch>/RESEARCH_NOTES.md`: Codex's own sources (URLs, saved images in `references_codex/`), disagreements with Claude's research, missing perspectives it found.
- `IMAGE_GENERATION_PROMPTS.md`, `ASSET_MANIFEST.csv`, `PIVOTS.json`, `SHA256SUMS.txt`.
- `codex_handoff/CODEX_PROGRESS.csv`: Codex's own task manifest, appended after every asset: `asset_id,batch,state,files,date,notes`. Claude does **not** edit this file.

## 4. If a generated layer fails
Diagnose the actual problem; correct the affected component only; preserve approved layers; generate a focused replacement; repeat the specific failed test; record the result. Do not regenerate whole characters or environments for a small defect.

## 5. Hand-over checklist (done at the time, each item evidenced)
1. Confirm the Codex app is open on the intended workspace (screenshot).
2. Give it `codex_handoff/START_HERE.md`'s absolute path and ask it to read it first.
3. Confirm Codex reports back that it read `PRODUCTION_ART_DIRECTION.md`, `ASSET_ACCEPTANCE_TESTS.md` and the Batch 0 brief.
4. Start Batch 0 only. Review.
5. Record each step in `PROGRESS_LOG.md` with the date and what the screen showed.

## 6. What is not allowed
No text/numbers/arrows/rays/dials in art; no real site names, signage, patches or people; no overwriting earlier deliveries; no `APPROVED` labels; no integration of a delivery that Codex itself marked failing.
