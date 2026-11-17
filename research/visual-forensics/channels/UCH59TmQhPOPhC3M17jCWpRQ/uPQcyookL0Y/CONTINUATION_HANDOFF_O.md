# Barely Evolved uPQcyookL0Y checkpoint O — PARTIAL

Earlier handoffs (L/M/N) preserved unchanged.

```json
{
  "status": "PARTIAL",
  "video_id": "uPQcyookL0Y",
  "checkpoint": "O",
  "parent": "76b1e2a378e1d803dc3cbf1987c8400f5bbd1367",
  "art": {
    "states_with_native_art_audit": 89,
    "of": 89,
    "mode": "sparse native representatives (2-4 per state)",
    "W041_W088_intra_state_motion_strips": "68 measured-peak strips reviewed (8 consecutive frames each)",
    "W001_W040_motion_strips": "generated (59), review in progress by reviewer_22/23 \u2014 NOT in O"
  },
  "narration": {
    "segments_with_partial_visual_assessment": "0-75 (76/76)",
    "qualification": "SPARSE_PARTIAL_ASR_ONLY_NOT_LISTENED",
    "full_audio_verified_segments": 0,
    "preserved_uncertainties": "8,11,22; seg25 head/tail; seg27 primary supplement; seg0 primary adjudication; seg4 MIXED_PARTIAL; reviewer15 corrections 18/19",
    "new_open_items": "seg67 ocean insert vs ASR rivers (unresolved); W085b fade-out not seen in strip f14026-14033"
  },
  "boundaries": {
    "states": "v6 unchanged 89 contiguous, 14647 frames",
    "new_unresolved_candidate": "UBC-001 W062 f10316->10317 discontinuity (tables/o_primary_corrections.csv)"
  },
  "state_prompts": {
    "W051_W088": 39,
    "W001_W050": "PENDING (reviewer_22/23)"
  },
  "asset_crosswalk": "m_asset_alias_crosswalk.csv unchanged; reviewers17-21 raw IDs preserved, cross-reviewer reconciliation PENDING",
  "production_specs": "production_specifications v1 (3 scoped drafts) unchanged; v2 PENDING",
  "actual_listening": "BLOCKED_CAPABILITY (../AUDIO_LISTENING_CAPABILITY_2026-11-03.json)",
  "reconstruction_test": "NOT_RUN",
  "review_relationship": "reviewers17-21 = Claude sonnet subagents; orchestrator Claude opus-5-5; same vendor; no human review; primary spot checks on 3 batches (tables/o_primary_corrections.csv, o_reviewer_*_provenance.json)",
  "validation": "o_validation_reviewer_*.json all errors=[] (coverage, sha256, witness, locator, in-segment time \u00b10.2s); sequential decode mismatches 0 for all batches",
  "resources": {
    "utc": "2026-11-03T17:18:37.671431+00:00",
    "five_hour": "UNKNOWN (no readable meter: Chrome extension disconnected; no CLI meter)",
    "weekly": "UNKNOWN",
    "paid_or_reset_credits_used": 0,
    "reviewer_tokens_this_session": {
      "r17": 171220,
      "r18": 163166,
      "r19": 160577,
      "r20": 188626,
      "r21": 173483
    },
    "disk_free": "/dev/disk3s5   460Gi   332Gi    95Gi    78%    4.1M  993M    0%   /System/Volumes/Data",
    "memory": "System-wide memory free percentage: 39%"
  },
  "CT_SCAN_COMPLETE": false,
  "next_operation": "validate reviewer_22/23 (strips W001-W040, prompts W001-W050) -> asset crosswalk extension -> production specs v2 + blueprint v2 -> bounded reconstruction test; videos mNLNb-Z4T0M (ingested, 145 boundary candidates) and GNaBxt_zIRA (ingest running)"
}
```

Workspace: /Users/ghilmankhan/YIOS-local-audits/barely-evolved/2026-11-02-uPQcyookL0Y-deep-ct-scan
Branch research/barely-evolved-visual-forensics; publication via external GIT_INDEX_FILE + commit-tree, normal push; canonical checkout untouched. Lock: ~/YIOS-local-audits/barely-evolved/.be_writer_lock (session 7a28d062).
