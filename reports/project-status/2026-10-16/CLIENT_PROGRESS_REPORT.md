# Progress report: YouTube Intelligence OS

**Date:** 16 October 2026 · **Prepared from:** repository and GitHub records as of that date

## Overview

YouTube Intelligence OS is an evidence-based research system for YouTube channels. It stores competitor and own-channel information with a record of where each fact came from. It then turns that information into content plans covering topics, titles, thumbnails, scripts and editing. Every conclusion points back to its source, and unproven ideas are labelled as hypotheses.

## Current stage

- **Core system (Version 1): complete** within the limits of the evidence collected. All automated tests pass (460 passed, 1 deliberately skipped).
- **Finance & Economics research: in progress.** The data foundation is finished and checked. The detailed reading and interpretation of that data is only partly done.
- **Video production experiments: in review.** Several illustrated short videos exist as drafts awaiting your review.

## Progress, stated honestly

A single overall percentage would be misleading, because the project mixes finished software, ongoing research and creative drafts. Separate, measured figures:

| Area | What is measured | Result |
|---|---|---|
| Core system | Automated tests passing | 460 of 461 (1 skipped by design) |
| Finance research: data foundation | Videos catalogued / transcripts found | 966 videos across 13 channels; 955 transcripts (98.9%) |
| Finance research: historical performance | Videos given a comparable performance rating | 723 of 966 (74.8%) |
| Finance research: detailed reading | Titles, topics and scripts reviewed by an analyst | 30 of 966 (about 3%); 17 scripts read in full |
| Finance research: thumbnails | Thumbnails downloaded and reviewed | 27 of 966 (about 3%) |
| Finance research: overall estimate | Weighted across 16 milestones | roughly **34% to 42%** (an estimate; see note) |
| Casual Economics study | Video packages built / fully reviewed by ear and eye | 11 of 11 built; 0 of 11 fully reviewed |
| Casually Finance study | Selected videos analysed | 16 of 18 |

*Note:* the Finance estimate counts the work against the full set of 966 videos. Against the smaller sample the team originally planned (30 videos and six extra channels), the planned work is done. The weights used for the estimate are a judgement, so treat it as a guide, not a guarantee.

## Major milestones completed

- Version 1 of the system finished and verified (11 September 2026), then extended with additional channel integrations through 11 October.
- Knowledge base consolidating 5,976 historical sources, validated with zero errors (15 October).
- Finance baseline: every catalogued video and transcript checked and reproducible (16 October).
- Performance comparisons for 723 videos, with sensitivity checks showing most ratings hold under alternative methods.
- Source dates recovered for 595 records, allowing fair age comparisons.
- Latest quality check on the Finance work passed: automated validation and the full test run succeeded.

## Finance & Economics research coverage

Early findings (descriptive, not proof of cause): specific, number-led titles about monthly investing and household costs performed well; some mortgage and car-cost titles performed poorly and serve as counterexamples. Twelve candidate video topics and four pilot concepts have been drafted. They are **proposals, not yet validated**.

## Work in progress

- Wider reading of titles, scripts and thumbnails across all 13 channels.
- Study of smaller and newer channels (so far, the extra channels examined are mostly established ones).
- Illustrated short videos in review: three senior-health videos, a diabetes-and-heart-warning video, and a finance short.

## Outstanding tasks

1. Review of 936 remaining titles and topics, and more scripts and thumbnails.
2. Search-interest (Google Trends) and news-event checks for the Finance channels.
3. Dates and formats for 159 older records, which may not be recoverable.
4. Your review and approval of draft videos; medical statements in the health videos need a clinician's check.
5. Decisions on which of the open proposals to accept.

## Risks and blockers

- **Work saved only on one computer:** about 150 MB of production and research files are not yet backed up to the repository. We recommend deciding where they should be saved.
- **Approvals needed from you:** nothing has been merged into the main version without your approval, so several finished items are waiting.
- **Health content:** publication of the health videos requires clinical review.
- **Data limits:** competitor private statistics are unavailable, so the findings describe what happened, not why.
- **Session limits:** the research stopped twice at its usage limit; it can resume without repeating earlier work.

## Recent milestones

| Date | Milestone |
|---|---|
| 15 Oct | Knowledge base and Finance research plan delivered |
| 16 Oct (early) | Finance baseline validated; first research checkpoint |
| 16 Oct (morning) | Deeper script and title reviews; performance ratings expanded from 176 to 723 videos |
| 16 Oct | Three senior-health videos reached their third review version |

## Recommended next steps

1. Confirm where the unsaved production and research files should be stored.
2. Continue the Finance research with reviews of the channels not yet read in depth.
3. Provide a list of smaller or newer finance channels to study.
4. Schedule review of the draft videos and the clinical check of the health content.
5. Decide the order in which the waiting items should be merged.

## References

- Finance & Economics research: [Pull request 36](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/36), branch `research/finance-economics-intelligence` (draft)
- Casual Economics: [PR 25](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/25), Casually Finance: [PR 21](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/21) and [PR 28](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/28)
- Videos: [PR 34](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/34), [PR 32](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/32), [PR 30](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/30)

## Quality and validation status

All automated checks passed on the latest Finance update, and on every open proposal. No private or secret information was found in tracked files. Human review of audio and visuals is still pending for the videos and the Casual Economics study.
