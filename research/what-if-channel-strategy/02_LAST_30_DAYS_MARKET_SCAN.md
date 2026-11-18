# 02 — Last-30-days market scan (YouTube + Google Trends)

Observed 2026-11-18 via Claude in Chrome (owner-approved). Follows `01_COMPETITOR_AND_SOURCE_BANK_AUDIT.md`.
Labels: FACT (observed public number), DERIVED (computed from observed), INTERPRETATION, HYPOTHESIS.

## Sources

| ID | What | File (data/) | sha256 |
|---|---|---|---|
| SRC-YTS | 27 YouTube searches, "This month" filter, 713 unique results (596 Shorts, 117 longs) | `yt_search_thismonth_2026-11-18_top.tsv`, `..._query_summary.tsv` | 757108…5573, 78ed38…d0b |
| SRC-CHC | 11 channels, /videos + /shorts first page | `channel_census_2026-11-18.tsv` | af7f333d…d5573 |
| SRC-GT | Google Trends, YouTube + web search, 30d + 12m, 4 groups × 5 terms, anchor "black hole" | `google_trends_2026-11-18.tsv` | c649db…abaa |

### Limits (read first)
- The browser was **signed in (region PK)**, so search ranking is personalized. It was not a logged-out sample.
- Search results are ranked, not random. Medians describe what YouTube surfaced, not the niche.
- Shorts shelf capped at 25 per query; Shorts expose no channel or upload age.
- Only the 55 high-view rows were exported, because of a browser-tool output cap. The other 658 rows exist only as the counts in the query summary.
- Trends values are relative **within each 5-term group**. The groups cannot be added together.
- None of this is our audience. Competitor views ≠ our expected views (brief constraint).

## Findings

**F1 — Shorts supply is saturated and mostly unwatched (DERIVED).** 596 this-month "what if" Shorts surfaced, with a median of about 480 views. Only 20 of 596 reached ≥10K and 5 reached ≥100K. Per-query Shorts medians range from 130 to 1,200. INTERPRETATION: low-effort AI "what if" Shorts are flooding the format. A Short-first strategy competes in the noisiest pool.

**F2 — Long-form breakouts by brand-new channels are real (FACT, n small).** Channels about 1 month old with 1–6K subscribers have single videos at 195K–1.3M views within weeks:
- Lightbound: median 56K across 16 longs in about 30 days. TON 618 got 1.3M in 10 days.
- BrainZap: 799K and 660K.
- Manifesting: 977K.
- Ifcognito, Just Imagine if, WhatIfAnimations: one hit each, around 190–430K.

DERIVED: in most of these, the hit is 1–2 videos and the rest sit at about 1–20K, which matches the hit-driven pattern from 01 §2. HYPOTHESIS: the browse/suggested surface currently rewards *scale-visualization* and *"every X" ladder* formats on new channels.

**F3 — Formats that broke out this month (FACT titles; pattern = INTERPRETATION).**
- *Every-X ladder*: "Evolved at Every Ocean Depth", "on Every Planet", "Sun From Every Planet". This is the same ladder found in 5 of xkcd's top-10 longs.
- *Runaway escalation*: "Light Kept Getting Slower and Couldn't Stop".
- *Scale/POV simulation*: TON 618 from different distances, falling into Saturn.
- *Elimination*: "Ocean Rose 2,500 m — Only 1 Country Survives".
- *Whole-humanity transform*: "Every Human Woke Up 1 cm Tall".

**F4 — xkcd itself (FACT).**
- Mariana-Trench nuke: 2.94M in 3 weeks.
- "Eat the sun": 437K in 10 hours.
- A reaction video ("Nuclear Engineer Reacts", 177K) and a Short ("Nuked a Hurricane", 646K) ride the same nuke-the-ocean theme.

INTERPRETATION: "nuke + natural system" is hot *right now*, but it is also xkcd's freshest territory, so the collision risk is high. WIB-SA2 (nuke the hurricane) is timely but crowded.

**F5 — Tier-A bank topics: search supply this month (DERIVED from query summary).**

| Bank topic | This-month longs found | Best Short | Read |
|---|---|---|---|
| WIB-SA2 nuke hurricane | 2 (max 56 views) | 646K | Short demand proven; long gap |
| WIB-30/34 throw/orbital speed | 3–4 (max 154) | 142K / 40K | Short demand proven; long gap |
| WIB-10 hair dryer | 1 (51) | 1.5M (comedic, not physics) | Weak signal: the hit is off-topic |
| WIB-36 falling through Earth | 2 (42) | 10K | Low supply, low demand evidence |
| WIB-53 raindrop | 2 (6) | 5.6K | Low |
| WIB-31 neutrinos | 5 (max 15.6K) | 4.8K | Low |
| WIB-24 Cessna on other planets | 1 (4) | 24K | Low |
| WIB-07 periodic table | 4 (max 466K, a Minecraft video) | 1.6K | Web Trends interest is high (see F6) |
| WIB-17 small planet | 2 (138K) | 14K | Moderate |
| WIB-32 speed bump | 4 (130K, BeamNG crash) | 13K | Demand sits in car-sim content, not physics |

INTERPRETATION: few long-form competitors this month on most tier-A topics. That is either an opening or a sign of no demand. Search data alone cannot tell which.

**F6 — Google Trends (DERIVED, relative only).**
- YouTube search, 30 days: "what if" is about 5× "black hole". "hurricane" (65.8) and "nuke" (34) are large, and "periodic table" is about 28.
- "neutron star", "neutrino", "mariana trench" and "speed of light" each sit at 1–4.
- "sun disappeared" (ratio 1.38) and "earth stopped spinning" (1.67) are rising, but from a near-zero base.
- Web, 30 days: "periodic table" (73) is about 3× "black hole"; "hurricane" is falling (0.72) after the season.
- "xkcd" registers 0 on YouTube search.

INTERPRETATION: viewers don't search for xkcd-style premises by keyword. These are browse/suggested-driven formats, so Trends is weak evidence for topic choice and should be at most a minor scoring input.

**F7 — Channel census.**
- The incumbent "What If" (8.99M subs) runs 20–25 min longs at a median of about 400K.
- minutephysics had no own upload in 30 days.
- Untold Brahmanda is Hindi and is excluded as an English competitor.

## What this changes for scoring (proposal, pending approval)
1. Weight "format fit" (ladder, escalation, scale-POV) above keyword search volume.
2. Long-form first. Shorts serve as excerpts or tests, not the main bet (F1 + 01 §1: 38 of 40 xkcd Shorts are excerpts).
3. Collision penalty for nuke/ocean topics while xkcd's Mariana video is fresh.
4. Trends = tiebreaker only.

## Framework record
This is a market-scan addendum to the 01 audit, not a content plan, so the `--framework-plan` gate does not apply yet. It applies to the calendar.
