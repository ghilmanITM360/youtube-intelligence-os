# YIOS Batch25 verified recovery receipt

Status VERIFIED. Uploaded bytes: 57,205,534; complete independently retrieved SHA-256 verified bytes: 57,205,534. Source mappings: 2.

All-in physical uploaded bytes before this MD: 4,803,237,801; independently verified bytes: 4,803,237,801. This MD is additional payload, counted by its separate CONTROL-UPLOAD/VERIFY receipts after complete independent readback. No duplicate/partial I/O is counted as new recovery coverage.

Authenticated owner kgk2930@gmail.com; approved private yios hierarchy. Actual namespace IDs, source paths, hashes, bytes and remote object IDs follow. Source stability and current owner/private/parent/size gates passed. No source deletion/move/cleanup, Git/PR/branch/stash/LFS/production mutation, payment or reset credit use by this backup. This is file-level cloud recovery; independent-machine disaster recovery and production ownership acceptance remain unproven.

```json
{
  "receipt": {
    "status": "VERIFIED",
    "batch": 25,
    "completed_utc": "2026-10-26T15:19:51.106640+00:00",
    "files": [
      {
        "source_absolute": "/Users/ghilmankhan/workprojects/video data of what if/video_forensics_output/weird_and_worrying_questions/00_source/audio/audio.wav",
        "restore_relative": "machine-a/workprojects/video data of what if/video_forensics_output/weird_and_worrying_questions/00_source/audio/audio.wav",
        "root": "/Users/ghilmankhan/workprojects/video data of what if",
        "kind": "regular",
        "bytes": 1520336,
        "allocated_path_bytes": 1523712,
        "mtime_ns": 1789555305000000000,
        "device": 16777229,
        "inode": 73031574,
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
        "sequence": 461,
        "proposed_destination_name": "00461__audio.wav",
        "fresh_stat": {
          "st_size": 1520336,
          "st_mtime_ns": 1789555305000000000,
          "st_ctime_ns": 1790005150060195359,
          "st_ino": 73031574,
          "st_dev": 16777229
        },
        "fresh_sha256": "faa95195032014766557a1e628ff41bd3cb7c94c515f645626c856cb5a6a6089",
        "hash_refreshed_utc": "2026-10-26T15:15:41.735535+00:00",
        "status": "VERIFIED",
        "remote_id": "1B5JjAc99wHCDK0IYxd8-zv0bler4clWp",
        "remote_url": "https://drive.google.com/file/d/1B5JjAc99wHCDK0IYxd8-zv0bler4clWp/view?usp=drivesdk",
        "upload_utc": "2026-10-26T15:17:45.122294+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1B5JjAc99wHCDK0IYxd8-zv0bler4clWp",
            "title": "audio.wav",
            "mime_type": "audio/wav",
            "size": "1520336",
            "url": "https://drive.google.com/file/d/1B5JjAc99wHCDK0IYxd8-zv0bler4clWp/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1B5JjAc99wHCDK0IYxd8-zv0bler4clWp/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T15:16:16.500Z",
            "modified_time": "2026-09-16T10:41:45.000Z",
            "parent_ids": [
              "198o_PWgjXwgUlczYhbe_IGEJroPCnBzo"
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
          "sequence": 461,
          "remote_id": "1B5JjAc99wHCDK0IYxd8-zv0bler4clWp",
          "retrieval_file_id": "sediment://file_00000000ab8481fa9c61d31b8d7ff4a9",
          "metadata": {
            "id": "1B5JjAc99wHCDK0IYxd8-zv0bler4clWp",
            "title": "audio.wav",
            "mime_type": "audio/wav",
            "size": "1520336",
            "url": "https://drive.google.com/file/d/1B5JjAc99wHCDK0IYxd8-zv0bler4clWp/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1B5JjAc99wHCDK0IYxd8-zv0bler4clWp/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T15:16:16.500Z",
            "modified_time": "2026-09-16T10:41:45.000Z",
            "parent_ids": [
              "198o_PWgjXwgUlczYhbe_IGEJroPCnBzo"
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
          "started_utc": "2026-10-26T15:17:51.730086+00:00",
          "retrieved_bytes": 1520336,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "1520336",
          "retrieved_sha256": "faa95195032014766557a1e628ff41bd3cb7c94c515f645626c856cb5a6a6089",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T15:17:56.317006+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/workprojects/video data of what if/video_forensics_output/what-if-earth-grew-1cm-every-second/05_audio/source_audio.wav",
        "restore_relative": "machine-a/workprojects/video data of what if/video_forensics_output/what-if-earth-grew-1cm-every-second/05_audio/source_audio.wav",
        "root": "/Users/ghilmankhan/workprojects/video data of what if",
        "kind": "regular",
        "bytes": 55685198,
        "allocated_path_bytes": 55689216,
        "mtime_ns": 1789558709000000000,
        "device": 16777229,
        "inode": 73027125,
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
        "sequence": 462,
        "proposed_destination_name": "00462__source_audio.wav",
        "fresh_stat": {
          "st_size": 55685198,
          "st_mtime_ns": 1789558709000000000,
          "st_ctime_ns": 1790005149987222236,
          "st_ino": 73027125,
          "st_dev": 16777229
        },
        "fresh_sha256": "dd05a0d2f3c66bf6442f23266c4f6bb488e629fb932052768807968ddd68bc61",
        "hash_refreshed_utc": "2026-10-26T15:15:41.770218+00:00",
        "status": "VERIFIED",
        "remote_id": "1uuP9kXah7Tk43n2mQ08kED5kgOnOMu_n",
        "remote_url": "https://drive.google.com/file/d/1uuP9kXah7Tk43n2mQ08kED5kgOnOMu_n/view?usp=drivesdk",
        "upload_utc": "2026-10-26T15:17:43.645475+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1uuP9kXah7Tk43n2mQ08kED5kgOnOMu_n",
            "title": "source_audio.wav",
            "mime_type": "audio/wav",
            "size": "55685198",
            "url": "https://drive.google.com/file/d/1uuP9kXah7Tk43n2mQ08kED5kgOnOMu_n/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1uuP9kXah7Tk43n2mQ08kED5kgOnOMu_n/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T15:16:51.207Z",
            "modified_time": "2026-09-16T11:38:29.000Z",
            "parent_ids": [
              "198o_PWgjXwgUlczYhbe_IGEJroPCnBzo"
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
          "sequence": 462,
          "remote_id": "1uuP9kXah7Tk43n2mQ08kED5kgOnOMu_n",
          "retrieval_file_id": "sediment://file_0000000074ac81fa8e72ca067d7b8a33",
          "metadata": {
            "id": "1uuP9kXah7Tk43n2mQ08kED5kgOnOMu_n",
            "title": "source_audio.wav",
            "mime_type": "audio/wav",
            "size": "55685198",
            "url": "https://drive.google.com/file/d/1uuP9kXah7Tk43n2mQ08kED5kgOnOMu_n/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1uuP9kXah7Tk43n2mQ08kED5kgOnOMu_n/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T15:16:51.207Z",
            "modified_time": "2026-09-16T11:38:29.000Z",
            "parent_ids": [
              "198o_PWgjXwgUlczYhbe_IGEJroPCnBzo"
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
          "started_utc": "2026-10-26T15:18:08.254911+00:00",
          "retrieved_bytes": 55685198,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "55685198",
          "retrieved_sha256": "dd05a0d2f3c66bf6442f23266c4f6bb488e629fb932052768807968ddd68bc61",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T15:18:45.225940+00:00"
        }
      }
    ],
    "uploaded_bytes": 57205534,
    "independently_retrieved_bytes": 57205534,
    "mapped_source_files": 2,
    "selection_amendment": null,
    "preflight": {
      "account": "kgk2930@gmail.com",
      "privacy": "OWNER_ONLY",
      "five_hour_used": 57,
      "weekly_used": 16,
      "paid_credits": "0",
      "observed_at": "2026-10-26T15:15:41.478Z",
      "ui_used_gb": 5.22,
      "storage_ui": "5.22GB of15GB; owner authenticated Google One UI freshly reloaded; Drive4.92GB Gmail302.23MB",
      "conservative_free_bytes": 9295067678,
      "mac_free_bytes": 15499059200,
      "context": "Full Batch24 checkpoint and versioned MD independently verified; current context adequate; exact meter unavailable",
      "ownership": "No backup Python process active; protected Claude writer preserved, no production ownership taken",
      "charges": "Existing storage allowance, no purchases/payment/reset credits",
      "destination_folder_id": "12FkMHzKAtNYleLwX2UBmbMDMlk_6sXEf"
    },
    "postflight": {
      "batch_dir": "/Users/ghilmankhan/YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd/batch-0025",
      "account": "kgk2930@gmail.com",
      "privacy": "OWNER_ONLY",
      "five_hour_used": 62,
      "weekly_used": 16,
      "paid_credits": "0",
      "observed_at": "2026-10-26T15:19:50.853Z",
      "ui_used_gb": 5.27,
      "storage_ui": "5.27GB of15GB; fresh authenticated Google One UI; Drive4.98GB Gmail302.23MB",
      "conservative_free_bytes": 9241380587,
      "mac_free_bytes": 17902600192,
      "context": "Full Batch24 checkpoint and versioned MD independently verified; current context adequate; exact meter unavailable",
      "ownership": "No backup Python process active; protected Claude writer preserved, no production ownership taken",
      "charges": "Existing storage allowance, no purchases/payment/reset credits",
      "destination_folder_id": "198o_PWgjXwgUlczYhbe_IGEJroPCnBzo"
    },
    "permissions": "Owner-only Restricted; no changes",
    "encryption": "Google provider managed; owner-held client key not established",
    "retention": "Until explicit owner removal approval",
    "coverage": "File-level verified recovery only; no complete-package or independent-machine recovery claim"
  },
  "recovery_mapping": {
    "files": [
      {
        "source_absolute": "/Users/ghilmankhan/workprojects/video data of what if/video_forensics_output/weird_and_worrying_questions/00_source/audio/audio.wav",
        "restore_relative": "machine-a/workprojects/video data of what if/video_forensics_output/weird_and_worrying_questions/00_source/audio/audio.wav",
        "bytes": 1520336,
        "fresh_sha256": "faa95195032014766557a1e628ff41bd3cb7c94c515f645626c856cb5a6a6089",
        "remote_id": "1B5JjAc99wHCDK0IYxd8-zv0bler4clWp",
        "remote_url": "https://drive.google.com/file/d/1B5JjAc99wHCDK0IYxd8-zv0bler4clWp/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/workprojects/video data of what if/video_forensics_output/what-if-earth-grew-1cm-every-second/05_audio/source_audio.wav",
        "restore_relative": "machine-a/workprojects/video data of what if/video_forensics_output/what-if-earth-grew-1cm-every-second/05_audio/source_audio.wav",
        "bytes": 55685198,
        "fresh_sha256": "dd05a0d2f3c66bf6442f23266c4f6bb488e629fb932052768807968ddd68bc61",
        "remote_id": "1uuP9kXah7Tk43n2mQ08kED5kgOnOMu_n",
        "remote_url": "https://drive.google.com/file/d/1uuP9kXah7Tk43n2mQ08kED5kgOnOMu_n/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      }
    ]
  },
  "cumulative_before_this_control": {
    "mapped_source_paths": 470,
    "uploaded_bytes_including_controls": 4803237801,
    "verified_bytes_including_controls": 4803237801,
    "remaining_payload_bytes": 7196762199,
    "remaining_plan_files": 82
  }
}
```
