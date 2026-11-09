# Word and Excel analysis

Open Casually_Finance_Analysis.docx for the full 29-page research report. Open Casually_Finance_Analysis.xlsx for the 206-upload table and working editorial templates. The report interprets observed associations; private CTR, retention and traffic-source data remain unavailable. Both use the frozen October 11, 2026 snapshot.

Excel includes Summary, Video performance, Title patterns, Topic analysis, Storyboards, Motion and assets, Production gates, Scorecards, Own analytics and Method. The main video table has filters and frozen identifiers. Date cells display UTC. Numbers and dates remain typed. Summary counts and chart follow calculated tiers. Peer medians, selection and bootstrap intervals are frozen outputs of build_analytics.py; Excel edits alone do not refresh them. Amber scorecard and analytics cells are editable. Editorial scores are QA gates, not learned performance predictors.

## Reproduce the Office conversion

Use Codex load_workspace_dependencies to obtain the bundled Python executable, Node executable and Node package directory. Copy OFFICE_TOOLS/*.mjs into a temporary working directory and link its node_modules to the returned package directory. This avoids modifying managed dependencies or installing repository packages. Pass absolute paths where needed.

Run in order with those bundled executables:

1. Node convert_chart.mjs <research-root>/PERFORMANCE_BY_AGE.svg
2. Python OFFICE_TOOLS/build_office.py <research-root> <research-root>/OFFICE
3. Node build_workbook.mjs <research-root>/OFFICE
4. Python OFFICE_TOOLS/add_excel_links.py <research-root>/OFFICE/Casually_Finance_Analysis.xlsx
5. Python OFFICE_TOOLS/validate_office.py <research-root>

The conversion uses temporary cf-office-data.json and cf-office-hyperlinks.json under /private/tmp. The workbook is authored with Artifact Tool. Native hyperlink relationships are added through a narrow standard-library OOXML patch because this engine does not implement HYPERLINK formulas. The spreadsheet reader is used only for saved-file verification. Remove the automatically generated XLSX inspect NDJSON after verification; it is an internal diagnostic, not an owner deliverable.

Render the DOCX with the Documents skill render_docx.py into a temporary QA directory and inspect every page. Optional PNG/PDF renders are internal QA, not required deliverables. Office ZIP timestamps and tool versions can change file hashes on regeneration; source values, classifications and evidence references must reconcile. Analytics reproduction remains deterministic independently of Office serialization.

## Validation

OFFICE_VALIDATION.json records independent reconciliation of every Video_ID, title, view count, publication time and tier; numeric/date types; scorecard blank/zero input checks; formula-error scan; 272 native Excel links; 66 Word links and output hashes. All 29 Word pages and all 10 spreadsheet views were visually reviewed. No live Microsoft Excel session was used. Focused evidence validation also confirms 45 frozen inputs unchanged and analytics regenerated identically.

The local full repository suite retains six inherited failures from an unmaterialized channel-registry LFS pointer. Exact failures are recorded in ../REPOSITORY_TEST_STATUS.json. Hosted CI status belongs to the current PR head and is reported separately in draft PR 28. No source files or production engine were changed for this conversion.
