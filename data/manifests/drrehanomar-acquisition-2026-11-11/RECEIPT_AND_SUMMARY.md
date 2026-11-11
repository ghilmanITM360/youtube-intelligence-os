# Dr Rehan Omar (@DrRehanOmar) — metadata pilot receipt, 2026-11-11

Channel identity: UCQIzqH7QZ9viBYpOFqgSXMg ("Decode Your Heart – Dr. Rehan"), 55 subs, joined 2026-02-03.
Matches registry channel (OWN_CHANNEL; registry status COMPLETE; DS-000032, 56 videos, plaintext subtitles, no timestamps).
Actor: streamers/youtube-scraper (h7sDV53CddomktSi5), Free plan, pay-per-event $0.004/video; transcribeMinute add-on $0.048/min (NOT used).
All runs launched via authenticated Apify Console UI; no token/cookie read, stored or displayed. Exported via Console Export (JSON, all fields).

| Run | ID | Purpose | Items | Charged |
|---|---|---|---|---|
| 1 | hchPTn0xs6ghlnOHt | metadata; auto-cap $0.12 truncated it | 37 | $0.120 |
| 2 | pIE5dtwJbn9aPHR6K | full metadata, cap $0.30 | 66 | $0.264 |
| 3 | V9H05XX1hbLLhUUj8 | subtitles-only (SRT) for the 10 new videos, cap $0.10 | 10 | $0.040 |
| **Total** | | | | **$0.424 (cap $0.50)** |

Run 1 was started unintentionally by a mis-click (layout shift) before the cap was raised; it stayed under the $0.50 cap.
Other API-origin runs on this account (6+ during session, ~$0.04 charged, 0-1 results) were NOT started by this session.

## Results
- Total public videos: 66 (29 long-form + 37 Shorts); channelTotalVideos=66 confirmed in all 66 rows; ids unique, all single channelId.
- Registry holds 56; all 56 present in pilot 2; 10 NEW (published up to 2026-11-02): -Nsa1XSR3Ww -fY4QrGAlrY 7pM3KcBjdtk 8ADAYc67kSE 8sSZGR75QI8 95hFygsos1o VfIjpMVClGA jaz-iYzpOfI sBi5nhTtUQ8 zP9mqinzN98
- Metadata fields present 66/66: id,title,url,date,duration,viewCount,likes,commentsCount,text,thumbnailUrl,channelId.
- Captions (10 new, SRT with timestamps): 8 user_generated, 2 auto_generated, 10/10 en. Registry's 56: 31 user, 12 auto, 13 type-unrecorded; all have text but PLAINTEXT (no timestamps).
- Not verified: caption availability for the 56 already-held videos in timestamped form (not re-fetched).

## Cost of complete timestamped acquisition (66 videos)
- Existing-caption download is free: run DS-000032 billed 56 'result' events only ($0.224), transcribeMinute=0.
- Full timestamped SRT for all 66 = 66 x $0.004 = $0.264 (new 10 already done: $0.040 -> remaining 56 = $0.224).
- Videos with no captions would need speech-to-text: $0.048 per started minute (not needed so far; none observed missing).
- Nothing further launched; awaiting approval.

Files: pilot1/ pilot2/ pilot3_subtitles/ each with dataset.json + dataset.sha256 (raw Console exports, unmodified).
Canonical DB and repo untouched.
