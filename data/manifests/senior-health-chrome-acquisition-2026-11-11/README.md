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

## Addendum — Registry (September-snapshot) channels refreshed to 2026-11-11

Method: Chrome (logged-out-equivalent public pages), $0, no Apify. Each channel's /videos page was read newest-first and diffed by video ID against the 7 registry channels in `01-unified-video-table.csv` (batch `B_REGISTRY_SEP`). Only IDs not already present were collected (metadata from `ytInitialPlayerResponse`, likes label, UI transcript panel — YouTube's new `transcript-segment-view-model` element). Output: `REGISTRY_CHANNELS_INCREMENTAL_NEW_VIDEOS.jsonl` (46 new videos; none duplicate existing IDs).

| Channel | Registry (Sep) | New videos | New with transcript | New publish range |
|---|---|---|---|---|
| Senior Health Hub | 122 | 5 | 5 | 2026-09-23..2026-10-06 |
| Better Health While Aging | 98 | 2 | 2 | 2026-10-12..2026-10-30 |
| Dr. Okoro | 66 | 0 | - | none since 2026-07-20 (inactive) |
| Dr. Ares Senior | 35 | 12 | 12 | 2026-09-21..2026-10-28 |
| Dr. Aliza Wright | 32 | 3 | 3 | 2026-11-02..2026-11-05 |
| Dr. Elias Senior Health | 29 | 24 | 23 | 2026-09-10..2026-11-04 |
| Doctor Thomas | 22 | UNAVAILABLE | - | channel page empty; sampled video `fj4TaPrLl8U` reports "removed for violating Terms of Service" (channel likely terminated; other 21 videos not individually checked) |

Limits (NOT VERIFIED / not done):
- Views/likes of the ~404 older registry videos were NOT refreshed (still Sep values); only new videos carry Nov values.
- BHWA/Hub Shorts tabs were not enumerated; only the /videos tab was diffed. Only the first ~30–53 newest items per channel were loaded (enough to reach known IDs on every channel except where noted).
- `cwgUAeZWydc` (Elias): transcript panel empty after 2 attempts; metadata present.
- Not merged into `01-unified-video-table.csv` or Reports 1–6; earlier conclusions unchanged.
