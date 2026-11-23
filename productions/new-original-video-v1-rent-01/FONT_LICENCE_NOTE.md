# Font licence check (2026-11-21)
- Marker Felt and Chalkboard SE: Apple system fonts. Their name tables carry only "Copyright 2003-10 Apple Computer, Inc." with no embedded licence; use is governed by the macOS software licence, which does not clearly allow redistribution in published video. Treated as NOT cleared. Removed from the renderer.
- Replacement (SIL Open Font License 1.1, texts kept beside the files in `v1r4_assets/fonts_ofl/`, SHA-256 in `SHA256.txt`, fetched from the google/fonts repository): Patrick Hand (labels and numerals), Caveat Brush (display words). Kalam Bold was tested and not used.
- Source tags: Helvetica (Apple system font). Same caveat applies; swap to Patrick Hand or another OFL sans before publication if the owner wants a fully cleared set. Numeral readability: Patrick Hand's 7 has a crossbar and reads clearly at 640 px width (checked on phone-size frames).
- This is a practical check, not legal advice.
