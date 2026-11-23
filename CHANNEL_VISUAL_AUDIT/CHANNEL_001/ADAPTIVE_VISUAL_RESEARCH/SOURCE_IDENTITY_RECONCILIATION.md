# Source identity reconciliation

The baseline had 179 ID-linked physical rows and 178 distinct public IDs. Archived metadata matching corrected the Video006 prefix and supplied or confirmed links using exact normalized titles or a unique SnapYT prefix, matching channel ID, format, and duration within two seconds. Such a link is metadata-supported. Its SHA remains the identity of the local binary. Existing trusted joins remain preferred.

Five otherwise excluded candidate collisions were compared to an already SHA-linked file at nominal 7, 23 and 43 seconds. Run `ffmpeg -ss TIME -i INPUT -frames:v 1 -vf scale=56:100,format=gray -f rawvideo -` for both. Compute mean absolute luma difference across the 5,600 bytes. This samples visual equivalence as supplementary title and duration evidence. It does not prove frame-identical or full audiovisual equality. Pairs are recorded in TRANSCODE_IDENTITY_SAMPLES.csv. The distinct encodings remain separate physical and hash records.

At closure 213 of 216 physical rows are linked to 207 distinct public IDs, with 215 distinct SHA-256 values across all physical files. Three files are unresolved: `58-More-Home-SnapYT.App.mp4`, `Home-Prices-Are-SnapYT.App.mp4` and `It-Was-Supposed-SnapYT.App.mp4`. The archived metadata did not yield a usable unique title-and-duration match. The unresolved rows remain usable for local visual research by hash. No guessed public accession is assigned.

Input snapshot and operation are identified in `reconcile_metadata.py` and the continuation checkpoint. Inventory tier and analysis depth remain independent of all identity joins.
