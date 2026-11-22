# V1 Rent segment 0-75 s: QA report (final = r3)
File: out/V1_RENT_segment_0-75s_take2.mp4, sha256 a40bbccc147368b49c7af10060c537225f4f6c1c1d25fb8e83ec8ba74577516c (also out/V1_RENT_segment_0-75s_take2.sha256). Earlier: _r1, _r2 kept.
Mechanical (Claude): H.264 1920x1080 30 fps, 2250 frames, 75.000 s, AAC 48 kHz mono; full ffmpeg decode no errors; audio vs Take 2 source lag 0 ms, corr 0.99999; no zero-motion second; max frame diff 1.81 (no jump cuts).
Independent read-only visual QA (separate reviewer agent, 2026-11-21): PASS WITH ISSUES, no critical defects, numbers 2.8/2.7/7.7/25.9/35.3 correct, sync within about 0.3-0.6 s of spoken words.
Open issues (not fixed, no further render by owner instruction):
1. Medium: source lines and bar labels barely legible at 390 px phone width (legible at 1080p).
2. Medium: counters pass through wrong intermediate values (about 0.7 s count-up); final value lands 0.3-0.6 s after the word.
3. Low: value labels tight to labels above; hard-cut pose swaps with a few px head shift; label/bar leads the word by about 0.4 s at 7.7% and 25.9%.
Ownership: remote check clean; Machine B unobservable; proceeded on owner direction (WRITE_CLAIM_V1_RENT.md).
Not covered: no lip sync (single closed-mouth pose), no real BLS/Zillow screenshots, narration after 122.7 s unsupported (separate publishing blocker). Nothing committed or pushed.
