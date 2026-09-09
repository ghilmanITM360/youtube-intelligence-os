# CH-000004 Packaging Intelligence — Step 17B

This versioned successor preserves the original Step 17A pilot. It adds current remote thumbnail snapshots and revalidates visual hypotheses. It does not assert publication-time or metric-observation-time packaging.

# Thumbnail Acquisition

| Measure | Result |
|---|---:|
| Registered URLs | 83 |
| Attempted | 83 |
| Valid decoded images | 83 |
| Failed downloads | 0 |
| Invalid images | 0 |
| Unique SHA-256 binaries | 83 |
| Duplicate hash groups | 0 |
| Long-form | 43 |
| Shorts | 40 |

Acquisition fetched only URLs already registered in canonical `thumbnail_evidence` for CH-000004. No crawling, discovery, YouTube API, or Apify call occurred. Raw binaries use content-addressed, gitignored storage. Durable provenance is in `data/manifests/DS-000017-thumbnail-snapshot-2026-09-09.json`.

# Temporal Evidence Limitations

All 83 images are `CURRENT_REMOTE_SNAPSHOT`. Historical binaries verified: 0. Title records were observed on 2026-08-28; thumbnails were retrieved on 2026-09-09. Every joined package is therefore `CURRENT_THUMBNAIL_WITH_CANONICAL_TITLE` with `TEMPORAL_ALIGNMENT_UNKNOWN`.

Current thumbnail state may be described alongside a video's historical public-performance observation. It cannot be credited with causing that performance.

# Thumbnail Observations

Measured metadata: 82 images are 1280×720; one Shorts image is 405×720. Formats: 82 JPEG and one AVIF. Total accepted payload: 5,890,738 bytes. Every accepted file has non-zero dimensions, decoded successfully, and has a SHA-256.

AI visual review covered all 83 images using six contact sheets. All visual judgments are `AI_INTERPRETATION`; no OCR was used.

| Observation | Items |
|---|---:|
| Illustration style | 83 |
| Text visible | 55 |
| Diagram style | 56 |
| Single hero | 30 |
| Multi-object | 53 |
| Extreme-scale visual | 39 |
| Consequence scene | 38 |
| Comparison layout | 7 |
| Explicit split layout | 2 |

# Thumbnail Archetypes

| ID | Pattern | Items | Format | Finding |
|---|---|---:|---|---|
| THUMB-ARCH-001 | Branded single-scene xkcd illustration | 43 | Long-form | Observed common |
| THUMB-ARCH-002 | Vertical animation excerpt | 40 | Shorts | Observed common; surface-dependent |
| THUMB-ARCH-003 | Labeled scale or diagram | 39 | Mixed | Observed common |
| THUMB-ARCH-004 | Consequence scene | 38 | Mixed | Observed common |
| THUMB-ARCH-005 | Contrast or split comparison | 7 | Mixed | Observed rare; only 2 explicit splits |

These are current visual associations. Winner status is not inferred.

# Title–Thumbnail Pair Analysis

| Relationship | Items |
|---|---:|
| Thumbnail adds scale | 33 |
| Title adds stakes | 21 |
| Thumbnail adds concrete object | 17 |
| Contrast pair | 6 |
| Redundant | 6 |

Verified historical pairs: 0. Temporally uncertain pairs: 83. Pair classes describe current thumbnails joined to canonical title snapshots, not verified historical upload packages.

# Provisional Archetype Revalidation

| Prior archetype | Result | Reason |
|---|---|---|
| PKG-ARCH-001 | CONFIRMED_BY_VISUAL_EVIDENCE | Single-hero and labeled-scale visuals recur across both formats. |
| PKG-ARCH-002 | PARTIALLY_CONFIRMED | Comparison exists, but explicit splits are rare and performance alignment is unknown. |
| PKG-ARCH-003 | PARTIALLY_CONFIRMED | Feasibility titles currently pair with concrete scale visuals; format and temporal limits remain. |
| PKG-ARCH-004 | REVISED | Single consequence scenes recur; multi-stage consequence chains do not. |

# Opportunity Package Revalidation

All 15 original packages remain `HYPOTHESIS_FOR_TESTING`.

| Result | Packages |
|---|---:|
| SUPPORTED_BY_CHANNEL_VISUAL_EVIDENCE | 13 |
| PLAUSIBLE_BUT_UNOBSERVED | 2 |
| CONTRADICTED_BY_CHANNEL_PATTERN | 0 |
| INSUFFICIENT_EVIDENCE | 0 |

Single-hero/scale and comparison concepts have channel precedents. Two consequence-chain concepts remain plausible but unobserved as multi-stage layouts. Exact package-level rationale and canonical video support are recorded in v2 JSON.

# Shorts vs Long-Form Findings

Long-form current snapshots consistently use wide xkcd illustrations with a red `what if?` badge. Shorts primarily use vertical animation excerpts; 39 of 40 retrieved URLs returned 1280×720 canvases containing vertical material, while one returned native 405×720.

Current YouTube Help confirms Shorts custom-thumbnail support on eligible verified accounts, while display differs by surface. Native title/thumbnail A/B testing excludes Shorts. Thumbnail availability does not establish Shorts-feed ranking impact.

# What We Still Cannot Infer

- Which thumbnail existed at publication or metric observation.
- Historical causal effects on views, watch time, CTR, retention, or satisfaction.
- Transfer from long-form packaging to Shorts, or vice versa.
- A winning package before a native concurrent test.
- Exact thumbnail text where too small to inspect; no OCR claims were added.

Official guardrails: [content performance](https://support.google.com/youtube/answer/16559650), [custom thumbnails](https://support.google.com/youtube/answer/72431), and [native A/B testing](https://support.google.com/youtube/answer/16391400).

# Packaging Intelligence Verdict

`WORKING_FOR_CURRENT_VISUAL_PATTERN_ANALYSIS`

Historical causal package analysis: `NOT_SUPPORTED`.
