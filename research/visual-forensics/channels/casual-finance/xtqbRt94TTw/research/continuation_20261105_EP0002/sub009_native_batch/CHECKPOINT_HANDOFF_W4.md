# Video006 xtqbRt94TTw checkpoint W4 (SUB009 native review)
Parent remote: 9a1ab68762563dba8b509e96fb53fef025129f26 (W3). Source SHA256 030a85ad...a7a66 re-hashed this run PASS; W3 seal PASS.
Extraction: reused ep0015 native frames 336-345; new native 346-405 (60 PNG, local only, not published). Alignment: re-extracted 345 is pixel-identical to ep0015 f00345.
Measured (yellow threshold as ep0015, changed px + bbox) + visual (strip_338-398_roi.jpg 10 native ROI crops, overview_f377_half.jpg).
- SUB009 (candidate 339-396): continuation phase of EP0015 (pose 337 + highlight onset 338). Highlight sweeps first body line left-to-right ~18 px/frame, right edge 157 (338) -> 853 (377, 'vote:'); single line y600-619. Cursor (I-beam then arrow) moves 378-396; static from 397. Pointer/figure ROI unchanged 338-405.
Ledger v28 -> v29: exactly 1 row changed (SUB009); 948 IDs and order unchanged. Queue 628 -> 627 (CURRENT_NATIVE_QUEUE_v5.json).
Validation: positive asserts (onset 338, monotonic growth 339-377, end 853, single line, cursor 378-396, static 397-405) + negative asserts (pointer ROI zero change, no new highlight after 377, only 4px residue right of x900 at 338) pass; 4 mutated-threshold negative runs all rejected; 1-row diff check pass.
Unknowns: 4 scattered px at 338 in header banner (likely encoder residue after 13053-px pose swap); +46 yellow px at 383 (cursor overlap likely); cursor path sampled visually 8/19 frames. Audio NOT_LISTENED. CT_SCAN_COMPLETE=false. 0/35 certified.
Env note: python3 -I hides user-site numpy; integrators run with plain python3 (own scripts, local frames).
NEXT: SUB010 (450-459 cursor drift; first item of queue v5), then EP0018 (461), SUB011; extract only each bounded native window (e.g. 445-465 covers SUB010+EP0018).
Writer: Claude scheduled run b69509dd (vf_lock v3 token), released at end.
