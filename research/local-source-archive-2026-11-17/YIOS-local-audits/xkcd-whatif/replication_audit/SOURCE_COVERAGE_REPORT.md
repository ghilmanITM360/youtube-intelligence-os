# SOURCE_COVERAGE_REPORT
All numbers re-derived 2026-11-14 from census.csv + videos/<id>/quality_gate.json + CLOSURE_LEDGER_v1.csv (see REFERENCE_VIDEO_DATABASE.csv).

## Video-level (91 public videos)
| Level | Long | Shorts | Total |
|---|---|---|---|
| Public (live check 2026-11-14) | 45 | 46 | 91 |
| Local file | 44 | 44 | 88 |
| Ingested (frames, ASR, tables) | 44 | 26 | 70 |
| Quality gate, VISUAL_ANALYSIS_PARTIAL | 24 | 20 | 44 |
| Visual closure, VISUAL_ANALYSIS_COMPLETE (visual only) | 9 | 20 | 29 |
| CT_SCAN_COMPLETE / full AV sign-off | 0 | 0 | 0 |
Reason for 0: audio listening is BLOCKED_CAPABILITY. ASR and loudness are machine signals, not listening. 11,685 of 173,344 gated frames (6.7%) sit in listed unviewed/unverified intervals.
Independent evidence is smaller: 9 closed/library Shorts are narration excerpts of long videos, re-laid for 9:16. Answer to "how many videos fully analysed": **0** with full CT-scan status; **29** with visual-only closure (20 Shorts + 9 long), roughly 24 long + 11 Shorts independent-equivalent in the broader library.

## Coverage of the production system: transparent measure (my rubric, heuristic)
Score per dimension: 1 = measured AND viewed AND held-out checked; 0.5 = measured or inferred, partial/sampled; 0 = unavailable.
| # | Dimension | Score | Basis |
|---|---|---|---|
| 1 | Canvas, line weight, palette | 1 | measured on 5,458 states, held-out passes |
| 2 | Layout / composition grammar | 1 | 240 clusters viewed, v7/v8 held-out |
| 3 | Character system (narrator, modifier kit) | 0.5 | 3 model sheets viewed; no motion rig facts, no expression library study at motion level |
| 4 | State / entry rhythm | 1 | all 5,458 states; held-out 1-5 |
| 5 | Transitions | 0.5 | dissolve linear 6 f, cut; only 13 motion windows |
| 6 | Camera | 0.5 | locked by default, moves 9-12 f blurred; easing UNAVAILABLE |
| 7 | Typography | 0.5 | font class inferred, font not identified |
| 8 | Script / narration structure | 0.5 | transcripts exist but ASR_UNCERTIFIED; book text exists; no verified structural study here |
| 9 | Sound effects / foley | 0 | UNAVAILABLE |
| 10 | Music / mix / loudness | 0 | loudness measured only, never listened to |
| 11 | Export spec (res, fps, aspect) | 1 | 1920x1080 / 1080x1920 at 24 fps |
| 12 | Authoring software / pipeline of the source | 0 | UNKNOWN, cannot be inferred from pixels |
Sum 6.5 / 12 = **54%**. Rubric is mine, not an objective percentage. The unstudied half is exactly sound, narration timing and true motion curves.
