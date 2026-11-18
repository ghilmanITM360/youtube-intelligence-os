# Phase Five addendum (master Phase Five parts B and C), 2026-11-18

Added by the audit pass because the master's Phase Five asked for thumbnail and script intelligence beyond titles. Labels: VERIFIED (computed) / INFERRED / UNKNOWN. Script: `hook_features.py` (read-only on the DB; run `python3 -I` from the repo root).

## C. Script and opening intelligence (computed)
Sample: 64 channels with 8+ long videos (Mr. Finance excluded), videos 14+ days old that have a transcript; "top" = 2x or more the channel's own long-form median (880 videos), "low" = below the median (1,477). Same method as the title test in Phase E.
| Opening feature | Top | Low |
|---|---:|---:|
| number or amount in first 40 words | 66% | 65% |
| question mark in first 40 words | 7% | 7% |
| "you / your" in first 40 words | 71% | 66% |
| "but / yet / except / however / instead" in first 100 words | 39% | 39% |
| greeting or "in this video" in first 40 words | 5% | 4% |
| "imagine / picture this" in first 40 words | 7% | 5% |
| median transcript length (words) | 3,042 | 2,999 |
Reading (INFERRED, correlation only; auto-captions, regex, topic and channel size not controlled): **none of these opening features separates winning from below-median videos by more than 5 points.** The Phase B observation that top videos open with a number or a contradiction is therefore NOT a difference between winners and losers; most videos in this set open that way. Consequence for us: a number-first, contradiction-first opening is table stakes (65% of low videos have it), not a differentiator. What would differentiate is unmeasured here: topic, packaging and the quality of the payoff.
Not done: frame-level visual-sequence analysis, pattern-interrupt counting, retention structure (needs video or Studio data), story arc coding by reading. These stay NA.

## B. Thumbnail intelligence (status)
- Looked at: 61 primary-six thumbnails and six montages (Phase B, VERIFIED by viewing). Findings: one dominant word or number, one emotion, one object, a real chart in the macro channels; three of six share a round-head cartoon look.
- Not redone: sub-niche-level thumbnail comparison across the other 66 channels. The repo already holds a thumbnail library and 966-thumbnail pattern CSV (`research/finance-economics-intelligence/`, REUSED from earlier audits, structural not semantic, never evidence of CTR). I did not re-read or re-sample them in this pass. Gap stays OPEN.
- Rule kept: thumbnail appearance never implies CTR or retention.
