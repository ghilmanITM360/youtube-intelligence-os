# Method and framework record: the What If? 83-script study

**Scope.** This study analyses the script only. It uses the transcript text of xkcd's What If? (CH-000004, DS-000017, acquired 2026-08-31). It does no visual, motion, editing, audio or thumbnail analysis; those parts of the reference prompt are switched off by the user's override.

**The user's brief.** The request is the "MASTER 83-VIDEO YOUTUBE SCRIPT INTELLIGENCE & REVERSE-ENGINEERING SYSTEM", supplied in chat on 2026-11-17.

## Analytical framework

| Item | Value |
|---|---|
| Primary method | Script sections of `03_ULTRA_PRECISION_VISUAL_SCRIPT_ORIGINAL.txt` (SHA-256 `fea21e6c…d9e9ad`; path `research/portable-recovery/machine-b-2026-11-02/.../source-prompts/`) |
| Sections used | SCRIPT_FIRST_PASS (l.491), SCRIPT_ANALYZER_PANEL with seven lenses (l.524), SCRIPT_ANALYZER_CONSENSUS (l.760), TITLE_THUMBNAIL_SCRIPT_ALIGNMENT (l.1283, title only), RETENTION_ARCHITECTURE (l.1313), CREATOR_FORMULA (l.1438), FINAL_VIDEO_SYNTHESIS §2 SCRIPT ENGINE (l.1722), CONFIDENCE_SYSTEM (l.368), ANTI_HALLUCINATION_RULES (l.390) |
| Repo framework | `data/knowledge/reference_knowledge.db`, framework **v1** (schema 11) |
| Retrieved sections (FTS5 `build_reference_kb.search`, 2026-11-17) | open loop: RM-4bbe6c6e34b2:p.55, p.48; RM-62565f03d2c1:p.16; RM-aacc8fc2373d:p.4 · hook: RM-4bbe6c6e34b2:p.6, p.12; RM-62565f03d2c1:p.32, p.26 · payoff: RM-4bbe6c6e34b2:p.44, p.43; RM-8b65784803f2:p.4; RM-52235e9459a8:p.3 · BUT THEREFORE: RM-52235e9459a8:p.1–3 · call to action: RM-63c5338e6a9e:p.6; RM-d0f681ddcabe:p.16, p.13 · intro: RM-cb50fe7ec900:p.2; RM-62565f03d2c1:p.25–26 · throughline: RM-242707556f81:p.1, p.4 · mini hook: RM-6d9840bbe0ca:p.1–2 |
| Source members | RM-4bbe6c6e34b2 Hook guide · RM-52235e9459a8 BUT/THEREFORE · RM-6d9840bbe0ca Script Analyzer · RM-cb50fe7ec900 Intro Analyzer · RM-242707556f81 Seven Engine / 16 Commandments · RM-8b65784803f2 Title Analyzer · RM-63c5338e6a9e SEO checklist · RM-62565f03d2c1 new YT algorithm updates · RM-d0f681ddcabe algorithm guide · RM-aacc8fc2373d Renae blueprint |

### Rules applied per audit (all are `CREATIVE_HEURISTIC` unless noted; none is a platform fact)

| Code in audits | Rule | What it checks |
|---|---|---|
| HOOK-01 | FR-HOOK-01 | Context lean, then a scroll-stop beat, then a contrarian snapback. The rule says not to penalise explainers that lack these beats. |
| INTRO-01..04 | FR-INTRO-01..04 | Clarity, curiosity, tone and setup of the opening. Whether the title expectation matches the opening. Over- or under-explaining. Early anticlimax. |
| SCR-01..06 | FR-SCR-01..06 | Spine, retention mechanics, promise delivery, cause and effect, CTA placement, curiosity gaps. |
| BT-01 | FR-BT-01 | Beats joined by BUT/THEREFORE rather than "and then". |
| 16C-05 / 07 / 13 / 16 | FR-16C-05/07/13/16 | Throughline. New loops opened before old ones close. Plain language. Echo ending. |
| VC-05 / VC-09 | FR-VC-05/09 | Specific numbers (specificity is not accuracy). Conciseness. |
| TITLE-02..04 | FR-TITLE-02..04 | Title-concept match. Over-promise risk. The title opens a loop that the video pays off. |

Judgments are CONFORMS, PARTIAL, ABSENT or N/E (not evaluable).

### Exceptions, with reasons

- **FR-16C-06** (a reset every 20–30 s) is N/E. The transcripts have no timestamps.
- **FR-NA-01, FR-NA-02** are not applicable. They need audiovisual evidence or concern image/video prompting.
- **FR-NA-03** is not executed. The "seven lenses" are perspectives that one analyst (Claude) applied. No seven models were run and no 1–10 scores were given.
- **Thumbnail alignment** is not reviewed. Thumbnails are out of scope, so alignment is judged from the title only.
- **FR-SEO-01** is reported descriptively. There is no search-volume data.

## Evidence conventions

- **¶N** is the Nth paragraph under `## Script` in the video's script file (`research/what-if-scripts/{long,shorts}/NN-<id>.md`).
- **wA–B** is a word range. It is used for auto-captions without punctuation, where paragraphs collapse.
- Print a locator with `python3 research/what-if-scripts/analysis/locate.py V001 5`. Run `locate.py check` to verify that every cited locator exists.
- **Copyright handling.** The scripts are copyrighted (Randall Munroe / xkcd). Audits therefore cite locators and paraphrase instead of reproducing transcript text. The exact words are one command away.
- **Three registers are kept apart.** **Obs.** is an observed textual technique (High confidence when it is a direct structural fact). **Fn.** is the likely narrative function (Medium). **Eff.** is the audience effect, which is unverified (Speculative).
- **No timestamps exist.** The "first 30 seconds" are analysed as opening *beats* (B1, B2…), and no time intervals are inferred. Words per second (words ÷ listed duration) is a density estimate only.
- **No performance claims.** Views are recorded at acquisition in the inventory. No CTR, retention, watch-time or causal claim is made from writing quality.

## Duplication caveat (AGENTS rule 9)

Most Shorts are cut-downs of long-form videos: their 8-gram overlap with a parent long video is 80–100% (see `01_INVENTORY.md`). Every video still gets its own audit. In the cross-video counts, however, each content family is counted once. Counts are reported both per video (n=83) and per independent family.
