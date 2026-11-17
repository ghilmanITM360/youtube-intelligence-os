# YIOS Batch28 verified recovery receipt

Status VERIFIED. Uploaded bytes: 2,820,652; complete independently retrieved SHA-256 verified bytes: 2,820,652. Source mappings: 1.

All-in physical uploaded bytes before this MD: 4,822,914,968; independently verified bytes: 4,822,914,968. This MD is additional payload, counted by its separate CONTROL-UPLOAD/VERIFY receipts after complete independent readback. No duplicate/partial I/O is counted as new recovery coverage.

Authenticated owner kgk2930@gmail.com; approved private yios hierarchy. Actual namespace IDs, source paths, hashes, bytes and remote object IDs follow. Source stability and current owner/private/parent/size gates passed. No source deletion/move/cleanup, Git/PR/branch/stash/LFS/production mutation, payment or reset credit use by this backup. This is file-level cloud recovery; independent-machine disaster recovery and production ownership acceptance remain unproven.

```json
{
  "receipt": {
    "status": "VERIFIED",
    "batch": 28,
    "completed_utc": "2026-10-26T15:44:30.033813+00:00",
    "files": [
      {
        "source_absolute": "/Users/ghilmankhan/workprojects/video data of what if/video_forensics_output/what_if_the_moon_were_made_of_protons/00_source/audio/audio.wav",
        "restore_relative": "machine-a/workprojects/video data of what if/video_forensics_output/what_if_the_moon_were_made_of_protons/00_source/audio/audio.wav",
        "root": "/Users/ghilmankhan/workprojects/video data of what if",
        "kind": "regular",
        "bytes": 2820652,
        "allocated_path_bytes": 2822144,
        "mtime_ns": 1789553513000000000,
        "device": 16777229,
        "inode": 73029048,
        "nlink": 1,
        "sha256": "",
        "hash_status": "HASH_REQUIRED_BEFORE_TRANSFER",
        "object_key": null,
        "priority": "A_EVIDENCE",
        "provenance": "Phase 0 inventory + bounded known-root name/stat reconciliation 2026-10-25T23:56:39.325995+05:00",
        "publication": null,
        "binary_restore_status": "COMPLETE_REMOTE_BYTES_SHA256_VERIFIED",
        "upload_status": "UPLOADED_AND_VERIFIED",
        "actual_reclaimable_bytes": null,
        "backup_priority": "A_ORIGINAL_MEDIA",
        "rank": 0,
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "existing_remote_mapping": null,
        "verification_status": "HASH_REFRESH_REQUIRED",
        "sequence": 465,
        "proposed_destination_name": "00465__audio.wav",
        "fresh_stat": {
          "st_size": 2820652,
          "st_mtime_ns": 1789553513000000000,
          "st_ctime_ns": 1790005150016708571,
          "st_ino": 73029048,
          "st_dev": 16777229
        },
        "fresh_sha256": "0d42d9e1101ebc0193a432fca95e269bd16356d407ca24b40e6a9f798fd3c296",
        "hash_refreshed_utc": "2026-10-26T15:43:06.397278+00:00",
        "status": "VERIFIED",
        "remote_id": "1FDjx076px2wfnvwGqlufq3J_0RgMAIhF",
        "remote_url": "https://drive.google.com/file/d/1FDjx076px2wfnvwGqlufq3J_0RgMAIhF/view?usp=drivesdk",
        "upload_utc": "2026-10-26T15:44:00.991800+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1FDjx076px2wfnvwGqlufq3J_0RgMAIhF",
            "title": "audio.wav",
            "mime_type": "audio/wav",
            "size": "2820652",
            "url": "https://drive.google.com/file/d/1FDjx076px2wfnvwGqlufq3J_0RgMAIhF/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1FDjx076px2wfnvwGqlufq3J_0RgMAIhF/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T15:43:38.777Z",
            "modified_time": "2026-09-16T10:11:53.000Z",
            "parent_ids": [
              "14xZh95QcbVGOq9waETS11XFAGnKa48Dw"
            ],
            "drive_id": null,
            "current_user_can_share": true,
            "has_augmented_permissions": null,
            "shared": false,
            "permissions": [
              {
                "type": "user",
                "role": "owner",
                "emailAddress": "kgk2930@gmail.com",
                "domain": null,
                "displayName": "Ghilman khan",
                "allowFileDiscovery": null
              }
            ],
            "source_visibility_status": "permission_metadata_available"
          }
        },
        "retrieval": {
          "sequence": 465,
          "remote_id": "1FDjx076px2wfnvwGqlufq3J_0RgMAIhF",
          "retrieval_file_id": "sediment://file_0000000035a881faa6d078a6e34ee1e8",
          "metadata": {
            "id": "1FDjx076px2wfnvwGqlufq3J_0RgMAIhF",
            "title": "audio.wav",
            "mime_type": "audio/wav",
            "size": "2820652",
            "url": "https://drive.google.com/file/d/1FDjx076px2wfnvwGqlufq3J_0RgMAIhF/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1FDjx076px2wfnvwGqlufq3J_0RgMAIhF/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T15:43:38.777Z",
            "modified_time": "2026-09-16T10:11:53.000Z",
            "parent_ids": [
              "14xZh95QcbVGOq9waETS11XFAGnKa48Dw"
            ],
            "drive_id": null,
            "current_user_can_share": true,
            "has_augmented_permissions": null,
            "shared": false,
            "permissions": [
              {
                "type": "user",
                "role": "owner",
                "emailAddress": "kgk2930@gmail.com",
                "domain": null,
                "displayName": "Ghilman khan",
                "allowFileDiscovery": null
              }
            ],
            "source_visibility_status": "permission_metadata_available"
          },
          "started_utc": "2026-10-26T15:44:05.792653+00:00",
          "retrieved_bytes": 2820652,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "2820652",
          "retrieved_sha256": "0d42d9e1101ebc0193a432fca95e269bd16356d407ca24b40e6a9f798fd3c296",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T15:44:08.112757+00:00"
        }
      }
    ],
    "uploaded_bytes": 2820652,
    "independently_retrieved_bytes": 2820652,
    "mapped_source_files": 1,
    "selection_amendment": null,
    "preflight": {
      "account": "kgk2930@gmail.com",
      "privacy": "OWNER_ONLY",
      "five_hour_used": 81,
      "weekly_used": 19,
      "paid_credits": "0",
      "observed_at": "2026-10-26T15:43:06.232Z",
      "ui_used_gb": 5.29,
      "storage_ui": "5.29GB of15GB; fresh authenticated Google One UI; Drive4.99GB Gmail302.23MB",
      "conservative_free_bytes": 9219905751,
      "mac_free_bytes": 18977239040,
      "context": "Adequate context after checkpoint read; exact context meter unavailable. No unfinished batch.",
      "ownership": "No active backup helper identified; live protected Claude process preserved; other preservation chat notLoaded; no writer takeover.",
      "charges": "Existing storage allowance, no purchases/payment/reset credits"
    },
    "postflight": {
      "batch_dir": "/Users/ghilmankhan/YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd/batch-0028",
      "account": "kgk2930@gmail.com",
      "privacy": "OWNER_ONLY",
      "five_hour_used": 84,
      "weekly_used": 20,
      "paid_credits": "0",
      "observed_at": "2026-10-26T15:44:29.910Z",
      "ui_used_gb": 5.29,
      "storage_ui": "5.29GB of15GB; fresh authenticated Google One UI; Drive4.99GB Gmail302.23MB",
      "conservative_free_bytes": 9219905751,
      "mac_free_bytes": 18981806080,
      "context": "Adequate context after checkpoint read; exact context meter unavailable. No unfinished batch.",
      "ownership": "No active backup helper identified; live protected Claude process preserved; other preservation chat notLoaded; no writer takeover.",
      "charges": "Existing storage allowance, no purchases/payment/reset credits",
      "destination_folder_id": "14xZh95QcbVGOq9waETS11XFAGnKa48Dw"
    },
    "permissions": "Owner-only Restricted; no changes",
    "encryption": "Google provider managed; owner-held client key not established",
    "retention": "Until explicit owner removal approval",
    "coverage": "File-level verified recovery only; no complete-package or independent-machine recovery claim"
  },
  "recovery_mapping": {
    "files": [
      {
        "source_absolute": "/Users/ghilmankhan/workprojects/video data of what if/video_forensics_output/what_if_the_moon_were_made_of_protons/00_source/audio/audio.wav",
        "restore_relative": "machine-a/workprojects/video data of what if/video_forensics_output/what_if_the_moon_were_made_of_protons/00_source/audio/audio.wav",
        "bytes": 2820652,
        "fresh_sha256": "0d42d9e1101ebc0193a432fca95e269bd16356d407ca24b40e6a9f798fd3c296",
        "remote_id": "1FDjx076px2wfnvwGqlufq3J_0RgMAIhF",
        "remote_url": "https://drive.google.com/file/d/1FDjx076px2wfnvwGqlufq3J_0RgMAIhF/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      }
    ]
  },
  "cumulative_before_this_control": {
    "mapped_source_paths": 473,
    "uploaded_bytes_including_controls": 4822914968,
    "verified_bytes_including_controls": 4822914968,
    "remaining_payload_bytes": 7177085032,
    "remaining_plan_files": 79
  }
}
```
