# Security and Performance — 2026-11-11

Scope: static review + safe local runs. No intrusive testing, no live systems touched, no secret values displayed.

## Security
| # | Sev | Finding | Evidence |
|---|---|---|---|
| S1 | Positive | Tracked-secret scan clean | `scan_tracked_secrets.py` -> 0 findings; `.gitignore` excludes `.env*`, `*.pem`, `*.key` |
| S2 | Positive | Apify token read from env, sent as `Authorization: Bearer` header (not in URL), `https://api.apify.com` only, 90 s timeout, spend cap param | `scripts/apify_youtube_ingest.py` `ApifyHttp` |
| S3 | Positive | SQL uses `?` binding; f-string SQL builds only placeholder lists or fixed table names (26 ruff S608 hits reviewed as false positives) | `run_youtube_intelligence.py:131,420`; `build_reference_kb.py:19` |
| S4 | Positive | No `shell=True`, `os.system`, `pickle.load` in repo tooling; `subprocess` used only with arg lists in `production_pipeline.py` (ffprobe) | grep |
| S5 | Medium | Private/derived evidence is tracked in git history: 4 WAV audio files (`data/raw/forensic-analysis/DS-000013..16/**/audio*.wav`, >65 MB for three of the four), What If frames, five derived-private analytics files; repo is **private** (gh), but `docs/DATA_PRIVACY.md:9-11` marks them `NEEDS_OWNER_DECISION` | `gh repo view` PRIVATE; `git ls-files` |
| S6 | Medium | Repo is 5.4 GB `.git` with raw data tracked; any visibility change or new collaborator exposes all history | `du`, `git count-objects` |
| S7 | Medium | No dependency CVE scan in CI; only `pyproject` ranges and `uv.lock` | validate.yml |
| S8 | Low | Prompt-injection: reference text and transcripts are treated as data per AGENTS.md; there is **no LLM call in the shipped code** (grep: only offline research scripts/Whisper), so runtime exposure is nil today | grep |
| S9 | Low | No authn/authz, no network service, no API: nothing to attack remotely. Local file permissions: ignored DB files `-rw-------` | ls |
| S10 | Info | CI uses read-only `contents: read` token | validate.yml |

## Performance and reliability (measured vs theoretical)
- **Measured**: full pytest 37.7–43.9 s (462 tests); `PRAGMA integrity_check` on 141 MB registry DB and 52 MB inventory DB completes interactively.
- **Theoretical**: `IN (?,?,…)` lists in `run_youtube_intelligence.py:131,420` are bounded by channel video counts (hundreds–low thousands) — safe under modern SQLite's 32,766 limit; `next_id` scans a whole table per allocation (`register_supplied_channel.py:~21`) — O(n) per insert, fine at current sizes (≤45,774 rows).
- Registry DB (141 MB) is Git LFS: clean clones need `git lfs pull` or CI/bootstrap steps silently fail on a pointer file.
- No scheduler, queue, cache or background worker exists. Apify calls are manual, bounded by `maxTotalChargeUsd`; no retry (D5). API quota: YouTube API intentionally unused (AGENTS.md rule 13).
- Single points of failure: single-writer SQLite files committed to git; one machine at a time writes Finance (ownership protocol).
- Estimated operating cost: 0 USD/month for the codebase itself (no LLM/API calls); Apify cost is per-run, recorded in `apify_run_cost_observations` (10 rows).
