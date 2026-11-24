# Blueprint 07 — SHORT — Lunar laser round trip (Day 19)

**STATUS: PARTIAL — NEEDS SOURCE/CALCULATION.** The timing answer (≈ 2.56 s mean, 2.4–2.7 s range, Apollo-11 reflector, first echo 1 Aug 1969) is sourced or arithmetic. The "about one photon returns" twist is only snippet-level (Murphy review, APOLLO) and is gated until the primary paper is read. SELF-REVIEW.

## A. IDENTITY
- **Calendar:** Day 19, Short (45–60 s).
- **Current working title:** "How Long Does a Laser Take to Reach the Moon and Return?"
- **Issue:** none material; "return" implies something to bounce off.
- **Proposed alternatives:**
  1. "How Long Does a Laser Pulse Take to Hit the Moon and Come Back?" (Claude review's wording, close)
  2. "A Laser Fired at the Moon: When Does the Echo Arrive?" (adds the echo)
- **Central question:** How long does a laser pulse take to go to the Moon and back?
- **One-sentence answer (qualified):** About 2.5 seconds — 2.56 s at the mean distance, varying between roughly 2.4 and 2.7 s as the Moon's distance changes — and it only works because astronauts left mirrors there; about one photon of the ~2.7×10¹⁷ sent makes it back (gated beat).
- **Viewer expects:** a number (1–2 seconds?).
- **Viewer actually learns:** the number, why it moves, and that the echo is a handful of photons, not a flash.

## B. PRECISE SCENARIO
- **Changes:** none hypothetical; it is a real experiment. The model uses centre-to-centre distance (V07-C01) and a surface-to-surface check (V07-C05).
- **Normal:** light at c; the Moon at its real distances (NSSDC mean perigee 363,300 km, apogee 405,500 km; V07-C02).
- **Known:** first echo 1 Aug 1969 via Lick's 3 m telescope to the Apollo-11 array of 100 corner cubes (V07-C03, NIST). **Gated:** return rate (V07-C04).

## C. DEPENDENCY MAP
| Needed | Source | Status |
|---|---|---|
| t = 2d/c with c exact | defined constant; NSSDC distances (V07-C01/C02) | calculation |
| Range 2.4–2.7 s | NSSDC means; Murphy 2.33–2.71 s (snippet) | extreme values not used |
| Apollo-11 array, 1969 | NIST (V07-C03) | SOURCE_READ_EXTRACT |
| Photons out ≈ 2.7e17 | E = hc/λ for 100 mJ, 532 nm (V07-C04) | arithmetic with snippet inputs |
| Photons back ≈ 1 | Murphy/APOLLO snippets | **SNIPPET_ONLY** |

## D. CAUSE-AND-EFFECT STORY (compact)
| # | Cause / question | Science | Result | Leads to | Visual | Claim |
|---|---|---|---|---|---|---|
| 1 | Hook: "Fire a laser at the Moon. When does the echo arrive?" | — | the guess | "how far is the Moon in light?" | beam from Earth, running clock | — |
| 2 | THEREFORE use distance and c | one way ≈ 1.28 s; round trip ≈ 2.56 s | ~2.5 s | "does it stay at 2.56?" | clock reading 2.56 s with the formula t = 2d / c | V07-C01 |
| 3 | BUT the Moon's distance changes | mean perigee 363,300 km → 2.42 s; mean apogee 405,500 km → 2.71 s | 2.4–2.7 s | "what bounces it back?" | the elliptical orbit exaggerated, two clock values | V07-C02 |
| 4 | THEREFORE you need a mirror | Apollo 11's array of 100 corner cubes; first echo 1 Aug 1969 | the echo is a real measurement | "how strong is the echo?" | corner-cube sketch (three mutually perpendicular faces) | V07-C03 |
| 5 | **GATED beat:** BUT the echo is nearly nothing | a 100 mJ pulse holds ≈ 2.7e17 photons; on the order of one returns | "billions of billions out, about one back" | answer | tank of photons vs one photon | V07-C04 |

## E. NUMBERS INTO IMAGINABLE SCALE
- 2.56 s ≈ "the time it takes to say 'Moon' slowly twice" (approximate).
- 384,400 km: "about 30 Earths side by side" (30.1 Earth diameters at 12,742 km — arithmetic).
- 2.7e17 photons: a count, no analogy (avoid false precision); "≈ 1 back" only when sourced.

## F. HOOK, ESCALATION AND ENDING
- Hook (0–5 s): "How long does a laser take to get to the Moon and back?"
- First non-obvious reason: it isn't a constant, and you can't just see the echo.
- Escalation: one step (timing → mirror → echo strength).
- Direct answer: "About two and a half seconds — and the echo is almost nothing."
- Dry humor option: "the worst mirror-selfie in the Solar System." (optional) No-joke alternative: end on the 2.4–2.7 s range.

## G. VISUAL COMMUNICATION (text only)
- Clock readings in seconds with units; distance in km; an elliptical orbit labelled "exaggerated".
- Corner cube drawn schematically; do not copy any particular photograph.
- Must not depict: a laser visibly lighting the Moon's surface; a thick returning beam.

## H. ORIGINALITY AND PRIOR ART
- Closest: Munroe "Laser Pointer" (pp.27-34, many lasers at the Moon; adjacent premise, not round-trip timing) and the xkcd video "What if everyone pointed a laser at the moon?" (JqFSGkFPipM; title/metadata only, not watched). Codex noted an xkcd video about illumination/aiming lasers — different question.
- Ours: a timing question plus the reflector story and the echo's weakness.
- Do not copy: the chapter's jokes, numbers sequence or drawings.

## I. SCIENCE AND EDITORIAL REVIEW (SELF-REVIEW)
- Qualified: timing arithmetic and NASA means; NIST history.
- Open: the photon return rate (primary needed); extreme distances (recalled) not used.
- Highest-risk misunderstanding: "you can see the laser spot on the Moon" or "the Moon distance is fixed". Mitigation: range beat.
- Reviewer: lunar-laser-ranging literature check (Murphy, APOLLO) — not an expert sign-off.
- Blockers: read the primary return-rate source or drop beat 5.
- Confidence: research 0.85 for timing, 0.4 for the photon beat; story clarity high.

## J. FORMAT AND DEPENDENCIES
- Standalone; no parent. It echoes the Voyager "light-time" idea (Day 7) but needs no other video.
- If delayed: no effect on others. If the photon source isn't read: ship beats 1–4 (complete question and answer).
