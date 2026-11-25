# Lead Claude's own transcript review (2026-11-24)

Row-level record: `LEAD_TRANSCRIPT_READING_LEDGER.csv` (83 rows, 22 required columns + none removed). T-numbers below = row order (T01–T43 long, T44–T83 Shorts, in the order of `research/what-if-scripts/long/` then `shorts/`). ¶ = paragraph number in the reflowed file.

## 1. What I personally read, and how
- **Inventory:** 83 transcripts exist (43 `long`, 40 `shorts`) in `research/what-if-scripts/`, each citing a raw file `data/raw/competitors/DS-000017/apify/mzl5dCHF81LbcBamS/transcripts/<id>.txt` and its SHA-256. Check run before reading: all 83 raw files exist, every sha256 matches, and the word sequence of each reflowed file equals the raw file's (punctuation-insensitive). So reading the reflowed file is reading the raw content, with paragraph numbers added.
- **Two further transcripts** (`9VG0yqq_PHM`, `X97DDWvxaqQ`) are listed by the README as identity-verified but transcript-pending: **not available, not read, not counted**.
- **Reading:** I (the lead) printed every transcript with paragraph numbers and read each from first to last paragraph, in 10 batches, writing notes after every batch. No sub-agent output, earlier summary, coverage CSV or statistic was used to set `lead_claude_personally_read=YES`. Pre-existing audits were not opened for this review.
- **Exceptions:** T30 (`DiWFXv9N0Vs`) and T82 (`mEUqVgGf4e0`) end mid-sentence in the source ("…until they suddenly u…"): read in full as available; status `FULL_READ_BY_LEAD_SOURCE_TRUNCATED_AT_END`.
- **Not observed:** pictures, audio, timing, thumbnails, on-screen labels. Many scripts say "looks like this / this many" and the result lives on screen only (T01 ¶10,13,21; T12 ¶11,19; T13 ¶2; T53 ¶5). I cannot judge the visuals, only the narration.
- **Caption quality:** about 15 long transcripts look like auto captions (run-on blocks, garbled units, e.g. T03, T18, T19, T25, T28, T31–T34, T37–T40, T42, T43). Do not copy numbers from them. T18 has "5 m", "6 paws", "pawatts"; T28 "mill Fahrenheit"; T34 "1.5 mill", "kilogjle"; T03 "500 m" for the LHC beam (the Short T52 correctly says 500 miles).

## 2. What I learned: the narrative shape, with exceptions
(Counts are my own tallies from reading; they are approximate where marked.)

**Opening.** 41 of 43 longs open with a named asker plus the restated question (exceptions: T19 self-attributed new chapter with the only spoken promo; T24 popularity framing). Many add a deflating, blunt or counter-intuitive first answer: T04 ¶2 "nearly everyone would die", T15 ¶2 "wouldn't even warm you", T26 ¶3 flamethrower is the practical one, T07 ¶2 "not for the reason I expected", T40 ¶1 "most bowling balls float". Only 5 of 40 Shorts keep an asker (T64, T65, T68, T78, T81); the rest start on the question or premise sentence.

**Rules of the hypothetical.** The premise is made explicit, often as a named allowance, and everything else is held to real physics: T05 ¶2 (0.9c at release, then normal physics), T09 ¶3-4, T17 ¶3-4, T43 ¶3 (water replaced by air), T38 (allowances stacked until the question stops being physics ¶5-6). Slippery terms are defined by negative examples (T32 ¶2-3 "this is not a sunset"; T25 ¶2 money vs cash).

**Reasoning chains come in four shapes.**
1. *Limit ladder*: propose a version, defeat it with the next physical limit, repeat (T01, T03, T18, T19, T27, T36, T38). The last rung can be a hard ceiling (T19 ¶pair-production) or a number that proves impossibility (T27 ¶26 0.25c).
2. *Clock/time ladder*: consequences ordered by elapsed time (T05 nanoseconds, T16 microseconds→half-second, T17 day→1500 years, T37 hours→2 million years, T43 seconds→years). Scale questions use these.
3. *Invariant-first*: show what does not change, then rank what does (T20 ¶7-10 buoyancy and drag independent of gravity; T28 ¶5 gravity same outside a sphere; T09 ¶6 Earth unaffected).
4. *Feasibility audit*: multiply unit-bearing quantities to a power or mass and compare with a familiar load (T06 ¶4, T26 ¶25, T34, T63, T10).

**Number → picture.** Most numbers are given an anchor: 1 ns ≈ a foot of light (T15 ¶2), 100 pounds on a glass (T16 ¶24), Boston molasses (T25 ¶5), a squirrel lifted 300 microns (T34), a basketball-court circle (T10 ¶8). The exceptions are catalogues where the arithmetic is hidden (T02, T23, T44, T45, T72–T74).

**Uncertainty is stated in plain words, sometimes by quoting an expert.** Best models: T30 ¶12-13 (string theorist "we just don't know"), T07 ¶30 ("a conservative guess"), T29 ¶15-21 (sloppy estimate announced as sloppy), T23 ¶6,24 ("wild guess"), T35 ¶6 ("nobody has ever lost all their DNA"), T41 ¶29-30, T38 ¶6 (stop when the rules turn into fantasy), T22 ¶11-12 (arbitrary date disclosed).

**Answer position.** Early verdict is the common order (T02, T04–T09, T13, T15, T16, T18, T26–T31, T35, T36, T41–T43 give the answer or its sting in the first three paragraphs). Late or withheld on purpose: T11 (decoy, then solar, then the real answer ¶44), T24 (one-line reveal ¶33), T01 (answer ¶28-29), T14 (open two-outcome ending ¶36-37), T19 (limit at the end). So "answer early" is a tendency, "answer late" is also used when the structure is a ladder of candidates.

**Humor.** Always dry, usually attached to a completed explanation (T26 'Usually.', T36 ¶25 "ammunition – I mean fuel", T07 ¶45 detonators). Roughly two-thirds of longs end on a joke or callback (my count ~29/43), the rest on a principle, wonder image, limit or plain conclusion (T15, T17, T19, T20, T21, T30, T37). Counter-examples where humor replaces explanation: T24 (whole structure is irony; the answer is unreasoned), T02 (catalogue), T81 (humor-only Short). T19 is almost joke-free. **No transcript contains a subscribe/like CTA; the only spoken promo is T19 ¶1.**

**Tone adaptation.** T21 speaks to a four-year-old and still carries real physics (ladder ×100, centrifugal crossover ¶32-33). T31/T79/T80 treat a taboo topic with a moral line first. Both show the framework is not one fixed voice.

## 3. Long versus Short
- 38 of 40 Shorts are deletion-only or lightly cleaned cuts of one long (T83 is a clean re-edit of T32 with names and spelling fixed; T75 and T77 are clean cuts of auto-caption longs). Independent Shorts: T70 ("why is the sky blue", essay-like, no hypothetical) and T81 (inbox compilation).
- A Short is **one mechanism or one ladder**, sometimes one half of a long (T44/T45 from T02; T51/T52 from T03; T55/T56 from T04; T65/T66 from T21; T53/T54 from T01; T79/T80 from T31; T72/T73/T74/T71 from T23).
- Seams where cut-downs fail to stand alone: orphaned visual reference (T58 "You can also see…"), a picture-only answer (T53 ¶5, T63 ¶2 before ¶3 gives six), a missing explanation of terms (T47 starts mid-argument), a lost caveat (T82 drops the expert quote, T76 drops the honest "wouldn't fit"), a scenario half without its payoff (T66 ends on money).
- Lengths for reference only: longs 591–1,414 words (median ≈ 680); Shorts 79–492 words (T83 = 492 words in 2:10, T57 = 445 in 1:54). Not our targets.

## 4. Counterexamples to any proposed rule
| Proposed rule | Counterexample |
|---|---|
| Open on a named asker | T19, T24, all but 5 Shorts |
| Early verdict | T11, T24, T01, T14 |
| Humor on top of reasoning | T24, T81 |
| A reasoning chain exists | T02, T23, T44–T45, T72–T74 are catalogues |
| End on a joke | T15, T17, T19, T20, T21, T30 |
| Hypothetical always defined | T70 (no hypothetical), T33/T34 (a device or measurement question) |

## 5. Transcripts most relevant to our ten slots (patterns to learn, not wording to copy)
- Fall/drag/terminal speed: T40 (time = depth ÷ terminal speed; test the hidden assumption first), T37 (steady rate → timeline), T16 (pressure force), T38 (stop when physics ends).
- Light time / signals: T15 ¶2 (1 ns ≈ 1 ft), T18/T19 (laser limits, diffraction), T01 ¶11.
- Orbits/escape/low gravity: T20 (invariants), T17 ¶34-36 (Roche limit), T21 ¶32 (gravity vs centrifugal crossover), T28.
- Moon/tides/ocean: T04 ¶26 (tidal re-spin), T12 and T14 (stage ladders on a map), T28 ¶5-7 (invariant-first, small effects ranked), T24.
- Honest-limit language: T30, T07 ¶30, T29, T23, T38.
- **No transcript covers Voyager, Phobos, lunar-laser ranging or the farthest human.** That is a gap and an originality opportunity; it also means we have no xkcd evidence for how those exact topics are told.

## 6. How this changes the working framework
See `../CHANNEL_FRAMEWORK_V2.md` (section "What changed after my own reading"). In short: (1) my reading confirms the earlier tallies on asker (41/43) and Shorts asker (5/40) and Short = cut (38/40); (2) it adds the four reasoning shapes and the stop-when-physics-ends device; (3) it adds seam-checking for Shorts and the caption-quality warning; (4) it strengthens the instruction to state the arithmetic aloud because the xkcd Shorts that hide the figure on screen fail as stand-alone audio.

## 7. Limits of this review
One reader (the lead), one pass, text only, no visuals. Tallies are mine and approximate where marked. These are descriptions of 83 scripts, not evidence of xkcd's private process, and not evidence of what drives views or retention.
