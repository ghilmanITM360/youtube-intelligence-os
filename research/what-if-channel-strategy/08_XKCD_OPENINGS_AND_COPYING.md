# 08 — How xkcd's What If? opens its long videos, and why we don't copy it (2026-11-18)

**Evidence:** our own 83-script study, `research/what-if-scripts/analysis/`:
- `matrix.jsonl` (hook column)
- `audits/V###.md`

The study paraphrases the scripts and cites their locators; no transcript text is reproduced here. Counts are per long video (n = 43 of 83).

## 1. What they do (OBSERVED in the audits)

| Opening move | Long videos | What it is (paraphrase) |
|---|---|---|
| **Attributed question** | **37 / 43** | Names the real reader or viewer who sent the question, then reads the question out as the title states it |
| Second move after the question (varied; each type ≤ 2 videos) | — | Social proof ("lots of people ask this"), answer-first deflation, myth correction, premise-fencing (stating the rules), a comic literal reading, a shock flash-forward |
| Answer-first with the mechanism withheld | several (e.g. V001) | States the surprising one-word answer early, then makes you wait for *why* (V001 withholds it for ~19 paragraphs) |
| Call to action | **none in 38 / 43** | No "subscribe" asks; the video just ends |

**INTERPRETATION:**
- The attributed question is xkcd's **signature**, not a generic technique.
- It comes from their real format: *What If?* has always answered questions readers sent in, since the 2012 blog and the 2014 book.
- It works because a real person really asked. That creates social proof, and the joke can be "this person wanted to know something alarming".

## 2. What we do instead (already in the Day 1 script)

| xkcd | Unreasonably Exact | Evidence for our choice |
|---|---|---|
| Named reader's question | **Cold open on the most extreme end state**, then the title question | All 3 CT-scanned breakout competitors open on the end state (04 §3); framework FR-INTRO-02 |
| Monochrome stick figures, no on-screen labels | Original line art plus **SIMULATION / REAL DATA / THE MATH** tags and on-screen sources | Tracer's trust device (04 §2); our accuracy differentiator (06, 07) |
| Answer-first, mechanism withheld | We use answer-withholding too, through a persistent **tracker** (ladder, HUD) | Withholding is a generic storytelling technique; the tracker is from 04 |

**Later, legitimately:**
- Once real viewers send questions, crediting them by name is fair. It is a common practice (many channels do it), and not something xkcd owns.
- What we must never do is **invent** askers. That would be fabrication, and it contradicts a brand called "Exact".

## 3. Why we can't copy it

**What the law protects:**
- Copyright protects **expression**: the exact words, specific jokes, characters, drawings, and distinctive sequences of scenes.
- It does not protect **ideas or techniques**: "open with a question", "answer first", "use a ladder".

So we may use techniques. We may not reuse their scripts, phrasing, recurring jokes, stick-figure style, or their identity device (reader mail) in a way that makes us look like them.

**What happens if we do:**

| Consequence | How it happens | Source |
|---|---|---|
| **Video removed + copyright strike** | Munroe/xkcd files a takedown | YouTube Help: one strike removes the video and lasts 90 days (if Copyright School is completed); **3 strikes in 90 days → the channel is terminated and new channels can't be created** (https://support.google.com/youtube/answer/2814000) |
| **No monetisation for the whole channel** | Reviewers judge the content "reused" (lightly changed copies) or "inauthentic" (templated). This applies even with the original creator's permission | YouTube channel monetization policies (https://support.google.com/youtube/answer/1311392); "inauthentic content" renamed from "repetitious" on 15 July 2025 |
| **Our own gate blocks delivery** | Rule R1: ≥ 15% 5-gram overlap with any single transcript → FAIL; ≥ 5% → WARN | `docs/policies/AI-SLOP-RISK-RULES.md` |
| **Audience backlash** | xkcd's 1.38M subscribers know Munroe's voice; a copy gets called out in comments | INTERPRETATION (not measured) |
| **Head-to-head with the original** | A near-copy competes for the same viewers as the better-known original | HYPOTHESIS (not measured) |
| **Brand contradiction** | A channel whose promise is "exact, sourced, original" can't be built on someone else's writing | 07 §1 |

**Bottom line:** learn the *structure* (and we did, across 83 scripts). Write every word, joke and frame ourselves. That's what the slop gate, the IP boundary (01 §6) and this report enforce.
