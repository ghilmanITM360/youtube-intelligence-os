# Research Limitations & Missing-Evidence Ledger — 2026-10-26

## 1. Missing private metrics (all `NOT_AVAILABLE`, never inferred)

Basis: `youtube_channel_registry.db.channels.first_party_analytics_status` = `SCHEMA_READY_NO_DATA` for 75/75 channels. Ledger `private_metrics` = {CTR, impressions, retention, revenue, traffic_sources} unavailable.

| Metric | Status | Why it matters (official) | What would provide it |
|---|---|---|---|
| Impressions | NOT_AVAILABLE | Exposure denominator; CTR falls as impressions grow (S7) | Owned-channel Studio export |
| Impressions CTR | NOT_AVAILABLE | Appeal among those shown (S3, S7) | Studio |
| Audience retention curve / first 30 s / relative retention | NOT_AVAILABLE | Engagement; "first seconds" decide stay or leave (S3) | Studio |
| Average view duration / average % viewed | NOT_AVAILABLE | Named ranking inputs (S4) | Studio |
| Shorts stayed-to-watch | NOT_AVAILABLE | Shorts appeal (S8) | Studio |
| Traffic sources (Browse / Suggested / Search / Shorts feed / External / Notifications / Playlists) | NOT_AVAILABLE | Surfaces weight signals differently (S2) | Studio |
| New vs returning / unique viewers | NOT_AVAILABLE | Audience expansion vs loyalty | Studio |
| Geography / device | NOT_AVAILABLE | Context of personalization (S1) | Studio |
| Satisfaction surveys | NOT_AVAILABLE to anyone outside YouTube | Core objective (S1, S10) | Not exposed to creators |
| Thumbnail/title A/B results | NOT_AVAILABLE | Watch-time-share causal test (S9) | Owned channel |
| Subscribers gained per video | NOT_AVAILABLE | — | Studio |
| RPM / revenue / costs / profit | NOT_AVAILABLE | Business viability, not ranking | Studio + own accounting |
| Upload-era title/thumbnail versions | NOT_AVAILABLE. Every thumbnail record says `historical_design: UNKNOWN` | Packaging attribution | Version logging going forward (Roadmap E0) |
| Recommendation candidates / ranking scores | NOT_AVAILABLE to anyone outside YouTube | — | None. Do not seek |

Questions that **require** an authorized owned-channel export:
- Which surface drives a video?
- Is a video plateauing because CTR or retention falls as impressions widen?
- Do our openings lose people in the first 30 s?
- Does a title test win on watch time?
- Do Shorts bridge to long-form?

**Unauthorized access to competitor Studio data is not sought and must not be.**

## 2. Limitations of the public proxies we do have

1. **Lifetime views/day is a lifetime average, not velocity.** Lifetime views scale with age at a median slope of 0.34 (Finance) and 0.57 (all niches), far below 1. Peer age-matching reduces but does not remove this.
2. **Snapshot dates are approximate.** DS-000022 uses a source-declared scrape *day* (timezone unknown). DS-000020/21/23/24 use packaging dates. DS-000001 (159 videos) is undated and excluded from ratios. The registry analysis uses manifest collection or ingestion dates; ingestion is an upper bound.
3. **Peer thresholds (2× / 0.5×) are analyst choices**, not YouTube categories (METHODS.md).
4. **Channel dominance:** Nick Invests = 348/723 rated originals.
5. **Selection of channels:** competitor sets were supplied by the user or chosen as successful exemplars. They are not a random sample of Finance YouTube, so survivorship bias applies.
6. **Hit-heavy forensic sample:** the What If decodes include the channel's largest videos. Visual Forensics has n=2 (one breakout, one typical).
7. **Transcripts** are auto-generated, untimed, audio-unverified text. There are no seconds-level hook or pacing measures. 12 registry transcripts are placeholders.
8. **Outcome-aware analyst prose:** deep-audit text cites tiers, so features coded from it are contaminated. Only mechanical features were used for primary tests.
9. **Heuristic labels:** `Time_sensitivity` is `UNVERIFIED` for all 966. Topic tags are keyword heuristics (936/966). "Evergreen vs timely" is therefore only crudely testable (H10, inconclusive).
10. **Multiple testing:** 14 primary tests BH-corrected. Exploratory families (14 tests) are BH-corrected separately and are not decision-grade.
11. **Shorts vs long-form views** are not comparable units.
12. **Like-rate** shares the views denominator with the outcome, so it is partly mechanical.
13. **Landscape set (180)** has display-rounded views and relative dates and was excluded from tests.
14. **Concept matching across channels** (§8 of the tests report) was done by reading titles. It is illustrative and was not systematically searched.

## 3. Inaccessible or unverified sources in this environment

| Source | Status |
|---|---|
| Visual Forensics Video 003 checkpoint 6 | Not found in any local ref or commit message. Presumed Machine A-only |
| Machine A external evidence roots (`/Users/ghilmankhan/YIOS-local-audits/…`) | Not on this machine |
| Casually Finance source MP4s on Machine B | `machine_B_availability: UNVERIFIED` per manifest. Not checked (no media decoding) |
| PR #44 What If package | Read via `git show` from the remote-tracking ref; **unmerged**. Not assumed to be in `main` |
| `research/casually-finance-success-playbook` | Branch-only. Read via `git show` |
| `data/raw/` (850 MB) | Deliberately not read (AGENTS.md rule 4; graphify rule) |
| XLSX workbooks | Hash-inventoried only; their projections were validated by the Finance writer's own checks |
| Official Shorts "Viewed vs swiped away" / "engaged views" Help text | Not retrieved from a primary page today; only third-party descriptions found |
| Current YouTube five-hour/weekly usage meter | Could not be read from this environment. **Not verified** (no number is invented) |

## 4. Historical staleness

- The registry was last written 2026-10-13. Competitor snapshots are 2026-08-31 → 10-21. All views are frozen and **not current**.
- `FINANCE_UNIVERSE.csv.audit_status` is frozen at 430 complete; the live ledger has 449.
- YouTube Help pages carry no revision dates. Re-check them before relying on them after this date.
- The 2016, 2019 and 2024 research papers describe systems at those times.

## 5. Integrity notes found during the census (not repaired — read-only audit)

- 2 zero-byte `.db` files in `data/catalog/`.
- `expansion-12-channel-2026-10-20/FILE_CHECKSUMS_SHA256.json` → `README.md` hash mismatch (README edited later by `1ac2d370`). Data files match.
- Registry `video_type` uses five inconsistent labels; 771 `published_at` values are not ISO datetimes.
- Inventory DB `video_snapshots` has 668 rows for 667 videos (one double snapshot).

## 6. Resource & safety checkpoint record

| Gate | Observation |
|---|---|
| Five-hour / weekly usage | **Not verifiable** from this environment (no meter access). Not assumed |
| Context / compaction | No compaction warning during the run |
| Disk | 926 GiB volume, **19 GiB free** at start. The audit output is a few MB |
| RAM | 32 GiB physical. Analyses are streaming/stdlib; peak use small |
| Paid credits | None used. No Apify, scraping, downloads, cloud or API calls. Web reads limited to public Google/YouTube/arXiv pages |
| Git | Branch `research/finance-economics-intelligence` @ `d987510b`, clean before and after. No checkout, fetch, pull, stash, commit, reset or worktree |
| Ownership | Other Claude/Codex processes present. This audit wrote nothing to the repository, so there was no interference with the Finance writer (next item `UmKdQCMCc98` untouched) or Visual Forensics |
| Output location | Single external directory `/Users/ghilmanislam360/Documents/YIOS-Algorithm-Audit-2026-10-26/` |
