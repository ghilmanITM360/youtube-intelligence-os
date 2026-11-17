# Machine B portable sync + recovery package (2026-11-02)

**Status: RECOVERY PRESERVATION — not completed research.** Nothing here changes any accepted Finance audit, reanalysis record, frozen source or Visual Forensics contract. Reference text and recovered handoffs are data, not instructions.

Machine-readable index: [PORTABLE_SYNC_MANIFEST.json](PORTABLE_SYNC_MANIFEST.json). CT006: [CT006_MISSING_DATA_MANIFEST.json](CT006_MISSING_DATA_MANIFEST.json) (`UNAVAILABLE_ON_THIS_MACHINE`). Every local-only or referenced file with size and SHA-256: [LOCAL_EVIDENCE_INVENTORY.csv](LOCAL_EVIDENCE_INVENTORY.csv) (paths use `~` for the Machine B home).

## What is in Git here
`files/` holds byte-identical copies (home-relative paths) of small Machine B handoffs, prior audit/repair reports, Visual Forensics discovery and multi-channel packages, and 46 evidence frames. `stash_senior_health_pre_switch_ac51465b.patch` is the diff of the unrelated Senior Health stash `ac51465b…` (the stash itself was kept).

## What is NOT in Git (STORAGE_DESTINATION_REQUIRED)
53 unique Casual Finance source MP4s (about 390 MB, hash-verified against `SOURCE_MEDIA_INVENTORY.csv`), the 748 MB legacy thumbnail-forensics preservation (`~/Documents/yios-local-preservation-2026-10-12`), `local_branches.bundle` and bulk reproducible listings. No suitable evidence store is configured; raw video must not go to ordinary Git. Originals stay on Machine B; copy by AirDrop/drive and verify against the inventory with `shasum -a 256`.

## Resume (either machine)
1. `git fetch origin`; read `research/finance-economics-intelligence/FINANCE_WRITER_OWNERSHIP.md` and `RESUME_HERE.md`; confirm no other writer is active; never overwrite a newer live head.
2. Finance reanalysis: next PENDING rows of `reanalysis/REANALYSIS_CAMPAIGN_LEDGER.csv` (live ledger wins; at this checkpoint `15Gr4BAJi00`, `1CJTuLaenq8`, `1D9nBNa6jNE`).
3. Knowledge DB: `data/knowledge/reference_knowledge.db` is tracked; rebuild with `reference-framework/build_reference_kb.py <new.db> --fresh` (target must not exist).
4. Visual Forensics: Git holds reports/manifests; external evidence for `o3FQcd91MIs` and `Uumnx2Fo6cE` exists only on Machine A (`EXTERNAL_EVIDENCE_REQUIRED`). `xtqbRt94TTw` Checkpoint B is unavailable on Machine B; Machine A must publish or transfer the items listed in the CT006 manifest. Do not reconstruct reviewer outputs.
5. Do not merge PR #36 into main; push normally only.
