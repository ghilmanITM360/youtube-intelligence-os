# YIOS Complete Creator Intelligence & Algorithm Master Guide

*Written 2026-10-26 on Machine B in read-only mode against `youtube-intelligence-os` (branch `research/finance-economics-intelligence`). Analyses and the source census ran at HEAD `d987510b`. During the session the concurrent Finance writer committed NICK_174–179, so the live HEAD at final validation is `df80644a`. Those commits change only the Finance audit ledger and projections; the catalog DBs and `data/raw/` are unchanged. This guide changed nothing in the repository. This guide is not committed and not published. Its supporting ledgers are in `ledger/` next to this file.*

---

## How to read this guide

This guide teaches two things together:

1. **How YouTube discovers and recommends videos.** This covers what YouTube says officially, what Google's research papers once described, and what nobody outside YouTube knows.
2. **How a creator turns an idea into a video people choose, keep watching, and are glad they watched.** This draws on the project's original creator manuals, which are checked against real YIOS data.

Each major topic follows the same seven steps:

| Step | What you get |
|---|---|
| 🟢 **Beginner** | Plain explanation, no jargon |
| 🔵 **Technical** | The mechanism, the metric definitions and the caveats |
| 📜 **Source teaching** | What the original YIOS manuals say, with file and page |
| 📊 **YIOS evidence** | What the project's own data supports or contradicts |
| ⚠️ **Uncertain / contradicted** | Open questions and conflicts |
| 🎬 **Original example** | A new, clearly labelled example written for this guide |
| 🧪 **Apply & test** | How to use it and how to tell whether it worked |

Short **Roman Urdu** summaries (🇵🇰) follow the key ideas.

### Evidence labels used throughout

| Label | Meaning |
|---|---|
| `OFFICIAL_CURRENT` | Stated on a current YouTube Help page, the official blog, or by named YouTube staff on an official channel. Checked on the stated date |
| `HISTORICAL_PLATFORM_RESEARCH` | Published by Google or YouTube researchers (2016–2019 papers). True of the system they described, not proof of today's system |
| `DIRECT_PROJECT_OBSERVATION` | Measured in a YIOS dataset, with a locator |
| `STATISTICAL_ASSOCIATION` | A tested association in YIOS data, with no causal claim |
| `REPLICATED_PATTERN` | An association that held on data it was not discovered in |
| `CREATIVE_HEURISTIC` | A craft rule. Can be useful, but is not shown to affect ranking |
| `PLAUSIBLE_HYPOTHESIS` | Consistent with the evidence and testable, but not tested |
| `CONTRADICTED` | Official documentation or YIOS data says otherwise |
| `UNKNOWN` | Cannot be verified from outside YouTube |

### Source codes

The 19 original knowledge sources are coded **S01–S19**. Pages are PDF pages, counted at each form-feed.

| Code | File (all under `data/raw/global-youtube-knowledge/`) | Size | What it actually is |
|---|---|---|---|
| S01 | `DS-000011/Engine-by-Engine Personality & Lens (Cinematic-Psychological Profiles).docx.pdf` | 3 pp | Persona descriptions for six AI "engines" |
| S02 | `DS-000011/Hook (1).pdf` | 58 pp | AI-chat summaries of about 9 hook videos, plus a third-party "Viral Hook Vault" |
| S03 | `DS-000011/Hook guide.pdf` | 58 pp | **Byte-identical text to S02.** Different PDF hash (`4bbe6c…` vs `4129b2…`). Counted once |
| S04 | `DS-000011/Intro Analyzer Prompts.docx (1).pdf` | 2 pp | Seven persona prompts for the first 0–30 s |
| S05 | `DS-000011/Packaging (Thumbnail_Title) - SOP(1).pdf` | 1 p | Packaging SOP |
| S06 | `DS-000011/Renae_Creative_Engine_v2.5_Unified_Intelligence_Blueprint.pdf` | 12 pp | AI-written "creative OS" for What If-style science videos; contains the 16 Commandments |
| S07 | `DS-000011/Script Analyzer.pdf` | 2 pp | Seven persona script-review prompts |
| S08 | `DS-000011/The Magic of 'BUT' and 'THEREFORE' in Storytelling.docx (1).pdf` | 3 pp | AI chat summarising the South Park BUT/THEREFORE rule and a "Fusion Framework v2.0" |
| S09 | `DS-000011/The Ultimate Nano-Banana Prompt Guide.docx` | DOCX | Image-generation prompt guide |
| S10 | `DS-000011/Ultimate Google VEO 3 Prompt Guide for VIRAL Videos.docx` | DOCX | AI summary of an external VEO 3 PDF that is not in the repo |
| S11 | `DS-000011/Viral Checklist.pdf` | 2 pp | 11-point checklist attributed to Codie Sanchez |
| S12 | `DS-000011/YouTube Title Analyzer — Natural Language Prompts (2).pdf` | 6 pp | Title angle examples, "viral title formulas" and seven persona prompts |
| S13 | `DS-000011/YouTube algorithm guide.docx (2).pdf` | 117 pp | NotNotAbu2 newsletter guides (pp 1–20), then about 45 ChatGPT breakdowns of creator videos (pp 20–117) |
| S14 | `DS-000011/YouTube_Intelligence_Brain_v1_Verified_Creator_OS.md` | 2,931 words | An already-calibrated creator system prompt (truth hierarchy, Phase A–J pipeline) |
| S15 | `DS-000011/new YT algorithms updates.pdf` | 45 pp | One long ChatGPT conversation advising a health/symptoms Shorts channel |
| S16 | `DS-000011/🎯 YouTube Video SEO – COMPLETE CHECKLIST DOCUMENT (1).pdf` | 13 pp | SEO checklist |
| S17 | `DS-000011/📜 Seven Engine Storytelling Analysis Prompts (16 Commandments Integrated).pdf` | 6 pp | Persona prompts and the full 16 Commandments |
| S18 | `DS-000031/creator-strategy-audience-psychology-experimentation-corpus.txt` | 1,426 lines | Urdu/Roman-Urdu/English creator posts: feedback loops, niche bending, psychology arbitrage, competitor analysis |
| S19 | `DS-000018/2026 Algorithm Update - Google Docs tab snapshot.zip` | 63 tabs, 245,901 words | Creator video transcripts. Tab 39 is YouTube's Todd Beaupré on Creator Insider |

Official references **[S1]–[S18]** and **[T39]** are listed with access dates in `ledger/EXTERNAL_SOURCES.csv` and Part X. Square brackets mean an official reference; plain codes (S01–S19) mean an original YIOS source.

> **What this guide is not.** It is not a concatenation of earlier reports. The earlier same-day package `YIOS-Algorithm-Audit-2026-10-26/` was used only for its *reproducible statistical receipts*, and its QA script was re-run today: all checks PASS, with the repository and DB hashes unchanged. Every creator rule here was re-read from the original files.

---

# PART I — Complete Beginner Course

## I.1 What is YouTube actually trying to do?

🟢 **Beginner.** YouTube is a very large matching service. Every time someone opens the app, YouTube has to pick, out of millions of videos, the few that *this* person is most likely to watch and be glad they watched. It earns money when people keep coming back, so the goal is that you leave satisfied and come back tomorrow. "The algorithm" is not a judge that rates your video once. It makes billions of small predictions, one viewer at a time.

🔵 **Technical.**
- YouTube describes two goals: help each viewer find videos they want to watch, and maximise **long-term viewer satisfaction**. It says the system "doesn't follow a set formula" [S1].
- It names three groups of performance evidence: **Appeal** (does the right viewer choose it?), **Engagement** (do they keep watching?) and **Satisfaction** (were they glad?) [S3].
- YouTube's senior director of growth and discovery called the "north star" **long-term user value**. He said "no metric on its own is a good indicator of value", and that the weighting of signals is not the same for everyone, nor for the same viewer at all times [T39, ch. 5].
- Surveys exist because "not all time spent is equally valuable" [S2; S10; T39].

🇵🇰 *YouTube ka maqsad sirf views nahi. Har viewer ko woh video dikhana hai jo usay pasand aaye aur jis ke baad woh dobara YouTube par aaye. Koi aik "score" ya formula nahi.*

## I.2 How does a viewer discover a video?

🟢 **Beginner.** People find videos in a few different "rooms":

| Surface | What decides what appears (official) | Label |
|---|---|---|
| **Home / Browse** | Mainly *your* watch history | `OFFICIAL_CURRENT` [S2] |
| **Suggested / Up Next** | Mainly the video you are watching now | `OFFICIAL_CURRENT` [S2] |
| **Search** | Relevance to the query (title, description, content), engagement for that query, and quality (expertise, authoritativeness, trustworthiness) | `OFFICIAL_CURRENT` [S6]. Search results are "not a list of the most-viewed" [S5] |
| **Shorts feed** | Personalised to what YouTube thinks you want next, swipe by swipe | `OFFICIAL_CURRENT` [S2] |
| **Subscriptions / notifications** | Channels you follow. YouTube calls this the slice "not primarily influenced by an algorithm" | `OFFICIAL_CURRENT` (spoken) [T39 ch. 12] |

🔵 **Technical.** Recommendations are **pulled** for the viewer, not **pushed** by the video. The system activates "when a viewer opens their app or turns on their TV". It gathers *candidate* videos and *ranks* them for that viewer, so "each viewer gets a different ranking" [T39 ch. 2]. Google's 2016 paper described the same two stages: candidate generation, then ranking [S11, `HISTORICAL_PLATFORM_RESEARCH`]. The 2019 papers added multi-objective ranking, position-bias correction and exploration [S12; S13]. Current weights and features are **not public** (`UNKNOWN`).

🇵🇰 *Video ko YouTube "dhakelta" nahi. Har viewer ke liye jab woh app kholta hai, us waqt candidate videos chuni jaati hain aur us viewer ke liye rank hoti hain.*

## I.3 The metrics, defined properly

| Metric | Plain meaning | Precise definition and trap |
|---|---|---|
| **Impressions** | How often your thumbnail was shown | Counted thumbnail displays on YouTube surfaces. External embeds and some surfaces are not counted [S7] |
| **CTR** | Of those showings, how often someone clicked | Views from impressions ÷ impressions. Half of all channels' videos sit between **2% and 10%** [S7]. CTR *falls* as a video reaches broader, colder audiences [S7; T39 ch. 5]. **Not** a quality score |
| **Views** | Plays counted by YouTube | Long-form and Shorts views are different units. Do not compare them [prior YIOS audit] |
| **Watch time** | Total minutes watched | YouTube looks at absolute *and* relative time. 5 minutes of a 2-hour video means something different from 5 minutes of a 5-minute video [T39 ch. 5] |
| **AVD** (average view duration) | Average minutes watched per view | Compare only with *your* similar-length videos [T39 ch. 5] |
| **APV** (average percentage viewed) | Average share of the video watched | Short loops can exceed 100% on Shorts. In DYH data an APV of 126.6% coexisted with weak acceptance (see III.6) |
| **Audience retention curve** | The share still watching at each moment | Dips show *where* viewers left, not *why* |
| **Stayed to watch** (Shorts) | Share who did not swipe away at the start | Shorts-specific [S8] |
| **Returning viewers** | Viewers who came back | YouTube staff describe "a user coming back more often and watching content they report as valued" as a satisfaction signal [S13 p70–72 quoting Beaupré via vidIQ; consistent with T39] |
| **Satisfaction** | Was the time well spent? | Surveys, likes, dislikes, "Not interested", comments. None is sufficient alone [S2; T39] |
| **Traffic source** | Where the views came from | Browse, Suggested, Search, Shorts feed, Channel pages, External, and others. CTR differs by source [S7] |

🟢 **Beginner trap.** A "good CTR" with viewers leaving after 20 seconds is a **broken promise**, not a success. YouTube's own Help page warns about this clickbait pattern [S7].

🇵🇰 *CTR, retention, aur satisfaction teen alag sawaal hain: kya log ruke, kya dekhte rahe, kya khush hue. Kisi aik number ko "pass/fail" mat samjhein.*

## I.4 How a new creator makes a video, from scratch

The whole system on one line:

```
Audience → Demand → Channel fit → Story angle → Title + thumbnail → Hook → Script
   → Storyboard → Visual production → Narration/edit → Publish → Analytics → Experiment → Next video
```

The stages explained:

1. **Know one viewer.** Write down who they are and the situation they are in, for example "lying in bed at night, worried about a symptom" (S15 p7–10).
2. **Find proven demand.** Look for videos that outperform *their own channel's* normal (S14 §4A; S18 L126–188).
3. **Check channel fit.** Would this viewer expect it from you? (S18 Niche Bending.)
4. **Pick a story angle,** not just a topic (S15 p2–4; S14 §4B).
5. **Design the title and thumbnail before filming,** as one promise (S14 §4C; S15 p27).
6. **Write a hook** that confirms that promise in the first seconds (S02; S14 §4D; [S3]).
7. **Build the script on cause and effect** (BUT/THEREFORE), escalation and payoff (S08; S17).
8. **Plan visuals** that *prove* or *show consequences*, not decorations (S14 §4H; YIOS What If audit, Part V.5).
9. **Publish honestly.** Use accurate metadata, chapters only if they help, end screens and a playlist (S14 §4I; [S17], [S14]).
10. **Read analytics by layer.** No traffic means distribution; traffic but no click means packaging; clicks but no watching means content; clicks and watching means scale (S18 L262–343).
11. **Change one thing at a time** and record what you learned (S18 L6–89; S14 §4J).

The rest of the guide unpacks each stage.

---

# PART II — The Original Source Knowledge, Explained

This part gives each original framework in plain language: what it teaches, where it says so, why the author believes it works, and what kind of claim it is. Overlapping sources are merged, but each distinctive insight is kept with its locator.

## II.0 First, what kind of documents these are (source criticism)

🟢 Before trusting a rule, ask who wrote it and how they know.

🔵 A close reading of all 19 sources shows five very different document types. This matters more than any single rule.

| Type | Sources | Implication |
|---|---|---|
| **Creator SOP or checklist (human-written)** | S05 Packaging SOP, S11 Viral Checklist (Codie Sanchez), S16 SEO checklist, S13 pp 1–20 (NotNotAbu2 guides, with repeated "FREE call" sales prompts) | Practitioner opinion. No data or method given. S13's guides double as sales funnels |
| **AI-chat responses summarising creators' videos** | S02/S03 Hook ("Excellent — this is a goldmine…"), S13 pp 20–117 ("ChatGPT said:"), S15 (one long ChatGPT conversation), S08, S10 | **Second-hand, filtered by an LLM.** The LLM often adds its own invented numbers. For example "Keep CTR between 9–12%" (S13 p59), "Recommendation Probability Score" (S13 p48), "Hook³ × Retention × Emotional Response ÷ Swipe Rate" (S13 p92), and an illustrative "3–4 word overlays lifted 3s hold by 28–62%" (S02 p44) that is a template sentence, **not a measurement** |
| **AI-authored "operating systems"** | S06 Renae v2.5 ("Got it✅ — you're asking for…"), S14 Verified Creator OS | Normative design documents. S14 is already self-correcting: it has a truth hierarchy, bans invented thresholds, and treats lenses as "internal lenses, not … separate external models" |
| **Persona prompt libraries** | S01, S04, S07, S12 pp 3–6, S17 | Tools for producing critiques. Persona labels are inconsistent: Gemini is a "Story Architect", "Mythic Storyteller", "Story Surgeon", "Narrative Surgeon" and "Narrative-Algorithm Fusion" in different files. **Seven persona outputs are not seven independent experts** (claim C38) |
| **Transcripts and creator posts** | S18 (DS-000031), S19 (DS-000018) | Primary record of *what creators said*. T39 is the one first-party YouTube voice |

> **Biggest single finding of the source audit.** Most numeric thresholds circulating in YIOS's knowledge base come from AI paraphrase or creator folklore, not from YouTube or from data. Examples: 10% CTR, 20–30-second resets, 55/60/70-character titles, "first 60 minutes", "50–100 uploads". The same 117-page file (S13) gives CTR "targets" of 1–3%, 5%, 7%, 9–12% and ≥10%, and ideal lengths of "3–10 min is dying", "8+ min", "10–12 min", "14–20 min", "15–30 min" and "20–60 min". Contradiction at this scale is itself evidence that none of these is a platform rule.

🇵🇰 *Zyada tar "rules" (10% CTR, har 20 second reset, 60 character title) AI ke paraphrase ya creators ki raaye hain. YouTube ne aisa koi number nahi diya. Aik hi file mein CTR ke 5 mukhtalif "targets" likhe hain.*

---

## II.A Recommendation system (as the sources teach it)

📜 **Source teaching (merged).**
- **"Pull, not push" / "prediction engine, not distribution channel."** S18 L2 (Urdu lecture, 3:16–4:15): "YouTube is a prediction engine, not a distribution channel". It looks at the user profile, time, location, device and watch duration, then matches "right audience" with "right video". S13 pp 20–23 and 33–36 (ChatGPT summaries of the Beaupré/Ritchie interview) say the same.
- **Satisfaction is the core.** S18 L2 (4:23–6:52): "Satisfaction is the only algorithm". In order: click → stayed → "did it lead to a binge session" (your video extended the viewer's session even if they then watched other creators) → "did they come back". "Views are vanity metrics". S12 p1: "end-of-watch" signals (good abandonment, watching another from your channel, sharing) versus "Not interested", dislike or "immediately search[ing] for the exact same topic again". S12 also mentions satisfaction surveys ("If you get 1 star (often due to clickbait), your reach is suffocated") and retention *shape* (rewinding is good; frantic skipping is bad).
- **Two-stage architecture.** S18 L2 (7:14–8:12): candidate generation like a "nationwide entry test" shortlist, then ranking. S13 pp 38–39 says the same.
- **Context matters.** The time of day and device matter: TV at night versus phone in the morning (S13 p21).
- **No single metric.** S13 p21: "There's no single number" (attributed to Ritchie/Beaupré).
- **Testing on small groups.** S13 pp 4–5, 24, 40–41, 49–50, 66, 88–91: "YouTube will quietly test your video with a tiny audience". Group sizes are given as 5–10, ~100, 200–2,000 or 1,000 viewers depending on the speaker.
- **Channel "trust score", "warm-up", "zero-view jail", "valley of death", "escape velocity after 20–30 uploads".** S13 pp 28–31, 36–38, 49, 55–57, 87–88; S15 p36.

🔵 **What official evidence says** (detailed in Part IV):
- Pull, two stages, per-viewer ranking, context, satisfaction surveys and no fixed weights are all `OFFICIAL_CURRENT` [S1; S2; T39] or `HISTORICAL_PLATFORM_RESEARCH` [S11].
- "Each viewer gets a different ranking" and "it can learn that for subscribers, this video is not … performing well and for people who haven't watched the channel, it is" [T39 ch. 3]. This **contradicts** the folk rule that a weak first hour from subscribers "kills" a video.
- "We're not going to decide just based on the first hour or first 10,000 people" [T39 ch. 12]. Evergreen videos can get "the majority of their views … a month or … later" [T39 ch. 4].
- **There is no official "trust score."** The interview calls the system "very video centric" and says it is not "trying to find a single category for your content" [T39 ch. 6]. "Trust score" claims (C22) are `UNKNOWN` and must not be used as facts.
- The test-group sizes (5, 100, 1,000…) are `UNKNOWN`. They are mutually inconsistent and unsourced.

📊 **YIOS evidence.**
- Lifetime views/day keep accruing with age within channels. The median slope of log views/day against log age is 0.343 for the Finance originals and 0.574 across niches. A video's fate is not sealed in its first hours, consistent with [T39].
- Channel identity explains **37.8%** (Finance) to **57.5%** (all registry niches) of the variance in log views/day. *Which channel* a video is on matters statistically. This is an association, and it is consistent with audience-based pull.

🎬 **Original example (new).** A viewer who watched three rent-vs-buy calculators this week opens YouTube on a TV at 9 pm. The candidate pool now includes long personal-finance explainers. Your 18-minute "Rent vs Buy: The Real 10-Year Math" can rank for *this* viewer even if your subscribers mostly ignored it.

🧪 **Apply & test.**
- Judge a video against your own similar videos at the same age, not against an absolute bar.
- Use **Subscriptions-feed CTR** as a clean read of content appeal to your existing audience. Targeting doesn't change there, so differences between videos are about the content [T39 ch. 12].

🇵🇰 *Pehle ghante ke views se video ka faisla nahi hota. YouTube har audience (subscriber, naya viewer) ke liye alag seekhta hai. "Trust score" ka koi official saboot nahi.*

---

## II.B Viewer psychology

📜 **Source teaching.**
- **Curiosity gap / open loops.** S02 pp 1–5, S08 p2 (cites Loewenstein), S06 p6, S15 pp 16–20: "Human brain hates information gaps." A hook is "a sentence that creates one or more questions the viewer cannot answer" (S02 p6). "Make the gap, then fill the gap."
- **Pattern interruption / prediction error.** The Scroll-Stop Interjection "triggers the brain's prediction error system" (S02 p2).
- **Relevance and identity.** "Oh, this is about me" (S02 p1). "Identity" angle: "This explains YOU" (S15 p2). Watching situation versus demographics (S15 p7): "Your viewer is not a 'woman 35–50'… Your viewer is: Someone lying in bed at night worried about their health."
- **Familiarity ("cult hopping").** Use familiar brands and people to lower cognitive friction (S02 p4). S11 #11 "Credibility hack (Elon Musk, Taylor Swift, Apple)".
- **Benefit framing.** "If you want better sleep, you need magnesium" beats "You should take magnesium" (S02 p4).
- **Cognitive load.** Staccato sentences, the "12-year-old" test (S17 #13; S01 Google AI Studio persona), the "grandma test" (S02 p42).
- **Emotion over information.** S08 p2, S15 p21: "Emotion > Information". S06 p7 "Emotional Retention Sequence": Curiosity → Fear → Awe → Humor → Empathy → Closure.
- **Neurochemical language.** "dopamine bursts" (S01 p2), "dopamine–oxytocin cycles" (S06 p7), "mirror neurons" (S08 p3).
- **Audience sentence.** S18 L189–224: "My audience wants to watch ___ because they want to feel ___."
- **Silent majority.** Most viewers never comment, so analytics show behaviour that comments don't (S15 p6; S18 L189–224).

🔵 **Assessment.**
- The curiosity gap is a real research construct: Loewenstein's (1994) information-gap theory. Relevance and cognitive load are well-established principles of communication.
- **But** none of the sources tests them on YouTube outcomes. The neurochemical claims (dopamine, oxytocin, mirror neurons) are pop-neuroscience framing with no evidence in these documents (C39, `UNKNOWN`). Treat them as metaphors, never as mechanisms.
- "Emotion > Information" is a `CREATIVE_HEURISTIC`. YouTube's search quality signal explicitly values expertise and trustworthiness [S6], so for health and finance, *information quality is part of satisfaction*.

📊 **YIOS evidence.**
- Title-level "curiosity gap" wording was associated with **1.35×** peer-relative performance in the original 966 Finance videos (q = 0.042). On 418 videos from unseen channels it was **0.96×** (`SUGGESTIVE_NOT_ROBUST`, not replicated).
- "Threat/fear" wording was **0.75×** in the original set and **1.10×** in replication. That is no stable direction (C06, C07).
- Psychology *works through specific stories for specific audiences*. It is not a set of portable trigger words.

⚠️ **Contradiction.** S15 pp 19–25 calls "self-diagnosis anxiety" the "strongest psychological trigger" to exploit for a health channel. S14 §6 forbids "fear without proportional context" and "medical panic". **S14 governs** (claim C48). The YIOS medical case study (Part V.6) shows why.

🎬 **Example (new).**
- Weak: "Benefits of walking after meals."
- Situation-led: "That 2 a.m. sugar spike: what a 10-minute walk after dinner actually changes."
- The second version names a moment the viewer recognises and a concrete outcome, and makes no promise of a cure.

🧪 **Test.** On an eligible long-form video, use native **Test & Compare** [S9]. Compare a benefit-framed title with a situation-framed title, keeping the thumbnail fixed. The winner is decided by watch-time share, which already penalises empty curiosity.

🇵🇰 *Curiosity, relevance, aur kam cognitive load asli psychology hain. Magar "dopamine/oxytocin" sirf misaal hain, saboot nahi. Hamare data mein "curiosity" titles ka asar naye channels par dobara nazar nahi aaya.*

---

## II.C Audience and topic research

📜 **Source teaching.**
- **Outliers relative to a channel's own normal** reveal demand. S14 §4A step 5; S13 p4: watch 5–10 competitors, take their last 20 uploads, isolate the 2–3 outliers, and ask *why* (packaging? topic? stakes? length?). S13 p35: a vidIQ filter under 25k subscribers to find small-channel outliers.
- **An outlier is a demand signal, not a video.** S18 L126–188 (Urdu):
  - Extract the hidden demand: *famous person + sudden fall + desire to know the real cause*.
  - Then open "doors": Before, After, Why, What Changed, Biggest Mistake, Hidden Cause, Consequence, Rival, Replacement, Comeback, Downfall, What Everyone Missed.
  - Turn the outlier's *consequence* into the topic ("The Role That Made Him Famous" → "The Role He Could Never Escape").
  - Ask "what is the viewer's next question after this video?"
  - "One outlier often yields 10–20 good angles."
- **Topic demand versus angle demand; market cap.** S14 §4A step 6–7: niche-only, adjacent-audience or broad-human appeal. S15 p27 (via the absent MrBeast playbook): "Choose topics based on interest demand, not personal interest".
- **Niche research.** S18 L227–259:
  - There is no perfect niche, and competition can mean demand.
  - One viral video doesn't prove a niche; a pattern does.
  - Can you list 30–50 topics now?
  - Research 3–5 days, list 20–30 topics, commit, and don't switch niche weekly.
  - Fix topic, title, thumbnail and hook before blaming the niche.
- **Audience research method.** S18 L189–224: study winners *and* flops, read comments for requested follow-ups, look at CTR by topic, first-30-s retention, drop points, returning viewers, and subscribers gained per topic.
- **Competitor analysis, five things.** S18 L1194 and L1197–1423:
  1. Topic selection: repeated outperformers versus the channel average.
  2. Promise: the psychology, not the wording.
  3. Comments: content gaps.
  4. Retention craft: timestamp the hook, the main-story start, loop opens and answers. "You can't see the competitor's retention graph — you infer."
  5. Upload strategy after a hit: does the creator follow up with a cluster?
- **Critique of copy-led analysis.** S18 L399–464: competitor data tells you "what worked yesterday". Audience psychology suggests what may work tomorrow.
- **Audience radar account.** S13 pp 34–35: a fresh account trained on 10+ niche videos shows the niche's homepage.
- **Narrative Debt Mining.** S18 L467–555: half-known stories. Four types: Missing Middle, Unexplained Disappearance, Unexplained Change, Known Outcome/Unknown Cause.

🔵 **Technical caveat.**
- An "outlier" must be defined against a comparable baseline: the same channel, the same format and a similar age.
- Raw view counts confound channel size, video age and format. The YIOS peer-ratio method fixes this. It compares views/day with the median of up to 10 nearest-age peers on the same channel, format and snapshot, with peers 0.5–2× the target's age, at least 5 peers and the target at least 7 days old. It reproduces the stored ratios exactly (max relative difference 7.1e-5).

📊 **YIOS evidence.**
- Hits concentrate: the top 10% of a channel's videos take a median **66.9%** of its views, across 33 registry channels with dated snapshots (`REPLICATED_PATTERN` across channels).
- Some *concepts* won on two different channels. For example "Renting vs Buying — The Real Math" scored 350× and 297× peer ratio, and "compounding number" titles 51× and 67×. `PLAUSIBLE_HYPOTHESIS`: concrete decision questions with checkable numbers travel.
- But **identical titles also failed elsewhere.** "Your Life If You Start Building Wealth in Your 30s" scored 14.8× on one channel and 0.14× on another. "How Banks Treat You at Every Level of Wealth" scored 159× and 0.07×. Outliers are channel-and-audience-specific signals, not transferable recipes (C25).

🎬 **Example (new).**
1. A finance competitor's normal video gets 0.8× its peers, but "Why Your 401(k) Match Is Free Money" gets 6×.
2. Hidden demand: *a benefit I'm wasting without knowing*.
3. New doors: "The 401(k) Mistake That Costs New Hires $40k by 60", "What Happens to Your Match If You Quit in Year Two", "Roth vs Match: Which Dollar Comes First?".
4. Each must be checked for real payoff (Before → Event → After; S18 L979–1189).

🧪 **Test.**
- Treat a batch of 3–5 videos as one hypothesis, for example *hidden-cost decisions* (S18 Feedback Loop).
- Pre-register what "worked" means: the peer ratio on your channel at day 28, and 30-s retention against your median.

🇵🇰 *Outlier ko copy na karein. Us ke peeche ki "demand" samjhein, phir naye angle banayein. Hamare data mein aik hi title aik channel par 159× aur doosre par 0.07× gaya.*

---

## II.D Story angles

📜 **Source teaching.**
- **Same subject, different story.** S12 p1: ten "Every Time Tom Brady…" titles. S15 p1 maps each title to a psychological hook and to who clicks: underdog, comeback, revenge, shock, validation, drama, controversy, conflict, David vs Goliath, mystery. "Saturation doesn't happen at the topic level. It happens at the angle level."
- **Five universal angles** (S15 p2): Revelation, Danger, Identity, Contradiction, Prediction.
- **Twelve lenses** (S15 p3, Story Angle Generator prompt): underdog, hidden danger, identity, revenge/consequences, secret doctors don't say, unknowing mistake, time running out, myth vs reality, prediction, social comparison, body signal/warning, irreversible damage. Rules: no "5 symptoms of…", no repeated structures, no "shocking/amazing", "titles should feel like documentaries, not blog posts", and paste a *raw concept*, not a finished title.
- **Fifteen angle lenses** (S14 §4B): revelation, hidden danger, identity, mistake, contradiction, prediction, consequence, comeback, transformation, social comparison, warning signal, myth vs reality, investigation, experience/POV, completeness. For each angle record: core event, emotional trigger, viewer question, promised payoff, visual proof opportunity, factual risk. "Reject angles that cannot support a truthful and satisfying video."
- **Viewer-role verbs** (S12 p1): "Should Not Exist" → discovering; "Every Rank" → observing; "What Happened to the Family" → investigating; "WORST" → witnessing; "What It Feels Like" → experiencing; "POV" → deciding; "[Country] Just…" → reacting.
- **Niche Bending** (S18 L558–804): Core Niche + Adjacent Interest = Bent Niche. Five types:
  - Topic bending.
  - Emotional bending ("Why Nobody Really Knew Sonny Liston").
  - Audience bending ("23,000 Casualties in 8 Hours: America's Bloodiest Day Explained").
  - Perspective bending.
  - Format bending.
  - Test sentence: "This is a ___ channel, but we explore it through ___."
- **Psychology Arbitrage** (S18 L808–978): Outlier → Why click? → Psychology → Matching true story → New title.

🔵 **Assessment.** Angle generation is a `CREATIVE_HEURISTIC` and arguably the most valuable idea in the corpus. It moves effort from cosmetic rewording to *different promises*. Its risk is factual. "Irreversible damage", "secret doctors don't say" and "time running out" are three of S15's twelve lenses that are dangerous in medicine unless they are true (see the S14 §6 safeguards).

📊 **YIOS evidence.** Concrete decision angles (rent vs buy, compounding numbers) recur as cross-channel winners (`PLAUSIBLE_HYPOTHESIS`). No angle *family* has been tested with blind coding yet. The analyst prose in `VIDEO_AUDIT_966.jsonl` quotes each video's performance tier, so angle labels derived from it are **outcome-contaminated** (`DIRECT_PROJECT_OBSERVATION` of a method flaw).

🎬 **Example (new).** One core event: *mortgage rates fell 1 point*. Five angles:
- Revelation: "What the Rate Drop Doesn't Tell You About Your Payment".
- Danger: "The Refinance Trap Hiding in a Lower Rate".
- Identity: "If You Bought in 2023, This Rate Drop Is About You".
- Contradiction: "Why a Lower Rate Can Cost You More".
- Prediction: "What Your Payment Looks Like If Rates Fall Again".

Each must have a real worked calculation as its payoff.

🧪 **Test.** Use the S18 L979–1189 validation:
- Can you write 20 non-forced titles?
- Are 30+ real topics available?
- Does the psychology transfer?
- Is there a real payoff?
- Does it work with second-tier names, not only celebrities?

Then run 3–5 pilots before committing a channel.

🇵🇰 *Topic aik, kahaniyaan bohot. Saturation topic mein nahi, angle mein hoti hai. Har angle ka sach hona aur payoff hona lazmi hai.*

---

## II.E Packaging (title and thumbnail)

📜 **Source teaching (merged; locators in brackets).**

| Principle | Sources | Notes |
|---|---|---|
| Viewers decide in milliseconds; thumbnail first, then title | S05 p1; S12 p1 | |
| Know who must click; research packaging in similar niches | S05 steps 1–2; S16 p3; S13 pp 2, 19 | |
| Be genuine; "Realistic & Genuine packaging = more clicks"; "Hitting Audience Desire > Design" | S05 steps 3, 5 | "A mediocrely designed packaging that makes our target viewers stop… is always better" |
| Packaging should signal the video's type and length | S05 step 6 | A 10-minute video shouldn't look like a documentary |
| "Did the viewer enjoy your last video? It impacts the click" | S05 step 7 | Consistent with returning-viewer logic |
| Thumbnail: bright natural colours, big bold few words, ONE big idea, believable | S05 4a; S16 p8 "3–5 words"; S15 p40 "1–4 bold words"; S14 §4C "one dominant idea at mobile size" | |
| Title: one sentence; broad topic → short title, narrow → specific | S05 4b | |
| Title–thumbnail as **one system**; thumbnail **complements**, doesn't repeat | S14 §4C | |
| Composition: rule of thirds, centred symmetry, leading lines, triangle, S-curve, golden ratio — chosen by narrative purpose | S14 §4C | |
| Thumbnail = "compressed story": problem, mystery, stakes, **not the answer** | S15 pp 20–21; S08 p2; S06 p6 | "If the thumbnail answers the question → CTR drops" |
| Thumbnail-first ideation ("if it can't make a clickable thumbnail, the video will fail") | S15 p27 (MrBeast playbook, absent) | |
| Key info in the first 55 characters | S12 pp 3–4 | |
| Under 60 characters; keyword first; formula Keyword + Benefit + Curiosity | S16 pp 4–5 | |
| ~70 characters | S13 p47 | |
| Don't force titles under an arbitrary character count | S14 §11 | Contradicts the three rows above |
| "No face" is a mistake | S16 p8 | vs S14: face only "when emotionally truthful and relevant" |
| Make three *meaningfully different* packaging hypotheses | S14 §4C | |
| Seven "viral title formulas": Every [X]; What it feels like; POV; Should not exist; What happened to the family; WORST; [X] Just… | S12 pp 1–2; S15 pp 39–40 | "going viral right now" — no data |
| Goal 10%+ CTR | S05 | See C01 |

🔵 **Technical and official.**
- Titles, thumbnails and descriptions matter more than tags [S17].
- **Test & Compare** runs up to three variants on eligible long-form videos for up to two weeks. The winner is chosen by **watch-time share**, not CTR [S9]. This official choice confirms that packaging is judged by what happens *after* the click.
- CTR depends on traffic source and audience breadth. Small differences on small impression bases are noise [S7].
- The YIOS thumbnail-forensics report (`docs/research/thumbnail-forensics-2026-10-02/REPORT.md`) records the same official reading: "The often-cited 2–10% range is descriptive… not a target".

📊 **YIOS evidence.**
- **No historical thumbnail exists** for competitor videos. Every record says `historical_design: UNKNOWN`. Current thumbnails may differ from the ones shown at upload, so YIOS cannot test thumbnail effects on competitors.
- Title-wording tests (H01–H10) found no replicated effect:
  - Money amount 1.07× (q = 0.742).
  - Question mark 1.15× (q = 0.74).
  - List count 1.24× (q = 0.369; 0.76× in replication).
  - First person 0.80× (1.42× in replication).
- **First-party (owned channel "Decode Your Heart – Dr. Rehan", DS-000032, derived data, 2026-09-27):**
  - Lifetime thumbnail CTR **3.0%** on 36,159 impressions.
  - CTR by source: Search 2.71%, Suggested 2.9%, Browse 3.28%, Channel pages 7.03%.
  - In one matched pair, a specific lab-test package (`BCNWQ3uuSuE`, CTR 4.2%, 30-s retention 60.5%) beat a broad warning package (`SBrMW71O69U`, 2.87%, 38.46%). Confidence: MEDIUM. Impressions and video ages differ.
  - `7MXBh2hjfto` is a packaging defect: the title promised an appetite-suppressant comparison, the content debunked a cancer myth.

⚠️ **Uncertain.** Whether faces, colour or word count matter is **unknown** for YIOS channels. The only valid test is native Test & Compare on an owned eligible video.

🎬 **Example (new) — three meaningfully different packages for one finance video:**
- **A, Decision + number:** title "Rent vs Buy in 2027: The 10-Year Math Nobody Shows You"; thumbnail with two houses and a single red "$118,000?" with a question mark.
- **B, Identity:** title "If You Earn $70k, Here's Whether Buying Makes Sense"; thumbnail of a calculator held by a person in a rental, with "$70K" written on it.
- **C, Contradiction:** title "Why Renting Can Make You Richer (with real numbers)"; thumbnail of a split RENT ↑ / BUY ↓ arrow chart.

All three promise the same calculation, so the promise stays honest.

🧪 **Test.**
- Run A, B and C in Test & Compare.
- Record the variant files and hashes, start and end time, and the native verdict (Winner / Performed same / Inconclusive).
- Keep inconclusive results as inconclusive. Don't stop early.
- A paired title+thumbnail test measures the *package*, not each part separately.

🇵🇰 *Title aur thumbnail aik hi wada hain. YouTube ka apna A/B test jeetne wala watch-time share se chunta hai, CTR se nahi. 10% CTR koi official target nahi; hamare apne channel ka lifetime CTR 3.0% hai.*

---

## II.F Hooks and introductions

📜 **Source teaching.**
- **Three-step hook** (S02 pp 1–5, "Mega Tip"):
  1. **Context Lean**: topic clarity plus relevance ("Oh, this is about me").
  2. **Scroll-Stop Interjection**: a contrastive word (but / however / yet) that breaks the expected direction, "like running into a glass wall".
  3. **Contrarian Snapback**: an on-topic twist that reverses the assumption.
  - Example: Vegas Sphere: "biggest screen ever built…" → "but the screen is actually the least impressive part" → "the most impressive part is the audio".
  - Equivalent forms: Headline → Shocker → Misdirection (S02 p33), and Polarizing statement → Importance/credibility → Payoff promise (S02 p42).
- **Enhancers:**
  - Visual hooks: 3–5 bold words on screen, "just-enough motion", visual + text + voice aligned.
  - Benefit-first framing.
  - Cult hopping.
  - Compressed speed to value: "within 4 seconds (short form) or 1–2 minutes (long form)".
  - Staccato sentences (S02 pp 3–5).
- **Hook formulas** (S02 pp 10–14): Mistake Reveal, Counterintuitive Truth, Transformation Tease, Urgent Warning, Secret Reveal. **Six archetypes** (S02 pp 37–41): Fortune Teller, Experimenter, Teacher, Magician, Investigator, Contrarian. **Six "power words"** (S02 pp 45–48): Subject, Action, Objective, Contrast, (Proof), (Time).
- **Four components aligned:** spoken, visual, text, audio. "The difference between 500 and 500,000 views is max alignment among all four" (S02 p38, creator claim). There is also a **V–A–V intake model**: visual and text first, then audio, then back to the visual to confirm.
- **Key-visual-first workflow** (S02 p39): if you can't show a visual that proves the claim in 3–5 s, "kill the idea".
- **Visual hook library** (S02 pp 14–18): pop-in, title card, micro-montage, walk-in, transition on "but", match cut, hands POV, running, bird's-eye, disaster.
- **Integrity:**
  - "Pay off the exact curiosity you created" (S02 p8).
  - "If the snapback teases a different topic, viewers may itch to bail" (S02 p7).
  - Pitfalls: an overlay that reveals the twist, over-editing the first second, a shocker with no proof path (S02 p36).
- **S14 §4D hook families:** contrarian, curiosity, action, novel-insight, live demonstration, skill showcase, challenge, amazement, shock (responsibly), pain-to-transformation, identity, prediction.
  - Enhancers: proof early, short sentences, an early value sample, the promise unmistakably present, "one primary loop and, at most, one secondary loop".
  - "Never begin with a generic greeting, biography, long disclaimer, or topic definition unless essential."
- **Intro Analyzer** (S04): evaluate 0–30 s for clarity, curiosity gap, emotional charge, narrative setup, drop-off risk, and "Does the title/thumbnail expectation match the opening lines?"
- **First-30-seconds principle** (S14 §3): "quickly confirm the title/thumbnail promise… Never use an arbitrary hook rule when the content requires a different rhythm."

🔵 **Assessment.**
- S02 is mostly drawn from **short-form social and Meta ads**. Examples: "Meta also reads your first 3 seconds" (p48), Instagram safe zones (p55), split-testing via "sub-accounts" (p12).
- Its seconds-level schedules (0–3 s, 3–8 s) apply to vertical feeds. For YouTube long-form, the official focus is promise confirmation and relative retention [S3; T39].
- Speed-to-value claims ("4 seconds", "7–10 s Shorts / 45–60 s long-form", S13 p24) are `CREATIVE_HEURISTIC`s.

📊 **YIOS evidence.**
- Transcript-coded openings in the original Finance set:
  - Open-question openings **0.74×** (q = 0.042; `SUGGESTIVE_NOT_ROBUST`, not replicable because the replication set has no transcripts).
  - Personal story 1.19×, number 1.13×, "imagine" 0.97×, contrarian 1.00× (all non-significant).
  - **The source claim that questions make the strongest hooks has no support in YIOS.** The only signal points the other way (C08).
- **First-party (DYH):**
  - `nP9fDHP1jbo` loses viewers at 4–5 s at the line "The answer is simple". It gave the answer away too early.
  - Specific symptom/test openings hold more of the audience in selected pairs: 30-s retention 60.0–60.5% versus 38.46% (MEDIUM confidence, small samples).

🎬 **Example (new, long-form finance), with S02 roles mapped:**
- (Context Lean) "Most people decide rent versus buy by comparing rent to the mortgage payment."
- (Scroll-Stop) "But that comparison leaves out four costs that only owners pay."
- (Snapback) "Add them back, and on a $400,000 home the 'cheaper' option flips after year seven. Here's the full math, line by line."
- On screen: "RENT vs BUY — YEAR 7" with the line chart already visible (key visual first).

🧪 **Test.**
- On owned long-form, run a sequential A/B of *opening styles* (question versus stake-statement) over 6–10 videos.
- Keep the topic family constant. Compare 30-s retention relative to each video's own length band.
- Use the Studio retention curve to inspect the first major dip against the published cut.

🇵🇰 *Hook ka kaam: pehle hi lamhon mein wada confirm karna. Context → "lekin" → ulta mor. Hamare data mein sawal se shuru karna kamzor (0.74×) nikla, magar yeh dobara test nahi ho saka.*

---

## II.G Scriptwriting and story architecture

📜 **Source teaching.**
- **BUT / THEREFORE** (S08 pp 1–3, attributed to Trey Parker & Matt Stone): replace "and then" with **BUT** (conflict) or **THEREFORE** (consequence).
  - Example: "Fridge broke down (BUT) had to buy new one (THEREFORE)".
  - Medical example: "Patient collapses… BUT doctors intervene… THEREFORE…".
  - S14 §4E turns this into a spine: SETUP → BUT → THEREFORE → BUT → THEREFORE → ESCALATION → PAYOFF → ECHO/NEXT STEP.
- **The 16 Commandments** (S17 pp 4–5, full text; S06 pp 3–4, compact):

| # | Law | Core idea (source wording condensed) | Claimed effect |
|---|---|---|---|
| 1 | Instant Hook | visceral or intellectual question "in <3 seconds" | CTR, first-5-s AVD |
| 2 | Escalating Tension | stakes, speed or scale rise; never plateau | early drop-off |
| 3 | Cause & Effect | BUT/THEREFORE; no "and then" | retention |
| 4 | Promise Delivery | deliver the title/thumbnail promise | prevents midpoint anticlimax |
| 5 | Throughline | one central question | low cognitive load |
| 6 | Retention Resets | "Every 20–30 seconds" a new visual/emotional/conceptual reset | "short attention pulse" |
| 7 | Curiosity Loops | open new loops before closing old | watch time |
| 8 | Emotional Switching | awe → humour → tension → relief | fatigue |
| 9 | Cinematic Energy | motion: parallax, zooms, composition rhythm | perceived production value |
| 10 | Visual Metaphor | explain abstract with imagery; never narration alone | memory |
| 11 | Awe & Scale | at least one "holy sh*t" scale break | virality |
| 12 | Texture | vary pacing, tone, layers, silence | burnout |
| 13 | Universal Simplicity | 12-year-old language | completion |
| 14 | Cultural Accessibility | globally resonant symbols | international CTR |
| 15 | Payoff | "inevitable yet surprising — 'Oh, of course!'" | memory, shares |
| 16 | Echo | loop back to the opening | completion → subscribe |

- **Section questions** (S14 §4E): What new question is created? What new evidence is delivered? Why does the viewer care now? What changes? What visual proves it?
- **Retention map** (S14 §4F): promise confirmation → first proof → first escalation → midpoint re-hook → strongest evidence → payoff → summary → next-video bridge. Guard against: repetition, premature answers, *excessive withholding*, long explanation without visual change, unresolved promises, CTAs before value is earned.
- **Story Density / Reveal Inventory** (S18 L352–396):
  - Does the story turn every 60–90 s?
  - The "Aur phir…" test: 7–10 meaningful turns means there is enough material; 2–3 means the story is thin.
  - Count new information, understanding changes, escalations and unexpected turns.
  - "Click starts the video; story density completes it."
- **Question → Delay → Payoff** (S15 p6): answer too fast and viewers leave; delay with tension and they stay.
- **Mini → mega → ultimate payoff escalation** (S07 Claude prompt).
- **Hero's Journey overlay** (S17 Gemini): ordinary world → disruption → transformation.
- **HPC for Shorts** (S13 pp 85–86): Hook → Progression → Climax; don't reveal the payoff early.

🔵 **Assessment.**
- BUT/THEREFORE, throughline, promise delivery and payoff are long-established craft principles (`CREATIVE_HEURISTIC`, well-founded for comprehension).
- The **timed** laws (#1 "<3 s", #6 "20–30 s") are the weakest parts. They conflict with the corpus's other intervals: 2–3 s micro-hooks (S06 p8), 8–12 s BUT/THEREFORE alternation (S08 p1), 15–30 s re-hooks (S02 p8), 20–40 s resets (S01 p3), 25–40 s motion resets (S06 p3), 60–90 s turns (S18), 2–3 min micro-arcs and ~3-min attention dips (S08 p2; S15 p17).
- S14 itself overrides them: "Do not insert random pattern breaks on a timer. Use meaningful resets when attention, emotion, or information state changes." (§4F; anti-pattern §11).

📊 **YIOS evidence.**
- **Counterexample to pace rules (first-party, DYH):** `NznebmgFwXI` had 2 cuts and held 87.1% at 3 s. `KPYHy7MDmLM` had 33 cuts and held 57.89%. More cutting did not mean better holding (C10).
- What If's decoded production grammar (14 source videos) uses long holds and sparse states in many sequences. The rejected YIOS prototype audit says "Empty space is **not inherently wrong**… R05 and R02 have very sparse states" (PR #44, `FAILED_VIDEO_VISUAL_AUDIT.md`).

🎬 **Example (new, finance spine):**
- SETUP: "You can afford the $2,400 mortgage."
- BUT: "the payment is only 60% of what owning costs."
- THEREFORE: "we add taxes, insurance, maintenance and the lost return on your down payment."
- BUT: "rent rises too, 3% a year."
- THEREFORE: "we run both for 10 years."
- ESCALATION: "and the answer flips at year 7, but only if you stay."
- PAYOFF: the full chart.
- ECHO: back to "can you afford it?" with a better question.
- Reveal inventory: 8 turns. Material is sufficient.

🧪 **Test.** Score the script before recording with S14's section questions and the S18 reveal inventory. Afterwards, compare the first major retention dip with the script beat at that timestamp. Never use a dip alone to infer *why* viewers left (DYH diagnosis: "A dip alone does not identify why viewers left").

🇵🇰 *"Aur phir" ki jagah "lekin" aur "is liye". Har 20–30 second ka timer wala reset koi rule nahi; reset tab karein jab maloomat ya jazbaat badle. Hamare channel par 2 cuts wali video ne 33 cuts wali se behtar rok kar rakha.*

---

## II.H Visual storytelling and editing

📜 **Source teaching.**
- **Renae v2.5 (S06), for What If-style science:** keep xkcd's black/white minimalism, but add micro-motion (parallax, soft zoom), emotional colour beats (white = analysis, black = cosmic awe/scale, orange = warmth/discovery; S06 p6), subtle sound (heartbeat, hum, reverb), kinetic typography, and the rhythm hook → tension → mini-release → re-hook.
  - Guideline: 16:9; 1–4 s per beat; "Each sentence = 1 motion beat"; silence is part of rhythm (S06 p12).
  - The output format for line-by-line analysis covers: script line / visual / animation logic / story function / BUT-THEREFORE role / sound / algorithmic value / upgrade / CapCut-VEO reconstruction (S06 pp 10–12).
  - Descriptive claims about xkcd What If: stick figures, flat static framing with occasional pans or zooms, morphs instead of cuts, accent colour = subject colour (S06 p9).
- **Visual metaphor and cinematic energy:** Commandments 9–10.
- **Every visual must clarify, prove, escalate, emotionally translate or reset** (S14 §4H). There is also a production list: beat sheet, storyboard, A/B-roll, proof list, on-screen text, medical graphics, sound arc, thumbnail capture list, fact-check, disclosure checklist.
- **Human connection** (S14 §4G, from the absent Casey Neistat playbook): physical props, useful imperfection, the "So what?" rule, constraints. "The goal is not to look amateur. The goal is to retain visible humanity."
- **BUT/THEREFORE in camera** (S08 p2): BUT = camera shift, sudden cut or tonal contrast; THEREFORE = smooth dolly, warm light, resolution music.
- **Camera grammar** (S10 VEO 3 guide, S09 Nano-Banana guide): low angle = power, high angle = vulnerable, OTS = intimacy, POV = immersion. Write motion with durations ("dolly in slowly (1.2s)"). Lighting sets mood (warm = hopeful, cold blue = isolation).
  - Image prompts need 8 slots: subject, action, environment, lighting, camera, style, details, output.
  - Describe the desired scene rather than negatives.
  - Keep identity consistent across shots.
- **Thumbnail and frame composition:** foreground hero, negative space for text, 45° light, one accent colour (S02 pp 55–57).

🔵 **Assessment.** These are production `CREATIVE_HEURISTIC`s. The xkcd description in S06 is the author's *perception* and can be checked against YIOS forensics (below). The emotional colour codes are conventions, not tested effects.

📊 **YIOS evidence — the strongest observational material in the project:**
- **What If production brain** (PR #44 ref `origin/codex/what-if-archive-main-integration` @ `badec432`, **unmerged**): 14 decoded source videos.
  - Records: 7,864 words, 604 sentences, 581 visual states, 438 motions, 200 shots, 82 transition patterns, 1,421 audio-visual sync rows, 1,221 audio-trigger patterns.
  - The sample is **hit-heavy**. It includes the channel's biggest videos (`8fADp43wJwU` 9.53M, `UXA-Af-JeCE` 8.52M, `e3uk7jU3RHo` 7.93M views), so it describes house grammar and **cannot** show what causes success.
- **Rejected YIOS prototype** (PR #44 `research/production-experiments/what-if-derived/chair_test_v2_review/FAILED_VIDEO_VISUAL_AUDIT.md`). A 34.4-s "chair test" senior-health explainer in What If style was **rejected**. Core diagnosis:
  - > "The edit translates nouns into separate stock-like objects and sentences into labels. It seldom translates a claim into an observable consequence."
  - It had filled, clothed human figures beside outline furniture, a style mismatch with the references' stick construction.
  - A timer "floats" when the chair asset is swapped: a causality break.
  - One demonstrated stand produced two visible counts: a visual explanation error.
  - "Adding more icons would not solve it."
  - **Lesson:** visual storytelling means showing *state change and consequence*, not illustrating nouns. This is YIOS's own production lesson, not evidence about YouTube.
- **Casually Finance Visual Forensics** (`research/visual-forensics/`, visual-only, accepted 2026-10-24):
  - `Uumnx2Fo6cE` "The New American Housing Crisis Has Landed": 920.7 s, **507 visual states**, median state 1.25 s, 24.1 cuts/min, 12.5% of frames in motion, 73.1% hard single-frame changes.
    - Grammar: source-first article capture → pointer + highlight → doodle metaphor → big handwritten red number.
    - Major scene changes cluster at ASR sentence starts (58% vs 10% chance). Word-level sync is at chance (66.5% vs 60.1%).
  - `o3FQcd91MIs`: 278 s, 76 states, zero motion. Peer ratio 1.25 (TYPICAL).
  - `Uumnx2Fo6cE` is labelled BREAKOUT (6.65) by the branch method, but YIOS's own peer rule gives **no ratio**: it was 12 days old with fewer than 5 age peers.
  - Two videos cannot show that visual density causes a breakout (`UNKNOWN`).

⚠️ **Never present** a YIOS reconstruction as reference footage, or a hit's editing as the cause of its success.

🎬 **Example (new).** Script line: "Rent rises 3% a year."
- Weak visual: a "3%" label next to a house icon.
- Consequence visual: a rent receipt stack that visibly grows each "year" tick while a mortgage stack stays the same height until year 7, where the lines cross. This follows the source-first → pointer → metaphor → number grammar observed in `Uumnx2Fo6cE`.

🧪 **Test.** Build two edits of the same script segment (noun-label versus consequence-state). Measure the relative retention through that segment on an owned channel, or run an unlisted comprehension check with 10 target viewers ("What changed at year 7?").

🇵🇰 *Visual ka kaam cheez dikhana nahi, natija dikhana hai. Hamara apna rejected "chair test" prototype isi liye fail hua: nouns ko icons bana diya, consequence nahi dikhaya.*

---

## II.I SEO and publishing

📜 **Source teaching.**
- **S16 checklist, ten phases:**
  1. One-line purpose: "This video helps ___ to ___".
  2. Keyword research: one primary and 3–5 secondary keywords, using autosuggest, vidIQ, TubeBuddy, Trends.
  3. Competitor top 5: "Can I make something better?".
  4. Keyword in the first 30 s, repeated 2–3 times.
  5. Quality: 1080p, clear audio.
  6. Title: keyword first, <60 characters, Keyword + Benefit + Curiosity.
  7. Description: keyword in the first 25 words; 200–300+ words; timestamps.
  8. 10–20 tags, including a channel-name tag.
  9. Thumbnail "CTR = HUGE ranking factor".
  10. Settings (category, language, subtitles, end screens, cards, chapters, pinned comment, hashtags); engagement asks; 24-h promotion; playlists; analytics after 48 h (CTR 6–12%, retention 40%+).
  - Golden rules: no fake tags, no misleading titles, no bought views, "humans first, SEO second".
- **S14 §4I, SEO by traffic source:**
  - *Search-led videos:* natural query language in the title, opening and description; answer comprehensively; chapters; captions.
  - *Browse/Suggested-led videos:* broad human relevance and expectation matching; "metadata for clarity, not keyword stuffing".
  - Publishing checklist: strong first two description lines, captions, chapters, correct audience/language/disclosure settings, an end screen tied to the viewer's next question, a pinned comment that adds value, playlists, no misleading tags.
- **Sequencing / video ladders** (S13 p1): intro → deeper → advanced. Decide the viewing order before filming. Use end screens, pinned comments and playlists. S15 p35: build a chain, not standalone uploads.
- **Upload settings myths** (S13 pp 44–64): rename the file; schedule 24–48 h ahead "so YouTube can process"; upload from desktop (or from phone, depending on the speaker); post 30–60 min before peak; 60 hashtags "safely".

🔵 **Official.**
- Tags play "a minimal role"; they are useful for misspellings. Title, thumbnail and description matter more. Excessive tags in descriptions are spam [S17].
- **More than 60 hashtags → all are ignored**; over-tagging can remove a video from search [S14].
- Search ranks on relevance, engagement for that query, and quality [S6].
- Publish time "doesn't appear to affect long-term viewership" (live/premieres excepted). Consistency of quality matters more than frequency, and breaks aren't penalised [S1].

📊 **YIOS evidence.**
- **First-party (DYH, lifetime to 2026-09-27):**
  - Shorts feed 5,355 views (AVD 0:19).
  - YouTube search 1,175 views (11,245 impressions, CTR 2.71%, AVD 0:39).
  - Suggested 1,031 views (19,841 impressions, CTR 2.9%, AVD 1:07, the most watch time at 19.3 h).
  - Browse 405 views (CTR 3.28%).
  - Channel pages 139 views (CTR 7.03%).
  - Even a tiny medical channel gets meaningful search *and* suggested traffic. Suggested viewers watch longest.
- **Competitor search traffic is unknown** (no competitor traffic data). Whether "Rent vs Buy" won by search is `UNKNOWN`.

⚠️ **Contradicted or unsupported:** CTR 6–12% and retention 40% thresholds (C02); tags importance (C16); 60 hashtags (C17); publish-time effects (C20); file-name metadata (S13 pp 55–60; S14 §11 lists "file names" as a non-lever).

🎬 **Example (new).**
- Search-led: "How to calculate rent vs buy (step-by-step, 2027)". Uses the query language; chapters per cost item; the description gives the formula in the first two lines.
- Browse-led: "Rent vs Buy: The 10-Year Math Nobody Shows You".
- The same core content can be a search version and a browse version, but don't mix both intents in one title.

🧪 **Test.** After 28 days, compare traffic-source shares and CTR **per source**, not pooled. For search-led videos, check Studio search terms for the intended query.

🇵🇰 *Tags ka kirdar bohot kam; 60 se zyada hashtags lagayein to sab ignore. Upload ka waqt lambi muddat mein farq nahi daalta. Search wali video aur browse wali video ki SEO alag hoti hai.*

---

## II.J Analytics and optimisation

📜 **Source teaching.**
- **S14 §4J diagnosis ladder:**
  1. Low impressions → topic size, audience match, competition, channel fit.
  2. Impressions but low clicks → packaging or targeting.
  3. Clicks but early drop → promise mismatch, weak intro, slow value.
  4. Good intro but middle decline → escalation, repetition, overload.
  5. Good retention but weak loyalty → personality, meaning, next step.
  6. High views but low satisfaction → overpromise.
  - "Change one major variable at a time."
- **S18 L262–343, new-channel diagnosis.** Order: Audience → Topic → Packaging → Content → Scale.
  - The first 3–5 videos test **Audience Desire A vs B**, not Thumbnail A vs B.
  - Zero impressions: check public, processing and restrictions first. Don't overreact in the first hours.
  - After 48–72 h, clarify the topic and person ("Why Jennifer Grey's Career Changed After Dirty Dancing" > "The Decision That Changed Everything").
  - Matrix: impressions high + CTR low → packaging; CTR ok + retention weak → hook/script; CTR low + retention strong → packaging; both strong → scale.
  - Natural ceilings exist: narrow demand, topic limits.
  - Rule: **No Traffic = distribution; Traffic, no click = packaging; Click, no watch = content; Click + watch = scale.**
- **Feedback loop** (S18 L6–89): Hypothesis → Publish → Measure → Learn → Adjust → Repeat. A 5-line post-mortem per video: expected / happened / worked / failed / change next.
- **Exploration vs exploitation** (S18 L92–123): 70–80% proven, 20–30% experiments.
- **Retention graph** (S15 p5): dips = lost attention; spikes = rewatches; "go 5 seconds before the dip".
- **Content Legos** (S13 p25): nine levers (topic, angle, hook, storytelling, visuals, audio, title, thumbnail, pacing). Change one at a time.

🔵 **Official.**
- Compare videos **relative to similar ones** on your channel. Use retention graphs to see where people "relatively" drop off. Like rates help. "Listen to your audiences" [T39 ch. 5].
- Viral videos naturally show *lower* CTR and AVD as audiences broaden [T39 ch. 5; S7].
- The Subscriptions feed is a clean slice, and ~90% of subscribers not clicking is normal [T39 ch. 12–13].

📊 **YIOS evidence.**
- **Prediction failed:** a title/duration model did not beat the simple peer-median baseline. MAE 0.803 vs 0.782 (temporal split); 1.098 vs 1.073 (unseen channels). No YIOS "virality score" is justified (C37).
- **Likes are a poor satisfaction proxy:** like-rate is inversely related to peer ratio in **9/9** channels. Broader-reaching videos get proportionally fewer likes.
- **DYH:**
  - Shorts acceptance and depth are separate. `QfRaG71ZA_0` stayed 57.3% / APV 83.3%; `PTB-6fgaAKk` stayed 16.9% / APV 126.6%.
  - "Walking Shorts": `FVfG_HZV4qg` stayed 51.1% vs `kF26QB7xHiE` 27.0%, but views were 1,068 vs 1,212.
  - "Clearer feed acceptance did not equal more views; distribution and completion are separate stages."

🎬 **Example (new) — reading one result:**
- Video: 9,000 impressions, CTR 2.1% (channel median 3.0%), 30-s retention 61% (channel median 52%).
- Diagnosis: packaging problem, not content.
- Action: Test & Compare with two new thumbnails, keeping the title constant.

🧪 **Test.** Keep a per-video ledger with: hypothesis, variable changed, peer ratio at day 7/28, CTR by source, 30-s retention relative to length band, returning viewers, and the 5-line post-mortem.

🇵🇰 *Pehle masla kis "layer" par hai yeh dekhein: traffic, click, ya watch. Aik waqt mein aik cheez badlein. Hamara prediction model simple baseline se behtar nahi tha, is liye koi "viral score" nahi.*

---

## II.K Creative operating systems

📜 **What exists.**
- **Seven-engine persona system** (S01, S04, S07, S12, S17, S06 pp 5, 8–9). Personas: ChatGPT = Architect/Director-Philosopher; Grok = Viral Provocateur; Gemini = Mythic Storyteller (or Story Architect / Story Surgeon); Perplexity = Detective of Curiosity; DeepSeek = Retention/Algorithm Hacker; Google AI Studio = UX Storyteller / Universal Translator / Algorithmic Strategist; Claude = Literary Critic/Integrator.
  - Each has prompts for intros (S04), scripts (S07), titles (S12) and 16-Commandment reviews with 1–10 scores (S17).
  - Pitched as a Pixar-style "Brain Trust Room" (S01 p3).
- **Renae Creative Engine v2.5** (S06):
  - 13 performance dimensions.
  - 16 Commandments.
  - Fusion Framework v2.0: CTR science → AVD science → Retention science + BUT/THEREFORE + emotional architecture.
  - Visual grammar and line-level analysis format.
  - A 90-day roadmap with targets: +10% AVD, +15% 50%-retention, +10% 75%-retention, +10% CTR. **These targets are invented, with no baseline or measurement plan.**
- **Fusion Framework v2.0** (S08 pp 2–3): CTR engineering ("compressed micro-story"), AVD engineering (tension–release micro-arcs every 2–3 min), Retention engineering (payoff + tease next loop).
- **Verified Creator OS v1** (S14). The most mature document:
  - Truth hierarchy: official → own Studio → direct evidence → playbooks → patterns → hypotheses.
  - Labels: [Verified]/[Observed Pattern]/[Hypothesis]/[Unverified].
  - Phase A–J pipeline; seven lenses "not … claims that separate external models were consulted".
  - 15-dimension 1–10 scoring ("Do not average blindly; a severe failure in truthfulness, safety, promise delivery, or visual clarity disqualifies").
  - Anti-patterns.
  - Final principle: "Idea creates potential. Packaging earns attention. The intro confirms the decision. Story creates momentum. Evidence creates trust. Payoff creates satisfaction. Humanity creates loyalty. Analytics create the next improvement."
- **Scorecards.** S02 p9: a 12-item 1–5 hook rubric, "≥45 generally predicts strong hold" (unsupported). S18 L979–1189: a Format Arbitrage 7-item /5 scorecard (30–35 strong; <22 don't build).

🔵 **Assessment.**
- The persona system is a useful **checklist generator**: it forces a script to be examined for structure, virality, clarity and curiosity.
- But (C38) the outputs are LLM text. They are not seven independent measurements, and no persona has been validated against outcomes.
- The YIOS V1 code modules (`scripts/run_youtube_intelligence.py`, `report_packaging_intelligence.py`, `report_hook_script_intelligence.py`, `report_topic_opportunity.py`, `report_editing_visual_intelligence.py`, `report_channel_strategy_intelligence.py`) are the project's *implemented* OS. They compose evidence-traceable plans and do not use persona scores.

🧪 **How to use the persona OS honestly.**
1. Run the lenses as a checklist.
2. Merge their findings into S14's 15 dimensions.
3. Make **one** decision.
4. Record which *measurable* prediction it implies (for example, "30-s retention above channel median").
5. Never cite a persona score as evidence.

🇵🇰 *Saat "engines" asal mein saat zaviye (lenses) hain, saat alag mahireen nahi. Inko checklist ki tarah istemal karein; inka score saboot nahi.*

---

# PART III — What YIOS Actually Has: Data Census and Authority

🟢 **Beginner.** Before learning from data, know what the data *is*. YIOS has public competitor metadata (titles, views, dates, transcripts), deep human/AI audits of Finance videos, frame-level visual forensics for a few videos, and one owned channel's private Studio exports. It does **not** have competitor CTR, retention, traffic or revenue. Nobody outside a channel's Studio has those.

🔵 **Dated census.** All checked today, 2026-10-26, at HEAD `d987510b`; Finance audit counts re-read at `df80644a`. The same-day census receipts were re-validated by re-running `YIOS-Algorithm-Audit-2026-10-26/scripts/qa.py`: all PASS, DB SHA-256 unchanged, worktree clean.

| Population / asset | Count (live) | Authority / locator | Note |
|---|---|---|---|
| Finance registered identities | **1,612** = 966 original + 197 expansion-12 + 63 Monkey Explains + 386 reconciliation | `research/finance-economics-intelligence/reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv` | Its `audit_status` column is **stale** (430 complete) |
| Finance deep audits complete (all six reviews) | **449** at `d987510b` (13:22) → **455 / 1,157 remaining** at `df80644a` (17:21, NICK_179) | `research/finance-economics-intelligence/VIDEO_AUDIT_966.jsonl` (live ledger); `RESUME_HERE.md` | Written by the concurrent Finance session, not by this audit. Next untouched: NICK_180 `W-j0_v9cXuQ`. Statistical tests used the 449-audit snapshot; peer ratios don't depend on audit status |
| Original 966 with computable peer ratio | 723 (11 channels) | analysis receipt | DS-000001's 159 are undated |
| Replication videos with peer ratio | 418 (Expansion 169, Monkey 52, Casually Finance 197) | analysis receipt | Used for out-of-sample checks |
| Registry DB | 75 channels, 2,303 videos, 2,303 transcript rows (12 placeholders), 26 tables, quick_check ok, 0 FK violations | `data/catalog/youtube_channel_registry.db` (SHA `39e7a28b…`) | `video_type` labels inconsistent; 771 non-ISO `published_at` |
| Inventory DB | 28 tables; 667 videos (all in registry) | `data/catalog/youtube_inventory.db` (SHA `277c09f6…`) | Provenance |
| Empty DB files | 2 (0 bytes) | `data/catalog/youtube-intelligence-os.db`, `youtube_intelligence.db` | Not data |
| What If decoded source videos | 14 (hit-heavy) | PR #44 ref `badec432` (unmerged) | Production grammar only |
| Casually Finance visual CT scans | 2 (visual-only) | `research/visual-forensics/INDEX.csv` | Visual 003 **not on Machine B** |
| **Owned-channel first-party Studio (DS-000032 "Decode Your Heart – Dr. Rehan")** | 56 videos (27 regular, 29 Shorts); 56 retention exports, 46 curves; 22 matched comparisons; 15 medical-claim reviews (5 requiring action) | `docs/research/decode-your-heart-2026-09-27/` (derived) | **DERIVED_PRIVATE_ANALYTICS** (privacy class doc `docs/audits/DECODE-YOUR-HEART-PRIVACY-CLASSIFICATION-2026-10-03.md`). Raw ZIPs are not on this machine |
| Senior-health competitor research | DS-000003…DS-000010 channels; forensic v2/v3 registers | `docs/research/senior-health-2026-09-25/` | Public metadata + claim matrices |
| Packaging research (Genius History) | 10 title, 10 thumbnail, 10 package audits | `docs/research/packaging-validated-2026-10-11/` | Analyst scores, not measured CTR |
| Thumbnail forensics V1 | 6 thumbnails inspected | `docs/research/thumbnail-forensics-2026-10-02/` | First installment only |
| Global knowledge corpora | DS-000011 (17 files), DS-000018 (63 tabs), DS-000031 (1 file) | `data/raw/global-youtube-knowledge/` | Sources of Part II |

### III.1 Correction to the earlier same-day audit

The earlier package stated "First-party analytics = 0 for 75/75 channels". That is true **of the channel registry DB**. However, the repository *does* hold derived first-party Studio measurements for the owned senior-health channel DS-000032 under `docs/research/decode-your-heart-2026-09-27/`. That package was outside the registry's `first_party` tables. This guide uses those derived measurements (aggregates and a few matched pairs) and labels them `DIRECT_PROJECT_OBSERVATION (first-party, small channel)`.

| DS-000032 Studio period (as exported 2026-09-27) | Views | Watch h | Impressions | CTR |
|---|---|---|---|---|
| Last 28 days | 1,158 | 7.98 | 4,360 | 3.19% |
| Last 90 days | 2,507 | 22.71 | 18,579 | 3.04% |
| Lifetime | 8,366 | 45.62 | 36,159 | 3.00% |

### III.2 Evidence authority and permissible uses

| Data | Valid for | Invalid for |
|---|---|---|
| Frozen views + age + same-channel peers | Within-channel, age-matched comparison of lifetime public reach | CTR, retention, traffic source, causation |
| Title text | Mechanical feature coding | Packaging causation (upload-era titles and thumbnails unknown) |
| Current thumbnails | Describing present artwork | Upload-era packaging (`historical_design: UNKNOWN`) |
| Auto-caption transcripts | Lexical opening features | Timing in seconds, delivery |
| Deep-audit analyst prose | Qualitative context, claim audits | **Outcome-blind coding.** The prose quotes each video's tier, e.g. "Weak 0.14×" |
| What If forensic decode | House production grammar | Success-vs-failure inference (no low-performer decodes) |
| DS-000032 Studio exports | Own-channel diagnosis, matched comparisons | Generalising to other channels (tiny channel, ~8k lifetime views) |
| AI persona outputs | Checklists | Evidence |

### III.3 Quality findings (live)

- `FINANCE_UNIVERSE.csv.audit_status` is stale (430 vs 449).
- The checksum manifest of `expansion-12-channel-2026-10-20/README.md` no longer matches, because the README was edited after the manifest was written. All data files match.
- `video_type` is inconsistent: `video` 1,150 · `regular video` 890 · `shorts` 90 · `Short` 14 · NULL 159.
- `Time_sensitivity` = `UNVERIFIED` for all 966. 936/966 topic tags are title-keyword heuristics.
- Visual Forensics Video 003 is not accessible here (Machine A).

🇵🇰 *Hamare paas competitors ka CTR/retention nahi hai. Sirf apne channel (Decode Your Heart) ka Studio data hai, aur woh chhota channel hai. Pehli report ki "zero first-party data" wali baat registry tak sahi thi, poore repo ke liye nahi.*

---

# PART IV — The YouTube Algorithm: Evidence vs Myth

## IV.1 What is officially known (2026-10-26)

| # | Fact | Label | Ref |
|---|---|---|---|
| 1 | Goals: help viewers find what they want; long-term satisfaction | OFFICIAL_CURRENT | [S1] |
| 2 | No set formula; signals weighted differently per viewer, surface and context | OFFICIAL_CURRENT | [S1; T39 ch. 5] |
| 3 | Home relies mainly on watch history; Up Next on the current video; Shorts feed personalised | OFFICIAL_CURRENT | [S2] |
| 4 | Satisfaction surveys, likes/dislikes, "Not interested" are inputs | OFFICIAL_CURRENT | [S2; S10; T39] |
| 5 | Appeal / Engagement / Satisfaction framing | OFFICIAL_CURRENT | [S3] |
| 6 | Search: relevance, engagement, quality (expertise, authority, trust) | OFFICIAL_CURRENT | [S6] |
| 7 | Half of channels' videos have CTR 2–10%; CTR drops as reach broadens | OFFICIAL_CURRENT | [S7; T39] |
| 8 | Test & Compare picks winners by watch-time share | OFFICIAL_CURRENT | [S9] |
| 9 | Publish time doesn't appear to affect long-term viewership; breaks aren't penalised | OFFICIAL_CURRENT | [S1] |
| 10 | Tags minimal (misspellings); >60 hashtags → all ignored | OFFICIAL_CURRENT | [S17; S14] |
| 11 | Disclosing realistic AI content alone won't limit audience or monetisation | OFFICIAL_CURRENT | [S15] |
| 12 | Mass-produced, templated, low-value content and unmodified reused content are not monetisable ("inauthentic content", renamed from "repetitious") | OFFICIAL_CURRENT | [S16] |
| 13 | Shorts can be up to 3 minutes (from 2024-10-15) | OFFICIAL_CURRENT | [S18] |
| 14 | Non-subscribers can see a video in its first hour; responses are learned per audience; the system isn't based on the first hour or first 10,000 viewers | OFFICIAL_CURRENT (spoken) | [T39 ch. 3, 12] |
| 15 | Embed/ad/link traffic is down-weighted for homepage ranking if not predictive; comments-off and ads-off are not penalised | OFFICIAL_CURRENT (spoken) | [T39 ch. 5, 11] |
| 16 | Cross-topic Suggested traffic reflects shared viewers, not "confusion"; the system distinguishes topic/format per viewer within one channel | OFFICIAL_CURRENT (spoken) | [T39 ch. 9–10] |

## IV.2 Historical research (true of the described systems)

- **2016:** candidate generation → ranking; expected-watch-time objective; "example age" feature for freshness [S11].
- **2019:** multitask ranking (engagement + satisfaction objectives), position-bias correction [S12]; off-policy REINFORCE with exploration [S13].
- **2021 blog:** history from clicks (pre-2012) → watch time → surveys / "valued watch time" [S10].

These explain *why* satisfaction and per-viewer prediction matter. They do not reveal 2026 weights.

## IV.3 Myth audit of the original sources

The full matrix has 48 claims in `ledger/CLAIM_EVIDENCE_MATRIX.csv`. The most consequential:

| Claim (source) | Verdict | Why |
|---|---|---|
| "Goal 10%+ CTR" (S05) / "6–12%" (S16) / "≥10% core metric" (S13 p54) | **CONTRADICTED as thresholds** | [S7] range is descriptive; T39: even subscribers click "maybe 10% or less"; YIOS owned channel lifetime 3.0% |
| "YouTube first decides on click probability — only one thing" (S15 p8) | **CONTRADICTED** | [S1; S3; S9; T39] |
| "Ranks the curiosity gap / promotes questions" (S15 p1) | **CONTRADICTED** as mechanism | No official basis; YIOS curiosity effect did not replicate |
| "Fear titles always win" (S15; S02 Urgent Warning) | **CONTRADICTED** | 0.75× then 1.10× |
| "Questions are the strongest hooks" | **No support** | YIOS 0.74× (unreplicated) |
| "Reset every 20–30 s" (S17 #6) | **Not a rule** (heuristic) | Conflicting intervals; S14 bans; DYH counterexample |
| "Tags are crucial; 10–20 tags" (S16) | **CONTRADICTED** | [S17] |
| "60 hashtags safely" (S13 p45) | **CONTRADICTED** | [S14] |
| "Schedule/publish time drives success" (S13 pp 62–64) | **CONTRADICTED** (long-term) | [S1] |
| "Breaks/post less kills growth; pause 48 h after a hit" (S13) | **CONTRADICTED** | [S1] |
| "Channel trust score; warm-up accounts; proxies" (S13; S15) | **UNKNOWN / policy risk** | No official basis; fake-engagement risk |
| "Subscribers test first; weak first hour kills a video" | **CONTRADICTED** | [T39 ch. 3, 4, 12]; YIOS age slope |
| "Mixed topics reset the algorithm" | **Overstated** | [T39 ch. 9]; channel-audience alignment still matters (variance share) |
| "Copy proven formats — YouTube doesn't care about originality" (S13 pp 2–4) | **CONTRADICTED** as guarantee | [S16]; YIOS 159× vs 0.07× |
| "AI/faceless content automatically penalised"; "disclosing AI kills reach" (S13 p74) | **CONTRADICTED** | [S15; S16] — the risk is templated mass production, not AI per se |
| "Captions are now the main SEO" (S15 pp 10–14) | **PLAUSIBLE for search relevance, UNKNOWN for Browse** | [S6] |
| "Shorts auto-detected as <60 s" (S13 p82) | **OUTDATED** | [S18] |
| "LLMs/semantic understanding power matching" (S13 p22; S19 T36/T51) | **HISTORICAL/PLAUSIBLE** | Google semantic-ID research; no ranking spec |
| "Dopamine/oxytocin/mirror neurons drive retention" (S01, S06, S08, S15) | **UNKNOWN** (metaphor) | No evidence in sources |
| "Seven engines = independent experts" | **CREATIVE_HEURISTIC only** | No separate model runs evidenced |

## IV.4 Unknowns (cannot be verified from outside)

- The current feature weights.
- Test-group sizes for new videos.
- Whether "good abandonment" or re-searching is used as a signal.
- How much captions contribute to Browse.
- The exact role of Hype points.
- Whether comment *sentiment* is read.
- How Shorts views feed long-form recommendations.

**Any document that states these as facts is guessing.**

🇵🇰 *Official baatein: satisfaction, har viewer ke liye alag ranking, koi formula nahi, CTR 2–10% aam, publish time ka lamba asar nahi, tags kam ahem, AI disclosure se reach kam nahi hoti. Baqi "secret rules" zyada tar andaaze hain.*

---

# PART V — Channel and Virality Intelligence (with three case studies)

## V.1 What YIOS data says about "virality"

🟢 **Beginner.** Most videos on a channel do ordinarily; a few do enormously well. Which channel the video is on matters more than any wording trick. Titles that "go viral" on one channel often fail on another.

🔵 **Findings** (Finance original 966 plus replication sets; same-day receipts re-validated):

| Finding | Number | Label |
|---|---|---|
| Channel identity's share of variance in log views/day | 37.8% (Finance) / 57.5% (all niches) | STATISTICAL_ASSOCIATION |
| Top 10% of videos' share of channel views (median of 33 channels) | 66.9% | REPLICATED_PATTERN (across channels) |
| Title wording features surviving replication on unseen channels | **0 of 14 primary tests** | STATISTICAL_ASSOCIATION absent |
| Title + duration model vs peer-median baseline (MAE) | 0.803 vs 0.782; 1.098 vs 1.073 → model **not** better | CONTRADICTS "viral formulas" |
| Like-rate vs peer ratio | negative in 9/9 channels | DIRECT_PROJECT_OBSERVATION |
| Same concept on different channels | 14.8× (`uByLqFbCcEA`) vs 0.14× (`6dw0y-ATdwI`); 159× (`2LXED3ENhck`) vs 0.07× (`eB0XSeS7y8Q`) | counterexamples |
| Cross-channel recurring winners | rent vs buy (Logical Money 350×; Mark Invests `pnJCpIhshX4` 297×), real estate vs stocks (36×; `k-ZxdjawYDs` 102×), compounding threshold (`rnbgKswe2nA` 51.4×; `OX-fSJzHyPI` 67.1×), paying cash for cars (29×; 9.7×) | PLAUSIBLE_HYPOTHESIS |
| "Mistake" framing failure | "RMD mistake 84% make" `YL3stNaRSRc` **0.04×** | counterexample to S02's "Mistake Reveal" formula |

## V.2 Why concepts transfer poorly

- **Pull, not push.** Each channel's audience has its own history. A concept wins when it matches *that* audience's interests [T39; S2].
- **Survivorship.** Outlier lists show winners, not the many copies that failed. The repo senior-health claim matrix (`docs/research/senior-health-2026-09-25/forensic-v2/DS-000018-CLAIM-MATRIX.json`, ALG26-CLM-001) records Ares/Elias hits spawning "8-9 copies within days that mostly get 1-150 views".
- **Execution and trust.** The same title with weaker substance disappoints viewers. YIOS deep audits repeatedly find competitor arithmetic errors. For example, NICK_173 `UfqNzF7sQzo`: $950/month for 7 years at 10% ≈ $114.9K, not the implied $290K. A credibility gap is a differentiation opportunity (`PLAUSIBLE_HYPOTHESIS`).
- **Age and snapshot confounds.** Raw views mix age and channel size. YIOS uses peer ratios to correct for this.

## V.3 Defensible opportunity hypotheses

All are `PLAUSIBLE_HYPOTHESIS`; none is proven.

1. **H-A Concrete decision math.** Personally consequential comparisons with checkable numbers (rent/buy, cash/finance, invest $X/month) travel better than abstract "psychology of money" framings. Within-channel counterexample: `R2gYICl_VR0` 0.08×.
2. **H-B Accuracy as differentiation.** In finance and health, reconciled numbers and cited sources can raise satisfaction (survey and returning-viewer signals) where competitors cut corners.
3. **H-C Situation-led packaging.** For health, specific test/symptom-situation packages outperform broad warnings (DYH `BCNWQ3uuSuE` vs `SBrMW71O69U`; MEDIUM).
4. **H-D Topic clusters after a hit.** Follow a hit with the audience's next questions (S18 L1197–1423, Isra & Miraj worked example; S13 p1 video ladders). Untested in YIOS.

---

## V.4 One idea traced through every phase (worked example, new)

*All outputs below are **new examples** written for this guide. They are not observed reference footage.*

**Channel:** a new English personal-finance channel. **Viewer:** 28–40, renting, wondering whether to buy. Watching situation: evening, phone or TV, has seen two "rent vs buy" videos and is still unsure.

| Phase | Decision | Grounding |
|---|---|---|
| 1 Audience | "My audience wants honest decision math because they want to stop feeling stupid about the biggest purchase of their life." | S18 audience sentence |
| 2 Demand | Rent-vs-buy is a recurring cross-channel winner (350×, 297×) | Part V.1 |
| 3 Channel fit | "This is a money-decisions channel, explored through real 10-year math." | S18 Niche Bending test |
| 4 Angle | Contradiction + number: "the cheaper monthly option flips after year 7" | S14 §4B; S15 angles |
| 5 Package | Three variants A/B/C (II.E). Test & Compare after publishing | [S9] |
| 6 Hook | Context Lean → "But four costs are missing" → "it flips at year 7; here's every line" + chart visible | S02 3-step; [S3] promise confirmation |
| 7 Script | SETUP/BUT/THEREFORE spine, 8 reveal turns; midpoint re-hook "what if you move in year 5?" | S08; S14 §4E–F; S18 density |
| 8 Storyboard | One state per idea-change, not per noun: receipt stack vs mortgage stack; crossing lines at year 7; source-first captures of current rate data | II.H; `Uumnx2Fo6cE` grammar (observation) |
| 9 Production | Narration conversational; on-screen numbers match the script; fact-check sheet with every input cited | S14 §4G–H |
| 10 Publish | Browse-led title; first two description lines state the method; chapters per cost (useful for a calculation video); end screen to "How much house can you afford?"; playlist "Money decisions, with math" | S14 §4I; [S17] |
| 11 Analytics (day 7/28) | Peer ratio vs own videos; CTR by source; 30-s retention vs length band; returning viewers; Test & Compare verdict | S18 diagnosis; [T39] |
| 12 Experiment | If CTR is low but retention high → packaging test; if early dip at 0:40 → rewrite the opening of the next video only | S18 L262–343 |
| 13 Next video | Cluster the audience's next questions from comments: "What if I can only put 5% down?" | S18 competitor/comments method |

---

## V.5 Case study 1 — Finance / Economics (YIOS evidence-led)

🟢 **Beginner.** Finance viewers come for decisions. The data suggests concrete "should I do X or Y, with real numbers" videos are the most reliable winners, but only on the right channel and with honest math.

🔵 **Evidence:**
- 449 deep audits with claim and calculation receipts (live ledger).
- Peer ratios for 723 original videos plus 418 replication videos.
- Cross-channel winners and flips (V.1).
- Two visual CT scans of Casually Finance:
  - `Uumnx2Fo6cE`: 507 states, source-first evidence captures, handwritten numbers.
  - `o3FQcd91MIs`: 76 states, TYPICAL 1.25×.
  - These two videos **cannot** show that visual density causes success.

📜 **Sources applied:**
- S18 Psychology Arbitrage to generate angles from "Renting vs Buying — The Real Math".
- S14 §6-style accuracy discipline, generalised to finance.
- S16 for search-led companion videos ("rent vs buy calculator explained").

⚠️ **Uncertain:**
- Whether search drove the rent-vs-buy hits (no traffic data).
- Whether accuracy itself lifts reach (untested).
- Nick Invests dominates the data (concentration risk).

🎬 **New creative output** (example, not observed):
- Title: "Paying Cash for a Car vs Financing at 6.9%: The 5-Year Math".
- Hook: "Everyone says pay cash. But at today's savings rate, the math only favours cash in one of three cases. Here are all three, with the numbers on screen."
- Visual: two account balances drawn side by side, updated each month tick.

🧪 **Test criteria:**
- Day-28 peer ratio ≥ 1.0 on your own channel baseline (after ≥5 peers exist).
- 30-s retention ≥ channel median for the length band.
- Comments asking a follow-up question (topic-cluster signal).
- Zero arithmetic corrections required after publication.

## V.6 Case study 2 — Educational / science visual explainers (What If evidence)

🟢 **Beginner.** What If-style videos take an absurd question seriously and answer it with simple drawings and real physics. Their grammar is minimal and does not use flashy cuts.

🔵 **Evidence:**
- 83 What If registry videos. Long-form vs Shorts lifetime views/day medians are 4,123 vs 4,676 (different units, not comparable as performance).
- 14 decoded hit-heavy sources: 581 states, 438 motions, 200 shots, 1,421 A/V sync rows.
- **The rejected YIOS chair-test prototype** (34.4 s) failed because it illustrated nouns instead of consequences. It mixed asset families (filled clothed human vs outline furniture) and broke causality (a floating person when the chair swapped to a stopwatch).
- These are all `DIRECT_PROJECT_OBSERVATION` about production. None is evidence about YouTube ranking.

📜 **Sources applied:**
- S06 Renae v2.5: keep minimalism; add micro-motion, colour beats, silence; "Each sentence = 1 motion beat"; 1–4 s per beat.
- S06's description of xkcd (stick figures, morphs over cuts, subject-colour accents) is *consistent* with the forensic decode's sparse states. The empty-space rule, though, comes from the forensic audit, not S06.
- S08 Niagara-through-a-straw example structure (cold open BUT → micro-arc THEREFORE → escalation BUT → payoff THEREFORE).
- Commandment 11 (awe and scale) and 15 (inevitable yet surprising payoff).

⚠️ **Contradicted:**
- S06's "every 2–3 s must deliver a micro-hook" conflicts with the observed long holds in the references and with S14.
- S06's 90-day % targets are invented.

🎬 **New creative output** (example):
- Question: "What if the Moon were made of water?"
- Beat 1 (BUT): stick figure looks up; the Moon is drawn as a blue sphere; "It would hold its shape… for about a day."
- Beat 2 (THEREFORE): the sphere visibly slumps into an oblate blob as a timer line advances; the consequence is drawn, not labelled.
- Beat 3 (BUT): the blob begins to boil off at the surface.
- Payoff: tide arrows on Earth change length, compared to today's.

*Every physical claim requires a cited calculation before production. The drawings must show state changes.*

🧪 **Test criteria:**
- Script review: each sentence maps to one state change (S06 rule), and no beat is a label-only noun.
- Pre-publish comprehension check with 10 viewers ("what changed and why?").
- Post-publish: retention through each segment relative to channel median; Test & Compare on two thumbnail concepts (object-consequence vs character-reaction).

## V.7 Case study 3 — Medical / senior-health education (first-party evidence + clinical safeguards)

🟢 **Beginner.** Older viewers want trustworthy, specific answers they can act on safely. Fear sells clicks but can harm people and trust. YouTube's search quality signals reward expertise and trustworthiness [S6].

🔵 **Evidence (owned channel "Decode Your Heart – Dr. Rehan", DS-000032, derived first-party, to 2026-09-27):**
- **Reach is small and mixed:**
  - Lifetime 8,366 views; 36,159 impressions; CTR 3.0%.
  - Shorts feed is the largest view source (5,355 views, AVD 0:19).
  - Suggested gives the most watch time (19.3 h; AVD 1:07; CTR 2.9%).
  - Search gives 1,175 views (CTR 2.71%).
- **Specific beats broad, in one pair (MEDIUM):** `BCNWQ3uuSuE` (specific lab-test utility) CTR 4.2%, 30-s retention 60.5%. `SBrMW71O69U` (broad warning) 2.87%, 38.46%.
- **Shorts acceptance and depth are separate:** stayed-to-watch 57.3% with APV 83.3% (`QfRaG71ZA_0`) vs 16.9% with APV 126.6% (`PTB-6fgaAKk`). Better acceptance did not guarantee more views (`FVfG_HZV4qg` vs `kF26QB7xHiE`).
- **Pace is not the lever:** 2 cuts → 87.1% at 3 s (`NznebmgFwXI`) vs 33 cuts → 57.89% (`KPYHy7MDmLM`).
- **Defects matter:**
  - `7MXBh2hjfto` title/content mismatch.
  - `UeGxF8-hb2s` black and silent 0:50–1:28 (44% of runtime).
  - Caption timecode defects in 10/56 transcripts.
  - 5 medical claims requiring action across 12 reviewed videos.
- External: senior-health competitor research (`docs/research/senior-health-2026-09-25/`). Repo claim matrix ALG26-CLM-001: bathing (507K) and eyesight (569K) winners had near-zero web-search demand, consistent with non-search discovery. Traffic sources are unknown for competitors.

📜 **Sources applied:**
- S14 §6 senior-health mode (governs):
  - Accuracy non-negotiable.
  - Authoritative sources.
  - No diagnosis from symptoms.
  - No cure language.
  - Who should avoid an exercise or food.
  - Red flags only when justified.
  - No infantilising.
  - "Calm authority plus emotional clarity".
  - Titles "around legitimate curiosity, not medical panic".
- S15's viewer-situation prompt ("someone worried at 1:30 AM") *for empathy*. Its "self-diagnosis anxiety" exploitation is rejected (C48).
- S08 medical BUT/THEREFORE example.
- S10 VEO doctor example: requires altered/synthetic disclosure if a realistic synthetic doctor is shown [S15]. Never show a synthetic person as a real clinician.

⚠️ **Safeguards (mandatory, per S14 §6 and YIOS DYH reviews):**
- Every medical claim gets a source and a reviewer.
- "Talk to your doctor if…" with specific red flags.
- No dosage instructions without clinical context.
- Thumbnails must not show fabricated test results or impossible transformations.
- Retention must never be invented for no-curve videos (the DYH builder enforces `LIMITED_BY_UNAVAILABLE_EVIDENCE`).

🎬 **New creative output** (example):
- Title: "The 30-Second Chair Test: What Your Result Means After 70 (and when to stop)".
- Hook: "If standing up from a chair has started to feel different, there's a simple 30-second test doctors use. But the number only means something if you do it safely — so here's the safe way first."
- Visual: the same drawn person and the same chair throughout. One stand = one tally. A stop palm when dizziness appears. This fixes each failure in the rejected prototype.

🧪 **Test criteria:**
- Medical review sign-off before upload.
- 30-s retention vs channel median.
- Test & Compare: "specific test + safety" vs "broad warning" packages, holding content constant.
- Comments monitored for misunderstanding. Correct in a pinned comment if needed.

🇵🇰 *Teen case studies: (1) Finance mein sachi calculation wali "X ya Y" videos; (2) What If mein har jumle ke saath tasveer ka badalna, sirf icon nahi; (3) Health mein khauf nahi, specific aur mehfooz jawab. Hamare apne channel mein specific lab-test wali video broad warning se behtar chali.*

---

# PART VI — Storytelling & Production Engineering (the integrated framework)

This part merges S02, S06, S08, S14, S17 and S18 with the YIOS production lessons into one framework. Rules marked ★ have YIOS or official support. The rest are craft heuristics, to be used as checks rather than laws.

## VI.1 The Promise Chain

Every element must carry the same promise forward:

```
Idea (demand)  →  Angle (the story inside the topic)
   →  Package (title + thumbnail = one promise)  ★ [S9 watch-time share judges it]
      →  Hook (confirms the promise fast)  ★ [S3; DYH 30-s retention pairs]
         →  Spine (BUT/THEREFORE turns; reveal inventory ≥7)
            →  Visual states (each shows a change/consequence)  ★ [YIOS rejected-prototype audit]
               →  Payoff (delivers exactly what was promised)  ★ [S7 clickbait pattern; S16 policy]
                  →  Echo / next question (cluster)  [S14; S18]
```

A break anywhere is a **promise failure**. Examples: thumbnail ≠ content (DYH `7MXBh2hjfto`), answer given too early (DYH `nP9fDHP1jbo` at 4–5 s), visuals that label nouns (chair-test prototype).

## VI.2 Script engineering checklist

| Check | Pass condition | Source |
|---|---|---|
| Throughline | One sentence states the central question | S17 #5 |
| Promise in opening | Title/thumbnail promise is audible and visible within the opening beat | S14 §3; [S3] |
| Turns | ≥7 meaningful "and then → BUT/THEREFORE" turns | S18 L352–396; S08 |
| Loops | 1 primary + ≤1 secondary open loop at a time | S14 §4D |
| Withholding | Answer delayed by tension, never by padding ("excessive withholding" is a failure) | S14 §4F; S15 p6 |
| Escalation | Stakes, scale or specificity rise in each third | S17 #2 |
| Midpoint re-hook | A new question at roughly 45–55% of runtime | S14 §4F |
| Evidence | Every factual claim has a cited source; numbers recompute | YIOS deep-audit practice |
| Payoff | "Inevitable yet surprising" and matches the title | S17 #15 |
| Echo / next | Returns to the opening question and bridges to one next video | S17 #16; S13 p1 |
| Language | Passes the "12-year-old / grandma" test; staccato opening, longer later | S17 #13; S02 pp 4–5, 42 |
| CTA | Only after value is delivered | S02 p8; S14 §4F |

## VI.3 Visual grammar rules

1. ★ **Show a state change, not a noun** (rejected chair-test prototype).
2. **One idea change = one visual state.** Hold while the idea holds. Empty space is fine if a relation develops (PR #44 audit). Compare S06 "Each sentence = 1 motion beat".
3. **Evidence before metaphor** for finance and news: source capture → pointer/highlight → metaphor → big number (observed in `Uumnx2Fo6cE`; describes one video and is not a causal rule).
4. **One asset family.** Never mix filled realistic figures with outline drawings (PR #44 audit).
5. **Causality in edits.** An object swap must not orphan another object (the floating-person error).
6. **Counts match actions.** One demonstrated action = one tally (PR #44 audit).
7. **Colour carries meaning, sparingly.** One accent (S02 p56); subject-colour accents (S06 p9).
8. **Readable at phone size.** Overlay 3–5 words; 12–16 characters per line for vertical (S02 p56).
9. **Audio supports beats.** A small sound at the contrast beat (S02 p7); silence as rhythm (S06 p12). In YIOS forensics, scene changes cluster at sentence starts (58% vs 10% chance) in `Uumnx2Fo6cE`; word-level sync is at chance.
10. **Synthetic media.** Disclose realistic AI people or events [S15]; keep identity consistent (S09; S10).

## VI.4 Editing pace

The DYH counterexample (2 cuts > 33 cuts at 3 s), S14's ban on timer resets, and the What If long holds together mean **pace is set by information change, not by a clock**. Use the conflicting intervals in the sources (2–3 s … 3 min) only as *audit prompts*. Ask "has anything new happened in the last N seconds?" and never treat the answer as a mandatory cut.

## VI.5 Thumbnail–title engineering

- Write the viewer's **pre-click question** (S15 p9) and make the package answer *"why should I find out?"*, never the answer itself (S15 p21).
- **Complement, don't repeat:** if the title says the number, the thumbnail shows the consequence (S14 §4C).
- Make three meaningfully different hypotheses (decision, identity, contradiction). Test natively [S9].
- Signal format and length truthfully (S05 step 6).
- Medical: no fabricated results, no impossible transformations (S14 §6).

🇵🇰 *Poora nizaam aik "wada zanjeer" hai: idea → angle → title/thumbnail → hook → kahani → visuals → payoff → agla sawal. Kahin bhi wada toota to viewer chala jata hai.*

---

# PART VII — Complete Operational SOP (checklists and templates)

## VII.1 Pre-production

**Step 1 — Audience card**
```
Viewer:                     Watching situation (time/device/state):
Present tension (pain/fear/desire/confusion/identity/aspiration):
Audience sentence: "My audience wants ___ because they want to feel ___."
What they already believe / suspect:
```

**Step 2 — Demand evidence (≥3 rows)**

| Source video | Channel | Peer ratio or "views vs normal" | Hidden demand | Angle doors opened |
|---|---|---|---|---|

Rule: one viral video ≠ demand. You need a pattern on ≥2 channels, or repeated outperformers on one channel (S18 L227–259).

**Step 3 — Angle sheet** (per S14 §4B). Generate ≥5 distinct angles. For each, record: core event | emotional trigger | viewer question | promised payoff | visual proof | factual/medical risk. Reject angles without a true payoff.

**Step 4 — Package hypotheses** (before the script). Three variants: title, thumbnail concept, which pre-click question each raises, and why it is honest.

**Step 5 — Hook draft.** Context Lean → Scroll-stop → Snapback (or Headline → Shocker → Misdirection). Key visual named. First value within the opening beat.

**Step 6 — Script and reveal inventory.** BUT/THEREFORE spine; count turns (≥7); midpoint re-hook; payoff; echo; one next-video bridge.

**Step 7 — Fact-check sheet**

| # | Claim (verbatim) | Source + date | Recomputed? | Reviewer | Medical/financial risk |
|---|---|---|---|---|---|

**Step 8 — Storyboard table**

| t | Script line | Visual *state change* | BUT/THEREFORE role | On-screen text (≤5 words) | Audio | Asset family |
|---|---|---|---|---|---|---|

## VII.2 Production QC (before export)

- [ ] Every state shows a change; no label-only noun beats
- [ ] Single asset family; no orphaned objects; counts match actions
- [ ] No black or silent gaps (DYH `UeGxF8-hb2s` defect class)
- [ ] Caption timecodes correct (10/56 DYH transcripts had defects)
- [ ] Title promise delivered (compare with title text)
- [ ] Disclosure decided honestly [S15]; audience setting correct; no misleading metadata

## VII.3 Publishing

- [ ] Title (decide search-led or browse-led; don't mix)
- [ ] Thumbnail variants loaded into Test & Compare (eligible long-form) [S9]
- [ ] First two description lines: what the viewer will learn and the method or source
- [ ] Chapters only if they help navigation (useful for calculation/tutorial videos; S13 opinion that chapters hurt stories is untested)
- [ ] Tags: only misspellings or variants [S17]; hashtags ≤ a few, never >60 [S14]
- [ ] End screen → the viewer's next question; playlist placement
- [ ] Pinned comment adds value or a correction
- [ ] Notifications ON (staff advice against unchecking) [T39 ch. 12]
- [ ] No fake engagement, no proxies, no "warm-up" tricks (policy risk)

## VII.4 Post-publish analytics routine

| When | Look at | Decision rule |
|---|---|---|
| Hours 0–48 | Nothing decisive. Check only processing, restrictions and obvious defects | Don't change packaging in panic (S18; [T39 ch. 4, 12]) |
| Day 7 | Impressions by source; CTR **by source**; Subscriptions-feed CTR vs your other videos | Low subs-feed CTR vs peers → content/packaging appeal problem [T39] |
| Day 7 | Retention curve: first major dip, 30-s retention vs length band | Dip at a known beat → fix that beat *in the next video* |
| Day 28 | Peer ratio vs your own videos at the same age; returning viewers; Test & Compare verdict | Record in the experiment log; one variable per next video |
| Monthly | New/casual/regular viewers; top suggested sources | Cluster planning |

**Diagnosis ladder** (S18 + S14 merged):

| Pattern | Layer | Action |
|---|---|---|
| No impressions | Distribution / clarity | Clarify topic and person; check restrictions; next video more recognisable |
| Impressions, low CTR (vs own baseline, per source) | Packaging | Test & Compare |
| CTR ok, early drop | Hook / promise | Rewrite opening; confirm promise |
| Good intro, middle decline | Escalation / density | More turns, less repetition |
| Good watch, weak return | Loyalty | Next-step design, personality, series |
| High views, complaints | Overpromise | Fix package; pinned correction |

## VII.5 Experiment log template

```
ID | Date | Video | Hypothesis | Variable changed (ONE) | Held constant | Metric + threshold (pre-registered)
   | Result day 7 | Result day 28 | Verdict (supported / not / inconclusive) | Lesson | Next action
```

## VII.6 Templates for prompts (honest versions)

- **Lens review prompt** (from S01/S07/S17, corrected by S14 §5): "Review this script through seven lenses: structure, myth/meaning, virality, retention risk, curiosity questions, clarity, integration. These are internal lenses, not separate experts. Return one reconciled recommendation, the single biggest risk, and one measurable prediction."
- **Angle generator** (S15 p3, safety-amended): "Identify the core event. Generate 12 titles using distinct lenses. Each must imply a true story with a real payoff. No medical panic, no fabricated urgency. Mark any title whose claim needs a source."
- **Viewer situation** (S15 p8–10): keep as written. It is about empathy, not exploitation.

🇵🇰 *SOP: audience card → demand ka saboot → 5 angles → 3 packages → hook → kahani → fact-check → storyboard → QC → publish → 7/28 din ka jaiza → aik waqt mein aik tajurba.*

---

# PART VIII — Advanced Research Methods

## VIII.1 The peer ratio (YIOS's core outcome measure)

For a target video *v* on channel *c*, format *f*, in snapshot *s*:

```
vpd(v)   = views(v) / age_days(v)              (age measured at snapshot; v must be ≥ 7 days old)
Peers(v) = up to 10 videos on (c, f, s) with age in [0.5·age(v), 2·age(v)], nearest in age; require ≥ 5
ratio(v) = vpd(v) / median{ vpd(p) : p ∈ Peers(v) }
Tier: STRONG ≥ 2;  WEAK < 0.5
```

*Why:* this removes channel size, format (Shorts vs long-form) and most of the age effect. *Validation:* reproduces stored `Lifetime_rate_ratio` with max relative difference 7.1e-5. *Limits:* lifetime public reach only; no impressions; frozen snapshots; undated datasets are excluded.

## VIII.2 Testing a creative hypothesis on observational data

1. **Code features mechanically or blind.** Do not code from analyst prose, which quotes outcomes and so leaks them.
2. **Stratify within channel.** Effect = weighted mean over channels of [mean log ratio(feature) − mean log ratio(no feature)], reported as a multiplier `exp(effect)`.
3. **Permutation test.** Shuffle labels within channel (4,000 permutations) to get *p*.
4. **Bootstrap CI.** 1,500 resamples.
5. **Multiple testing.** Benjamini–Hochberg *q* across the pre-declared family (14 primary tests).
6. **Sensitivity.** Leave-one-channel-out (LOCO) and temporal halves.
7. **Replication.** Apply the frozen rule to unseen channels (418 videos).
8. **Prediction check.** Does a model (ridge, λ = 5) beat the peer-median baseline on temporal and unseen-channel splits? Report MAE with bootstrap CI of the gain.
9. **Counterexamples.** Always list them (V.1).

Seed `20261026`; stdlib only. Code: `YIOS-Algorithm-Audit-2026-10-26/scripts/analyze.py`. These results were `RECEIPT_REVIEWED_AND_QA_RERUN` today; the full analysis was not re-executed.

## VIII.3 Experimental design for owned channels

- **Native Test & Compare** [S9]: randomised by YouTube, judged on watch-time share. This is the best causal tool available.
  - Isolate one component (thumbnail-only, with the title fixed) when you want a mechanism.
  - Paired variants test the package.
  - Respect Inconclusive results. Do not peek and stop early.
  - Shorts are ineligible.
- **Sequential within-channel tests** (opening styles, angle families) are *not* randomised. Use ≥6–10 videos per arm, alternate the arms, match topic families, and compare against each video's own length band and age-matched peers.
- **Matched pairs** (the DYH method): same channel, similar topic and length. Record competing explanations and confidence. Make no causal claims.
- **Pre-registration:** write the metric and threshold before publishing (VII.5).

## VIII.4 Validity threats (checklist)

| Threat | Example in YIOS | Mitigation |
|---|---|---|
| Outcome leakage | Analyst prose cites "Weak 0.14×" | Blind or mechanical coding only |
| Survivorship | What If decodes = hits only | Decode low performers too |
| Channel confound | 38–58% of variance between channels | Within-channel stratification |
| Age / snapshot | Frozen 2026-09 snapshots | Peer ratio; repeat snapshots |
| Format mixing | Shorts vs long-form view units | Separate analyses |
| Historical packaging unknown | Thumbnails may have changed | Treat packaging as current-only |
| Multiple testing | 14+ features | BH correction; replication |
| Small n | DYH 56 videos; VF n = 2 | Label confidence; no causal claims |
| Concentration | Nick Invests dominates Finance | LOCO |
| AI-generated "evidence" | S02 "28–62%" template line | Source criticism (II.0) |
| Private data | DS-000032 derived analytics | Keep private; aggregate in reports |

## VIII.5 Evidence standards for adding a "rule" to YIOS

A creative rule can be promoted from `CREATIVE_HEURISTIC` only if **all** of the following hold:

1. It has a pre-declared metric.
2. It produced an effect within channel.
3. The effect survives multiple-testing correction.
4. It replicates on unseen channels, or in ≥2 native Test & Compare wins with no losses on owned videos.
5. It has counterexamples documented.
6. It does not conflict with official policy.

No title, hook or pacing rule meets this standard today.

🇵🇰 *Kisi creative rule ko "saabit" kehne ke liye: pehle se tay metric, channel ke andar asar, multiple-testing correction, naye channels par dobara asar, aur counterexamples. Abhi koi rule is maiyar par poora nahi utarta.*

---

# PART IX — Decisions & Roadmap

## IX.1 What YIOS actually knows

1. YouTube optimises per-viewer long-term satisfaction with no public formula [S1; T39].
2. The channel/audience fit dominates measurable variance; hits are concentrated.
3. Title-wording "formulas" did not replicate, and predictive modelling from titles/duration failed.
4. Concrete decision-math concepts recur as cross-channel winners (hypothesis).
5. Competitor finance content often has arithmetic flaws (claim receipts) — a credibility gap.
6. On the owned medical channel:
   - Reach is small: CTR 3.0% lifetime.
   - Suggested traffic watches longest.
   - Specific packages beat a broad one in a matched pair.
   - Pace did not predict holding.
   - Production defects exist.
7. YIOS's own visual prototype failed by labelling nouns instead of showing consequences.

## IX.2 What remains missing

- Competitor CTR, retention and traffic. These are unobtainable; do not ask for competitors' Studio access.
- Repeat competitor snapshots (velocity).
- Transcripts for 646 expansion videos.
- Blind packaging coding.
- Upload-era thumbnails.
- Visual Forensics Video 003 (Machine A).
- Low-performer What If decodes.
- DS-000032 per-video traffic-source drill-downs and new/casual/regular monthly re-exports (listed as remaining in the DYH checkpoint).
- The 9+ external sources referenced in S15 but absent (Part X.3).

## IX.3 Priority experiments (owned channels only)

| # | Experiment | Design | Success metric | Prerequisite |
|---|---|---|---|---|
| E1 | Specific vs broad medical packaging | Test & Compare on 3 mature eligible DYH long-form videos | Watch-time-share winner; then CTR + 30-s retention | Medical review of both packages |
| E2 | Opening style | Question-open vs stake-statement-open, 6+ videos per arm, alternating | 30-s retention vs length-band median | Same topic family |
| E3 | Consequence-state visuals | Two edits of one segment; unlisted comprehension check + live segment retention | Comprehension ≥8/10; segment retention ≥ median | Production capacity |
| E4 | Decision-math finance pilot | 3–5 pilots across subjects (rent/buy, cash/finance, $X/month) | Day-28 peer ratio ≥1 once peers exist; zero math corrections | New/owned finance channel |
| E5 | Topic cluster after a hit | Follow any STRONG video with 2–3 next-question videos | Returning viewers; suggested from own channel | A STRONG video |
| E6 | Search-led companion | Search-intent version of a browse winner | Search impressions + CTR (search) | Studio search terms |

## IX.4 Implementation changes proposed (NOT executed; need owner approval)

1. Update `FINANCE_UNIVERSE.csv.audit_status` from the live ledger (stale 430 vs 449).
2. Refresh the `expansion-12-channel-2026-10-20` checksum manifest after the README edit.
3. Normalise `video_type` labels and `published_at` formats in the registry.
4. Add a `source_class` field (CREATOR_SOP / AI_PARAPHRASE / AI_OS / PROMPT_LIBRARY / TRANSCRIPT / OFFICIAL) to knowledge records. Tag invented numbers as `UNSOURCED_NUMBER`.
5. Register DS-000032 derived analytics in the registry's first-party layer (privacy-preserving), so that "first-party = 0" stops being reported.
6. Retire numeric thresholds from prompts: 10% CTR, 20–30 s resets, 55/60/70-character title caps, 8-minute minimum.
7. Add the chair-test failure lessons (VI.3 rules 1–6) to the production QC.

## IX.5 Prerequisites

Each item needs separate owner authorisation:
- Any repository write or commit.
- Paid scraping or downloads.
- Machine A access (Visual 003, raw Studio ZIPs).
- Making the repo public. The DS-000032 privacy class requires history handling first.

---

# PART X — Source and Evidence Appendix

## X.1 Original sources (SHA-256, size, pages)

All at `data/raw/global-youtube-knowledge/` in HEAD `d987510b`. The identical blobs exist on all 79 local refs; no alternate versions were found in branches or history.

| ID | File | SHA-256 | Bytes | Pages | Words extracted |
|---|---|---|---|---|---|
| S01 | DS-000011/Engine-by-Engine Personality & Lens (Cinematic-Psychological Profiles).docx.pdf | 09b5a16f89d9645532e85c7b3c2322162d8b7cf4a84429123af4a4d8d525675f | 130,832 | 3 | 868 |
| S02 | DS-000011/Hook (1).pdf | 4129b210dba81ecb527d42730e3ed7458e68feb7b0d921c82baaa3d6a6e433e9 | 682,676 | 58 | 10,003 |
| S03 | DS-000011/Hook guide.pdf (text ≡ S02) | 4bbe6c6e34b2279aacbd584e26c4ce8e6155eaba1e4193387f8a1a1161ee3c54 | 682,682 | 58 | 10,003 |
| S04 | DS-000011/Intro Analyzer Prompts.docx (1).pdf | cb50fe7ec9002fc2c9435818dff22aa801710280040918fbfb4208012a1a1679 | 76,967 | 2 | 469 |
| S05 | DS-000011/Packaging (Thumbnail_Title) - SOP(1).pdf | b59c1a19427812c977939e795b255c000986278b6d97db2a982d7ef12565555c | 89,849 | 1 | 340 |
| S06 | DS-000011/Renae_Creative_Engine_v2.5_Unified_Intelligence_Blueprint.pdf | aacc8fc2373df717450b9d9d63ff8d96027dfa6f3e97381fd74db80b12b0f3c3 | 352,994 | 12 | 2,047 |
| S07 | DS-000011/Script Analyzer.pdf | 6d9840bbe0caa759a91819392e7df33d547a656ffd153bc51cb1f196dd539354 | 78,002 | 2 | 671 |
| S08 | DS-000011/The Magic of 'BUT' and 'THEREFORE' in Storytelling.docx (1).pdf | 52235e9459a8d7364229502474071c2635bdd4810d51ebff86c4d53460d9495e | 218,253 | 3 | 1,184 |
| S09 | DS-000011/The Ultimate Nano-Banana Prompt Guide.docx | 445c7efa1420d0ae391ea27f1fffd2032d80898f18761a1d99eddae65ad451c5 | 1,011,212 | — | 754 |
| S10 | DS-000011/Ultimate Google VEO 3 Prompt Guide for VIRAL Videos.docx | ccbee7dd74453abc2261769a0c686cef94e2fe6ab3a50141e257a754680ab7c5 | 26,005 | — | 3,747 |
| S11 | DS-000011/Viral Checklist.pdf | 2d31bc62bc873eed7ba11d3ec5eb10181d0bcd778af78bd5678d91758ff22fd3 | 83,373 | 2 | 294 |
| S12 | DS-000011/YouTube Title Analyzer — Natural Language Prompts (2).pdf | 8b65784803f2cc6e0cb7b7cf2ebef8ed36110c91cae22a2f63416d529d0d57ba | 136,532 | 6 | 1,728 |
| S13 | DS-000011/YouTube algorithm guide.docx (2).pdf | d0f681ddcabed20ba6bd739133d68ae871f6a9ebfa4bbad9cf6b4095e5ccf274 | 2,626,862 | 117 | 47,422 |
| S14 | DS-000011/YouTube_Intelligence_Brain_v1_Verified_Creator_OS.md | 115e9d3974b136513c26adfd73df2385815b9d721006c3a84c17c19588a69950 | 20,885 | — | 2,931 |
| S15 | DS-000011/new YT algorithms updates.pdf | 62565f03d2c156433c11d663d8664d006faf5e46499e7b19d08f8fac166b3d56 | 404,341 | 45 | 8,989 |
| S16 | DS-000011/🎯 YouTube Video SEO – COMPLETE CHECKLIST DOCUMENT (1).pdf | 63c5338e6a9e4489f30a6b2023dcf8113c62bc17952d9221b48f6edf689506f5 | 170,257 | 13 | 942 |
| S17 | DS-000011/📜 Seven Engine Storytelling Analysis Prompts (16 Commandments Integrated).pdf | 242707556f8156010abfd96c8465f885274cb3a759ccbd95ccbd79a66d502bed | 210,886 | 6 | 1,510 |
| S18 | DS-000031/creator-strategy-audience-psychology-experimentation-corpus.txt | ab555773faf5b04158aba4d61ebbb4310ac95bb299d07562074556ccfe6d3533 | 70,730 | — | 1,426 lines |
| S19 | DS-000018/2026 Algorithm Update - Google Docs tab snapshot.zip | 3992987b88dd4faa16f37b84b502d38b1defaab8fdef8c03722baa1622855a1f | 566,739 | 63 tabs | 245,901 |

**Coverage:**
- S01–S18: full text read.
- S19: all 63 titles indexed. Tab 39 read in full. Targeted numeric-claim extraction across all tabs (`ledger/ds18_targeted_claims.txt`). The other 62 tabs were **not** read word-for-word.
- Embedded figures and tables in S01, S06, S08 and S17 were read through layout-preserving text. No PDF contains essential images that text extraction loses, except S02/S03 (embedded video thumbnails or links; filenames only).

## X.2 The 15 brief targets — discovery status

All 15 are `FOUND_EXACT` (S01–S08, S11–S17 above). The two Hook PDFs are one source (identical text, distinct hashes). Additional relevant files found: S09, S10 (DS-000011), S18 (DS-000031) and S19 (DS-000018). Full ledger: `ledger/SOURCE_DISCOVERY_INVENTORY.csv`.

## X.3 Not found or inaccessible

| Item | Status |
|---|---|
| `YIOS_Original_Frameworks_Source_Extraction_2026-10-26.md` (owner extraction pack) | NOT_FOUND on Machine B (repo, all refs, ~ depth 4) |
| Legendary YouTube Thumbnail Analyzer (DOCX); 10 Intro Templates by Jon Youshaei; The MrBeast Playbook by Jon Youshaei; The Casey Neistat Playbook by Jon Youshaei; RenaeGem — The Cinematic–Algorithmic Mastermind; the "prompts" Fusion Framework PDF; YouTube algorithm guide.docx (1); the original Ultimate Google VEO 3 Prompt Guide PDF; 9 image boards/slides ("YouTube's 2026 Algorithm: 9 Game-Changing Updates", "Trust Score Cheat Sheet", "Read Your Audience's Mind", "Inauthentic Content", "2026 Strategy Playbook", "10 rookie mistakes", "Master the Hook", timing and research slides) | NOT_FOUND (referenced in S15/S10). Their content survives only as AI summaries (S15 pp 22–45) and as S14's synthesis |
| `~/Downloads/Unlock_The_Secrets_of_YouTube_Growth_–_Own_53_Secret_ChatGPT_Prompts.pdf`; `~/Downloads/YIOS_Complete_YouTube_Algorithm_Intelligence_Guide_2026-10-26.pdf` | DISCOVERED_OUTSIDE_SCOPE_NOT_READ |
| Raw YouTube Studio ZIPs (DS-000032, 69 ZIPs: 60 retention, 4 content, 3 traffic, 1 device, 1 geography); Visual Forensics Video 003 | INACCESSIBLE (Machine A). Derived DS-000032 measurements are in the repo and were used |
| `knowledge/youtube/` (30 files; 2026-10-15 knowledge consolidation, incl. `SOURCE_CATALOG.csv` 5,976 locators) | FOUND_SECONDARY — used for discovery only, never as evidence; every claim in this guide was re-read from S01–S19 |

## X.4 YIOS data locators used

- `data/catalog/youtube_channel_registry.db` — SHA `39e7a28ba592b9022bd1b32f4c288edde519730164a98ea858ce90c44d52f654`
- `data/catalog/youtube_inventory.db` — SHA `277c09f64bc71678a0ae52c0084be8bde4f38db87dba52b12bbac59c6914618d`
- `research/finance-economics-intelligence/VIDEO_AUDIT_966.jsonl` (live ledger)
- `research/finance-economics-intelligence/reconciliation-all-repository-2026-10-21/FINANCE_UNIVERSE.csv`
- `research/visual-forensics/INDEX.csv`; `research/visual-forensics/channels/casual-finance/Uumnx2Fo6cE/research/key_facts.json`
- `docs/research/decode-your-heart-2026-09-27/Decode_Your_Heart_Research_Checkpoint.json` (DERIVED_PRIVATE_ANALYTICS)
- `docs/audits/DECODE-YOUR-HEART-PRIVACY-CLASSIFICATION-2026-10-03.md`
- `docs/research/senior-health-2026-09-25/forensic-v2/DS-000018-CLAIM-MATRIX.json`
- `docs/research/thumbnail-forensics-2026-10-02/REPORT.md`
- `docs/research/packaging-validated-2026-10-11/README.md`
- `data/manifests/DS-000011.md`, `DS-000018.md`, `DS-000031.md`
- `data/intelligence/global/creator-strategy-knowledge-DS-000031.json` (segment line ranges)
- PR #44 ref `origin/codex/what-if-archive-main-integration` @ `badec432`: `research/production-experiments/what-if-derived/chair_test_v2_review/FAILED_VIDEO_VISUAL_AUDIT.md`
- `scripts/run_youtube_intelligence.py` and `scripts/report_*.py` (V1 modules)
- Statistical receipts: `/Users/ghilmanislam360/Documents/YIOS-Algorithm-Audit-2026-10-26/derived/analysis_results.json`, `receipts/census.json`

## X.5 Denominators

| Statement | Denominator |
|---|---|
| Title tests | 723 original rated videos (11 channels); replication 418 |
| Concentration 66.9% | median over 33 registry channels with dated snapshots |
| Variance share | Finance originals / registry all niches |
| Like-rate inversion | 9 channels |
| DYH CTR 3.0% | 36,159 lifetime impressions, 57 rows |
| DYH retention curves | 46 of 56 videos |
| Visual states 507 | one video (`Uumnx2Fo6cE`) |
| What If grammar | 14 decoded videos |

## X.6 Major internal contradictions in the sources

| Topic | Conflicting statements |
|---|---|
| CTR target | 10%+ (S05) · 6–12% (S16) · >7% (S13 p32) · 9–12% / ≥10% (S13 p54, 59) · 1–3% Shorts (S13 p97) · none (S14) |
| Reset cadence | 2–3 s (S06 p8) · 8–12 s (S08) · 10–15 s (S13 p60, 80) · 15–30 s (S02) · 20–30 s (S17, S06) · 20–40 s (S01) · 25–40 s (S06) · 60 s (S13 p78) · 60–90 s (S18) · 2–3 min (S08) · no timer (S14) |
| Title length | 55 chars (S12) · <60 (S16) · ~70 (S13 p47) · no arbitrary cap (S14) |
| Video length | "3–10 min dying" (S13 p92) · 8+ (S13 p58) · 10–12 (S13 p59) · 14–20 (S13 p55) · 15–30 (S13 p51) · don't stretch to 8 (S14) |
| Upload device | phone (S13 p49–50, 73) · desktop (S13 p62) · doesn't matter (S13 p82) |
| Publishing | schedule 24–48 h (S13 p62) · private 12–24 h (S13 p107) · official: publish time no long-term effect [S1] |
| Uploads before breakout | 20–30 (S13 p38) · 30–45 days (S13 p56) · 50–100 (S13 p109) |
| AI disclosure | kills reach (S13 p74) · doesn't reduce reach (S13 p47; S14; [S15]) |
| Faces in thumbnails | "No face" = mistake (S16) · only when truthful (S14) |
| Gemini persona | Story Architect · Mythic Storyteller · Story Surgeon · Narrative Surgeon · Narrative-Algorithm Fusion |
| Health framing | exploit self-diagnosis anxiety (S15) · no medical panic (S14 §6) |

## X.7 External references

See `ledger/EXTERNAL_SOURCES.csv` (S1–S18, T39), with URLs, publication and access dates. All were accessed 2026-10-26, except S9b (repo receipt dated 2026-10-02).

---

*End of guide. Verification receipts: `ledger/VALIDATION_REPORT.md`. Continuation: `ledger/CONTINUATION_HANDOFF.md`.*
