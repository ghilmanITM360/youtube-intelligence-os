# Canonical Paths

Read this first. This is the map of where things live in this brain.

| What | Path |
|---|---|
| Source index | `SOURCE_VIDEO_INDEX.csv` |
| Source map | `SOURCE_TO_FORENSIC_MAP.csv` |
| Master data | `01_master_data/` |
| Production DNA | `02_production_dna/` |
| Reconstruction system | `03_reconstruction_system/` |
| Patterns | `04_patterns/` |
| Blueprints | `05_blueprints/` |
| Validator | `validator/validate_brain.py` |
| Release manifest + hashes | `RELEASE_MANIFEST.json` |
| Testing / generalization protocol | `testing/` |
| Legacy files | `legacy/` — never use as canonical intelligence |

## Rules

- If a file exists in both a canonical location above and `legacy/`, the canonical location wins. Always.
- `legacy/` is provenance only: superseded guides, duplicate CSVs, retired manifests. Nothing under `legacy/` is authoritative, referenced by any canonical index, or used to answer a question about current corpus state.
- Corpus statistics (word/sentence/shot/state/motion/asset/audio-event/AV-sync counts) are defined once, in `01_master_data/`, and computed fresh by `validator/validate_brain.py`. `02_production_dna/DNA_INDEX.json`, `03_reconstruction_system/RECONSTRUCTION_INDEX.json`, and `BRAIN_MANIFEST.json` must all agree with those computed values — the validator checks this and fails if they don't.
- Verify the whole brain with one command, run from anywhere (it resolves paths from its own file location, not the cwd) — just give it the right relative or absolute path to this script:

```bash
python3 "/Users/ghilmanislam360/GhilmanProjects/video data of what if/production_intelligence_brain/validator/validate_brain.py"
```
