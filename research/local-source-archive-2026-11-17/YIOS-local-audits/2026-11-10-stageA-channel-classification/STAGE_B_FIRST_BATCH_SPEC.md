# Stage B: execution spec for proposed batch B1 (NOT APPROVED)

Reference: PR #38 `research/monkey-explains-1999` at `f176aa2861cd93913b977e6159a4e00f4eabeacc`. That run used Actor `streamers/youtube-scraper` build 0.0.318. The pilot was `eLqJpMWfweLnELwLX` ($0.012). The full run was `Us4zQZvU2IbImyHl3` (dataset `6qXYLfuijVGOM9iWX`, $0.488, 122 raw rows) with `transcriptionAndSubtitle=NONE`. It produced 76 public rows, 45 members-only rows kept as evidence, and 0 captions. Those costs belong to that historical run only. **@MonkeyExplains1999 is REUSE: do not rerun it.**

## Gate: all must hold before any call

- The owner approves the exact UC IDs, per-channel result limits and a USD ceiling. Free credits count against the ceiling.
- Decision 018 is satisfied: approved provider, a cost cap set before the run, no paid AI add-ons. Shorts are included only because the owner approves them as part of this batch.
- `APIFY_TOKEN` is read from the environment only and is never printed or saved.
- Recheck live, and record a timestamped receipt for each: Actor ID, build, input schema, pricing per event (video, date-range, transcript minute, AI), plan and balance.
- Stop if the build or schema differs from 0.0.318 in a field this spec uses, or if the price exceeds the $0.004/video estimate.

## B1 targets

| # | Channel | UC ID | Niche | Reported videos | Limit (total) | Est. USD |
|---|---|---|---|---:|---:|---:|
| 1 | Kevin Explains | `UCMl8WtFdqfnzzKcC2KWZZnQ` | FINANCE | 166 | 188 | 0.752 |
| 2 | Lana Maynes | `UCj0uhARVVmROWv9TBpVIr9Q` | FINANCE | 90 | 105 | 0.420 |
| 3 | Mark Calloway | `UCAOeipQ5KGzZ2McMF1RNsrQ` | FINANCE | 86 | 100 | 0.400 |
| 4 | Marcus Retires | `UCW_JmbBR0gsRGIUGRY3WA-Q` | FINANCE | 29 | 37 | 0.148 |
| 5 | Capital Case | `UCZXShYiBJlahi8mCNiU3XBg` | ECONOMICS | 13 | 20 | 0.080 |
| 6 | Business Decoded | `UCr1NnI7dwgIqeGJymhKL37A` | ECONOMICS | 42 | 52 | 0.208 |
| 7 | Built On You | `UC8p5EKG8jlsL2R2bvr2fZ3g` | ECONOMICS | 9 | 15 | 0.060 |
| 8 | Dr. Vitalis | `UCLxJ_nQg42P-0XNRdGwA2gg` | SENIOR_HEALTH | 27 | 35 | 0.140 |
| 9 | Dr. Cale Smith | `UCsPba6Pqq_cp37zyU6MP82g` | SENIOR_HEALTH | 17 | 24 | 0.096 |
| 10 | Dr. Wade Collins | `UC1rXgYI3Eqsyyt06QEbGg3Q` | SENIOR_HEALTH | 10 | 16 | 0.064 |
| 11 | Dr. Dinnes Senior | `UCvHD6lldf4L3XMAmGU44cYw` | SENIOR_HEALTH | 23 | 31 | 0.124 |
| 12 | Historically | `UCoZd78hRUdxxsuGiABuHF_A` | HISTORY | 85 | 99 | 0.396 |
| 13 | ThePastInLines | `UCSwjhnEm3TP94W_lvs9miIQ` | HISTORY | 38 | 47 | 0.188 |
| 14 | Ethos | `UC2YHYn047fkAob8Od3leQjw` | HISTORY | 19 | 26 | 0.104 |
| 15 | Rome Unscrolled | `UCuyKlvQhPbPKdENL8y1lDrA` | HISTORY | 9 | 15 | 0.060 |
| | **Total** | | | **663** | **810** | **3.240** |

- Each limit is 110% of the reported count plus 5. Split it per format (`maxResults`, `maxResultsShorts`, `maxResultStreams`) after the live tab counts are rechecked.
- **Proposed ceiling: $3.50.** That is $3.24 plus a pilot of about $0.02, with margin.
- Inputs use exact channel URLs of the form `https://www.youtube.com/channel/<UC ID>`.

## Run order

1. **Pilot.** One small channel (Rome Unscrolled), limits 3/3/0, subtitles NONE. Verify channel ownership (`channelId` equals the target), the output field shape and the per-video charge.
2. **Full B1.** Run only the approved IDs and limits.
   - Stop if a row's channel ID mismatches.
   - Stop if the cost-to-date projects over the ceiling.
   - Stop if the row count exceeds its limit or the output shape changes.
3. **Captions.** Run only if approved: existing-subtitles mode (`ALWAYS_SUBTITLES`-type, no speech-to-text fallback). Paid transcription, AI summaries, video analysis and thumbnail binaries each need their own approval. All default OFF.

## Capture and outputs (PR #38 conventions)

- **Per run:** raw dataset JSON, run JSON, sanitized input, Actor/build, UTC timestamps, run/dataset IDs, finalized `usageTotalUsd`, and SHA-256 of every raw file.
- **Per channel:**
  - `CHANNEL_IDENTITY.json` (subscriber and channel totals as time-stamped observations)
  - `VIDEO_MASTER.csv`/`.jsonl`
  - `VIDEO_METADATA_GAPS.csv`
  - `ACCESS_RESTRICTIONS.csv`
  - `METADATA_VALIDATION.json`
  - `SOURCE_COMPLETENESS_REPORT.md`
  - `APIFY_RUN_MANIFEST.json`
  - `FILE_CHECKSUMS_SHA256.json`
  - the workbook
- **Field rules:**
  - Keep regular videos, Shorts, streams and restricted (members-only) rows separate.
  - Write unknown fields as UNKNOWN or empty, **never 0**.
  - When a run is capped, do not claim full public coverage.
  - Caption fields: an existing caption track, retrieved caption text and generated ASR stay distinct.

## Validation (report local and CI results separately)

- Video IDs are unique and each URL matches its video ID.
- Every row belongs to the target channel ID.
- Raw, JSONL, CSV and workbook counts reconcile; regular + Shorts + streams + restricted adds up to the raw count.
- Missing-field semantics hold: no zero is substituted for an unknown.
- Hash manifest matches the files.
- Secret scan passes: no token, cookie or credential appears.

Do not register or publish anything in this stage. Registry ingestion needs a separate, explicitly approved follow-up (after PR #20 and the frozen-registry separation in PR #45).
