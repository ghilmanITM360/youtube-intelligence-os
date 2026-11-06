# Video006 xtqbRt94TTw checkpoint W3 (SUB007 + SUB008 native review)
Parent remote: a69a8a755d494df1225ca1d319e74e34f8b23ef5 (W2). Source SHA256 030a85ad...a7a66 re-hashed this run PASS; W2 seal PASS.
Work: no new extraction; reused native frames 303-338 (ep0014/ep0015 batches). Measured (date-ROI blue selection left edge, changed px vs prev) + visual (strip_307-336_roi.jpg, 12 native ROI crops).
- SUB007 (308-313): continuation phase of the SUB006 drag, not an independent onset. Selection left edge 170 -> 142 over 308-312; I-beam becomes arrow at 312; 313 is a 1px settle that looks the same as 312.
- SUB008 (327-335): arrow cursor move, exact onset 327 after a static hold (314-326, changed px <= 2), last change 335; static at 336; selection kept; no new content. EP0015 pose follows at 337.
Ledger v27 -> v28: exactly 2 rows changed (SUB007, SUB008); 948 IDs and order unchanged. Queue 630 -> 628 (CURRENT_NATIVE_QUEUE_v4.json).
Validation: positive asserts (growth 308-312, hold 314-326, motion 327-335, static 336, pose 337) + negative asserts (no selection growth after 313, no motion >= 100 px before 327 in 314-326) all pass; 2-row diff check pass.
Unknowns: +12 blue px at 329 (likely anti-aliasing near cursor); cursor path sampled visually on 6 of 9 frames. Audio NOT_LISTENED. CT_SCAN_COMPLETE=false. 0/35 certified.
NEXT: SUB009 (first item of queue v4), then SUB010, EP0018; extract only each bounded native window.
Writer: Claude scheduled run 5c8c86e3 (vf_lock v3 token), released at end.
