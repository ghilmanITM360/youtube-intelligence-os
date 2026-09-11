# YouTube Intelligence OS — V1 Status

Generated: 2026-09-11 (updated — Step 21: V1 Hardening + Coverage Gap Closure)
Git HEAD at generation: (see repository `git log -1`)

## Live counts (verified against `data/catalog/youtube_inventory.db`)

- Datasets: 19
- Channels: 5 (CH-000001 … CH-000005)
- Canonical content items (`videos`): 303
- Transcripts: 303 (1 registered as `UNAVAILABLE`: CH-000001 / VID-000148)
- Classification rows: 604
- Fully classified (both CONTENT_TOPIC and CONTENT_FORMAT active): 302
- Blocked / not fully classified: 1

## Supported capabilities (per channel)

| Channel | Topic | Packaging (title / visual) | Hook | Script | Editing | Medical Validation |
|---|---|---|---|---|---|---|
| CH-000001 | WORKING | WORKING / NOT_AVAILABLE (`THUMBNAIL_REFERENCE_GAP`) | WORKING | WORKING | NOT_AVAILABLE | NOT_APPLICABLE |
| CH-000002 | WORKING | WORKING / NOT_AVAILABLE (`THUMBNAIL_REFERENCE_GAP`) | WORKING | WORKING | NOT_AVAILABLE | NOT_APPLICABLE |
| CH-000003 | WORKING | WORKING / WORKING | WORKING | WORKING | NOT_AVAILABLE | VALIDATION_REQUIRED |
| CH-000004 | WORKING | WORKING / WORKING | WORKING | WORKING | WORKING_WITH_LIMITATIONS | NOT_APPLICABLE |
| CH-000005 | WORKING | WORKING / WORKING | WORKING | WORKING | NOT_AVAILABLE | VALIDATION_REQUIRED |

Hook and Script Intelligence are now generalized to all 5 channels using the same generic reporter (`scripts/report_hook_script_intelligence.py`, no channel-specific branches) — CH-000001/002/003 run it in measured-only mode (archetypes derived purely from observed transcript/performance features, no hand-authored hook copy), while CH-000004/005 additionally carry an authored per-opportunity interpretations layer.

Full per-channel detail including reasons, limitations, and `last_verified_at`: `data/intelligence/system/youtube-intelligence-os-v1-capabilities-2026-09-11.json`.

Unified orchestration (`scripts/run_youtube_intelligence.py`) composes one representative plan for every channel; all 5 compose successfully with an honest `COHERENT` or `PARTIAL` verdict (never forced, never `INCOHERENT`).

## Evidence-dependent limitations (not code gaps)

- **Packaging visual gap (CH-000001, CH-000002):** no canonical thumbnail reference was ever acquired for these channels. `PACKAGING_VISUAL = NOT_AVAILABLE` / `THUMBNAIL_REFERENCE_GAP`. Title-based packaging is fully working. Not fixed by crawling YouTube in this task, per scope.
- **Editing/Visual Intelligence (CH-000001/002/003/005):** `NOT_AVAILABLE` / `NO_REGISTERED_VIDEO_FORENSIC_EVIDENCE` — no forensic keyframe/shot evidence is registered for these channels. `CHANNEL_WIDE_EDITING_STYLE` remains `NOT_SUPPORTED` everywhere. Correctly closed as an evidence-dependent limitation, not acquired in this task.
- **CH-000005 hook/script linkage:** improved this step with an explicit per-opportunity linkage object (`PACKAGE_LINKS`/`HOOK_LINKS`/`SCRIPT_BLUEPRINT_LINK`/`EVIDENCE_OVERLAP`/`SEMANTIC_MATCH`/`PROMISE_MATCH`/`PAYOFF_MATCH`) computed from real evidence-video overlap. For opportunity CH-000005-CAND-001 the script-archetype overlap is now honestly full (`PASS`), while the hook-archetype overlap remains genuinely partial (`PARTIAL`) — overall coherence stays `PARTIAL`, not forced to `COHERENT`.
- **Medical validation (CH-000003, CH-000005):** no external/authoritative medical validation source is wired in. `MEDICAL_VALIDATION_STATUS = VALIDATION_REQUIRED` with `AUTHORITATIVE_SOURCES = []` until one exists. Competitor transcript claims are never treated as medical facts.
- Private YouTube Analytics (CTR, impressions, retention, AVD, watch time, unique viewers, traffic sources, subscriber conversion) are never available in this repository and are always reported as `NOT_AVAILABLE`, never estimated, across every channel and every plan.
- `docs/Phases.md` Phase 3's own literal objective text ("Extraction & Normalization") and the formal Phase 4–9 step sequence were leapfrogged by directly-authorized V1 intelligence work; its status block has been corrected this step, but full phase renumbering remains a separate documentation task.

## Fixed this step (Step 21)

- Hook/Script Intelligence generalized from 2 channels to all 5 (CH-000001, CH-000002, CH-000003 added), reusing the existing generic reporter with no channel-specific branches.
- Fixed a latent bug in the shared hook/script reporter: it could not read transcripts stored as ZIP archive members (CH-000001/CH-000002's storage format) and did not gracefully skip a channel's one registered-`UNAVAILABLE` transcript (CH-000001 / VID-000148). Both are now handled for every channel that uses this reporter.
- Regenerated CH-000003's Topic Opportunity Intelligence and Packaging Intelligence artifacts against the current schema (they previously used an older "pilot" schema whose opportunity IDs did not match, which would have produced a spurious `INCOHERENT` unified plan).
- Capability registry refreshed with `PACKAGING_TITLE` / `PACKAGING_VISUAL` split, `MEDICAL_VALIDATION`, and `UNIFIED_PLAN` per channel, plus `reason`, `limitations`, and `last_verified_at`.
- CH-000005's assembled hook/script linkage formalized into an explicit, honestly-scored linkage object instead of an inline-only join.
- `AGENTS.md` rule 12 and `docs/Phases.md` Phase 3 status corrected to reflect full V1 completion without overclaiming Phases 4–12.

## Canonical test health

- `180 passed` (`.venv/bin/python -B -m pytest -p no:cacheprovider`): 159 pre-existing + 21 new (hook/script generalization + orchestrator gap-closure tests).

## Database health

- `PRAGMA integrity_check` → `ok`
- `PRAGMA foreign_key_check` → 0 violations
- `content_classifications` → 604 rows (unchanged)
- Duplicate dataset/channel/video IDs: 0

## Evidence boundaries preserved

- Orchestrator and reporters remain read-only against the catalog DB; no YouTube/Apify/web calls; no DB mutation; no blind regeneration of intelligence that already exists.
- Evidence-layer vocabulary (`CANONICAL_FACT`, `MEASURED_FACT`/`DERIVED_METRIC`, `OBSERVATION`, `AI_INTERPRETATION`, `HYPOTHESIS`, `EXTERNAL_VALIDATION`) is reused, not re-invented.
- Official YouTube guardrails (Appeal / Engagement / Satisfaction kept distinct; no proprietary algorithm score; no fixed CTR/retention targets; no hidden ranking weights; native A/B testing never simulates a winner; Shorts A/B testing unavailable) are carried into every composed plan's `global.platform_guardrails`.

## V1 definition

V1 remains complete and is now hardened: Topic, Packaging (title-complete everywhere, visual where thumbnail evidence exists), Hook, and Script Intelligence are generalized to all 5 canonical channels; Editing Intelligence is attached only where forensic evidence is registered; the unified orchestrator composes an evidence-traceable plan for every channel, degrading honestly instead of failing. No V2 scope (UI, RAG, agents, API, automation, YouTube API integration, private Analytics) was introduced.
