# 02a — Playbook Framework Extract (YouTube Automation Complete Master Playbook)

- Source: `~/Downloads/YouTube_Automation_Complete_Master_Playbook.pdf` (557 PDF pages; pdftotext read in full, see §13).
- Extracted 2026-11-11. Page numbers = PDF page index (not the course's internal page numbers).
- Status of this file: EXTRACTED OBSERVATIONS of what the source says. The source is a course compilation (creative heuristics, owner preferences, unverified platform claims). Nothing here is a platform fact unless §11/§12 says Part D supports it, and Part D itself was not independently re-verified by this extraction.
- Quoting: wording is paraphrased; verbatim quotation was deliberately kept to a minimum. Title templates in §5 are the source's fill-in patterns.
- The source contains many prompts addressed to an AI. They are described here, not executed.

---

## 1. Outlier method (p6–9; variants p28, p34, p90–91, p94, p100, p113, p123; critique p554)

**Definition (p6):** a video that far outperformed what the uploading channel's size predicts; the excess is attributed to topic + packaging, not the channel.

**Formula — the source is internally inconsistent (record which one you use):**
| Variant | Denominator | Where |
|---|---|---|
| A (Lesson 2.1) | channel subscriber count | p7, p9 |
| B (Lesson 2.7) | subscribers in one screenshot, channel average views in another; compiler preserved both | p28 |
| C (Topic Method 1) | channel average view count | p34 |
| D (validation prompts) | "channel typical views" | p100, p113 |
| E (Repackage engine) | "fair baseline": nearby uploads, channel norms, comparable videos, age | p123 |
| F (Part D, new) | median views of comparable uploads of similar format and age | p554 |

**Thresholds (variant A, p7):** 1–3x normal; 5–10x strong performer; 10–50x clear outlier; 50–100x+ mega outlier. Method 1 uses 10x+ on variant C (p34). Prompts D use labels Normal / Moderate / Strong / Extreme Outlier with no numeric cut-offs (p100–101, p113).

**Channel-size filters:** 1K–100K subs, 20+ uploads, similar content (p6–7); parenthetical says "quality" niches may go up to <1M (p6–7); Method 1 says 5K–200K (p34). Small channels (1K–10K) are preferred as cleaner topic signals (p8).

**Steps (p6–8):** (1) find 10–15 niche channels; (2) sort by Most Popular, compute ratio; (3) analyse why — aim for 30–50 outliers; (4) build the database; (5) cross-validate: same topic as an outlier on multiple channels = strongest signal, top of calendar.

**Record per outlier (p7–8):** Channel | Subscribers | Title | Views | Outlier Ratio | Topic (precise) | Title Structure | Thumbnail (subject, text, emotion) | Format | Length | Top 20–50 comments (what viewers want more of) | Upload date + triggering event vs evergreen | Notes.

**Niche validation by outlier count (p8, p9):** 20+ outlier topics at 10x+ across 10–15 channels = green light; 3–5 = too narrow (broaden/bend); 0 = no proven demand.

**Velocity check (p9):** same views over 3 years = evergreen/slow; in ~2 weeks = active Browse/Suggested demand (highest priority); spike-then-flat = event-driven, check recurrence.

**Additional signals (p90–91, p94):** repeated outliers > one viral accident; cross-channel validation; topic depth ("can I make 100?"); freshness (format still works on recent uploads); judge views relative to subs AND to channel average, number of similar winners, recency.

**Part D caveats (p554):** views/subs is noisy (subs change, age differs, traffic source unknown); an outlier shows interest in that video under its publishing conditions, not continuing demand or causation. Add: upload date, age in days, views/day, median of comparable uploads, topic cluster, freshness trigger, source URL. Do not compare ratios across Shorts and long-form.

## 2. Niche vs Format vs Template; Format Arbitrage; Niche Bending

**Three layers (p11–13):**
- NICHE = who you serve: audience segment + persistent interest + monetisation pathway. Not a topic.
- FORMAT = repeatable delivery structure. Ten listed: Listicle/Countdown, Then & Now, Biography/Story Arc, Explainer/Deep Dive, What Happened To, Comparison/Versus, Documentary/Investigative, Reaction/Commentary, Timeline/Chronology, Myth-Busting (p12). One niche supports many formats.
- TEMPLATE = the fill-in script/editing blueprint inside a format. Example 7-part Then & Now template with timestamps: Hook 0:00–0:30, Origin 0:30–2:30, Fame Peak 2:30–4:30, Behind the Scenes 4:30–6:00, After 6:00–8:00, Today 8:00–9:00, CTA + tease 9:00–9:30 (p12–13).
- Why it matters (p13): variety without losing identity; rotate 3–5 templates per format to avoid repetitive-content flags; templates enable delegation; add a format to expand without changing niche. Cross-niche table is truncated after item 4 (p13).
- Six multi-act template skeletons (p14): Resurrection Arc, Villain Reframe, Mystery Unpack, Downfall Formula, Underdog Blueprint, Mind Shift (Hook → Common Belief → Why Believed → Counter Evidence → Truth → New Perspective → CTA). Templates 7–10 not visible.
- Related vocabulary: SUBJECT / TOPIC / ANGLE / FORMAT (p122); TOPIC vs FORMAT vs FINAL TITLE (p53); Niche vs Angle vs Working Topic vs Final Title, angle formula = Subject + Lens + Viewer Payoff, angle must yield 50+ ideas (p510, p513).

**Format Arbitrage (p18–20):** move a format proven in niche A into niche B where it is absent/underused.
- Steps: (1) survey 5–10 other niches, find 2–3 dominant formats each with outlier ratios across multiple channels; (2) ask whether anyone in the target niche uses it; (3) validate: fits the audience? 50+ videos possible? naturally fills 8+ minutes?; (4) publish 3–5 videos, compare CTR/AVD to niche benchmarks.
- 10-Minute Audit (p19–20): list 10 formats (Then & Now, Iceberg, Top 10, What Happened To, Day-in-the-Life, Comparison, Myth-Buster, Timeline, Challenge, Transformation); search "[niche] + format"; score: many established results = saturated, few/small channels = opportunity, zero = open but validate demand. Keep a running Format Library.
- Validation prompt (p111–120), 13 steps: decode the format into an abstract psychological formula; verify source-format strength (repeatable vs one celebrity; multiple channels; recent); target-audience demand for the underlying psychology (exact-format demand vs underlying demand); psychology-distance score 1–5; 20-title stress test (flag if <12 A-level); celebrity-power test (Tier 1/2/3); topic inventory (Tier A–D; 30/50/100 videos; idea vs series vs niche); payoff test BEFORE → EVENT → AFTER; thumbnail transfer /5; packaging gap ("nobody is doing it" may be absent demand); 5-video pilot; score 10 categories ×5 = /50 (43–50 very strong, 37–42 pilot, 31–36 experimental, 25–30 weak, <25 reject; any critical ≤2 is a potential kill); verdict GREEN / YELLOW (series only) / RED. Inputs required listed p111.

**Niche Bending (p24–26):** combine two adjacent niches to serve the overlap.
- Process: list 5–10 candidate niches; build a pair matrix; validate; test with first 10 videos (impressions, CTR vs niche, AVD, subscribes).
- Five validation tests (p24): audience overlap (cross-suggestions, shared channels, comments); outlier cross-check at the intersection; 50+ ideas depth; CPM viability; competition scan (5+ established = no longer open, 0–2 = early).
- Mistakes (p25): forcing unrelated niches, both low-CPM, too narrow (<50 ideas), drifting out of the intersection, ignoring audience vocabulary. Bending = strategic (where), arbitrage = tactical (how); beginners may skip bending (p26).
- Validation prompt (p97–109), 19 steps incl.: core audience desire sentence; bend type (Topic/Emotional/Audience/Perspective/Format/Era/Demographic/Storytelling); Audience Bridge 1–5 on viewing behaviour; crossover evidence STRONG–NONE; viewer-expectation class CORE / SAFE / AGGRESSIVE / TOO FAR; 20-topic stress test (flag if <12 A/B); same-viewer test; GREEN/YELLOW/RED content-distance zones; packaging = familiarity + novelty; celebrity dependence; topic inventory; identity sentence; fragmentation risk; graduated 5-video pilot; metrics to watch; 12 categories ×5 = /60 (51–60, 44–50, 36–43, 30–35, <30); verdicts GREEN / GREEN AS SERIES FIRST / YELLOW / RED. Data needed table p97.

## 3. Competitor research — Module 2.7 "15-Minute Channel Audit" (p28–30)

Run on 10–20 competitors at start, then 2–3/week.
| Minutes | Step | Fields to capture |
|---|---|---|
| 0–2 | Channel snapshot | name, subs, total videos, creation date, uploads in last 30 days, est. monthly views |
| 2–5 | Top 10 by Most Popular | exact titles + structure (question/number/emotion/gap/length), views + outlier ratio, lengths (avg of top performers), topics, formats |
| 5–8 | Thumbnail teardown | colours, text (word count, font), faces/expressions, focal object, before/after, template consistency |
| 8–11 | Cadence & growth | uploads/week over 3 months, days/times, growth inflection + what was uploaded then, early vs recent content, dead periods |
| 11–13 | Hook & script | first 30s of top 3: opening type, time to point, VO style, pattern interrupts, transitions; then 40–60% mark: pacing sag, visual variety, tightness |
| 13–15 | Comments | top 30–50 on 3 top videos: requests, complaints, emotional responses, questions, debates |

**Steal File (p29–30), six sections:** Title Templates (30–50 patterns), Thumbnail Patterns, Hook Formulas (question / bold claim / what-if / story / stat), Format Playbook, Topic Bank, Anti-Patterns (large-channel flops and why).

Related templates: Practical Month competitor teardown — one big, one mid, one new channel; avg views of last 10; transcribe first 30s of top video; what they do badly (p494). Niche template — 10 minimum, 15–20+ competitors with link, subs, recent avg views, angle/format; outlier table (views/age, why it worked, what to adapt) (p511–512).

## 4. Topic selection methods (p33–50)

The masterclass advertises 12 methods (Part A new channels ×6, Part B established ×3, Part C hybrid ×3); **only Methods 1–4 are present** (p33, p37). Target surfaces: Browse and Suggested (p33–34).

**Method 1 — Outlier Transplant (p34–35):** (1) 10–15 same/adjacent-niche channels, 5K–200K subs; (2) outliers at 10x+ (÷ avg views), top 3–5 per channel → 30–50+ topics; (3) demand check: search topic, views of top results, recency, still growing; (4) supply check: 2–3 good videos with millions = room, ~50 good videos = saturated; (5) apply your own format; (6) attach a proven title format. Tip: best transplants come from adjacent niches.

**Method 2 — Title Template Injection (p39–40):** library of formats (9 of 10 visible): Psychology of X; What Happened to X?; Why X Was Actually [claim]; Rise and Fall of X; X Explained in [time/way]; Dark Side of X; How X Actually Works; [N] Things You Didn't Know About X; Untold Story of X. Steps: pick 3–5 formats from outliers; list 20–30 topics; build topics × formats matrix (30×5 = 150); filter by (a) genuine curiosity, (b) proven demand, (c) would I click — keep 20–30; search-validate each (absent angle = gap; present but weak = beat it). Warning: content must deliver the title's promise.

**Method 3 — Cross-Niche Format Snatch (p44):** (1) survey 5–10 outside niches, ~30 min each; (2) keep formats producing 500K+ repeatedly across channels; (3) search "[niche] + format" — zero/few = gap; (4) logic check that the format fits; (5) make the first video on the source structure; (6) combine with Method 2. Case study and summary truncated (p44, p46).

**Method 4 — Demand/Supply Gap Scan (p48–49):** (1) 15–20 candidates (summary says 50–100) from competitors, other niches, comment requests, outlier DB; (2) supply = count of videos on the topic with 50K+ views (summary says 10K+; discrepancy preserved, p50); (3) demand = total views on existing videos; (4) grade: A = high demand/low supply (make now), B = high/high (needs unique angle), C = low/low (search play), D = low/high (avoid); (5) calendar the A-tier. Tip: specific long-tail + emotional resonance.

Adjacent: Practical Month topic bank columns — topic, discovery method, comparable video + views + date, search intent, retention risk, GO/NO-GO, reason; ≥4 methods across 20 topics (p494). Part D scorecard (new, /25): evidence freshness, multi-channel validation, distinct angle, research feasibility, audience fit (p556).

## 5. The 100 title formats (p52–70) + Title Psychology Breakdown

Five-part title engine: Subject, Situation, Trigger, Tension, Promise (p53). Source states mechanisms are hypotheses and examples are illustrative, not case studies (p53–54).

**01 Curiosity, mystery & disappearance — information gap + recognisable subject (p55)**
001 What Really Happened to [X]? · 002 The Real Reason [X] [Did Y] · 003 What Nobody Tells You About [X] · 004 The Untold Story of [X] · 005 Why [X] Suddenly Disappeared · 006 Inside the Hidden World of [X] · 007 What Happened at the [Event/Place]? · 008 The Dark Side of [X] · 009 [X] Is Way [Scarier/Stranger] Than You Think · 010 The [X] Nobody Was Supposed to See

**02 Failure, downfall & destruction — loss aversion + causality (p56)**
011 The Rise and Fall of [X] · 012 The Rise, Fall & Rise Again of [X] · 013 What Really Killed [X]? · 014 Why [X] Failed · 015 How [X] Destroyed [Y] · 016 The Mistake That Destroyed [X] · 017 [X] Had Everything — Until [Y] · 018 [X] Will Fail, Here's Why · 019 [X] Tried to Warn You · 020 What Went Wrong With [X]?

**03 Contradiction, irony & reversal — expectation violation (p57)**
021 [X] Did [A] — But [B] Happened · 022 How [X] Won But Still Lost · 023 When [X]'s Greatest Strength Became Its Weakness · 024 Nobody Wanted This [X] Anymore · 025 [X] Was Supposed to Fail — But [Y] Happened · 026 How [X] Became the Most Hated [Y] · 027 Why [X] Refused to [Y] · 028 The [X] That Shouldn't Exist · 029 [X] Lasted Only [Short Period] — But [Long-Term Result] · 030 Yeah… No Wonder [X] [Outcome]

**04 Characters, decisions & defining moments — narrative transportation (p58)**
031 When a [Moment/Decision] Changed [X] Forever · 032 When an [Opportunity/Event] Went Completely Wrong · 033 The Night [X] [Unexpected Event] · 034 The [Person] Who [Extraordinary Action] · 035 How One [Person] Is Keeping [X] Alive · 036 The Incredible [X] Story · 037 From [A] to [B]: How [X] Changed · 038 The Last [X] · 039 The Genius of [X] · 040 Why [Group] Loves [X]

**05 Explainers, rankings & nostalgia — completeness + comparison + recognition (p59)**
041 Every [X] Explained · 042 Every [X] Ranked From Worst to Best · 043 The [Number] Levels of [X] · 044 The [X] Iceberg Explained · 045 The Entire History of [X] · 046 [X] vs [Y]: What's the Real Difference? · 047 Do You Remember These [X]? · 048 Before [X], How Did People [Y]? · 049 The Most [Adjective] [X] Ever · 050 [Number] [X] That [Unexpected Consequence]

**06 Revelations, evidence & hidden mechanisms — discovery + authority + proof (p60)**
051 The Truth About [X] · 052 The Secret Behind [Outcome] · 053 How [X] Actually Works · 054 The Evidence That Changed [X] · 055 What [Experts/Insiders] Know About [X] · 056 The [Recording/Document] That Revealed [X] · 057 What They Found Inside [X] · 058 The Only Reason [X] Worked · 059 What [X] Gets Wrong About [Y] · 060 The Parts of [X] You Never Get to See

**07 Time, legacy & cultural change — before/after + memory (p61)**
061 Whatever Happened to [X]? · 062 Why You Don't See [X] Anymore · 063 When [X] Ruled [Place/Era] · 064 The Forgotten [X] That Once [Y] · 065 The Last Days of [X] · 066 Before [X] Existed, [Y] Was Different · 067 How [X] Changed [Y] Forever · 068 The [X] We Lost Along the Way · 069 What [X] Looked Like [Number] Years Ago · 070 When [X] Was Everywhere

**08 Small causes, big consequences — scale contrast (p62)**
071 How One Small [Decision] Changed Everything · 072 The Rejection That Created [X] · 073 When [X] Said No to [Y] · 074 The Last-Minute Change That Saved [X] · 075 When a [Mistake] Turned Into [Success] · 076 The [Role/Job] Nobody Wanted · 077 [X] Almost Never Happened · 078 The Moment [X] Realized [Y] · 079 It Wasn't [A] That Ended [X] — It Was [B] · 080 [X] Tried to [Goal]. Instead, [Outcome]

**09 Problems, trade-offs & practical insight — utility + risk reduction (p63)** *(closest fit to health how-to content)*
081 How Much Does [X] Really Cost? · 082 Why [X] Is So Expensive · 083 The Hidden Economics of [X] · 084 The Beginner's Guide to [X] · 085 [Number] Mistakes That Ruin [X] · 086 The Biggest Myth About [X] · 087 Why [X] Works (And [Y] Doesn't) · 088 What Happens When [X] Is Removed? · 089 [X] Explained in [Number] Minutes · 090 What It Takes to [Achieve X]

**10 Conflict, stakes & alternative outcomes — conflict + uncertainty (p64)**
091 [X] vs [Y]: The Battle That Changed [Z] · 092 How [X] Survived [Y] · 093 The Warnings [X] Ignored · 094 The [Number] Minutes That Changed [X] · 095 What If [X] Had Never Happened? · 096 The Closest [X] Ever Came to [Y] · 097 [X] Was One Step Away From [Y] · 098 When [X] Turned Against [Y] · 099 The Decision [X] Regretted for Years · 100 How [X] Became [Its Own Worst Enemy]

**Selection rule (p54):** unknown ending → family 01; documented causes → 02/turning points; clashing facts → 03; comparable set → rankings/explainer; emotionally remembered → nostalgia/legacy.
**Workflow (p65):** define viewer + topic; find the strongest true tension; pick 3–5 compatible families; draft 8–12 variations; score best three; pair with one thumbnail idea.
**Title scorecard (p66), 0–5 each, /30:** audience recognition, clarity, curiosity gap, stakes/relevance, distinctiveness, proof & delivery. 26–30 strong, 21–25 revise, 0–20 rethink; any unsupported claim is a veto. Source says this is not a CTR predictor.
**12 title mistakes + safety checklist (p68); pre-publish questions (p70).**
Other explainer-format templates in a chat log (p532–533): What Happens ___ in ___ Explained; 7 Levels of ___; Every Level of ___ Explained; Your Life as ___; Why It Sucks to Be ___; Everything About ___ Explained in ___ Minutes; The Entire History of ___; All ___ Explained; What It Was Like to Be ___ in ___; Ranking ___ from Weakest to Most Powerful.

**Title Psychology Breakdown dimensions (p128–132), per title:** 1 Original title; 2 Simple breakdown (role-components joined by "+", not generic labels like curiosity/fear); 3 Function of each component; 4 Deep psychological formula (one sentence preserving the cause-effect mechanism); 5 Viewer's internal question; 6 Cause-and-effect chain (Subject → Action → Immediate Result → Hidden Consequence → Harm/Irony); 7 What must stay the same; 8 What can change; 9 Topic discovery question; 10 Cross-niche application (10 real topics); 11 Final master formula. Priorities: cause-effect, irony, contradiction, who caused / benefited / suffered, what changed, why surprising.

**Topic-to-Title engine (p156–163):** Subject/Situation/Trigger/Tension/Promise table; 15 psychological lenses (contradiction, mystery, unexpected consequence, hidden cost, reversal, self-destruction, comparison, power/vulnerability, outsider, transformation, overlooked knowledge, completeness, irony, cause-effect, human behaviour); 3 titles per angle; score 1–10 on curiosity, specificity, tension, clarity, audience relevance, credibility = /60.

## 6. Topic Validation prompt (p72–80)

Input: topic + pasted search-result titles only. Phases:
1. Understand the topic — niche, audience, viewer intent, series vs single (p72).
2. Clean and cluster all titles — dedupe; direct / partial / irrelevant; per cluster: theme, title structures, approaches, triggers, crowding, diversity. Mark views/dates unverified if absent (p72–73).
3. Supply pattern: A Diverse, B Repetitive, C Concentrated, D Weak Relevant. High supply is never an automatic rejection (p73–74).
4. Gap scan: subject, angle, format, psychological (12 motivations), specificity, niche-bending. A missing angle is only an apparent gap (p74–75).
5. Score 0–5 each, /25: Search Relevance, Content Variety, Differentiation Potential, Topic Repeatability, Packaging Potential. Must not score demand, CTR, retention or virality without data (p75–76).
6. Verdict: A Recommended for Testing / B Conditional — Change the Angle / C Not Recommended, with stated conditions (p76–77).
7. Exactly five distinct opportunities, each: topic, title, trigger, evidence, differentiation, difficulty, alternative title (p77–78).
8. Output format incl. best first video and 3-step action plan (p78–80).
Strict rules (p80): no fabricated performance; do not call a format proven without evidence; search frequency ≠ demand; separate observations, hypotheses, assumptions.

## 7. Act Structure analysis

**Fixed 6-act model (p148–154): Hook → Context → Rising Action → Climax → Resolution → CTA/Exit.**
Per act: location, purpose, what happens, viewer question created/answered, why it works, transition. Rising Action adds developments, escalation, open loops; Climax adds payoff, which promise it fulfils, emotional effect; CTA adds natural vs forced.
Extra outputs: one-screen structure; retention chain Promise → Understanding → Escalation → Payoff → Closure → Next Video; information curve with intensity 1–10 per act (strong promise, controlled slowdown, continuous escalation, peak, satisfying decline, smooth transfer); retention devices (14 types, each with line, technique, why, payoff location); transition sentences between acts; teaching summary. Rules: no invented timestamps; an open loop requires a delayed answer; a new fact is not automatically escalation; say when the transcript does not fit six acts.

**Outlier Act Structure analysis — natural-section model (p134–146), 12 tasks:**
1. Natural sections (do not force a count): location, what happens, section job, viewer question, why they keep watching, transition.
2. Curiosity chain; name the PRIMARY retention engine (one big loop, multiple loops, escalating questions, delayed answers, contradiction, mystery, cause-effect, countdown, transformation, comparison, investigation).
3. Re-hook table (location, line, type, what it makes the viewer want) + average interval + aggressive/moderate/light.
4. Payoff system: where each promise is created and paid; was a new loop opened; main payoff.
5. Information escalation pattern; is the strongest material held back.
6. Opening (first 30–60s): first-line job, title connection, information withheld, open loop, stakes, expectation, transition; abstract opening formula.
7. Closer (last 30–90s): what resolves, final insight, emotional note, last-line technique, CTA type, closer formula.
8. Acts (5–10) built from sections: narrative job, viewer question, escalation, exit hook.
9. Content-neutral format skeleton (most important).
10. Compressed one-line skeleton.
11. 5–10 writer retention rules traceable to the transcript.
12. Copy (format) vs do-not-copy (content).
Summary block (p145): primary format, retention engine, section count, act count, average re-hook interval, main payoff placement (% through), closer style, one-line skeleton.

## 8. Script Writing Engine, masterclass, AI workflow

**Engine pipeline (p156–261), seven chained prompts:** (1) Topic-to-Title (p156–164); (2) Central Argument & Viewer Promise — 3 arguments (direct / human conflict / deeper), explicit / implicit / emotional promise, tension, payoff design, /70 comparison, creative brief (p165–173); (3) Act Structure — five alternatives (6/7/8/9/10 acts), per act: purpose, content, viewer question, engagement, payoff, forward momentum; scored /70 (p174–190); (4) Story Beats — ~3–6 beats/act, 11 fields each, mini-arc Entry → Development → Complication → Payoff → Transition, curiosity & payoff tracker (p191–208, truncated); (5) Retention Engineering (p209–225, truncated); (6) Scriptwriting (p226–243, truncated); (7) Quality Audit (p244–261, truncated).

**Architecture — six zones (p320–321) / universal skeleton with word budgets (p323):** Hook 0–5s (15–30 words) → Stakes Frame 5–15s (25–50) → First Curiosity Loop 15–45s (30–60) → Context 100–200 → Segments 150–300 each with 15–25-word micro-cliffhangers → Climax 150–300 → False Resolution 20–40 → Final Reveal 80–150 → Mid-CTA 20–35 → Close + Future Pace 30–60. Rising middle = 45s to 70%; climax 70–90%; close final 10%.

**Hook rules:** seven hook types — Question, Shock Stat, Contradiction, Mystery, Story Drop, Direct Challenge, Impossible Choice (p265–266). Engine's three strategies: contradiction/surprise, consequence/high-stakes, mystery/hidden explanation (p213). First-90s map: 0–15 immediate interest, 15–30 central tension, 30–60 deepen question, 60–90 first real answer (p214–215). Banned openers such as greetings, agenda statements and "have you ever wondered"-style lines (p230). Hook is 1–2 sentences, sayable in under 8 seconds (p297–298); hook + stakes under 60 words, close under 60 words (p306). Stakes inside 15s (p501).

**18 named techniques (p265–283) with sub-techniques:**
1. Opening Hooks — first line creates an immediate reason to stay.
2. Curiosity Gaps — tease, then delay: Delayed Payoff, Stacked Loop, Bridging Tease, Withholding Tease.
3. Pattern Interrupts — sudden shift resets attention: Tonal Shift, Unexpected Analogy, Rhetorical Question Drop, Scripted Beat/Pause, Visual/Edit Cues.
4. Nested Storytelling — a story inside a story: Context Detour, Parallel Thread, Flashback Insert, Character Origin.
5. Escalation Chains — each segment more intense: Intensity, Signposted, Emotional, Final Reveal.
6. Direct Address — "you": Immersion Command, Personal Implication, Assumption Challenge, Inclusive We.
7. Micro-Cliffhangers — bridges at segment ends: Question Bridge, Consequence Tease, Reversal Tease, Superlative Bridge.
8. Authority & Credibility Drops — Precise Number, Source Citation, Expert Quote, Date Anchor.
9. Contrast & Comparison — Then vs Now, Expectation vs Reality, David vs Goliath, Side-by-Side Specification.
10. Emotional Anchoring — Sensory Language, Empathy Placement, Consequence Framing, Nostalgia Triggers, Awe and Wonder.
11. Callbacks & Payoffs — Planted Detail, Full-Circle Return, Revaluation Callback.
12. False Resolution — apparent ending, then more: Premature Conclusion, Hidden Chapter, "Or Did It" Reversal.
13. Viewer Qualification — flatter those still watching: Survivor Compliment, Insider Frame, Exclusion Trigger.
14. Pacing Variation — Rapid-Fire Sequence, Dramatic Slowdown, Rhythm Switch, Breath Mark.
15. CTA Integration — Mid-Roll Value, Content-Locked, Community, Embedded.
16. Future Pacing — Unanswered Question, Sequel Tease, Bigger Story Hint.
17. Recontextualization — flip a familiar thing: Hidden Origin, Misunderstood Purpose, Villain Redemption/Hero Reversal.
18. Stakes Framing — why care: Personal, Historical, Survival, Legacy, Economic.

**Engine-level techniques:** 10 re-hook types (new information, contradiction, consequence, reversal, deeper explanation, comparison, human element, unresolved question, scale, payoff-to-new-question) (p216–217); open/closed loop table (p217–218); three payoff levels micro / act / final (p220); seven escalation types — stakes, conflict, knowledge, scale, psychological, consequence, comparative (p221–222); ten narrative pattern interrupts, e.g. broad↔specific, individual→system, complexity→clarity (p224).

**Numeric rules (two schools that conflict — record which is applied):**
| Rule | Playbook / masterclass | Engine prompts |
|---|---|---|
| Pattern interrupt | every 15–30s (p268, p284); 20–30s in docs (p326); flag >30s ≈ 80 words (p301) | no quota; do not insert to fill one (p225) |
| Re-hook | micro-cliffhanger at every transition (p284) | check for one roughly every 60–120s, diagnostic only (p217) |
| Techniques per script | 5–8 / 6–8 layered (p264, p284); minimum 8 of 18 (p296) | — |
| Open loops | ≥1 before 30s (p320, p350); ≥2 open through middle (p301) | no forgotten or fake loops (p218) |
| Narration pace | ~160 wpm; 8–10 min = 1,400–1,600 words (p323) | 125–140 slow, 140–155 standard, 155–165 fast; 15 min ≈ 2,100–2,325 (p184, p242) |
| Sentence length | — | often ~11–18 words, varied (p236) |
| CTA | at 50–70% after a payoff (p284); final 15s future pace | engine's final act: no CTA (p182) |
| Visual cue | every 15–20s (p303) | engine forbids editing notes (p224) |
| Doc acts | Setup 20% / Conflict 50% / Climax 20% / Epilogue 10% (p326) | allocation by content, not equal (p184–185) |
| Shorts | 140–170 words; max 160 (p323, p307) | — |

**Retention heat map (p349):** 0–3s hook; 5–10s stakes; 25–35s first loop; 60–90s interrupt + cliffhanger; 50% qualification + escalation; 70–80% false resolution; final 15s future pace. Presented as pattern knowledge, no data shown.

**10 script types with structures (p324–336, quick-select p312–315, mapping p348):** Countdown/Listicle (midpoint bump, false resolution before #1), Documentary, Explainer (misconception → simple → deep → impact → callback), Biography, Then & Now, Dark History, Versus, Mystery, Engineering/Science, Geopolitical/Economic.

**AI workflow, 12 steps (p287–316):** topic brainstorm + validation; fact file → gap dive → fact sheet; competitor script analysis (hook style, structure, techniques, what they missed); script type; outline with engagement mapping + audit; 5 hooks + 3 stakes frames; section-by-section writing; engagement second pass; visual cues; fact-check + policy audit; pacing calibration; export + optional Short.

**Reverse-engineered format prompt (p394–409):** map the new topic onto the reference's section functions; preserve information order, curiosity system, payoff placement, escalation, re-hook rhythm, opening and closer logic; never copy content; format serves truth; 10-point match check.

**Health-relevant policy notes (source's own claims, unverified):** no contradicting medical consensus without peer-reviewed citation; no medical advice; no unproven cures (p341); three disclaimer templates (p346–347); no misleading before/after thumbnails (p345); source-then-information-then-complexity framing (p342).

## 9. Script audit

**MASTER FACELESS YOUTUBE SCRIPT AUDIT (p353–392), 50 parts.** Inputs: title, thumbnail concept, audience, length, niche, style, script.
- Verdict: produce as-is / minor revision / major revision / rewrite sections / do not produce. Score /100: 95–100 exceptional, 90–94 excellent, 85–89 strong, 80–84 good foundation, 70–79 significant problems, <70 major rewrite (p354–355).
- Depth ladder L1 Surface Facts → L2 Context → L3 Causality → L4 Contradiction/Complexity → L5 Interpretation → L6 Deep Narrative Insight; scores for research, interpretive and overall depth (p356–358).
- Tests: "So what?" per beat (p358–359); Story vs Biography = Character → Desire → Obstacle → Decisions → Consequences → Change (p359); hook (curiosity, specificity, visual potential, stakes, question, information control, title link, progression) (p360–361); curiosity engine and "curiosity deserts" (p361–362); escalation (p362); natural acts, merge duplicates (p363); pacing with removable-% bands 0–5 / 5–10 / 10–20 / 20%+ (p364); repetition Keep/Combine/Delete (p365); information value A–D incl. "research vanity" (p365); character depth; emotional journey; conflict; stakes; causal chain gaps (p366–369); contradictions as thematic spine (p369); predictability; three-viewer knowledge gap (novice / casual / expert) (p370); credibility flags and claim classes Safe / Needs citation / Needs stronger evidence / Needs qualification / Potentially misleading (p371–372); nuance; originality; narrator voice; clarity (p372–374); faceless visual storytelling; show vs tell; top 5 moments (p375–377); re-hook points; 5 predicted drop-offs with severity; remove-this-section test (p377–378); transition logic (therefore/but vs meanwhile/next) (p378–379); midpoint; climax; ending = Answer → Reinterpretation → Meaning → Final thought (p379–381); theme; sentence-level; AI-writing tells; density; expectation vs delivery; best-material placement; missing material; counterargument; honesty test (p381–386); retention map 1–10 per section, explain <8 (p386).
- **Scorecard, 22 categories /10 (p387–388):** Title Fulfillment, Hook, Story, Structure, Curiosity, Research Depth, Interpretive Depth, Character Depth, Conflict, Stakes, Cause & Effect, Escalation, Emotional Journey, Pacing, Clarity, Narration, Originality, Credibility, Visual Storytelling, Re-hooks/Retention, Climax, Ending/Payoff → overall /100, not a mechanical average if a fatal flaw exists.
- Outputs: Must Fix / Should Fix / Optional; editor comments; surface / better / deepest version; final verdict READY / MINOR / MAJOR / NOT READY (p388–391). Section test: does it deepen, complicate, escalate, humanise or move toward the answer (p392).

**Engine Quality Audit (p244–261, truncated in Phase 10):** foundation assessment; title alignment + promise fulfilment /10; hook audit (8 criteria, 10 red flags); act-by-act (10 criteria); beat execution; retention risks (12 categories); energy vs engagement 1–10 per section; loop/re-hook/payoff table; repetition (8 types); language (naturalness, clarity, rhythm, voice consistency, VO readiness /10). Explicitly forbids fabricating retention %, AVD or CTR (p257).

**Pre-publish checklist (p350–351):** 12 engagement checks (hook, stakes ≤15s, loop <30s, interrupt ≤30s, cliffhanger per transition, escalation, callback, false resolution, CTA placement, future pace, pacing, word count) + 10 policy checks. Outline engagement audit, 7 checks (p296); draft audit with density LOW–EXCELLENT (p301).

## 10. Voiceover / production workflow (brief)

- VO emotion prompt (p411–423): add bracketed delivery tags without changing any word; read for meaning first; emotional contrast; do not over-tag; pause tiers (short / normal / long, long used rarely); slow for numbers and reversals; emphasise words not paragraphs; quiet for heavy moments; genre palettes; 10-point check.
- Visual cue vocabulary: B-ROLL, IMAGE, TEXT OVERLAY, CUT TO, ZOOM, ANIMATION, BEAT/PAUSE, MUSIC (p303).
- Explainer storyboard director (p425–438): exactly 20 scenes, crude hand-drawn stick-figure style, face identity cards, background then character prompts. Character-sheet prompt (p542–545); storyboard-grid prompt (p546–552).
- Practical Month (p491–507): W1 niche + teardown + channel + 20 topics; W2 five packages, two scripts (8–12 min, ~1,300–1,900 words), three hook variants, fact sheets (unverified claims cap the week at 60), production plan; W3–W4 VO, asset/licence sheet, publish, analytics reading; weighted rubrics (p501–502). Thumbnails 1280×720, ≤4 words, mobile test (p495).
- Celebrity compilation workflow (p441–489): source-ID / moment-ID pipeline with verification statuses — not relevant to health beyond its provenance discipline.

## 11. Part D — independent web research appendix (p554–556)

Labelled as new, dated 11 Nov 2026, separate from the course. It states the course thresholds (10x, 20+ outliers, 50+ ideas, 2–3 competitors, A–D grades) are heuristics, not YouTube thresholds. Stated facts and its cited sources:
1. Recommendations are personalised, using clicks, watch time, satisfaction surveys, shares, likes, dislikes; no fixed recipe — https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/
2. Outlier limits and the median-of-comparables ratio (no external source; appendix reasoning).
3. Impressions CTR varies by content, audience and surface; about half of channels/videos fall in 2%–10%; high CTR/AVD does not guarantee impressions; public views reveal nothing about CTR or retention — https://support.google.com/youtube/answer/7628154
4. Browse, Suggested and Search are separate traffic sources; check the mix in Studio — https://support.google.com/youtube/answer/9314355
5. Studio A/B tests: up to three titles/thumbnails, winner by watch time, days to two weeks, Shorts excluded — https://support.google.com/youtube/answer/16391400 ; accurate, concise titles with key words early — https://support.google.com/youtube/answer/12340300
6. Retention reports show intro, top moments, spikes, dips — https://support.google.com/youtube/answer/9314415
7. July 2025 monetisation update: repetitive/mass-produced content can be ineligible as inauthentic; rotating templates is not enough; reused content needs significant original value — https://support.google.com/youtube/answer/1311392
8. Mid-roll eligibility at eight minutes or longer; a slot does not guarantee an ad — https://support.google.com/youtube/answer/6175006
9–10. Suggested /25 scorecard and measurement dashboard columns (appendix's own); audience and reach metric references — https://support.google.com/youtubecreatorstudio/answer/9314416 , https://support.google.com/youtube/answer/9314486

## 12. Claims register

Claims are paraphrased closely (verbatim quotation minimised); check the page for exact wording. Classes: PLATFORM_CLAIM_UNVERIFIED (PCU), CREATIVE_HEURISTIC (CH), SUPPORTED_BY_PART_D (SPD). "Part D qualifies" = the appendix disputes or narrows it.

| # | Page | Claim (close paraphrase) | Class |
|---|---|---|---|
| 1 | 6 | An outlier's performance is driven by topic and packaging, not the channel | PCU — Part D qualifies (p554) |
| 2 | 6 | A small channel's 500K video proves massive demand; the algorithm pushed it because viewers wanted it | PCU — Part D qualifies |
| 3 | 6 | Outlier title/thumbnail achieved "massive CTR" | PCU — CTR not observable publicly (p554) |
| 4 | 7, 9 | Ratio bands 1–3x / 5–10x / 10–50x / 50–100x+ | CH (Part D: not official) |
| 5 | 8, 9 | 20+ outlier topics = green light; 3–5 too narrow; 0 = no demand | CH |
| 6 | 9 | 500K views in two weeks means it hit Browse and Suggested hard | PCU |
| 7 | 11 | A well-defined niche lets the algorithm classify the channel and keeps CPM high | PCU |
| 8 | 13 | Rotating 3–5 templates is enough to stay safe from the inauthentic-content system | PCU — contradicted by Part D item 7 |
| 9 | 18 | A format new to a niche yields higher CTR and higher AVD | PCU |
| 10 | 18 | The algorithm rewards novelty within a niche and pushes it harder | PCU |
| 11 | 19 | 8+ minutes is the sweet spot for ad revenue | SPD in part (mid-roll eligibility only, p555) |
| 12 | 24 | Novelty = CTR = algorithm boost | PCU |
| 13 | 24 | A bent niche is classified uniquely and matched precisely | PCU |
| 14 | 25 | Oversimplified reached 60+ million subscribers | PCU (factual claim, unverified) |
| 15 | 28 | Competitors' top videos are evidence of what the algorithm pushes | PCU |
| 16 | 30 | Shot-for-shot recreation will be flagged under Reused Content | SPD in part (policy exists, p555) |
| 17 | 33 | A bad video on the right topic beats a great video on the wrong one, every time | CH (absolute; no evidence) |
| 18 | 33 | Bad topic selection is the #1 reason faceless channels fail | CH |
| 19 | 33 | Methods are exact processes used to generate millions of views | PCU (no evidence shown) |
| 20 | 33 | Browse needs recognised demand + high predicted CTR + strong predicted AVD | PCU — Part D: signals are not a fixed recipe |
| 21 | 34 | If demand persists, YouTube will distribute a new well-packaged version too | PCU |
| 22 | 39 | Title formats validated across 100+ niches with millions of data points | PCU (no data; the 100-format guide itself denies guarantees, p53–54) |
| 23 | 39 | Browse is fundamentally a CTR test on a test audience | PCU — Part D qualifies (p554) |
| 24 | 40 | Proven title formats increase CTR | CH |
| 25 | 44 | Novel format → unusually high CTR and strong AVD → pushed on homepage | PCU |
| 26 | 48 | The algorithm is actively looking to fill demand/supply gaps | PCU |
| 27 | 48 | Search engagement leads YouTube to push the video to Browse | PCU — Part D: do not assume (p555) |
| 28 | 48 | A-tier topic will rank quickly and get pushed to Browse | PCU |
| 29 | 265, 320 | About 3 seconds to hook before the viewer leaves / before a view counts | PCU |
| 30 | 268, 284 | Pattern interrupts should appear every 15–30 seconds | CH |
| 31 | 272 | Retention typically dips at 30s, 1 min and mid-video | PCU (no data) |
| 32 | 303 | Visual cues let an editor work 3x faster and 5x better | CH |
| 33 | 321 | Mediocre topic + perfect structure beats a great topic with flat delivery, every time | CH (contradicts #17) |
| 34 | 331 | Then & Now has massive browse potential; side-by-side thumbnail maximises CTR | PCU |
| 35 | 340 | Repetitious-content flag can disqualify a whole channel from YPP | SPD (p555) |
| 36 | 344 | Three copyright strikes in 90 days = termination, no appeal of termination | PCU (not covered by Part D) |
| 37 | 349 | Drop-off pattern derived from analysing thousands of faceless videos | PCU (no data) |
| 38 | 278 | "Top 5%" / "99% never will" viewer-qualification lines | CH (scripted lines with invented statistics; avoid in health content) |
| 39 | 554 | Half of channels/videos have impressions CTR around 2%–10% | SPD (Part D's own, cites YouTube Help) |
| 40 | 555 | A/B test winner decided by watch time, not CTR | SPD (Part D's own) |

No literal "guaranteed results" promise was found; the strongest absolutes are #17, #28, #33. Several later documents explicitly disclaim guarantees (p53–54, p66, p74, p80, p162, p186, p257).

## 13. Coverage record

- Read sequentially and completely: pages 1–557 (form-feed delimited), in 13 contiguous chunks; none sampled or skipped. No recourse to the PDF was needed.
- Near-empty pages (divider/label or blank): 31 (header only), 440 ("START PROJECT"), 446, 450, 462, 470, 477 (prompt labels), 449 and 557 (blank).
- Table-extraction noise only (no lost content): 15–16, 20–22, 35–37, 40–42, 45–46, 49–50 (extraction-status tables), 511–528 (blank form rows).
- Source-level truncations (missing in the source, not invented here): p13 (framework table stops at item 4), p14 (templates 7–10), p19 (case study 2 and a cut passage), p28 (one unclear number), p37 (Methods 5–12 absent), p39 (title format 10), p44/46 (Method 3 case study end and summary), p208 (Story Beats prompt cut in Phase 10), p225 (Retention prompt cut in Phase 10), p243 (Scriptwriting prompt cut in Phase 10), p261 (Quality Audit cut in Phase 10), p435–436 (output-format lines clipped).
- Source inconsistencies preserved: outlier denominator (§1); Method 4 supply threshold 50K vs 10K and candidate count 15–20 vs 50–100 (p48–50); lesson numbering 2.3/2.4 and 2.4/2.5 (p22, p26); narration pace 160 wpm vs 125–165 wpm (§8).
- External share links (p532, p535–539) were not opened.
