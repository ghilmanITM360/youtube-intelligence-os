# Codex Brief — Validate Dr Rehan's 30-Day Topics (Google Trends + YouTube + News)

> **Roman Urdu summary:**
> - Codex har topic ko Google Trends par check karega: 12 months, 30 days, 7 days aur 24 hours. Web Search aur YouTube Search dono par.
> - Phir YouTube par dekhega ke is mahine, is hafte aur aaj upload hui videos ko kitne views mile. 24 ghante ka asli farq do snapshots se nikalega.
> - Phir news check karega.
> - Aakhir mein har topic ko GO / ANGLE-CHANGE / SWAP / DROP dega. Results CSV mein bhare jayenge.

## 0. Context
- **Channel:** Decode Your Heart – Dr. Rehan (`UCQIzqH7QZ9viBYpOFqgSXMg`). Real cardiologist, 55 subs, 66 videos.
- **Pivot:** pure senior health (60+). Three pillars: Heart & BP after 60, heart medicines after 60, heart tests after 60.
- **Plan + calendar:** `01-REVIEW-PIVOT-AND-30-DAY-CALENDAR.md`. Read sections 2 and 3 first.
- **Input:** `03-topics-for-validation.csv` has 20 topics (T01–T20). Each row lists keywords, YouTube queries and competitor evidence. Columns from `gt_` onward are blank; you fill them.
- **Window:** checks happen on the day you run them. Record `checked_at` as ISO-8601 UTC on every row.

## 1. Rules (from AGENTS.md — non-negotiable)
1. **No YouTube Data API.**
   - Use the public YouTube website in a browser, logged out or incognito, so personalization stays minimal.
   - No paid Apify or other paid tools without the owner's approval.
2. **Never modify raw evidence.**
   - Save raw snapshots as new files under `data/raw/channel-data/dr-rehan-topic-validation-<YYYY-MM-DD>/`.
   - Snapshot types: Trends CSV downloads, page text or JSON, and screenshots if needed.
   - Add `SHA256SUMS.txt` and a short `README.md` covering what, when, how and which tool.
3. **Label every number:**
   - **OBSERVED:** read off a page or CSV.
   - **INFERRED:** computed.
   - **NOT VERIFIED:** anything else.
   - Google Trends values are **relative indices (0–100), not search volumes**. Never present them as volumes.
4. Do not edit `01-...md`. Write results to the CSV and a new `04-CODEX-VALIDATION-RESULTS.md`.
5. Do not log in to Dr Rehan's YouTube or Studio.
6. Work on a branch, and commit only the files listed in section 6.

## 2. Google Trends (trends.google.com, browser)
For each topic, use `primary_keyword`. If it is near zero, also try `alt_keywords` one by one and record the best-performing term in `gt_best_term`.

| Run | Geo | Time range | Property | Fill column |
|---|---|---|---|---|
| a | United States | Past 12 months | Web Search | `gt_us_12m_shape` (rising / flat / falling / seasonal-peak-now / seasonal-peak-later) |
| b | United States | Past 30 days | Web Search | `gt_us_30d_avg` (avg index), `gt_us_30d_last7_vs_prev` (up / flat / down) |
| c | United States | Past 7 days | Web Search | `gt_us_7d_avg` |
| d | United States | Past day | Web Search | `gt_us_24h_avg` (if "not enough data", write `NED`) |
| e | United States | Past 30 days | **YouTube Search** | `gt_us_yt_30d_avg` |
| f | Worldwide | Past 30 days | Web Search | `gt_ww_30d_avg` |
| g | Pakistan | Past 30 days | Web Search | `gt_pk_30d_avg` (audience geography is unknown, so this is a hedge) |

**Comparability:** in run b, compare the term against the fixed anchor **"blood pressure"**. Trends allows up to 5 terms per comparison, so put the anchor in every batch. Record `gt_us_30d_vs_anchor` as the ratio of topic average to anchor average. Without this anchor, indices from different topics cannot be compared.

**Rising queries:** from run b, copy the top 5 "Rising" related queries into `gt_rising_queries`, separated by `;`. Write "Breakout" where Trends shows it.

## 3. YouTube (youtube.com search, browser)
For each topic, run every query in `youtube_queries`. Columns get the best query's values; the raw file gets all queries.

1. **Filters:** apply Upload date = **This month**, **This week** and **Today** in turn, with Sort = Relevance. Note: YouTube's filter UI changes, so record the labels you actually see.
2. **Top 10 results per filter:** capture video_id, title, channel, subscriber count, views, "x days ago" and duration. Save the raw data.
3. **Fill these columns:**

| Column | Label | What to put |
|---|---|---|
| `yt_month_n10k` | OBSERVED | Count of results in "This month" with ≥10K views |
| `yt_month_top_views` | OBSERVED | Top views in "This month", with its video_id |
| `yt_month_median_views_per_day` | INFERRED | Median views/day of the top 10. Use views ÷ days since upload, with "x days ago" taken as the midpoint |
| `yt_week_top_views` | OBSERVED | Top views in "This week" |
| `yt_today_top_views` | OBSERVED | Top views in "Today" |

4. **True last-24-hours views:**
   - YouTube does not show views gained in the last 24 hours, so take two snapshots. Snapshot the top 5 "This month" videos per topic (`/watch?v=` page view count) at T0, then again at T0 + 24h (±1h).
   - Write the sum of deltas to `yt_24h_delta_top5` (INFERRED).
   - If you cannot come back after 24h, write `NOT_MEASURED`. **Do not estimate.**
5. **Who wins:** fill `yt_dominant_channels` with the top 3 channel names.
   - Mark `CLONE` if a channel belongs to the template network listed in `research/senior-health-forensics/SYNTHESIS_44_channels.md` §2 (branch `origin/research/senior-health-apify-2026-11-11`): Dr. Ares Senior, Dr. Elias Senior Health, Dr. William Parker, Dr. Cale/Caleb/Kale Smith, Doctor Thomas, Dr. Franklin, Dr. Avery Senior, Healing & Health.
   - Mark `REAL-CLINICIAN` only if a verifiable named clinician is shown, such as Better Health While Aging.
6. **Competitor evidence re-check:**
   - For each id in `competitor_evidence_ids`, open the watch page and record current views in `evidence_views_now` (OBSERVED), using `id:views;…`.
   - This shows whether the topic is still collecting views.
7. **Autocomplete:** type `primary_keyword` into the YouTube search box and record the first 5 suggestions in `yt_autocomplete`.

## 4. News (Google News + official sources)
For each topic, search Google News for `primary_keyword` over **Past 7 days** and **Past month**. Also check the relevant official sites:
- AHA newsroom and ACC
- FDA recalls and safety communications
- CDC
- NIH and NEJM/JAMA for any trial named in `news_hook`

Fill these columns:
- `news_7d`: count + best headline | outlet | date | URL
- `news_30d`: same format, past month
- `news_hook_confirmed`: yes / no / partly

For **T01 (STREAM)**, also record:
- primary results at 2 years and 4 years
- the NEJM citation
- the investigators' advice

For **T10 (recalls)**, record the exact products, lots and FDA class from the FDA enforcement report or recall page.

**Copyright:** summarize in your own words; don't paste article text.

## 5. Scoring and verdict (per topic)
Compute `demand_score` (INFERRED, 0–10) from four parts:

| Part | Points | Basis |
|---|---|---|
| Trends | 0–3 | `gt_us_30d_vs_anchor` ≥0.20 = 3; 0.05–0.2 = 2; 0.01–0.05 = 1; <0.01 = 0. Add +1 if the 12-month shape is rising or the seasonal peak is now or next month, capped at 3 |
| YouTube | 0–4 | `yt_month_n10k` ≥3 = 2, 1–2 = 1. Add +1 if `yt_month_median_views_per_day` ≥500. Add +1 if the competitor evidence gained views since the snapshot |
| Competition | 0–2 | 2 if the top 3 are mostly CLONE or low-credibility (a real cardiologist differentiates); 1 if mixed; 0 if dominated by large real-clinician or major-institution channels |
| News | 0–1 | 1 if `news_hook_confirmed` = yes within 30 days |

**Verdict** (`codex_verdict`):

| Verdict | Condition |
|---|---|
| **GO** | score ≥6 |
| **ANGLE-CHANGE** | score 4–5, or demand exists but the top results own the exact angle. Propose a sharper senior/cardiologist angle in `codex_notes` |
| **SWAP** | score ≤3. Suggest the best reserve topic (T12–T20) from the same pillar |
| **DROP** | medical-claim risk you can't support with a guideline. Explain in notes |

Also fill `suggested_title` (≤70 chars, with an age marker, no "SHOCKING", "INSTANTLY" or fake percentages). Do not change medical content; Dr Rehan decides.

## 6. Deliverables
1. `docs/research/dr-rehan-content-plan-2026-11-16/03-topics-for-validation.csv`: fill the blank columns only. Do not edit the input columns.
2. `docs/research/dr-rehan-content-plan-2026-11-16/04-CODEX-VALIDATION-RESULTS.md`, in Roman Urdu, containing:
   - a ranked table of the 20 topics (score, verdict, one-line reason)
   - the revised 30-day calendar with swaps applied
   - the "rising queries" that suggest **new** topics not on the list, with a maximum of 5 and an evidence line for each
   - limits: Trends is relative, YouTube search is personalized and regional, 24h deltas measured or not
3. Raw snapshots and checksums under `data/raw/channel-data/dr-rehan-topic-validation-<date>/`.
4. **Time budget:** ~20 topics × (7 Trends runs + ~3 queries × 3 filters + news). Do the calendar topics T01–T11 first, then the reserves.
