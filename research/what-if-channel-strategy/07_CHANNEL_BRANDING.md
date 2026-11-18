# 07 — Channel branding: name, logo, banner, descriptions (proposal, 2026-11-18)

**Status:** PROPOSAL. The owner picks the final name. Every asset below is generated from one script (`branding/make_brand_assets.py`), so changing the name means editing one constant and re-running it.

## 1. Brand position (from the research, not taste)

**What the research says the channel should stand for:**

| Finding | Source | Brand consequence |
|---|---|---|
| Competitors win with "one big subject + a hard number" packaging. xkcd wins without text only because it is a 1.38M-subscriber brand | 03 §4 | The brand look must carry **numbers**, not a mascot |
| All three CT-scanned outliers use a persistent progress tracker | 04 §3 | Visual motif = a **ruler/ladder** |
| Tracer's trust device (labelled layers plus on-screen citations) vs Fossil's factual slip | 04 §2–3 | Differentiator = **accuracy you can see**: SIMULATION / REAL DATA / THE MATH tags |
| Science pass corrected 2 thumbnails and reframed 6 angles | 06 | The promise has to be kept: "exact" is a commitment, not decoration |
| "What If" is crowded (34 of 58 current search titles) and Marvel holds a registered WHAT IF... mark (Reg. 1868234, comics) | 02 data; Justia (https://trademarks.justia.com/744/27/what-74427882.html) | **Keep "What if" out of the channel name.** Use it freely in titles for hypotheticals (owner rule, 06) |
| Creator heuristic: a faceless channel should be a searchable *brand*, with the same name on other platforms; start fresh rather than rebrand a channel with more than 200 subscribers | Reference framework RM-1f228411d7ab:chunk.157, chunk.133 (creator heuristic, **not** a platform fact) | Choose a name whose handle is free, and claim the same name off YouTube too |

**Position statement:** ridiculous questions, answered with real physics, with the working shown. The brand is the *gap* between an absurd premise and a precise answer.

## 2. Name

**How names were checked:** 31 candidates. For each, YouTube channel search plus a `/@handle` probe (`data/name_collision_checks_2026-11-18.tsv`), then a web/trademark search on the finalists.

**Limits:**
- The searches were personalised (signed-in Chrome).
- A free handle can be taken at any time.
- The trademark searches went through aggregators, not the USPTO.

| Rank | Name | Handle | Evidence | For | Against |
|---|---|---|---|---|---|
| **1 (recommended)** | **Unreasonably Exact** | @unreasonablyexact (free) | No same-name channel. No brand, book or trademark found for the phrase (only unrelated "Unreasonable" marks) | States the differentiator outright. Funny, which suits the genre. Works for any topic, so it does not lock the channel into a format | 18 characters, long for a spoken name. "Exact" is a promise that every video must keep |
| 2 | Absurd Precision | @absurdprecision (free) | No brand found | Shorter; the same promise | Near-collision: "Absurdly Precise" (3 subs, handle @asskmewhatif, a what-if channel) |
| 3 | Hypothetically Exact | @hypotheticallyexact (free) | Clean | Says "hypothetical" without "what if" | Longer, softer |
| 4 | Fermi Ladder | @fermiladder (free) | Clean | Nerd credibility (Fermi estimates) plus the ladder format | Obscure to a general audience; ties the brand to one format |

**Rejected because taken or crowded:**
- Order of Magnitude
- Napkin Math
- Run the Numbers
- Edge Case
- Measure Twice
- Back of the Envelope
- Sanity Check
- Show Your Working
- Scale Ladder
- Rung by Rung
- Seriously Hypothetical
- Absurdly Precise
- (others in the TSV)

**Before committing to a name:**
1. Claim the handle in YouTube Studio; that is the authoritative check.
2. Check that the same name is free on Instagram, TikTok and X, and as a .com domain (not checked here).
3. If you want legal certainty, search the USPTO directly.

## 3. Visual identity

**Assets** (in `branding/`; SVG = editable source, PNG = upload file):

| Asset | File | YouTube spec it meets |
|---|---|---|
| Profile picture | `logo_profile.png` (800×800) | Displayed at 98 px as a circle; JPG/PNG; ≤ 15 MB |
| Banner | `banner.png` (2560×1440) | Recommended 2560×1440, min 2048×1152, 16:9, ≤ 6 MB. Text and logo sit in the centred 1546×423 safe area (`banner_safe_area_check.png` shows the box) |
| Video watermark | `watermark.png` (300×300) | Square, min 150×150, < 1 MB |
| Sample thumbnail (Day 25) | `thumbnail_sample_day25.png` (1280×720) | Shows the thumbnail system: one subject, one verified number, one evidence tag |

The specs come from YouTube Help, "Manage your channel branding": https://support.google.com/youtube/answer/10456525

**Logo (the "≈ → =" mark):**
- A rough wave (≈, "about") sits over a dead-straight line (=, "exactly"), with three ruler ticks.
- It reads as *rough question → exact answer*.
- It has no text, so it survives a name change. It has no figure, so there is no stick-figure resemblance (IP boundary, 01 §6).
- Checked at the 98 px display size: it is still legible.

**Banner:**
- A log-scale ruler from 1 m to 10 light-years. Every rung is a verified number from this calendar (06):
  - 1 m
  - 39 km (fastest fall)
  - 3,596 km (loneliest human)
  - 406,771 km (Artemis II)
  - 10 ly (alien astronomers)
- The ruler *is* the progress-tracker motif from 04.
- The evidence-layer tags sit below the safe area, so only TV viewers see them. The faint ruler line extends to the edges for desktop.

**Palette:**

| Token | Hex | Use |
|---|---|---|
| Ink | `#10182B` | Background |
| Paper | `#F3EEE3` | Line art, text |
| Signal | `#FF8A1F` | The exact answer, the key number, the main rung (one per frame) |
| SIMULATION | `#9B8CFF` | Modelled segments |
| REAL DATA | `#3CC6B3` | Measured or recorded facts |
| THE MATH | `#FFC23D` | Worked calculations |

**Type:**
- Avenir Next Heavy for the wordmark and thumbnail words.
- Avenir Next Medium for the tagline.
- Menlo Bold for numbers and tags.
- These are the macOS system fonts used in the render. On another machine, either install them or swap in free near-equivalents (Nunito Sans Black, JetBrains Mono), then re-render.

**Thumbnail rules:**
- 1 subject.
- 1 verified number in Signal orange, at most 4 words.
- 1 evidence tag in a corner.
- Draw to scale wherever the scale *is* the story. In the Day 25 sample, the ~110 km lunar orbit is drawn at 12 px against a 1,737 km Moon radius of 190 px. The draft had it about 4× too far out, and that was corrected.

## 4. Descriptions (ready to paste)

**Channel description** (726 characters; YouTube limit 1,000):

```
Absurd questions. Real numbers. Sources on screen.

How fast would you fall from every height between 1 metre and the edge of space? Who was the loneliest human ever? We take ridiculous hypotheticals seriously and answer them with real physics, worked out step by step.

Every video labels what you're looking at:
SIMULATION - what we modelled
REAL DATA - what was measured
THE MATH - how we got the number

Numbers are recomputed from primary sources (NASA, JPL, peer-reviewed papers), and every source is listed in the video description. Get something wrong and we pin the correction.

New long videos twice a week, plus Shorts.

Original animation. Independent channel, not affiliated with any book, comic or other channel.
```

Keep "we pin the correction" only if you will actually do it (it is a promise).

**Video description template:**

```
<One-sentence answer-first hook that matches the title.>

<2–3 sentences: what the video works out and the surprising result.>

CHAPTERS
00:00 <cold open: the most extreme rung>
...

SOURCES (as shown on screen)
[REAL DATA] <claim> — <source, URL>
[THE MATH] <what we calculated, from which inputs>
[SIMULATION] <what is modelled and its main simplification>

Corrections: <none yet / pinned comment>
```

**Short description** (Shorts get very little description reading):
- one line hook
- "Full video:" link
- one source line

**Channel keywords:**
- what if science
- hypothetical physics
- science explained
- physics calculations
- space
- astronomy
- scale comparison
- thought experiment
- fermi estimate
- science animation

**Playlists** (one per format family; this mirrors the calendar's test design and the end-screen rule "next video of the same family"):

| Playlist | Family |
|---|---|
| Every Rung (ladders) | L |
| To Scale | S |
| Timelines | T |
| Runaways | R |
| One Number | Q |
| Shorts | — |

## 5. What this does not prove

- None of these choices is tested. Brand effect on CTR cannot be measured before launch.
- The Day 14 and Day 30 reviews (05 §4–5) judge format families, not branding. Do not change the branding during the 30-day test, or the comparison breaks.
- The name checks are a snapshot from a personalised YouTube session.
- No professional designer reviewed the art. The assets are clean, honest starting points, not final brand work.
