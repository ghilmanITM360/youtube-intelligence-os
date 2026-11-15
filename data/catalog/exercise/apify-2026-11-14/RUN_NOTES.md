# Exercise channels Apify run, 2026-11-14
Actor streamers/youtube-scraper (build 0.0.333), account CLAUDE, $4/1000 videos. Input: 20 long + 20 Shorts per channel, sortVideosBy POPULAR, no subtitles.
Runs (raw/ file <- run id): pilot mBKYbVxprgIZXPnVa; batch1 2wKy4jiKo1BcQ9PvJ; batch2 LW4PVc1wWhWZXdeGR; batch3 wL34ftvgFcXGMFjdV; batch4 goZ9FekiRFeCMMABK.
Wasted duplicates (same input as batch1, data NOT kept): runs 4fjIz7lxMbQEgTb8G, jc5PfCJXp3c7cqgco, LHFSgi6uFq8eDNP5w (~$1.3). Cause: Console "Start" ignored unsaved JSON edit.
Result: 567 unique videos, 22 channels with data. No data: YourCaptainGray, simplestrengthlabhq, Physiform (empty rows). Suspect: Yellow Dude (1 row, 0 views), CoCo Fit (86 subs).
Not covered: BropumpYT, ItsFastedFred (already in repo). SHA256SUMS.txt covers raw/. Nothing committed.
Yellow Dude retry (2026-11-14): run Cm9yFAO4zdfnlOOcH, input = channel-ID /videos URL, maxResults 20, NO sortVideosBy (default newest), Shorts 0 (channel has no Shorts tab). Returned 20 videos, $0.08. Earlier runs used sortVideosBy POPULAR and returned 1 row for this channel: POPULAR sort is the likely cause. Saved as raw/exercise_yellowdude_retry_Cm9yFAO4zdfnlOOcH.json, SHA256SUMS.txt regenerated.
Possible same cause for other 0-row channels (YourCaptainGray, simplestrengthlabhq, Physiform) and the 0-Shorts channels: not tested.
3-channel retry (2026-11-14): run KL671NrLUu8vnISHX, no sortVideosBy, 20 long, 0 Shorts, $0.052. Rows: Captain Gray 4, Physiform 4, Simple Strength Lab 5 (fewer than 20 each; channel size vs actor limit not verified). raw/exercise_3channels_retry_KL671NrLUu8vnISHX.json. SHA256SUMS regenerated.

## Transcripts run V1Ch3xq1FLDJMAmAN (2026-11-14)
- Input: transcripts_input.json (top 8 long videos by viewCount per channel, 189 URLs), downloadSubtitles=true, subtitlesFormat=plaintext, lang en.
- Result: 189 rows, 169 with transcript text (avg ~1,290 words). Cost $0.756. Missing: 피지컬에셋 (3/8), namat (4/8), Metal Pump (3/8), BlueGym Animation (3/8), Captain Gray (3/4) - likely no English captions.
- File: raw/exercise_transcripts_top8_V1Ch3xq1FLDJMAmAN.json (subtitles[].plaintext). Apify credit left ~$0.5.
