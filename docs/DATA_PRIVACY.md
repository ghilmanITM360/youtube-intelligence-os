# Data privacy and raw evidence

Current governance is documented in [Security](Security.md), the [What If privacy policy](WHAT_IF_INTEGRATION_WORKFLOW.md#privacy-and-raw-media-policy), and the [per-file safety review](audits/WHAT_IF_REPOSITORY_SAFETY_2026-10-09.md).

What If raw MP4s, audio, frames, duplicated release packages and temporary query payloads stay outside Git. Generated staging is ignored. Reviewed contracts, checksums, code, tests, documentation and derived production summaries with provenance may be committed. Raw Studio exports and new private-derived analytics remain ignored/local-only. Never commit credential values.

Historical findings use these operational classifications:

- Seven audio files: NEEDS_OWNER_DECISION for relocation; PRIVATE_LOCAL_ONLY is the intended future storage rule. Preserve current tracked evidence until an immutable archive and catalog reference migration are verified.
- 251 indexed shot frames: KEEP_TRACKED as required historical evidence. MOVE_TO_LFS is an optional separate migration, requiring reference/hash validation.
- Five derived-private analytics files: NEEDS_OWNER_DECISION, currently retained under KEEP_PRIVATE_REPO_ONLY governance. Before broader sharing, choose sanitization or PRIVATE_LOCAL_ONLY migration and removal from the current tree.

No current policy authorizes destroying required evidence to reduce repository size. Removing a current-tree file does not remove earlier commits. Any history purge requires explicit owner authorization. The existing per-file review lists every affected path; its historical classification labels are preserved.
