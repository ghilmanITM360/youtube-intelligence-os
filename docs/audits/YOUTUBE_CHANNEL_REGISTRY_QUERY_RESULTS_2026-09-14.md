# YouTube Channel Registry Query Results

Run date: 2026-09-14

Database: `data/catalog/youtube_channel_registry.db` (generated, Git-ignored)

Query catalog: `data/catalog/channel_registry/example_queries.sql`

## 1. Target channels with complete extraction

26 rows: Brimm.; Bro Pump; CIPHER UNIT; Crayon Capital; Dark Ledger; Explain In Paint; Genius History; Hypothetically; Ink Explainer; Lost Legacy; Luco; Mack; Maximus; Money Life POV; My Chaotic Stories; Oddlyhuman; Past Tense; Shaami Finance; Sonny Finance; Stickly; The Life Outline; Unknown Frequencies; Zenn; Zoozle; ago.; inkly.

Eight other original targets are `COMPLETE_WITH_LIMITATIONS`; they are not collapsed into this result.

## 2. Target channels awaiting extraction

29 rows: Alicia Invests; Bernard; Brick Body; Brofessor Stein; Casual Finance; Casually Explained; Chat History; Chill Dude Explains; David Explains Money; Fasted Fred; Finance Simplified; Ivan Invests; Mark - Retired at 55; Max Invests; Millionaire Problems; Neu; Nostalgic Wheels; Overhead; Parenting Hacks; Parentitude; quack doc; Rick Finance; The Career Machine; The Expensive Part; The Wise Future; Tom - Lazy Dividend Investor; Tom - Lazy Investor; Tom Talks Money; Wealth Logic.

Ten are original targets and 19 are later additions. All identities are verified; extraction has not started.

## 3. Standard-package channels

39 rows: Apesthetic; Bob Invests; Brimm.; Bro Pump; CIPHER UNIT; Carl Invests; Crayon Capital; Dark Ledger; Decode Your Heart - Dr. Rehan; Doctor Thomas; Dr. Ares Senior; Dr. Okoro; Explain In Paint; Genius History; Hypothetically; Ink Explainer; Just Some Guy Stories; Lost Legacy; Lucas Grant; Luco; Mack; Maximus; Money Life POV; My Chaotic Stories; Nick Invests; Oddlyhuman; Past Tense; Primate Economics; Shaami Finance; Sonny Finance; Stickly; The Life Outline; Tp Dossier; Unknown Frequencies; Well.; Zenn; Zoozle; ago.; inkly.

Every row has one exact package workbook and one transcript ZIP path.

## 4. Historical-format channels

Five rows:

- Dr. Aliza Wright | Advice: `DS-000006`
- Dr. Elias Senior Health: `DS-000019`
- Matty Invests: `DS-000001`
- Mr. Finance: `DS-000001`
- xkcd's What If?: `DS-000012`, `DS-000013`, `DS-000014`, `DS-000015`, `DS-000017`

These are not reported as standard packages.

## 5. Channels with real transcripts

43 channels. Registry total: 2,015 real transcripts.

## 6. Channels with placeholders

- Doctor Thomas: one explicit no-YouTube-subtitle placeholder.
- Lucas Grant: 10 members-only/captions-unavailable placeholders.
- Matty Invests: one explicit unavailable-caption placeholder.

Total: 12.

## 7. Channels with missing descriptions

- Apesthetic: 1.
- Doctor Thomas: 1.
- Primate Economics: 13.

Total: 15.

## 8. Channels with thumbnail URLs only

38 rows, exactly the standard-package channels. Each package video has a thumbnail URL, but no downloaded thumbnail evidence is registered in the standard package.

## 9. Channels with downloaded thumbnail evidence

- Dr. Aliza Wright | Advice: 32.
- Dr. Elias Senior Health: 29.
- xkcd's What If?: 83.

## 10. Channels with forensic video evidence

One row: xkcd's What If? (`UC6IxnFzHofFJ5X2PycSMsww`), 107 measured keyframes, three unique canonical source videos, 107 timestamped visual-state observations. Evidence: `data/intelligence/channels/CH-000004/editing-visual-intelligence-pilot-2026-09-11.json`.

## 11. Screenshot-only unmapped subjects

Five rows: Dr. Adewale; Dr. Waterling; The Senior Health Podcast; Senior Health Hub; The Health Educator. All remain separate from canonical channels. Doctor Thomas is no longer listed here: it is now a canonical standard-package channel (DS-000029).

## 12. Generated intelligence by capability

| Capability | Generated rows |
|---|---:|
| Topic Opportunity | 5 |
| Packaging | 5 |
| Hook | 5 |
| Script | 5 |
| Editing/Visual | 1 |
| Unified Orchestration | 5 |
| Channel Strategy | 4 |
| First-party Analytics | 0 |

Generated rows include evidence paths. Packaging is partial/title-only for Matty Invests and Mr. Finance. Editing/Visual is partial for xkcd because evidence covers three videos. Channel Strategy retains limited cross-niche calibration.

## 13. Input exists but output is not generated

The 38 standard-package channels each have input-ready rows for Topic Opportunity, Packaging, Hook, and Script: 38 rows per capability, 152 rows total. `generated_artifact_available` remains false.

## 14. First-party Analytics status

72 channels: `SCHEMA_READY_NO_DATA`. Zero channels: `INGESTED`. Public scraped metrics are not first-party Analytics.

## 15. Data gaps for one channel

Using Lucas Grant as the parameterized example returns 10 video-level unavailable public-view fields, each with `Value unavailable in stored source evidence.` and a canonical video URL. Transcript placeholders are separately represented in `transcripts`, not conflated with metric gaps.

## 16. Transcript search

FTS5 runtime support: enabled. Phrase `money`, first five video IDs:

- `KmQ7koHwuqY` — The Economics of Owning a Ski Resort
- `Nq0FwNlv8_c` — The Economics of Owning an Accounting Firm
- `ev2HYq2HdnA` — The Economics of Owning a Laundromat
- `l0sy1sZX8Ig` — The Economics of Owning a Cement Plant
- `biobbpiQFsc` — Why Less is More in Retirement

The standard-SQL `LIKE` fallback returned the same first five IDs.

## 17. Original versus later-added progress

| Group | Extraction status | Channels |
|---|---|---:|
| Original 44 | `COMPLETE` | 26 |
| Original 44 | `COMPLETE_WITH_LIMITATIONS` | 8 |
| Original 44 | `NOT_EXTRACTED` | 10 |
| Later-added 19 | `NOT_EXTRACTED` | 19 |

## Alias demonstration

Nick Invests (`UCXzNNA2ngRpRiWvyA7eGd6w`) returns submitted rows 13 and 18. Row 18 is marked as an exact duplicate of row 13; both original URLs remain preserved.
