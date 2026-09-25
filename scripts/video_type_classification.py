"""Normalize raw `videos.video_type` source values into one analytical taxonomy.

The registry stores whatever raw type string each acquisition pipeline produced
(Apify `content_type`, historical-catalog imports, supplied workbooks). Those
raw values are never rewritten — they are the source record. This module only
maps them to a consistent read-time classification for reporting/aggregation.
"""

REGULAR = "REGULAR"
SHORT = "SHORT"
STREAM = "STREAM"
UNKNOWN = "UNKNOWN"

_REGULAR_RAW = {"video", "regular video", "regular"}
_SHORT_RAW = {"short", "shorts"}
_STREAM_RAW = {"live", "livestream", "stream", "streams"}


def classify_video_type(raw_video_type) -> str:
    """Map a raw source `video_type` value to REGULAR/SHORT/STREAM/UNKNOWN."""
    normalized = str(raw_video_type or "").strip().lower()
    if normalized in _REGULAR_RAW:
        return REGULAR
    if normalized in _SHORT_RAW:
        return SHORT
    if normalized in _STREAM_RAW:
        return STREAM
    return UNKNOWN
