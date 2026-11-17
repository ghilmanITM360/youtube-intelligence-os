# Correction to PUBLICATION_INTEGRITY_L.md (checkpoint M)
The L report stays as published. One sentence in its Coverage section is wrong:
"Its supplement hash is the first dry-run, which no longer exists; it was a receipt, not evidence."
Correct: the supplement row for campaign/PUBLICATION_K.json, the K seal entry and the K commit blob all hold the same hash. That dry-run was the one the K push sealed, and those bytes are in the K tree and restored locally.
So the row overlaps the K tree in path and content. Effect on counts: none. The union of 902 paths and the 315 supplement rows stay as stated; 1 of those 315 is also published.
This checkpoint also publishes the L preflight and final receipts. The M receipts stay local until a later checkpoint exists; the M commit itself is on the remote.
