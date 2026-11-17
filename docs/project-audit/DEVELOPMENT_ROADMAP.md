# Development Roadmap — 2026-11-11

Priorities respect AGENTS.md: V2 (UI/RAG/agents/API/automation/YouTube API) does not start automatically.

| Pri | Item | Benefit | Depends on | Effort | Validation |
|---|---|---|---|---|---|
| P0 | Owner decision: push audit merge commit `2b6ccea5` / commit audit edits (Finance writer-protocol applies) | Local = remote | owner | XS | `git status`, CI green |
| P0 | Enforce Finance reference gates in CI (merge PR #45 or add steps) — D1 | Accepted audits cannot silently regress | PR #45 review | S | CI red when annex removed |
| P1 | Decide privacy of tracked audio/frames/derived analytics (S5/S6) | Reduces leak risk of a 5.4 GB private history | owner | M | `docs/DATA_PRIVACY.md` closed items |
| P1 | Declare or retire `python-docx` use (D2) | Clean-install reproducibility | — | S | fresh venv |
| P1 | Triage the 20+ draft PRs: merge, close, or consolidate | Cuts divergence (research branch 210 commits ahead of main) | owner | M | open PR count |
| P1 | Real first-party YouTube Analytics export ingestion | Turns diagnostics from READY into real | owner data | M | diagnosis report from real data |
| P2 | Add CVE scan (`pip-audit`) + Dependabot to CI (S7) | Supply-chain visibility | — | S | CI step |
| P2 | Retry/backoff for Apify GETs; transactional ID allocation (D4, D5) | Reliability | — | S | mock tests |
| P2 | Smoke tests for the 17 untested builders (D7) | Regression safety | — | M | coverage report |
| P2 | Stop hash-pinning repo-owned code or document the re-pin step (D3) | Contributor ergonomics | owner | M | doc/test |
| P2 | Clean `reference_knowledge.db` schema (D6); refresh `PROJECT_STATUS.md` (D16) | Clarity | — | S | table list |
| P3 | Expand niches/channels per niche to reach `ROBUST_CROSS_NICHE_PATTERN` | Evidence strength | supplied data | L | calibration artifact |
| P3 | Pillow 14 readiness (D10); remove Node from CI (D13) | Hygiene | — | S | CI |
| P3 | V2 (UI first, per `ui/v1`) only after explicit authorization | Product | owner | XL | — |
