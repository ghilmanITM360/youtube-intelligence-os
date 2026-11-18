# Phase A: Knowledge base forensic analysis (2026-11-18)

Labels: VERIFIED (read or fetched today) / REUSED (from earlier repo audits, not re-read today) / INFERRED / UNKNOWN. This file integrates the knowledge sources into the new-channel branch. It does not replace the earlier audits (paths in section 7).

## 1. What each source is

| Source | What it really is | Authority for us |
|---|---|---|
| Master Playbook PDF (`~/Downloads/YouTube_Automation_Complete_Master_Playbook.pdf`, 556 pp, compiled 2026-11-11, outside repo) | Part A to C: creator-course lessons, title formats, validation and script prompts (compiled, unmodified). Part D (pp. 554-556): new official-source appendix dated 2026-11-11 | Creative heuristics and prompt templates; only Part D cites official YouTube pages |
| DS-000011 (17 files) + supplement 2026-11-11 | Mixed creator-education and creative library (hook, packaging SOP, viral checklist, script/intro analyzers, algorithm guides, storytelling engines, image/video prompt guides, "Intelligence Brain v1") | Creative heuristics; not official YouTube material |
| DS-000018 | One third-party Google Doc snapshot with 63 creator-video transcript tabs about the "2026 algorithm" | Commentary. Earlier audit of 33 claims: 10 supported, 12 partial, 1 contradicted, 8 lacking primary support, 2 not verifiable |
| DS-000031 | Urdu/Hinglish creator lectures (topic selection, comments as research, post-hit behaviour) | Context only |
| Repo framework | `data/knowledge/reference_knowledge.db` (rule classes: creative heuristic, owner preference, platform claim, empirical hypothesis, tool-specific, superseded) and `scripts/check_slop_risk.py` | Mandatory for content plans and scripts |

## 2. Reading coverage (honest)

- Today: Playbook Part D read in full (3 pages); six official YouTube Help pages fetched (section 4); playbook text extraction re-done (92,260 words, 556 pages).
- Earlier, REUSED: `00_PROJECT_OVERVIEW/PDF_KNOWLEDGE_MAP.md` records pp. 1-108, 263-284, 318-352, 425-439 and 554-556 as read in full, and pp. 109-262, 285-317, 353-424, 440-553 as outline/rule level only (mostly prompt templates). I did not re-read those mid-sections today. Claim "whole PDF read" would be false.
- DS-000011 / DS-000018: not re-read today; rely on `DS-000011-DS-000018-DEEP-KNOWLEDGE-AUDIT.md` (2026-09-24) and the 2026-09-04 primary-source validation file.

## 3. What the Playbook gives us, by rule class

| Class | Content | Use for the new channel |
|---|---|---|
| Creative heuristic | Outlier transplant, title formats (100), five-part title engine, thumbnail one-idea rule, hook zones (0-5 s, 5-15 s, 30 s loop), but/therefore, engagement techniques, script audit checklists | Starting hypotheses to test on our own videos; never rules |
| Course heuristic that conflicts with official guidance | "8+ minute sweet spot" (Module 2.3), 10x outlier, 20+ outliers, 50+ topic ideas, A/B/C/D supply grades | Treated as working heuristics (Part D says so itself) |
| Prompt/workflow templates | Validators, repackage plugin, script engine, VO emotion, storyboard | Production tooling candidates (Phase J), gated by the slop checker |
| Official-source | Part D sections 1 to 10 | Anchors; re-verified below |

Known internal inconsistencies (from the earlier map): Method 2 lists 9 of 10 title formats; Method 4 supply threshold 50K+ vs 10K+; lesson numbering 2.3/2.4/2.5; several screenshot transcriptions with gaps.

## 4. Official claims re-verified today (2026-11-18)

Fetched from support.google.com. Pages show only a "2026 Google" footer, no last-updated date, except the monetization page, whose newest changelog entry is 2025-07-15.

| Claim | Result | Source |
|---|---|---|
| Half of channels/videos have impressions CTR between 2% and 10%; varies by content, audience, placement; videos under about a week old or under 100 views can be wider; high CTR with low view duration may signal clickbait | **VERIFIED**. Not a target; no universal benchmark | answer/7628154 |
| A/B tests: up to 3 titles and/or thumbnails; winner by watch-time share, not CTR; excluded: Shorts, scheduled lives, Premieres, made-for-kids, mature, private; desktop Studio only; about 2 weeks | **VERIFIED**. A video is a Short if 3 minutes or less and square or taller | answer/16391400 |
| Mid-rolls on monetized videos 8 minutes or longer; no guarantee an ad serves | **VERIFIED** (page has one small internal inconsistency about Shorts defaults) | answer/6175006 |
| Repetitive/mass-produced content is "inauthentic" and not monetizable; template-made AI content is listed explicitly; reused content needs significant original commentary; channel-level review | **VERIFIED** (renamed 2025-07-15). Allowed: AI for editing scripts or backgrounds if original insight is added | answer/1311392 |
| Browse, Suggested and Search are separate traffic sources; no new-channel guidance | **VERIFIED** definitions | answer/9314355 |
| AI disclosure required for realistic AI-generated or altered content (real person saying something they did not, altered real events, realistic scenes that did not occur); not required for non-realistic content, script/title/thumbnail help, or cloning your own voice | **VERIFIED**. Disclosure alone does not limit reach or monetization | answer/14328491 |

New findings that matter for a finance channel (not in Part D):
1. **AI-generated personas presenting as human experts who give financial advice are not monetizable** (the page's example is AI podcast hosts offering financial guidance). So we must not present an AI voice or avatar as an adviser; frame as explainer, not personal financial advice, and decide the voice and persona policy now (Phase F/J).
2. Content that **only reads out** text from websites or news feeds is not monetizable; news-driven finance videos need original analysis and sourcing.
3. Reviewers judge the **whole channel**: main theme, top and newest videos, titles, thumbnails, About. A templated 30-video calendar is itself a risk.

## 5. Contradictions, stale items, tests still open

- DS-000011 "10%+ CTR" goal vs official 2% to 10% median band: treat as creator target only (REUSED; confirmed today).
- Playbook "8+ min sweet spot" vs official: 8 minutes is an ad-eligibility rule only. Competitor data today supports length diversity: Monkey Economics 42 of 60 items are Shorts (41 typed SHORT plus one of 60 s or less); Casual Finance 185 of 223 are Shorts.
- No threshold in any source can be tested without our own YouTube Studio data: CTR, retention, impressions, traffic mix. Competitor public views are not CTR.
- DS-000018: stays context, not platform fact (REUSED). The one claim marked contradicted remains in the earlier audit file.
- Not re-run today: Viral-checklist score vs performance (earlier result: no within-channel relationship; REUSED).

## 6. Consequences for the new-channel decisions (HYPOTHESES to test, not conclusions)

1. Use the measurement dashboard in Part D section 10 from video 1 (Studio columns), and keep A/B title/thumbnail tests for long-form only (Shorts excluded).
2. Build originality in at channel level: distinct structure per video, own source work, no generic template look; run `scripts/check_slop_risk.py` on every script.
3. Decide a human-voice-or-clearly-labelled-narration policy before production; no AI "expert" persona.
4. Add a monetization-risk line to the topic scorecard: original analysis present? sources primary? not a news read-out?
5. Keep the playbook's 25-point scorecard (evidence freshness, multi-channel validation, distinct angle, research feasibility, audience fit) as one input to the 100-point scoring in Phase D.

## 7. Source paths (read-only)
- `research/finance-economics-channel-forensics/00_PROJECT_OVERVIEW/PDF_KNOWLEDGE_MAP.md`, `GLOBAL_KNOWLEDGE_MAP.md`
- `research/finance-economics-channel-forensics/02_SHARED_EVIDENCE/PDF_PRINCIPLE_EVALUATION.csv`, `04_FINAL_SYNTHESIS/PLAYBOOK_RUBRIC_SCORECARD_2026-11-14.md`
- `DS-000011-DS-000018-DEEP-KNOWLEDGE-AUDIT.md` (repo root), `data/intelligence/global/youtube-algorithm-primary-validation-2026-09-04.md`
- `data/raw/global-youtube-knowledge/DS-000011`, `DS-000018`, `DS-000011-supplement-2026-11-11`, `DS-000031`
- Official pages fetched 2026-11-18: answer ids 7628154, 16391400, 1311392, 6175006, 14328491, 9314355 on support.google.com/youtube
