# V006 xtqbRt94TTw checkpoint Y2 (scheduled run 2026-11-15)
G007.02 ruling (Y1, G007_02_RULING.json) integrated into visual_event_ledger_v45.csv via integrate_y2.py: only row G007.02 changed (verdict NATIVE_ONSET_OF_S0015_SINGLE_REVIEW, observed 1141..1141, bounds_role ONSET_EVENT_OF_S0015, conflict note: draft S0015 [1142,1155] starts one frame late). Frames/pts/timing_precision unchanged. 948 rows, all other rows byte-equal to v44.
Queue v21 = v20 items unchanged (561 strict rows; G007.02 was never in the strict queue), new baseline v45.
Checks: positive (948 rows, single-row diff, frames unchanged, queue 561) PASS; negative (tampered extra row / frame drift detected) PASS.
NOT done: production spec draft S0015 interval is still [1142,1155] in the production draft; binding [1141,1155] to be applied in a production-draft revision. No new media; single reviewer; audio 0; CT_SCAN_COMPLETE=false; 0 of 35.
Source sha256 030a85ad...a7a66 re-verified; Y1 sums OK; remote head at start 784db366 (= Y1).
Next exact operation: verify queue item EP0078 (2437-2469, article scroll + Author card) with adjacent native context; optionally apply S0015 [1141,1155] in a production-draft revision.
