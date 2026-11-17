# Text file needed from Machine B

Status: BLOCKED. `/Users/ghilmanislam360` is not on this Mac and no remote access is available from here. Text only: no credentials, no media.

## Copy on Machine B
`/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-05-independent-remote-restore/recovery/UNAVAILABLE_UNIQUE_HASHES.csv`

First run `shasum -a 256 <file>` and send the digest with it. Open the file and confirm it holds hashes and paths only.

## Put it on Machine A
`/Users/ghilmankhan/YIOS-local-audits/2026-11-06-o3FQ-Uumnx-forensic-manifest/input/UNAVAILABLE_UNIQUE_HASHES.csv`

The owner picks the channel, such as AirDrop or USB. Nothing in this folder needs a cloud destination.

## Then run on Machine A
```
cd /Users/ghilmankhan/YIOS-local-audits/2026-11-06-o3FQ-Uumnx-forensic-manifest
shasum -a 256 input/UNAVAILABLE_UNIQUE_HASHES.csv   # must equal the digest from Machine B
python3 -I join_missing_list.py input/UNAVAILABLE_UNIQUE_HASHES.csv
```
Only `recovered_from_inventory` and `recovered_all_local` are recovery counts. Until this runs, 1,006 is a count of hashes on this Mac, not hashes recovered from the 5,767 list.

## The other direction also works
Copy `inventory_1006_hashes.csv`, `unique_hashes.csv`, `join_missing_list.py` and `SHA256SUMS` to Machine B and run the same join there.

Also useful if present: `recovery/RECOVERY_REMOTE_RECONCILIATION.csv`, and `recovery/DEDUPLICATED_RECOVERY_MANIFEST.csv` from the recovery-closure package.
