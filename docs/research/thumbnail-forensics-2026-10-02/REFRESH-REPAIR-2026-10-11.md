# Dynamic packaging dashboard refresh

The workbook refresh previously asserted fixed totals (2,303 titles, 518 thumbnails, 518 packages and 121 QA reviews), used fixed row bounds, and did not advance the current-channel resume pointer. JSON reconciliation left completed/remaining video counts stale.

`dashboard_payload()` now derives counts from exact video/title IDs, the shared verified thumbnail/package union, explicit passing QA records and channel coverage. Duplicate QA/title IDs count once. Unapproved drafts remain excluded. A channel cannot retain COMPLETE when its verified package/thumbnail/QA coverage is incomplete. Queue remaining counts and current-channel selection use that same reconciliation. Existing package QA takes priority over new work. Historical audits and raw images are unchanged.

Refresh with the bundled Python and Node runtimes, using the existing Artifact Tool dependency link:

```sh
python docs/research/thumbnail-forensics-2026-10-02/reconcile_packaging_progress.py --payload /tmp/yios-packaging-workbook/payload.json
cp docs/research/thumbnail-forensics-2026-10-02/refresh_progress_workbook.mjs /tmp/yios-packaging-workbook/refresh.mjs
node /tmp/yios-packaging-workbook/refresh.mjs docs/research/thumbnail-forensics-2026-10-02/PACKAGING-PROGRESS.xlsx edit /tmp/yios-packaging-workbook/payload.json
python docs/research/thumbnail-forensics-2026-10-02/validate_progress_workbook.py
```

Artifact Tool authors cells, recalculates formulas, checks totals and renders the dashboard. Its export then passes through `preserve_workbook_features.py`, which transplants authored cell values/formulas/caches into the pre-edit native package so unsupported extensions, data bars, filters, panes and styles survive. This helper does not calculate or invent dashboard values. The baseline is captured before each edit, not obtained by resetting Git.

Current reconciliation: 2,303 titles, 518 verified thumbnails, 518 packages, 121 explicit QA, one complete channel. Hypothetically remains 5/39 complete with 34 remaining. No visual review was performed in this repair. All eleven sheet names, every original formula, native table/filter parts, freeze panes and data-bar definitions were compared against the pre-edit workbook and preserved. Native Excel recalculation was not run; Artifact Tool recalculation and exported caches were checked.

Regression coverage includes current union totals, a new valid QA review advancing counts/resume automatically, duplicate IDs, channel overlays, draft exclusion, rejection of stale COMPLETE, and workbook/JSON agreement. Passing QA is not inferred from QA_PENDING.
