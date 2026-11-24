# DS-000011 remaining files: review and application (2026-11-23)

Raw folder `data/raw/global-youtube-knowledge/DS-000011/` was opened read-only; text was extracted to a scratchpad. `git status` there stays clean. Nothing in this note changes a topic decision, score, order or the cadence recommendation (B, fallback A).

## Count correction
The folder holds **17 files**, not 18. 5 were read earlier (see DS000011_PACKAGING_AND_HOOK_APPLICATION.md). The other **12** are covered here, so all 17 have now been opened. Depth differs (see column "Depth").

## Classification (all are creator advice or AI-generated summaries, not platform facts, not channel evidence)
| File (sha256 prefix) | What it is | Rule class | Depth |
|---|---|---|---|
| Hook (1).pdf (4129b210) | Same extracted text as Hook guide.pdf (0 diff lines); different bytes/hash only | Duplicate content, not independent evidence | text diff |
| Engine-by-Engine Personality (09b5a16f) | Six AI "filmmaker personas" (ChatGPT = Nolan+Sorkin, etc.) | Tool-specific / role-play prompt design | full |
| Intro Analyzer Prompts (cb50fe7e) | 7 persona prompts for 0-30 s intro review | Tool-specific prompts | full |
| Script Analyzer (6d9840bb) | 7 persona prompts for script review | Tool-specific prompts | full |
| Seven Engine Storytelling Prompts (24270755) | 7 prompts + "16 Commandments of Storytelling" | Creative heuristic | full |
| BUT/THEREFORE (52235e94) | Chat transcript about the South Park rule + "Fusion Framework" | Creative heuristic (structure) | full |
| Renae Creative Engine v2.5 (aacc8fc2) | Blueprint to turn xkcd What If into "cinematic" videos | Creative heuristic + owner-style preference | first ~230 lines of 12 pages (rest is the same four foundations restated) |
| YouTube_Intelligence_Brain v1 (115e9d39) | A "creator OS" prompt for a doctor-led senior-health channel | Tool-specific prompt; **different channel** | full |
| YouTube algorithm guide (d0f681dd, 117 pp) | Many creator videos summarised by an AI | Empirical hypotheses / platform claims, mostly unverified | headings + cadence and number greps only (not every page) |
| new YT algorithms updates (62565f03, 45 pp) | AI commentary on creator whiteboards, caption update, story angles | Empirical hypotheses | first ~420 lines |
| Nano-Banana prompt guide (445c7efa) | Image-prompt template | Tool-specific | head only |
| VEO 3 prompt guide (ccbee7dd) | Video-prompt template | Tool-specific | head only |

## What is usable
- **BUT / THEREFORE and "no AND THEN"** (Seven Engine #3, BUT/THEREFORE file, Renae, Brain). Consistent across files and already how the What If candidates are built (setup, twist, computed result). Use as a script check, not as a ranking factor.
- **Promise delivery** (Commandment 4). Matches the existing title risk checks (the "same speed" and "jump never ends" wording). Reinforces, does not add.
- **Brain md, truth hierarchy** (official docs > own analytics > supplied evidence > playbooks > creator patterns > hypotheses; "never present a hypothesis as an algorithmic fact"). Same discipline as rules L1-L20. It is also the one file that warns against pattern breaks "on a timer".
- **Story angle vs topic** (new YT algorithms updates): saturation is at the angle level. Consistent with my topic-vs-angle split. It is an opinion, not tested here.
- **Renae**: explicitly keeps xkcd black-and-white minimalism and changes pacing, sound and structure. A style preference for this channel's owner, not evidence about what performs.

## What is not used (and why)
- **Numeric thresholds**: "CTR above 7% likely to go viral", "retention above 40% / 30%", "CTR 9-12% is a green flag", "stay-to-watch at least 80%", "60%+ AVD in first 3 videos", Renae's 90-day "+10% AVD / +15% retention / +10% CTR". These are unsourced creator or AI statements, and some conflict with each other (7% vs 10%). They are not benchmarks and not forecasts, so none enters a score, a plan target or a go/no-go (L-rules: no numeric forecasts).
- **Cadence advice**: "post 3-5 Shorts per week max", "pause uploads 48 hours after a Short performs", "react within 24-48 hours of a trend", "8-12 minute format". Single-source, unverified. Cadence B (6 longs + 8 Shorts in 60 days, about one Short a week) is far below the 3-5 ceiling, so there is no conflict, but the advice is not support for B either. B still rests on the observed competitor cadence in this audit.
- **Fixed reset timers** ("reset every 20-30 s", "micro-hook every 2-3 s", "BUT/THEREFORE every 8-12 s"). Arbitrary and inconsistent across files; Brain md itself says not to do this.
- **Persona claims** ("ChatGPT thinks like Nolan", "Grok has chaos pacing"). Role-play labels. Not capabilities, not evidence.
- **"Viewer satisfaction / YouTube reads captions as a ranking signal / copy winners and change angle 3-20%"**. Unverified; not used.
- **Brain md senior-health rules and Dr. Rehan mode**. Another channel. Not applied here (channel intelligence stays separate).
- **VEO 3 / Nano-Banana**: generation tooling advice (clip length, credits, access). Time-sensitive tool facts, not checked; irrelevant to topic order.
- **"Installed in memory 2025-10-20"** style lines in the BUT/THEREFORE file are chat residue, not facts about any system here.

## Internal conflicts found in the corpus
- CTR "strong" thresholds differ (7% vs 9-12% vs 10%+).
- Pattern-break advice differs (timers in Renae/Seven Engine vs "do not use timers" in Brain md).
- Algorithm guide: "algorithm does not reward consistency" (around line 1002) next to "maintain upload consistency" (around line 2854).

## Plan impact
None to topic order, scores or cadence. Two script-time checks are reinforced: (1) every beat should be setup, BUT or THEREFORE, and (2) the title promise must be delivered inside the video. Both already apply.

## Not done
- Algorithm guide (117 pp) and algorithm updates (45 pp) were not read line by line; only structure and number/cadence greps. A claim I did not grep for could exist.
- Renae pages after the first ~230 lines, Nano-Banana and VEO 3 beyond the head were skimmed, not studied.
- DS-000018 snapshot zip, DS-000031 and the 2026-11-11 supplement are still unopened.
