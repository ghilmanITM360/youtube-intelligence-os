# Reconstruction test RT3 — long-form structure (2026-11-04T16:38Z), manual v0.4 §6+§9, fresh spec-only worker
Audit: worker read BRIEF_RT3.md (Read) and spec_s6.md/spec_s9.md (cat); nothing else. Output RT3_animatic.mp4 1440 f, 60 s, 24 fps, 1920x1080, silent. Measured with source pipeline (RT_EVALUATION.json). Primary viewed render SHEET_02 (0.6 scale).

| Check | Result |
|---|---|
| events/min / median hold / 1-frame share / activity share | PASS 21.0 / 1.96 s / 0.76 / 0.138 |
| intended events detected ±2 f | 21/24, 0 unexplained |
| series card: hard cut, start 6–31 s, ≈2 s | PASS: cut f360 (15.0 s), HOLD f361–f407 (48 f) |
| end card: final HOLD ≈10 s | PASS: 239 f measured (worker intended 240; first end-card frame is the cut ACTIVITY) |
| persistent anchor, write-on, slide-with-blur, aside, original identity | PASS on SHEET_02 ('SUN CLOCK' banner, 'AT NOON' typed, blur slide, teal 'PEBBLE PONDERS' card) |
| object-detail contrast | WEAK on SHEET_02 (sparse canvases, minimal objects) — §9 rule present but under-applied |
| narration sync | NOT TESTABLE (silent) |
Verdict: RECONSTRUCTION_TEST_PASS_STRUCTURE (long-form skeleton reproduced frame-exactly from spec); art density remains the weakest transfer.
