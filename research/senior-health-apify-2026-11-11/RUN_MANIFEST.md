# Senior-health Apify acquisition, 2026-11-11

- Source: owner-supplied list of 24 handles (22 unique); resolved to 21 distinct channel IDs by public channel page. Dr. Elias Senior Health (UCQcBYZxFW7YwNMU8-DsT3Uw) skipped: already in the canonical registry. Two input handles were duplicates of each other.
- Actor: streamers/youtube-scraper build 0.0.332, $0.004/result, subtitles/AI/transcripts OFF, regular videos only (Shorts/streams limit 0). Run through the signed-in Apify Console (account gullu); no API token read or stored.
- Run 1 QSwBSjJff8yJXnnNK: 21 channels, limit 50 each, 460 rows, $1.840 (cap $4.30).
- Run 2 ffSoyEykFOE9HdWax: top-up for Dr. Waterling and Vital Years Wellness (limit 200), 141 rows, $0.564 (cap $1.00). Overlaps run 1; deduped by video id, later run wins.
- Total charged $2.404; 501 unique videos, 21 channels, all COMPLETE vs channelTotalVideos.
- Dr. Waterling (UCLVvBoF...) was previously metadata-only in DS-000034 (71 records) and screenshot-only SUBJ; this is the first full Apify capture.
- Raw datasets are immutable under raw/ (SHA-256 in SHA256SUMS.txt). senior_health_apify.db is derived (tables runs/channels/videos; videos.raw_json holds the full row). Rebuild: python3 -I build_outputs.py.
- NOT done: canonical registry DB (data/catalog/youtube_channel_registry.db) not modified; it is rebuilt from manifests by scripts/build_youtube_channel_registry.py and needs an approved registration step.
