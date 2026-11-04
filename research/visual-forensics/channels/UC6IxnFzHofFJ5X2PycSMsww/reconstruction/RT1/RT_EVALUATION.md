# Reconstruction test RT1 — result (spec-only fresh worker; evaluated with the source pipeline)

Inputs given to worker: spec_s6.md + spec_s9.md (manual v0.2 §6, §9) + BRIEF_RT1.md beat list (original topic, original identity: pebble narrator, teal #1F8A8A). Transcript audit: worker Read only those 3 files; no source images/videos. Output RT1_animatic.mp4 (sha256 in evidence/source_sha256.txt), 576 f, 24 fps CFR, 1920x1080, silent.
Measured with the identical xk_measure → xk_scenedetect → xk_segment pipeline (tables/, RT_EVALUATION.json). Primary viewed render SHEET_01 (0.6 scale).

| Check | Result |
|---|---|
| Intended events detected at intended frame ±2 | 19/21 matched; 0 unexplained measured onsets |
| 1-frame activity share (manual: majority) | PASS 0.74 |
| Activity frame share | PASS 0.095 |
| events/min (dev 18.4–39.2) | **FAIL 47.5** |
| median hold (dev 1.13–2.84 s) | **FAIL 0.96 s** |
| Visual grammar (primary SHEET_01) | lecture frame + typed question card (≈10 f) + 1-frame object pop + 8-f teal stroke write-on + label pop after object: reproduced |
| Object detail (§2: objects drawn with much more detail than figures) | **FAIL** — geometric low-detail mug; §9 does not state this rule |
| Audio/narration sync | NOT TESTABLE (silent render; no listening capability) |

Verdict: RECONSTRUCTION_TEST_PARTIAL. Root causes are in the SPEC, not the worker: (1) the RT1 beat list packed 21 events into 24 s, impossible with 1.5–2.5 s holds — §9 lacks an explicit event budget (target ≈0.33–0.5 events/s, i.e. ~8–12 events per 24 s); (2) §9 omits the object-detail contrast rule from §2. Fix in manual v0.3 §9, then run RT2 with a new fresh worker.
