# Source Ingestion Recommendations

Recommendations only. **Nothing described here has been performed.** No file has been copied into `data/raw/` or anywhere else in the canonical repository. These recommendations are input to Phase 1 (`docs/Phases.md`), which requires a separate, explicit, human-approved action per dataset before any copy occurs.

## Priority summary

| Discovery ID | Dataset | Priority | Why |
|---|---|---|---|
| DISC-002 | Matty Invests / Mr. Finance competitor dataset | **P0 — Critical** | Fully structured, two complete real channels, transcripts included, self-verified provenance. Highest immediate value for Phase 6 (Competitor Intelligence) once the pipeline exists. |
| DISC-001 | Forensic video reconstruction | P1 — High Value | Best available worked example of the forensic-evidence model (`docs/Database.md`), but scoped to a single unnamed video. |
| DISC-004 | Dr. Adewale competitor screenshots | P1 — High Value | Real, legible competitor evidence, but unstructured (images only) and mixes first-party (YouTube) with third-party (vidIQ) data in the same frame. |
| DISC-003 | YouTube craft/strategy corpus | P1 / P2 — High Value / Useful (split by document, see below) | Reusable Global Knowledge, but 10 of 15 documents remain uncharacterized (`docs/source-discovery/SOURCE_DISCOVERY_REPORT.md` sampling limitations) — recommend re-inspecting before assigning final priority per-document. |
| Adjacent zip archives (`files.zip`, `files (1).zip`, `files (2).zip`, `files (1)fulldata*.zip`, `all training data of youtube 2.zip`, `Dr. Adewale.zip`) | Archive duplicates of the four datasets above | **P4 — Noise/Rebuildable** | Confirmed or high-confidence exact/near-exact duplicates of already-recommended folders (`docs/source-discovery/SOURCE_DUPLICATE_REPORT.md`). No independent evidentiary value once the folder version is ingested. |
| `files` (plain folder) | Duplicate of DISC-001 | P4 — Noise/Rebuildable | Confirmed byte-identical to `files (1)`. |
| `Hook (1).pdf` vs. `Hook guide.pdf` (within DISC-003) | Possible revision pair | **HOLD — Needs Human Decision** | Not confirmed which (if either) is authoritative; ingest both with the relationship flagged rather than guessing. |

## What should be ingested first

**Recommend DISC-002 (`files (1)fulldata (1)`) as the first controlled ingestion testcase.** Reasoning:

1. It is the cleanest, most structured, most self-documented dataset found — it states its own source, scrape date, and completeness, reducing the risk of the ingestion pipeline having to guess at provenance.
2. It directly exercises the hardest parts of the planned Phase 1 workflow at once: a multi-sheet spreadsheet (`YouTube_Master_Data.xlsx`) plus a nested archive (`Transcripts_All_159_Videos.zip`) containing 160 further files organized by channel subfolder — a good stress test of the manifest/hash/dataset-detection logic in `docs/DATA_ENTRY_WORKFLOW.md` and `docs/DATA_INVENTORY.md` before those tools ever touch messier material.
3. It maps cleanly onto multiple `docs/Database.md` entities at once (`channels`, `videos`, `transcripts`) with no ambiguity about semantic class (B — Competitor Evidence) or evidence layer (`RAW_SOURCE`/`EXTRACTED_FACT`).
4. Unlike DISC-001 and DISC-004, it carries no unresolved revision ambiguity or mixed-provenance-in-one-frame problem to solve before ingestion can even begin.

## What should remain external / reference-only for now

- The 10 DISC-003 documents not yet individually read. Recommend a short follow-up read-through (not full Phase 0.5 scope re-run — just closing the sampling gap) before assigning per-document FOUNDATIONAL/HIGH VALUE/SUPPORTING/REDUNDANT/OUTDATED status, since that judgment was explicitly deferred in `docs/source-discovery/SOURCE_DATASET_INVENTORY.md`.
- The 10 `Dr. Adewale` screenshots not yet individually viewed — same reasoning; confirm they carry the same YouTube-vs-vidIQ data-mixing pattern as the 3 sampled before building an extraction prompt around that assumption.
- The source video file referenced by `FORENSIC_RECONSTRUCTION.md` (`7_Things_Wealthy_Retirees_Stopped_Buying_to_Stay_Rich.mp4`) — not present in any of the four folders; if it exists elsewhere in `~/Downloads`, it was out of scope for this task and would need its own discovery pass.

## What should be selectively copied

- DISC-001: copy `FORENSIC_RECONSTRUCTION.md` and `EDL_216_shots.csv` as the canonical pair; the two evidence JPGs as supporting visual assets. No selection needed beyond folder-level (only 4 files, all relevant).
- DISC-004: copy all 13 screenshots as-is (small dataset, no internal duplication found), but flag at ingestion time that vidIQ-derived figures within them are `OBSERVATION`, never `EXTRACTED_FACT`, per `docs/Database.md` §1.
- DISC-003: recommend ingesting per-document rather than as one bulk copy, once the follow-up read closes the sampling gap — some of the 15 may turn out redundant with each other (e.g. the possible `Renae_Creative_Engine`/`Engine-by-Engine` pairing) in ways not yet confirmed.

## What should be excluded as cache/noise

- `files` (plain folder) — exact duplicate of `files (1)`.
- `files.zip`, `files (1).zip` — exact duplicate archives of `files (1)`.
- `files (2).zip`, `files (1)fulldata.zip`, `files (1)fulldata (1).zip` — exact duplicate archives, high-confidence match to `files (1)fulldata (1)`.
- `all training data of youtube 2.zip` — high-confidence archive duplicate of `all training data of youtube`, plus `__MACOSX` resource-fork noise.
- `Dr. Adewale.zip` — high-confidence archive duplicate of `Dr. Adewale`, plus `__MACOSX` noise.

None of these should ever be deleted by this project (they belong to the user, outside repository control) — they are simply recommended as **not worth ingesting a second time** once their folder counterpart is ingested.

## What requires human review

- The `Hook (1).pdf` / `Hook guide.pdf` revision ambiguity (DISC-003) — needs either a manual content diff or the user's own knowledge of which is current.
- Whether the three Group-B zip archives (`files (2).zip`, `files (1)fulldata.zip`, `files (1)fulldata (1).zip`) genuinely match `files (1)fulldata (1)` member-for-member, or merely resemble it by name/size — recommend a member-level check before treating them as fully redundant (currently "probable," not "confirmed," per `docs/source-discovery/SOURCE_DUPLICATE_REPORT.md`).
- Authorship/rights status of DISC-003 material not originally produced by the user (e.g. the Codie Sanchez–attributed Viral Checklist) before any redistribution or reuse beyond internal reference.

## What should never be deleted

Nothing found during this discovery pass should be deleted by this project under any circumstance — the four source folders and all adjacent files are user-owned material outside repository control, and Phase 0.5's explicit boundary is discovery, not cleanup (`docs/Phases.md`, Phase 0.5 Prohibited). Even confirmed exact duplicates are left in place; "exclude from ingestion" above means "don't copy a second time," not "remove the original."

## Proposed first controlled ingestion testcase

**DISC-002, ingested as a single test case covering both its files** (`YouTube_Master_Data.xlsx` + `Transcripts_All_159_Videos.zip`), following `docs/DATA_ENTRY_WORKFLOW.md` exactly: preserve originals into `data/raw/inbox/`, inspect, inventory both files plus the 160 archive members, compute SHA-256 for all of them, determine semantic role (Class B, `RAW_SOURCE`/`EXTRACTED_FACT`), and record findings in `data/manifests/` — with no extraction, normalization, or database work performed, per Phase 1's explicit boundary (`docs/Phases.md`).

This recommendation is not an instruction to proceed. Phase 1 begins only when the user separately authorizes it.
