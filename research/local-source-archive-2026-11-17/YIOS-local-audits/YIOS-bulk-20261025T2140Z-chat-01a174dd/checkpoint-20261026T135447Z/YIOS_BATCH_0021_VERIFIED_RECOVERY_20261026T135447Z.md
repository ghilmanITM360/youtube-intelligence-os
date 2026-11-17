# YIOS Batch21 verified recovery receipt

Status VERIFIED. Uploaded bytes: 135,069,719; complete independently retrieved SHA-256 verified bytes: 135,069,719. Source mappings: 20.

All-in physical uploaded bytes before this MD: 4,378,694,907; independently verified bytes: 4,378,694,907. This MD is additional payload, counted by its separate CONTROL-UPLOAD/VERIFY receipts after complete independent readback. No duplicate/partial I/O is counted as new recovery coverage.

Authenticated owner kgk2930@gmail.com; approved private yios hierarchy. Actual namespace IDs, source paths, hashes, bytes and remote object IDs follow. Source stability and current owner/private/parent/size gates passed. No source deletion/move/cleanup, Git/PR/branch/stash/LFS/production mutation, payment or reset credit use by this backup. This is file-level cloud recovery; independent-machine disaster recovery and production ownership acceptance remain unproven.

```json
{
  "receipt": {
    "status": "VERIFIED",
    "batch": 21,
    "completed_utc": "2026-10-26T13:54:47.812480+00:00",
    "files": [
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How fast could a human accellerate (while staying alive)？ [eSPcp-tfGbA].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/How fast could a human accellerate (while staying alive)？ [eSPcp-tfGbA].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 3964374,
        "allocated_path_bytes": 3964928,
        "mtime_ns": 1792432582000000000,
        "device": 16777229,
        "inode": 93824209,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 386,
        "proposed_destination_name": "00386__How fast could a human accellerate (while staying alive)？ [eSPcp-tfGbA].mp4",
        "fresh_stat": {
          "st_size": 3964374,
          "st_mtime_ns": 1792432582000000000,
          "st_ctime_ns": 1792830801518590503,
          "st_ino": 93824209,
          "st_dev": 16777229
        },
        "fresh_sha256": "13bc33ec2f511cd322872d97677cf0f265695a50a6d09ded86c495f86e2ae3ea",
        "hash_refreshed_utc": "2026-10-26T13:31:33.897323+00:00",
        "status": "VERIFIED",
        "remote_id": "1klRTfU55bJeQBKhqNYBEZUqe8KFRqRiw",
        "remote_url": "https://drive.google.com/file/d/1klRTfU55bJeQBKhqNYBEZUqe8KFRqRiw/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:14.570378+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1klRTfU55bJeQBKhqNYBEZUqe8KFRqRiw",
            "title": "How fast could a human accellerate (while staying alive)？ [eSPcp-tfGbA].mp4",
            "mime_type": "video/mp4",
            "size": "3964374",
            "url": "https://drive.google.com/file/d/1klRTfU55bJeQBKhqNYBEZUqe8KFRqRiw/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1klRTfU55bJeQBKhqNYBEZUqe8KFRqRiw/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:33:33.282Z",
            "modified_time": "2026-10-19T17:56:22.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 386,
          "remote_id": "1klRTfU55bJeQBKhqNYBEZUqe8KFRqRiw",
          "retrieval_file_id": "sediment://file_000000001adc82119392b1404ab3c491",
          "metadata": {
            "id": "1klRTfU55bJeQBKhqNYBEZUqe8KFRqRiw",
            "title": "How fast could a human accellerate (while staying alive)？ [eSPcp-tfGbA].mp4",
            "mime_type": "video/mp4",
            "size": "3964374",
            "url": "https://drive.google.com/file/d/1klRTfU55bJeQBKhqNYBEZUqe8KFRqRiw/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1klRTfU55bJeQBKhqNYBEZUqe8KFRqRiw/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:33:33.282Z",
            "modified_time": "2026-10-19T17:56:22.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:35:40.979567+00:00",
          "retrieved_bytes": 3964374,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "3964374",
          "retrieved_sha256": "13bc33ec2f511cd322872d97677cf0f265695a50a6d09ded86c495f86e2ae3ea",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:35:44.830666+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How fast could a vehicle go around a track - but the racer does not have to survive. [rgUfcFAPicY].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/How fast could a vehicle go around a track - but the racer does not have to survive. [rgUfcFAPicY].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 4020273,
        "allocated_path_bytes": 4022272,
        "mtime_ns": 1792432578000000000,
        "device": 16777229,
        "inode": 93824161,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 387,
        "proposed_destination_name": "00387__How fast could a vehicle go around a track - but the racer does not have to survive. [rgUfcFAPicY].mp4",
        "fresh_stat": {
          "st_size": 4020273,
          "st_mtime_ns": 1792432578000000000,
          "st_ctime_ns": 1792830801517813089,
          "st_ino": 93824161,
          "st_dev": 16777229
        },
        "fresh_sha256": "d18d25dc30ea607c4f16838db8c594fc85bdc46e67ad723519e47636bff3e831",
        "hash_refreshed_utc": "2026-10-26T13:31:33.901185+00:00",
        "status": "VERIFIED",
        "remote_id": "1R3VdfZEeGzjFkTcEqWgAucK6RnGANFzB",
        "remote_url": "https://drive.google.com/file/d/1R3VdfZEeGzjFkTcEqWgAucK6RnGANFzB/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:15.387985+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1R3VdfZEeGzjFkTcEqWgAucK6RnGANFzB",
            "title": "How fast could a vehicle go around a track - but the racer does not have to survive. [rgUfcFAPicY].mp4",
            "mime_type": "video/mp4",
            "size": "4020273",
            "url": "https://drive.google.com/file/d/1R3VdfZEeGzjFkTcEqWgAucK6RnGANFzB/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1R3VdfZEeGzjFkTcEqWgAucK6RnGANFzB/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:33:25.805Z",
            "modified_time": "2026-10-19T17:56:18.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 387,
          "remote_id": "1R3VdfZEeGzjFkTcEqWgAucK6RnGANFzB",
          "retrieval_file_id": "sediment://file_00000000da9c81f59a5a8c8411fd90ed",
          "metadata": {
            "id": "1R3VdfZEeGzjFkTcEqWgAucK6RnGANFzB",
            "title": "How fast could a vehicle go around a track - but the racer does not have to survive. [rgUfcFAPicY].mp4",
            "mime_type": "video/mp4",
            "size": "4020273",
            "url": "https://drive.google.com/file/d/1R3VdfZEeGzjFkTcEqWgAucK6RnGANFzB/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1R3VdfZEeGzjFkTcEqWgAucK6RnGANFzB/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:33:25.805Z",
            "modified_time": "2026-10-19T17:56:18.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:35:53.102508+00:00",
          "retrieved_bytes": 4020273,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "4020273",
          "retrieved_sha256": "d18d25dc30ea607c4f16838db8c594fc85bdc46e67ad723519e47636bff3e831",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:35:57.943757+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How high could the magnitude of Earthquakes go？ [wBLVmEZV2Oc].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/How high could the magnitude of Earthquakes go？ [wBLVmEZV2Oc].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 3584843,
        "allocated_path_bytes": 3588096,
        "mtime_ns": 1792432610000000000,
        "device": 16777229,
        "inode": 93824310,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 388,
        "proposed_destination_name": "00388__How high could the magnitude of Earthquakes go？ [wBLVmEZV2Oc].mp4",
        "fresh_stat": {
          "st_size": 3584843,
          "st_mtime_ns": 1792432610000000000,
          "st_ctime_ns": 1792830801519448251,
          "st_ino": 93824310,
          "st_dev": 16777229
        },
        "fresh_sha256": "ffff4ea989fcadd3f3744b3756a5e58fc3d997c127dfac41ba6d46cd1638f5b1",
        "hash_refreshed_utc": "2026-10-26T13:31:33.905074+00:00",
        "status": "VERIFIED",
        "remote_id": "1RdiayHjSaC296SVdfvG37VuzgpyenvHE",
        "remote_url": "https://drive.google.com/file/d/1RdiayHjSaC296SVdfvG37VuzgpyenvHE/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:11.968762+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1RdiayHjSaC296SVdfvG37VuzgpyenvHE",
            "title": "How high could the magnitude of Earthquakes go？ [wBLVmEZV2Oc].mp4",
            "mime_type": "video/mp4",
            "size": "3584843",
            "url": "https://drive.google.com/file/d/1RdiayHjSaC296SVdfvG37VuzgpyenvHE/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1RdiayHjSaC296SVdfvG37VuzgpyenvHE/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:32:41.434Z",
            "modified_time": "2026-10-19T17:56:50.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 388,
          "remote_id": "1RdiayHjSaC296SVdfvG37VuzgpyenvHE",
          "retrieval_file_id": "sediment://file_0000000090ac8211affb8641239dca39",
          "metadata": {
            "id": "1RdiayHjSaC296SVdfvG37VuzgpyenvHE",
            "title": "How high could the magnitude of Earthquakes go？ [wBLVmEZV2Oc].mp4",
            "mime_type": "video/mp4",
            "size": "3584843",
            "url": "https://drive.google.com/file/d/1RdiayHjSaC296SVdfvG37VuzgpyenvHE/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1RdiayHjSaC296SVdfvG37VuzgpyenvHE/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:32:41.434Z",
            "modified_time": "2026-10-19T17:56:50.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:41:04.072282+00:00",
          "retrieved_bytes": 3584843,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "3584843",
          "retrieved_sha256": "ffff4ea989fcadd3f3744b3756a5e58fc3d997c127dfac41ba6d46cd1638f5b1",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:41:07.076825+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How long could the human race survive on only cannibalism？ [jjzYUOd5HAA].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/How long could the human race survive on only cannibalism？ [jjzYUOd5HAA].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 3166180,
        "allocated_path_bytes": 3166208,
        "mtime_ns": 1792432462000000000,
        "device": 16777229,
        "inode": 93824103,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 389,
        "proposed_destination_name": "00389__How long could the human race survive on only cannibalism？ [jjzYUOd5HAA].mp4",
        "fresh_stat": {
          "st_size": 3166180,
          "st_mtime_ns": 1792432462000000000,
          "st_ctime_ns": 1792830801512092147,
          "st_ino": 93824103,
          "st_dev": 16777229
        },
        "fresh_sha256": "d777c2589b3cbf8d4ece36df4b5bb48a6a527099b37fc93d2f2461dc7cf0c753",
        "hash_refreshed_utc": "2026-10-26T13:31:33.908318+00:00",
        "status": "VERIFIED",
        "remote_id": "1INtXlRFiLalPfUUA3Hw-CLNdR8MVK9qY",
        "remote_url": "https://drive.google.com/file/d/1INtXlRFiLalPfUUA3Hw-CLNdR8MVK9qY/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:17.134069+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1INtXlRFiLalPfUUA3Hw-CLNdR8MVK9qY",
            "title": "How long could the human race survive on only cannibalism？ [jjzYUOd5HAA].mp4",
            "mime_type": "video/mp4",
            "size": "3166180",
            "url": "https://drive.google.com/file/d/1INtXlRFiLalPfUUA3Hw-CLNdR8MVK9qY/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1INtXlRFiLalPfUUA3Hw-CLNdR8MVK9qY/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:32:24.261Z",
            "modified_time": "2026-10-19T17:54:22.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 389,
          "remote_id": "1INtXlRFiLalPfUUA3Hw-CLNdR8MVK9qY",
          "retrieval_file_id": "sediment://file_0000000065dc81fa87abf7ef38a57568",
          "metadata": {
            "id": "1INtXlRFiLalPfUUA3Hw-CLNdR8MVK9qY",
            "title": "How long could the human race survive on only cannibalism？ [jjzYUOd5HAA].mp4",
            "mime_type": "video/mp4",
            "size": "3166180",
            "url": "https://drive.google.com/file/d/1INtXlRFiLalPfUUA3Hw-CLNdR8MVK9qY/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1INtXlRFiLalPfUUA3Hw-CLNdR8MVK9qY/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:32:24.261Z",
            "modified_time": "2026-10-19T17:54:22.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:41:12.016138+00:00",
          "retrieved_bytes": 3166180,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "3166180",
          "retrieved_sha256": "d777c2589b3cbf8d4ece36df4b5bb48a6a527099b37fc93d2f2461dc7cf0c753",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:41:17.205186+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How long could you drive towards the sunset？ [rGZ6TsXvi8E].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/How long could you drive towards the sunset？ [rGZ6TsXvi8E].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 5941596,
        "allocated_path_bytes": 5943296,
        "mtime_ns": 1792432448000000000,
        "device": 16777229,
        "inode": 93824282,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 390,
        "proposed_destination_name": "00390__How long could you drive towards the sunset？ [rGZ6TsXvi8E].mp4",
        "fresh_stat": {
          "st_size": 5941596,
          "st_mtime_ns": 1792432448000000000,
          "st_ctime_ns": 1792830801519287501,
          "st_ino": 93824282,
          "st_dev": 16777229
        },
        "fresh_sha256": "1e4498d55a84d0ec6d1bbd543a665ce4b47bdbff336b602d611047c63cf35189",
        "hash_refreshed_utc": "2026-10-26T13:31:33.913351+00:00",
        "status": "VERIFIED",
        "remote_id": "113DPLaT6-527A4YhZTDOyCwrxtY_If01",
        "remote_url": "https://drive.google.com/file/d/113DPLaT6-527A4YhZTDOyCwrxtY_If01/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:18.854574+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "113DPLaT6-527A4YhZTDOyCwrxtY_If01",
            "title": "How long could you drive towards the sunset？ [rGZ6TsXvi8E].mp4",
            "mime_type": "video/mp4",
            "size": "5941596",
            "url": "https://drive.google.com/file/d/113DPLaT6-527A4YhZTDOyCwrxtY_If01/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/113DPLaT6-527A4YhZTDOyCwrxtY_If01/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:32:20.912Z",
            "modified_time": "2026-10-19T17:54:08.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 390,
          "remote_id": "113DPLaT6-527A4YhZTDOyCwrxtY_If01",
          "retrieval_file_id": "sediment://file_000000002ce081fa8f17084e1c8fee3a",
          "metadata": {
            "id": "113DPLaT6-527A4YhZTDOyCwrxtY_If01",
            "title": "How long could you drive towards the sunset？ [rGZ6TsXvi8E].mp4",
            "mime_type": "video/mp4",
            "size": "5941596",
            "url": "https://drive.google.com/file/d/113DPLaT6-527A4YhZTDOyCwrxtY_If01/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/113DPLaT6-527A4YhZTDOyCwrxtY_If01/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:32:20.912Z",
            "modified_time": "2026-10-19T17:54:08.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:41:22.473979+00:00",
          "retrieved_bytes": 5941596,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "5941596",
          "retrieved_sha256": "1e4498d55a84d0ec6d1bbd543a665ce4b47bdbff336b602d611047c63cf35189",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:41:27.997153+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How long would you survive with no DNA？ [s3oLIDaElaE].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/How long would you survive with no DNA？ [s3oLIDaElaE].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 5953255,
        "allocated_path_bytes": 5955584,
        "mtime_ns": 1792432196000000000,
        "device": 16777229,
        "inode": 93824112,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 391,
        "proposed_destination_name": "00391__How long would you survive with no DNA？ [s3oLIDaElaE].mp4",
        "fresh_stat": {
          "st_size": 5953255,
          "st_mtime_ns": 1792432196000000000,
          "st_ctime_ns": 1792830801512146688,
          "st_ino": 93824112,
          "st_dev": 16777229
        },
        "fresh_sha256": "50be6832b2e744074e47eee6672a9733eae20669f3b4f07854c204abaf1d171c",
        "hash_refreshed_utc": "2026-10-26T13:31:33.918167+00:00",
        "status": "VERIFIED",
        "remote_id": "1uIcBRSmPshoVzbQjkY2MughotywCFNbq",
        "remote_url": "https://drive.google.com/file/d/1uIcBRSmPshoVzbQjkY2MughotywCFNbq/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:30.620294+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1uIcBRSmPshoVzbQjkY2MughotywCFNbq",
            "title": "How long would you survive with no DNA？ [s3oLIDaElaE].mp4",
            "mime_type": "video/mp4",
            "size": "5953255",
            "url": "https://drive.google.com/file/d/1uIcBRSmPshoVzbQjkY2MughotywCFNbq/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1uIcBRSmPshoVzbQjkY2MughotywCFNbq/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:32:37.736Z",
            "modified_time": "2026-10-19T17:49:56.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 391,
          "remote_id": "1uIcBRSmPshoVzbQjkY2MughotywCFNbq",
          "retrieval_file_id": "sediment://file_000000005cd88211accaa10713191f3f",
          "metadata": {
            "id": "1uIcBRSmPshoVzbQjkY2MughotywCFNbq",
            "title": "How long would you survive with no DNA？ [s3oLIDaElaE].mp4",
            "mime_type": "video/mp4",
            "size": "5953255",
            "url": "https://drive.google.com/file/d/1uIcBRSmPshoVzbQjkY2MughotywCFNbq/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1uIcBRSmPshoVzbQjkY2MughotywCFNbq/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:32:37.736Z",
            "modified_time": "2026-10-19T17:49:56.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:41:37.164437+00:00",
          "retrieved_bytes": 5953255,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "5953255",
          "retrieved_sha256": "50be6832b2e744074e47eee6672a9733eae20669f3b4f07854c204abaf1d171c",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:41:41.979005+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How many elevators would you need in a billion-story building？ [oMtAHGv-DU4].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/How many elevators would you need in a billion-story building？ [oMtAHGv-DU4].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 2880001,
        "allocated_path_bytes": 2883584,
        "mtime_ns": 1792432530000000000,
        "device": 16777229,
        "inode": 93824141,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 392,
        "proposed_destination_name": "00392__How many elevators would you need in a billion-story building？ [oMtAHGv-DU4].mp4",
        "fresh_stat": {
          "st_size": 2880001,
          "st_mtime_ns": 1792432530000000000,
          "st_ctime_ns": 1792830801517603048,
          "st_ino": 93824141,
          "st_dev": 16777229
        },
        "fresh_sha256": "b5e9cbbfab3c278531d54254df6dc1fea2084c3850a25ad489c6af8933cff95f",
        "hash_refreshed_utc": "2026-10-26T13:31:33.920932+00:00",
        "status": "VERIFIED",
        "remote_id": "1RTPxccNP93es1uObydD9ZlzrFhW_wRp7",
        "remote_url": "https://drive.google.com/file/d/1RTPxccNP93es1uObydD9ZlzrFhW_wRp7/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:16.298177+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1RTPxccNP93es1uObydD9ZlzrFhW_wRp7",
            "title": "How many elevators would you need in a billion-story building？ [oMtAHGv-DU4].mp4",
            "mime_type": "video/mp4",
            "size": "2880001",
            "url": "https://drive.google.com/file/d/1RTPxccNP93es1uObydD9ZlzrFhW_wRp7/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1RTPxccNP93es1uObydD9ZlzrFhW_wRp7/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:32:27.397Z",
            "modified_time": "2026-10-19T17:55:30.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 392,
          "remote_id": "1RTPxccNP93es1uObydD9ZlzrFhW_wRp7",
          "retrieval_file_id": "sediment://file_00000000e92c8206b1ca11200ba12e94",
          "metadata": {
            "id": "1RTPxccNP93es1uObydD9ZlzrFhW_wRp7",
            "title": "How many elevators would you need in a billion-story building？ [oMtAHGv-DU4].mp4",
            "mime_type": "video/mp4",
            "size": "2880001",
            "url": "https://drive.google.com/file/d/1RTPxccNP93es1uObydD9ZlzrFhW_wRp7/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1RTPxccNP93es1uObydD9ZlzrFhW_wRp7/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:32:27.397Z",
            "modified_time": "2026-10-19T17:55:30.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:45:28.770556+00:00",
          "retrieved_bytes": 2880001,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "2880001",
          "retrieved_sha256": "b5e9cbbfab3c278531d54254df6dc1fea2084c3850a25ad489c6af8933cff95f",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:45:31.806576+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/If all humans died, when would the last light go out？ [8fADp43wJwU].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/If all humans died, when would the last light go out？ [8fADp43wJwU].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 11798131,
        "allocated_path_bytes": 11800576,
        "mtime_ns": 1792432368000000000,
        "device": 16777229,
        "inode": 93824119,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 393,
        "proposed_destination_name": "00393__If all humans died, when would the last light go out？ [8fADp43wJwU].mp4",
        "fresh_stat": {
          "st_size": 11798131,
          "st_mtime_ns": 1792432368000000000,
          "st_ctime_ns": 1792830801517424007,
          "st_ino": 93824119,
          "st_dev": 16777229
        },
        "fresh_sha256": "973bb97ae6717fa54d42fe3524fcc6921016a65fa23ccae4b569ea62e91f2b4b",
        "hash_refreshed_utc": "2026-10-26T13:31:33.930387+00:00",
        "status": "VERIFIED",
        "remote_id": "1zYEIxVrC0VgPg4OR5vKsizdxy59nkXFa",
        "remote_url": "https://drive.google.com/file/d/1zYEIxVrC0VgPg4OR5vKsizdxy59nkXFa/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:25.976896+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1zYEIxVrC0VgPg4OR5vKsizdxy59nkXFa",
            "title": "If all humans died, when would the last light go out？ [8fADp43wJwU].mp4",
            "mime_type": "video/mp4",
            "size": "11798131",
            "url": "https://drive.google.com/file/d/1zYEIxVrC0VgPg4OR5vKsizdxy59nkXFa/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1zYEIxVrC0VgPg4OR5vKsizdxy59nkXFa/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:32:33.684Z",
            "modified_time": "2026-10-19T17:52:48.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 393,
          "remote_id": "1zYEIxVrC0VgPg4OR5vKsizdxy59nkXFa",
          "retrieval_file_id": "sediment://file_00000000d6248211a985eddee407584e",
          "metadata": {
            "id": "1zYEIxVrC0VgPg4OR5vKsizdxy59nkXFa",
            "title": "If all humans died, when would the last light go out？ [8fADp43wJwU].mp4",
            "mime_type": "video/mp4",
            "size": "11798131",
            "url": "https://drive.google.com/file/d/1zYEIxVrC0VgPg4OR5vKsizdxy59nkXFa/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1zYEIxVrC0VgPg4OR5vKsizdxy59nkXFa/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:32:33.684Z",
            "modified_time": "2026-10-19T17:52:48.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:45:43.832813+00:00",
          "retrieved_bytes": 11798131,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "11798131",
          "retrieved_sha256": "973bb97ae6717fa54d42fe3524fcc6921016a65fa23ccae4b569ea62e91f2b4b",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:45:50.348011+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/If you put a toaster in a freezer, which wins？ [9VG0yqq_PHM].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/If you put a toaster in a freezer, which wins？ [9VG0yqq_PHM].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 5009650,
        "allocated_path_bytes": 5013504,
        "mtime_ns": 1792432158000000000,
        "device": 16777229,
        "inode": 93824061,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 394,
        "proposed_destination_name": "00394__If you put a toaster in a freezer, which wins？ [9VG0yqq_PHM].mp4",
        "fresh_stat": {
          "st_size": 5009650,
          "st_mtime_ns": 1792432158000000000,
          "st_ctime_ns": 1792830801511886522,
          "st_ino": 93824061,
          "st_dev": 16777229
        },
        "fresh_sha256": "1a5c6363860a5c2c90c608602c8c9a9e3a8241238c8d75d0d4c94a16ac6016ac",
        "hash_refreshed_utc": "2026-10-26T13:31:33.934611+00:00",
        "status": "VERIFIED",
        "remote_id": "1mFuf81sipvCJaNkuQ8oIBpv_3Wj2jYYI",
        "remote_url": "https://drive.google.com/file/d/1mFuf81sipvCJaNkuQ8oIBpv_3Wj2jYYI/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:32.672367+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1mFuf81sipvCJaNkuQ8oIBpv_3Wj2jYYI",
            "title": "If you put a toaster in a freezer, which wins？ [9VG0yqq_PHM].mp4",
            "mime_type": "video/mp4",
            "size": "5009650",
            "url": "https://drive.google.com/file/d/1mFuf81sipvCJaNkuQ8oIBpv_3Wj2jYYI/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1mFuf81sipvCJaNkuQ8oIBpv_3Wj2jYYI/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:33:29.793Z",
            "modified_time": "2026-10-19T17:49:18.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 394,
          "remote_id": "1mFuf81sipvCJaNkuQ8oIBpv_3Wj2jYYI",
          "retrieval_file_id": "sediment://file_000000002ee88211b2b7d5da3c70de6e",
          "metadata": {
            "id": "1mFuf81sipvCJaNkuQ8oIBpv_3Wj2jYYI",
            "title": "If you put a toaster in a freezer, which wins？ [9VG0yqq_PHM].mp4",
            "mime_type": "video/mp4",
            "size": "5009650",
            "url": "https://drive.google.com/file/d/1mFuf81sipvCJaNkuQ8oIBpv_3Wj2jYYI/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1mFuf81sipvCJaNkuQ8oIBpv_3Wj2jYYI/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:33:29.793Z",
            "modified_time": "2026-10-19T17:49:18.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:46:00.034830+00:00",
          "retrieved_bytes": 5009650,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "5009650",
          "retrieved_sha256": "1a5c6363860a5c2c90c608602c8c9a9e3a8241238c8d75d0d4c94a16ac6016ac",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:46:04.201403+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/Is there such a thing as a magnitude 0 earthquake？ [FKXVs4UteSc].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/Is there such a thing as a magnitude 0 earthquake？ [FKXVs4UteSc].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 3902844,
        "allocated_path_bytes": 3903488,
        "mtime_ns": 1792432608000000000,
        "device": 16777229,
        "inode": 93824034,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 395,
        "proposed_destination_name": "00395__Is there such a thing as a magnitude 0 earthquake？ [FKXVs4UteSc].mp4",
        "fresh_stat": {
          "st_size": 3902844,
          "st_mtime_ns": 1792432608000000000,
          "st_ctime_ns": 1792830801511770689,
          "st_ino": 93824034,
          "st_dev": 16777229
        },
        "fresh_sha256": "ceae7efbeec972b8dee0d4ca6498a20502167d6b57a04fc37ecbd376ab466b3e",
        "hash_refreshed_utc": "2026-10-26T13:31:33.937880+00:00",
        "status": "VERIFIED",
        "remote_id": "1sflXdqwiw3FtnYFu5vo41sVkQsvERQfI",
        "remote_url": "https://drive.google.com/file/d/1sflXdqwiw3FtnYFu5vo41sVkQsvERQfI/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:12.811019+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1sflXdqwiw3FtnYFu5vo41sVkQsvERQfI",
            "title": "Is there such a thing as a magnitude 0 earthquake？ [FKXVs4UteSc].mp4",
            "mime_type": "video/mp4",
            "size": "3902844",
            "url": "https://drive.google.com/file/d/1sflXdqwiw3FtnYFu5vo41sVkQsvERQfI/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1sflXdqwiw3FtnYFu5vo41sVkQsvERQfI/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:33:22.716Z",
            "modified_time": "2026-10-19T17:56:48.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 395,
          "remote_id": "1sflXdqwiw3FtnYFu5vo41sVkQsvERQfI",
          "retrieval_file_id": "sediment://file_00000000185081fa8b0f060b2efddcce",
          "metadata": {
            "id": "1sflXdqwiw3FtnYFu5vo41sVkQsvERQfI",
            "title": "Is there such a thing as a magnitude 0 earthquake？ [FKXVs4UteSc].mp4",
            "mime_type": "video/mp4",
            "size": "3902844",
            "url": "https://drive.google.com/file/d/1sflXdqwiw3FtnYFu5vo41sVkQsvERQfI/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1sflXdqwiw3FtnYFu5vo41sVkQsvERQfI/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:33:22.716Z",
            "modified_time": "2026-10-19T17:56:48.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:46:09.069151+00:00",
          "retrieved_bytes": 3902844,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "3902844",
          "retrieved_sha256": "ceae7efbeec972b8dee0d4ca6498a20502167d6b57a04fc37ecbd376ab466b3e",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:46:14.508117+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/More weird and worrying questions [alBQCm0QpJg].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/More weird and worrying questions [alBQCm0QpJg].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 9005195,
        "allocated_path_bytes": 9007104,
        "mtime_ns": 1792432424000000000,
        "device": 16777229,
        "inode": 93824284,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 396,
        "proposed_destination_name": "00396__More weird and worrying questions [alBQCm0QpJg].mp4",
        "fresh_stat": {
          "st_size": 9005195,
          "st_mtime_ns": 1792432424000000000,
          "st_ctime_ns": 1792830801519309251,
          "st_ino": 93824284,
          "st_dev": 16777229
        },
        "fresh_sha256": "41e9cd3ba2abbf3b278de04a36c182422ea60a0cc4447ea4e4d24aad9f50da56",
        "hash_refreshed_utc": "2026-10-26T13:31:33.945668+00:00",
        "status": "VERIFIED",
        "remote_id": "12cuL_Mhpmu9KHurDqt0kW2xrMYlg9dI8",
        "remote_url": "https://drive.google.com/file/d/12cuL_Mhpmu9KHurDqt0kW2xrMYlg9dI8/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:20.174662+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "12cuL_Mhpmu9KHurDqt0kW2xrMYlg9dI8",
            "title": "More weird and worrying questions [alBQCm0QpJg].mp4",
            "mime_type": "video/mp4",
            "size": "9005195",
            "url": "https://drive.google.com/file/d/12cuL_Mhpmu9KHurDqt0kW2xrMYlg9dI8/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/12cuL_Mhpmu9KHurDqt0kW2xrMYlg9dI8/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:34:09.746Z",
            "modified_time": "2026-10-19T17:53:44.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 396,
          "remote_id": "12cuL_Mhpmu9KHurDqt0kW2xrMYlg9dI8",
          "retrieval_file_id": "sediment://file_00000000db1481f5a77725a22200d3c3",
          "metadata": {
            "id": "12cuL_Mhpmu9KHurDqt0kW2xrMYlg9dI8",
            "title": "More weird and worrying questions [alBQCm0QpJg].mp4",
            "mime_type": "video/mp4",
            "size": "9005195",
            "url": "https://drive.google.com/file/d/12cuL_Mhpmu9KHurDqt0kW2xrMYlg9dI8/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/12cuL_Mhpmu9KHurDqt0kW2xrMYlg9dI8/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:34:09.746Z",
            "modified_time": "2026-10-19T17:53:44.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:46:23.230298+00:00",
          "retrieved_bytes": 9005195,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "9005195",
          "retrieved_sha256": "41e9cd3ba2abbf3b278de04a36c182422ea60a0cc4447ea4e4d24aad9f50da56",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:46:28.324434+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/Petition to send a swimming pool to the moon! [mtTbwHzhUiM].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/Petition to send a swimming pool to the moon! [mtTbwHzhUiM].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 1408778,
        "allocated_path_bytes": 1409024,
        "mtime_ns": 1792432584000000000,
        "device": 16777229,
        "inode": 93824031,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 397,
        "proposed_destination_name": "00397__Petition to send a swimming pool to the moon! [mtTbwHzhUiM].mp4",
        "fresh_stat": {
          "st_size": 1408778,
          "st_mtime_ns": 1792432584000000000,
          "st_ctime_ns": 1792830801511740689,
          "st_ino": 93824031,
          "st_dev": 16777229
        },
        "fresh_sha256": "8fb3d1a30ae873e0047871202d0c59fa085f46560d61de91abf22261a6e7ea58",
        "hash_refreshed_utc": "2026-10-26T13:31:33.947450+00:00",
        "status": "VERIFIED",
        "remote_id": "1AIgOaWdoyKG8rQ8Bwej22fz4nP8HSCCF",
        "remote_url": "https://drive.google.com/file/d/1AIgOaWdoyKG8rQ8Bwej22fz4nP8HSCCF/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:13.667827+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1AIgOaWdoyKG8rQ8Bwej22fz4nP8HSCCF",
            "title": "Petition to send a swimming pool to the moon! [mtTbwHzhUiM].mp4",
            "mime_type": "video/mp4",
            "size": "1408778",
            "url": "https://drive.google.com/file/d/1AIgOaWdoyKG8rQ8Bwej22fz4nP8HSCCF/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1AIgOaWdoyKG8rQ8Bwej22fz4nP8HSCCF/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:34:04.788Z",
            "modified_time": "2026-10-19T17:56:24.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 397,
          "remote_id": "1AIgOaWdoyKG8rQ8Bwej22fz4nP8HSCCF",
          "retrieval_file_id": "sediment://file_000000008e5081f887b43aa984789d67",
          "metadata": {
            "id": "1AIgOaWdoyKG8rQ8Bwej22fz4nP8HSCCF",
            "title": "Petition to send a swimming pool to the moon! [mtTbwHzhUiM].mp4",
            "mime_type": "video/mp4",
            "size": "1408778",
            "url": "https://drive.google.com/file/d/1AIgOaWdoyKG8rQ8Bwej22fz4nP8HSCCF/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1AIgOaWdoyKG8rQ8Bwej22fz4nP8HSCCF/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:34:04.788Z",
            "modified_time": "2026-10-19T17:56:24.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:46:35.445792+00:00",
          "retrieved_bytes": 1408778,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "1408778",
          "retrieved_sha256": "8fb3d1a30ae873e0047871202d0c59fa085f46560d61de91abf22261a6e7ea58",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:46:37.996416+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/Weird and worrying questions [SLd4hnmeW_g].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/Weird and worrying questions [SLd4hnmeW_g].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 13478240,
        "allocated_path_bytes": 13479936,
        "mtime_ns": 1792432456000000000,
        "device": 16777229,
        "inode": 93824266,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 398,
        "proposed_destination_name": "00398__Weird and worrying questions [SLd4hnmeW_g].mp4",
        "fresh_stat": {
          "st_size": 13478240,
          "st_mtime_ns": 1792432456000000000,
          "st_ctime_ns": 1792830801519154002,
          "st_ino": 93824266,
          "st_dev": 16777229
        },
        "fresh_sha256": "893ebff4dda30f790f56131052879b3353d75af7ba35edece8f95bf5810a3ac5",
        "hash_refreshed_utc": "2026-10-26T13:31:33.957149+00:00",
        "status": "VERIFIED",
        "remote_id": "11up_P2_b0cNX8qoRfuv8HqWDvbRq7qe-",
        "remote_url": "https://drive.google.com/file/d/11up_P2_b0cNX8qoRfuv8HqWDvbRq7qe-/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:17.976365+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "11up_P2_b0cNX8qoRfuv8HqWDvbRq7qe-",
            "title": "Weird and worrying questions [SLd4hnmeW_g].mp4",
            "mime_type": "video/mp4",
            "size": "13478240",
            "url": "https://drive.google.com/file/d/11up_P2_b0cNX8qoRfuv8HqWDvbRq7qe-/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/11up_P2_b0cNX8qoRfuv8HqWDvbRq7qe-/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:34:24.893Z",
            "modified_time": "2026-10-19T17:54:16.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 398,
          "remote_id": "11up_P2_b0cNX8qoRfuv8HqWDvbRq7qe-",
          "retrieval_file_id": "sediment://file_00000000ceb081fa8789f590ddfe2180",
          "metadata": {
            "id": "11up_P2_b0cNX8qoRfuv8HqWDvbRq7qe-",
            "title": "Weird and worrying questions [SLd4hnmeW_g].mp4",
            "mime_type": "video/mp4",
            "size": "13478240",
            "url": "https://drive.google.com/file/d/11up_P2_b0cNX8qoRfuv8HqWDvbRq7qe-/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/11up_P2_b0cNX8qoRfuv8HqWDvbRq7qe-/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:34:24.893Z",
            "modified_time": "2026-10-19T17:54:16.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:46:44.619023+00:00",
          "retrieved_bytes": 13478240,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "13478240",
          "retrieved_sha256": "893ebff4dda30f790f56131052879b3353d75af7ba35edece8f95bf5810a3ac5",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:46:51.860347+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if ALL the sun’s power was focused in one place？ [qu8nx1qUwEU].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if ALL the sun’s power was focused in one place？ [qu8nx1qUwEU].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 6942960,
        "allocated_path_bytes": 6946816,
        "mtime_ns": 1792432206000000000,
        "device": 16777229,
        "inode": 93824039,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 399,
        "proposed_destination_name": "00399__What if ALL the sun’s power was focused in one place？ [qu8nx1qUwEU].mp4",
        "fresh_stat": {
          "st_size": 6942960,
          "st_mtime_ns": 1792432206000000000,
          "st_ctime_ns": 1792830801511801939,
          "st_ino": 93824039,
          "st_dev": 16777229
        },
        "fresh_sha256": "4aa23ce06382a270b60e287b062763b6d936a2af9fa8619c33ec8b408c18beea",
        "hash_refreshed_utc": "2026-10-26T13:31:33.962881+00:00",
        "status": "VERIFIED",
        "remote_id": "11mOrKDOWxsT1fbTitFoyl-0faBR7HOgb",
        "remote_url": "https://drive.google.com/file/d/11mOrKDOWxsT1fbTitFoyl-0faBR7HOgb/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:29.532542+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "11mOrKDOWxsT1fbTitFoyl-0faBR7HOgb",
            "title": "What if ALL the sun’s power was focused in one place？ [qu8nx1qUwEU].mp4",
            "mime_type": "video/mp4",
            "size": "6942960",
            "url": "https://drive.google.com/file/d/11mOrKDOWxsT1fbTitFoyl-0faBR7HOgb/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/11mOrKDOWxsT1fbTitFoyl-0faBR7HOgb/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:34:17.930Z",
            "modified_time": "2026-10-19T17:50:06.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 399,
          "remote_id": "11mOrKDOWxsT1fbTitFoyl-0faBR7HOgb",
          "retrieval_file_id": "sediment://file_00000000a2cc81faaa853e9ba8268add",
          "metadata": {
            "id": "11mOrKDOWxsT1fbTitFoyl-0faBR7HOgb",
            "title": "What if ALL the sun’s power was focused in one place？ [qu8nx1qUwEU].mp4",
            "mime_type": "video/mp4",
            "size": "6942960",
            "url": "https://drive.google.com/file/d/11mOrKDOWxsT1fbTitFoyl-0faBR7HOgb/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/11mOrKDOWxsT1fbTitFoyl-0faBR7HOgb/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:34:17.930Z",
            "modified_time": "2026-10-19T17:50:06.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:46:57.347781+00:00",
          "retrieved_bytes": 6942960,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "6942960",
          "retrieved_sha256": "4aa23ce06382a270b60e287b062763b6d936a2af9fa8619c33ec8b408c18beea",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:47:03.319894+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if Earth grew 1cm every second？ [-1-ldW4kpLM].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if Earth grew 1cm every second？ [-1-ldW4kpLM].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 9486746,
        "allocated_path_bytes": 9490432,
        "mtime_ns": 1792432288000000000,
        "device": 16777229,
        "inode": 93824298,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 400,
        "proposed_destination_name": "00400__What if Earth grew 1cm every second？ [-1-ldW4kpLM].mp4",
        "fresh_stat": {
          "st_size": 9486746,
          "st_mtime_ns": 1792432288000000000,
          "st_ctime_ns": 1792830801519382460,
          "st_ino": 93824298,
          "st_dev": 16777229
        },
        "fresh_sha256": "dce7aed164da0da8979608392520c88e295185550c0d8b18950e58666a3c26b3",
        "hash_refreshed_utc": "2026-10-26T13:31:33.970303+00:00",
        "status": "VERIFIED",
        "remote_id": "1kAyihJrHkTv_lCVYB86c6bKwNTPSz_7I",
        "remote_url": "https://drive.google.com/file/d/1kAyihJrHkTv_lCVYB86c6bKwNTPSz_7I/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:28.269099+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1kAyihJrHkTv_lCVYB86c6bKwNTPSz_7I",
            "title": "What if Earth grew 1cm every second？ [-1-ldW4kpLM].mp4",
            "mime_type": "video/mp4",
            "size": "9486746",
            "url": "https://drive.google.com/file/d/1kAyihJrHkTv_lCVYB86c6bKwNTPSz_7I/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1kAyihJrHkTv_lCVYB86c6bKwNTPSz_7I/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:34:01.857Z",
            "modified_time": "2026-10-19T17:51:28.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 400,
          "remote_id": "1kAyihJrHkTv_lCVYB86c6bKwNTPSz_7I",
          "retrieval_file_id": "sediment://file_00000000b6e481fa8db31f73fcf1dffd",
          "metadata": {
            "id": "1kAyihJrHkTv_lCVYB86c6bKwNTPSz_7I",
            "title": "What if Earth grew 1cm every second？ [-1-ldW4kpLM].mp4",
            "mime_type": "video/mp4",
            "size": "9486746",
            "url": "https://drive.google.com/file/d/1kAyihJrHkTv_lCVYB86c6bKwNTPSz_7I/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1kAyihJrHkTv_lCVYB86c6bKwNTPSz_7I/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:34:01.857Z",
            "modified_time": "2026-10-19T17:51:28.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:47:08.652967+00:00",
          "retrieved_bytes": 9486746,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "9486746",
          "retrieved_sha256": "dce7aed164da0da8979608392520c88e295185550c0d8b18950e58666a3c26b3",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:47:13.951339+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if Earth suddenly stopped spinning？ [gp5G1QG6cXc].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if Earth suddenly stopped spinning？ [gp5G1QG6cXc].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 10418611,
        "allocated_path_bytes": 10420224,
        "mtime_ns": 1792432402000000000,
        "device": 16777229,
        "inode": 93824122,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 401,
        "proposed_destination_name": "00401__What if Earth suddenly stopped spinning？ [gp5G1QG6cXc].mp4",
        "fresh_stat": {
          "st_size": 10418611,
          "st_mtime_ns": 1792432402000000000,
          "st_ctime_ns": 1792830801517457757,
          "st_ino": 93824122,
          "st_dev": 16777229
        },
        "fresh_sha256": "b0dd04e6e66fefe7c468e747fc50a0a7cea576c9019fc39af4d39d0175180248",
        "hash_refreshed_utc": "2026-10-26T13:31:33.978436+00:00",
        "status": "VERIFIED",
        "remote_id": "13G2nfEuqKDZROQsal5l9BSEl2lI8v-oA",
        "remote_url": "https://drive.google.com/file/d/13G2nfEuqKDZROQsal5l9BSEl2lI8v-oA/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:24.376098+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "13G2nfEuqKDZROQsal5l9BSEl2lI8v-oA",
            "title": "What if Earth suddenly stopped spinning？ [gp5G1QG6cXc].mp4",
            "mime_type": "video/mp4",
            "size": "10418611",
            "url": "https://drive.google.com/file/d/13G2nfEuqKDZROQsal5l9BSEl2lI8v-oA/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/13G2nfEuqKDZROQsal5l9BSEl2lI8v-oA/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:33:56.603Z",
            "modified_time": "2026-10-19T17:53:22.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 401,
          "remote_id": "13G2nfEuqKDZROQsal5l9BSEl2lI8v-oA",
          "retrieval_file_id": "sediment://file_00000000866881fa8c92c30b5dded23a",
          "metadata": {
            "id": "13G2nfEuqKDZROQsal5l9BSEl2lI8v-oA",
            "title": "What if Earth suddenly stopped spinning？ [gp5G1QG6cXc].mp4",
            "mime_type": "video/mp4",
            "size": "10418611",
            "url": "https://drive.google.com/file/d/13G2nfEuqKDZROQsal5l9BSEl2lI8v-oA/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/13G2nfEuqKDZROQsal5l9BSEl2lI8v-oA/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:33:56.603Z",
            "modified_time": "2026-10-19T17:53:22.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:47:19.177959+00:00",
          "retrieved_bytes": 10418611,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "10418611",
          "retrieved_sha256": "b0dd04e6e66fefe7c468e747fc50a0a7cea576c9019fc39af4d39d0175180248",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:47:26.689812+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if Earth’s Water Suddenly Disappeared？ [4ZVtHknKuvg].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if Earth’s Water Suddenly Disappeared？ [4ZVtHknKuvg].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 6088613,
        "allocated_path_bytes": 6090752,
        "mtime_ns": 1792432162000000000,
        "device": 16777229,
        "inode": 93824143,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 402,
        "proposed_destination_name": "00402__What if Earth’s Water Suddenly Disappeared？ [4ZVtHknKuvg].mp4",
        "fresh_stat": {
          "st_size": 6088613,
          "st_mtime_ns": 1792432162000000000,
          "st_ctime_ns": 1792830801517633214,
          "st_ino": 93824143,
          "st_dev": 16777229
        },
        "fresh_sha256": "fd96c7878fd8713e45ce1e29784fde7e42d6ba4374844844c7482edda703f1c8",
        "hash_refreshed_utc": "2026-10-26T13:31:33.984072+00:00",
        "status": "VERIFIED",
        "remote_id": "1fW4hdKy8q1C0DQq0UJ1e34r2rr_1qT0j",
        "remote_url": "https://drive.google.com/file/d/1fW4hdKy8q1C0DQq0UJ1e34r2rr_1qT0j/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:31.666829+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1fW4hdKy8q1C0DQq0UJ1e34r2rr_1qT0j",
            "title": "What if Earth’s Water Suddenly Disappeared？ [4ZVtHknKuvg].mp4",
            "mime_type": "video/mp4",
            "size": "6088613",
            "url": "https://drive.google.com/file/d/1fW4hdKy8q1C0DQq0UJ1e34r2rr_1qT0j/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1fW4hdKy8q1C0DQq0UJ1e34r2rr_1qT0j/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:33:44.801Z",
            "modified_time": "2026-10-19T17:49:22.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 402,
          "remote_id": "1fW4hdKy8q1C0DQq0UJ1e34r2rr_1qT0j",
          "retrieval_file_id": "sediment://file_00000000dc7481fab59de9c0f7416eca",
          "metadata": {
            "id": "1fW4hdKy8q1C0DQq0UJ1e34r2rr_1qT0j",
            "title": "What if Earth’s Water Suddenly Disappeared？ [4ZVtHknKuvg].mp4",
            "mime_type": "video/mp4",
            "size": "6088613",
            "url": "https://drive.google.com/file/d/1fW4hdKy8q1C0DQq0UJ1e34r2rr_1qT0j/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1fW4hdKy8q1C0DQq0UJ1e34r2rr_1qT0j/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:33:44.801Z",
            "modified_time": "2026-10-19T17:49:22.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:47:31.388944+00:00",
          "retrieved_bytes": 6088613,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "6088613",
          "retrieved_sha256": "fd96c7878fd8713e45ce1e29784fde7e42d6ba4374844844c7482edda703f1c8",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:47:36.493656+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if NASCAR had no rules？ [JcXpCyPc2Xw].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if NASCAR had no rules？ [JcXpCyPc2Xw].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 8918111,
        "allocated_path_bytes": 8921088,
        "mtime_ns": 1792432404000000000,
        "device": 16777229,
        "inode": 93824189,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 403,
        "proposed_destination_name": "00403__What if NASCAR had no rules？ [JcXpCyPc2Xw].mp4",
        "fresh_stat": {
          "st_size": 8918111,
          "st_mtime_ns": 1792432404000000000,
          "st_ctime_ns": 1792830801518207213,
          "st_ino": 93824189,
          "st_dev": 16777229
        },
        "fresh_sha256": "a8aa9dbcd4cf3510e31d11b6c38e4106a5d6d103c55388ec480a0e3b06245d5e",
        "hash_refreshed_utc": "2026-10-26T13:31:33.993641+00:00",
        "status": "VERIFIED",
        "remote_id": "1WWolOAXo5_WtU4WDiRKLtrN9cIpNJocH",
        "remote_url": "https://drive.google.com/file/d/1WWolOAXo5_WtU4WDiRKLtrN9cIpNJocH/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:23.245563+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1WWolOAXo5_WtU4WDiRKLtrN9cIpNJocH",
            "title": "What if NASCAR had no rules？ [JcXpCyPc2Xw].mp4",
            "mime_type": "video/mp4",
            "size": "8918111",
            "url": "https://drive.google.com/file/d/1WWolOAXo5_WtU4WDiRKLtrN9cIpNJocH/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1WWolOAXo5_WtU4WDiRKLtrN9cIpNJocH/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:33:50.154Z",
            "modified_time": "2026-10-19T17:53:24.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 403,
          "remote_id": "1WWolOAXo5_WtU4WDiRKLtrN9cIpNJocH",
          "retrieval_file_id": "sediment://file_00000000386081fa8d5ee275a0035d8f",
          "metadata": {
            "id": "1WWolOAXo5_WtU4WDiRKLtrN9cIpNJocH",
            "title": "What if NASCAR had no rules？ [JcXpCyPc2Xw].mp4",
            "mime_type": "video/mp4",
            "size": "8918111",
            "url": "https://drive.google.com/file/d/1WWolOAXo5_WtU4WDiRKLtrN9cIpNJocH/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1WWolOAXo5_WtU4WDiRKLtrN9cIpNJocH/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:33:50.154Z",
            "modified_time": "2026-10-19T17:53:24.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:53:39.827976+00:00",
          "retrieved_bytes": 8918111,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "8918111",
          "retrieved_sha256": "a8aa9dbcd4cf3510e31d11b6c38e4106a5d6d103c55388ec480a0e3b06245d5e",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:53:46.170723+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if a glass of water were LITERALLY half empty？ [0EytSWiKrFg].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if a glass of water were LITERALLY half empty？ [0EytSWiKrFg].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 6801271,
        "allocated_path_bytes": 6803456,
        "mtime_ns": 1792432290000000000,
        "device": 16777229,
        "inode": 93824028,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 404,
        "proposed_destination_name": "00404__What if a glass of water were LITERALLY half empty？ [0EytSWiKrFg].mp4",
        "fresh_stat": {
          "st_size": 6801271,
          "st_mtime_ns": 1792432290000000000,
          "st_ctime_ns": 1792830801511711231,
          "st_ino": 93824028,
          "st_dev": 16777229
        },
        "fresh_sha256": "44b332517aab51a89aa392ac1482bd852bffd90820dcada09fdbfecf091e2732",
        "hash_refreshed_utc": "2026-10-26T13:31:33.999698+00:00",
        "status": "VERIFIED",
        "remote_id": "1YC-wFVqNUjGkReIVVzXPzfwRJGBzT2ly",
        "remote_url": "https://drive.google.com/file/d/1YC-wFVqNUjGkReIVVzXPzfwRJGBzT2ly/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:27.159964+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1YC-wFVqNUjGkReIVVzXPzfwRJGBzT2ly",
            "title": "What if a glass of water were LITERALLY half empty？ [0EytSWiKrFg].mp4",
            "mime_type": "video/mp4",
            "size": "6801271",
            "url": "https://drive.google.com/file/d/1YC-wFVqNUjGkReIVVzXPzfwRJGBzT2ly/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1YC-wFVqNUjGkReIVVzXPzfwRJGBzT2ly/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:34:14.052Z",
            "modified_time": "2026-10-19T17:51:30.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 404,
          "remote_id": "1YC-wFVqNUjGkReIVVzXPzfwRJGBzT2ly",
          "retrieval_file_id": "sediment://file_00000000926081fa88b0d364c3b9361e",
          "metadata": {
            "id": "1YC-wFVqNUjGkReIVVzXPzfwRJGBzT2ly",
            "title": "What if a glass of water were LITERALLY half empty？ [0EytSWiKrFg].mp4",
            "mime_type": "video/mp4",
            "size": "6801271",
            "url": "https://drive.google.com/file/d/1YC-wFVqNUjGkReIVVzXPzfwRJGBzT2ly/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1YC-wFVqNUjGkReIVVzXPzfwRJGBzT2ly/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:34:14.052Z",
            "modified_time": "2026-10-19T17:51:30.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:53:51.054954+00:00",
          "retrieved_bytes": 6801271,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "6801271",
          "retrieved_sha256": "44b332517aab51a89aa392ac1482bd852bffd90820dcada09fdbfecf091e2732",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:53:56.561123+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if all the lightning on Earth struck the same place at once？ [fs28lEq9smw].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if all the lightning on Earth struck the same place at once？ [fs28lEq9smw].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 12300047,
        "allocated_path_bytes": 12300288,
        "mtime_ns": 1792432374000000000,
        "device": 16777229,
        "inode": 93824152,
        "nlink": 1,
        "sha256": null,
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
        "sequence": 405,
        "proposed_destination_name": "00405__What if all the lightning on Earth struck the same place at once？ [fs28lEq9smw].mp4",
        "fresh_stat": {
          "st_size": 12300047,
          "st_mtime_ns": 1792432374000000000,
          "st_ctime_ns": 1792830801517724839,
          "st_ino": 93824152,
          "st_dev": 16777229
        },
        "fresh_sha256": "5fbeb72646d1ac65ce0d3a68fbf43c3e12783db3685483bca174f91743f09c2e",
        "hash_refreshed_utc": "2026-10-26T13:31:34.008879+00:00",
        "status": "VERIFIED",
        "remote_id": "1NkkU4PES4uhW47CxX6dvj4pAwnXXP1bx",
        "remote_url": "https://drive.google.com/file/d/1NkkU4PES4uhW47CxX6dvj4pAwnXXP1bx/view?usp=drivesdk",
        "upload_utc": "2026-10-26T13:35:25.197265+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1NkkU4PES4uhW47CxX6dvj4pAwnXXP1bx",
            "title": "What if all the lightning on Earth struck the same place at once？ [fs28lEq9smw].mp4",
            "mime_type": "video/mp4",
            "size": "12300047",
            "url": "https://drive.google.com/file/d/1NkkU4PES4uhW47CxX6dvj4pAwnXXP1bx/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1NkkU4PES4uhW47CxX6dvj4pAwnXXP1bx/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:34:35.796Z",
            "modified_time": "2026-10-19T17:52:54.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "sequence": 405,
          "remote_id": "1NkkU4PES4uhW47CxX6dvj4pAwnXXP1bx",
          "retrieval_file_id": "sediment://file_00000000409481faa6133a4418d1694b",
          "metadata": {
            "id": "1NkkU4PES4uhW47CxX6dvj4pAwnXXP1bx",
            "title": "What if all the lightning on Earth struck the same place at once？ [fs28lEq9smw].mp4",
            "mime_type": "video/mp4",
            "size": "12300047",
            "url": "https://drive.google.com/file/d/1NkkU4PES4uhW47CxX6dvj4pAwnXXP1bx/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1NkkU4PES4uhW47CxX6dvj4pAwnXXP1bx/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T13:34:35.796Z",
            "modified_time": "2026-10-19T17:52:54.000Z",
            "parent_ids": [
              "1L5rki43CFKeZROIgzXVA_Bwags_-onLN"
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
          "started_utc": "2026-10-26T13:54:02.237562+00:00",
          "retrieved_bytes": 12300047,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "12300047",
          "retrieved_sha256": "5fbeb72646d1ac65ce0d3a68fbf43c3e12783db3685483bca174f91743f09c2e",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T13:54:09.235274+00:00"
        }
      }
    ],
    "uploaded_bytes": 135069719,
    "independently_retrieved_bytes": 135069719,
    "mapped_source_files": 20,
    "preflight": {
      "account": "kgk2930@gmail.com",
      "privacy": "OWNER_ONLY",
      "ui_used_gb": 4.75,
      "conservative_free_bytes": 9799726336,
      "storage_ui": "4.75 GB of 15 GB; fresh owner Google One UI, Drive4.46GB Gmail302.23MB",
      "observed_at": "2026-10-26T13:31:33.786Z",
      "five_hour_used": 26,
      "weekly_used": 11,
      "paid_credits": "0",
      "context": "Batch20 atomic receipt preserved; sufficient context, no unsaved transfer; exact meter unavailable",
      "ownership": "Stable read-only originals; protected sessions preserved",
      "destination_folder_id": "12FkMHzKAtNYleLwX2UBmbMDMlk_6sXEf",
      "charges": "Existing allowance; paid credits zero, no upgrade/payment action",
      "mac_free_bytes": 24761827328
    },
    "postflight": {
      "batch_dir": "/Users/ghilmankhan/YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd/batch-0021",
      "account": "kgk2930@gmail.com",
      "privacy": "OWNER_ONLY",
      "ui_used_gb": 4.88,
      "conservative_free_bytes": 9660139898,
      "storage_ui": "4.88GB of15GB; fresh authenticated owner Google One UI; Drive4.58GB Gmail302.23MB",
      "observed_at": "2026-10-26T13:54:47.600Z",
      "five_hour_used": 31,
      "weekly_used": 11,
      "paid_credits": "0",
      "context": "Batch20 atomic receipt preserved; sufficient context, no unsaved transfer; exact meter unavailable",
      "ownership": "Stable read-only originals; protected sessions preserved",
      "destination_folder_id": "1L5rki43CFKeZROIgzXVA_Bwags_-onLN",
      "charges": "Existing allowance; paid credits zero, no upgrade/payment action",
      "mac_free_bytes": 24740933632
    },
    "permissions": "Owner-only Restricted; no changes",
    "encryption": "Google provider managed; owner-held client key not established",
    "retention": "Until explicit owner removal approval",
    "coverage": "File-level verified recovery only; no complete-package or independent-machine recovery claim"
  },
  "recovery_mapping": {
    "files": [
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How fast could a human accellerate (while staying alive)？ [eSPcp-tfGbA].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/How fast could a human accellerate (while staying alive)？ [eSPcp-tfGbA].mp4",
        "bytes": 3964374,
        "fresh_sha256": "13bc33ec2f511cd322872d97677cf0f265695a50a6d09ded86c495f86e2ae3ea",
        "remote_id": "1klRTfU55bJeQBKhqNYBEZUqe8KFRqRiw",
        "remote_url": "https://drive.google.com/file/d/1klRTfU55bJeQBKhqNYBEZUqe8KFRqRiw/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How fast could a vehicle go around a track - but the racer does not have to survive. [rgUfcFAPicY].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/How fast could a vehicle go around a track - but the racer does not have to survive. [rgUfcFAPicY].mp4",
        "bytes": 4020273,
        "fresh_sha256": "d18d25dc30ea607c4f16838db8c594fc85bdc46e67ad723519e47636bff3e831",
        "remote_id": "1R3VdfZEeGzjFkTcEqWgAucK6RnGANFzB",
        "remote_url": "https://drive.google.com/file/d/1R3VdfZEeGzjFkTcEqWgAucK6RnGANFzB/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How high could the magnitude of Earthquakes go？ [wBLVmEZV2Oc].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/How high could the magnitude of Earthquakes go？ [wBLVmEZV2Oc].mp4",
        "bytes": 3584843,
        "fresh_sha256": "ffff4ea989fcadd3f3744b3756a5e58fc3d997c127dfac41ba6d46cd1638f5b1",
        "remote_id": "1RdiayHjSaC296SVdfvG37VuzgpyenvHE",
        "remote_url": "https://drive.google.com/file/d/1RdiayHjSaC296SVdfvG37VuzgpyenvHE/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How long could the human race survive on only cannibalism？ [jjzYUOd5HAA].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/How long could the human race survive on only cannibalism？ [jjzYUOd5HAA].mp4",
        "bytes": 3166180,
        "fresh_sha256": "d777c2589b3cbf8d4ece36df4b5bb48a6a527099b37fc93d2f2461dc7cf0c753",
        "remote_id": "1INtXlRFiLalPfUUA3Hw-CLNdR8MVK9qY",
        "remote_url": "https://drive.google.com/file/d/1INtXlRFiLalPfUUA3Hw-CLNdR8MVK9qY/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How long could you drive towards the sunset？ [rGZ6TsXvi8E].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/How long could you drive towards the sunset？ [rGZ6TsXvi8E].mp4",
        "bytes": 5941596,
        "fresh_sha256": "1e4498d55a84d0ec6d1bbd543a665ce4b47bdbff336b602d611047c63cf35189",
        "remote_id": "113DPLaT6-527A4YhZTDOyCwrxtY_If01",
        "remote_url": "https://drive.google.com/file/d/113DPLaT6-527A4YhZTDOyCwrxtY_If01/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How long would you survive with no DNA？ [s3oLIDaElaE].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/How long would you survive with no DNA？ [s3oLIDaElaE].mp4",
        "bytes": 5953255,
        "fresh_sha256": "50be6832b2e744074e47eee6672a9733eae20669f3b4f07854c204abaf1d171c",
        "remote_id": "1uIcBRSmPshoVzbQjkY2MughotywCFNbq",
        "remote_url": "https://drive.google.com/file/d/1uIcBRSmPshoVzbQjkY2MughotywCFNbq/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/How many elevators would you need in a billion-story building？ [oMtAHGv-DU4].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/How many elevators would you need in a billion-story building？ [oMtAHGv-DU4].mp4",
        "bytes": 2880001,
        "fresh_sha256": "b5e9cbbfab3c278531d54254df6dc1fea2084c3850a25ad489c6af8933cff95f",
        "remote_id": "1RTPxccNP93es1uObydD9ZlzrFhW_wRp7",
        "remote_url": "https://drive.google.com/file/d/1RTPxccNP93es1uObydD9ZlzrFhW_wRp7/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/If all humans died, when would the last light go out？ [8fADp43wJwU].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/If all humans died, when would the last light go out？ [8fADp43wJwU].mp4",
        "bytes": 11798131,
        "fresh_sha256": "973bb97ae6717fa54d42fe3524fcc6921016a65fa23ccae4b569ea62e91f2b4b",
        "remote_id": "1zYEIxVrC0VgPg4OR5vKsizdxy59nkXFa",
        "remote_url": "https://drive.google.com/file/d/1zYEIxVrC0VgPg4OR5vKsizdxy59nkXFa/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/If you put a toaster in a freezer, which wins？ [9VG0yqq_PHM].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/If you put a toaster in a freezer, which wins？ [9VG0yqq_PHM].mp4",
        "bytes": 5009650,
        "fresh_sha256": "1a5c6363860a5c2c90c608602c8c9a9e3a8241238c8d75d0d4c94a16ac6016ac",
        "remote_id": "1mFuf81sipvCJaNkuQ8oIBpv_3Wj2jYYI",
        "remote_url": "https://drive.google.com/file/d/1mFuf81sipvCJaNkuQ8oIBpv_3Wj2jYYI/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/Is there such a thing as a magnitude 0 earthquake？ [FKXVs4UteSc].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/Is there such a thing as a magnitude 0 earthquake？ [FKXVs4UteSc].mp4",
        "bytes": 3902844,
        "fresh_sha256": "ceae7efbeec972b8dee0d4ca6498a20502167d6b57a04fc37ecbd376ab466b3e",
        "remote_id": "1sflXdqwiw3FtnYFu5vo41sVkQsvERQfI",
        "remote_url": "https://drive.google.com/file/d/1sflXdqwiw3FtnYFu5vo41sVkQsvERQfI/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/More weird and worrying questions [alBQCm0QpJg].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/More weird and worrying questions [alBQCm0QpJg].mp4",
        "bytes": 9005195,
        "fresh_sha256": "41e9cd3ba2abbf3b278de04a36c182422ea60a0cc4447ea4e4d24aad9f50da56",
        "remote_id": "12cuL_Mhpmu9KHurDqt0kW2xrMYlg9dI8",
        "remote_url": "https://drive.google.com/file/d/12cuL_Mhpmu9KHurDqt0kW2xrMYlg9dI8/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/Petition to send a swimming pool to the moon! [mtTbwHzhUiM].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/Petition to send a swimming pool to the moon! [mtTbwHzhUiM].mp4",
        "bytes": 1408778,
        "fresh_sha256": "8fb3d1a30ae873e0047871202d0c59fa085f46560d61de91abf22261a6e7ea58",
        "remote_id": "1AIgOaWdoyKG8rQ8Bwej22fz4nP8HSCCF",
        "remote_url": "https://drive.google.com/file/d/1AIgOaWdoyKG8rQ8Bwej22fz4nP8HSCCF/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/Weird and worrying questions [SLd4hnmeW_g].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/Weird and worrying questions [SLd4hnmeW_g].mp4",
        "bytes": 13478240,
        "fresh_sha256": "893ebff4dda30f790f56131052879b3353d75af7ba35edece8f95bf5810a3ac5",
        "remote_id": "11up_P2_b0cNX8qoRfuv8HqWDvbRq7qe-",
        "remote_url": "https://drive.google.com/file/d/11up_P2_b0cNX8qoRfuv8HqWDvbRq7qe-/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if ALL the sun’s power was focused in one place？ [qu8nx1qUwEU].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if ALL the sun’s power was focused in one place？ [qu8nx1qUwEU].mp4",
        "bytes": 6942960,
        "fresh_sha256": "4aa23ce06382a270b60e287b062763b6d936a2af9fa8619c33ec8b408c18beea",
        "remote_id": "11mOrKDOWxsT1fbTitFoyl-0faBR7HOgb",
        "remote_url": "https://drive.google.com/file/d/11mOrKDOWxsT1fbTitFoyl-0faBR7HOgb/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if Earth grew 1cm every second？ [-1-ldW4kpLM].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if Earth grew 1cm every second？ [-1-ldW4kpLM].mp4",
        "bytes": 9486746,
        "fresh_sha256": "dce7aed164da0da8979608392520c88e295185550c0d8b18950e58666a3c26b3",
        "remote_id": "1kAyihJrHkTv_lCVYB86c6bKwNTPSz_7I",
        "remote_url": "https://drive.google.com/file/d/1kAyihJrHkTv_lCVYB86c6bKwNTPSz_7I/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if Earth suddenly stopped spinning？ [gp5G1QG6cXc].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if Earth suddenly stopped spinning？ [gp5G1QG6cXc].mp4",
        "bytes": 10418611,
        "fresh_sha256": "b0dd04e6e66fefe7c468e747fc50a0a7cea576c9019fc39af4d39d0175180248",
        "remote_id": "13G2nfEuqKDZROQsal5l9BSEl2lI8v-oA",
        "remote_url": "https://drive.google.com/file/d/13G2nfEuqKDZROQsal5l9BSEl2lI8v-oA/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if Earth’s Water Suddenly Disappeared？ [4ZVtHknKuvg].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if Earth’s Water Suddenly Disappeared？ [4ZVtHknKuvg].mp4",
        "bytes": 6088613,
        "fresh_sha256": "fd96c7878fd8713e45ce1e29784fde7e42d6ba4374844844c7482edda703f1c8",
        "remote_id": "1fW4hdKy8q1C0DQq0UJ1e34r2rr_1qT0j",
        "remote_url": "https://drive.google.com/file/d/1fW4hdKy8q1C0DQq0UJ1e34r2rr_1qT0j/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if NASCAR had no rules？ [JcXpCyPc2Xw].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if NASCAR had no rules？ [JcXpCyPc2Xw].mp4",
        "bytes": 8918111,
        "fresh_sha256": "a8aa9dbcd4cf3510e31d11b6c38e4106a5d6d103c55388ec480a0e3b06245d5e",
        "remote_id": "1WWolOAXo5_WtU4WDiRKLtrN9cIpNJocH",
        "remote_url": "https://drive.google.com/file/d/1WWolOAXo5_WtU4WDiRKLtrN9cIpNJocH/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if a glass of water were LITERALLY half empty？ [0EytSWiKrFg].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if a glass of water were LITERALLY half empty？ [0EytSWiKrFg].mp4",
        "bytes": 6801271,
        "fresh_sha256": "44b332517aab51a89aa392ac1482bd852bffd90820dcada09fdbfecf091e2732",
        "remote_id": "1YC-wFVqNUjGkReIVVzXPzfwRJGBzT2ly",
        "remote_url": "https://drive.google.com/file/d/1YC-wFVqNUjGkReIVVzXPzfwRJGBzT2ly/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if all the lightning on Earth struck the same place at once？ [fs28lEq9smw].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if all the lightning on Earth struck the same place at once？ [fs28lEq9smw].mp4",
        "bytes": 12300047,
        "fresh_sha256": "5fbeb72646d1ac65ce0d3a68fbf43c3e12783db3685483bca174f91743f09c2e",
        "remote_id": "1NkkU4PES4uhW47CxX6dvj4pAwnXXP1bx",
        "remote_url": "https://drive.google.com/file/d/1NkkU4PES4uhW47CxX6dvj4pAwnXXP1bx/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      }
    ]
  },
  "cumulative_before_this_control": {
    "mapped_source_paths": 413,
    "uploaded_bytes_including_controls": 4378694907,
    "verified_bytes_including_controls": 4378694907,
    "remaining_payload_bytes": 7621305093,
    "remaining_plan_files": 139
  }
}
```
