# Senior Health — Chrome-based acquisition (2026-11-11)

Method: public YouTube pages in a normal Chrome session (no Apify, no YouTube API, $0 spend, no sign-in used).
- Video list: channel /videos tab, scrolled until fully loaded.
- Metadata: `ytInitialPlayerResponse` of each watch page (title, description, duration, views, keywords, category, publish date, thumbnail URL, caption-track list).
- Transcript: YouTube "Show transcript" panel (timestamp m:ss + text). Auto-captions (ASR) where caption track kind = asr.
- Failed approaches (not used): direct `timedtext` caption URL (empty body), `youtubei/v1/get_transcript` (HTTP 400 precondition failed).
Local-only helper: a loopback receiver wrote raw per-video JSON to a scratchpad (not committed).

## Results
| Channel | ID | Videos collected | Transcripts | Status |
|---|---|---|---|---|
| Doctor Laura (@DoctorLaura-e1w1o) | UCBLbqhYNAve3LmpThhB4OXA | 67 / 67 (matches probe) | 63 | COMPLETE for metadata; 4 transcripts PANEL_EMPTY (asr track exists, UI panel did not render; retryable) |
| Neal K. Shah (@nealkshah) | UChy5xzO6JM4v221lU4Z0hpw | 146 long-form of 913 reported (547k subs) | 0 (not attempted) | PARTIAL metadata only |

PANEL_EMPTY videos: VFQ83cfPhus, sXXGA2oHx1g, et6XTfv-wQE, zMv12xxy4TU.

## Limits (UNAVAILABLE, not invented)
- Likes: 1 of 67 captured (aria-label not reliably present) → `likes` null otherwise. Comment counts not collected.
- Neal K. Shah: 913 videos reported includes Shorts; only the loaded long-form list (146, 2026-05-08 → 2026-11-09) was collected. Shorts tab and older long-form not collected.
- Doctor Laura latest upload 2026-07-09 (inactive ~4 months at collection).
- Views are public counts at collection time (`collected_at`), single snapshot.
- Not run: Alan A.M (no URL), 4th missing channel of "26" (no record), 7 September-snapshot channels refresh, 8 legacy videos (IDs never identified).
- Doctor Laura / Neal K. Shah NOT yet merged into Reports 1-6 or `01-unified-video-table.csv`; earlier conclusions unchanged.

## Validation
No duplicate video IDs; all Doctor Laura rows have the expected channel_id; all Neal rows share one channel_id; 0 fetch errors.
