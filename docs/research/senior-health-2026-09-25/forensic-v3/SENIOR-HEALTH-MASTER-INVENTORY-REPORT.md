> **SUPERSEDED (2026-09-28):** the current inventory, category counts, exact missing IDs and paid-run plan are in `SENIOR-HEALTH-MASTER-INVENTORY-REPORT-2026-09-28.md`, `SENIOR-HEALTH-MASTER-INVENTORY-2026-09-28.json/.csv` and `PAID-ACQUISITION-PLAN-2026-09-28.md` (live re-enumeration, 143 leads, per-video public metadata DS-000034). This file is kept unchanged below as the 2026-09-25 historical record.

# Senior Health Master Inventory, Missing-Data Matrix & Acquisition Plan — 2026-09-25

**Status:** Phases 1–4 and 6 complete, zero-spend. Phases 5 (live Apify account audit) and 7 (paid acquisition) are **BLOCKED**: the Claude-in-Chrome extension reports an OAuth account mismatch and `APIFY_TOKEN` is not set, so the authenticated Apify Console could not be opened. No Actor run was started; spend this pass: **$0.000**.

Machine-readable sources (regenerate with `scripts/build_master_inventory.py`):
- `SENIOR-HEALTH-MASTER-INVENTORY.json` / `.csv` — one record per recovered lead (69), with exact missing video IDs.
- `live-catalog-2026-09-25/live/*.json` — raw public YouTube tab enumeration (Videos, Shorts, Live), every video ID and title, observed 2026-09-25 by `scripts/yt_tabs.py`. Public web pages only; not the YouTube Data API.
- `live-catalog-2026-09-25/candidates.tsv` — the recovered lead list and its source report.
- `live-catalog-2026-09-25/apify-actor-public-2026-09-25.json` — public (unauthenticated) Actor record: latest build and public tier pricing.

## Method

1. **Recovery (Phase 1).** Every `UC…` ID and `@handle` in every Senior Health document was extracted (117 files, 107 IDs; 75 of those IDs are registry channels, most outside this niche). Sources: the canonical registry, `SENIOR-HEALTH-ACQUISITION-AND-REPO-SYNC-REPORT-2026-09-22.md` (8 seeds), `SENIOR-HEALTH-CHANNEL-DISCOVERY-2026-09-22.md` (24 candidates), `COMPETITOR-DISCOVERY-REGISTER.md` Part B (10 new + exclusions), `EXTERNAL-BREAKOUT-RESEARCH-RAW.md` / `SMALL-CHANNEL-BREAKOUT-FORENSICS.md` / `forensic-v2/external/CH_channel_pages.txt` (16 breakout-research handles). Handles were resolved to canonical IDs from each live page's `<link rel="canonical">`; deduplication is by Channel ID only.
2. **Live catalog (Phase 2/6).** For each resolvable channel the public Videos, Shorts and Live tabs were fully paginated. A tab is recorded `TAB_ABSENT(...)` only when YouTube served a different tab for that route (verified per channel, not assumed). For every live channel with a header count, Videos + Shorts + Live equals the header count, except three adjacent/reference channels not proposed for spend: ElderfitTV (179 of 191 enumerable), SeniorHood (74 of 76) and Health Wellness Pharmacist (Shorts enumeration errored; UNKNOWN). Those differences are UNKNOWN (possibly members-only or otherwise non-public items), not extraction failures.
3. **Comparison.** Live IDs were diffed against `videos` in `youtube_channel_registry.db`. A gap consisting only of the newest items of a newest-first tab is classified `NEW_UPLOADS_SINCE_SNAPSHOT` (catalog complete at acquisition time); anything else is `HISTORICAL_GAP`.
4. **Apify recovery (Phase 5, partial).** The inventory DB registers 8 `streamers/youtube-scraper` runs; all 8 have manifests under `data/manifests/apify/` and all are ingested. Whether the account holds other completed, unintegrated runs **cannot be checked without Console access** — this remains open.

## Headline totals

| Category (final-requirements vocabulary) | Count | Channels |
|---|---:|---|
| ALREADY COMPLETE (catalog complete at snapshot) | 6 | Dr. Okoro, Doctor Thomas, Dr. Aliza Wright \| Advice, Senior Health Hub, Dr. Ares Senior, Dr. Elias Senior Health |
| PARTIALLY ACQUIRED (historical gap) | 1 | Better Health While Aging — 4 oldest Shorts |
| QUALIFIED AND PENDING (direct, never acquired) | 14 | backlog Group C, table below |
| IDENTITY ONLY (discovered, adjacent/reference/low-priority, not proposed for spend) | 34 | table below |
| REMOVED / UNVERIFIABLE / EXCLUDED | 13 | table below |
| OWN CHANNEL (held out of competitor statistics) | 1 | Decode Your Heart – Dr. Rehan (complete: 27 + 29 = 56) |
| NEWLY DISCOVERED (this pass) | 0 | Phase 11 not started, by the brief's priority order |
| NEWLY ACQUIRED (this pass) | 0 | blocked on Console access |
| INDIVIDUAL ANALYSIS COMPLETE (Phase 9 standard) | 0 | 7 competitors have case-level sections in `SMALL-CHANNEL-BREAKOUT-FORENSICS.md`; none has a standalone per-channel analysis |
| **Total recovered leads** | **69** | |

Phase-2 letter classes: A = 6, B = 1, C = 0, D = 0, E = 48 (14 qualified + 34 identity-only), F = 13, own = 1. C and D are empty because no Senior Health channel is registered metadata-only, and the two historical screenshot-only subjects (Dr. Okoro via DS-000005, Doctor Thomas via DS-000003) have since been fully acquired (DS-000028, DS-000029).

## Findings that change prior records

1. **BHWA gap re-verified with exact IDs.** Live: 80 regular + 18 Shorts + no Live tab = 98 (header 98). Repository: 80 + 14. Cause: `actor_input.json` for run `AuZ65QkXBmVIXcOn9` set `maxResultsShorts: 14`. Missing: `-SMFhfZrjm0` (All About IADLs), `U6kI1V6CQVs` (All About ADLs), `5Jqvsfq6UBo` (Aging Parent with Memory Loss Won't Accept Help), `x0Z5ziQNtWQ` (DO THIS: 4 Types of Exercise in Aging). All 4 are publicly listed today; none appears anywhere else in the repository or in any registered Apify dataset.
2. **Three "complete" channels now have post-snapshot uploads** (not extraction failures): Dr. Elias +12 (repo newest 2026-09-09), Dr. Ares +2, Senior Health Hub +1. Exact IDs are in the JSON.
3. **Senior Fitness With Meredith has 100 archived streams.** The earlier "454 videos, $1.82" estimate is correct in total but is 340 regular + 14 Shorts + 100 streams. A run with `maxResultStreams: 0` (the pipeline default) would silently miss 22% of the catalog.
4. **Senior Wellness** is now 100 (was 98/99); **Dr. Holloway** 49, **Healthy Aging (r5z)** 35 (was 33), **Health Science Daily** 12 (was 10). Historical counts were not reused.
5. **Correction to `COMPETITOR-DISCOVERY-REGISTER.md` Part B:** `@SeniorShapeFitness` does **not** redirect to Dr. Waterling. It resolves to its own channel `UCkWYei5MULuRDhH7uxtZqqA` ("SeniorShape Fitness", 880K subscribers, 370 regular + 46 Shorts). Reclassified from excluded to identity-only / requalify; not proposed for spend until its niche fit is sampled.
6. Dead handles (`@SeniorWellnessPodcast`, `@seniorlifenutrition`, `@SeniorHealthCares`) still return 404; the 5 removed/terminated/empty channels are unchanged; `@memoryhealthnutrition` is still empty.
7. **Registry projection gap (not missing evidence):** `videos.thumbnail_url` is empty for the Apify-sourced Senior Health channels, although all 5 raw Apify datasets carry a thumbnail URL for every record (DS-000028 66/66, DS-000029 22/22, DS-000030 122/122, DS-000032 56/56, DS-000033 94/94) and channel-level `thumbnail_metadata_status` is already `COMPLETE`. Downloaded thumbnail images exist only for DS-000006, DS-000017, DS-000019.
8. Dr. Ares Senior's 35 registered videos carry `video_type = 'regular video'` rather than `video`; all 37 live items are on the Videos tab, so they are regular uploads.

## Missing-data matrix

### Registered channels (A/B) and own channel

| Class | Channel | Channel ID | Live regular / Shorts / streams | Repo regular / Shorts / other | Real transcripts | Descriptions | Missing (kind) |
|---|---|---|---|---|---:|---:|---|
| OWN | Decode Your Heart - Dr. Rehan | `UCQIzqH7QZ9viBYpOFqgSXMg` | 27 / 29 / 0 | 27 / 29 / 0 | 56 | 56 | 0  |
| A | Senior Health Hub | `UCAYG0fzUyxv6OevH88qA45w` | 121 / 2 / 0 | 120 / 2 / 0 | 122 | 120 | 1 (NEW_UPLOADS_SINCE_SNAPSHOT) |
| A | Dr. Okoro | `UCMJxAeBJ0d1JC937de1eZ0Q` | 65 / 1 / 0 | 65 / 1 / 0 | 66 | 66 | 0  |
| A | Doctor Thomas | `UCFuGMi0idGeyXl6wYK9hg7Q` | 22 / 0 / 0 | 22 / 0 / 0 | 21 | 21 | 0  |
| A | Dr. Aliza Wright \| Advice | `UCXZi5JVeuTluazF-fYqQgNA` | 32 / 0 / 0 | 32 / 0 / 0 | 32 | 32 | 0  |
| A | Dr. Ares Senior | `UC356D-NzdnznBOftTpYoBLw` | 37 / 0 / 0 | 0 / 0 / 35 | 35 | 35 | 2 (NEW_UPLOADS_SINCE_SNAPSHOT) |
| A | Dr. Elias Senior Health | `UCQcBYZxFW7YwNMU8-DsT3Uw` | 41 / 0 / 0 | 29 / 0 / 0 | 29 | 29 | 12 (NEW_UPLOADS_SINCE_SNAPSHOT) |
| B | Better Health While Aging | `UCFpxvukIqCAUA7YizI-q9Dw` | 80 / 18 / 0 | 80 / 14 / 0 | 94 | 94 | 4 (HISTORICAL_GAP) |

### Qualified, never acquired (class E, backlog Group C) — priority order

| # | Channel | Channel ID | Header | Live regular | Live Shorts | Live streams | Streams tab | Results needed | Est. @ $0.004 | Cumulative |
|---:|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| 1 | Senior Wellness | `UCslmaJaMSw8F8BId4CxByJw` | 100 | 100 | 0 | 0 | TAB_ABSENT(Home) | 100 | $0.400 | $0.400 |
| 2 | More Life Health Seniors | `UCC4TRhL4BiA7--jpxVVXcpQ` | 162 | 159 | 3 | 0 | TAB_ABSENT(Home) | 162 | $0.648 | $1.048 |
| 3 | Senior Fitness With Meredith | `UC2BaKQ5vqal9yaC-VbpD5ZQ` | 454 | 340 | 14 | 100 | Live | 454 | $1.816 | $2.864 |
| 4 | Dr. Brooks \| Senior Health | `UClzqmRzoC-7r8GiB_XQUn_A` | 107 | 107 | 0 | 0 | TAB_ABSENT(Videos) | 107 | $0.428 | $3.292 |
| 5 | Senior Health Today | `UCLxLjL1XVaKqZg-wZ2EBspA` | 57 | 57 | 0 | 0 | TAB_ABSENT(Home) | 57 | $0.228 | $3.520 |
| 6 | The Senior Centered PT | `UCRxZVn1cDGyo_p7ZbxhkeUQ` | 66 | 62 | 4 | 0 | TAB_ABSENT(Home) | 66 | $0.264 | $3.784 |
| 7 | Dr. Nora Khalil | `UCX_cW2SeHF1iBxbjx41vfrA` | 65 | 65 | 0 | 0 | TAB_ABSENT(Home) | 65 | $0.260 | $4.044 |
| 8 | Dr. Franklin Senior Health | `UCPjG4ZRBkiO1y_vHlnj8jIg` | 37 | 37 | 0 | 0 | TAB_ABSENT(Videos) | 37 | $0.148 | $4.192 |
| 9 | Senior Vital Health | `UCUUKjcYdqOHk2j-pbUnWDNw` | 195 | 195 | 0 | 0 | TAB_ABSENT(Videos) | 195 | $0.780 | $4.972 |
| 10 | Healthy Aging Hub | `UC4oT7W2VOi-TJI3WWU51DHA` | 516 | 500 | 16 | 0 | TAB_ABSENT(Home) | 516 | $2.064 | $7.036 |
| 11 | Senior Meal Coach | `UCHOrUqhgZmEwhmXqvLwghpg` | 94 | 92 | 2 | 0 | TAB_ABSENT(Videos) | 94 | $0.376 | $7.412 |
| 12 | Senior Mobility Care | `UCj-4CkWt2waFCjt5h7fZSiA` | 15 | 2 | 13 | 0 | TAB_ABSENT(Home) | 15 | $0.060 | $7.472 |
| 13 | Ageless Balance | `UCxD2fste1dR0EUhj0gB8aOw` | 62 | 60 | 2 | 0 | TAB_ABSENT(Home) | 62 | $0.248 | $7.720 |
| 14 | Healthy Living After 60 | `UC6VFFdBkvTxy8VUO0d2h1Xg` | 99 | 69 | 30 | 0 | TAB_ABSENT(Home) | 99 | $0.396 | $8.116 |

### Other discovered channels (class E, adjacent / reference / lower-priority direct — not proposed for spend)

| Channel | Channel ID | Prior class | Live regular / Shorts / streams | Results if acquired |
|---|---|---|---|---:|
| Dr. Waterling | `UCLVvBoFiBC6oj7mT62GFAEA` | adjacent_downgraded | 71 / 0 / 0 | 71 |
| Healthy Aging with Dr. Doctor | `UCZyMQ8q7rq83_705upHZyTA` | adjacent | 119 / 270 / 5 | 394 |
| Dr. Holloway After 60 | `UC5pKio2JgSLI2vkBzny6nEg` | small_direct | 49 / 0 / 0 | 49 |
| Healthy Aging - Senior Health Tips | `UCk6fYu-O4DR1x2taFkAu_BA` | small_direct | 5 / 0 / 0 | 5 |
| Dr. James Senior Health Tips | `UCP8RIWduYwo86eX_bbOrK4w` | small_direct | 16 / 0 / 0 | 16 |
| Wisdom After 60 | `UC5MkHMM9vnjSb0MFp4AmKgQ` | mixed | 6 / 0 / 0 | 6 |
| ElderfitTV Experts In Over 60s Health & Fitness | `UCTDTzy68kOwNdyJVLgDf8Og` | adjacent | 137 / 42 / 0 | 179 |
| Body Fix Exercises—for over 50s | `UC9QgDBvyfbflM9zCBqp2GNA` | adjacent | 208 / 20 / 0 | 228 |
| Senior Book | `UCVrDYU1DiPbgrUVuBPrXrnw` | mixed | 55 / 0 / 0 | 55 |
| Healthy Aging | `UCfC4q2PEmYGaem9_w4HqkcQ` | small_direct | 35 / 0 / 0 | 35 |
| Dr. Dani Fisher | `UCK5aB2dkLd7Nijh9cTdGNEw` | adjacent | 41 / 23 / 0 | 64 |
| Life After 60+ | `UCWMQjQav8YSbAq17YVrqjKg` | mixed | 111 / 0 / 0 | 111 |
| Health Science Daily | `UC_l_kwmbc2aAYB6HoBFQ8Jw` | mixed | 12 / 0 / 0 | 12 |
| Healthy After 60 | `UCHKL5CjA8WbYb1M-FsECINA` | small_direct | 31 / 0 / 0 | 31 |
| Dr. Misha Kogan | `UCOftxdr17X7h_7OicYB5chw` | adjacent | 212 / 7 / 0 | 219 |
| Richard Kelley M.D. | `UCjPqI2_Ym14ufiF5rFvTt_w` | adjacent | 80 / 24 / 0 | 104 |
| Living Our Best With Memory Loss | `UC-utlT1CFaucWho9VNvafOw` | adjacent | 44 / 36 / 0 | 80 |
| Her Health 60+ | `UC_2ODzPSUYDfGA_wdUSnCOA` | adjacent_flagged | 139 / 0 / 0 | 139 |
| SeniorShape Fitness | `UCkWYei5MULuRDhH7uxtZqqA` | adjacent_requalify | 370 / 46 / 0 | 416 |
| Gentle Health | `UCWaCQ2kTiKH2gi4JFL8Jd6w` | breakout_reference | 260 / 13 / 0 | 273 |
| Amos Boone | `UC6KTAvulzsVXazS3Sh9WlxQ` | breakout_success | 43 / 0 / 0 | 43 |
| SeniorHood | `UCoGVNMCKuxaj2F3USdjgh0Q` | breakout_success | 74 / 0 / 0 | 74 |
| Aging Senior Health | `UCiWDd6ZLoAnAx8puH_LW7Dg` | breakout_failure | 71 / 39 / 0 | 110 |
| Fit Lit Health | `UCCuyfe6dQSAk9GtIwZulm_A` | breakout_reference | 130 / 14 / 0 | 144 |
| Senior Mobility | `UC7-ayx2Gvl-LY-nWduvZ0Eg` | breakout_failure | 13 / 0 / 0 | 13 |
| Health 365 | `UCdcxd2LzKjS3c7N0ts3U8fg` | breakout_failure | 54 / 0 / 0 | 54 |
| Senior strength secrets | `UCkgngn8vg4ke7sdVhukQraQ` | breakout_failure | 37 / 4 / 0 | 41 |
| Dr. Yonatan Whitten | `UCKKl53eAW7ZRiG-mkKlytHg` | established_reference | 277 / 110 / 0 | 387 |
| SENIOR FOOD BLOG | `UCigmuqNIp6jowy4Fhos4B5w` | established_reference | 79 / 0 / 0 | 79 |
| Senior BeWell | `UC0VKDC7DQLEp49PYNCAYpwQ` | established_reference | 243 / 0 / 0 | 243 |
| Seniors Circle | `UChNzlaVNP2SD523yfBuJFkA` | established_reference | 114 / 0 / 0 | 114 |
| Dr Todd Sullivan | `UCl1D88Sx_HAoUGEI3m46DPw` | adjacent_reference | 275 / 202 / 0 | 477 |
| Health Wellness Pharmacist | `UCQMoPZTEzln2uLS9opH845g` | large_reference | 1010 / — / 27 | 1037 |
| TopHealthTips | `UCsPe1heI3hv4sXzG_MIiySQ` | breakout_reference | 147 / 0 / 0 | 147 |

### Removed, unverifiable or excluded (class F)

| Channel | Channel ID / handle | Reason | Live status 2026-09-25 |
|---|---|---|---|
| Dr. Adewale | `UC5qNIOYcXj-uIh6n5dWfLLg` | removed | This channel was removed because it violated our Community Guidelines. |
| The Health Educator | `UC8ycZesiOH1DSgZl_qjruvg` | removed | This channel was removed because it violated our Community Guidelines. |
| The Senior Health Podcast | `UCeY8vK104Gbzp4aqnTz4gzQ` | terminated | This account has been terminated for violating YouTube or Google's Terms of Service. |
| Senior Health Protect | `UC1kEG25q-JE69jVw5ITXCrA` | terminated | This account has been terminated for violating YouTube or Google's Terms of Service. |
| Ageless Science | `UCEKEI-mj_sFPB6uU_SPPLNg` | empty | doesn't have any content |
| Senior Doctor | `UCHD_OASn-zMvONZyhhKECQw` | persona_clone | live, excluded by rule (29 videos) |
| Senior Health (V) | `UCgJ-ngDJ4tDDcdaGnWo8rJQ` | persona_clone | live, excluded by rule (22 videos) |
| Senior Health Care Explained | `UCCxtkPept6w5ZpiYwlqNdsQ` | thin | live, excluded by rule (3 videos) |
| Senior Wellness Podcast | `@SeniorWellnessPodcast` | dead_handle | HANDLE_UNRESOLVED:<HTTPError 404: 'Not Found'> |
| Senior Life Nutrition | `@seniorlifenutrition` | dead_handle | HANDLE_UNRESOLVED:<HTTPError 404: 'Not Found'> |
| SeniorHealthCares | `@SeniorHealthCares` | dead_handle | HANDLE_UNRESOLVED:<HTTPError 404: 'Not Found'> |
| Memory Health | `UClKQ8qjOGi2up1Jcjz6MoMg` | empty | doesn't have any content |
| Dr. Aliza Wright (Senior Health clone) | `UC1SDr8dfs0uED3GQIBW6edg` | persona_clone_breakout | live, excluded by rule (35 videos) |

Transcript and description completeness for acquired channels (public-catalog completeness is reported separately above):

| Channel | Real subtitles / acquired | Descriptions / acquired | Disclosed gaps |
|---|---|---|---|
| Better Health While Aging | 94 / 94 | 94 / 94 | 4 Shorts not acquired |
| Senior Health Hub | 122 / 122 | 120 / 122 | 2 descriptions verified empty on public watch pages (DS-000030_DESCRIPTION_VERIFICATION.json) |
| Doctor Thomas | 21 / 22 | 21 / 22 | `fj4TaPrLl8U` has no YouTube captions (`NO_SUBTITLE_AVAILABLE`); 1 description empty |
| Dr. Okoro | 66 / 66 | 66 / 66 | — |
| Dr. Aliza Wright \| Advice | 32 / 32 | 32 / 32 | — |
| Dr. Ares Senior | 35 / 35 | 35 / 35 | — |
| Dr. Elias Senior Health | 29 / 29 | 29 / 29 | — |
| Own: Dr. Rehan | 56 / 56 | 56 / 56 | — |

## Budget state (from repository records — live values NOT verified)

| Item | Value | Source |
|---|---|---|
| Owner-approved campaign cap | $4.50 | `docs/audits/SENIOR_HEALTH_ACQUISITION_CHECKPOINT.md` |
| Campaign runs since cap | Okoro $0.264, Thomas $0.088, SHH $0.488, BHWA $0.376 = **$1.216** | `apify_source_runs` |
| Own-channel run DS-000032 | $0.224 — not recorded as inside or outside the cap | `apify_source_runs` |
| Remaining approved budget | **$3.060** (conservative, counting DS-000032) to $3.284 | derived |
| Account credit | $3.40 last reported; **unverified** | brief |
| Actor / build | `streamers/youtube-scraper` / `0.0.303` (public latest, finished 2026-09-18) — same build as all recent runs | public Actor API |
| Price | $0.004 per result, public FREE tier; `result` is the only event charged when AI add-ons and date filters are off; no start fee listed. Authenticated price **unverified** | public Actor API |

## Proposed acquisition scope (awaiting authorization + Console access)

Every run: `transcriptionAndSubtitle: "ALWAYS_SUBTITLES"` (existing YouTube captions only; prior runs with this setting billed `transcribeMinute: 0`), `subtitlesLanguage: "any"`, `subtitlesFormat: "plaintext"`, `aiVideoDescription: false`, `aiVideoSummary: false`, no `oldestPostDate`/`dateFilter` (avoids the $0.0013 date-filter event), platform `maxTotalChargeUsd` set to the hard cap. The deprecated `downloadSubtitles` key (still emitted by `scripts/apify_youtube_ingest.py build_actor_input`) is not used. One channel per run; each run is validated, ingested with `scripts/apify_youtube_ingest.py ingest-existing`, packaged, registered and committed before the next starts.

| Run | Target | Input (beyond the common settings) | Results | Expected | Hard cap | Cumulative cap |
|---|---|---|---:|---:|---:|---:|
| R1 | BHWA historical backfill | `startUrls`: the 4 exact `https://www.youtube.com/shorts/<id>` URLs above | 4 | $0.016 | $0.020 | $0.020 |
| R2 | Dr. Elias refresh | channel URL, `sortVideosBy: NEWEST`, `maxResults: 12`, Shorts 0, streams 0 | 12 | $0.048 | $0.060 | $0.080 |
| R3 | Dr. Ares refresh | channel URL, NEWEST, `maxResults: 2` | 2 | $0.008 | $0.012 | $0.092 |
| R4 | Senior Health Hub refresh | channel URL, NEWEST, `maxResults: 1` | 1 | $0.004 | $0.008 | $0.100 |
| R5 | Senior Wellness | `UCslmaJaMSw8F8BId4CxByJw`, `maxResults: 100`, Shorts 0, streams 0 | 100 | $0.400 | $0.420 | $0.520 |
| R6 | More Life Health Seniors | `UCC4TRhL4BiA7--jpxVVXcpQ`, `maxResults: 159`, `maxResultsShorts: 3`, streams 0 | 162 | $0.648 | $0.668 | $1.188 |
| R7 | Senior Fitness With Meredith | `UC2BaKQ5vqal9yaC-VbpD5ZQ`, `maxResults: 340`, `maxResultsShorts: 14`, `maxResultStreams: 100` | 454 | $1.816 | $1.840 | **$3.028** |

**Proposed cumulative maximum: $3.028** (expected $2.940), inside the conservative $3.060 remaining approved budget and the last-reported $3.40 credit. Caps allow a few results of headroom for uploads between now and the run.

- R1 note: a video-URL run returns only the requested items, so no already-held Short is re-bought. Fallback if the Actor does not return Shorts for `/shorts/` URLs: channel URL with `maxResults: 0, maxResultsShorts: 18` (18 results, $0.072, 14 duplicates discarded by video ID). Confirm after the run that the 4 records carry `channelId = UCFpxvukIqCAUA7YizI-q9Dw` and are typed as Shorts.
- R2–R4 are optional snapshot refreshes; skipping them saves $0.060 and leaves those channels "complete as of snapshot".
- Next by priority, **outside the current budget**: Dr. Brooks ($0.428), Senior Health Today ($0.228), The Senior Centered PT ($0.264), Dr. Nora Khalil ($0.260), Dr. Franklin ($0.148), Senior Vital Health ($0.780), Healthy Aging Hub ($2.064), Senior Meal Coach ($0.376), Senior Mobility Care ($0.060), Ageless Balance ($0.248), Healthy Living After 60 ($0.396). All 14 qualified channels total $8.116; the 11 not in R5–R7 need $5.252 of new authorization.
- Subtitle coverage cannot be pre-computed without per-video checks; past Senior Health runs averaged 99.7% caption availability (303 of 304 videos in DS-000028/29/30/33). Missing subtitles will be recorded as `NO_SUBTITLE_AVAILABLE`, never fabricated.

## Blockers and what unblocks them

1. **Browser extension account mismatch** (`tabs_context_mcp`: "the OAuth token Claude Code is using belongs to a different claude.ai account"). Fix: unset `CLAUDE_CODE_OAUTH_TOKEN` if set, `/logout` then `/login` in Claude Code, and sign the Chrome extension into the same claude.ai account. Alternatively export `APIFY_TOKEN` in the shell for the API pipeline.
2. **Owner authorization** for R1–R7 (cap $3.028) or a subset, and a ruling on whether DS-000032 counts against the $4.50 cap.
3. After access: verify live credit, billing period, authenticated price, and scan the account's run list for completed runs whose default dataset is not among the 8 registered `actor_run_id`s before paying for anything.

## Not done in this pass (by the brief's priority order)

Phase 9 individual research, Phase 10 combined-analysis recomputation and Phase 11 new discovery all depend on acquisitions that could not run. No research conclusion or statistic was changed; the V3 reports and workbook still describe the 7-channel internal cohort.
