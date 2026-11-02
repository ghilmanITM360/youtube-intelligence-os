# 01 — Existing visual-forensics work in YIOS (discovery)

Run: 2026-10-23, Machine B (`ghilmanislam360@Users-MacBook-Pro.local`). Repository `/Users/ghilmanislam360/Documents/youtube-intelligence-os`, branch `research/finance-economics-intelligence`, HEAD `7e70f061`, working tree clean before and after. Evidence below was read from Git objects (`git show`, `git ls-tree`) after `git fetch origin`. No checkout, merge or branch change was made.

## Summary table

| Workstream | Channel | Where | Tip / checkpoint | Videos | Status (verified from receipts) | Local on Machine B? |
|---|---|---|---|---|---|---|
| Editing forensics (Claude, Machine A) | Casually Finance | `origin/research/casually-finance-editing-forensics` | `090f84b3` (2026-10-20, "long-form procedure, not started; usage 96 % / 93 %") | 48 local on A (38 Shorts + 10 long-form) | **38 VISUAL_FORENSICS_COMPLETE_AUDIO_LISTENING_BLOCKED** (depth A 2, B 32, C 4); 10 long-form NOT started under this method | Git: yes (pushed). Frame dumps: **no** (Machine A `/Users/ghilmankhan/workprojects/yio-cf-editing-forensics-local-evidence`). Source MP4s: **yes** (all 48, hash-identical) |
| Original forensic research (Codex) | Casually Finance | `origin/codex/casually-finance-forensic-research` | `043b85bf` (2026-10-13) | 17 per-video folders | 10 long-form `QA.json status = PASS_STRUCTURAL` (one also `AUDIOVISUAL_QA_PARTIAL`); `turJ6VMfUjI` evidence folder only, no QA; others overlap the 38 Shorts | Git: yes |
| Deep dive (Codex) | Casual Economics | `origin/codex/casual-economics-forensic-research` | `fce81670` (2026-10-14) | 11 | Structural packages 11/11 PASS; shot census NOT_CERTIFIED; motion PARTIAL; independent visual QA NOT_PERFORMED; **AV sign-off 0/11** | Git: yes. Source MP4s: yes, 11/11 hash-identical to Codex `SOURCE_VERIFICATION.json` |
| What If production brain | xkcd's What If (CH-000004) | External corpus `~/GhilmanProjects/video data of what if/` + `main:data/manifests/what-if-forensic-source-v1.json` | brain release v1.0.0 | 14 sources (12 mapped to IDs, 2 UNRESOLVED) | Brain self-reports `COMPLETE_VALIDATED`; YIOS main registers 3 canonical videos with visual-temporal evidence (`editing-visual-intelligence-pilot-2026-09-11.json`) | Corpus: yes (Machine B). **Source copies differ by hash** from the new `xkcd Channel` folder (different downloads), so reuse needs ID-level mapping, not hash identity |
| Packaging/thumbnail forensics | multiple | `research/thumbnail-forensics-complete-2026-10-04`, `integration/packaging-forensics-validated-subset-2026-10-11` | — | — | Thumbnail/title packaging only. **Not video visual analysis.** | — |
| Metadata only | Barely Evolved; Monkey Explains (1999) | `research/barely-evolved-metadata`, `research/monkey-explains-1999-metadata` | `c4212c90`, `f176aa28` | — | Metadata snapshots; **no frame/scene work** | — |
| None found | Primate Economics, Primitive Education, MonkeBiznis ("monke") | — | — | — | **No prior visual analysis** in any branch, main, or Downloads manifest | — |

## Casually Finance editing forensics — exact stopping point

From `STATUS.json` and `RESUME_HERE.md` at `090f84b3`:

- Phase 1 gate PASSED. Population on Machine A: 54 local files, 48 unique videos (38 Shorts, 10 long-form), 2.818 h, 264,982 native frames; 210 public videos.
- `videos_complete`: 38 IDs, all `VISUAL_FORENSICS_COMPLETE_AUDIO_LISTENING_BLOCKED`, each with `videos/<id>/QA.json`.
- `queue_prior_partial_16` (actually 10 IDs): `o3FQcd91MIs, kwMHrTFCWUE, dlBhLhn8lL0, 5umJ63d3rzQ, xtqbRt94TTw, -X6YzlY_8tM, Uumnx2Fo6cE, DgbHW0IqHrI, 0ll9rEtoRrs, roe3SgezmmU`.
- `longform_procedure`: status `WRITTEN_NOT_STARTED`, LF-0 to LF-6, pilot `o3FQcd91MIs`. Stopped because five-hour usage was 96 % at 2026-10-20 22:13.
- `blocked`: `turJ6VMfUjI` = "source missing locally" on A. **On Machine B this source is present** (`Why You (Mathematically) Need Inflation`, 63.4 s Short, bracket-ID filename). It is a real unblock, but it is not hash-verified against any Machine A record because A never had it.
- The claim recorded on the branch: "NOT 100% COMPLETE … the 10 long-form videos are not analysed."
- The worktree path in RESUME_HERE (`/Users/ghilmankhan/...`) belongs to Machine A's user. It does not exist on Machine B. No worktree for this branch exists here (`git worktree list` shows only the main checkout).

## Is the evidence genuinely complete or only sampled?

- **CF 38 Shorts:** per-event, frame-accurate authoring (scene timeline, motion events with easing fits, colour-area, captions) with QA. This is the most rigorous visual coverage in YIOS. It is still single-reviewer, and listening was blocked: audio is measured signal + Whisper ASR only.
- **CF 10 long-form (Codex):** `PASS_STRUCTURAL` with a sampled visual reconstruction. Not equivalent to the Shorts contract.
- **Casual Economics 11:** structural, sampled (4 s point samples plus temporal sequences, or candidate-state segmentation). Its own register says fixed sampling missed short states.
- **What If:** brain tables (states, shots, motions, words) exist for 14 sources. Whether every source meets a full-timeline contract was not re-audited this run → `HISTORICAL_UNVERIFIED` in the ledger.
- **Audio listening:** no workstream ever performed human listening. Every package says ASR / measured signal only.

## Published or local?

All Git workstreams above are pushed to `origin` (GitHub). Raw frame dumps and MP4s are deliberately outside Git. For CF editing forensics, those dumps exist only on Machine A, but every script regenerates them from the source MP4.
