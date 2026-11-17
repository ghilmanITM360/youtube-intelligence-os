# YIOS Archive — Machine A

Historical audit outputs moved here on 2026-10-29. This directory is on the same Mac and is **not an independent backup**. The original evidence inside each folder is unchanged.

- `storage/`: prior folder census and targeted SSD cleanup decisions.
- `discovery/`: Machine A and Machine B evidence crosswalk.
- `research-export/`: original export identity and missing-path audit chronology. These are audit outputs, not the original 5,373-file export.
- `recovery/`: V8 readiness, reconciliation and V7 coverage receipts, including historical failures and exceptions.

`RELOCATION_MAP.csv` gives old and new paths, counts and full content-manifest SHA-256. `OPERATIONS.jsonl` is the append-only move/deletion log. All nine moves were on the same volume and passed before/after file SHA-256, count and inode checks. Historical files and their embedded old absolute paths were not rewritten.

Protected in place: `/Users/ghilmankhan/YIOS-local-audits` (active CT/Finance/V7 evidence) and `/Users/ghilmankhan/yios-git-recovery` (Git recovery state, including unrelated offline-map entries).

On 2026-10-29, 20 local generated Batch 35 `.tar.gz` wrappers were deleted after fresh local SHA-256, live Drive metadata and existing independent complete remote SHA/member verification. Drive objects, source members, manifests and incident receipts remain. Refer to `OPERATIONS.jsonl` and the original Batch 35 `RECEIPT.json`.

Blocked cleanup: Casually Finance `_work` (active-use and exact regeneration unresolved); Downloads What If duplicate tree (unique children, editing dependencies and independent recovery unresolved). Workprojects YIOS roots were not moved or deleted.
