# 03 · Script library

| Folder | Contents | Status |
|---|---|---|
| `approved/` | [README](approved/README.md): where each **approved / recorded** narration lives | Pointers. The recordings stay inside each production |
| `working-drafts/` | Empty locally. The current V3 working drafts for Slots 03–10 are in the GitHub repo (`productions/unreasonably-exact-script-rewrite-v3/revised_scripts_v3/`) | |
| `historical/` | V1 script texts, V2 revised scripts, V1/V2 voiceover DOCX, Slot 01 alternative, Slot 02 transcript and provenance audit | Superseded; kept for history (moved here 2026-11-26, see `../MIGRATION_MANIFEST.csv`) |
| `build-tools/` | Python that built the DOCX script packages, plus the 2026-11-25 verified pass | `build_docx.py` output path updated to `historical/` |

**Rule.** A production script must also pass the repo's AI-slop gate (`scripts/check_slop_risk.py`) before delivery. See repo `AGENTS.md`.
