# 12 Codex + Claude production workflow for future original What If-style science videos (DRAFT v2, 2026-11-23)

Status: **design draft, never exercised.** No video is made under this directive. It is built from what the research shows is needed, not from an assumption that a tool is installed or tested. The two-agent split below was **not tested across two agents**; no frameworks were installed or run for this draft. In this Claude session the HyperFrames skills are listed as available, but no composition was rendered, so their fitness is UNVERIFIED. Repository rules apply (AGENTS.md): no new worktree, never auto-merge, scripts into `productions/<project>/**/*SCRIPT*.md`, AI-slop gate, private media outside Git.

## Roles
| | CODEX: visual research and asset studio | CLAUDE: animation and editing studio |
|---|---|---|
| Inputs | question, owner brief, research knowledge base (`knowledge_base_draft/`) | script, asset pack, physics sheet, scene spec |
| Produces | scientific reference sheet per script (claims, assumptions, recomputed values, sources); beat-by-beat script breakdown; original scene concepts; characters, props, poses, backgrounds as layered SVG/PNG with anchors; geometry contracts; physics-model prep (parameters, time step) where a simulation is warranted; asset QA records | timeline (24 fps), 2D motion, composition (2.5D or 3D only when the method table in `08_ORIGINAL_ASSET_RECIPES.md` says so), camera, procedural diagrams, narration sync, sound design, transitions, render, full-video QA |
| Hands over | asset pack + `scene_spec.json` + physics sheet + QA log | render, QA report, change requests back to Codex |

## Shared record (one set of IDs, normalised coordinates, seconds and 24 fps frames)
- `asset_id` OA-nnn (schema `08_ASSET_CONTRACT_SCHEMA.json`), `source_id`, `claim_id` (pattern of `07_SCIENCE_CLAIM_CHECKS.csv`), `scene_id` (pattern of `08_SCENE_BREAKDOWN_AND_METHOD_CHOICE.csv`).
- `scene_spec.json`: scene_id, narration clause and its time range, method, asset_ids with layer order and anchors (0-1), safe canvas, motion anchors, duration, physics claim ids, `to_scale` flag.
- QA log rows: who (model or person; **kind: self, human or independent**), what, verdict, date. A self-review is never recorded as independent.

## Gates (each blocks the next step)
1. Script: AI-slop gate verdict shown to the owner (a PASS is a proxy); every spoken physical number has a claim row with a recompute and a source; no copied xkcd wording, joke or art.
2. Asset pack: originality check against the reference list, layers and anchors present, style parameters recorded, physics marker (to scale / schematic / partly) set.
3. Animation: timeline against narration; machine alignment of ASR segments against events (as in `09_AV_ALIGNMENT_ALL88.csv`); **human listening pass** for sync and mix before any audio claim.
4. Export: full-video QA by a person; coverage and limits stated.

## What the research says to plan against (comparison values, not rules)
Speech about 3.6 w/s; narration from 0 s; first visual event within about 2 s; an event about every 2 s; scene swap about every 8 s; negative space high; thin 5 to 6 px line on a 1080 short side; one accent colour. Evidence: `knowledge_base_draft/RULE_EVIDENCE_LEDGER.csv`.

## Open design questions (owner)
Which tool owns SVG rigging; whether physics simulations are needed at all for the first episodes (the method table says most ideas do not need them); where drafts live (a branch is only needed for publication); registry IDs for SRC01/SRC02.

---
# History: v1 text (2026-11-23, earlier) kept below
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
3. (Done in the continuation: ledgers for all 88 videos with media, ASR for all 88; see `13_FINAL_REPORT.md`.)
4. Strategy edit: replace the 7.77 s-only pacing line with the three aligned quantities; revisit the length-cut rationale (owner decision).

## Addendum 2026-11-23 (third pass): checks the workflow should require
1. For every spoken physical number, compare three texts: the catalog caption, the ASR and the on-screen label, and the recomputed value; units and prefixes ("paws", "terowatt", petawatt versus terawatt) and homophones ("soil" for "oil") change verdicts.
2. Define the quantity before judging a number (total, delivered, recoverable; radius versus diameter; per flash versus per strike); a comparison of different quantities is "OPEN", not "discrepant".
3. State which published relation or constant set was used when more than one exists (energy-magnitude 1.5/4.8 versus 1.44/5.24).
4. Recompute every rule's numbers from the cited files before reuse; an audit found 7 of 23 rules needing qualification.
5. A second pass by the same model family is self-review and must be labelled so; only a human or a different-family reviewer is independent.
