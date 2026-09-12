# DS-000022 Package Validation Report

- Packages: 7
- Workbook video rows: 732
- Unique video IDs: 732
- Transcript files: 732
- Placeholder transcript files: 10
- ZIP members: 739
- Formula cells with usable cached values: 2998
- Missing descriptions: 0
- Apify recovery: Not performed by validator; preserved missing-value evidence is listed below.
- Original Actor raw JSON and Actor run IDs: Not supplied.

| Channel | Videos | Transcript files | ZIP members | Missing descriptions | Status |
|---|---:|---:|---:|---:|---|
| Tp Dossier | 92 | 92 | 93 | 0 | VALID |
| Carl Invests | 80 | 80 | 81 | 0 | VALID |
| Well. | 32 | 32 | 33 | 0 | VALID |
| Lucas Grant | 95 | 95 | 96 | 0 | VALID |
| Nick Invests | 363 | 363 | 364 | 0 | VALID |
| Bob Invests | 57 | 57 | 58 | 0 | VALID |
| Just Some Guy Stories | 13 | 13 | 14 | 0 | VALID |

## Missing field evidence

| Channel | Video ID | Field | Stored value |
|---|---|---|---|
| Lucas Grant | `IyN2D4n6XiM` | Views | N/A |
| Lucas Grant | `q8ZdQ4OsD7U` | Views | N/A |
| Lucas Grant | `H6F-ZVkKv0Q` | Views | N/A |
| Lucas Grant | `18yXTv-V498` | Views | N/A |
| Lucas Grant | `p26tUA4TawM` | Views | N/A |
| Lucas Grant | `Hgn-6mge3p8` | Views | N/A |
| Lucas Grant | `eL2wbhmkhZA` | Views | N/A |
| Lucas Grant | `KyXa--2pZy8` | Views | N/A |
| Lucas Grant | `AdM_xvqsZ5M` | Views | N/A |
| Lucas Grant | `yQA24eKfcIY` | Views | N/A |

## Placeholder transcript evidence

- Lucas Grant: `18yXTv-V498`
- Lucas Grant: `AdM_xvqsZ5M`
- Lucas Grant: `H6F-ZVkKv0Q`
- Lucas Grant: `Hgn-6mge3p8`
- Lucas Grant: `IyN2D4n6XiM`
- Lucas Grant: `KyXa--2pZy8`
- Lucas Grant: `eL2wbhmkhZA`
- Lucas Grant: `p26tUA4TawM`
- Lucas Grant: `q8ZdQ4OsD7U`
- Lucas Grant: `yQA24eKfcIY`

## Validation scope

Checked exact sheet order and columns, typed IDs/dates/numbers, freeze panes, filters, formula caches/errors, description reconciliation, valid video URLs, ZIP integrity/root structure, UTF-8, required transcript sections and headers, exact transcript word counts or explicit placeholders, filename/ID/title/channel mapping, and complete INDEX listings.

## Visual workbook review

- Rendered and reviewed all five sheets in all seven workbooks: 35/35 sheet checks.
- Sheet order, header styling, widths, wrapping, freeze panes, filters, number formats, and hyperlink presentation were consistent with the supplied package format.
- No unexpected `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, or `#N/A` formula errors were found.
- The ten genuine Lucas Grant data gaps are visibly highlighted and agree with the Verification sheet.

## Recovery decision

No Apify recovery run was performed. The Lucas Grant Verification sheet records that the same ten videos returned no view count and no transcript on two separate scrapes, which is preserved evidence of a stable source limitation rather than a confirmed recoverable scrape failure. The packages therefore contain 722 complete plaintext transcripts and ten explicit zero-word placeholder files. All 732 videos have complete individual descriptions.
