# YouTube Intelligence OS — V1 Status

Generated: 2026-09-11
Git HEAD at generation: (see repository `git log -1`, commit "system: add unified YouTube intelligence orchestration")

## Live counts (verified against `data/catalog/youtube_inventory.db`)

- Datasets: 19
- Channels: 5 (CH-000001 … CH-000005)
- Canonical content items (`videos`): 303
- Transcripts: 303
- Classification rows: 604
- Fully classified (both CONTENT_TOPIC and CONTENT_FORMAT active): 302
- Blocked / not fully classified: 1

## Supported capabilities

| Layer | Status |
|---|---|
| Foundation (ingestion, provenance, immutability) | CLOSED |
| Classification | WORKING |
| Topic Opportunity Intelligence | WORKING (CH-000001, CH-000002, CH-000003, CH-000004, CH-000005) |
| Packaging Intelligence | WORKING (all 5 channels) |
| Hook / Script Intelligence | WORKING (CH-000004, CH-000005 only) |
| Editing / Visual Intelligence | WORKING_WITH_FORENSIC_EVIDENCE (CH-000004 only) |
| Unified orchestration (`scripts/run_youtube_intelligence.py`) | WORKING — composes existing layers, degrades gracefully when Editing is unavailable |

Full per-channel detail: `data/intelligence/system/youtube-intelligence-os-v1-capabilities-2026-09-11.json`.

## Known limitations

- Hook/Script Intelligence has not been generalized to CH-000001, CH-000002, or CH-000003.
- Editing/Visual Intelligence exists only for CH-000004, and only where forensic keyframe/shot evidence is registered; `CHANNEL_WIDE_EDITING_STYLE` remains `NOT_SUPPORTED` everywhere.
- For channels without an authored per-opportunity hook/script blueprint (e.g. CH-000005), the orchestrator links channel-wide hook/script archetypes to an opportunity by evidence-video overlap; this is disclosed as a `PARTIAL` coherence dimension, not hidden as a full match.
- No external/authoritative medical validation source is wired in; health-channel opportunities are flagged `medical_validation_required` until one exists.
- Private YouTube Analytics (CTR, impressions, retention, AVD, watch time, unique viewers, traffic sources, subscriber conversion) are never available in this repository and are always reported as `NOT_AVAILABLE`, never estimated.
- `docs/Phases.md` and `AGENTS.md` rule 12 phase bookkeeping lag actual repository state (see `docs/PROJECT_SCOPE.md` note added 2026-09-11); reconciling the full phase roadmap is out of scope for this task.

## Canonical test health

- `159 passed` (`.venv/bin/python -B -m pytest -p no:cacheprovider`): 139 pre-existing + 20 new orchestrator tests.

## Database health

- `PRAGMA integrity_check` → `ok`
- `PRAGMA foreign_key_check` → 0 violations
- Duplicate dataset IDs: 0
- Duplicate channel IDs: 0
- Duplicate video IDs: 0
- Conflicting active classifications: 0

## Evidence boundaries preserved

- Orchestrator is read-only against the catalog DB; it never mutates it, never calls YouTube/Apify/the web, and never regenerates intelligence artifacts that already exist.
- Evidence-layer vocabulary (`CANONICAL_FACT`, `MEASURED_FACT`/`DERIVED_METRIC`, `OBSERVATION`, `AI_INTERPRETATION`, `HYPOTHESIS`, `EXTERNAL_VALIDATION`) is reused from existing artifacts, not re-invented.
- Official YouTube guardrails (Appeal / Engagement / Satisfaction kept distinct; no proprietary algorithm score; no fixed CTR/retention targets; no hidden ranking weights) are carried into every composed plan's `global.platform_guardrails`.

## V1 definition

V1 is complete: the OS ingests/registers canonical evidence, classifies it, derives Topic/Packaging/Hook/Script intelligence, attaches Editing intelligence where forensic evidence exists, degrades safely where it does not, and composes an evidence-traceable unified plan via `scripts/run_youtube_intelligence.py` — all guardrails preserved, all tests passing, DB clean.
