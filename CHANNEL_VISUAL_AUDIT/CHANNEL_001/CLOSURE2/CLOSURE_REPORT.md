# CASUAL FINANCE (CH001) CLOSURE 2 REPORT, 2026-11-22
Follows the Codex independent audit (PARTIAL, targeted research required). Scope: the three named gaps only. No new full video scans; V1 Rent untouched; no push.

## 1. Corrected coverage (`COVERAGE_MATRIX.csv`, `tier` column; `tools/build_coverage_matrix.py`)
216 physical MP4 files; 215 unique SHA-256 (duplicate = idless "Why Japan's Economy Is Awful" Shorts); 34 landscape / 182 Shorts physical (34 / 181 unique). Visual coverage tiers: **17 gated** (13 long-form, 4 Shorts; 2,148 shot records; visual-only, no human listening), **11 partial** (4 L2 Short state tables, 2 hash-keyed Short tables, o3FQcd91MIs, incomplete gG239LrksH4, and 3 files with older editing-forensics workspaces I did not inspect; Codex counted 8), **188 coarse**. Audio-visual coverage: 13 long-forms have unverified ASR alignment (1,437 sentence intervals); zero human-listened. Pooled long-form shot median 2.87 s (IQR 1.87-4.40 s over 2,052 intervals; 11.8-23.7 boundaries/min).

## 2. Codex corrections
`CODEX_CORRECTION_DISPOSITION.md`: 8 accepted, 1 modified (partial count), 0 rejected; Bitcoin f157 example not re-measured. The 4.8 s rule is retracted everywhere operational; legacy numbers kept with banners.

## 3. Targeted source windows
All eight windows analysed at native fps (`EVIDENCE_FORENSICS_2026-11-22.md`, `forensics/EVIDENCE_EVENTS.csv`): 9 annotation events in 6 documents. New rules: no universal delay; red ellipses were instant complete marks (4/9) or pre-marked (3/9); one progressive yellow sweep (2.0 s, paced to the clause); lead-in-hold reveal; clause-boundary replacement cut; mark timing ranged from +1.0 s after to 1.3 s before the spoken number. Sample is small (5 videos, ASR-unverified). Displayed claims: NY Fed $1.28T and U.S. Courts 24,737 vs 23,107 (+7.1%) confirmed; EIA tooltip value, Proactive/MacroMicro figures, and the "decade-long high" claim unverified. Detector caveat: colour detectors fire on artwork; only viewed frames count.

## 4. Claim gate
`tools/claim_gate.py`: statuses, ten semantic checks, excerpt entailment of numbers/definitions/quotes, unit licensing, hypothetical label and arithmetic, qualification presence. 19 negative/positive tests (banking-definition error, dollar-vs-percent conflation, unsupported number, misleading comparison, hypothetical shown as actual, fabricated quote, missing qualification, UNVERIFIED/REJECTED, unreviewed check, source tag without excerpt, wrong arithmetic) all pass; 7 proof-contract tests show the real proof register cannot render after tampering. Limits: cannot establish truth; spoken number-words are not parsed; relies on honest review of the ten checks.

## 5. Document renderer
`V1/tools/doc_scene.py` (+ `doc_scene_schema.md`): extends the existing beat engine via `document_item()`; immutable source with SHA check, source-pixel crops with enforced aspect, document-local annotations through one transform, instant/progressive marks, legibility and required-context guards, frame-addressable event table. 17 tests incl. a pixel test of registration through a zoom (that test caught a real crop-box bug before rendering). No existing renderer file was modified.

## 6. Proof
`productions/doc-animation-proof-01/out/DOC_PROOF_60s.mp4` (SHA in `DOC_PROOF_60s.sha256`): silent 60 s, 1920x1080, 30 fps, authentic CFPB capture (retrieved 2026-11-22T05:38:47Z), progressive yellow highlight, red underlines, instant red ellipses, marks registered through two zooms, hard cut from evidence into a labelled original hypothetical diagram ($1,000 at 5%: +$50.00, +$52.50, +$55.13, balance $1,157.63; simple $150.00 vs compound $157.63, +$7.63), existing provisional host. Slop gate on `PROOF_SCRIPT.md`: PASS (proxy; manual checklist C1-C5 remain human).

## 7. Independent acceptance
`productions/doc-animation-proof-01/out/INDEPENDENT_REVIEW_2026-11-22.md`: gates 1,3,5,7,8,9,11,12 PASS; 2,4,6,10 PASS WITH NOTES; no blocking defects; audio PENDING. Open cosmetic notes: column header cropped after 18.8 s, E5 ellipse touches adjacent text, ~0.1 s near-white frames at beat changes (about 39.5 s, 46.2 s; reviewer-observed, not frame-verified by me), E6 highlight has no spoken counterpart.

## 8. Decisions
**A. Long-form research readiness: CLOSED WITH DOCUMENTED LIMITATIONS.** The corrected rules, evidence-animation taxonomy and playbook support planning purposeful original long-form videos. Not 100% mastery: n=9 evidence events, ASR unverified, 188 files coarse.
**B. Production capability: DEMONSTRATED for one document type.** Claim gate, document scene operation and a short proof pass tests and an independent review. Untested: PDF/scrolling documents, tall pages, narration sync against real speech, BLS-type manual captures, rights clearance (provisional).
**C. Shorts and audio-visual validation: LIMITED.** Shorts remain partially validated (single-video evidence; the dense/full-bleed 3132dfa8 variant vs sparse/captioned not compared). No sound-design intelligence; no human listening; the proof's audible review gate is PENDING.

## 9. Requirements for future productions
Capture sources manually where sites block bots; confirm rights; record narration before final timing; human-listen to every edit seam; owner reviews V1 Rent R9/R9b open items separately (unchanged). Rights status of the CFPB capture is provisional.
