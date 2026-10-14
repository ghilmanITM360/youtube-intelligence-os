# Final QA and limitations register

| Area | Status | Limitation / remaining work |
|---|---|---|
| Source identity | 11/11 hash-verified | Japan, 2008 and GD were re-hashed this session; the other eight reuse earlier verification. Full decode integrity is not certified because H.264 `mmco` seek warnings appeared in multiple videos. |
| Structural packages | 11/11 PASS | Historical six use candidate-state segmentation. Research five use 4 s point samples plus temporal sequences. The two methods differ, so their coverage is not equivalent. |
| Shot/state census | NOT_CERTIFIED | Fixed sampling misses short states (e.g. JPN 570 "underground city" and 666 "4.25%" were found only in sequences). |
| Motion | PARTIAL | 160 research sequences plus historical animation reviews. Easing, exact onset, keyframe values and software are UNKNOWN. Motion recipes are inferred. |
| Independent visual QA | NOT_PERFORMED | Single primary agent reviewed everything at contact-sheet scale. |
| Audio | SIGNAL_ONLY | No direct listening. Narration content is ASR_INFERRED. Music is SOURCE_DECLARED. SFX, pauses and sync are unverified. |
| Full AV sign-off | 0/11 | Needs continuous playback and listening. |
| Financial claims | PARTIAL | Claim registers exist per video. Only targeted checks were done (historical six, plus "widely documented" notes). HIGH_PRIORITY_CHECK items remain open (e.g. JPN palace > California, JAL landholdings; C08 12:1 leverage; GD 25-country list, trade pies, -90% vs -70% labels). |
| Thumbnails | Current CDN only | Upload-time thumbnails are not certified. Mobile legibility was tested for the historical six only. |
| Performance | Public counts only | Greece current views UNAVAILABLE (LOGIN_REQUIRED). Recent views/day is based on a 2.36-day gap and is noisy. Private analytics are UNKNOWN. |
| Google Trends | Collected | One search term per topic; normalized 0–100 per request; low-volume series contain zeros or INSUFFICIENT_DATA (Japan web, Norway YouTube). Worldwide only. |
| News | Partial | A dated credible event was found only for the GD window. Other windows: none found. |
| Channel DNA / blueprint | COMPLETE | Based on sampled evidence. Asset counts are design families, not file counts. The blueprint forbids copying source artwork. |
| Git | See git log | No MP4s or bulk frames committed. Scratch frames are kept locally at `~/Documents/Codex/2026-10-14/.../work/<video_id>/`. |
