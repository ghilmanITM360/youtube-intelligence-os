# Prompt for ONE Claude Desktop local scheduled task (owner registers it in the app)

Suggested: name `finance-machine-a-continuation`, cwd `/Users/ghilmankhan/workprojects/yios-finance-machine-a`,
cadence every 5–6 hours (a local scheduled task only fires while the Mac is awake and Claude Desktop is open;
there is no supported "usage-reset" trigger, so each run checks limits itself).

---
Continue YIOS Finance Intelligence on Machine A. Follow
`research/finance-economics-intelligence/machine_a_tools/RUNBOOK.md` exactly, starting with section 0 gates.
If any gate fails (remote moved unexpectedly, usage ≥90% five-hour or ≥95% weekly, lock held, wrong branch),
make no research writes, report why in Roman Urdu, and exit. Otherwise take the queue head from
`build_continuation_queue.py`, audit eligible videos in 2–5 video batches with full six-dimension evidence,
validate, commit and push only to `codex/finance-machine-a-owner-directed`, verify the remote head, and stop at
85% five-hour usage after publishing. Never touch PR #36, `research/finance-economics-intelligence`, the
Casually Finance forensic branch, credits, or `TFtBWn9CWOU`. Release the lock before exiting. End with a compact
Roman Urdu checkpoint (accepted, totals, original/expansion, SHA, remote verification, validators, quotas, next video).
