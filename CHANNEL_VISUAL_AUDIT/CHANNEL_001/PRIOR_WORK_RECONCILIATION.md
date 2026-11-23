# Prior-work reconciliation, CH001 CasuallyFinance (2026-11-20)
Workspaces are NOT moved. Statuses follow rulebook sec. 3.
| Path | Claim | Check made | Status | Defect / next |
|---|---|---|---|---|
| research/visual-audit/CHANNEL_001_CasuallyFinance/01_DATA_INVENTORY.csv | 216 MP4s, hashes | all 216 exist; 216/216 ffprobe-decodable | VERIFIED | |
| .../04_SHOT_ANALYSIS.csv | 2,195 shots, 18 videos | merged from ledgers; 10nEByVLya0 ledger checked vs MP4 frames (22 shots, timing consistent with sheet) | PARTIAL | text fields shallow; narrative placed in wrong columns |
| ~/YIOS-local-audits/2026-11-08-10nEByVLya0-deep-ct-scan/ (states, shots, captions, ASR, frames) | 61 states, caption events, audio | used as render input; mid-shot frames viewed against ledger text for 22 shots | VERIFIED for timing; CONTRADICTED on one description (S022 hair colour, see error log E11) | |
| 11_MOTION_WINDOWS*.csv/md | 341 windows, 15 videos | tool re-run during session | VERIFIED (coarse, grey diff) | no per-element transforms |
| 13_COMMUNICATION_ROLE_LABELS_* | 722 draft role labels | self-checked 85% on samples | PARTIAL, INFERRED | draft only |
| 14_VISUAL_DECISION_ENGINE.md | 53.0% vs 47.8% baseline | held-out run | VERIFIED, weak | |
| 21_AUTO_MOTION_PROFILE_* | pace index, 162 IDs | calibrated vs ledger (corr 0.78, n=15) | PARTIAL | not shot-level |
| REPRODUCTION_TESTS/ (original "Test C") | original-scene render | not a same-video test | PARTIAL | counts only toward generalization |
Missing vs rulebook: 05, 06 (as separate files), 07-10, 12-13 grammar files, 16 evidence register, SCENE_BLUEPRINTS for the other 18 ledger videos, second novel-scene test.
