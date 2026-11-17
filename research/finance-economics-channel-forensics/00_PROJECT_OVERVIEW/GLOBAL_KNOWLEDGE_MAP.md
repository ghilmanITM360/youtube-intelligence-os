# Global YouTube Knowledge Map — SUPPORTING authority

**Source B located at:** `data/raw/global-youtube-knowledge/` (present identically in the canonical checkout and worktrees). Format discovered by inspection (2026-11-12): a raw-evidence folder of three dataset IDs, not a database or branch.

| Dataset | Files | What it actually is | How it is used here |
|---|---|---|---|
| DS-000011 | 16 files: `YouTube_Intelligence_Brain_v1_Verified_Creator_OS.md`; PDFs: Hook guide (+duplicate “Hook (1)”), Intro Analyzer Prompts, Packaging (Thumbnail/Title) SOP, Renae Creative Engine v2.5, Script Analyzer, The Magic of BUT and THEREFORE, Viral Checklist (Codie Sanchez), YouTube Title Analyzer prompts, YouTube algorithm guide, new YT algorithm updates, Video SEO checklist, Seven Engine Storytelling (16 Commandments), Engine-by-Engine Personality & Lens; DOCX: Nano-Banana prompt guide, VEO 3 prompt guide | Creator-strategy frameworks and prompts | Context for packaging, hook/intro, storytelling and truth discipline |
| DS-000018 | `2026 Algorithm Update - Google Docs tab snapshot.zip` (63 tabs, Hindi/Urdu creator-video transcripts with timestamps, manifest with source URLs) | Third-party creator commentary on the 2026 algorithm | Context only; not used as platform fact |
| DS-000031 | `creator-strategy-audience-psychology-experimentation-corpus.txt` (Urdu/Hinglish lecture transcripts) | Creator lectures: topic selection, promise, comments as research, retention craft, “what does a competitor do after a hit”, niche/format bending, expected-vs-actual review loop | Context for topic research & post-hit behaviour |

Reading coverage: Brain v1 (DS-000011) read in full; Packaging SOP, Viral Checklist, Intro Analyzer, Script Analyzer and BUT/THEREFORE read via text extraction (from the 2026-11-12 audit `knowledge/` folder); DS-000018 and DS-000031 inspected structurally and by headings. Nano-Banana / VEO prompt guides are image/video-generation prompts — not relevant to channel judging.

**Scope rule from the brief:** DS-000011 / DS-000018 are *not* used as additional judges. Where a global-knowledge idea differs from the PDF, the PDF verdict stands and the difference is noted.

## Supporting concepts mapped to PDF principles

| PDF principle | Global-knowledge concept (document → section) | Agreement / tension |
|---|---|---|
| P01 outliers, P06 competitor research | Brain v1 §4 Phase A “find true outliers relative to each source channel's normal performance; separate topic demand from angle”; DS-000031 “Upload Strategy — Hit ke baad competitor kya karta hai?” | Agrees; Brain adds “relative to channel normal”, matching this study's PI method and PDF Part D §2 |
| P02 niche/audience | Brain v1 §4 “define the exact viewer and present tension”; Packaging SOP “know who you're getting to click” | Agrees |
| P04 repetition | Brain v1 §3 “Monetization originality principle” | Agrees with PDF Part D §7 |
| P08-P11 packaging | Packaging SOP: one big idea, bold few words, genuine claims, packaging must signal video type/length; Brain v1 §3 “title/thumbnail must set correct expectation; A/B winners chosen on watch time” | Agrees; SOP's “10%+ CTR” goal is a creator target, contradicted as a universal benchmark by PDF Part D §3 |
| P12-P14 hook/intro | Brain v1 §3 “first 30 s should confirm the promise; never use an arbitrary hook rule”; Intro Analyzer prompts | Partial tension: PDF Masterclass prescribes fixed zones (0-5 s, 5-15 s, 30 s loop); Brain warns against fixed timing rules |
| P15 / script | BUT/THEREFORE doc: causal “but/therefore” beats instead of “and then” | Complements Engagement §2/§7; measured via but-density only (proxy) |
| P16 authority | Brain v1 §2 truth hierarchy, §7 primary-source research | Agrees; stronger for finance (YMYL) |
| P19 length | Brain v1 §11 anti-pattern “stretch videos to eight minutes for its own sake” | Agrees with PDF Part D §8, in tension with Module 2.3 p.19 |
| P21 topic first | Viral Checklist #1 audience pain point; DS-000031 “Topic Selection — logon ko kis cheez mein waqai interest hai” | Agrees |
| P22 promise delivery | Brain v1 §13 “the intro confirms the decision… payoff creates satisfaction” | Agrees |

Viral-checklist items (pain point, transformation, emotion, contrarian, specificity, urgency, familiarity, motivate, concise, enhancer words, credibility hack) were tested in the 2026-11-12 forensic audit (`16_viral_checklist_score_vs_perf.csv`): the composite score showed **no** within-channel relationship with PI. That result is referenced, not re-run.
