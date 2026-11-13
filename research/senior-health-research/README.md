# Senior-health research — top-viewed topics + hook patterns (2026-11-13)

Source: `data/catalog/senior_health_complete.db` (local build, split copy in `data/catalog/senior_health/`). Script: `analyze.py` (read-only, rerunnable). Every CSV row carries `video_id` / `channel_id`.

## Scope (FACTS)
- Long-form only (>=180 s, not shorts/streams), channels with >=10 such videos with views: **4,814 videos, 77 channels**.
- Hook analysis needs a transcript: **2,269 videos, 58 channels**.
- "Relative views" = video views / that channel's median long-form views (1.0 = normal for that channel). This removes big-channel-vs-small-channel effects.

## Caveats (read before using)
- Topic/hook/format labels are **keyword rules (AI interpretation)**, not human-coded. A video can carry several topic labels.
- Transcripts exist for a *sampled* subset (newest + most-viewed + least-viewed per channel), so hook results have selection bias.
- Concentration: top-100 videos = 162.5M views; 28 are from one channel (Body Fix Exercises), 11 More Life Health, 8 ElderfitTV. Raw top lists reflect these channels' topics.
- Correlation only. No CTR/retention data; views also depend on age, thumbnail, channel size.
- Views are a snapshot at scrape time; videos with null views excluded.

## 1. Top-viewed topics
`topics_top100_vs_base.csv` — share of a topic among the top-100 videos vs its share of all long-form (lift):
- **Over-represented in top 100:** neck 7.3x, shoulder/rotator 5.1x, knee 3.1x, hip 2.4x, back/spine 2.0x, chair/seated exercise 1.7x, stretching 1.6x.
- **Under-represented:** vitamins/supplements 0.22x, kidney/liver 0x, weight loss 0x, gut 0x, eyes/hearing 0x, diabetes 0.33x, food/diet 0.54x (food is 24% of all videos but 13% of the top 100).

`topics_by_relative_views.csv` — within-channel view (median relative views; "wins" = channels where the topic beats the rest of that channel):
- Higher than the channel norm: neck 1.5, gut 1.4 (5/5 channels), hip 1.39 (6/9), chair/seated 1.31 (11/13 channels), vitamins 1.30 (15/22), strength 1.14 (23/34).
- Lower: back/spine 0.71, hands/arthritis 0.74, weight loss 0.69, eyes 0.69, diabetes 0.77.
- Two lists disagree on some topics (gut, vitamins: good *within channel*, but absent from the mega-hits; back/spine: mega-hits but weak median). Read: joint-pain "fix" content (neck/shoulder/knee/hip) produces the biggest outliers; **chair/seated is the most consistent** (works in 11 of 13 testable channels). Mega-hits are a handful of videos from a few channels, so neck/shoulder claims rest on few channels (neck 9, shoulder 8).

Title formats (`title_formats_by_relative_views.csv`): "how to / fix / relief" 1.14 (30/55 channels), emoji 1.39 (n=40, 10 channels). Numbers in title, age callouts, questions, ALL-CAPS, warnings all ~1.0, i.e. **no lift**; most channels use them, so they don't differentiate.

## 2. Hooks (first 60 words of transcript)
`hook_patterns_by_relative_views.csv`:
- Little separation. Best: first-person/personal story 1.31 (n=47, only 4/6 testable channels), senior/age address 1.11 (27/50 channels), greeting opener 1.11 (n=266, 24 channels, 5/10).
- **Promise/"in this video I will show you" opener is the clear negative: 0.73** (n=146; beats rest in only 8/15 channels).
- Question, number/stat, warning, credential, direct command: ~1.0, no effect.
- Qualitative (`hook_samples_top_vs_bottom.csv`, top 30 vs bottom 30 by relative views): the top samples open with a **direct second-person scenario or pattern interrupt** ("Stop what you're doing for 30 seconds and look down at your feet", "You wake up in the middle of the night and a sharp pain grips your leg", "Have you ever sat in the bathroom for 30 minutes…"). Bottom samples open with a channel intro / greeting / topical update ("Hello everyone, this is Dr… COVID update", "welcome to Elder fit TV, my name's Tom"). This is a reading of 60 samples, not a statistic; my rule-based "greeting" label does not separate them (greetings appear in both).

## Confidence
- Medium: chair/seated consistency; promise-opener underperforms; joint-pain topics over-represented in mega-hits.
- Low: any single hook label effect (small gaps, ~half of channels), neck/shoulder (few channels), the scenario-opener impression (60 samples, hand-read, not coded).
- Not tested: thumbnails, retention, duration, upload age, channel-size interaction. Those need separate passes.

## Files
`analyze.py`, `topics_by_relative_views.csv`, `topics_top100_vs_base.csv`, `top100_videos_by_views.csv`, `title_formats_by_relative_views.csv`, `hook_patterns_by_relative_views.csv`, `hook_samples_top_vs_bottom.csv`.
