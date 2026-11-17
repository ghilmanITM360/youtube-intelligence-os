- **Decode correction.** The first decode inserted one duplicate frame near f100 (3,026 vs 3,025 native frames) because ffmpeg's default frame-rate mode normalised an irregular timestamp; the pipeline now decodes with `-fps_mode passthrough` and this video was re-analysed; all frame numbers in the tables are native (`MEASURED`, QA check `decoded_frames_equal_ffprobe_frames`).
- **Layout.** 720p source. A two-line burned-in title ('the world's safest market is breaking') is present only for the first 6 s (f0-188), unlike the full-duration headline of `Qof71Ef-3EU` and `DEgQTSsSX9U`; after that the frame is full-bleed with hand-lettered captions (`DIRECTLY_OBSERVED`).
- **Sparse white compositions.** Scene changes replace small objects on white, so only ~7 % of the frame changes at a cut (versus 25-60 % on screenshot-heavy Shorts); the per-video cut/pop thresholds are therefore relative (`MEASURED`).
- **Meme and brand imagery.** A meme photograph ('Coincidence?' then 'I THINK NOT!', zoomed), the Avengers logo and the OECD logo carry jokes and authority beats; rights status unverified.
- **Reuse across videos.** The pension card with green check, bond tags, '?' circle, detective figure, blackboard presenter and the Earth with eyes recur from `DEgQTSsSX9U` and `Qof71Ef-3EU`; this video is a re-edit of the pension theme with 6 added country charts (`DIRECTLY_OBSERVED`).
- **No screen recording or generated motion identified.**

## Uncertainties (DEPTH_C)
41 detected changes (chart appearances, small slides, caption-chunk growth) are kept as UNRESOLVED_CHANGE rows and not classified; of the three event sheets only the first two were viewed; caption timing not measured; creator tools unknown; no listening; single reviewer.
