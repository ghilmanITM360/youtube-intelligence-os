# Machine A Finance continuation runbook

Durable copy of the per-batch helpers that produced NICK_189 onward. A fresh session
(manual or scheduled) must start here, never from a NICK number remembered in chat.

## 0. Gates (stop without research writes if any fails)
1. `cd /Users/ghilmankhan/workprojects/yios-finance-machine-a`; branch is
   `codex/finance-machine-a-owner-directed`; `git fetch`; local = upstream = `git ls-remote` head.
   If the remote moved and the change is not yours, stop and report.
2. Read live five-hour and weekly usage. Unreadable → record `UNKNOWN`. ≥90% five-hour or ≥95%
   weekly → no new audit; exit. Never buy, spend or redeem credits.
3. `python3 build_continuation_queue.py lock acquire <session-id>` — `LOCKED ...` means another
   writer is running: exit. Release with `lock release` when the session ends.
4. Record `gh pr view 36 --json headRefOid,state` and `git ls-remote origin
   research/finance-economics-intelligence`. Never push there or modify PR #36.

## 1. Pick work
`python3 build_continuation_queue.py` → the `next` field of `FINANCE_CONTINUATION_QUEUE_SUMMARY.json`
is the head; take the next 2–5 `ELIGIBLE` rows. Do not touch `DEFERRED_PRESERVED_PARTIAL`
(includes `TFtBWn9CWOU`) or `BLOCKED_*` rows.

## 2. Per video (`export FINANCE_WORK=<local dir outside git>`; `FINANCE_SESSION=<session-id>`)
- `python3 machine_a_tools/src.py VID $FINANCE_WORK/nXXX/text.txt` — master, peers, transcript SHA, archive containment.
- Read the whole stored transcript; fetch `i.ytimg.com/vi/VID/maxresdefault.jpg` (fallback hqdefault),
  inspect native and `sips -z 180 320` mobile.
- Check material claims against primary sources; reproduce arithmetic.
- Write `nXXX/spec.py` (shape: `example_spec_NICK_194.py`; `FIRST_END` must be a short phrase without newlines).
- `python3 machine_a_tools/gen2.py nXXX/spec.py` → packet + READ_RECEIPTS.

## 3. Integrate (single writer)
Copy packets and `NICK_{vid}.jpg` into `audit-batches/`; `python3 build_audit_966.py`; rebuild the workbook
(`node build_workbook_1612.mjs` via the artifact-tool runtime); bump the completed count in
`test_combined_workbook.py`; `validate_audit_966.py`, `validate_research.py`, `pytest -q test_*.py` (38),
`node --test test_workbook_formatting.mjs` (2); `machine_a_tools/wbdiff.py old new` (only target rows);
`machine_a_tools/vr.py`, `machine_a_tools/post.py`; prepend RESUME_HERE; rebuild the queue; commit; push;
verify local = upstream = remote.

## Limits
No audio/visual review beyond thumbnails, no native Excel recalculation, no inferred impressions/CTR/
retention/revenue/demographics. Expansion rows are all `BLOCKED_MISSING_SOURCE_TRANSCRIPT` until a
transcript is registered; metadata alone never makes them complete.
