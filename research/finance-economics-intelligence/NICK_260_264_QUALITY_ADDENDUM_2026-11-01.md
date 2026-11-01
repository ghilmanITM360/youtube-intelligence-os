# NICK_260–264 evidence-quality addendum (2026-11-01, Machine A)

Status: **FOCUSED_CORRECTION_RECORDED; ACCEPTED_PACKETS_UNCHANGED.** This follows the NICK_165 precedent. The original packets, receipts, ledger rows and workbook are not edited. This file records what a direct primary-source recheck found. A later narrow correction commit may apply it to the packet and its projections. Earlier packets (≤ NICK_264) are **not** retro-labelled with the new `source_confidence` scale, so they do not meet the standard introduced in NICK_265.

## Source-confidence profile of the accepted packets

| Packet | Claim groups | Claims with source_ids | Source receipts (access scope) |
|---|---|---|---|
| NICK_260 `mErWx9GiVUc` | 57 | 17 | 13 × `SEARCH_SUMMARY_OF_PRIMARY_OR_REPORTED_SOURCE` |
| NICK_261 `mKVSk76bOJI` | 12 | 0 | 1 × analyst recall |
| NICK_262 | 37 | 1 | 2 × search summary |
| NICK_263 `mWhpJZrTyNU` | 11 | 2 | 1 × search summary, 1 × recall |
| NICK_264 `maClOD9240k` | 16 | 2 | 1 × search summary, 1 × recall |

None of the 18 source receipts in NICK_260–264 was a directly inspected primary document. Arithmetic verdicts (K02) were independently reproduced and are unaffected.

## Correction 1 — NICK_260 C17 (high impact): verdict reversed

- Creator statement: "12.7% of all credit card balances are 90+ days delinquent" (stored text from char 10413). Video published 2026-04-07.
- Accepted verdict: "NYF4Q … annualised flow into serious delinquency of about 7.1% … The 12.7% figure was not found … Unsupported as stated." It rested on search summaries only.
- Primary evidence, directly inspected: New York Fed Household Debt and Credit Report 2025Q4 data workbook, `https://www.newyorkfed.org/medialibrary/interactives/householdcredit/data/xls/HHD_C_Report_2025Q4.xlsx` (SHA-256 `1969610624cf0c45a84a47018ccc9d464113dc4f6921ec85d0f07e833925bd55`; durable copy at `/Users/ghilmankhan/finance-work-machine-a/quality260/`). It was released before the upload.
  - Sheet "Page 12 Data" (Percent of Balance 90+ Days Delinquent by Loan Type), row `25:Q4`, CC = **12.7016**. Row `25:Q3` CC = 12.41.
  - Sheet "Page 14 Data" (New Seriously Delinquent Balances, the flow measure), row `25:Q4`, CC = 7.1293.
- Corrected verdict: **VERIFIED** (`PRIMARY_SOURCE_DIRECTLY_INSPECTED`). 12.7% is the stock share of card balances 90+ days delinquent. The 7.1% is a different measure (the annualised flow into serious delinquency). The accepted packet confused the two.
- Report PDF also preserved locally: `HHDC_2025Q4.pdf` SHA-256 `9f635fa98b092ab4c7a969ffe1ee7266d10f81892d8402ed2488e3bdc347d05b`.

## Correction 2 — NICK_260 C20 (partial): figures now dated

- Creator statement includes "serious-delinquency transition 14.3%" and "$1.696 trillion". The accepted packet called these "not checked".
- Same workbook, "Page 14 Data": student loan flow into serious delinquency `25:Q3` = 14.26 and `25:Q4` = 16.19. The report PDF says "Outstanding student loan debt stood at $1.66 trillion in 2025Q4" and "9.6% of balances 90+ days delinquent".
- Disposition: 14.3% **matches 2025Q3** but was **stale** at the April 2026 upload (Q4 = 16.2%, released February 2026). $1.696T does not match the NY Fed's $1.66T; it may come from the Department of Education federal-portfolio series, which was not checked. "Fastest since 2000", the 43 million borrowers, the $39,633 average and the 7 million in default remain unverified.

## Not rechecked (bounded scope)

NICK_260 C42 (existing-home sales vs 2009; NAR is licence-restricted), C18 (Edmunds), C26 (Challenger totals), and the NICK_261–264 recall-based verdicts. They keep their accepted labels; their verdicts rest on search summaries or recall, as disclosed in the table above.
