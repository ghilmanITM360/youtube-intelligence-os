# R13: optional cross-vendor review, ready to run (not run)

## What R13 requires, and what was done

**Source of the requirement.** R13 comes from the owner's final-audit prompt, which says: "Describe actual reviewer independence accurately. Do not invent an additional human-review requirement unless the kit explicitly requires it."

**What the kit says.**
- The kit (`visual-ct-scan` v1.0, references 01–14) never requires a reviewer from a different vendor or model.
- Reference 10 warns that a simulated "panel of experts" is not independent empirical validation.
- The kit asks for a `reviewer` locator in `quality_gate.json`.

So R13 is read as: a separate reviewer, plus an accurate account of how independent that reviewer is.

**What was done (2026-11-05).**
- **Batch 1.** A fresh reviewer was given only a frozen brief (`BRIEF_BLIND_REVIEW.md`, sha256 in `BRIEF_FREEZE_SHA256.txt`), the three source hashes, and unlabelled native-resolution sheets. It saw no ledger and no prior labels. It named 69 intervals blind:
  - all 28 LOW-confidence tile-only rows;
  - all 11 camera-UNCERTAIN rows;
  - a seeded random 30 (10 per video).
- **Batch 2.** The same procedure was run on the 30 tile-only rows labelled STATIC_HOLD that the dense measurement contradicts. Its files are in `batch2/`.
- **Reconciliation.** Disagreements were resolved afterwards by:
  - deterministic measurement (`BLIND_ADJUDICATION_MEASURE.csv`, `../dense/CAMERA_CHAIN_ALL_<vid>.csv`);
  - orchestrator native-frame checks.

  All outputs are kept. The reconciliation is in `BLIND_RECONCILIATION*.csv`.

**Honest limit.** The blind reviewer and the orchestrator are both Claude models (Anthropic). They are separate contexts with no shared labels, but they are the same vendor.

## If the owner wants a different-vendor check as well

**Authorization needed first.**
- A Codex CLI is installed on Machine A at `/Applications/ChatGPT.app/Contents/Resources/codex-cli`, and `~/.codex` holds an auth file.
- It was **not used**. Running it would send frames derived from competitor videos to an external service, and this task forbids uploading media without explicit owner authorization.

**Bundle (already on Machine A, local only):**
- `BRIEF_BLIND_REVIEW.md`, unchanged;
- `BLIND_SHEET_INDEX_FOR_REVIEWER.csv`;
- `sheets_local_only/*_B###.jpg` (24 sheets), and `batch2/` (11 sheets).

**Steps after authorization:**
1. Give the other reviewer only these files. Have it write `BLIND_REVIEW_XV.csv` with the same header.
2. Reconcile its labels against the ledger. Run `python3 ../scripts/blind_reconcile.py`, with `BLIND_REVIEW.csv` replaced by `BLIND_REVIEW_XV.csv` as the input.
3. Compare its labels with the Claude blind labels (`BLIND_REVIEW.csv`), class by class.
4. Record agreement rates. Adjudicate any new disagreement on native frames, the way it is done in `blind_reconcile.py`.
