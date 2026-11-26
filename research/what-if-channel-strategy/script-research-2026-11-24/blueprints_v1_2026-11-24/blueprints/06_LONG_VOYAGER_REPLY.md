# Blueprint 06 — LONG — A reply from Voyager (Day 16)

**STATUS: PARTIAL — NEEDS SOURCE/CALCULATION (and NEEDS EDITORIAL DECISION on stretch risk).** The light-time arithmetic and NASA's Nov 2026 status are sourced; the 2024 real-world precedent is only snippet/secondary level; the status may change before release; and the slot risks being a stretched Short. Position kept; alternatives in 09. SELF-REVIEW.

## A. IDENTITY
- **Calendar:** Day 16, Long (3–4 min; do not pad to 5).
- **Current working title:** "Why Would a Reply From Voyager Take Two Days?"
- **Issue:** "would" and "reply" imply a working exchange; NASA's 2026-11-19/20 posts report no science or engineering data since 14 Nov (carrier only), and the previous Short already answers "why a day".
- **Proposed alternatives:**
  1. "What Happens When You Send a Command to Voyager 1?" (the process, not a promised reply)
  2. "How Do You Fix a Spacecraft When Every Reply Takes Two Days?" (the debugging angle; uses the 2024 case only if sourced)
- **Central question:** How long does it take for a command to reach Voyager 1 and an answer to come back, and what does that do to anyone trying to fix or ask something?
- **One-sentence answer (qualified):** At least ~48 hours of light time per exchange (24 h each way), plus onboard handling, antenna scheduling and the team's analysis — and because Voyager 1's data stopped on 14 Nov 2026, any reply here is hypothetical.
- **Viewer expects:** a story of a message and a reply.
- **Viewer actually learns:** what a two-day loop does to a conversation, why the spacecraft must act alone, and how cautious step-by-step diagnosis works.

## B. PRECISE SCENARIO
- **Changes (ASSUMPTION):** Earth sends one small, safe command at time T0, with no operator delay; the spacecraft receives it, acts within seconds, and replies. (Hypothetical, labelled "if it were answering".)
- **Normal:** signals at c; distance ≈ 25.9 billion km (V03-C02); commands weekly, listening daily (V06-C02).
- **Real status (dated):** data stopped 14 Nov 2026; carrier signal still received; NASA suspects the onboard data-handling computer; "weeks or longer" (V06-C03).
- **Not claimed:** that Voyager 1 receives, obeys or answers.

## C. DEPENDENCY MAP
| Needed | Source | Status |
|---|---|---|
| One-way 24 h, round trip ~48 h | NASA release and blog (V06-C01) | SOURCE_READ_EXTRACT |
| Daily listening, weekly commands | NASA release (V06-C02) | SOURCE_READ_EXTRACT |
| Status 14 Nov onward | NASA blog 2026-11-18 (page updated 2026-11-20) (V06-C03) | re-check at release |
| 2024 precedent (command 18 Apr, confirmed 20 Apr, ~45 h) | news citing JPL (V06-C04) | SNIPPET_ONLY — **needs primary** |
| Conversation arithmetic (10 cycles = 20 days) | V06-C05 | arithmetic |
| "Do not imply a reply" | V06-C06 | policy |

## D. CAUSE-AND-EFFECT STORY (beats)
| # | Cause / story question | Science | Result | Leads to | Visual | Claim |
|---|---|---|---|---|---|---|
| 1 | Hook: "You type one line to Voyager 1. When do you get an answer?" | rules: a hypothetical safe command, no human delay | question set; "if it were answering" tag | "when does the line arrive?" | timeline bar labelled T0 … T0+48 h | V06-C06 |
| 2 | THEREFORE walk the loop | 24 h out, spacecraft acts, 24 h back | at least ~48 h; Earth's view at T0 is the spacecraft of a day ago | "what does 'a day old' do?" | split screen: Earth clock vs Voyager clock, with a 24 h offset | V06-C01 |
| 3 | BUT you can't just ask when you like | listened to daily; commands weekly | even before light time, a command waits for its slot | "how do engineers act on this?" | calendar strip with a weekly "uplink" slot | V06-C02 |
| 4 | THEREFORE the real way to diagnose is small steps | a real precedent (only after sourcing): 18 Apr 2024 command, confirmed two days later (~45 h) | each test costs two days; ten cycles = 20 days | "what is the situation right now?" | stack of ten exchanges filling a 20-day calendar | V06-C04, V06-C05 |
| 5 | BUT now: data stopped on 14 Nov 2026 | carrier still received; attitude control seems to keep pointing; suspected data-handling computer; "weeks or longer" | the team is diagnosing at two-day cadence; we do not know the outcome | "so who flies the spacecraft?" | dated status card with the NASA source line | V06-C03 |
| 6 | THEREFORE the spacecraft must act alone | decisions can't wait two days | autonomy is a design requirement, not a luxury (editorial inference from the loop time) | answer | closing graphic: the 48 h loop with "no reply promised" | V06-C01, C06 |

## E. NUMBERS INTO IMAGINABLE SCALE
- 48 h: "two sunrises" (exact: two 24 h cycles).
- 10 exchanges = 20 days: arithmetic, "a three-week conversation of ten sentences" (≈ 20 days = just under 3 weeks).
- 25.9 billion km: 173 au (from the Short), not repeated at length.
Qualification: light time excludes everything else.

## F. HOOK, ESCALATION AND ENDING
- Hook (0–15 s): "A one-line command to Voyager 1. Two days until you know." State "if it were answering".
- First non-obvious reason: the delay is not only about waiting; it means you always act on old news.
- Escalation: warranted only along the loop (one cycle → ten cycles → current real status). Do not invent an emergency.
- Direct answer: "At least two days per exchange — and right now we don't know whether it would answer."
- Dry humor option: "the slowest chat in the Solar System, with the best read receipts" (careful: keep tone respectful; optional). No-joke alternative: end on the 20-day calendar.

## G. VISUAL COMMUNICATION (text only)
- Beat 2: two clocks 24 h apart; arrows labelled "24 h", "24 h".
- Beat 4: ten stacked cycles on a calendar; labelled "if each took exactly 48 h".
- Beat 5: a dated card "NASA, 18–20 Nov 2026" — never an animation that shows the spacecraft recovering.
- Must not depict: a reply received, a rescue, mission-control celebration, or a fake "signal found" graphic.

## H. ORIGINALITY AND PRIOR ART
- No book chapter on Voyager found by OCR (OCR-limited); no registry video title (titles only); xkcd comic 3325 (cited by Codex) not opened — NOT CHECKED. Earlier Claude/Codex reviews disagree about this slot (Claude rejects it, Codex keeps it conditional).
- Our angle: conversation/debugging at two-day latency; the 2024 case as the single real example (if sourced).
- Do not copy: any xkcd wording or imagery; no reproduction of NASA text.

## I. SCIENCE AND EDITORIAL REVIEW (SELF-REVIEW)
- Qualified: light time and round trip; NASA status as of 20 Nov.
- Open: the 2024 precedent (primary source), the present status, onboard autonomy statements (V06-C06 is policy; "autonomy as a design requirement" is editorial inference, not sourced).
- Highest-risk misunderstanding: that a reply happened or will. Mitigation: "if it were answering" tag; dated status.
- Reviewer: JPL-literate reviewer or a NASA source read for the 2024 timeline.
- Blockers: primary source for 2024; status re-check on the release day; decide whether this slot should remain a Long.
- Confidence: research 0.55; story clarity medium (stretch risk).

## J. FORMAT AND DEPENDENCIES
- **Distinct from Short 03:** Short = *why a day*; Long = *what a two-day loop does to a conversation and to repairs*. Share only the light-day figure.
- **Does the Long contain a distinct multi-beat payoff?** Beats 3–6 are not in the Short. If beats 4–5 cannot be sourced, the Long collapses into a stretched Short → recommend swapping or shrinking (see 09).
- **If the Short (Day 7) is delayed:** the Long must restate the light-day in one beat. **If this Long is delayed:** nothing else depends on it.
