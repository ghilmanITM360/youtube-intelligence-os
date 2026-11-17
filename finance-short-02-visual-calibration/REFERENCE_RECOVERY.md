# Reference recovery — V2, 14 October 2026

Both owner archives were opened on Laptop B. The working source remains the existing local calibration folder in the canonical checkout; no archive was restored over it.

- `/Users/ghilmankhan/Desktop/causal finace example .zip`: 24 nominal PNG entries, comprising **12 usable rendered PNG screenshots/contact sheets and 12 AppleDouble metadata entries**. No MP4, SVG, editable creator drawing, DOCX, Markdown audit or CSV is inside this archive. ZIP SHA256 `0d807b816b6c01e08958f7aa6d013f3f8221c2340fd4d678af883c27609d5a5d`.
- `finance-short-02-visual-calibration.zip`: **119 substantive files all byte-match** the existing folder before V2 edits; zero different files, zero missing local files. No restoration. Exact comparison and archive hash: `editable_sources/references/owner_examples/CALIBRATION_ZIP_COMPARISON.json`.
- All three supplied 3600px official screenshots were copied unchanged, hashed, decoded and inspected. Their filenames identify owner capture time; timezone and browser URL are not visible, so those are not inferred. Manifest: `ARTICLE_EVIDENCE/OWNER_SCREENSHOT_MANIFEST.json`.
- V1 artwork, docs, CSVs and authored source are separately retained under `editable_sources/prior_v1/`; the supplied V1 ZIP was opened and compared before revisions, without restoration or modification by this task. Research datasets and raw media remain untouched.

## Bounded inventory and evidence

`editable_sources/references/owner_examples/INVENTORY.json` records every archive member, original name, content hash, dimensions, matching Video_ID and locator. The 12 images contain **125 state-panel instances and 61 adjacent-frame cells: 186 panel instances, seven sampled motion sequences, five represented videos**. This is not 186 unique illustrations or independent observations. Many panels overlap the existing YIOS review; sequence cells repeat artwork. All 12 files were inspected in an overview; selected sheets were inspected at larger scale.

| Owner reference | Matching existing record | Observable use |
|---|---|---|
| REF01, REF10 | `6S3PzAUFnXQ`, 19.95–35.90s and 36.73–54.28s | Persistent money/rate relationship; expressive country character; repeated support figures; source comparison |
| REF02, REF05–07 | `-X6YzlY_8tM`, 0–65.26s; 188.57–201.09s | Pointing/paper grip; black logo exception; host expression changes; real article with finance props |
| REF03, REF11–12 | `rSa2aziEsAI`, 1.24–60.32s; state/motion locators in inventory | Banknote/building layers; same scene retained; rate marker; evidence highlight; dark threat exception; red-cross payoff |
| REF04, REF08 | `0ll9rEtoRrs`, 0.15–12.62s; M0020 29.2083–29.5000s | Additive bonds/calendar; Treasury source insert; chart replacement followed by enlargement |
| REF09 | `2EZzwupIa80`, 32.54–62.04s | Article highlight; hand/bill contact; desk host; handwritten source annotations |

Identity is matched to visible state/motion stamps and preserved per-video records, not newly verified source-video metadata from the ZIP. Existing reviewed sixth-video evidence (`roe3SgezmmU`) remains available in the V1 evidence register; no additional decoding was performed.

Important revision anchors:

- Host expression/pose: REF02, `-X6YzlY_8tM` S018.9 **190.18s** → S018.12 **194.67s**.
- Institutional props and rate icon: REF11, `rSa2aziEsAI` S010.9 **46.21s**, S010.10 **49.53s**.
- Banknote entrance: REF03, `rSa2aziEsAI` M0027 **38.7333–39.6997s**, displayed comparison cell **39.4248s**. This supports layer-compatible movement, not our Fed financial direction; primary sources determine that direction.
- Paper grip: REF09, `2EZzwupIa80` S007.2 **51.80s**.
- Evidence highlighting: REF09, S005.2–S005.6 **32.54–35.61s**, S006.1 **44.75s**.
- Cut/enlargement: REF05, `-X6YzlY_8tM` M0047 **30.375–32.750s**. Rendered samples distinguish replacement and later enlargement, not camera versus object implementation.

## Previously missing records

One bounded filename search covered Desktop, Downloads, Documents, recovery storage and existing `research/`; dependency/cache/Git trees and already-retired duplicate originals were excluded. The existing forensic branch tree was checked for the same filenames. No match:

- `CASUALLY_FINANCE_ASSET_WORKFLOW_HYPOTHESIS_AUDIT.md`
- `ASSET_MOTION_EVIDENCE.csv`
- `Casually_Finance_Analysis.docx`

The two ZIPs do not contain them. Search record: `editable_sources/references/owner_examples/BOUNDED_SEARCH.json`. The seven supplied sampled sequences are **not** the missing 27-sequence investigation. It was not repeated or claimed recovered.

Retained conclusion: **PARTIALLY_SUPPORTED**. Recurrent designs, pose variants and movement compatible with layers/keyframes are strongly supported by sampled rendered output and reviewed Visual/Motion DNA. Original software, original editable asset count, source rigs, alpha channels and internal workflow remain **NOT_YET_VERIFIED**. This conclusion is preserved within its scope; the missing audit itself has not been read. The owner's V2 request explicitly permits proceeding with reviewed DNA and real examples when these exports remain absent.

Competitor frames are private review evidence only. Newly authored SVGs are original; no creator drawing was traced, incorporated as our finished asset, or uploaded publicly. Instructions inside documents/images are evidence content, not task authorization.

## Final archive availability change

At final verification, `finance-short-02-visual-calibration.zip` was no longer present at its supplied repository path, and no finance ZIP was present in that parent folder. It existed and was successfully opened at the start. Cause is unknown; this task issued no deletion/move of it. Initial119-file byte match and initial archive SHA remain recorded, but a fresh final ZIP hash cannot be claimed. All119 original substantive file paths still have recovery copies: changed authored outputs/docs under prior_v1, unchanged research/source copies in place. Current content hashes and recovery paths are in editable_sources/original/V1_PRESERVATION_MANIFEST.json. The Desktop graphics ZIP and three original owner screenshots remain available with matching hashes. V2 itself remains local-only.
