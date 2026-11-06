# Video006 xtqbRt94TTw checkpoint W2 (EP0015 pose/highlight compound)
Parent remote: 649401e66118cdacf25353cf3a40fe0d168b09c2 (W1). Source SHA256 030a85ad...a7a66 re-hashed this run PASS; W1 seal PASS.
Work: native frames 313-345 extracted (33 PNG, local only, ep0015_native_batch/frames). Measured (yellow px, changed px vs prev) + visual (strip_336_338.jpg).
- EP0015: pose swap exact onset 337 (changed px 13053; 336 has 1); yellow highlight on 'The' onset 338 (256 px, grows to 2149 at 345). Compound split: two onsets one frame apart.
- SUB008 (327-335): small cursor-scale diffs 108-156 px/frame, pose static; measured only, not individually viewed.
Ledger v26 -> v27: exactly 1 row changed (EP0015); 948 IDs/order unchanged. Queue 631 -> 630 (CURRENT_NATIVE_QUEUE_v3.json).
Validation: positive (948 rows, 1-row diff, onset asserts 337/338) + negative (yellow absent for all frames <=337) as expected.
Unknowns: highlight extent after 345; SUB007/SUB008 not visually inspected. Audio NOT_LISTENED. CT_SCAN_COMPLETE=false. 0/35 certified.
NEXT: SUB007 (308-313) + SUB008 (327-335) visual strips from existing native frames; no new extraction.
Writer: Claude scheduled run 88d103b4 (vf_lock v3 token), released at end.
