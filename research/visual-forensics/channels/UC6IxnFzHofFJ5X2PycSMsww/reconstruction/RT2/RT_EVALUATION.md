# Reconstruction test RT2 — result (fresh spec-only worker, manual v0.3 §6+§9)
Transcript audit: worker Read only BRIEF_RT2.md, spec_s6.md, spec_s9.md (no source media). Worker wrote its own beat list (original topic "What if every elevator in a city stopped at once?"). Output RT2_animatic.mp4: 576 f, 24 fps CFR, 1920x1080, silent. Measured with the source pipeline (RT_EVALUATION.json); primary viewed render SHEET_02 (0.6 scale).

| Check | RT1 (v0.2 spec) | RT2 (v0.3 spec) |
|---|---|---|
| events/min (dev 18.4–39.2) | FAIL 47.5 | PASS 25.0 |
| median hold (dev 1.13–2.84 s) | FAIL 0.96 | PASS 2.21 |
| 1-frame activity share | PASS 0.74 | PASS 0.70 |
| activity frame share | PASS 0.095 | PASS 0.056 |
| intended events detected ±2 f | 19/21 | 10/10, 0 unexplained |
| object-detail contrast | FAIL | PASS (window-grid buildings, shaft, car vs minimal pebble narrator) |
| persistent anchor / hard cuts / slide-blur / aside / dark escalation swap | partial | PASS (teal banner 'ELEVATORS STOPPED: ALL' T+00:30→T+24:00; slide with blur f252–f260; 'WELL. THAT'S A LOT OF STAIRS.'; lights-off 1-frame swap on dark canvas) |
| audio / narration sync | NOT TESTABLE | NOT TESTABLE (silent; no listening capability) |

Verdict: RECONSTRUCTION_TEST_PASS_VISUAL_RHYTHM (silent, single 24 s sample, one worker model family). The v0.3 §9 spec reproduces the measured rhythm and device grammar with an original identity. Not tested: narration-driven timing, long-form structure (title/end card), Shorts 9:16 re-layout, art quality judged by humans.
