# What If? 83-script reverse-engineering study: status and continuation

**Status (2026-11-17): Phase 1 is done. Phase 2: 50/83 audited (V001–V050). The cross-video report (Phase 5) and the playbook (Phase 6) have not started and must not start until 83/83 are done.**

| Deliverable | File | State |
|---|---|---|
| Method, framework record, exceptions | [00_METHOD.md](00_METHOD.md) | done |
| D1 Dataset inventory | [01_INVENTORY.md](01_INVENTORY.md) (+ `inventory.json`) | done: 83 readable, 0 exact duplicates, no timestamps |
| D2 Individual audits | `audits/V###.md` | V001–V050 |
| D3 Comparison matrix | [03_COMPARISON_MATRIX.md](03_COMPARISON_MATRIX.md) (from `matrix.jsonl`) | 50 rows |
| D4 Cross-video report | — | not started (it needs all 83) |
| D5 Master playbook | — | not started |
| D6 Limitations | — | started below; to be finalised with D4 |
| Coverage ledger | `coverage_ledger.json` | synced by `render.py` |

## Continue

1. `python3 render.py` prints the next unprocessed VID.
2. Read that batch's transcripts in full. Shorts that are cut from a long video (see the inventory's Overlap column) must still be read in full and get their own audit. Map which parent ¶ each one reuses with `python3 reuse.py PARENT SHORT` (6-gram overlap above 50% per ¶). In an audit, write another video's paragraph as `V002 ¶5`; `locate.py check` validates it against that video. The same holds for word ranges (`V003 w331–421`). *Fix (batch 4):* until then the check matched only ASCII-hyphen ranges, and every audit uses en dashes, so no word range had ever been checked. It now accepts both and checks single words (`w684`). All V001–V030 ranges pass the stricter check.
3. Write `audits/V###.md` in the same headings as V001, and append one row to `matrix.jsonl`.
4. Run `python3 render.py && python3 locate.py check`. The check must print `ok`.
5. Batches: ~~V011–V020~~, ~~V021–V030~~, ~~V031–V040~~, ~~V041–V050~~ (done), V051–V060, V061–V070, V071–V083.

## Corpus facts already established (High; verified over all 83 raw transcripts)

- **CTAs are almost absent.** No transcript contains subscribe, Patreon, comment, sponsor or next-video wording. There is **one explicit promotion**: V019 opens with the question "comes from me", then names the What If? 10th-anniversary edition as "now available online and in print" (w1–30). *Correction (2026-11-17):* the batch-1 regex missed this promotion because it searched for "my book" and "new book". A broader search (edition, available, in print, anniversary, previous, video) found it. The CTA inventory is completed per audit, not by regex alone.
- **Serial cross-references.** V014 ("In the previous What If"), V018 ("we learned our lesson about that already", a callback to V009), V019 ("at the end of the laser pointer video"), V063 ("the reverse of the video which asked…") and V080 ("from the What If inbox").
- **Derived Shorts.** 56 of 83 transcripts have 30% or more 8-gram overlap with another transcript. Most Shorts are cut-downs of a long video, so the counts in D4 must be reported per video *and* per independent content family.
- **Unpunctuated auto-captions.** V003, V018, V019, V025, V030, V042, V045, V048, V051, V060, V063, V068, V071, V077, V080 and V083 are auto_generated captions. Locators for those that lack punctuation use word ranges (wA–B). V018, V025 and V030 are auto-generated but punctuated; they still use word ranges because their paragraphs are very long.

## Provisional batch-1 observations (V001–V010, all long-form; NOT generalised)

These are working hypotheses to test against the remaining 73 transcripts. They are not findings.

- In 10/10, the opening is an attributed viewer question ("This is a question from [name]…"). In 10/10, the second beat reframes it: misconception correction, flash-forward shock, answer-first with a withheld *reason*, literal deflection, myth-bust, or a performed stammer.
- **Answer early, withhold the mechanism.** This appears in V001, V003, V006 and V007.
- In batch 1, the ending is always a punch-line button or a reframe (a rulebook, a proverb rewrite, deadpan advice, a reality-check quote, an ironic coda), with no summary and no CTA. Batch 2 adds other ending types (see below).
- Recurring spines: the obstacle or constraint ladder (V001, V003, V006, V007), the consequence cascade (V004, V005, V009), the scale ladder (V002) and the frame narrative (V010).
- In every derived Short checked so far (V028/29, V031, V032, V037/38, V040/41, V043/44), the creator cut the long script at a structural seam: an act break, a direction pivot, or one obstacle segment.

## Provisional batch-2 observations (V011–V020, all long-form; NOT generalised)

- The attributed-question opening holds in 19 of V001–V020. **V019 is the exception**: the narrator asks the question ("comes from me") and the line doubles as a book promo.
- New ending types: an elegiac image (V011), a deliberately open question (V014), a moral aphorism (V015, V019), a wonder image after the human story ends (V017), an idiom extension (V016, after V010's proverb rewrite) and a playful real-world CTA (V020).
- **Serial architecture appears.** V012's portal outlet on Mars seeds V014. V017 winks at V012. V018 calls back to V009. V019 refuses V018's ending and takes its title from V018's refrain.
- New loop devices: a false final answer (V011), an intentionally abandoned comic loop (V015), an announced deferral "in a minute" (V019), a six-times refrain (V018), a running indicator thread (V017's pendulum clock) and a running gag subplot (V012's Dutch, V014's map taste).
- Cold-open evidence: an `[intro]` caption cue sits after the question in V017 ¶2. Whether other videos have an intro sting can't be established from captions alone.
- In every derived Short checked in batch 2 (V033, V034, V035, V052, V053, V055, V056), the cut follows a structural seam or a condensed full arc. V034 lifts only the riddle (V017 ¶9–10), and V035 only the advocacy segment (V020 ¶23–28).

## Provisional batch-3 observations (V021–V030; 8 long + the first 2 Shorts; NOT generalised)

- The attributed-question opening holds in 26 of the 28 long videos so far (exceptions: V019, and **V024**, which opens differently): it calls itself the most-asked What If question and says other answers already covered it. The two Shorts (V028, V029) have **no attribution line**, because they are verbatim excerpts that start after V002's asker line.
- **V028 and V029 add no words of their own.** Each is 100% contained in V002 (¶5–14 and ¶21–34), and together they split V002 at its pivot. This is the first direct evidence that Shorts here can be pure excerpts; later Shorts must be checked for new wording.
- New hook devices: a spoiler teaser then rewind (V021), a planted absurd promise paid about 95% later with an explicit callback (V023), a meta-contrarian admission of competing coverage (V024), a literal idiom (V025), reversing the asker's own ranking (V026), a retracted apocalypse teaser that returns (V027), and a teased *unit* of the answer (V030).
- New structures: a satirical benefits list (V024), an iterative "more realistic" recomputation (V022), region then city tours (V023), and a P.S. that flips one assumption (V030).
- **Bureaucratic anticlimax as a comic device** recurs: building codes worse than death (V025) and international committees and treaties as bookends (V027).
- Loose end: V030 leaves the asker's eclipse sub-question essentially unanswered.
- **Short cuts again follow structural seams**, and V023 is cut into four (method, continents, cities, coda). Several Shorts drop the long version's comic frame and keep the physics chain (V073 drops V027's committee bookends; V072 drops V025's building-code joke; V076 drops V026's Boston anecdote).
- Ending types added: a consolation button (V021), a statistical reversal (V022), a delayed pop-culture payoff (V023), a one-line reveal of the obvious (V024), a callback (V025, V027), an open trailing tease (V026), a self-aware anti-doom wink (V029), and a P.S. (V030).

## Provisional batch-4 observations (V031–V040; 2 long + 8 Shorts; NOT generalised)

- **No Short in this batch adds new content.** V031, V032, V033 and V035 are word-exact contiguous excerpts (word counts identical to the parent span: V010 ¶4–6, V007 ¶15–28, V011 ¶30–32, V020 ¶23–28). V034 and V040 are **trimmed** excerpts (one linking sentence cut from V017 ¶9; V001 ¶1, ¶9, ¶11–14 minus the asker line, the desk joke and two desk sentences). V037 and V038 are **abridgements** of V003, made by deleting sentences, with no new vocabulary beyond caption spelling.
- **Abridgement can break the logic** (Obs., High). V037 drops V003's straightaway step, so its 4 G time falls from about 2 h to about 1 h 45 with no stated reason. V038 drops V003's "850 tracks" multiplier, so its LHC figures (2.7 ms per 500 miles vs. about 2 s per Daytona 500) contradict each other.
- **What gets excerpted.** A parent's detour (V031), its provisional answer *without* the overriding twist (V033), a self-contained riddle (V034), its persuasive coda (V035), and its obstacle half with the solution half held back (V040). A Short can therefore state a weaker conclusion than its parent (V033).
- **Series mechanics.** V037→V038 is a two-part split by constraint (survive vs. not), and V038 opens with a two-sentence recap bridge. V040 ends on "That's no good."; V041 continues it (confirmed in batch 5).
- **Long-form additions.** V036: a two-path warning hook ("gruesome, unless…") with both halves paid and an explicit "I told you" callback, a staged correction gag, and a term-redefinition ending. V039: a serial superlative ("most destructive… to date"), the first named expert quoted (twice: once saying "we don't know", once giving the verdict), an announced deferral (GR) that rescues a dead end, and a **deliberate mid-word cut-off ending** (identical in V081).
- **The attributed-question opening** now holds in 28 of the 30 long videos (V036 and V039 conform). No Short so far keeps an attribution line.

## Provisional batch-5 observations (V041–V050; 3 long + 7 Shorts; NOT generalised)

- **All seven Shorts are abridgements made by deletion.** A word-level diff against each parent finds no inserted or changed words in V041, V044 and V050 (V043 has one caption typo), and only six new words in total elsewhere: V046 "that", a one-word "would" join and "light" → "flash"; V047 "either way, you'd" → "basically we'd"; V049 an inserted "do". Across batches 4–5, **no Short adds new content.**
- **Abridgement gaps recur, milder than in batch 4** (Obs., High). V041 keeps the *required* rotation rate but cuts Hubble's *actual* rate, so "too slow" is unquantified. V043 cuts the "you'd be fine if you were the only one with a bunker" setup of its reversal. V044 cuts the spray-mixing step, leaving "the subsequent turbulent mixing" without an antecedent. V047's "you can also see" refers to footage whose introduction was cut. V049's "As it was" loses its counterfactual. V050's "As discussed elsewhere" loses its referent. One deletion is a deliberate repair: V044 drops "Back" from "Back at the equator".
- **Split-parent pairs.** V040/V041 (V001: problems, then the fix) and V043/V044 (V004: people, then oceans and the day) join V037/V038. Both new pairs repeat the same opening question in part two instead of V038's recap bridge. The paired titles differ (V043 "to the population" vs. V044 "to the Earth").
- **Parents' comic buttons are often cut.** V044 drops "Thank you, Moon", V046 the hit-by-pitch rule, V047 the neighbourhood lasers, V049 the gunshot punchline. V041 and V050 keep the parent's final lines.
- **Release cadence (dates only).** From V036 on, uploads are weekly in a repeating long, Short, Short pattern. The Shorts recycle the earliest long videos roughly in catalogue order (V003, V001, V004, V005, V006, V008, V009).
- **Long-form additions.** V042: a moral-disclaimer hook and the first explicit double answer (the literal reading, then "what Quinn was imagining"). V045: definition-first rules with a non-example gag, and the first answer that rejects the title's own method (drive north, not west), backed by the narrator's own route search. V048: a suspicious-asker hook with a callback ending, and a riddle-style answer ("twilight, or moonlight").
- **The attributed-question opening** holds in 31 of the 33 long videos. None of the 17 Shorts so far keeps an attribution line.

## Limitations (running list for D6)

- No timestamps, so the "first 30 s" is analysed as opening beats. FR-16C-06 is not evaluable.
- No retention, CTR or watch-time data. Every audience effect is labelled Speculative.
- Auto-captions may mis-transcribe words and numbers (for example "kilm" and "hatron" in V003, and "6 paws" for 6 PW in V018, garbled unit names in V030 w684–720, and V045's place names, "dayight" and "nancond").
- Several scripts reference on-screen visuals the text doesn't describe (V012 maps, V013 "this many", V014 phase diagram, V016 left/right glasses, V022 path maps, V023 climate maps, V026's closing tease, V027's cited PDF). Those beats can't be fully assessed from text.
- Several Shorts' payoffs are on screen only (V033's deictic "this", V040 ¶5 "looks like this", V047's "you can also see"); V039's cut-off ending depends on delivery.
- Thumbnails were not reviewed, so alignment is judged from the title only.
- Scientific claims inside the scripts are not fact-checked; specific numbers are noted, not verified.
- The audits paraphrase and cite locators instead of quoting, to avoid reproducing the copyrighted scripts.
- The two newest videos (`9VG0yqq_PHM`, `X97DDWvxaqQ`) have no transcript and are outside the 83.
