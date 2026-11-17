# What If? 83-script reverse-engineering study: status and continuation

**Status (2026-11-17): Phase 1 is done. Phase 2 is done: 83/83 audited (V001–V083). The cross-video report (Phase 5) and the playbook (Phase 6) have not started; they are unblocked but need an explicit request.**

| Deliverable | File | State |
|---|---|---|
| Method, framework record, exceptions | [00_METHOD.md](00_METHOD.md) | done |
| D1 Dataset inventory | [01_INVENTORY.md](01_INVENTORY.md) (+ `inventory.json`) | done: 83 readable, 0 exact duplicates, no timestamps |
| D2 Individual audits | `audits/V###.md` | V001–V083 (complete) |
| D3 Comparison matrix | [03_COMPARISON_MATRIX.md](03_COMPARISON_MATRIX.md) (from `matrix.jsonl`) | 83 rows |
| D4 Cross-video report | — | not started (it needs all 83) |
| D5 Master playbook | — | not started |
| D6 Limitations | — | started below; to be finalised with D4 |
| Coverage ledger | `coverage_ledger.json` | synced by `render.py` |

## Continue

1. `python3 render.py` prints the next unprocessed VID.
2. Read that batch's transcripts in full. Shorts that are cut from a long video (see the inventory's Overlap column) must still be read in full and get their own audit. Map which parent ¶ each one reuses with `python3 reuse.py PARENT SHORT` (6-gram overlap above 50% per ¶). In an audit, write another video's paragraph as `V002 ¶5`; `locate.py check` validates it against that video. The same holds for word ranges (`V003 w331–421`). *Fix (batch 4):* until then the check matched only ASCII-hyphen ranges, and every audit uses en dashes, so no word range had ever been checked. It now accepts both and checks single words (`w684`). All V001–V030 ranges pass the stricter check.
3. Write `audits/V###.md` in the same headings as V001, and append one row to `matrix.jsonl`.
4. Run `python3 render.py && python3 locate.py check`. The check must print `ok`.
5. Batches: ~~V011–V020~~, ~~V021–V030~~, ~~V031–V040~~, ~~V041–V050~~, ~~V051–V060~~, ~~V061–V070~~, ~~V071–V083~~ (all done). Next is D4 (the cross-video report), then D5 (the playbook); neither is started. Write a derivation list as `V012 ¶1, V012 ¶3–13, …` (repeat the parent's VID before every ¶): `locate.py check` attributes a bare `¶N` to the audited video itself.

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

## Provisional batch-6 observations (V051–V060; 4 long + 6 Shorts; NOT generalised)

- **Correction to batches 4–5.** The note "none of the 17 Shorts keeps an attribution line" no longer holds. **V056 and V058 keep it in ¶1** because their parents' attributed paragraph survived the cut (V015 ¶1, V021 ¶1). V052, V053 and V055 cut it, and V059 starts after it. So 2 of 23 Shorts keep an attribution line. The attributed-question opening holds in 35 of the 37 long videos (exceptions: V019, V024).
- **Still no Short adds new content (23 of 23).** V052, V053, V055, V056 and V058 are abridgements by deletion. V059 is a word-exact contiguous excerpt (V021 ¶6–17, 273 words). The only non-deletions are one relocated 8-word clause (V053 ¶2, moved from the end of V014 ¶1), one moved word (V056 ¶1) and one caption variant (V058 "spacecrafts").
- **Cut seams, again (Obs., High).** V052's "Cool." lost its aircraft-carrier setup; its Dutch gag keeps the jokes but loses the setup (V012 ¶14) and the closing line (V012 ¶38). V053's "Mars isn't that cold" lost its comparison. V056's "dim flash in your eyes" is the only trace of the cut eye section, and its question lost the premise that its answer reverses. V055 shows a **deliberate repair**: the connector "Fortunately, we don't need to –" was deleted so ¶5 reads cleanly.
- **A split pair with a cross-dependency.** V058 and V059 split V021 at its turn (V021 ¶18–19): V058 takes the stacking ladder (V021 ¶20–35, ¶38) and V059 the four problems (V021 ¶6–17). **V058 ¶8 says the tower will not collapse "like jello"; jello is introduced only in V059, published a week later.** The Short order reverses the parent's order.
- **First title/script mismatch.** V059's title promises an elevator count for a billion-story building. The script gives no count and never mentions "billion-story"; elevators are one of four listed problems. It also ends mid-list, with no closing beat, because the excerpt stops before the parent's turn.
- **Paired sequels in both formats.** V012 → V014 (long) is mirrored by V052 → V053 (Short): V052's rover joke is V053's premise, and V053 opens with a one-sentence recap of "the previous What If". V053 is the first Short whose opening is a recap bridge.
- **Long-form additions.** V051: a multiply-then-compare estimate with an explicit yardstick (a novel per half-minute powers a laptop), a verdict leaked in the first 40 words, and a pun ending on "novel". V054: no digits except one figure, three proxies ranked by similarity, a "walking ghost" refrain (¶16, ¶23) and a dark silver-lining ending on genetic surveillance. V057: an early yes (2% in), one unit ruler (thrust-to-weight), a multiplication ladder ending in a ceiling, a first answer at about 69% (w699), a second act ("Can we do better?") built on real autocannon, a correction gag used twice (¶25, ¶31) and an ending that is one long conditional. V060: a binary question answered by a rule, a narrator riposte ("did you bring a coat?") that is also the variable in the answer, an elapsed-time ladder, and a post-mortem coda that is about 15% of the script, closed by "So, there's that."
- **New ending types.** A pun button (V051), a dark silver lining (V054), a conditional-fantasy ending (V057), a cosmic coda followed by a shrug (V060).
- **Recurring bits.** The squirrel as a mass unit (V051 w175–219, V057 ¶20). The staged correction gag (V036, V057 ×2). The Dutch gag (V012, V052).
- **Internal-arithmetic checks (my own, not fact-checks).** V051, V055, V057, V058 and V060 reproduce their own stated figures, with two rounding notes in V055 (100 ÷ 15 is about 6.7; 150,000 × one cent is $1,500 against "about a thousand") and one in V057 (¶20's net lift uses the bullets-only thrust, not ¶15's "up to 30% higher").
- **Release cadence (dates only).** The weekly long, Short, Short pattern continues (V054–V056, V057–V059), with gaps in the corpus at 2025-12-09 and 2025-12-30 to 2026-01-13. Whether videos exist outside the 83 is unknown. The Shorts keep moving forward through the catalogue (V012, V014, V013, V015, V021).

## Provisional batch-7 observations (V061–V070; 2 long + 8 Shorts; NOT generalised)

- **Attribution, updated.** V062 also keeps its attribution line (N. Murdoch), so **3 of 31 Shorts** keep one (V056, V058, V062). The attributed-question opening holds in 37 of the 39 long videos (V063 and V068 conform; exceptions V019, V024).
- **Qualifier on "no Short adds new content".** It still holds for substantive content (31 of 31), but **four Shorts rewrite the question line**: V066, V067, V069 and V070 all delete the asker and V023 ¶1's "spread out the same way as now, but" and add a retargeting phrase: V066 "INSTANTLY" (a V023 ¶64 word), V067 "Earth's climate", V070 "world's largest cities" (lifted from V023 ¶49), and **V069 "your country"**, the first words with no counterpart anywhere in the parent ("country" is not in V023). V070 also drops the opener "Now," as a seam repair.
- **Two more split families, both published in reverse order.** V022 splits into V062 (¶1–12, the star) and V061 (¶13–18, the planet); V061 came out a week *earlier* and says planet paths are "more complex" than star paths it does not contain. V023 splits four ways: coda V066 (04-21), method V067 (04-28), continents V069 (05-12), cities V070 (05-19). **No Short contains V023 ¶3 (the tilt clarification), ¶6, ¶27 or ¶62–64**, so none defines what "rotated by 90 degrees" means.
- **Cut parent turns, again.** V061 drops the parent's rebuttal (V022 ¶19–20) and ends on a jab; V062 ends on a method caveat (V022 ¶12) with no button; V064 drops the parent's meta-contrarian opening (V024 ¶2–3) and four of nine benefits; V066 drops V023's explicit callback (¶62) but keeps the plant and payoff.
- **Title/script gaps.** V069's title promises "your country"; the script is continental. V067's promised answers (deserts, beaches, tornadoes) are on screen only. These follow V059's mismatch in batch 6.
- **Independent Short.** V065 is an argument, not a calculation: textbook answer, "sort of true", a contrarian thesis ("air is blue"), a concession, a statue analogy and an echo ending. It has no figures and no attribution, and it is among the five shortest scripts (167 words).
- **Long-form additions.** V063 mirrors V060 ("the reverse of the video…", and ¶3's "the previous video"), reuses its rate, turns at 41% with "But wait a minute", climbs a power ladder (about 100 kW to over 10 MW, which reproduces on my arithmetic), adds protective assumptions until the question is "fantasy", and **ends without stating the answer**. V068 runs myth correction → coin-and-21-dice decay analogy → picowatt scale shock → pivot to the banana's chemical energy → a rotting, exploding pile → "the rest of the banana is the real threat". Its decay figures reproduce, but **its house-power figure needs checking against the audio**: on its own "couple of picowatts", 300 quadrillion bananas give roughly 0.6–0.9 MW, about a thousand times a typical house's draw (my assumption).
- **New ending types.** A methodological caveat (V062), a rule collapse with the answer unsaid (V063), a single reversal line after a satirical list (V064), a normative recommendation (V065), a movie-parody button (V066), an inverted-risk button (V068).
- **Release cadence (dates only).** Shorts now dominate: V061–V062 (03-10, 03-17), long V063 (03-24), Shorts V064–V067 (04-02 to 04-28), long V068 (05-05), Shorts V069–V070. Longs came out at 3-week and 6-week intervals (V060 03-03, V063 03-24, V068 05-05). Shorts now draw on V022, V024 and V023.

## Provisional batch-8 observations (V071–V083; 4 long + 9 Shorts; NOT generalised)

- **Final counts.** 43 long and 40 Shorts. The attributed-question opening holds in **41 of 43 long videos** (exceptions V019, V024). **4 of 40 Shorts** keep a "This question comes from…" line (V056, V058, V062, V076). V080 names five askers inline ("Shelby asks…").
- **Independent Shorts: only two** (V065, V080). The other 38 Shorts are cut-downs of a long video, so any per-video count in D4 must be reported per content family as well.
- **Parents with auto-captions blur the diff.** Five Shorts in this batch (V072, V075, V078, V079, V082) derive from auto-caption parents (V025, V030, V042, V045). Their word-level diffs mix real edits with caption repair ("Longerbian" becomes "Longyearbyen", "pron" becomes "prion"), so a few added words (V072 "of", "worth", "dollars", "now"; V075 "and the Sun,"; V082 "PyEphem and", "I've") cannot be called edits. The count "no Short adds new substantive content" (40 of 40, with V065 and V080 independent) still holds.
- **A two-reading split with shared opener.** V042 yields V078 (the calorie reading) and V079 (the half-eats-half reading). Both open on the same three-sentence disclaimer, and V079's question is rebuilt from V042's own words. V078 edits the asker's name out ("in Quinn's scenario, we would" becomes ", we'd").
- **Repairs and non-repairs.** V081 deletes V039's string-theorist section **and** its follow-up joke ("Dr. Keeler's diagnosis"), so the cut is clean. V070 (batch 7) and V082 show opposite results: V082 leaves a stranded "or" at the start of ¶2 where "For the purpose" lost its lead-in. V072 keeps the building-code gag but drops its set-up.
- **Cut payoffs and flat endings.** V073 drops the committee bookends and ends on a consequence with no button. V075 asks the eclipse question in ¶1 and answers it only in the P.S., after cutting the parent's 317-word colder-Earth section. V076 cuts the parent's reversal and its payoff.
- **Title/script mismatch, again.** V081's title says the Moon is made of protons; the script (and V039's title) say electrons. V076's title coins a "microwave as a snowblower" hybrid that the script never states. V082's title names the method (drive towards the sunset) that its answer rejects. V072's title has a grammar slip.
- **Odd formats.** V080 is a question montage with five loops opened and none closed. V065 (batch 7) and V080 are the two independent Shorts. V079 has the only emoji in a title.
- **Long-form additions.** V071: a premise-flipping fact, an imagined objection, a self-gathered tally and a variant ladder whose times **reproduce from the stated speed and a displacement of about 5.5 kg on my arithmetic**. V074: a five-line "technically" correction run and a falsification-joke ending. V077: a one-line gag answer, a joke on not knowing a term, and an angle claim whose "six separations" and "about 20°" disagree on simple geometry (**check the audio**). V083: the second elapsed-time ladder (after V060), a landmark (the Titanic at airliner speed, which reproduces) and an asker-blame ending in the family of V048's.
- **New ending types.** A falsification joke (V074), a P.S. that flips the premise (V075, the parent's own), a plain practical recommendation (V076), a sports-bracket pun (V079), a cut-off sentence (V081, the parent's), a concern question to the last asker (V080), an asker-blame callback (V083).
- **Release cadence (dates only).** Weekly Shorts continue; longs at V071 (05-26), V074 (06-16), V077 (07-07), V083 (08-25): a three-week rhythm in June–July, then a seven-week gap with no long after V077 (07-14 to 08-18 are all Shorts), ending in V083.

## Limitations (running list for D6)

- No timestamps, so the "first 30 s" is analysed as opening beats. FR-16C-06 is not evaluable.
- No retention, CTR or watch-time data. Every audience effect is labelled Speculative.
- Auto-captions may mis-transcribe words and numbers (for example "kilm" and "hatron" in V003, and "6 paws" for 6 PW in V018, garbled unit names in V030 w684–720, and V045's place names, "dayight" and "nancond"; V051's "1.5 mill", "kilogjle" and "What Pulse" hide its units and a site name; V060 w455 has a dropped word, "you you"; V063 and V068 carry non-speech and music tags inside sentences).
- Several scripts reference on-screen visuals the text doesn't describe (V012 maps, V013 "this many", V014 phase diagram, V016 left/right glasses, V022 path maps, V023 climate maps, V026's closing tease, V027's cited PDF, V052 ¶5's maps, V055 ¶2's "this many", and the maps of V061, V062, V066, V067, V069 and V070). Those beats can't be fully assessed from text.
- Several Shorts' payoffs are on screen only (V033's deictic "this", V040 ¶5 "looks like this", V047's "you can also see"); V039's cut-off ending depends on delivery.
- Thumbnails were not reviewed, so alignment is judged from the title only.
- Scientific claims inside the scripts are not fact-checked; specific numbers are noted, not verified.
- The audits paraphrase and cite locators instead of quoting, to avoid reproducing the copyrighted scripts.
- The two newest videos (`9VG0yqq_PHM`, `X97DDWvxaqQ`) have no transcript and are outside the 83.
- Where a Short's parent has auto-captions (V025, V030, V042, V045, and earlier ones), the word-level diff cannot separate a creator's edit from a caption restoration.
- Internal-arithmetic checks in the audits are mine and use a few outside constants (densities, a heliopause distance, household draw); they test the scripts' own consistency, not their facts. Two flagged items (V068's house-power figure, V077's angle) need a check against the audio.
