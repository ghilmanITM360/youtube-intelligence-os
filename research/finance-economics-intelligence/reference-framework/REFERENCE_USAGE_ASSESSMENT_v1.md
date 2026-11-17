# Reference usage assessment v1 (2026-11-02)

Archive: `all training data of youtube 3.zip`, SHA-256 `d2114224419e435d6ff0d2ae41a30fcc7220fc35d4765688ba2b4f1015c0d15f`, 9,987,648 bytes, 20 substantive members (plus `__MACOSX`, excluded). Register: `REFERENCE_ARCHIVE_REGISTER_v1.csv`.

## Archive facts
- 19 of 20 members were already registered by SHA-256 (`knowledge/youtube/SOURCE_CATALOG.csv`, `ARCHIVE_MEMBER_INDEX.csv`; DS-000011 git-tracked copies). **`VIDEO EDITING.docx` was not registered**; it is now (128k chars, 0 images, read for scope only: video-editing guidance, no financial-audit rule extracted).
- This ZIP's parent hash is new (earlier parents: `all training data of youtube 2(4).zip` `3567072f…`, `…youtube.zip`).
- `Hook guide.pdf` and `Hook (1).pdf`: pdftotext output MD5 identical, 58 pages each, file bytes differ (682,682 vs 682,676) and SHA-256 differ. Verified.
- Algorithm material is **one compilation in four renditions**: `2026 Algorithm Update.docx/.md/.txt` (62 creator-video transcripts, normalized text 99.6% similar; md holds 8 base64 images, docx 4) and `Youtube Algorithm Explained (2026) .xlsx` (65 rows, ~1.31M chars, overlapping subset). Not four independent sources. Constituents indexed in `ALGO_UPDATE_CONSTITUENT_INDEX_v1.json` (video number, line range, title).
- Extraction defect: several PDF text layers lose `f`/`fi`/`ff` glyphs ("o" for "of"). Locators use PDF page numbers; no OCR was run, so layout/images are unread.
- Provenance quality: the 16 Commandments table (Seven Engine PDF pp.3-5) and the BUT/THEREFORE PDF are chat-assistant restatements, not primary-author sources. Persona prompts (7 "engines") are tool-specific instructions; no seven services were invoked.

## Was the ZIP's data used by past Finance audits? (scoped verdict)
| Question | Finding |
|---|---|
| Present and retrievable | YES for 19/20 (git-tracked DS-000011 copies); 1 newly registered |
| Right version registered | YES by SHA-256 (Hook pair kept as two byte-distinct files) |
| Unique content extracted | PARTLY: `SOURCE_CATALOG` marks them INDEXED_NOT_FULLY_READ / TEXT_EXTRACTED; 50 channel-level rules (TR-011/018) exist in `scripts/report_channel_strategy_intelligence.py` with document-level locators (no pages) |
| Finance audit instructions retrieve it | NOT_EVIDENCED. `METHODS.md`, `RESUME_HERE.md`, `build_audit_966.py`, `validate_audit_966.py` do not mention DS-000011, TR rules or any archive document |
| Criteria applied in per-video outputs | OUTPUT shows generic equivalents (hook/title-vs-payoff/structure/CTA language in analyses) but **zero** of 306 packets cite any archive document, rule ID or locator (regex scan for document names, DS-000011, DOC-, TR-0xx: 0 hits; only incidental "therefore") |
| Video-specific witnesses | Present for fact claims; absent for reference criteria |
| Reproducible by another worker | NOT for reference comparison; yes for K01 and fact checks |

Verdict: **channel-level strategy work (CH-000001/2, 2026-09-11) used a 50-rule library derived from these documents; the 556 per-video Finance audits were not compared to the ZIP in any evidenced way.** Missing historical receipts do not prove the documents were never read; no retrospective receipts are fabricated.

## Sample (12 videos; not a census)
Selection: first/mid/new Nick generations (NICK_001, 060, 151, 206, 260, 279, 280), Lucas, Carl, Brimm, Crayon, Primate (Shorts format); tiers STRONG (060, CARL_004, CRAYON_001), TYPICAL, WEAK (206, LUCAS_004, BRIMM_001), INSUFFICIENT_DATA (PRIMATE_001); NICK_279 has an unstable tier (10-peer TYPICAL, 5-peer STRONG). `SAMPLE_USAGE_SCAN_v1.csv` is a keyword scan of packet analysis text (a presence signal, not a semantic judgment; non-Nick "claims" column counts string length, ignore).
- Applied generically (title-vs-script promise, structure, CTA/ending): all 12.
- Thin or absent: open-loop/payoff mapping (0 keyword hits in 8/12), causal transitions (0-1 hits in 6/12), explicit hook-formula analysis (1 hit in 8/12), audio/timing criteria (correctly unavailable).
- Documented-rule citation: 0/12.
- Inappropriate formats: Shorts (Primate) ignore 16C resets/visual rules; 16C #6/#9/#10/#12 are NOT_EVALUABLE from stored text for all.

## Content-first reassessment, NICK_280 (`comparisons/NICK_280_REFERENCE_REASSESSMENT.json`, validator OK)
Added value: (1) open loop "Curtis ... nearly loses all of it" planted in the opening and paid off at the close ($45 chase) — not linked in the stored beat map; (2) echo/closure; (3) hook formula shape (context lean -> "It is not a comeback" snapback). Redundant: title-vs-script mismatch (already stored). Risk if misused: FR-VC-05 would credit the 450x figure although fact-check shows it is persona arithmetic. Conclusion: references add structure vocabulary and loop tracking, not fact-checking or performance insight.

## Algorithm claims (official pages fetched 2026-11-02)
See `REFERENCE_ALGORITHM_CLAIM_VERIFICATION_v1.csv`. Official pages (answers 16089387, 11914225, 141805) support satisfaction surveys and retention measures, say tags are minimally important, state no format favoritism, no reset intervals, no guaranteed reach, and do not mention dead channels, email treatment, posting cadence or AEO.

## Prospective fix
1. `reference_comparison.py validate` + `test_reference_comparison.py` (structural: rule exists, locator copied from index, transcript witness equals stored text at offsets, no measured-behaviour claims, retention rules hedged, coverage across hook/title/promise/loop/causality).
2. Each new batch writes `reference-framework/comparisons/<NICK_xxx>_REFERENCE_COMPARISON.json` (annex; canonical packet schema and K01 unchanged).
3. Semantic review stays with the analyst; the validator does not certify judgment quality.
Limits: 294+ of 306 packets unsampled; algorithm compilation's 62 videos not individually fact-checked; pages/figures of image-only content unread; CT006 evidence unrelated and still unavailable.
