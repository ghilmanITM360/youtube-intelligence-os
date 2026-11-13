# HANDOFF PROMPT — Senior-Health data completion + research (paste this whole file into the next AI)

You are continuing work in repo `/Users/ghilmankhan/workprojects/youtube-intelligence-os`, branch `research/senior-health-apify-2026-11-11`, draft PR #50. Last pushed commit when this file was written: see `git log -1` (the commit that added this file; the one before it is `8d237c35`).

## 0. Rules you MUST follow (from the owner and the repo)
- Never merge or close the PR. Never force push. Never reset --hard / clean destructively. Never modify raw source evidence. Push only to this branch.
- Reply to the owner in **Hinglish** (Roman Hindi+English). The owner is non-technical on infra; explain simply with numbers.
- Never use cookies, logins or bypass tricks against YouTube. Do not use paid credits or upgrade Apify without asking the owner first. Residential proxy in the actor input is OK only because the owner approved it for this run; ask again if unsure.
- Keep facts, observations and AI interpretation separate (repo AGENTS.md). Preserve provenance. Do not treat AI guesses as facts.
- Git commit trailer: `Co-Authored-By: <your model name> <noreply@anthropic.com>`.
- claude-mem is broken (org disabled subscription access); it cannot save memories. Do not try to restart it. Tell the owner once.
- Max DB file size 100 MB per file (GitHub). Owner wants a "senior database engineer" structure: split files, checksums.

## 1. Goal (owner's words, translated)
Get a **complete senior-health YouTube data set** (video list, views, titles, thumbnails, descriptions, transcripts) for a merged set of **48 channels = 25 new "good views" channels + 23 channels that were already complete**. **Research starts only after this data is merged.** Extract everything possible from Apify; whatever the free account cannot reach is left for the owner's other Apify account. Push everything to GitHub continuously.

## 2. What exists (state as of 2026-11-13)
### Database
- Working DB (gitignored, local): `data/catalog/senior_health_complete.db` (tables: `channels`, `videos`, `transcripts`, `ds34_records`). Total in DB: **5,802 videos, 2,433 with transcripts**.
- Pushed split DB (all <100 MB): `data/catalog/senior_health/senior_health_core.db` (channels+videos+raw), `senior_health_transcripts_1.db`, `_2.db`, `_3.db`, `SHA256SUMS.txt`. Rebuild with `python3 scripts/build_senior_health_split.py` (asserts counts, writes checksums). GitHub warns core >50 MB; only a warning.
- `videos` columns: video_id, channel_id, url, title, published, duration_seconds, video_type, views, likes, comments, description, hashtags, keywords, thumbnail_url, has_transcript, source, sources, raw_json. `transcripts`: video_id, text, word_count, language, kind, sha256, source.
- Index/docs: `research/senior-health-master/` (README.md, MASTER_CHANNELS.csv, TRANSCRIPT_COVERAGE.csv, REMAINING_CHANNELS_NEW_GOOD_VIEWS.csv = the 25 channels, REMAINING_FOR_SECOND_APIFY_ACCOUNT.csv, APIFY_INPUT_REMAINING_LIVE.json).

### Scripts
- `scripts/import_apify_transcripts.py file.json` — imports Apify dataset JSON (success rows only, existing transcripts kept, updates has_transcript and counts).
- `scripts/build_senior_health_split.py` — rebuilds split DB + SHA256SUMS.
- `scripts/select_senior_health_apify_ids.py [max]` — prints next actor input of missing IDs for the 25 channels (60-video plan, priority order).

### Transcript plan ("60-video plan")
Per channel: if ≤60 videos take all; else **30 newest + 20 most viewed + 10 least viewed (≥90 days old)**. Full-channel transcripts for big channels were intentionally NOT pursued (cost/benefit).

## 3. The three channel groups
### 3a. The 25 NEW "good views" channels (the main target)
Defined by `research/senior-health-master/REMAINING_CHANNELS_NEW_GOOD_VIEWS.csv` (these were tier 3/4 public-metadata channels picked for good average views). Result: **1,113 videos, 753 transcripts** (all 1,113 have title/thumbnail; ~99.5% views; ~95% descriptions; **only ~36% have a published date** — gap, see §5).
| # | Channel | channel_id | Videos in DB | Transcripts | Missing live-but-failed | Missing dead |
|--:|---|---|--:|--:|--:|--:|
| 1 | Dr Thomas (Senior Health Expert) | UCKPrwcj7dscl74AeQLyqI1g | 29 | 29 | 0 | 0 |
| 2 | Dr. Aliza Wright Senior Health | UC1SDr8dfs0uED3GQIBW6edg | 0 | 0 | 0 | 0 |
| 3 | Dr. Aliza Wright / Advice  | UCXZi5JVeuTluazF-fYqQgNA | 32 | 32 | 0 | 0 |
| 4 | Dr. Ares Senior | UC356D-NzdnznBOftTpYoBLw | 39 | 39 | 0 | 0 |
| 5 | Dr. Atlas Senior Health | UC1BwGJgU9P04BDlFIsIagTQ | 19 | 17 | 2 | 0 |
| 6 | Dr. Elias Senior Health  | UCQcBYZxFW7YwNMU8-DsT3Uw | 43 | 43 | 0 | 0 |
| 7 | Dr. Franklin Senior Health | UCPjG4ZRBkiO1y_vHlnj8jIg | 46 | 9 | 0 | 37 |
| 8 | Dr. James Hargrove / Senior Health Tips | UCc3pBOuX5Y2WuQKnu12axBA | 84 | 66 | 0 | 0 |
| 9 | Healing & Health | UCwdi3NgBtFc_LfhoxQ2eB7w | 21 | 21 | 0 | 0 |
| 10 | Health Science Daily | UC_l_kwmbc2aAYB6HoBFQ8Jw | 15 | 0 | 15 | 0 |
| 11 | Healthy Aging - Senior Health Tips | UCk6fYu-O4DR1x2taFkAu_BA | 5 | 5 | 0 | 0 |
| 12 | Healthy Aging Institute with Dr. Emily Reynolds | UCZAvBGW-zGauREli-W8ULJA | 20 | 20 | 0 | 0 |
| 13 | SENIOR FOOD BLOG | UCigmuqNIp6jowy4Fhos4B5w | 79 | 60 | 0 | 0 |
| 14 | Senior Care  | UC7srybknsyI4FJZUZwJse1Q | 82 | 60 | 0 | 0 |
| 15 | Senior Health Doctor Anderson | UC2NLae1urSTqbqy-xQlfuPg | 13 | 0 | 0 | 13 |
| 16 | Senior Health Guide | UC54iH9l-ysR-s520PqjIOSA | 90 | 58 | 2 | 0 |
| 17 | Senior Health Tips Today | UCM1uK63d-bQM1Gs84zt85rw | 60 | 60 | 0 | 0 |
| 18 | Senior Health Today | UC9wj0RldADh7gV-iqv0DCOg | 33 | 0 | 0 | 33 |
| 19 | Senior Health Today | UCLxLjL1XVaKqZg-wZ2EBspA | 57 | 57 | 0 | 0 |
| 20 | Senior Kidney Care 60+ | UCelOIhQUaG1j4JBco99v-Wg | 61 | 11 | 49 | 0 |
| 21 | Senior Meal Coach | UCHOrUqhgZmEwhmXqvLwghpg | 94 | 60 | 0 | 0 |
| 22 | SeniorHood | UCoGVNMCKuxaj2F3USdjgh0Q | 83 | 63 | 0 | 0 |
| 23 | The Senior Health Hub | UC7_acN6HOq0kEv97tT-WJpA | 37 | 36 | 1 | 0 |
| 24 | Wisdom After 60 | UC5MkHMM9vnjSb0MFp4AmKgQ | 7 | 7 | 0 | 0 |
| 25 | Your Guide to Senior Kidney Wellness | UC-N9uQkNot38EpeKA271W9A | 64 | 0 | 0 | 60 |

### 3b. The 23 already-complete channels (tier 1 + tier 2 where every video has a transcript)
Result: **647 videos, 647 transcripts** — nothing to do; just include them in the research.
| # | Channel | channel_id | Videos in DB | Transcripts | Missing live-but-failed | Missing dead |
|--:|---|---|--:|--:|--:|--:|
| 1 | Ansel Senior Health | UCX_263NGp5srFTs-HfgWdSw | 32 | 32 | 0 | 0 |
| 2 | Better Health While Aging | UCFpxvukIqCAUA7YizI-q9Dw | 98 | 98 | 0 | 0 |
| 3 | DR HENRY JASON | UC-a-yheeRqTvbKMt7UDivfA | 6 | 6 | 0 | 0 |
| 4 | DR.MICHAEL SMITH | UCWRwyjjX2Kwry0jdqqEja_w | 8 | 8 | 0 | 0 |
| 5 | Decode Your Heart – Dr. Rehan | UCQIzqH7QZ9viBYpOFqgSXMg | 56 | 56 | 0 | 0 |
| 6 | Dr. Aliza Wright / Advice  | UCXZi5JVeuTluazF-fYqQgNA | 32 | 32 | 0 | 0 |
| 7 | Dr. Ares Senior | UC356D-NzdnznBOftTpYoBLw | 39 | 39 | 0 | 0 |
| 8 | Dr. Avery Senior | UC9qTnpiqpVWSXeHmL1_Dykw | 43 | 43 | 0 | 0 |
| 9 | Dr. Cale Smith | UCsPba6Pqq_cp37zyU6MP82g | 17 | 17 | 0 | 0 |
| 10 | Dr. Caleb Smith | UCcU-11Q0ZU2wz1qY2MbKGuA | 8 | 8 | 0 | 0 |
| 11 | Dr. Daniel Parker | UCsOXJjVo8dV3QF0MTbaBC_w | 8 | 8 | 0 | 0 |
| 12 | Dr. Edward Mitchell | UCtdjBmg3xjAMFkE_m677pFg | 11 | 11 | 0 | 0 |
| 13 | Dr. Elias Senior Health  | UCQcBYZxFW7YwNMU8-DsT3Uw | 43 | 43 | 0 | 0 |
| 14 | Dr. Lawson Health | UCKMngg0B8dVEKgY4xkZSYMw | 27 | 27 | 0 | 0 |
| 15 | Dr. Micheal Adeyemi | UCKn8eHaQNQbh-yKHicDiKow | 40 | 40 | 0 | 0 |
| 16 | Dr. Oakheart Longevity | UCjBoB0OlO_IEOElE5XMMgTA | 15 | 15 | 0 | 0 |
| 17 | Dr. Okoro | UCMJxAeBJ0d1JC937de1eZ0Q | 66 | 66 | 0 | 0 |
| 18 | Dr. Varexon Senior | UCqn57ZAz-ref74As-aUwlxQ | 17 | 17 | 0 | 0 |
| 19 | Dr. kale Smith | UCiGa-LVm3Omf8Qx1XTVs4rA | 19 | 19 | 0 | 0 |
| 20 | Healing & Health | UCwdi3NgBtFc_LfhoxQ2eB7w | 21 | 21 | 0 | 0 |
| 21 | Longevity Decoded | UCIVloPYGeHvpVqT_mkSyq9g | 16 | 16 | 0 | 0 |
| 22 | Metabolic Unlocked | UCtRL3C1RK-ljNJIyDTA4KaA | 12 | 12 | 0 | 0 |
| 23 | Vital Years Project | UCwuXzD8hg_kGwP0HHHwQruQ | 13 | 13 | 0 | 0 |

### 3c. The 6 near-complete tier 1/2 channels (not in the 23, not in the 25)
336 videos, 310 transcripts. Gaps are small/unfixable (dead videos or the 60-video plan cap).
| # | Channel | channel_id | Videos in DB | Transcripts | Missing live-but-failed | Missing dead |
|--:|---|---|--:|--:|--:|--:|
| 1 | Doctor Thomas | UCFuGMi0idGeyXl6wYK9hg7Q | 22 | 21 | 0 | 0 |
| 2 | Dr. Vitalis | UCLxJ_nQg42P-0XNRdGwA2gg | 27 | 26 | 0 | 0 |
| 3 | Dr. Waterling | UCLVvBoFiBC6oj7mT62GFAEA | 71 | 60 | 0 | 0 |
| 4 | PrimeWellness | UCrz5nlYL41KJS21ef9ey3JA | 22 | 21 | 0 | 0 |
| 5 | Senior Health Hub | UCAYG0fzUyxv6OevH88qA45w | 124 | 122 | 0 | 0 |
| 6 | Vital Years Wellness | UCLokQKT7DqcO756ACKyomUQ | 70 | 60 | 0 | 0 |

(Other channels in the DB — tier 3 rest, tier 4 identity-only ~75 — were NOT part of this task; they have partial/no transcripts and are out of scope unless the owner asks.)

## 4. What happened, in order (all done and pushed)
1. Built `senior_health_complete.db` (159 channels, 5,370 videos at start, 459 transcripts) → split DB.
2. Free Apify account ($5 plan) with actor `srd836/youtube-transcript-pro` (R6WMSrMpTdFSsYEo8, **$0.005 per delivered transcript, failures free**): runs plGekyopZRj2rzQhI (+307), 8LIogmlj1NrUohbPJ (+73), F35KcnFwDBctRSuLP (+3, 41 failed).
3. Owner switched to a second Apify account ($10 plan): run d3RHge2CxREQFZrfP failed 100% (no proxy → "IP block"), aborted, free; run **uR1ZcpdcJ3rYAskrK** with `proxyConfiguration` residential: **+94 transcripts, 69 failed ($0.47)**. Commit `8d237c35`.
4. Old yt-dlp caption backfill (channels 49–151) is **on hold** because of YouTube IP 429 — do not resume with cookies/bypass.

## 5. What is left (honest list)
1. **212 videos missing in the 60-video plan**: 143 dead (oEmbed 404 / removed) + 69 "video unavailable/private" on both accounts. The actor cannot get them. Optional: retry the 69 later (maybe temporary); do not expect much.
2. **Published dates**: only 405/1,113 videos of the 25 channels have `published`. Some channels (e.g. Dr. Franklin Senior Health, Senior Meal Coach) are fully empty. Investigate source (`raw_json`, DS-000034 vs Apify) and fill where a legitimate source exists; otherwise document the gap. This also weakens the "30 newest" selection logic.
3. Terminated channel: Dr. Aliza Wright Senior Health (UC1SDr8dfs0uED3GQIBW6edg) — gone, keep what we have.
4. Tier 3 (rest) and tier 4 channels need a paid Apify metadata run (~$18 for ~4,500 videos) — only if the owner asks.
5. Second Apify account has about $5.1 of $10 free usage left (usage was $4.88/$10 after the last run). Actor input must include: `{"includeMetadata":true,"language":"en","videoUrls":[ids],"proxyConfiguration":{"useApifyProxy":true,"apifyProxyGroups":["RESIDENTIAL"]}}`.

## 6. How to run the actor via browser (what worked)
- Open `https://console.apify.com/actors/R6WMSrMpTdFSsYEo8/input` → JSON tab → set Monaco value via JS: `monaco.editor.getModels().find(m=>m.getValue().length>100).setValue(JSON.stringify(obj))` (typing JSON by hand adds stray brackets) → click Save & start (the owner may need to click it themselves if the permission classifier blocks the start).
- Speed ≈ 3–8 s per video; 163 videos ≈ 20 min. Don't use `get_page_text` on the output (≈1 MB); use `javascript_tool`.
- Export: Export → JSON, All fields → Download to ~/Downloads, then `python3 scripts/import_apify_transcripts.py <file>`, rebuild split DB, update README/CSV, commit, push.

## 7. NEXT STEPS for you (in order)
1. `git pull`/check status, read `research/senior-health-master/README.md`, open the DB and verify the counts in §3 (they came from the DB at write time).
2. Ask the owner ONE question: which research angle first for the 48 channels (e.g., top-viewed topics, title/thumbnail patterns, hook/script patterns, transcripts content, competitor blueprint for a new senior-health channel). Do not start research before the owner picks.
3. Optionally (if the owner agrees) look at the published-date gap (§5.2) first — it affects every time-based analysis.
4. Do the research from the DB only (no model memory as source of truth), writing results under `research/senior-health-master/` or a new `research/senior-health-research/` folder, with provenance (video_id/channel_id references).
5. Commit and push regularly; report to the owner in Hinglish with real numbers.

## 8. Definition of "48-channel research set"
`{25 channels in §3a} ∪ {23 channels in §3b}` = 48 channels; videos = 1,760; transcripts = 1,400.
