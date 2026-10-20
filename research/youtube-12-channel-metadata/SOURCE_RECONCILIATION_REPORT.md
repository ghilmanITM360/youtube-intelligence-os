# Twelve-channel source reconciliation

Snapshot completed at 2026-10-20T07:54:15.819Z using `streamers/youtube-scraper` build `0.0.318`.

## Acquisition

- Pilot: run `sITkppEYgnOijb9Oz`, dataset `9wMPVD6GcfyqlLsXs`, cost $0.012.
- Identity sweep: run `c2ohHxnXWxULA6vdT`, dataset `XofPEGRTaJo0ils7c`, cost $0.144.
- Full sweep: run `dVdEwIBncKCxyZCEU`, dataset `5aiVNFBbrGdiKajXc`, cost $1.856.
- Total new spend: $2.012. The full run used one in-place resurrection after the initial 600-second timeout and ultimately succeeded with zero failed requests.
- Paid transcripts, AI summaries, AI descriptions, video analysis, and comment scraping were disabled.

## Reconciliation

- Requested targets: 12; exact identities resolved: 12.
- Raw full-run rows: 464.
- Unique accessible public videos: 445.
- Regular videos: 371; Shorts: 74; streams: 0.
- Explicit members-only exclusions: 0.
- Cross-channel duplicate video IDs: 0.
- Eleven channels exactly match their Actor-reported channel upload count.
- `@unclejohnfinancial` reports 56 uploads but returned 53 accessible public records. The three-item difference remains unresolved and is not treated as captured public content.

All mutable metrics are point-in-time snapshots. Thumbnail URLs were retained without downloading binaries. Transcript and caption counts reflect only metadata emitted automatically while transcript acquisition was disabled.
