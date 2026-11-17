# Finance + Economics metadata acquisition: approval packet (NOT APPROVED)

Prepared 2026-11-10. This replaces the mixed-niche B1. Scope is the 31 incoming channels whose Stage A primary niche is FINANCE (24) or ECONOMICS (7). No Apify run has started and nothing has been spent. The canonical DB is untouched (read-only).

## 1. Live recheck (2026-11-10, public Apify API, no token used)

| Check | Result | Evidence |
|---|---|---|
| Actor | `streamers/youtube-scraper` (id `h7sDV53CddomktSi5`) | `source/live/actor.json` sha256 `8c83f1b3…b4a2` |
| Build | **0.0.327** (2026-11-09). PR #38 used 0.0.318. | `source/live/build.json` sha256 `f0058bcd…0473` |
| Input fields this plan uses | `startUrls`, `maxResults`, `maxResultsShorts`, `maxResultStreams`, `transcriptionAndSubtitle` (enum incl. `NONE`), `sortVideosBy` (`NEWEST`), `aiVideoDescription`/`aiVideoSummary` (default false): all present, same types. | `source/live/input_schema_live.json` |
| Price, Free tier | `result` (video) **$0.004**: unchanged. Add-ons not used: date-filter $0.0013, AI description/summary $0.015, transcript minute $0.048. | actor.json `pricingInfos` |
| Account balance / plan | **BLOCKED.** `APIFY_TOKEN` is not in this session's environment. | — |

The build changed, so the output row shape must be confirmed in the pilot against PR #38's raw shape before any tranche runs.

## 2. Reuse: six existing packages verified by channel ID

All six `CHANNEL_IDENTITY.json` files and every `VIDEO_MASTER.csv` row match the canonical UC ID. All snapshots are from 2026-10-20 and all have new uploads since then.

| Channel | Package | Snapshot UTC | Rows (type) | Live count 11-09 vs package | Recorded gaps |
|---|---|---|---|---|---|
| Primate Economics | PR #39 `primateeconomics` @967ea707 | 2026-10-20 07:54 | 29 (16 reg, 13 Shorts) | 30 vs 29 (+1) | 13 Shorts lack descriptions |
| Logical Money | PR #39 `logicalmoney72` | 2026-10-20 07:54 | 20 (19/1) | 26 vs 20 (+6) | none |
| Mark Invests | PR #39 `markbuildsus` | 2026-10-20 07:54 | 81 (81/0) | 98 vs 81 (+17) | none |
| Uncle Frank Retirement | PR #39 `unclefrankretirement16` | 2026-10-20 07:54 | 27 (27/0) | 35 vs 27 (+8) | none |
| Uncle John Financial | PR #39 `unclejohnfinancial` | 2026-10-20 07:54 | 53 (48/5) | 60 vs 56 (+4) | 3 reported videos never captured, and not marked members-only |
| MonkeyExplains | PR #38 `monkey-explains-1999` @f176aa28 | 2026-10-20 06:24 | 76 public (61/15), 45 members-only kept as evidence | 142 vs 121 (+21) | 3 descriptions missing, 48 gap rows |

Notes on these packages:

- No package collected captions (`transcriptionAndSubtitle=NONE`), so "false" in the caption field means not collected. It does not mean a video has no captions.
- No package downloaded thumbnail files. Thumbnail URLs are present.

**Proposed gap-fill (tranche G).** One newest-first run per channel (`sortVideosBy=NEWEST`). Each limit is the new-upload count plus 5 overlap rows. The overlap rows prove the new rows join onto the package with no gap. MonkeyExplains gets double the margin, because members-only rows appear in its feed and are billed.

- This needs no date-filter add-on.
- It does not refresh view counts on old rows.
- The Primate Economics Short descriptions and the 3 missing Uncle John videos are recorded as gaps only. Neither is in this plan.

## 3. Extraction targets

Full per-channel rows, including the start URL, the tabs seen and the scope, are in `Finance_List.csv`, `Economics_List.csv` and `All_31_Targets.csv`.

**How the limits were set:**

- **Regular videos.** The limit is the 2026-11-09 reported count ×1.10, plus 5.
- **Shorts.** A channel gets a Shorts limit only if its public Shorts tab exists. Of the 25 new channels, only 2 have one.
- **Streams.** No channel has a Live tab, so every stream limit is 0.

**Cost:** estimated cost = the limit × $0.004. That is the maximum. Billing counts only rows actually returned.

### FINANCE: first tranche (T1)

| Channel | UC ID | Package | Regular / Shorts / Streams | Est. USD |
|---|---|---|---|---:|
| Kevin Explains | `UCMl8WtFdqfnzzKcC2KWZZnQ` | none | 188 / 0 / 0 | 0.752 |
| Lana Maynes | `UCj0uhARVVmROWv9TBpVIr9Q` | none | 105 / 0 / 0 | 0.420 |
| Mark Calloway | `UCAOeipQ5KGzZ2McMF1RNsrQ` | none | 100 / 0 / 0 | 0.400 |
| Marcus Retires | `UCW_JmbBR0gsRGIUGRY3WA-Q` | none | 37 / 0 / 0 | 0.148 |

### FINANCE: follow-up (T2)

| Channel | UC ID | Package | Regular / Shorts / Streams | Est. USD |
|---|---|---|---|---:|
| Walter Canada | `UCQng0CgVwiA79VEPJ9e--zw` | none | 123 / 0 / 0 | 0.492 |
| Nia Prescott | `UC3a2fNfeG-zvJcuDD9R8bLw` | none | 109 / 0 / 0 | 0.436 |
| Finance POV | `UC4zls8vK8iiTSQpnaIxICkg` | none | 90 / 0 / 0 | 0.360 |
| Ronnie Finance | `UCA-ucSJ_2mY4EqjenOT2u3w` | none | 71 / 0 / 0 | 0.284 |
| POV Wealth | `UCryM-LAkg31P_B0GeshJQjg` | none | 71 / 0 / 0 | 0.284 |
| Robin MBA | `UCOvq-1piPnzCmrqfSspVIwA` | none | 67 / 0 / 0 | 0.268 |
| Madeline | `UChghyih02gp-TC7w22ULaXQ` | none | 59 / 0 / 0 | 0.236 |
| Nate's Money Map | `UCtOrKVgo-bsh4XoSCA8R_mg` | none | 40 / 0 / 0 | 0.160 |
| Finance ANALYST | `UCWQA4bQidJMFH3odS-RGEyA` | none | 37 / 0 / 0 | 0.148 |
| Frank Law | `UCdFjOki_gKUfvDq3SmL36mg` | none | 32 / 0 / 0 | 0.128 |
| Housing | `UC3Tzh0Wu1C9s3AI2Oqc8kIA` | none | 31 / 0 / 0 | 0.124 |
| Arthur Penrose, UK Pension Guide | `UCsAnRVKKrZCD7YRVLu5FdSQ` | none | 30 / 0 / 0 | 0.120 |
| Wealth Logic Australia | `UCpUvGrDOLrlhpUr5hXnpD9g` | none | 29 / 0 / 0 | 0.116 |
| This make cents | `UCWrtDO6izx1KXQu_BZBrQYg` | none | 27 / 27 / 0 | 0.108 |
| Sarah Rickshaw | `UCn2nfMN6I-ozJikqW-zk_6A` | none | 19 / 0 / 0 | 0.076 |

### FINANCE: reuse plus gap-fill (G)

| Channel | UC ID | Package | Regular / Shorts / Streams | Est. USD |
|---|---|---|---|---:|
| Mark Invests | `UCcj_KU4ZN6bx6Ki68hNJWqw` | PR #39 | 22 / 0 / 0 | 0.088 |
| Uncle Frank Retirement | `UCLh3aiudWdnfR0QDC8aLEhQ` | PR #39 | 13 / 0 / 0 | 0.052 |
| Logical Money | `UCKhpM-cu2Cod-GyG6KngNYg` | PR #39 | 11 / 11 / 0 | 0.044 |
| Uncle John Financial | `UCWugleQL2wqr5N1X4o8yyLw` | PR #39 | 9 / 9 / 0 | 0.036 |
| Primate Economics | `UC14Fb2zWTEZklONPXFbLrTQ` | PR #39 | 6 / 6 / 0 | 0.024 |

### ECONOMICS: first tranche (T1)

| Channel | UC ID | Package | Regular / Shorts / Streams | Est. USD |
|---|---|---|---|---:|
| Business Decoded | `UCr1NnI7dwgIqeGJymhKL37A` | none | 52 / 0 / 0 | 0.208 |
| Capital Case | `UCZXShYiBJlahi8mCNiU3XBg` | none | 20 / 0 / 0 | 0.080 |
| Built On You | `UC8p5EKG8jlsL2R2bvr2fZ3g` | none | 15 / 0 / 0 | 0.060 |

### ECONOMICS: follow-up (T2)

| Channel | UC ID | Package | Regular / Shorts / Streams | Est. USD |
|---|---|---|---|---:|
| Mr. Ranks | `UCGwJ94gUJNUWt-EW3zpWotA` | none | 69 / 0 / 0 | 0.276 |
| Econ in a Nutshell | `UC_DdIoJzHZXlEKTVy41_KQw` | none | 19 / 0 / 0 | 0.076 |
| The Wealth Engine | `UCfTD1TTaLoeF02x8wWFUcKw` | none | 14 / 14 / 0 | 0.056 |

### ECONOMICS: reuse plus gap-fill (G)

| Channel | UC ID | Package | Regular / Shorts / Streams | Est. USD |
|---|---|---|---|---:|
| MonkeyExplains | `UCiBGqUxeTe4AYQyRseSZaKw` | PR #38 | 47 / 47 / 0 | 0.188 |

For the 6 reuse channels, each limit is the new-upload count plus 5 overlap rows (MonkeyExplains has extra margin). These are not full-channel limits.

### Totals and proposed hard caps

| Tranche | Channels | Max billable rows | Est. USD | **Proposed hard cap** |
|---|---:|---:|---:|---:|
| Pilot (Built On You, 3/0/0) | 1 | 3 | 0.012 | 0.05 |
| T1: B1 Finance/Economics subset | 7 | 517 | 2.068 | **2.25** |
| G: reuse gap-fill | 6 | 108 | 0.432 | **0.50** |
| T2: follow-up | 18 | 937 | 3.748 | **4.00** |
| **All 31** | 31 | 1,565 | 6.26 | **6.80** |

Free credits count against these caps.

## 4. How the run would work once approved

- **One run per channel.** `maxResults*` limits apply per channel, so a separate run is the only way to keep each channel at its own approved limit.
  - Each run carries `maxTotalChargeUsd` set to its estimate + $0.01 (`PROPOSED_ACTOR_INPUTS_SANITIZED.json`).
  - The tranche cap is checked against cumulative `usageTotalUsd` before each next run.
- **What is collected.** Captions `NONE`. AI add-ons off. No media or thumbnail files downloaded. Public content only.
- **Pilot first.** Check four things:
  - every row's `channelId` equals the target ID;
  - the row shape matches PR #38 on build 0.0.327;
  - the charge per video is $0.004;
  - no add-on events were charged.
- **Then the approved tranche, with these stops:**
  - a row's channel ID does not match the target;
  - spend so far is on course to exceed the cap;
  - more rows come back than the limit allows;
  - the output shape changes.
- **Outputs, in PR #38 format, for each channel:**
  - `CHANNEL_IDENTITY.json`, with subscriber and total counts stamped with the time they were observed;
  - `VIDEO_MASTER.csv` and `.jsonl`, covering titles, descriptions, publish times, durations, views, likes, comments, watch URLs and thumbnail URLs;
  - `VIDEO_METADATA_GAPS.csv`, `ACCESS_RESTRICTIONS.csv` and `METADATA_VALIDATION.json`;
  - the run manifest, the raw JSON and SHA-256 checksums.
- **Field rules.** An unknown value is written as UNKNOWN or left empty, never 0. Members-only rows stay separate. When a run hits its limit, it is not reported as full public coverage.
- **Where results go.** Durable local storage (`~/YIOS-local-audits/…`). Nothing is registered, no DB is written, and nothing is committed or put in a PR unless separately asked.

## 5. Owner approval needed (reply with exact choices)

1. **Tranches:** pilot, plus T1 (7 IDs above), plus G (6 IDs), with caps $0.05, $2.25 and $0.50 ($2.80 total). Or approve a different set.
2. Whether T2 (18 IDs, $4.00 cap) runs in the same session after T1 validates, or waits for a separate approval.
3. **The token.** `APIFY_TOKEN` must be present in the environment that launches Claude Code, so the live balance and plan can be checked. It is never printed or saved.
4. **The build.** Accept build 0.0.327, subject to the pilot shape check.
