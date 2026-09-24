# CHANNEL DATA DEEP AUDIT

Audit date: 2026-09-20. Scope: current workspace, read-only. Canonical registry snapshot is 2026-09-14; later DS-000027 raw acquisition is reconciled separately. Raw evidence was not modified.

# 1. Executive Summary

- **77 distinct channel-like references:** 70 verified canonical channels plus 7 screenshot-only unresolved subjects. Unresolved subjects are not counted as canonical channels.
- **70 canonical unique channels:** 64 targets and 6 outside-target historical channels. Registry contains 69; Dr. Ares Senior is verified in later DS-000027 evidence but not yet added to registry.
- **41 channels have meaningful video data; 41 have real transcripts; 29 remain identity-only.**
- **Strongest broad holding:** 35 standard channel packages, 1,601 videos, 1,591 real transcripts, 10 placeholders, 14 missing descriptions. Adding five historical channels and DS-000027 yields 1,939 videos, 1,928 real transcripts, 11 placeholders, 14 missing descriptions.
- **Generated intelligence:** 5 historical channels have topic and hook/script artifacts; 5 have packaging artifacts; 5 unified plans; 4 strategy artifacts; only xkcd’s What If? has forensic editing intelligence. Thirty-five packaged channels are input-ready but have no generated channel-specific intelligence artifacts.
- **Major gaps:** 29 identity-only channels; no real first-party Analytics for any channel; actual image/video evidence for only 3 canonical channels; forensic video for only 1; DS-000027 package/registry integration incomplete; local SQLite file is zero bytes.

# 2. Exact Channel Count

| Measure | Exact count | Basis |
|---|---:|---|
| Total distinct channel references found | 77 | 70 verified IDs + 7 unresolved screenshot subjects |
| Canonical unique channels | 70 | 69 registry IDs + verified DS-000027 ID |
| Duplicate/alias submission rows reconciled | 4 | 67 submitted rows normalized to 63 target identities in registry |
| Target channels | 64 | 63 registry targets + Dr. Ares added target |
| Historical/outside-target channels | 6 | Registry target_group=OUTSIDE_TARGET |
| Identity-only channels | 29 | Registry source_group=IDENTITY_ONLY |
| Channels with extracted standard packages | 35 | Registry package layer |
| Channels with any meaningful video records | 41 | 35 packaged + 5 historical + DS-000027 raw |
| Channels with generated intelligence | 5 | CH-000001 through CH-000005 |
| Channels with real transcripts | 41 | At least one real transcript |
| Channels with actual visual evidence | 3 | Dr. Aliza, Dr. Elias, xkcd; URL strings excluded |
| Channels with forensic video | 1 | xkcd’s What If? only |
| Channels with first-party Analytics | 0 | Schema/import capability exists; no real export ingested |

Count conflict resolved: 2026-09-14 registry reports 69 canonical channels. Current workspace also contains verified DS-000027 Dr. Ares acquisition, created 2026-09-20. This audit therefore reports 70 current canonical identities while preserving registry count and integration gap. Seven named screenshot subjects lack Channel IDs and remain outside canonical count.

# 3. Master Channel Inventory

| # | Canonical Channel | Channel ID | Handle | URL | Dataset IDs | Source Group | Package Status | Videos | Descriptions | Real Transcripts | Transcript Placeholders | Thumbnail Metadata | Downloaded Visuals | Forensic Video | Topic Intelligence | Packaging Intelligence | Hook/Script Intelligence | Editing Intelligence | Strategy Intelligence | First-Party Analytics | Main Storage Paths | Missing Data |
|---:|---|---|---|---|---|---|---|---:|---:|---:|---:|---|---:|---|---|---|---|---|---|---|---|---|
| 1 | Crayon Capital | UCP9RPj_BG0vit2TNM7LuRxA | @Crayon_Capital | https://www.youtube.com/channel/UCP9RPj_BG0vit2TNM7LuRxA | DS-000023 | STANDARD_PACKAGE | STANDARD_PACKAGE | 30 | 30 | 30 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000023; data/extracted/channel-data/DS-000023/packages/crayon-capital | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 2 | Lucas Grant | UCTcOboZIhgrKHMDm-oTlTOg | @LucasGrant-usa | https://www.youtube.com/channel/UCTcOboZIhgrKHMDm-oTlTOg | DS-000022 | STANDARD_PACKAGE | STANDARD_PACKAGE | 95 | 95 | 85 | 10 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000022; data/extracted/channel-data/DS-000022/packages/lucas-grant | 10 real transcripts, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 3 | Well. | UCW4NZzZ-6At6DFrCn7rJ0bQ | @Well.4 | https://www.youtube.com/channel/UCW4NZzZ-6At6DFrCn7rJ0bQ | DS-000022 | STANDARD_PACKAGE | STANDARD_PACKAGE | 32 | 32 | 32 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000022; data/extracted/channel-data/DS-000022/packages/well | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 4 | Brimm. | UC1GwXFBhh1fiLLuZxs8VRXA | @brimm-tv | https://www.youtube.com/channel/UC1GwXFBhh1fiLLuZxs8VRXA | DS-000024 | STANDARD_PACKAGE | STANDARD_PACKAGE | 44 | 44 | 44 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000024; data/extracted/channel-data/DS-000024/packages/brimm | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 5 | Zoozle | UChFs6t9iB1yv0X8fuKtNIvA | @zoozleworld | https://www.youtube.com/channel/UChFs6t9iB1yv0X8fuKtNIvA | DS-000023 | STANDARD_PACKAGE | STANDARD_PACKAGE | 39 | 39 | 39 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000023; data/extracted/channel-data/DS-000023/packages/zoozle | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 6 | Just Some Guy Stories | UCNO35SZS-e3f1hLIDon_mag | @justsomeguystories | https://www.youtube.com/channel/UCNO35SZS-e3f1hLIDon_mag | DS-000022 | STANDARD_PACKAGE | STANDARD_PACKAGE | 13 | 13 | 13 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000022; data/extracted/channel-data/DS-000022/packages/just-some-guy-stories | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 7 | Brofessor Stein | UCZqJKUTmgB-cffFSzL3ENJA | @BrofessorStein | https://www.youtube.com/channel/UCZqJKUTmgB-cffFSzL3ENJA | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 8 | Lost Legacy | UC96yqt8xjtShTpgdoIo0Lqg | @LostLegacy-YT | https://www.youtube.com/channel/UC96yqt8xjtShTpgdoIo0Lqg | DS-000024 | STANDARD_PACKAGE | STANDARD_PACKAGE | 45 | 45 | 45 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000024; data/extracted/channel-data/DS-000024/packages/lost-legacy | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 9 | ago. | UCJqZXjdkolPUgVcf6WBm8VA | @ago-chanell | https://www.youtube.com/channel/UCJqZXjdkolPUgVcf6WBm8VA | DS-000024 | STANDARD_PACKAGE | STANDARD_PACKAGE | 50 | 50 | 50 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000024; data/extracted/channel-data/DS-000024/packages/ago | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 10 | Carl Invests | UCxoC2voi0vPg2hwqgfjdhYw | @carlinvestsUS | https://www.youtube.com/channel/UCxoC2voi0vPg2hwqgfjdhYw | DS-000022 | STANDARD_PACKAGE | STANDARD_PACKAGE | 80 | 80 | 80 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000022; data/extracted/channel-data/DS-000022/packages/carl-invests | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 11 | Hypothetically | UC0L9hD7HMwWU7xuU5HRA6Iw | @HypotheticallyHQ | https://www.youtube.com/channel/UC0L9hD7HMwWU7xuU5HRA6Iw | DS-000024 | STANDARD_PACKAGE | STANDARD_PACKAGE | 39 | 39 | 39 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000024; data/extracted/channel-data/DS-000024/packages/hypothetically | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 12 | Casually Explained | UCr3cBLTYmIK9kY0F_OdFWFQ | @CasuallyExplained | https://www.youtube.com/channel/UCr3cBLTYmIK9kY0F_OdFWFQ | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 13 | Nick Invests | UCXzNNA2ngRpRiWvyA7eGd6w | @nickinvestsUS | https://www.youtube.com/channel/UCXzNNA2ngRpRiWvyA7eGd6w | DS-000022 | STANDARD_PACKAGE | STANDARD_PACKAGE | 363 | 363 | 363 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000022; data/extracted/channel-data/DS-000022/packages/nick-invests | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 14 | Primate Economics | UC14Fb2zWTEZklONPXFbLrTQ | @Primateeconomics | https://www.youtube.com/channel/UC14Fb2zWTEZklONPXFbLrTQ | DS-000020 | STANDARD_PACKAGE | STANDARD_PACKAGE | 28 | 15 | 28 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000020; data/extracted/channel-data/DS-000020/packages/primate-economics | 13 descriptions, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 15 | Apesthetic | UCGnTHU6UMQQlR6cl4CP3jlg | @ApestheticGuide | https://www.youtube.com/channel/UCGnTHU6UMQQlR6cl4CP3jlg | DS-000020 | STANDARD_PACKAGE | STANDARD_PACKAGE | 22 | 21 | 22 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000020; data/extracted/channel-data/DS-000020/packages/apesthetic | 1 descriptions, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 16 | Maximus | UCJgTBuO9fbNvgL_IS8pqtqg | @Pastwithmax | https://www.youtube.com/channel/UCJgTBuO9fbNvgL_IS8pqtqg | DS-000023 | STANDARD_PACKAGE | STANDARD_PACKAGE | 5 | 5 | 5 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000023; data/extracted/channel-data/DS-000023/packages/maximus | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 17 | Bernard | UC_FStSURaDad8-xo6jH1j4Q | @BernardAnimationOfficial | https://www.youtube.com/channel/UC_FStSURaDad8-xo6jH1j4Q | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 18 | The Life Outline | UCeVwhrEnYjCNdaDr47x4dSw | @TheLifeOutline | https://www.youtube.com/channel/UCeVwhrEnYjCNdaDr47x4dSw | DS-000023 | STANDARD_PACKAGE | STANDARD_PACKAGE | 15 | 15 | 15 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000023; data/extracted/channel-data/DS-000023/packages/the-life-outline | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 19 | Max Invests | UCXSpMZ1S5In6aRCyWdM5CAw | @MaxInvests-US | https://www.youtube.com/channel/UCXSpMZ1S5In6aRCyWdM5CAw | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 20 | Fasted Fred | UC91LLjU9cbyLBOjSxWR3cMg | @ItsFastedFred | https://www.youtube.com/channel/UC91LLjU9cbyLBOjSxWR3cMg | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 21 | Brick Body | UCq1V-pmuLDjjTrgFyzxYQ5g | @bricklifts | https://www.youtube.com/channel/UCq1V-pmuLDjjTrgFyzxYQ5g | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 22 | Bro Pump | UCQTcmLiL5_HMUnO1GRwCdjQ | @BropumpYT | https://www.youtube.com/channel/UCQTcmLiL5_HMUnO1GRwCdjQ | DS-000023 | STANDARD_PACKAGE | STANDARD_PACKAGE | 21 | 21 | 21 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000023; data/extracted/channel-data/DS-000023/packages/bro-pump | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 23 | Chat History | UCicVSNyM7PMXEzdoAsTB02w | @ChatHistory | https://www.youtube.com/channel/UCicVSNyM7PMXEzdoAsTB02w | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 24 | Parentitude | UCJ8_5EeAN8fg0JIhxgHKndw | @Parentitude | https://www.youtube.com/channel/UCJ8_5EeAN8fg0JIhxgHKndw | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 25 | Parenting Hacks | UC4eR2RUwoQrYEgbzReQV3HA | @Parentinghacks-x6k | https://www.youtube.com/channel/UC4eR2RUwoQrYEgbzReQV3HA | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 26 | Bob Invests | UCAKBDBaY1dP7OdZkGPiDnug | @bobinvestsUS | https://www.youtube.com/channel/UCAKBDBaY1dP7OdZkGPiDnug | DS-000022 | STANDARD_PACKAGE | STANDARD_PACKAGE | 57 | 57 | 57 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000022; data/extracted/channel-data/DS-000022/packages/bob-invests | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 27 | Sonny Finance | UCFvEZUMNoAVjSoSB8NrV7yw | @Sonny_Finance | https://www.youtube.com/channel/UCFvEZUMNoAVjSoSB8NrV7yw | DS-000020 | STANDARD_PACKAGE | STANDARD_PACKAGE | 39 | 39 | 39 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000020; data/extracted/channel-data/DS-000020/packages/sonny-finance | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 28 | Money Life POV | UCCEwJbv7D1CYzxdKYYOH6AA | @MoneyLifePOV | https://www.youtube.com/channel/UCCEwJbv7D1CYzxdKYYOH6AA | DS-000020 | STANDARD_PACKAGE | STANDARD_PACKAGE | 20 | 20 | 20 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000020; data/extracted/channel-data/DS-000020/packages/money-life-pov | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 29 | My Chaotic Stories | UC9m3w-9L_Bt34x02IQXQ5kg | @mychaoticstories | https://www.youtube.com/channel/UC9m3w-9L_Bt34x02IQXQ5kg | DS-000020 | STANDARD_PACKAGE | STANDARD_PACKAGE | 23 | 23 | 23 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000020; data/extracted/channel-data/DS-000020/packages/my-chaotic-stories | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 30 | inkly | UCcWtWryYdHHiNWfZGSROl1A | @inklyHQ | https://www.youtube.com/channel/UCcWtWryYdHHiNWfZGSROl1A | DS-000021 | STANDARD_PACKAGE | STANDARD_PACKAGE | 28 | 28 | 28 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/inkly | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 31 | Ink Explainer | UCpgrEMx8diLrw7YNQ6r3uUw | @Inkexplainer96 | https://www.youtube.com/channel/UCpgrEMx8diLrw7YNQ6r3uUw | DS-000021 | STANDARD_PACKAGE | STANDARD_PACKAGE | 15 | 15 | 15 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/ink-explainer | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 32 | Dark Ledger | UCDglfjh__GM2RFM1oAL3a6A | @darkledger13 | https://www.youtube.com/channel/UCDglfjh__GM2RFM1oAL3a6A | DS-000021 | STANDARD_PACKAGE | STANDARD_PACKAGE | 38 | 38 | 38 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/dark-ledger | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 33 | Shaami Finance | UC5ZSqmk7PKry99xdiRDrc0A | @ShaamiFinance | https://www.youtube.com/channel/UC5ZSqmk7PKry99xdiRDrc0A | DS-000021 | STANDARD_PACKAGE | STANDARD_PACKAGE | 13 | 13 | 13 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/shaami-finance | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 34 | Oddlyhuman | UCxyQ6jK98CCOsy-gwV8QaFA | @OddlyHuma-n | https://www.youtube.com/channel/UCxyQ6jK98CCOsy-gwV8QaFA | DS-000021 | STANDARD_PACKAGE | STANDARD_PACKAGE | 13 | 13 | 13 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/oddlyhuman | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 35 | Luco | UChGF6aMxELhXOKg2EDDLYNg | @LucoVids | https://www.youtube.com/channel/UChGF6aMxELhXOKg2EDDLYNg | DS-000021 | STANDARD_PACKAGE | STANDARD_PACKAGE | 4 | 4 | 4 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/luco | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 36 | Past Tense | UCS3iXffTKXrhKWGXaPckb8A | @PastTense01 | https://www.youtube.com/channel/UCS3iXffTKXrhKWGXaPckb8A | DS-000021 | STANDARD_PACKAGE | STANDARD_PACKAGE | 24 | 24 | 24 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/past-tense | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 37 | Zenn | UCK8TbMQGDbB94EOR3aGJo3Q | @Zenn0009 | https://www.youtube.com/channel/UCK8TbMQGDbB94EOR3aGJo3Q | DS-000021 | STANDARD_PACKAGE | STANDARD_PACKAGE | 35 | 35 | 35 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/zenn | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 38 | Genius History | UC-q0RDBWjYlYA2KkPzq0WSQ | @genius_history01 | https://www.youtube.com/channel/UC-q0RDBWjYlYA2KkPzq0WSQ | DS-000021 | STANDARD_PACKAGE | STANDARD_PACKAGE | 10 | 10 | 10 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/genius-history | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 39 | Unknown Frequencies | UCm1yxl_4qMbStLHpHQu6xWg | @unknownfrequencies-tv | https://www.youtube.com/channel/UCm1yxl_4qMbStLHpHQu6xWg | DS-000021 | STANDARD_PACKAGE | STANDARD_PACKAGE | 19 | 19 | 19 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/unknown-frequencies | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 40 | CIPHER UNIT | UC9ibMPcwu9pesqKEyzlut7w | @CIPHER_UNIT | https://www.youtube.com/channel/UC9ibMPcwu9pesqKEyzlut7w | DS-000021 | STANDARD_PACKAGE | STANDARD_PACKAGE | 17 | 17 | 17 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/cipher-unit | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 41 | Mack | UCaS30yIIV6y2zqSnHGdIGMQ | @MackExplains7 | https://www.youtube.com/channel/UCaS30yIIV6y2zqSnHGdIGMQ | DS-000025 | STANDARD_PACKAGE | STANDARD_PACKAGE | 76 | 76 | 76 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000025; data/extracted/channel-data/DS-000025/packages/mack | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 42 | Stickly | UC53wkzZ3aXyeH9-eIgi17WA | @SticklyExplains | https://www.youtube.com/channel/UC53wkzZ3aXyeH9-eIgi17WA | DS-000025 | STANDARD_PACKAGE | STANDARD_PACKAGE | 75 | 75 | 75 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000025; data/extracted/channel-data/DS-000025/packages/stickly | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 43 | Explain In Paint | UCmYG4TVuzHphjTrP3YKYGYQ | @ExplainInPaint1 | https://www.youtube.com/channel/UCmYG4TVuzHphjTrP3YKYGYQ | DS-000025 | STANDARD_PACKAGE | STANDARD_PACKAGE | 82 | 82 | 82 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000025; data/extracted/channel-data/DS-000025/packages/explain-in-paint | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 44 | quack doc | UC2NRf0-PH8IiMq5uA5FHJnA | @quackdoc | https://www.youtube.com/channel/UC2NRf0-PH8IiMq5uA5FHJnA | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 45 | Casual Finance | UCrNfRFWnLC3tCy1TnyhVQ7g | @CasuallyFinance | https://www.youtube.com/channel/UCrNfRFWnLC3tCy1TnyhVQ7g | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 46 | Mark - Retired at 55 | UCegPlgZVNg0g1pAzZtGH4dw | @MarkRetiredAt55 | https://www.youtube.com/channel/UCegPlgZVNg0g1pAzZtGH4dw | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 47 | Tom - Lazy Dividend Investor | UCUhTFmf6v8Kk2-ofFD2udkg | @Tom-Lazy-Dividend-Investor | https://www.youtube.com/channel/UCUhTFmf6v8Kk2-ofFD2udkg | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 48 | Tom - Lazy Investor | UCHKwo7_qXD8ixLZmpPlIb_w | @1MillionWithin5Years | https://www.youtube.com/channel/UCHKwo7_qXD8ixLZmpPlIb_w | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 49 | Finance Simplified | UCogYxvdGc8i7qfjPct1c-Bg | @FinanceSimplified-USA1 | https://www.youtube.com/channel/UCogYxvdGc8i7qfjPct1c-Bg | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 50 | Rick Finance | UCDLINT0o_8a0kObYN5bBqUw | @RickFinance1 | https://www.youtube.com/channel/UCDLINT0o_8a0kObYN5bBqUw | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 51 | Overhead | UCmzMVqE2c-yPv7vmjThk4CA | @OverheadCosts | https://www.youtube.com/channel/UCmzMVqE2c-yPv7vmjThk4CA | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 52 | Millionaire Problems | UCQnC6FoEgp4VcmbPTsO9VRQ | @millyproblems | https://www.youtube.com/channel/UCQnC6FoEgp4VcmbPTsO9VRQ | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 53 | Ivan Invests | UCDokTQePVxNZUqmzevDM7NQ | @VanillaInvestor | https://www.youtube.com/channel/UCDokTQePVxNZUqmzevDM7NQ | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 54 | Nostalgic Wheels | UC3itSU41yG8jSOk8UudxoaQ | @TheWealthCortexx | https://www.youtube.com/channel/UC3itSU41yG8jSOk8UudxoaQ | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 55 | The Career Machine | UChGiil8Qsg7qdJ0tZsQo2VA | @careermachine-u4f | https://www.youtube.com/channel/UChGiil8Qsg7qdJ0tZsQo2VA | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 56 | Chill Dude Explains | UCYwOOHF1BZ_hqPVnLnrT_fw | @ChillDudeExplains | https://www.youtube.com/channel/UCYwOOHF1BZ_hqPVnLnrT_fw | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 57 | The Expensive Part | UCe2TLO3VWaMP8EthzGjSG6Q | NONE / NOT AVAILABLE | https://www.youtube.com/channel/UCe2TLO3VWaMP8EthzGjSG6Q | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 58 | Wealth Logic | UCZ-H-n8fa7NqReTRKe7ByEg | @TheWealth_Logic | https://www.youtube.com/channel/UCZ-H-n8fa7NqReTRKe7ByEg | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 59 | Neu | UChS4VG1jXDcxDnUvwcMcxtg | @neu-youtube | https://www.youtube.com/channel/UChS4VG1jXDcxDnUvwcMcxtg | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 60 | The Wise Future | UC5OaD2jizn_ZFQrB6jzXo4g | @TheWiseFuture | https://www.youtube.com/channel/UC5OaD2jizn_ZFQrB6jzXo4g | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 61 | Alicia Invests | UCFPfloFwa6X2UddqRH83rAA | @AliciaInvestsUS | https://www.youtube.com/channel/UCFPfloFwa6X2UddqRH83rAA | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 62 | David Explains Money | UC2ExrTzlNc8uNmNXodWOC-A | @DavidExplainsMoney | https://www.youtube.com/channel/UC2ExrTzlNc8uNmNXodWOC-A | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 63 | Tom Talks Money | UCKqgbX0MOmE5ZzyFpTP524g | @TomTalksMoney2k | https://www.youtube.com/channel/UCKqgbX0MOmE5ZzyFpTP524g | NONE / NOT AVAILABLE | IDENTITY_ONLY | NO_PACKAGE | 0 | 0 | 0 | 0 | NONE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json | video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 64 | Dr. Aliza Wright \| Advice | UCXZi5JVeuTluazF-fYqQgNA | @Dr.AlizaWrightAdvice | https://www.youtube.com/channel/UCXZi5JVeuTluazF-fYqQgNA | DS-000006 | HISTORICAL_CATALOG | HISTORICAL_FORMAT | 32 | 32 | 32 | 0 | COMPLETE | 39 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | PARTIAL | UNAVAILABLE | data/raw/competitors/DS-000006; data/manifests/DS-000006.md | forensic video, first-party Analytics |
| 65 | Dr. Elias Senior Health | UCQcBYZxFW7YwNMU8-DsT3Uw | @Dr.EliasYT | https://www.youtube.com/channel/UCQcBYZxFW7YwNMU8-DsT3Uw | DS-000019 | HISTORICAL_CATALOG | HISTORICAL_FORMAT | 29 | 29 | 29 | 0 | COMPLETE | 29 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | PARTIAL | UNAVAILABLE | data/raw/competitors/DS-000019; data/manifests/DS-000019.md | forensic video, first-party Analytics |
| 66 | Matty Invests | UCkqzov98m_7niJOXwbRQgBA | @MattyInvests | https://www.youtube.com/channel/UCkqzov98m_7niJOXwbRQgBA | DS-000001 | HISTORICAL_CATALOG | HISTORICAL_FORMAT | 94 | 94 | 93 | 1 | NONE | 0 | NOT_AVAILABLE | READY | PARTIAL | READY | UNAVAILABLE | PARTIAL | UNAVAILABLE | data/raw/competitors/DS-000001; data/manifests/DS-000001.md | 1 real transcripts, downloaded visual evidence, forensic video, first-party Analytics |
| 67 | Mr. Finance | UC6AwWrRKNrwt83CMJqeTUzw | @misterfinanceyt | https://www.youtube.com/channel/UC6AwWrRKNrwt83CMJqeTUzw | DS-000001 | HISTORICAL_CATALOG | HISTORICAL_FORMAT | 65 | 65 | 65 | 0 | NONE | 0 | NOT_AVAILABLE | READY | PARTIAL | READY | UNAVAILABLE | PARTIAL | UNAVAILABLE | data/raw/competitors/DS-000001; data/manifests/DS-000001.md | downloaded visual evidence, forensic video, first-party Analytics |
| 68 | Tp Dossier | UCFKmBxFC3dOkUv1GirzTjww | @TPDossierYT | https://www.youtube.com/channel/UCFKmBxFC3dOkUv1GirzTjww | DS-000022 | STANDARD_PACKAGE | STANDARD_PACKAGE | 92 | 92 | 92 | 0 | COMPLETE | 0 | NOT_AVAILABLE | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000022; data/extracted/channel-data/DS-000022/packages/tp-dossier | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |
| 69 | xkcd's What If? | UC6IxnFzHofFJ5X2PycSMsww | @xkcd_whatif | https://www.youtube.com/channel/UC6IxnFzHofFJ5X2PycSMsww | DS-000012, DS-000013, DS-000014, DS-000015, DS-000017 | HISTORICAL_CATALOG | HISTORICAL_FORMAT | 83 | 83 | 83 | 0 | COMPLETE | 190 | AVAILABLE_WITH_LIMITATIONS | READY | READY | READY | PARTIAL | UNAVAILABLE | UNAVAILABLE | data/raw/competitors/DS-000012; data/manifests/DS-000012.md; data/raw/competitors/DS-000013; data/manifests/DS-000013.md; data/raw/competitors/DS-000014; data/manifests/DS-000014.md; data/raw/competitors/DS-000015; data/manifests/DS-000015.md; data/raw/competitors/DS-000017; data/manifests/DS-000017.md | strategy artifact, first-party Analytics |
| 70 | Dr. Ares Senior | UC356D-NzdnznBOftTpYoBLw | @Dr.Ares-YT | https://www.youtube.com/channel/UC356D-NzdnznBOftTpYoBLw | DS-000027 | RAW_ACQUISITION_PENDING_PACKAGE | NO_PACKAGE | 35 | 35 | 35 | 0 | COMPLETE | 0 | NOT_AVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | data/raw/channel-data/DS-000027; data/manifests/DS-000027_*.json | downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics |

## Unresolved screenshot-only subjects

| Subject | Dataset | Screenshots | Canonical ID | Use today |
|---|---|---:|---|---|
| Doctor Thomas | DS-000003 | 5 | NONE / NOT AVAILABLE | Screenshot visual observation only; identity resolution required before channel joins |
| Dr. Adewale | DS-000004 | 13 | NONE / NOT AVAILABLE | Screenshot visual observation only; identity resolution required before channel joins |
| Dr. Okoro | DS-000005 | 10 | NONE / NOT AVAILABLE | Screenshot visual observation only; identity resolution required before channel joins |
| Dr. Waterling | DS-000007 | 13 | NONE / NOT AVAILABLE | Screenshot visual observation only; identity resolution required before channel joins |
| The Senior Health Podcast | DS-000008 | 37 | NONE / NOT AVAILABLE | Screenshot visual observation only; identity resolution required before channel joins |
| Senior Health Hub | DS-000009 | 24 | NONE / NOT AVAILABLE | Screenshot visual observation only; identity resolution required before channel joins |
| The Health Educator | DS-000010 | 11 | NONE / NOT AVAILABLE | Screenshot visual observation only; identity resolution required before channel joins |

## Compact channel data cards

### Channel: Crayon Capital

Canonical ID: `UCP9RPj_BG0vit2TNM7LuRxA`; Handle: `@Crayon_Capital`; URL: https://www.youtube.com/channel/UCP9RPj_BG0vit2TNM7LuRxA
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000023. Counts: 30 videos, 30 descriptions, 30 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000023; data/extracted/channel-data/DS-000023/packages/crayon-capital. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Lucas Grant

Canonical ID: `UCTcOboZIhgrKHMDm-oTlTOg`; Handle: `@LucasGrant-usa`; URL: https://www.youtube.com/channel/UCTcOboZIhgrKHMDm-oTlTOg
Status/source/datasets: COMPLETE_WITH_LIMITATIONS / STANDARD_PACKAGE / DS-000022. Counts: 95 videos, 95 descriptions, 85 real transcripts, 10 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000022; data/extracted/channel-data/DS-000022/packages/lucas-grant. Missing: 10 real transcripts, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Well.

Canonical ID: `UCW4NZzZ-6At6DFrCn7rJ0bQ`; Handle: `@Well.4`; URL: https://www.youtube.com/channel/UCW4NZzZ-6At6DFrCn7rJ0bQ
Status/source/datasets: COMPLETE_WITH_LIMITATIONS / STANDARD_PACKAGE / DS-000022. Counts: 32 videos, 32 descriptions, 32 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000022; data/extracted/channel-data/DS-000022/packages/well. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Brimm.

Canonical ID: `UC1GwXFBhh1fiLLuZxs8VRXA`; Handle: `@brimm-tv`; URL: https://www.youtube.com/channel/UC1GwXFBhh1fiLLuZxs8VRXA
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000024. Counts: 44 videos, 44 descriptions, 44 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000024; data/extracted/channel-data/DS-000024/packages/brimm. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Zoozle

Canonical ID: `UChFs6t9iB1yv0X8fuKtNIvA`; Handle: `@zoozleworld`; URL: https://www.youtube.com/channel/UChFs6t9iB1yv0X8fuKtNIvA
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000023. Counts: 39 videos, 39 descriptions, 39 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000023; data/extracted/channel-data/DS-000023/packages/zoozle. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Just Some Guy Stories

Canonical ID: `UCNO35SZS-e3f1hLIDon_mag`; Handle: `@justsomeguystories`; URL: https://www.youtube.com/channel/UCNO35SZS-e3f1hLIDon_mag
Status/source/datasets: COMPLETE_WITH_LIMITATIONS / STANDARD_PACKAGE / DS-000022. Counts: 13 videos, 13 descriptions, 13 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000022; data/extracted/channel-data/DS-000022/packages/just-some-guy-stories. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Brofessor Stein

Canonical ID: `UCZqJKUTmgB-cffFSzL3ENJA`; Handle: `@BrofessorStein`; URL: https://www.youtube.com/channel/UCZqJKUTmgB-cffFSzL3ENJA
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Lost Legacy

Canonical ID: `UC96yqt8xjtShTpgdoIo0Lqg`; Handle: `@LostLegacy-YT`; URL: https://www.youtube.com/channel/UC96yqt8xjtShTpgdoIo0Lqg
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000024. Counts: 45 videos, 45 descriptions, 45 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000024; data/extracted/channel-data/DS-000024/packages/lost-legacy. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: ago.

Canonical ID: `UCJqZXjdkolPUgVcf6WBm8VA`; Handle: `@ago-chanell`; URL: https://www.youtube.com/channel/UCJqZXjdkolPUgVcf6WBm8VA
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000024. Counts: 50 videos, 50 descriptions, 50 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000024; data/extracted/channel-data/DS-000024/packages/ago. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Carl Invests

Canonical ID: `UCxoC2voi0vPg2hwqgfjdhYw`; Handle: `@carlinvestsUS`; URL: https://www.youtube.com/channel/UCxoC2voi0vPg2hwqgfjdhYw
Status/source/datasets: COMPLETE_WITH_LIMITATIONS / STANDARD_PACKAGE / DS-000022. Counts: 80 videos, 80 descriptions, 80 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000022; data/extracted/channel-data/DS-000022/packages/carl-invests. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Hypothetically

Canonical ID: `UC0L9hD7HMwWU7xuU5HRA6Iw`; Handle: `@HypotheticallyHQ`; URL: https://www.youtube.com/channel/UC0L9hD7HMwWU7xuU5HRA6Iw
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000024. Counts: 39 videos, 39 descriptions, 39 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000024; data/extracted/channel-data/DS-000024/packages/hypothetically. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Casually Explained

Canonical ID: `UCr3cBLTYmIK9kY0F_OdFWFQ`; Handle: `@CasuallyExplained`; URL: https://www.youtube.com/channel/UCr3cBLTYmIK9kY0F_OdFWFQ
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Nick Invests

Canonical ID: `UCXzNNA2ngRpRiWvyA7eGd6w`; Handle: `@nickinvestsUS`; URL: https://www.youtube.com/channel/UCXzNNA2ngRpRiWvyA7eGd6w
Status/source/datasets: COMPLETE_WITH_LIMITATIONS / STANDARD_PACKAGE / DS-000022. Counts: 363 videos, 363 descriptions, 363 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000022; data/extracted/channel-data/DS-000022/packages/nick-invests. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Primate Economics

Canonical ID: `UC14Fb2zWTEZklONPXFbLrTQ`; Handle: `@Primateeconomics`; URL: https://www.youtube.com/channel/UC14Fb2zWTEZklONPXFbLrTQ
Status/source/datasets: COMPLETE_WITH_LIMITATIONS / STANDARD_PACKAGE / DS-000020. Counts: 28 videos, 15 descriptions, 28 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000020; data/extracted/channel-data/DS-000020/packages/primate-economics. Missing: 13 descriptions, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Apesthetic

Canonical ID: `UCGnTHU6UMQQlR6cl4CP3jlg`; Handle: `@ApestheticGuide`; URL: https://www.youtube.com/channel/UCGnTHU6UMQQlR6cl4CP3jlg
Status/source/datasets: COMPLETE_WITH_LIMITATIONS / STANDARD_PACKAGE / DS-000020. Counts: 22 videos, 21 descriptions, 22 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000020; data/extracted/channel-data/DS-000020/packages/apesthetic. Missing: 1 descriptions, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Maximus

Canonical ID: `UCJgTBuO9fbNvgL_IS8pqtqg`; Handle: `@Pastwithmax`; URL: https://www.youtube.com/channel/UCJgTBuO9fbNvgL_IS8pqtqg
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000023. Counts: 5 videos, 5 descriptions, 5 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000023; data/extracted/channel-data/DS-000023/packages/maximus. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Bernard

Canonical ID: `UC_FStSURaDad8-xo6jH1j4Q`; Handle: `@BernardAnimationOfficial`; URL: https://www.youtube.com/channel/UC_FStSURaDad8-xo6jH1j4Q
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: The Life Outline

Canonical ID: `UCeVwhrEnYjCNdaDr47x4dSw`; Handle: `@TheLifeOutline`; URL: https://www.youtube.com/channel/UCeVwhrEnYjCNdaDr47x4dSw
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000023. Counts: 15 videos, 15 descriptions, 15 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000023; data/extracted/channel-data/DS-000023/packages/the-life-outline. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Max Invests

Canonical ID: `UCXSpMZ1S5In6aRCyWdM5CAw`; Handle: `@MaxInvests-US`; URL: https://www.youtube.com/channel/UCXSpMZ1S5In6aRCyWdM5CAw
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Fasted Fred

Canonical ID: `UC91LLjU9cbyLBOjSxWR3cMg`; Handle: `@ItsFastedFred`; URL: https://www.youtube.com/channel/UC91LLjU9cbyLBOjSxWR3cMg
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Brick Body

Canonical ID: `UCq1V-pmuLDjjTrgFyzxYQ5g`; Handle: `@bricklifts`; URL: https://www.youtube.com/channel/UCq1V-pmuLDjjTrgFyzxYQ5g
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Bro Pump

Canonical ID: `UCQTcmLiL5_HMUnO1GRwCdjQ`; Handle: `@BropumpYT`; URL: https://www.youtube.com/channel/UCQTcmLiL5_HMUnO1GRwCdjQ
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000023. Counts: 21 videos, 21 descriptions, 21 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000023; data/extracted/channel-data/DS-000023/packages/bro-pump. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Chat History

Canonical ID: `UCicVSNyM7PMXEzdoAsTB02w`; Handle: `@ChatHistory`; URL: https://www.youtube.com/channel/UCicVSNyM7PMXEzdoAsTB02w
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Parentitude

Canonical ID: `UCJ8_5EeAN8fg0JIhxgHKndw`; Handle: `@Parentitude`; URL: https://www.youtube.com/channel/UCJ8_5EeAN8fg0JIhxgHKndw
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Parenting Hacks

Canonical ID: `UC4eR2RUwoQrYEgbzReQV3HA`; Handle: `@Parentinghacks-x6k`; URL: https://www.youtube.com/channel/UC4eR2RUwoQrYEgbzReQV3HA
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Bob Invests

Canonical ID: `UCAKBDBaY1dP7OdZkGPiDnug`; Handle: `@bobinvestsUS`; URL: https://www.youtube.com/channel/UCAKBDBaY1dP7OdZkGPiDnug
Status/source/datasets: COMPLETE_WITH_LIMITATIONS / STANDARD_PACKAGE / DS-000022. Counts: 57 videos, 57 descriptions, 57 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000022; data/extracted/channel-data/DS-000022/packages/bob-invests. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Sonny Finance

Canonical ID: `UCFvEZUMNoAVjSoSB8NrV7yw`; Handle: `@Sonny_Finance`; URL: https://www.youtube.com/channel/UCFvEZUMNoAVjSoSB8NrV7yw
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000020. Counts: 39 videos, 39 descriptions, 39 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000020; data/extracted/channel-data/DS-000020/packages/sonny-finance. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Money Life POV

Canonical ID: `UCCEwJbv7D1CYzxdKYYOH6AA`; Handle: `@MoneyLifePOV`; URL: https://www.youtube.com/channel/UCCEwJbv7D1CYzxdKYYOH6AA
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000020. Counts: 20 videos, 20 descriptions, 20 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000020; data/extracted/channel-data/DS-000020/packages/money-life-pov. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: My Chaotic Stories

Canonical ID: `UC9m3w-9L_Bt34x02IQXQ5kg`; Handle: `@mychaoticstories`; URL: https://www.youtube.com/channel/UC9m3w-9L_Bt34x02IQXQ5kg
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000020. Counts: 23 videos, 23 descriptions, 23 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000020; data/extracted/channel-data/DS-000020/packages/my-chaotic-stories. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: inkly

Canonical ID: `UCcWtWryYdHHiNWfZGSROl1A`; Handle: `@inklyHQ`; URL: https://www.youtube.com/channel/UCcWtWryYdHHiNWfZGSROl1A
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000021. Counts: 28 videos, 28 descriptions, 28 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/inkly. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Ink Explainer

Canonical ID: `UCpgrEMx8diLrw7YNQ6r3uUw`; Handle: `@Inkexplainer96`; URL: https://www.youtube.com/channel/UCpgrEMx8diLrw7YNQ6r3uUw
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000021. Counts: 15 videos, 15 descriptions, 15 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/ink-explainer. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Dark Ledger

Canonical ID: `UCDglfjh__GM2RFM1oAL3a6A`; Handle: `@darkledger13`; URL: https://www.youtube.com/channel/UCDglfjh__GM2RFM1oAL3a6A
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000021. Counts: 38 videos, 38 descriptions, 38 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/dark-ledger. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Shaami Finance

Canonical ID: `UC5ZSqmk7PKry99xdiRDrc0A`; Handle: `@ShaamiFinance`; URL: https://www.youtube.com/channel/UC5ZSqmk7PKry99xdiRDrc0A
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000021. Counts: 13 videos, 13 descriptions, 13 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/shaami-finance. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Oddlyhuman

Canonical ID: `UCxyQ6jK98CCOsy-gwV8QaFA`; Handle: `@OddlyHuma-n`; URL: https://www.youtube.com/channel/UCxyQ6jK98CCOsy-gwV8QaFA
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000021. Counts: 13 videos, 13 descriptions, 13 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/oddlyhuman. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Luco

Canonical ID: `UChGF6aMxELhXOKg2EDDLYNg`; Handle: `@LucoVids`; URL: https://www.youtube.com/channel/UChGF6aMxELhXOKg2EDDLYNg
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000021. Counts: 4 videos, 4 descriptions, 4 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/luco. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Past Tense

Canonical ID: `UCS3iXffTKXrhKWGXaPckb8A`; Handle: `@PastTense01`; URL: https://www.youtube.com/channel/UCS3iXffTKXrhKWGXaPckb8A
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000021. Counts: 24 videos, 24 descriptions, 24 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/past-tense. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Zenn

Canonical ID: `UCK8TbMQGDbB94EOR3aGJo3Q`; Handle: `@Zenn0009`; URL: https://www.youtube.com/channel/UCK8TbMQGDbB94EOR3aGJo3Q
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000021. Counts: 35 videos, 35 descriptions, 35 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/zenn. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Genius History

Canonical ID: `UC-q0RDBWjYlYA2KkPzq0WSQ`; Handle: `@genius_history01`; URL: https://www.youtube.com/channel/UC-q0RDBWjYlYA2KkPzq0WSQ
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000021. Counts: 10 videos, 10 descriptions, 10 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/genius-history. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Unknown Frequencies

Canonical ID: `UCm1yxl_4qMbStLHpHQu6xWg`; Handle: `@unknownfrequencies-tv`; URL: https://www.youtube.com/channel/UCm1yxl_4qMbStLHpHQu6xWg
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000021. Counts: 19 videos, 19 descriptions, 19 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/unknown-frequencies. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: CIPHER UNIT

Canonical ID: `UC9ibMPcwu9pesqKEyzlut7w`; Handle: `@CIPHER_UNIT`; URL: https://www.youtube.com/channel/UC9ibMPcwu9pesqKEyzlut7w
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000021. Counts: 17 videos, 17 descriptions, 17 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000021; data/extracted/channel-data/DS-000021/packages/cipher-unit. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Mack

Canonical ID: `UCaS30yIIV6y2zqSnHGdIGMQ`; Handle: `@MackExplains7`; URL: https://www.youtube.com/channel/UCaS30yIIV6y2zqSnHGdIGMQ
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000025. Counts: 76 videos, 76 descriptions, 76 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000025; data/extracted/channel-data/DS-000025/packages/mack. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Stickly

Canonical ID: `UC53wkzZ3aXyeH9-eIgi17WA`; Handle: `@SticklyExplains`; URL: https://www.youtube.com/channel/UC53wkzZ3aXyeH9-eIgi17WA
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000025. Counts: 75 videos, 75 descriptions, 75 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000025; data/extracted/channel-data/DS-000025/packages/stickly. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: Explain In Paint

Canonical ID: `UCmYG4TVuzHphjTrP3YKYGYQ`; Handle: `@ExplainInPaint1`; URL: https://www.youtube.com/channel/UCmYG4TVuzHphjTrP3YKYGYQ
Status/source/datasets: COMPLETE / STANDARD_PACKAGE / DS-000025. Counts: 82 videos, 82 descriptions, 82 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000025; data/extracted/channel-data/DS-000025/packages/explain-in-paint. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: quack doc

Canonical ID: `UC2NRf0-PH8IiMq5uA5FHJnA`; Handle: `@quackdoc`; URL: https://www.youtube.com/channel/UC2NRf0-PH8IiMq5uA5FHJnA
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Casual Finance

Canonical ID: `UCrNfRFWnLC3tCy1TnyhVQ7g`; Handle: `@CasuallyFinance`; URL: https://www.youtube.com/channel/UCrNfRFWnLC3tCy1TnyhVQ7g
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Mark - Retired at 55

Canonical ID: `UCegPlgZVNg0g1pAzZtGH4dw`; Handle: `@MarkRetiredAt55`; URL: https://www.youtube.com/channel/UCegPlgZVNg0g1pAzZtGH4dw
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Tom - Lazy Dividend Investor

Canonical ID: `UCUhTFmf6v8Kk2-ofFD2udkg`; Handle: `@Tom-Lazy-Dividend-Investor`; URL: https://www.youtube.com/channel/UCUhTFmf6v8Kk2-ofFD2udkg
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Tom - Lazy Investor

Canonical ID: `UCHKwo7_qXD8ixLZmpPlIb_w`; Handle: `@1MillionWithin5Years`; URL: https://www.youtube.com/channel/UCHKwo7_qXD8ixLZmpPlIb_w
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Finance Simplified

Canonical ID: `UCogYxvdGc8i7qfjPct1c-Bg`; Handle: `@FinanceSimplified-USA1`; URL: https://www.youtube.com/channel/UCogYxvdGc8i7qfjPct1c-Bg
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Rick Finance

Canonical ID: `UCDLINT0o_8a0kObYN5bBqUw`; Handle: `@RickFinance1`; URL: https://www.youtube.com/channel/UCDLINT0o_8a0kObYN5bBqUw
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Overhead

Canonical ID: `UCmzMVqE2c-yPv7vmjThk4CA`; Handle: `@OverheadCosts`; URL: https://www.youtube.com/channel/UCmzMVqE2c-yPv7vmjThk4CA
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Millionaire Problems

Canonical ID: `UCQnC6FoEgp4VcmbPTsO9VRQ`; Handle: `@millyproblems`; URL: https://www.youtube.com/channel/UCQnC6FoEgp4VcmbPTsO9VRQ
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Ivan Invests

Canonical ID: `UCDokTQePVxNZUqmzevDM7NQ`; Handle: `@VanillaInvestor`; URL: https://www.youtube.com/channel/UCDokTQePVxNZUqmzevDM7NQ
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Nostalgic Wheels

Canonical ID: `UC3itSU41yG8jSOk8UudxoaQ`; Handle: `@TheWealthCortexx`; URL: https://www.youtube.com/channel/UC3itSU41yG8jSOk8UudxoaQ
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: The Career Machine

Canonical ID: `UChGiil8Qsg7qdJ0tZsQo2VA`; Handle: `@careermachine-u4f`; URL: https://www.youtube.com/channel/UChGiil8Qsg7qdJ0tZsQo2VA
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Chill Dude Explains

Canonical ID: `UCYwOOHF1BZ_hqPVnLnrT_fw`; Handle: `@ChillDudeExplains`; URL: https://www.youtube.com/channel/UCYwOOHF1BZ_hqPVnLnrT_fw
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: The Expensive Part

Canonical ID: `UCe2TLO3VWaMP8EthzGjSG6Q`; Handle: `NONE / NOT AVAILABLE`; URL: https://www.youtube.com/channel/UCe2TLO3VWaMP8EthzGjSG6Q
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Wealth Logic

Canonical ID: `UCZ-H-n8fa7NqReTRKe7ByEg`; Handle: `@TheWealth_Logic`; URL: https://www.youtube.com/channel/UCZ-H-n8fa7NqReTRKe7ByEg
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Neu

Canonical ID: `UChS4VG1jXDcxDnUvwcMcxtg`; Handle: `@neu-youtube`; URL: https://www.youtube.com/channel/UChS4VG1jXDcxDnUvwcMcxtg
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: The Wise Future

Canonical ID: `UC5OaD2jizn_ZFQrB6jzXo4g`; Handle: `@TheWiseFuture`; URL: https://www.youtube.com/channel/UC5OaD2jizn_ZFQrB6jzXo4g
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Alicia Invests

Canonical ID: `UCFPfloFwa6X2UddqRH83rAA`; Handle: `@AliciaInvestsUS`; URL: https://www.youtube.com/channel/UCFPfloFwa6X2UddqRH83rAA
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: David Explains Money

Canonical ID: `UC2ExrTzlNc8uNmNXodWOC-A`; Handle: `@DavidExplainsMoney`; URL: https://www.youtube.com/channel/UC2ExrTzlNc8uNmNXodWOC-A
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Tom Talks Money

Canonical ID: `UCKqgbX0MOmE5ZzyFpTP524g`; Handle: `@TomTalksMoney2k`; URL: https://www.youtube.com/channel/UCKqgbX0MOmE5ZzyFpTP524g
Status/source/datasets: IDENTITY_VERIFIED_DATA_NOT_EXTRACTED / IDENTITY_ONLY / NONE / NOT AVAILABLE. Counts: 0 videos, 0 descriptions, 0 real transcripts, 0 placeholders.
Available: video metadata NONE; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json. Missing: video metadata, descriptions, transcripts, thumbnail metadata, downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: IDENTITY TRACKING ONLY.

### Channel: Dr. Aliza Wright | Advice

Canonical ID: `UCXZi5JVeuTluazF-fYqQgNA`; Handle: `@Dr.AlizaWrightAdvice`; URL: https://www.youtube.com/channel/UCXZi5JVeuTluazF-fYqQgNA
Status/source/datasets: COMPLETE / HISTORICAL_CATALOG / DS-000006. Counts: 32 videos, 32 descriptions, 32 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_EVIDENCE; forensic video NOT_AVAILABLE; generated intelligence TOPIC_OPPORTUNITY, PACKAGING, HOOK, SCRIPT, CHANNEL_STRATEGY, UNIFIED_ORCHESTRATION; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/competitors/DS-000006; data/manifests/DS-000006.md. Missing: forensic video, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH, THUMBNAIL RESEARCH, CONTENT BLUEPRINT.

### Channel: Dr. Elias Senior Health

Canonical ID: `UCQcBYZxFW7YwNMU8-DsT3Uw`; Handle: `@Dr.EliasYT`; URL: https://www.youtube.com/channel/UCQcBYZxFW7YwNMU8-DsT3Uw
Status/source/datasets: COMPLETE / HISTORICAL_CATALOG / DS-000019. Counts: 29 videos, 29 descriptions, 29 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_EVIDENCE; forensic video NOT_AVAILABLE; generated intelligence TOPIC_OPPORTUNITY, PACKAGING, HOOK, SCRIPT, CHANNEL_STRATEGY, UNIFIED_ORCHESTRATION; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/competitors/DS-000019; data/manifests/DS-000019.md. Missing: forensic video, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH, THUMBNAIL RESEARCH, CONTENT BLUEPRINT.

### Channel: Matty Invests

Canonical ID: `UCkqzov98m_7niJOXwbRQgBA`; Handle: `@MattyInvests`; URL: https://www.youtube.com/channel/UCkqzov98m_7niJOXwbRQgBA
Status/source/datasets: COMPLETE_WITH_LIMITATIONS / HISTORICAL_CATALOG / DS-000001. Counts: 94 videos, 94 descriptions, 93 real transcripts, 1 placeholders.
Available: video metadata COMPLETE_WITH_LIMITATIONS; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence TOPIC_OPPORTUNITY, PACKAGING, HOOK, SCRIPT, CHANNEL_STRATEGY, UNIFIED_ORCHESTRATION; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/competitors/DS-000001; data/manifests/DS-000001.md. Missing: 1 real transcripts, downloaded visual evidence, forensic video, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH, CONTENT BLUEPRINT.

### Channel: Mr. Finance

Canonical ID: `UC6AwWrRKNrwt83CMJqeTUzw`; Handle: `@misterfinanceyt`; URL: https://www.youtube.com/channel/UC6AwWrRKNrwt83CMJqeTUzw
Status/source/datasets: COMPLETE_WITH_LIMITATIONS / HISTORICAL_CATALOG / DS-000001. Counts: 65 videos, 65 descriptions, 65 real transcripts, 0 placeholders.
Available: video metadata COMPLETE_WITH_LIMITATIONS; thumbnail metadata NONE; actual visuals NONE; forensic video NOT_AVAILABLE; generated intelligence TOPIC_OPPORTUNITY, PACKAGING, HOOK, SCRIPT, CHANNEL_STRATEGY, UNIFIED_ORCHESTRATION; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/competitors/DS-000001; data/manifests/DS-000001.md. Missing: downloaded visual evidence, forensic video, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH, CONTENT BLUEPRINT.

### Channel: Tp Dossier

Canonical ID: `UCFKmBxFC3dOkUv1GirzTjww`; Handle: `@TPDossierYT`; URL: https://www.youtube.com/channel/UCFKmBxFC3dOkUv1GirzTjww
Status/source/datasets: COMPLETE_WITH_LIMITATIONS / STANDARD_PACKAGE / DS-000022. Counts: 92 videos, 92 descriptions, 92 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000022; data/extracted/channel-data/DS-000022/packages/tp-dossier. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

### Channel: xkcd's What If?

Canonical ID: `UC6IxnFzHofFJ5X2PycSMsww`; Handle: `@xkcd_whatif`; URL: https://www.youtube.com/channel/UC6IxnFzHofFJ5X2PycSMsww
Status/source/datasets: COMPLETE_WITH_LIMITATIONS / HISTORICAL_CATALOG / DS-000012, DS-000013, DS-000014, DS-000015, DS-000017. Counts: 83 videos, 83 descriptions, 83 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals FORENSIC_VIDEO_EVIDENCE; forensic video AVAILABLE_WITH_LIMITATIONS; generated intelligence TOPIC_OPPORTUNITY, PACKAGING, HOOK, SCRIPT, EDITING_VISUAL, UNIFIED_ORCHESTRATION; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/competitors/DS-000012; data/manifests/DS-000012.md; data/raw/competitors/DS-000013; data/manifests/DS-000013.md; data/raw/competitors/DS-000014; data/manifests/DS-000014.md; data/raw/competitors/DS-000015; data/manifests/DS-000015.md; data/raw/competitors/DS-000017; data/manifests/DS-000017.md. Missing: strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH, THUMBNAIL RESEARCH, EDITING RESEARCH, CONTENT BLUEPRINT.

### Channel: Dr. Ares Senior

Canonical ID: `UC356D-NzdnznBOftTpYoBLw`; Handle: `@Dr.Ares-YT`; URL: https://www.youtube.com/channel/UC356D-NzdnznBOftTpYoBLw
Status/source/datasets: PARTIAL / RAW_ACQUISITION_PENDING_PACKAGE / DS-000027. Counts: 35 videos, 35 descriptions, 35 real transcripts, 0 placeholders.
Available: video metadata COMPLETE; thumbnail metadata COMPLETE; actual visuals THUMBNAIL_URL_ONLY; forensic video NOT_AVAILABLE; generated intelligence NONE / NOT AVAILABLE; first-party Analytics NONE / NOT AVAILABLE.
Storage: data/raw/channel-data/DS-000027; data/manifests/DS-000027_*.json. Missing: downloaded visual evidence, forensic video, generated intelligence, strategy artifact, first-party Analytics. Best uses: TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH.

# 4. Channel Groups

- **Group A — Full/near-full generated intelligence:** Matty Invests, Mr. Finance, Dr. Aliza Wright | Advice, Dr. Elias Senior Health, xkcd’s What If?. Topic, packaging, hook/script, unified plan generated. Strategy exists for first four; editing exists only for xkcd.
- **Group B — Strong research packages:** 35 STANDARD_PACKAGE channels. Metadata, descriptions, thumbnail URLs, transcripts support topic/title/hook/script/public-performance research. Intelligence is input-ready, not generated.
- **Group C — Raw-acquisition ready:** Dr. Ares Senior. Complete 35-record raw Actor output with public metadata, descriptions, thumbnail URLs, auto-generated English subtitles; package and registry integration pending.
- **Group D — Identity-only:** 29 registry channels. Identity tracking only.
- **Group E — Visual-ready:** Dr. Aliza Wright | Advice, Dr. Elias Senior Health, xkcd’s What If?. Only xkcd has forensic video/frame evidence.
- **Unresolved visual subjects:** 7 screenshot sets; useful for bounded screenshot observations, not canonical channel analysis.

# 5. Dataset to Channel Map

| Dataset ID | Dataset Name | Channel(s) | Raw Source | Package | Videos | Transcripts | Purpose | Status |
|---|---|---|---|---|---:|---:|---|---|
| DS-000001 | Matty Invests & Mr. Finance Competitor Dataset | Matty Invests, Mr. Finance | `data/raw/competitors/DS-000001` | Historical XLSX/ZIP | 159 | 158 | Historical competitor evidence | REGISTERED |
| DS-000002 | "7 Things Wealthy Retirees Stopped Buying to Stay Rich" — Forensic Video Reconstruction | NONE / NOT AVAILABLE | `data/raw/forensic-analysis/DS-000002` | None | 1 | 0 | Unknown-channel finance video forensic evidence | INGESTED; channel unresolved |
| DS-000003 | Doctor Thomas — Competitor Channel Screenshots | Doctor Thomas (unresolved subject) | `data/raw/competitors/DS-000003` | None | 0 | 0 | Channel screenshots | INGESTED; identity unresolved |
| DS-000004 | Dr. Adewale — Competitor Channel Screenshots | Dr. Adewale (unresolved subject) | `data/raw/competitors/DS-000004` | None | 0 | 0 | Channel screenshots | INGESTED; identity unresolved |
| DS-000005 | Dr. Okoro — Competitor Channel Screenshots | Dr. Okoro (unresolved subject) | `data/raw/competitors/DS-000005` | None | 0 | 0 | Channel screenshots | INGESTED; identity unresolved |
| DS-000006 | Dr. Aliza Wright / Advice — Competitor Channel Screenshots | Dr. Aliza Wright \| Advice | `data/raw/competitors/DS-000006` | Historical format | 32 | 32 | Screenshots + structured acquisition | REGISTERED |
| DS-000007 | Dr. Waterling — Competitor Channel Screenshots | Dr. Waterling (unresolved subject) | `data/raw/competitors/DS-000007` | None | 0 | 0 | Channel screenshots | INGESTED; identity unresolved |
| DS-000008 | The Senior Health Podcast — Competitor Channel Screenshots | The Senior Health Podcast (unresolved subject) | `data/raw/competitors/DS-000008` | None | 0 | 0 | Channel screenshots | INGESTED; identity unresolved |
| DS-000009 | Senior Health Hub — Competitor Channel Screenshots | Senior Health Hub (unresolved subject) | `data/raw/competitors/DS-000009` | None | 0 | 0 | Channel screenshots | INGESTED; identity unresolved |
| DS-000010 | The Health Educator — Competitor Channel Screenshots | The Health Educator (unresolved subject) | `data/raw/competitors/DS-000010` | None | 0 | 0 | Channel screenshots | INGESTED; identity unresolved |
| DS-000011 | All Training Data of YouTube — Global Knowledge Corpus | NONE / NOT AVAILABLE | `data/raw/global-youtube-knowledge/DS-000011` | None | 0 | 0 | Global training corpus; not channel dataset | INGESTED |
| DS-000012 | Sunset Video Forensic Reconstruction — Case 1 ("How long could you drive towards the sunset") | xkcd's What If? | `data/raw/forensic-analysis/DS-000012` | None | 1 | 0 | xkcd forensic case 1 | INGESTED |
| DS-000013 | Moon/Electron Physics Video Forensic Reconstruction | xkcd's What If? | `data/raw/forensic-analysis/DS-000013` | None | 1 | 0 | xkcd forensic case | INGESTED |
| DS-000014 | "Weird and Worrying Questions" Video Forensic Reconstruction | xkcd's What If? | `data/raw/forensic-analysis/DS-000014` | None | 1 | 0 | xkcd forensic case | INGESTED |
| DS-000015 | Sunset Video Forensic Reconstruction — Case 2 (independent re-run, possible revision of Case 1) | xkcd's What If? | `data/raw/forensic-analysis/DS-000015` | None | 1 | 0 | xkcd same-source independent analysis | INGESTED |
| DS-000016 | Retiree Daily-Routines Video Forensic Reconstruction | NONE / NOT AVAILABLE | `data/raw/forensic-analysis/DS-000016` | None | 1 | 0 | Unknown-channel retiree video forensic evidence | INGESTED; channel unresolved |
| DS-000017 | xkcd's What If? — Apify Channel Acquisition | xkcd's What If? | `data/raw/competitors/DS-000017` | Historical format | 83 | 83 | xkcd channel acquisition | REGISTERED |
| DS-000018 | 2026 Algorithm Update — Multi-Tab Creator Research Corpus | NONE / NOT AVAILABLE | `data/raw/global-youtube-knowledge/DS-000018` | None | 0 | 0 | Global creator research corpus; not channel dataset | REGISTERED |
| DS-000019 | Dr. Elias Senior Health — Supplied Canonical Channel Export | Dr. Elias Senior Health | `data/raw/competitors/DS-000019` | Historical format | 29 | 29 | Supplied Dr. Elias export | REGISTERED |
| DS-000020 | Five-Channel YouTube Apify Dataset Packages | Primate Economics, Apesthetic, Sonny Finance, Money Life POV, My Chaotic Stories | `data/raw/channel-data/DS-000020` | 5 packages | 132 | 132 | Five-channel acquisition | STRUCTURED_REGISTERED |
| DS-000021 | Eleven-Channel YouTube Apify Dataset Packages | inkly, Ink Explainer, Dark Ledger, Shaami Finance, Oddlyhuman, Luco, Past Tense, Zenn, Genius History, Unknown Frequencies, CIPHER UNIT | `data/raw/channel-data/DS-000021` | 11 packages | 216 | 216 | Eleven-channel acquisition | STRUCTURED_REGISTERED |
| DS-000022 | Seven User-Provided YouTube Channel Packages | Lucas Grant, Well., Just Some Guy Stories, Carl Invests, Nick Invests, Bob Invests, Tp Dossier | `data/raw/channel-data/DS-000022` | 7 packages | 732 | 722 | User-provided packages | VALIDATED; 10 placeholders |
| DS-000023 | Funded Master Channel Extraction — Batch 1 | Crayon Capital, Zoozle, Maximus, The Life Outline, Bro Pump | `data/raw/channel-data/DS-000023` | 5 packages | 110 | 110 | Funded batch 1 | STRUCTURED_REGISTERED |
| DS-000024 | Funded Master Channel Extraction — Batch 2 | Brimm., Lost Legacy, ago., Hypothetically | `data/raw/channel-data/DS-000024` | 4 packages | 178 | 178 | Funded batch 2 | STRUCTURED_REGISTERED |
| DS-000025 | Funded Master Channel Extraction — Batch 3 | Mack, Stickly, Explain In Paint | `data/raw/channel-data/DS-000025` | 3 packages | 233 | 233 | Funded batch 3 | STRUCTURED_REGISTERED |
| DS-000026 | 29-channel acquisition preflight proposal only (no dataset/run) | 29 identity-only registry channels | `data/raw/channel-data/DS-000026/preflight` | None | 0 | 0 | 29-channel preflight only | PROPOSED; no run/dataset |
| DS-000027 | Dr. Ares Senior Complete Channel Extraction (raw run; package pending) | Dr. Ares Senior | `data/raw/channel-data/DS-000027` | None yet | 35 | 35 | Dr. Ares raw acquisition | RUN SUCCEEDED; integration pending |

Overlap/lineage: DS-000012 and DS-000015 use same source video `rGZ6TsXvi8E` but are proven independent analysis passes, not independent source videos. DS-000006, DS-000019, and DS-000017 appear twice in some registry `dataset_ids` arrays; duplicates were collapsed. DS-000020 through DS-000025 report zero cross-dataset video-ID overlaps. DS-000026 is proposal/preflight, not acquired evidence. DS-000027 is later raw acquisition, not yet a standard package.

# 6. Channel to Dataset Map

| Channel | Dataset IDs | Relationship |
|---|---|---|
| Crayon Capital | DS-000023 | STANDARD_PACKAGE |
| Lucas Grant | DS-000022 | STANDARD_PACKAGE |
| Well. | DS-000022 | STANDARD_PACKAGE |
| Brimm. | DS-000024 | STANDARD_PACKAGE |
| Zoozle | DS-000023 | STANDARD_PACKAGE |
| Just Some Guy Stories | DS-000022 | STANDARD_PACKAGE |
| Brofessor Stein | NONE / NOT AVAILABLE | Identity registry only |
| Lost Legacy | DS-000024 | STANDARD_PACKAGE |
| ago. | DS-000024 | STANDARD_PACKAGE |
| Carl Invests | DS-000022 | STANDARD_PACKAGE |
| Hypothetically | DS-000024 | STANDARD_PACKAGE |
| Casually Explained | NONE / NOT AVAILABLE | Identity registry only |
| Nick Invests | DS-000022 | STANDARD_PACKAGE |
| Primate Economics | DS-000020 | STANDARD_PACKAGE |
| Apesthetic | DS-000020 | STANDARD_PACKAGE |
| Maximus | DS-000023 | STANDARD_PACKAGE |
| Bernard | NONE / NOT AVAILABLE | Identity registry only |
| The Life Outline | DS-000023 | STANDARD_PACKAGE |
| Max Invests | NONE / NOT AVAILABLE | Identity registry only |
| Fasted Fred | NONE / NOT AVAILABLE | Identity registry only |
| Brick Body | NONE / NOT AVAILABLE | Identity registry only |
| Bro Pump | DS-000023 | STANDARD_PACKAGE |
| Chat History | NONE / NOT AVAILABLE | Identity registry only |
| Parentitude | NONE / NOT AVAILABLE | Identity registry only |
| Parenting Hacks | NONE / NOT AVAILABLE | Identity registry only |
| Bob Invests | DS-000022 | STANDARD_PACKAGE |
| Sonny Finance | DS-000020 | STANDARD_PACKAGE |
| Money Life POV | DS-000020 | STANDARD_PACKAGE |
| My Chaotic Stories | DS-000020 | STANDARD_PACKAGE |
| inkly | DS-000021 | STANDARD_PACKAGE |
| Ink Explainer | DS-000021 | STANDARD_PACKAGE |
| Dark Ledger | DS-000021 | STANDARD_PACKAGE |
| Shaami Finance | DS-000021 | STANDARD_PACKAGE |
| Oddlyhuman | DS-000021 | STANDARD_PACKAGE |
| Luco | DS-000021 | STANDARD_PACKAGE |
| Past Tense | DS-000021 | STANDARD_PACKAGE |
| Zenn | DS-000021 | STANDARD_PACKAGE |
| Genius History | DS-000021 | STANDARD_PACKAGE |
| Unknown Frequencies | DS-000021 | STANDARD_PACKAGE |
| CIPHER UNIT | DS-000021 | STANDARD_PACKAGE |
| Mack | DS-000025 | STANDARD_PACKAGE |
| Stickly | DS-000025 | STANDARD_PACKAGE |
| Explain In Paint | DS-000025 | STANDARD_PACKAGE |
| quack doc | NONE / NOT AVAILABLE | Identity registry only |
| Casual Finance | NONE / NOT AVAILABLE | Identity registry only |
| Mark - Retired at 55 | NONE / NOT AVAILABLE | Identity registry only |
| Tom - Lazy Dividend Investor | NONE / NOT AVAILABLE | Identity registry only |
| Tom - Lazy Investor | NONE / NOT AVAILABLE | Identity registry only |
| Finance Simplified | NONE / NOT AVAILABLE | Identity registry only |
| Rick Finance | NONE / NOT AVAILABLE | Identity registry only |
| Overhead | NONE / NOT AVAILABLE | Identity registry only |
| Millionaire Problems | NONE / NOT AVAILABLE | Identity registry only |
| Ivan Invests | NONE / NOT AVAILABLE | Identity registry only |
| Nostalgic Wheels | NONE / NOT AVAILABLE | Identity registry only |
| The Career Machine | NONE / NOT AVAILABLE | Identity registry only |
| Chill Dude Explains | NONE / NOT AVAILABLE | Identity registry only |
| The Expensive Part | NONE / NOT AVAILABLE | Identity registry only |
| Wealth Logic | NONE / NOT AVAILABLE | Identity registry only |
| Neu | NONE / NOT AVAILABLE | Identity registry only |
| The Wise Future | NONE / NOT AVAILABLE | Identity registry only |
| Alicia Invests | NONE / NOT AVAILABLE | Identity registry only |
| David Explains Money | NONE / NOT AVAILABLE | Identity registry only |
| Tom Talks Money | NONE / NOT AVAILABLE | Identity registry only |
| Dr. Aliza Wright \| Advice | DS-000006 | HISTORICAL_CATALOG |
| Dr. Elias Senior Health | DS-000019 | HISTORICAL_CATALOG |
| Matty Invests | DS-000001 | HISTORICAL_CATALOG |
| Mr. Finance | DS-000001 | HISTORICAL_CATALOG |
| Tp Dossier | DS-000022 | STANDARD_PACKAGE |
| xkcd's What If? | DS-000012, DS-000013, DS-000014, DS-000015, DS-000017 | HISTORICAL_CATALOG |
| Dr. Ares Senior | DS-000027 | RAW_ACQUISITION_PENDING_PACKAGE |

# 7. Data Architecture

```text
Channel identity / target submissions
  data/raw/channel-targets + normalized registry + XLSX tracker

Raw evidence
  XLSX / ZIP / JSON / TXT / PNG / forensic frame artifacts

Manifests and ledgers
  dataset Markdown, file CSVs, hashes, run/cost evidence, relationship records

Historical local SQLite catalog
  regenerable index; current workspace DB is zero bytes and unusable

Extracted packages
  per-channel workbook + transcript ZIP; combined JSON/CSV/XLSX

Normalized registry
  69-channel 2026-09-14 snapshot; DS-000027 not yet integrated

Intelligence artifacts
  topic + packaging + hook/script + editing + strategy + unified plans
```

# 8. Available Fields/Data Types

- Standard package workbooks: channel identity plus 28-column video table; IDs, titles, URLs, dates, duration, views, likes, comments, descriptions, thumbnail URLs, type and derived public metrics where defined. Transcript ZIPs hold plaintext; timing generally not preserved.
- Historical structured channels: same core public metadata, descriptions, transcript references, snapshot metrics, classifications and provenance; storage varies by dataset.
- Channel-level public metadata may include subscribers, reported video count, join date, channel views, description, location and observation time. Availability varies; these are snapshots, not private Analytics.
- Classifications separate topic/format/niche/audience/presenter/editing claims from evidence. Editing claims require forensic evidence.
- DS-000027 raw records contain 35/35 IDs, titles, URLs, dates, durations, views, likes, comments, descriptions, thumbnail URLs, channel identity and auto-generated English subtitle plaintext.

# 9. Video Metadata Coverage

- 41 channels / 1,939 videos have meaningful video records. All 35 standard packages and DS-000027 report IDs, titles, URLs, publish dates, duration, views, likes, comments and thumbnail URLs complete. Historical channels retain public snapshots but exact field completeness is dataset-specific.
- Public metrics support relative/outlier analysis only. They do not provide impressions, CTR, retention or watch time.
- Partially populated exceptions: Primate Economics lacks 13 descriptions; Apesthetic lacks 1. Matty Invests has 1 transcript placeholder. Lucas Grant has 10 placeholders. Identity-only channels have no video rows.

# 10. Description Coverage

| Scope | Videos | Descriptions | Missing | Coverage |
|---|---:|---:|---:|---:|
| Standard packages | 1,601 | 1,587 | 14 | 99.1% |
| Historical structured channels | 303 | 303 | 0 | 100.0% |
| DS-000027 raw | 35 | 35 | 0 | 100.0% |
| All canonical video holdings | 1,939 | 1,925 | 14 | 99.3% |

# 11. Transcript Coverage

| Channel | Videos | Real Transcripts | Placeholder/Missing | Coverage % | Timing Quality |
|---|---:|---:|---:|---:|---|
| Crayon Capital | 30 | 30 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Lucas Grant | 95 | 85 | 10 | 89.5% | Plaintext/positional; exact timing not registered |
| Well. | 32 | 32 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Brimm. | 44 | 44 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Zoozle | 39 | 39 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Just Some Guy Stories | 13 | 13 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Brofessor Stein | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Lost Legacy | 45 | 45 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| ago. | 50 | 50 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Carl Invests | 80 | 80 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Hypothetically | 39 | 39 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Casually Explained | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Nick Invests | 363 | 363 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Primate Economics | 28 | 28 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Apesthetic | 22 | 22 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Maximus | 5 | 5 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Bernard | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| The Life Outline | 15 | 15 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Max Invests | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Fasted Fred | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Brick Body | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Bro Pump | 21 | 21 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Chat History | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Parentitude | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Parenting Hacks | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Bob Invests | 57 | 57 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Sonny Finance | 39 | 39 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Money Life POV | 20 | 20 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| My Chaotic Stories | 23 | 23 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| inkly | 28 | 28 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Ink Explainer | 15 | 15 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Dark Ledger | 38 | 38 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Shaami Finance | 13 | 13 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Oddlyhuman | 13 | 13 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Luco | 4 | 4 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Past Tense | 24 | 24 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Zenn | 35 | 35 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Genius History | 10 | 10 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Unknown Frequencies | 19 | 19 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| CIPHER UNIT | 17 | 17 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Mack | 76 | 76 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Stickly | 75 | 75 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Explain In Paint | 82 | 82 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| quack doc | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Casual Finance | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Mark - Retired at 55 | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Tom - Lazy Dividend Investor | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Tom - Lazy Investor | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Finance Simplified | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Rick Finance | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Overhead | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Millionaire Problems | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Ivan Invests | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Nostalgic Wheels | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| The Career Machine | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Chill Dude Explains | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| The Expensive Part | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Wealth Logic | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Neu | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| The Wise Future | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Alicia Invests | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| David Explains Money | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Tom Talks Money | 0 | 0 | 0 | NOT AVAILABLE | NONE / NOT AVAILABLE |
| Dr. Aliza Wright \| Advice | 32 | 32 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Dr. Elias Senior Health | 29 | 29 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Matty Invests | 94 | 93 | 1 | 98.9% | Plaintext/positional; exact timing not registered |
| Mr. Finance | 65 | 65 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Tp Dossier | 92 | 92 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| xkcd's What If? | 83 | 83 | 0 | 100.0% | Plaintext/positional; exact timing not registered |
| Dr. Ares Senior | 35 | 35 | 0 | 100.0% | Auto-generated subtitle plaintext; source track present, package timing not normalized |

Placeholders are not transcripts. Overall real-transcript coverage among video holdings: 1,928 / 1,939 = 99.4%. Eleven placeholders: Lucas Grant 10, Matty Invests 1.

# 12. Thumbnail/Visual Coverage

- Thumbnail metadata URLs: 39 channels (35 standard packages, 3 historical visual channels, DS-000027). URLs alone do not support visual-style claims.
- Downloaded/registered visual evidence: 3 canonical channels. Dr. Aliza and Dr. Elias have thumbnail/screenshot evidence; xkcd has forensic visual evidence. Seven unresolved subjects add 113 screenshots but cannot be joined to canonical Channel IDs.
- Visual observations: channel intelligence includes thumbnail annotations for Dr. Elias; historical screenshot evidence and xkcd forensic artifacts permit bounded visual observations. Do not generalize beyond sampled assets.

# 13. Forensic Video Coverage

- xkcd’s What If?: AVAILABLE_WITH_LIMITATIONS. Three canonical videos have registered visual-temporal evidence; editing intelligence is PARTIAL.
- All other canonical channels: NOT AVAILABLE. DS-000002 and DS-000016 contain forensic evidence for videos whose canonical channel identity is unresolved; they are not assigned to a channel.

# 14. Intelligence Coverage

| Channel | Topic | Packaging | Hook/Script | Editing | Strategy | Unified Plan | Generated artifact note |
|---|---|---|---|---|---|---|---|
| Crayon Capital | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Lucas Grant | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Well. | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Brimm. | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Zoozle | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Just Some Guy Stories | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Brofessor Stein | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Lost Legacy | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| ago. | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Carl Invests | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Hypothetically | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Casually Explained | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Nick Invests | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Primate Economics | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Apesthetic | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Maximus | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Bernard | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| The Life Outline | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Max Invests | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Fasted Fred | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Brick Body | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Bro Pump | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Chat History | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Parentitude | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Parenting Hacks | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Bob Invests | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Sonny Finance | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Money Life POV | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| My Chaotic Stories | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| inkly | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Ink Explainer | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Dark Ledger | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Shaami Finance | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Oddlyhuman | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Luco | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Past Tense | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Zenn | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Genius History | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Unknown Frequencies | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| CIPHER UNIT | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Mack | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Stickly | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| Explain In Paint | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| quack doc | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Casual Finance | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Mark - Retired at 55 | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Tom - Lazy Dividend Investor | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Tom - Lazy Investor | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Finance Simplified | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Rick Finance | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Overhead | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Millionaire Problems | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Ivan Invests | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Nostalgic Wheels | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| The Career Machine | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Chill Dude Explains | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| The Expensive Part | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Wealth Logic | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Neu | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| The Wise Future | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Alicia Invests | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| David Explains Money | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Tom Talks Money | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |
| Dr. Aliza Wright \| Advice | READY | READY | READY | UNAVAILABLE | PARTIAL | READY | TOPIC_OPPORTUNITY, PACKAGING, HOOK, CHANNEL_STRATEGY, UNIFIED_ORCHESTRATION |
| Dr. Elias Senior Health | READY | READY | READY | UNAVAILABLE | PARTIAL | READY | TOPIC_OPPORTUNITY, PACKAGING, HOOK, CHANNEL_STRATEGY, UNIFIED_ORCHESTRATION |
| Matty Invests | READY | PARTIAL | READY | UNAVAILABLE | PARTIAL | READY | TOPIC_OPPORTUNITY, PACKAGING, HOOK, CHANNEL_STRATEGY, UNIFIED_ORCHESTRATION |
| Mr. Finance | READY | PARTIAL | READY | UNAVAILABLE | PARTIAL | READY | TOPIC_OPPORTUNITY, PACKAGING, HOOK, CHANNEL_STRATEGY, UNIFIED_ORCHESTRATION |
| Tp Dossier | READY | READY | READY | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | inputs ready; no generated artifact |
| xkcd's What If? | READY | READY | READY | PARTIAL | UNAVAILABLE | READY | TOPIC_OPPORTUNITY, PACKAGING, HOOK, EDITING_VISUAL, UNIFIED_ORCHESTRATION |
| Dr. Ares Senior | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | UNAVAILABLE | none |

READY means evidence inputs or validated output are usable; final column distinguishes generated artifacts. Editing remains UNAVAILABLE without registered forensic evidence.

# 15. First-Party Analytics Coverage

0 / 70 channels have ingested first-party Analytics. Import schema and diagnostic code are ready, but no YouTube Studio/Analytics export exists. Therefore impressions, CTR, watch time, average view duration, retention, subscribers gained/lost and traffic sources are unavailable for every channel.

# 16. Channel × Capability Matrix

| Channel | Topic Research | Title Research | Transcript Research | Hook Research | Script Research | Thumbnail Research | Editing Research | Public Performance | Private Analytics | Content Blueprint |
|---|---|---|---|---|---|---|---|---|---|---|
| Crayon Capital | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Lucas Grant | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Well. | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Brimm. | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Zoozle | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Just Some Guy Stories | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Brofessor Stein | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Lost Legacy | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| ago. | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Carl Invests | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Hypothetically | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Casually Explained | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Nick Invests | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Primate Economics | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Apesthetic | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Maximus | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Bernard | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| The Life Outline | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Max Invests | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Fasted Fred | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Brick Body | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Bro Pump | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Chat History | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Parentitude | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Parenting Hacks | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Bob Invests | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Sonny Finance | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Money Life POV | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| My Chaotic Stories | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| inkly | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Ink Explainer | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Dark Ledger | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Shaami Finance | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Oddlyhuman | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Luco | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Past Tense | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Zenn | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Genius History | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Unknown Frequencies | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| CIPHER UNIT | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Mack | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Stickly | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| Explain In Paint | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| quack doc | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Casual Finance | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Mark - Retired at 55 | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Tom - Lazy Dividend Investor | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Tom - Lazy Investor | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Finance Simplified | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Rick Finance | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Overhead | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Millionaire Problems | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Ivan Invests | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Nostalgic Wheels | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| The Career Machine | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Chill Dude Explains | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| The Expensive Part | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Wealth Logic | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Neu | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| The Wise Future | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Alicia Invests | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| David Explains Money | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Tom Talks Money | NO | NO | NO | NO | NO | NO | NO | NO | NO | NO |
| Dr. Aliza Wright \| Advice | YES | YES | YES | YES | YES | YES | NO | YES | NO | YES |
| Dr. Elias Senior Health | YES | YES | YES | YES | YES | YES | NO | YES | NO | YES |
| Matty Invests | YES | YES | YES | YES | YES | NO | NO | YES | NO | YES |
| Mr. Finance | YES | YES | YES | YES | YES | NO | NO | YES | NO | YES |
| Tp Dossier | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |
| xkcd's What If? | YES | YES | YES | YES | YES | YES | YES | YES | NO | YES |
| Dr. Ares Senior | YES | YES | YES | YES | YES | NO | NO | YES | NO | NO |

# 17. Data Gaps

- Channels missing all transcripts: 29 identity-only channels. Channels with partial real transcript coverage: 2 (Lucas Grant, Matty Invests).
- Channels missing descriptions: 2 partially (Primate Economics 13; Apesthetic 1); 29 identity-only lack descriptions because no video dataset exists.
- Channels missing actual visual evidence: 67 / 70. Thumbnail URL metadata is not actual imagery.
- Channels missing generated topic/packaging/hook-script intelligence: 65 / 70. Thirty-five are input-ready; 29 identity-only and DS-000027 integration remain incomplete.
- Channels missing forensic evidence: 69 / 70.
- Channels with only identity: 29 / 70.
- Channels missing first-party Analytics: 70 / 70.

# 18. Duplicate/Alias Analysis

- 67 submitted target rows normalize to 63 canonical target channels: 4 duplicate/alias submission rows reconciled by Channel ID/normalized URL. No name-only merge used.
- Repeated registry dataset IDs for DS-000006, DS-000017 and DS-000019 were deduplicated in this report; they are repeated references, not independent datasets.
- DS-000012 and DS-000015 share source video and source hash. Relationship is `SAME_SOURCE_INDEPENDENT_ANALYSIS`; count source video once, preserve both analysis passes.
- DS-000020 through DS-000025 validation reports show zero cross-dataset video-ID overlap.
- Similar names such as multiple “Tom” or “Invests” channels remain separate because Channel IDs differ.

# 19. Storage Locations

- Registry: `data/normalized/channel-targets/YOUTUBE_CHANNEL_REGISTRY.json`; tracker: `data/normalized/channel-targets/YOUTUBE_CHANNEL_MASTER_TRACKER.xlsx`.
- Target authority: `data/raw/channel-targets/user-supplied-youtube-channels-2026-09-14.json`; target manifests: `data/manifests/YOUTUBE_CHANNEL_TARGETS.*`.
- Standard raw evidence: `data/raw/channel-data/DS-000020` through `DS-000025`; packages: matching `data/extracted/channel-data/<dataset>/packages/<channel>/`; combined exports beside packages.
- Historical raw evidence: `data/raw/competitors/DS-*`, `data/raw/forensic-analysis/DS-*`, with dataset manifests under `data/manifests/`.
- Dr. Ares raw evidence: `data/raw/channel-data/DS-000027/apify/dqMkTSwYwRir4QfUM/`; config/preflight under `data/manifests/DS-000027_*.json`; no extracted package yet.
- Intelligence: `data/intelligence/channels/CH-000001` through `CH-000005`, cross-channel comparisons, blueprints, plans and system registries.
- Catalog schema: `schemas/inventory/*.sql`; local DB: `data/catalog/youtube_inventory.db` (currently 0 bytes). Durable manifests/raw evidence remain source of truth.

# 20. Source-of-Truth Rules

Raw evidence and hashes outrank derived catalog rows. Manifests provide durable provenance. Normalized registry controls identity joins as of its generation date. Later verified evidence must be disclosed, not silently forced into stale registry totals. Public metrics are point-in-time observations. Transcript placeholders remain unavailable records. AI interpretations remain labeled intelligence, never factual observations.

# 21. What Each Data Type Can Be Used For

| Data Available | What We Can Learn / Do |
|---|---|
| Channel ID / identity | Reliable joins, duplicate prevention, competitor tracking, future acquisition matching |
| Channel snapshots | Public size/cadence context at observation time; not private performance |
| Video IDs, titles, dates, duration, type | Topic trends, title structures, upload cadence, format mix, evergreen/recent analysis |
| Views, likes, comments, views/day, engagement | Relative public performance, outliers, content-family benchmarking; not CTR/retention/watch time |
| Descriptions | Topic context, CTA patterns, entities, products/services, links |
| Transcript plaintext | Hooks, script structure, storytelling, claims, CTAs, tone, depth, repeated messaging; timing claims limited |
| Thumbnail URLs | Future acquisition locator only; no visual-style analysis |
| Downloaded thumbnails/screenshots | Composition, faces, text density, contrast, archetypes and themes within sampled evidence |
| Forensic video/frames | Cuts, pacing, B-roll, visual rhythm, on-screen text, camera/edit patterns within sampled videos |
| Classifications | Comparable topic/format/niche/audience/presenter labels with provenance |
| Generated intelligence | Topic opportunities, packaging patterns, hook/script findings, strategy comparisons and content plans |
| First-party Analytics | Would enable CTR, impressions, retention, watch time and audience behavior; none ingested today |

# 22. What We Can Do With Each Channel Today

| Channel | Realistic current use |
|---|---|
| Crayon Capital | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Lucas Grant | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Well. | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Brimm. | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Zoozle | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Just Some Guy Stories | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Brofessor Stein | IDENTITY TRACKING ONLY |
| Lost Legacy | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| ago. | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Carl Invests | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Hypothetically | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Casually Explained | IDENTITY TRACKING ONLY |
| Nick Invests | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Primate Economics | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Apesthetic | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Maximus | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Bernard | IDENTITY TRACKING ONLY |
| The Life Outline | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Max Invests | IDENTITY TRACKING ONLY |
| Fasted Fred | IDENTITY TRACKING ONLY |
| Brick Body | IDENTITY TRACKING ONLY |
| Bro Pump | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Chat History | IDENTITY TRACKING ONLY |
| Parentitude | IDENTITY TRACKING ONLY |
| Parenting Hacks | IDENTITY TRACKING ONLY |
| Bob Invests | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Sonny Finance | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Money Life POV | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| My Chaotic Stories | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| inkly | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Ink Explainer | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Dark Ledger | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Shaami Finance | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Oddlyhuman | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Luco | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Past Tense | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Zenn | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Genius History | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Unknown Frequencies | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| CIPHER UNIT | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Mack | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Stickly | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| Explain In Paint | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| quack doc | IDENTITY TRACKING ONLY |
| Casual Finance | IDENTITY TRACKING ONLY |
| Mark - Retired at 55 | IDENTITY TRACKING ONLY |
| Tom - Lazy Dividend Investor | IDENTITY TRACKING ONLY |
| Tom - Lazy Investor | IDENTITY TRACKING ONLY |
| Finance Simplified | IDENTITY TRACKING ONLY |
| Rick Finance | IDENTITY TRACKING ONLY |
| Overhead | IDENTITY TRACKING ONLY |
| Millionaire Problems | IDENTITY TRACKING ONLY |
| Ivan Invests | IDENTITY TRACKING ONLY |
| Nostalgic Wheels | IDENTITY TRACKING ONLY |
| The Career Machine | IDENTITY TRACKING ONLY |
| Chill Dude Explains | IDENTITY TRACKING ONLY |
| The Expensive Part | IDENTITY TRACKING ONLY |
| Wealth Logic | IDENTITY TRACKING ONLY |
| Neu | IDENTITY TRACKING ONLY |
| The Wise Future | IDENTITY TRACKING ONLY |
| Alicia Invests | IDENTITY TRACKING ONLY |
| David Explains Money | IDENTITY TRACKING ONLY |
| Tom Talks Money | IDENTITY TRACKING ONLY |
| Dr. Aliza Wright \| Advice | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH, THUMBNAIL RESEARCH, CONTENT BLUEPRINT |
| Dr. Elias Senior Health | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH, THUMBNAIL RESEARCH, CONTENT BLUEPRINT |
| Matty Invests | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH, CONTENT BLUEPRINT |
| Mr. Finance | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH, CONTENT BLUEPRINT |
| Tp Dossier | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |
| xkcd's What If? | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH, THUMBNAIL RESEARCH, EDITING RESEARCH, CONTENT BLUEPRINT |
| Dr. Ares Senior | TOPIC RESEARCH, TITLE RESEARCH, PUBLIC PERFORMANCE BENCHMARKING, TRANSCRIPT RESEARCH, HOOK RESEARCH, SCRIPT RESEARCH |

# 23. Cross-Channel Research Possibilities

| Use case | Possible now | Required data | Current limitation |
|---|---|---|---|
| Topic opportunity research | YES | Comparable titles/descriptions/public metrics | 41 channels usable; 29 identity-only excluded |
| Competitor comparison | YES | Matched public metadata and/or transcripts | Compare like niches/time windows; public snapshots differ by date |
| Title pattern research | YES | Titles + public metrics | No causal CTR claims |
| Hook library | YES | Real transcripts | Mostly untimed/positional; 29 channels absent |
| Script structure library | YES | Real transcripts | Timing and speaker segmentation limited |
| Thumbnail pattern library | PARTIAL | Downloaded images + observations | Only 3 canonical channels have actual visual evidence |
| Editing pattern library | PARTIAL | Forensic video/frame evidence | Only one identified channel; three canonical sampled videos |
| Channel-specific strategy | YES | Metadata/transcripts and comparator | Generated artifacts only for 4 channels |
| Cross-niche strategy | PARTIAL | Multiple comparable channels per niche | Calibration has only 2 channels per niche; no robust cross-niche heuristic |
| Content blueprint generation | YES | Topic + packaging + hook/script inputs | Generated plans exist for 5; can run engine for data-ready packages |
| New video planning | YES | Evidence-backed opportunity + packaging + script layers | Editing unavailable for most channels; no private Analytics validation |

# 24. Current Limitations

- Registry snapshot predates DS-000027; current audit reconciles it explicitly. DS-000027 documentation also conflicts internally: earlier preflight handoff says no run, while later config/raw evidence proves successful run. Later timestamped raw/config evidence is authoritative; package/manifest integration remains incomplete.
- Local SQLite catalog is zero bytes. SQLite cross-check unavailable; manifests, registry, ledgers, raw JSON and packages provide independent checks.
- Public metrics are snapshots and cannot substitute for impressions, CTR, retention, watch time or audience-source data.
- Transcript timing mostly untimed/positional. Do not claim second-exact hook pacing from plaintext.
- URL-only thumbnails cannot support visual analysis. Forensic conclusions cover sampled videos, not whole channels.
- Seven screenshot subjects lack canonical IDs; no safe merge to named channels is possible.

# 25. Highest-Value Next Data To Acquire

Priority uses capability unlocked × channels affected × existing readiness:

1. Complete DS-000027 packaging, manifest and registry integration. Unlocks one already-acquired channel with no new scrape.
2. Acquire/finish video datasets for 29 identity-only targets. Unlocks topic/title/performance/transcript work across largest blocked group.
3. Download representative thumbnail sets for 36 research-ready nonvisual channels (35 packages + Dr. Ares). Unlocks packaging visual research using existing metadata URLs.
4. Acquire bounded forensic samples for channels where editing research matters. Unlocks editing intelligence; prioritize cross-channel comparable samples, not all videos.
5. Ingest real first-party Analytics only for owned channels. Unlocks CTR, retention, watch-time and packaging validation; competitor channels cannot supply these privately.

# 26. Final Mental Model

Pick channel by canonical Channel ID. First inspect registry row. If STANDARD_PACKAGE, expect workbook + transcript ZIP under extracted dataset path, raw/run evidence under matching raw dataset path, and metadata/transcript research readiness. If historical, follow manifest into `data/raw/competitors` and CH-00000x intelligence paths; format varies. If identity-only, expect registry identity only. If Dr. Ares, expect raw DS-000027 records but no package yet. For visuals, distinguish URL, downloaded image, observation and forensic video. For intelligence, distinguish input-ready from generated artifact. For private metrics, expect none.

# Required Summary Table

| Data Layer | Channels Covered | Missing | Practical Use |
|---|---:|---:|---|
| Identity | 70 | 0 | Stable joins, deduplication, tracking |
| Video Metadata | 41 | 29 | Topics, cadence, formats, public performance |
| Descriptions | 41 | 29 | Context, CTAs, entities; 2 channels partial |
| Transcripts | 41 | 29 | Hooks, scripts, claims; 2 channels partial |
| Thumbnail Metadata | 39 | 31 | Future visual acquisition; title/URL joins |
| Actual Visual Evidence | 3 | 67 | Thumbnail composition and bounded visual patterns |
| Forensic Video | 1 | 69 | Editing, pacing, B-roll, visual rhythm |
| Topic Intelligence | 5 | 65 | Generated opportunities; 35 more input-ready |
| Packaging Intelligence | 5 | 65 | Generated title/thumbnail patterns; 35 more input-ready |
| Hook/Script Intelligence | 5 | 65 | Generated hook/script patterns; 35 more input-ready |
| Editing Intelligence | 1 | 69 | Evidence-bound editing patterns |
| Strategy Intelligence | 4 | 66 | Benchmarks and channel blueprints |
| First-Party Analytics | 0 | 70 | CTR, retention, watch time when future owned-channel export exists |

---

## Terminal Summary

```text
CHANNEL DATA AUDIT COMPLETE

Canonical channels: 70
Channels with meaningful video data: 41
Channels with transcripts: 41
Channels with full/near-full generated intelligence: 5
Identity-only channels: 29
Channels with actual visual evidence: 3
Channels with forensic video: 1
Channels with first-party Analytics: 0

Strongest current use cases:
1. Topic opportunity research
2. Title and public-performance benchmarking
3. Transcript, hook, and script research
4. Evidence-backed content blueprint generation
5. Cross-channel and limited cross-niche strategy

Biggest data gaps:
1. 29 identity-only channels lack video datasets
2. 67 channels lack actual visual evidence
3. 69 channels lack forensic video
4. 70 channels lack first-party Analytics
5. DS-000027 integration and local SQLite catalog are incomplete

Full report:
CHANNEL-DATA-DEEP-AUDIT.md
```
