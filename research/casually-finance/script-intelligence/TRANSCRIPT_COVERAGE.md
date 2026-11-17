# Transcript coverage — Casually Finance (`@CasuallyFinance`, channel `UCrNfRFWnLC3tCy1TnyhVQ7g`)

> **UPDATE 2026-11-09 — supersedes the "16 of 206" figures below.** A local Whisper `base` run (fp16 off, CPU, word timestamps) produced 199 more transcripts from the verified local media (206/206 media matched by ID or title plus duration, 0 duration mismatches). Union with the 16 transcripts below, with 9 videos in both: **206 of 206 catalog videos have text** (33 long, 173 Shorts). All are `ASR_UNCERTIFIED`; the 9 overlapping videos were re-run with the same model, so they are not independent evidence. Whisper `base` mishears proper nouns. QC (empty text, time coverage, repeat loops, words per minute): 0 flagged. Data and checksums: `../transcripts_asr_base_20261109/`; per-video lookup: `../INDEX.csv`. The tables and Shorts findings below still describe only the original 16 and have not been re-derived.


Research date: 2026-10-14 (Asia/Karachi). Status: **TRANSCRIPT DATA INCOMPLETE FOR THE FULL CATALOG (16 of 206)**. Structural findings about Shorts rest on 6 transcripts.

## Provenance

- Canonical checkout: `/Users/ghilmankhan/workprojects/youtube-intelligence-os`, `main` @ `08e719264e31ecd82de24f8eeb8f065c08359fe5`, single worktree. On `main`, `data/raw/forensic-analysis/casually-finance/` is an empty directory skeleton.
- The Casually Finance corpus lives on the unmerged branches `origin/codex/casually-finance-forensic-research` @ `043b85bf58f84fb6a1c8981d54e3b233faa6a928` and its superset `origin/research/casually-finance-success-playbook` @ `fb1e56d03e5ad53086c74247cd2972b262d09b78`. Files were read with `git archive fb1e56d <paths>` into a session scratch folder. Nothing was checked out, no worktree was created, and no branch was modified.
- Source root: `data/extracted/forensic-analysis/casually-finance/2026-10-12/` (paths below are relative to it unless stated). Read any file with `git show fb1e56d:data/extracted/forensic-analysis/casually-finance/2026-10-12/<path>`.
- Excluded: `data/raw/competitors/DS-000030/.../transcripts/` (122 files). These belong to **Senior Health Hub**, not Casually Finance.

## Exact counts

| Measure | Count | Evidence |
|---|---:|---|
| Video identities in the saved snapshot (`20261011T182811Z`, collected 2026-10-11) | **206** (0 duplicates) | `01_CHANNEL_METADATA/metadata-coverage.json` |
| Long-form / Shorts | **33 / 173** | same; tabs and uploads playlist reconcile |
| Live check 2026-10-14 | **207** videos, 414K subscribers (snapshot: 412K) | youtube.com/@CasuallyFinance header |
| New since snapshot | 1 long-form: `9eBM5IF_bco` "The Money Squeeze Is Choking the World Economy" (2026-10-13 09:00 PT, 997 s, 94,090 views at check). No new Shorts after 2026-10-10 | watch page `ytInitialPlayerResponse` |
| **Full usable transcripts** | **16** (10 long-form, 6 Shorts) | `02_VIDEO_FORENSICS/<id>/TRANSCRIPT.csv`, `SENTENCES.csv` |
| Partial transcripts | **0** (each of the 16 spans its full narration; the last sentence ends less than 10 s before the metadata duration; the remaining tail is end card) | `SENTENCES.csv` last `end_sec` vs `duration_sec` |
| YouTube auto-generated or uploaded captions in the dataset | **0**. The snapshot reports `caption_availability = NOT_EXPOSED` for all 206 (player UNPLAYABLE) | `all-videos-metadata.csv` |
| Transcript type | Local **openai-whisper base** ASR with word timestamps (not human-verified, no speaker labels) | `02_VIDEO_FORENSICS/<id>/SOURCE.json` |
| **Missing transcripts** | **190 of 206** (23 long-form, 167 Shorts); **191 of 207** including the new long-form | — |
| …of which selected for forensics but media missing | 2 Shorts: `turJ6VMfUjI`, `Qof71Ef-3EU` (`BLOCKED_SOURCE_MISSING`) | `07_VALIDATION/MISSING_SHORTS_LOCAL_SEARCH.json` |
| Duplicated transcript files | 15 byte-identical pairs: `data/raw/forensic-analysis/casually-finance/forensic-research/02_VIDEO_FORENSICS/<id>/TRANSCRIPT.csv` = extracted copy (`cmp`, 15/15 identical; `-X6YzlY_8tM` exists only in the extracted copy). Plus derived `_work/0ll9rEtoRrs/transcript_readable.txt` and `whisper.json`. These are the **same evidence**, not corroboration | `cmp` run 2026-10-14 |
| Cross-video narration duplication | **5 of 6 Short transcripts are re-edits of long-form narration** (71–94% of each Short's 8-grams appear verbatim in the long-form). See SCRIPT_DNA §D | 8-gram matching over `TRANSCRIPT.csv` |

Coverage = 16/206 = **7.8%** of the catalog. For Shorts it is 6/173 = **3.5%**, and all six are from 2026-06-01 or later.

## The 16 transcripts, linked to Video_ID, title and date

ASR words = Whisper tokens (numerals count as one token). Low-conf = share of words with `asr_probability < 0.5`.

| Video_ID | Format | Published (PT) | Dur s | Title | ASR words | Low-conf | Narration source |
|---|---|---|---:|---|---:|---:|---|
| o3FQcd91MIs | LONG | 2025-07-28 | 278 | Why The Dumbest Investors Win (it's not why you think) | 777 | 2.1% | original |
| dlBhLhn8lL0 | LONG | 2025-08-11 | 407 | MicroStrategy: The Crypto Scam Hiding in Plain Sight | 1,031 | 2.2% | original |
| kwMHrTFCWUE | LONG | 2025-09-08 | 374 | Every Type of Investor Explained in 6 Minutes | 929 | 1.9% | original |
| 5umJ63d3rzQ | LONG | 2026-03-10 | 753 | Brace For Impact. | 2,302 | 2.0% | original |
| -X6YzlY_8tM | LONG | 2026-05-21 | 892 | The SpaceX IPO... It's Worse Than You Think | 2,754 | 2.0% | original |
| 0ll9rEtoRrs | LONG | 2026-09-01 | 1,012 | The World's Safest Market Is Breaking | 3,284 | 1.9% | original |
| DgbHW0IqHrI | LONG | 2026-09-16 | 996 | America Is Walking Into Something It Can't Stop | 3,189 | 2.3% | original |
| xtqbRt94TTw | LONG | 2026-09-22 | 828 | To Save the Economy... We're About to Break It | 2,674 | 2.1% | original |
| Uumnx2Fo6cE | LONG | 2026-09-29 | 921 | The New American Housing Crisis Has Landed | 3,030 | 1.7% | original |
| roe3SgezmmU | LONG | 2026-10-04 | 1,043 | The Stock Market Is Being Used as a Dumping Ground | 3,342 | 2.0% | original |
| JsK53moCyZA | SHORT | 2026-06-01 | 43 | The SpaceX IPO Nobody Can (Actually) Explain... | 133 | 0.8% | = -X6YzlY_8tM 0–43 s (94% of 8-grams) |
| rSa2aziEsAI | SHORT | 2026-08-26 | 61 | Why Japan's Economy Is Awful | 213 | 1.4% | **no overlap** with any transcribed long-form |
| 6S3PzAUFnXQ | SHORT | 2026-10-02 | 69 | America's Debt Hasn't Broken... Yet | 229 | 2.2% | = DgbHW0IqHrI 817–913 s (+1 line from 60 s) (79%) |
| PxgCsLSf-w4 | SHORT | 2026-10-05 | 65 | Somebody Is Quietly Repricing America | 205 | 2.4% | = DgbHW0IqHrI 101–145 s + 0–20 s, re-ordered (86%) |
| YGC3ao005as | SHORT | 2026-10-07 | 63 | We're Fighting A Battle Against the Market | 197 | 2.0% | = DgbHW0IqHrI 141–283 s (71%) |
| 2EZzwupIa80 | SHORT | 2026-10-10 | 75 | Nothing Forces the Government to Fix The $40 Trillion Debt | 238 | 2.9% | = DgbHW0IqHrI 210–312 s, re-ordered (84%) |

Missing but selected: `turJ6VMfUjI` "Why You (Mathematically) Need Inflation" (2026-08-02, 63 s) and `Qof71Ef-3EU` "The Cheap Money Era Is Coming to an End" (2026-09-08, 68 s). These are the channel's two highest-ratio Shorts. Their scripts are **unknown**; only their descriptions are available.

## Transcript quality issues

- Whisper-base mis-hearings of proper nouns: "Druck and Miller" (Druckenmiller), "Besent/Besant" (Bessent), "Lanar" (Lennar), "Thropic" (Anthropic), "Hendrick Bessambinder" (Bessembinder), "M&M wrapped about his mom's spaghetti" (an Eminem lyric reference). Numbers render with spacing artefacts ("$1 .75", "5 .3%").
- All numbers and quotes are `ASR_UNVERIFIED` unless the existing claim register (`07_VALIDATION/FINANCE_CLAIM_VERIFICATION.csv`, 287 groups) verified them. Profanity renders inconsistently between the SpaceX long-form and Short.
- Sentence segmentation is ASR-derived. Words-per-minute measures text span, not audible articulation.
- No listening sign-off exists (inherited limitation, `EVIDENCE_AND_LIMITATIONS.md` on the playbook branch).

## Descriptions as a labelled proxy (not transcripts)

All 206 records carry a description (Shorts median 82 words). Shorts descriptions usually restate the core claim in 2–5 sentences. In 4 of 6 transcribed Shorts, the description's first line paraphrases the spoken hook: `2EZzwupIa80`, `rSa2aziEsAI`, `6S3PzAUFnXQ`, and `JsK53moCyZA` (whose first line repeats its second spoken sentence). The other two (`PxgCsLSf-w4`, `YGC3ao005as`) use a different, more abstract line. SCRIPT_DNA and TITLE_DNA use descriptions **only** as `DESCRIPTION_PROXY` evidence of topic and opening claim. No script was reconstructed from a title or description.

## Not done (by instruction)

No paid scraping, no media download, no caption download for the new long-form (its player reports a caption track, which was not retrieved), no re-run of visual/motion forensics, and no re-validation of the 287-claim audit.
