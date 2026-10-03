# Decode Your Heart (DS-000032) privacy classification — 2026-10-03

Status: verified against the repository and `origin` on 2026-10-03. Repository `ghilmanITM360/youtube-intelligence-os` is **PRIVATE** with a single collaborator.

## Classes

| Class | Meaning | Where it lives | Git state |
|---|---|---|---|
| RAW_PRIVATE_STUDIO | Unmodified YouTube Studio exports (69 ZIPs: 60 audience-retention, 4 content, 3 traffic-source, 1 device, 1 geography) and the extracted copy under `data/raw/first-party/youtube-studio/` (70 files) | `~/Downloads` (ZIPs), repo checkout `data/raw/first-party/` (ignored by `data/raw/**/*`), independent backup `~/Documents/yios-private-backups/studio-exports-2026-10-03/` | Never committed. Ignored/local-only. Not on any remote. |
| DERIVED_PRIVATE_ANALYTICS | Measurements computed from raw Studio data (impressions, CTR, retention, audience, traffic, per-video metrics) | The five tracked files below | **Tracked and pushed** to private origin branch `research/senior-health-acquisition-phase-2` |
| PUBLIC_SAFE_RESEARCH | Public metadata, transcripts, public thumbnails, medical-claim reviews, code | DS-000032 package, scripts, tests | Tracked and pushed |

## The five tracked files carrying DERIVED_PRIVATE_ANALYTICS

1. `docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Video_Evidence_Register.json` (heaviest: per-video retention and CTR)
2. `docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Research_Checkpoint.json`
3. `docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Analytical_Workbook.xlsx` (sheets Own-Channel Analytics, Script & Retention, Long-form CTR vs Retention, others)
4. `docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Forensic_Report.docx`
5. `docs/research/decode-your-heart-2026-09-27/HANDOFF-2026-09-28.md` (summary mentions)

`Decode_Your_Heart_Local_Video_Asset_Inventory.json` contains no Studio metrics.

## Corrected stale claims

- `Research_Checkpoint.json` and its builder `scripts/build_decode_your_heart_recovery.py` said `remote_push_performed: false`. The five files were in fact pushed (origin `research/senior-health-acquisition-phase-2` = 373bf37). Now `true`, with a note.
- `HANDOFF-2026-09-28.md` said "local-only, do not push". Prefixed with a dated correction; original text kept.

## Recommendation

**KEEP_PRIVATE_REPO_ONLY** now, plus **SANITIZE_FUTURE_COMMITS**.

- Repo is private with one collaborator, so the pushed derived metrics are not publicly exposed. No history rewrite is recommended. `HISTORY_REWRITE_REQUIRED` would apply only if the repository is ever made public, forked, or shared with other collaborators.
- Before any visibility change or sharing: move the five files to an ignored path (`REMOVE_FROM_TRACKED_ARTIFACTS`) and rewrite history only with explicit owner authorization.
- Going forward: keep derived Studio output under ignored `data/intelligence/first-party/` (already ignored by `.gitignore`), and commit only public-safe findings.
- Not done in this pass (owner decision): moving/removing the five files, rewriting history, changing repo visibility.
