# o3FQcd91MIs and Uumnx2Fo6cE evidence on Machine A

Manifest only. No media was copied or uploaded.

- `rows.csv`: each path with fresh SHA-256 and size. `in_machine_b_portable_inventory` separates the rows from Machine B's inventory from other files in the same two folders.
- `unique_hashes.csv`: one row per hash.
- `inventory_1006_hashes.csv`: only the hashes referenced by Machine B's inventory.
- `summary.json`: counts.
- `TRANSFER_REQUEST.md`: the exact file request and destination.

1,009 is a row count, with 1,006 unique hashes. Neither number is a recovery count. These hashes have not been compared with the missing list.

## Pending input, BLOCKED until it reaches this Mac
`/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-05-independent-remote-restore/recovery/UNAVAILABLE_UNIQUE_HASHES.csv`

Also useful: `recovery/RECOVERY_REMOTE_RECONCILIATION.csv` and the recovery-closure package's `recovery/DEDUPLICATED_RECOVERY_MANIFEST.csv`.

Then run `python3 -I join_missing_list.py <path>`. That prints the exact recovered and still-missing counts.
