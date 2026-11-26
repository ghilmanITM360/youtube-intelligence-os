# 12 Codex and Claude workflow for this knowledge base

Start at `00_START_HERE.md` (file index with absolute paths). Read first, in order: `README_CHECKPOINT.md`, `13_FINAL_REPORT.md`, `11_EVIDENCE_REGISTER_PHASE5_13.csv`, `01_STRATEGY_GAPS_AND_CONFLICTS.md`.

**Authorities.** Canonical data stays in the repo (`research/what-if-scripts`, `research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww`, CH-000004). This folder is derived and local, outside Git. Source video lives in `YIOS-Media-Library/xkcd Channel/` (set `YIOS_MEDIA_ROOT`); never commit media.

**Rules for any agent**
1. Do not pool Brain (14 older encodes) and campaign (library bytes) rows; use the campaign as primary. Check `06_BRAIN_VS_CAMPAIGN_SAME_VIDEOS.csv`.
2. Count per content family (45), not per transcript (83), when reporting corpus facts.
3. Use one definition per pacing quantity (shot, event gap, hard cuts/min). See `06_LAYER_RECONCILIATION.md`.
4. 83 is the transcript count, not the channel count (91 census, 92 with Aony69nO5kI).
5. Tiers: VERIFIED, MEASURED, OBSERVED, INFERRED, UNVERIFIED, UNAVAILABLE, NOT_DONE, SUPERSEDED, CONTRADICTED. Never upgrade an inference.
6. No performance claims: no retention, CTR or watch-time data exists for xkcd.
7. No Casually Finance timing rules for What If. No copying of xkcd text, art or scripts.
8. Any new script goes through `scripts/check_slop_risk.py` and the reference-framework check. No push or merge without explicit owner authorization.

**Recompute.** `python3 -I scripts/phase5_corpus.py`, `phase6_timing.py`, `phase6_brain_vs_campaign.py`, `phase9_audio_levels.py` (about 10 minutes, ffmpeg), `build_master.py`, `phase7_sample.py`, `phase7_holdout.py`, `phase7_tally.py`, `phase7b_asr.py` (whisper.cpp, about 6 minutes), `phase7b_sample.py`, `phase7b_tally.py`, `phase7c_asr.py`, `phase7c_sample.py`, `phase7c_tally.py`, `ledger_build.py` and `ledger_validate.py` run with `uv run --no-project --with numpy python` (frames regenerate; coding is manual). All read-only on the repo and media.

**Division of labour (suggested, not tested across two agents).** Claude: reading and judging transcripts, frames and audits. Codex: deterministic recomputation, CSV validation, diffs. A second reviewer of a different model family or a human is needed before any tier is raised: none exists yet.

**Next work, in order of value**
1. Human listening pass on a sample (unblocks Phase 9 and sync).
2. A second coder (human or other model family) on `07_SCIENCE_VISUAL_CODING_*.csv`; scheme v1.1 (TITLE, EQUATION, SCENE) is in use from 07b; Shorts were coded in 07c (one frame each).
3. Ledgers for the 24 media-available videos without visual analysis; transcripts for X97DDWvxaqQ and alBQCm0QpJg (whisper, local).
4. Strategy edit: replace the 7.77 s-only pacing line with the three aligned quantities; revisit the length-cut rationale (owner decision).
