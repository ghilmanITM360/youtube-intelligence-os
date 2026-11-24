# DS-000011 packaging / hook PDFs — read and applied (2026-11-23)
**Read in full (text extracted to scratchpad; raw folder untouched, original files not modified):** `Packaging (Thumbnail_Title) - SOP(1).pdf` (1 p, sha256 b59c1a19…565555c), `Viral Checklist.pdf` (2 p, sha256 2d31bc62…2f22fd3), `YouTube Title Analyzer — Natural Language Prompts (2).pdf` (6 p, title-formula section read; long prompt list skimmed), `Hook guide.pdf` (58 p; opening 3-step formula and enhancers read, remaining pages skimmed), `🎯 YouTube Video SEO – COMPLETE CHECKLIST DOCUMENT (1).pdf` (13 p, first part read). **Not opened:** Script Analyzer, Intro Analyzer, Seven-Engine prompts, Renae blueprint, algorithm guides (DS-000011), DS-000018, DS-000031, supplement 2026-11-11.
**Rule class (AGENTS.md):** all of this is creator-authored advice or AI-generated summaries of videos — *creative heuristics / owner-supplied claims*, not platform facts and not evidence for this channel. Numbers such as "10%+ CTR" are the document's goal statements, not benchmarks or forecasts (L12).

## What each document says (paraphrase) and how it applies
| Source | Rule (class) | Application to Unreasonably Exact | Verdict |
|---|---|---|---|
| Packaging SOP §3 | Packaging claims must be true; realistic > fake attention; first 10 s of the video act as packaging (creative heuristic) | Matches L1/L4 and the plan's "truthful single promise". The first 10 s must deliver the title's exact quantity. | APPLY |
| SOP §4 | Bright natural colours, big bold few-word text, ONE big idea; title one sentence, short for broad / longer for narrow topics | Thumbnails: one number or one image per video; titles one sentence. The "1 km vs Edge of Space" title is a narrow, specific one-sentence title. | APPLY |
| SOP §5 | "Audience desire > design"; get feedback on packaging before finalising | We have no audience data; feedback = the owner/third-party review, not a CTR forecast. | APPLY (as a process step) |
| SOP §6 | Packaging should signal video length/type (a 10-min video should not look like a documentary) | Long vs Short packaging must differ; the Short "farthest from anyone" must not look like a long documentary. | APPLY |
| SOP §7 | Previous video experience affects the next click | Supports ordering a strong, ready first long, and not publishing weak filler (WIB-36 first only if ready). | APPLY (qualitative) |
| Title Analyzer prompts | Key information within the first ~55 characters; clear and direct, not clever analogies; curiosity gap; emotional trigger (awe/wonder) | Check below. Prompts are tool instructions, not evidence. | APPLY as a checklist |
| Title Analyzer "viral title formulas" | "Should Not Exist", "What X Feels Like", "[X] Just [did the impossible]", "Every Rank" etc. | Examples include unverifiable shock claims ("defies every law of physics"). Fails L1 and the truthful-promise rule for science titles. | REJECT the sensational formulas; keep only the "specific quantity" idea |
| Title Analyzer note on "Viewer Satisfaction"/Gemini signals | Claims about how YouTube measures satisfaction | Unverified in this document; treat as REPORTED only. Not used for any decision. | NOT USED |
| Viral Checklist (finance-creator checklist) | Pain point, transformation promise, contrarian thinking, numbers, urgency, "enhancer words" (secret, money, mistake), famous names | Genre mismatch for hypothetical science. Usable: specificity & numbers (204 km/h, 3,596.4 km) and concision. Not usable: pain/transformation/motivation; "credibility hack" with famous names would imply affiliation with xkcd or Randall Munroe → do NOT put those names in titles. | PARTIAL |
| Hook guide (3-step formula: Context Lean → Scroll-stop interjection ("but…") → Contrarian snapback; visual hook of 3–5 bold words) | Creative structure from a transcript summary | Usable for the first 10 s: state the question, add a contrast ("but the speed barely changes"), then the twist as the quantity. The twist must be the computed result, not an invented surprise. Not evidence that it raises retention. | APPLY to Shorts and long openings, with science-truth gate |
| SEO checklist | Main keyword in first 30 s; competition check of top results; one-line audience promise | Competition check is exactly what the saturation evidence did. Keyword tools (vidIQ/TubeBuddy) not used. | PARTIAL |

## Check of the current candidate packaging against these rules
| Title (TOPIC_PACKAGING_AND_SCIENCE_NOTES.md) | Chars | Key info in first 55? | Notes |
|---|---|---|---|
| Does a Higher Fall Hit Harder? 1 km vs the Edge of Space | 56 | Yes (cut at char 55 leaves "Edge of Spac"; the key question is earlier) | One sentence, specific. "Edge of Space" is the claim "100 km" – state the altitude on screen. |
| The Fall That Ends at the Same Speed | 36 | Yes | **Risk:** "same speed" is true only inside the model (204.0 vs 204.3 km/h with an unverified drag value; 186–229 km/h under ±20%). Use only with the assumption visible, or soften ("almost the same speed"). Truthfulness rule applies. |
| Could You Jump Into Orbit on a Tiny World? | 42 | Yes | Clear, no clever analogy. |
| The Planet Where One Jump Never Ends | 36 | Yes | Metaphor-leaning; "never ends" overstates (an orbit is a result for a stated radius/density). Prefer the question title. |
| What If a Pellet Were Neutron-Star Matter? | 42 | Yes | Avoids "bullet". Weight is conditional ("if something held it together") — put that condition in the first 10 s. |
**Unverified / not done:** thumbnails, the actual first 10 s, and any CTR claim. This is a rule check against creator advice, not a performance prediction.

## Impact on the plan
- No candidate decision or score changed. Packaging fields got tighter: (1) avoid sensational formulas and famous-name hooks, (2) soften "same speed" wording unless assumptions are on screen, (3) state conditions (altitude, radius/density, held-together) within the first 10 s, (4) Short vs long packaging must look different.
- Contradiction observed: the Viral Checklist urges "contrarian thinking" and "enhancer words", while the Packaging SOP says claims must be true and realistic. The plan resolves it by allowing contrast only where the computed result is itself surprising.
