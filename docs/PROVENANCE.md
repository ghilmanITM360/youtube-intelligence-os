# Provenance lifecycle

Repository evidence is authoritative. Keep source facts, extracted observations and AI hypotheses distinct. See [source contract](WHAT_IF_FORENSIC_SOURCE_CONTRACT.md) and [integration lifecycle](WHAT_IF_INTEGRATION_WORKFLOW.md).

Each normalized forensic observation retains canonical `youtube_video_id`, source video ID, forensic slug, source release, source table, local row ID, CSV row number, timing, supplied confidence, source-media hash, original fields and transformation version. Portable source references resolve through the configured corpus root plus the relative MASTER table path and row fragment.

Promotion validates this chain before publishing its deterministic observation index. Query recommendations retain exact supporting row references and confidence, grouped by shared provenance without dropping rows. Production plans label recommendations EVIDENCE_BACKED_HYPOTHESIS; observations do not prove causal performance effects.

A forensic video already in the catalog remains one channel sample. Observation counts measure evidence depth, not additional independent videos. Source coverage limitations and missing confidence remain explicit.

Updating a source release or canonical identity requires reviewed regeneration, never silent mutation of historical snapshots. Follow [update workflow](UPDATE_WORKFLOW.md) and [rollback](ROLLBACK.md).
