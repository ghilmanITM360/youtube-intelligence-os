"""Declarative logical-dataset / disposition rules for BATCH-000001
(Phase 1C). Built from direct inspection of the 12 source roots (recursive
`find`, `du`, and reading the primary evidence — `FORENSIC_RECONSTRUCTION.md`,
the existing `CODEX_PROJECT_INDEX.md` / `DATASET_INVENTORY.md` audit, spot
re-verified against the live filesystem) — not guessed from folder names.

Each ROOT_SPEC describes one of the 12 authorized source roots. `kind`:
  - "already_ingested": every file must hash-match an existing DS-000001
    source_files record; disposition is ALREADY_INGESTED if so, else the
    run must stop (RevisionDetected).
  - "flat_dataset": no interesting subdirectory structure — every regular
    file disposition INGEST into one dataset; directories themselves are
    recorded with disposition NOISE (structural, not evidence).
  - "codex": Documents/Codex — many logical datasets, resolved by CODEX_RULES
    below (longest relative-path-prefix match wins).

dataset_key is a stable symbolic name; scripts/register_batch.py allocates
the real DS-00000X id once, in REGISTRATION_ORDER, and copy_mode controls
whether canonical bytes are copied into data/raw/ or left as REFERENCE_ONLY
pointers to the original (large, frame-heavy) location.
"""

ROOT_SPECS = [
    {
        "index": 1,
        "path": "/Users/ghilmanislam360/Downloads/files (1)fulldata (1)",
        "kind": "already_ingested",
        "dataset_key": None,
        "existing_dataset_id": "DS-000001",
    },
    {
        "index": 2,
        "path": "/Users/ghilmanislam360/Downloads/files (1)",
        "kind": "flat_dataset",
        "dataset_key": "ROOT2_FORENSIC_RETIREES",
        "dataset_name": "\"7 Things Wealthy Retirees Stopped Buying to Stay Rich\" — Forensic Video Reconstruction",
        "semantic_class": "C",
        "content_domain": "FINANCE",
        "copy_mode": "COPY",
    },
    {
        "index": 3,
        "path": "/Users/ghilmanislam360/Downloads/Doctor Thomas",
        "kind": "flat_dataset",
        "dataset_key": "DOCTOR_THOMAS",
        "dataset_name": "Doctor Thomas — Competitor Channel Screenshots",
        "semantic_class": "B",
        "content_domain": "HEALTH",
        "copy_mode": "COPY",
    },
    {
        "index": 4,
        "path": "/Users/ghilmanislam360/Downloads/Dr. Adewale",
        "kind": "flat_dataset",
        "dataset_key": "DR_ADEWALE",
        "dataset_name": "Dr. Adewale — Competitor Channel Screenshots",
        "semantic_class": "B",
        "content_domain": "HEALTH",
        "copy_mode": "COPY",
    },
    {
        "index": 5,
        "path": "/Users/ghilmanislam360/Downloads/Dr. Okoro(2)",
        "kind": "flat_dataset",
        "dataset_key": "DR_OKORO",
        "dataset_name": "Dr. Okoro — Competitor Channel Screenshots",
        "semantic_class": "B",
        "content_domain": "HEALTH",
        "copy_mode": "COPY",
    },
    {
        "index": 6,
        "path": "/Users/ghilmanislam360/Downloads/Dr. Aliza Wright _ Advice (2)",
        "kind": "flat_dataset",
        "dataset_key": "DR_ALIZA_WRIGHT",
        "dataset_name": "Dr. Aliza Wright / Advice — Competitor Channel Screenshots",
        "semantic_class": "B",
        "content_domain": "HEALTH",
        "copy_mode": "COPY",
    },
    {
        "index": 7,
        "path": "/Users/ghilmanislam360/Downloads/Dr. Waterling(2)",
        "kind": "flat_dataset",
        "dataset_key": "DR_WATERLING",
        "dataset_name": "Dr. Waterling — Competitor Channel Screenshots",
        "semantic_class": "B",
        "content_domain": "HEALTH",
        "copy_mode": "COPY",
    },
    {
        "index": 8,
        "path": "/Users/ghilmanislam360/Downloads/The Senior Health Podcast(2)",
        "kind": "flat_dataset",
        "dataset_key": "SENIOR_HEALTH_PODCAST",
        "dataset_name": "The Senior Health Podcast — Competitor Channel Screenshots",
        "semantic_class": "B",
        "content_domain": "HEALTH",
        "copy_mode": "COPY",
    },
    {
        "index": 9,
        "path": "/Users/ghilmanislam360/Downloads/Senior Health Hub(2)",
        "kind": "flat_dataset",
        "dataset_key": "SENIOR_HEALTH_HUB",
        "dataset_name": "Senior Health Hub — Competitor Channel Screenshots",
        "semantic_class": "B",
        "content_domain": "HEALTH",
        "copy_mode": "COPY",
    },
    {
        "index": 10,
        "path": "/Users/ghilmanislam360/Downloads/The Health Educator(2)",
        "kind": "flat_dataset",
        "dataset_key": "HEALTH_EDUCATOR",
        "dataset_name": "The Health Educator — Competitor Channel Screenshots",
        "semantic_class": "B",
        "content_domain": "HEALTH",
        "copy_mode": "COPY",
    },
    {
        "index": 11,
        "path": "/Users/ghilmanislam360/Downloads/all training data of youtube",
        "kind": "flat_dataset",
        "dataset_key": "YT_TRAINING_CORPUS",
        "dataset_name": "All Training Data of YouTube — Global Knowledge Corpus",
        "semantic_class": "A",
        "content_domain": None,
        "copy_mode": "COPY",
    },
    {
        "index": 12,
        "path": "/Users/ghilmanislam360/Documents/Codex",
        "kind": "codex",
    },
]

# ---------------------------------------------------------------------------
# ROOT 12 (Codex) rules. Matched against the path relative to the Codex root,
# longest prefix wins. Independently spot-verified against the live
# filesystem (file counts for every noise dir below; confirmed .zip backups
# gone; confirmed the two "empty" dirs are actually empty) rather than
# trusted blindly from CODEX_PROJECT_INDEX.md / DATASET_INVENTORY.md, which
# were themselves used only to know where to look.
# ---------------------------------------------------------------------------

# (path_prefix, disposition, dataset_key, reason)
CODEX_RULES = [
    # --- noise / tooling, everywhere they occur ---
    ("2026-08-20/anaylze-this-vide/work/.swift-cache", "TOOLING", None,
     "Swift compiler cache — regenerable build artifact, not evidence"),
    ("2026-08-21/files-mentioned-by-the-user-how-2/work/video_forensics/pydeps", "TOOLING", None,
     "Vendored PyTorch/pip dependency tree — regenerable, not evidence"),
    ("2026-08-24/files-mentioned-by-the-user-simple/work/python_pkgs", "TOOLING", None,
     "Vendored Python dependency tree — regenerable, not evidence"),
    ("2026-08-24/files-mentioned-by-the-user-simple/work/swift-cache", "TOOLING", None,
     "Swift compiler cache — regenerable build artifact, not evidence"),
    ("2026-08-24/files-mentioned-by-the-user-simple/work/__pycache__", "TOOLING", None,
     "Python bytecode cache — regenerable, not evidence"),
    ("2026-08-24/files-mentioned-by-the-user-simple/work/models", "TOOLING", None,
     "Downloaded local Whisper ASR model weights — tool artifact, not evidence"),

    # --- confirmed-empty sibling dir, and the empty youtube-intelligence-os scaffold copy ---
    ("2026-08-21/files-mentioned-by-the-user-how", "NOISE", None,
     "Confirmed empty sibling directory (0 files)"),
    ("2026-08-27/you-are-setting-up-the-foundation/youtube-intelligence-os", "NOISE", None,
     "Empty scaffold copy (0 files); canonical repo is Decision 009's separate path, not this location"),

    # --- Project 1 (DS-01 sunset v1) vs the stray unrelated video mixed into its workspace ---
    ("2026-08-20/anaylze-this-vide/work/frame_samples", "HOLD", "CODEX_STRAY_UNRELATED_VIDEO",
     "Unrelated talking-head video's frames, accidentally mixed into the sunset-v1 workspace; contains an identifiable real person — held for human review, not registered as competitor/forensic evidence"),
    ("2026-08-20/anaylze-this-vide/outputs/video_contact_sheet.jpg", "HOLD", "CODEX_STRAY_UNRELATED_VIDEO",
     "Contact sheet of the same unrelated stray video"),
    ("2026-08-20/anaylze-this-vide", "SUPPORTING_EVIDENCE", "CODEX_SUNSET_V1",
     "Sunset video ('How long could you drive towards the sunset') forensic reconstruction case #1"),

    # --- Project 2 (DS-03/DS-04/DS-05) ---
    ("2026-08-21/files-mentioned-by-the-user-how-2/work/moon_protons_forensics", "SUPPORTING_EVIDENCE", "CODEX_MOON_PROTONS",
     "Moon/electron physics video forensic reconstruction case"),
    ("2026-08-21/files-mentioned-by-the-user-how-2/outputs/moon_protons_forensics", "SUPPORTING_EVIDENCE", "CODEX_MOON_PROTONS",
     "Moon/electron physics video forensic reconstruction case"),
    ("2026-08-21/files-mentioned-by-the-user-how-2/work/weird_worrying_forensics", "SUPPORTING_EVIDENCE", "CODEX_WEIRD_WORRYING",
     "\"Weird and worrying questions\" video forensic reconstruction case"),
    ("2026-08-21/files-mentioned-by-the-user-how-2/outputs/weird_worrying_forensics", "SUPPORTING_EVIDENCE", "CODEX_WEIRD_WORRYING",
     "\"Weird and worrying questions\" video forensic reconstruction case"),
    ("2026-08-21/files-mentioned-by-the-user-how-2/work/video_forensics", "SUPPORTING_EVIDENCE", "CODEX_SUNSET_V2",
     "Sunset video forensic reconstruction case #2 (independent, longer re-run of the same topic as CODEX_SUNSET_V1 — possible REVISION relationship, unresolved, flagged not merged)"),
    ("2026-08-21/files-mentioned-by-the-user-how-2/outputs/keyframes", "SUPPORTING_EVIDENCE", "CODEX_SUNSET_V2",
     "Sunset v2 keyframes, stored at outputs/ root rather than a subfolder"),
    # These 5 files sit directly under outputs/ with no dataset-specific
    # subfolder; visually confirmed (spot-checked, all 5 files) to show the
    # sunset/car/globe sequence, not moon/protons or weird-questions content
    # — they are a keyframe atlas for CODEX_SUNSET_V2, matching outputs/keyframes/.
    ("2026-08-21/files-mentioned-by-the-user-how-2/outputs/keyframe_atlas_01.jpg", "SUPPORTING_EVIDENCE", "CODEX_SUNSET_V2",
     "Sunset v2 keyframe atlas page 1/5 (visually confirmed sunset content)"),
    ("2026-08-21/files-mentioned-by-the-user-how-2/outputs/keyframe_atlas_02.jpg", "SUPPORTING_EVIDENCE", "CODEX_SUNSET_V2",
     "Sunset v2 keyframe atlas page 2/5"),
    ("2026-08-21/files-mentioned-by-the-user-how-2/outputs/keyframe_atlas_03.jpg", "SUPPORTING_EVIDENCE", "CODEX_SUNSET_V2",
     "Sunset v2 keyframe atlas page 3/5 (visually confirmed sunset content)"),
    ("2026-08-21/files-mentioned-by-the-user-how-2/outputs/keyframe_atlas_04.jpg", "SUPPORTING_EVIDENCE", "CODEX_SUNSET_V2",
     "Sunset v2 keyframe atlas page 4/5"),
    ("2026-08-21/files-mentioned-by-the-user-how-2/outputs/keyframe_atlas_05.jpg", "SUPPORTING_EVIDENCE", "CODEX_SUNSET_V2",
     "Sunset v2 keyframe atlas page 5/5 (visually confirmed sunset content)"),
    # The 3 topic-specific blueprint reports sit directly under outputs/
    # (not in a per-topic subfolder) — matched by exact filename, not a
    # shared prefix, since a shared-prefix rule previously misrouted all
    # three (plus the 5 atlas files above) into CODEX_MOON_PROTONS.
    ("2026-08-21/files-mentioned-by-the-user-how-2/outputs/How_long_could_you_drive_towards_the_sunset_forensic_blueprint.md",
     "SUPPORTING_EVIDENCE", "CODEX_SUNSET_V2", "Sunset v2 canonical forensic blueprint report"),
    ("2026-08-21/files-mentioned-by-the-user-how-2/outputs/Weird_and_worrying_questions_forensic_blueprint.md",
     "SUPPORTING_EVIDENCE", "CODEX_WEIRD_WORRYING", "Weird-and-worrying-questions canonical forensic blueprint report"),
    ("2026-08-21/files-mentioned-by-the-user-how-2/outputs/What_if_the_Moon_were_made_of_Protons_forensic_blueprint.md",
     "SUPPORTING_EVIDENCE", "CODEX_MOON_PROTONS", "Moon/protons canonical forensic blueprint report"),
    ("2026-08-21/files-mentioned-by-the-user-how-2/docs/superpowers/plans/2026-08-21-moon-protons-forensic-report.md",
     "REFERENCE_ONLY", "CODEX_MOON_PROTONS", "Execution-plan/provenance doc for the moon/protons case"),
    ("2026-08-21/files-mentioned-by-the-user-how-2/docs/superpowers/plans/2026-08-21-weird-worrying-video-forensics.md",
     "REFERENCE_ONLY", "CODEX_WEIRD_WORRYING", "Execution-plan/provenance doc for the weird-and-worrying-questions case"),

    # --- Project 3 (DS-06) ---
    ("2026-08-24/files-mentioned-by-the-user-simple/work/evidence_final", "SUPPORTING_EVIDENCE", "CODEX_RETIREE_ROUTINES",
     "Corrected shot-detection evidence (canonical — the deliverable generator consumes this, not work/evidence)"),
    ("2026-08-24/files-mentioned-by-the-user-simple/work/evidence", "SUPERSEDED", "CODEX_RETIREE_ROUTINES",
     "Draft shot-detection pass, superseded by work/evidence_final — kept as a linked prior revision, not deleted"),
    ("2026-08-24/files-mentioned-by-the-user-simple", "SUPPORTING_EVIDENCE", "CODEX_RETIREE_ROUTINES",
     "Retiree daily-routines video forensic reconstruction case"),

    # --- prior-session relocation-planning artifacts for this very repo
    # (the source of Decision 009 in the canonical repo's docs/DECISIONS.md);
    # historically informative, superseded by the canonical repo's current
    # DECISIONS.md, never raw video/competitor evidence ---
    ("2026-08-27/you-are-setting-up-the-foundation/work/relocation-plan.md", "REFERENCE_ONLY", None,
     "Prior-session repository-relocation planning doc; historical record of how this repo reached its canonical path (Decision 009), superseded by the live repo"),
    ("2026-08-27/you-are-setting-up-the-foundation/work/DECISIONS.md.next", "REFERENCE_ONLY", None,
     "Prior-session staged draft of docs/DECISIONS.md (through Decision 009 only); superseded by the canonical repo's current DECISIONS.md"),
    ("2026-08-20/ana", "NOISE", None,
     "Empty stray directory (0 files, apparent abandoned/renamed typo of anaylze-this-vide)"),

    # --- root-level generated audit docs about this very tree ---
    ("CODEX_FILE_INVENTORY.json", "REFERENCE_ONLY", None, "Prior-session generated audit artifact, not raw video evidence"),
    ("CODEX_MASTER_FORENSIC_AUDIT.md", "REFERENCE_ONLY", None, "Prior-session generated audit artifact, not raw video evidence"),
    ("CODEX_PROJECT_INDEX.md", "REFERENCE_ONLY", None, "Prior-session generated audit artifact, not raw video evidence"),
    ("DATASET_INVENTORY.md", "REFERENCE_ONLY", None, "Prior-session generated audit artifact, not raw video evidence"),
    ("DEEP_INSPECTION_REPORT.md", "REFERENCE_ONLY", None, "Prior-session generated audit artifact, not raw video evidence"),
    ("GLOBAL_AGENT_TOOLS_REPORT.md", "REFERENCE_ONLY", None, "Prior-session generated audit artifact, not raw video evidence"),
    (".DS_Store", "NOISE", None, "macOS Finder metadata file"),
]

# Registration order fixes the DS-00000X allocation sequence deterministically.
REGISTRATION_ORDER = [
    "ROOT2_FORENSIC_RETIREES",
    "DOCTOR_THOMAS",
    "DR_ADEWALE",
    "DR_OKORO",
    "DR_ALIZA_WRIGHT",
    "DR_WATERLING",
    "SENIOR_HEALTH_PODCAST",
    "SENIOR_HEALTH_HUB",
    "HEALTH_EDUCATOR",
    "YT_TRAINING_CORPUS",
    "CODEX_SUNSET_V1",
    "CODEX_STRAY_UNRELATED_VIDEO",
    "CODEX_MOON_PROTONS",
    "CODEX_WEIRD_WORRYING",
    "CODEX_SUNSET_V2",
    "CODEX_RETIREE_ROUTINES",
]

CODEX_DATASET_META = {
    "CODEX_SUNSET_V1": {
        "dataset_name": "Sunset Video Forensic Reconstruction — Case 1 (\"How long could you drive towards the sunset\")",
        "semantic_class": "C",
        "content_domain": None,
        "copy_mode": "SELECTIVE_COPY",
    },
    "CODEX_STRAY_UNRELATED_VIDEO": {
        "dataset_name": "Stray Unrelated Video Frames (accidental, contains identifiable real person)",
        "semantic_class": "H",
        "content_domain": None,
        "copy_mode": "REFERENCE",
    },
    "CODEX_MOON_PROTONS": {
        "dataset_name": "Moon/Electron Physics Video Forensic Reconstruction",
        "semantic_class": "C",
        "content_domain": None,
        "copy_mode": "SELECTIVE_COPY",
    },
    "CODEX_WEIRD_WORRYING": {
        "dataset_name": "\"Weird and Worrying Questions\" Video Forensic Reconstruction",
        "semantic_class": "C",
        "content_domain": None,
        "copy_mode": "SELECTIVE_COPY",
    },
    "CODEX_SUNSET_V2": {
        "dataset_name": "Sunset Video Forensic Reconstruction — Case 2 (independent re-run, possible revision of Case 1)",
        "semantic_class": "C",
        "content_domain": None,
        "copy_mode": "SELECTIVE_COPY",
    },
    "CODEX_RETIREE_ROUTINES": {
        "dataset_name": "Retiree Daily-Routines Video Forensic Reconstruction",
        "semantic_class": "C",
        "content_domain": None,
        "copy_mode": "SELECTIVE_COPY",
    },
}

# Directory names that mean TOOLING no matter what dataset tree they are
# nested inside (a swift-cache/__pycache__/hf-cache dir under an otherwise
# real forensic-evidence folder is still tooling, not evidence) — checked
# BEFORE dataset-prefix matching, not merely as a fallback.
TOOLING_DIR_NAMES = {
    "__pycache__", ".git", "node_modules", ".venv", "venv",
    "site-packages", ".swift-cache", "swift-cache", "pydeps", "python_pkgs",
    "hf-cache",
}

# Directory names that mean NOISE (junk sidecars, not dev tooling) no matter
# where nested.
NOISE_DIR_NAMES = {
    "__MACOSX",
}

# Extensions whose canonical bytes are always REFERENCE-only in SELECTIVE_COPY
# datasets (dense/proxy frame sequences) — copying every frame would bloat
# data/raw/ without adding evidence beyond what hashing+clustering already
# proves; the report/manifest/CSV files in the same dataset are still copied.
FRAME_DIR_MARKERS = ("dense_frames", "proxy_frames", "sunset_frame_dense", "sunset_frame_samples", "overview_frames", "keyframes")
