# Latest What If / Unreasonably Exact research index (added 2026-11-24)
Added on top of the 2026-11-23 archive by a Machine A session (user `ghilmankhan`). Nothing existing was overwritten except the README.md and MANIFEST rows noted below. **Status of everything here: DRAFT / partial. No owner approval of any proposed calendar is recorded in these files. No human listening, no expert/scientist review, no CTR/retention/impression data.** Claude reviews are same-model self-reviews; Codex reviews are a different tool but not expert review. Not "final", not "validated".

## Folders (all under `research/xkcd-what-if-research-archive/`)
| Folder | Author / kind | Date | Status |
|---|---|---|---|
| `topic_cadence_deep_audit_2026-11-23/` | Claude: topic selection + competitor upload cadence (959-row inventory, 25 channels, evidence CSVs, DS-000011/018/031 + supplement review notes, NEW-08 saturation re-run, WhatIfAnimations discrepancy note) | 2026-11-23/24 | Claude self-review, draft; known stale/contradictory wording listed in its LIMITATIONS_AND_OPEN_ITEMS.md; 5,701 discarded 429 rows in `raw/failed_429_rows_discarded.jsonl` |
| `claude_calendar_review_2026-11-24/` | Claude independent review of the owner's 10-upload calendar (verdict MIXED; REVIEW_DIRECTIVE.md holds the pasted task incl. the proposed calendar) | 2026-11-24 | Claude self-review; videos NOT watched; no thumbnails reviewed |
| `codex_calendar_review_2026-11-24/` | Codex independent review of the same 10-upload calendar (verdict Mixed) | 2026-11-24 | Codex review, partial |
| `codex_topic_order_audit_2026-11-23/` | Codex topic-selection / order audit (60-day alternative workbook) | 2026-11-23 | Codex audit, draft |
| `codex_cadence_topic_order_2026-11-23/` | Codex competitor cadence + 60-day topic order (22 channels) | 2026-11-23 | Codex audit, draft |
| `forensics_logs_supplement_2026-11-23/` | 7 small run logs from the Machine B forensics zip that the first archive omitted | 2026-11-23 | logs only |
| (earlier, unchanged) `forensics_2026-11-23/`, `codex_independent_review_2026-11-23/`, `codex_readiness_review_2026-11-23/`, `inputs/`, `earlier_*` | See README.md status table | 2026-11-23 and older | unchanged |

## Calendars: what is where
- Original Unreasonably Exact 30-day calendar (2026-11-23; the Codex text calls it the approved baseline, but no approval record was found by this session): already on branch `research/what-if-channel-strategy-2026-11-18` at `research/consolidation/WHATIF_UNREASONABLY_EXACT_30_DAY_CALENDAR_2026-11-23.{csv,xlsx}` and `WHATIF_TOP_VIDEOS_PLAN_2026-11-23.pdf` (byte-identical to the Downloads copies; mapping in `LATEST_MANIFEST_2026-11-24.csv`). Also `codex_cadence_topic_order_2026-11-23/ORIGINAL_30_DAY_BASELINE.csv` maps to the same content.
- The 10-upload proposal being audited exists only as text in `claude_calendar_review_2026-11-24/REVIEW_DIRECTIVE.md` (not a file elsewhere).
- Claude recommended 10 (`claude_calendar_review_2026-11-24/RECOMMENDED_30_DAY_CALENDAR.{csv,xlsx}`): fall long D1; fall Short D4; Voyager Short D7; tiny-planet orbit long D10; Phobos Short D13; laser Short D16; Moon-vanish long D19; tides Short D22; Worden Short D25; neutron-teaspoon long D28 = HOLD FOR SCIENCE.
- Codex recommended 10 (`codex_calendar_review_2026-11-24/RECOMMENDED_30_DAY_CALENDAR.{csv,xlsx}`): fall long D1; skydiver-slowdown Short D4; Voyager one-way Short D7; sideways-jump orbit long D10; laser-echo Short D13; Voyager-reply long D16; Phobos Short D19; ocean-without-Moon long D22; solar-tide Short D25; neutron-teaspoon Short D28 (neutron long held).
- Main differences: Claude keeps a neutron long as a gated D28 slot and a Moon-vanish long D19, rejects a Voyager reply long; Codex swaps the neutron long for a conditional Voyager reply long, moves the Moon/ocean long to D22.
- 60-day alternatives: `codex_topic_order_audit_2026-11-23/NEXT_60_DAYS_PRIORITIZED_PLAN.xlsx` (7 Dec 2026 to 4 Feb 2027 model) and `codex_cadence_topic_order_2026-11-23/PROPOSED_60_DAY_ORDER.{csv,xlsx}` (6 longs + 8 Shorts). Neither is owner-approved.

## Known unresolved science / data issues (HOLD FOR SCIENCE and open items; see each folder's own files)
- Fall long: drag area/mass inputs; landing speed 164 to 205 km/h across assumptions; "100 km peak" is model-only.
- Neutron-star teaspoon long: confinement/decompression premise has no primary source read; held by both Codex audits and the Claude calendar review.
- Moon vanishing: moonless axial-tilt claims not read from primary papers.
- Phobos/tiny planet: tide, shape and rotation effects not modelled; several constants from memory.
- Voyager: NASA status (no science/engineering data since 2026-11-14 per NASA release) must be re-checked before any Short.
- Worden distance record: newer records not checked.
- Demand: no CTR/impression/retention or age-matched view data for any topic; Google Trends values are relative 0 to 100.
- DS-000011/018/031 PDFs, Automation Playbook PDF and Munroe book text were not fully re-read in the latest review (earlier notes only).
- Fall script v3 existence is reported only; no video is finished.

## Excluded / unavailable (full list: `LATEST_MANIFEST_2026-11-24.csv`)
- Images/media: none among the new candidate files; 11788 jpg/png inside the Machine B zip and 26k+ png/jpg + 25 mp4 + 16 wav in `~/YIOS-local-audits/xkcd-whatif/` were not pushed.
- Raw public comment text (`comments_sample.jsonl`, 358604 bytes): excluded; metadata-only CSV added in `topic_cadence_deep_audit_2026-11-23/raw/comments_sample_METADATA_ONLY.csv`.
- `claude_calendar_review .../raw/u.pkl` (opaque pickle): excluded; zip copy of the Claude calendar review: excluded as duplicate container.
- Third-party copyrighted PDFs/book text: never pushed.
- Folders A, B, C are on Machine B, not this Mac (A as zip only); already archived on 2026-11-23.

## Duplicate mappings and versions
Byte-identical files already on GitHub were not re-copied: 13 files (status ALREADY_PRESENT_BYTE_IDENTICAL, with branch:path). Older versions and corrections of the forensics set stay in `forensics_2026-11-23/versions_before_reconcile_2026-11-23/` and `*_v1_*`/`*_v2prelight_*` files. Same-name files in the new folders (e.g. TOPIC_RESEARCH_EVIDENCE.csv in two folders) differ in content/version and are kept apart by folder.

## Counts for this addition
New files included: 183 (7726179 bytes) incl. this index and manifest excluded from that count. Verification: `python3 -I research/xkcd-what-if-research-archive/verify_manifest.py` (original contract; new files are listed in MANIFEST.csv) plus `LATEST_MANIFEST_2026-11-24.csv` (source-to-destination mapping).
