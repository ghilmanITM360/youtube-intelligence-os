# YIOS Batch23 verified recovery receipt

Status VERIFIED. Uploaded bytes: 107,603,827; complete independently retrieved SHA-256 verified bytes: 107,603,827. Source mappings: 20.

All-in physical uploaded bytes before this MD: 4,641,558,318; independently verified bytes: 4,641,558,318. This MD is additional payload, counted by its separate CONTROL-UPLOAD/VERIFY receipts after complete independent readback. No duplicate/partial I/O is counted as new recovery coverage.

Authenticated owner kgk2930@gmail.com; approved private yios hierarchy. Actual namespace IDs, source paths, hashes, bytes and remote object IDs follow. Source stability and current owner/private/parent/size gates passed. No source deletion/move/cleanup, Git/PR/branch/stash/LFS/production mutation, payment or reset credit use by this backup. This is file-level cloud recovery; independent-machine disaster recovery and production ownership acceptance remain unproven.

```json
{
  "receipt": {
    "status": "VERIFIED",
    "batch": 23,
    "completed_utc": "2026-10-26T14:40:49.842432+00:00",
    "files": [
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you drained the oceans？ [Jpy55EgMQgY].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you drained the oceans？ [Jpy55EgMQgY].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 7419676,
        "allocated_path_bytes": 7421952,
        "mtime_ns": 1792432356000000000,
        "device": 16777229,
        "inode": 93824159,
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
        "sequence": 426,
        "proposed_destination_name": "00426__What if you drained the oceans？ [Jpy55EgMQgY].mp4",
        "fresh_stat": {
          "st_size": 7419676,
          "st_mtime_ns": 1792432356000000000,
          "st_ctime_ns": 1792830801517780922,
          "st_ino": 93824159,
          "st_dev": 16777229
        },
        "fresh_sha256": "878e9d1518198312bc264c8f645925c87f8b5c50822c93caac2f86d115204f1d",
        "hash_refreshed_utc": "2026-10-26T14:25:33.779098+00:00",
        "status": "VERIFIED",
        "remote_id": "1tFKtI-vTLOmL6_PCKr0wTxE50B4llCQ9",
        "remote_url": "https://drive.google.com/file/d/1tFKtI-vTLOmL6_PCKr0wTxE50B4llCQ9/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:13.906905+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1tFKtI-vTLOmL6_PCKr0wTxE50B4llCQ9",
            "title": "What if you drained the oceans？ [Jpy55EgMQgY].mp4",
            "mime_type": "video/mp4",
            "size": "7419676",
            "url": "https://drive.google.com/file/d/1tFKtI-vTLOmL6_PCKr0wTxE50B4llCQ9/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1tFKtI-vTLOmL6_PCKr0wTxE50B4llCQ9/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:27:33.480Z",
            "modified_time": "2026-10-19T17:52:36.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 426,
          "remote_id": "1tFKtI-vTLOmL6_PCKr0wTxE50B4llCQ9",
          "retrieval_file_id": "sediment://file_00000000c82482118be395fd5591ff24",
          "metadata": {
            "id": "1tFKtI-vTLOmL6_PCKr0wTxE50B4llCQ9",
            "title": "What if you drained the oceans？ [Jpy55EgMQgY].mp4",
            "mime_type": "video/mp4",
            "size": "7419676",
            "url": "https://drive.google.com/file/d/1tFKtI-vTLOmL6_PCKr0wTxE50B4llCQ9/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1tFKtI-vTLOmL6_PCKr0wTxE50B4llCQ9/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:27:33.480Z",
            "modified_time": "2026-10-19T17:52:36.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:32:28.514924+00:00",
          "retrieved_bytes": 7419676,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "7419676",
          "retrieved_sha256": "878e9d1518198312bc264c8f645925c87f8b5c50822c93caac2f86d115204f1d",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:33:36.491573+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you drained the oceans？ [aMshLs0YCTQ].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you drained the oceans？ [aMshLs0YCTQ].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 4446513,
        "allocated_path_bytes": 4448256,
        "mtime_ns": 1792432548000000000,
        "device": 16777229,
        "inode": 93824280,
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
        "sequence": 427,
        "proposed_destination_name": "00427__What if you drained the oceans？ [aMshLs0YCTQ].mp4",
        "fresh_stat": {
          "st_size": 4446513,
          "st_mtime_ns": 1792432548000000000,
          "st_ctime_ns": 1792830801519262752,
          "st_ino": 93824280,
          "st_dev": 16777229
        },
        "fresh_sha256": "911525e63c0e1bc6aa08dbead51b6a6ea801a077bebf28da50228d761b2685e4",
        "hash_refreshed_utc": "2026-10-26T14:25:33.783438+00:00",
        "status": "VERIFIED",
        "remote_id": "1IqkfhEfHn-5Le4tZ54qpTaQ1sc3sy9Y1",
        "remote_url": "https://drive.google.com/file/d/1IqkfhEfHn-5Le4tZ54qpTaQ1sc3sy9Y1/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:05.013028+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1IqkfhEfHn-5Le4tZ54qpTaQ1sc3sy9Y1",
            "title": "What if you drained the oceans？ [aMshLs0YCTQ].mp4",
            "mime_type": "video/mp4",
            "size": "4446513",
            "url": "https://drive.google.com/file/d/1IqkfhEfHn-5Le4tZ54qpTaQ1sc3sy9Y1/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1IqkfhEfHn-5Le4tZ54qpTaQ1sc3sy9Y1/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:27:40.978Z",
            "modified_time": "2026-10-19T17:55:48.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 427,
          "remote_id": "1IqkfhEfHn-5Le4tZ54qpTaQ1sc3sy9Y1",
          "retrieval_file_id": "sediment://file_000000008dec8211b8876d40d76c3644",
          "metadata": {
            "id": "1IqkfhEfHn-5Le4tZ54qpTaQ1sc3sy9Y1",
            "title": "What if you drained the oceans？ [aMshLs0YCTQ].mp4",
            "mime_type": "video/mp4",
            "size": "4446513",
            "url": "https://drive.google.com/file/d/1IqkfhEfHn-5Le4tZ54qpTaQ1sc3sy9Y1/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1IqkfhEfHn-5Le4tZ54qpTaQ1sc3sy9Y1/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:27:40.978Z",
            "modified_time": "2026-10-19T17:55:48.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:33:42.091819+00:00",
          "retrieved_bytes": 4446513,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "4446513",
          "retrieved_sha256": "911525e63c0e1bc6aa08dbead51b6a6ea801a077bebf28da50228d761b2685e4",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:33:46.155151+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you dropped a bowling ball in the Mariana Trench？ [FYoHYq8VRt0].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you dropped a bowling ball in the Mariana Trench？ [FYoHYq8VRt0].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 5080341,
        "allocated_path_bytes": 5083136,
        "mtime_ns": 1792432172000000000,
        "device": 16777229,
        "inode": 93824165,
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
        "sequence": 428,
        "proposed_destination_name": "00428__What if you dropped a bowling ball in the Mariana Trench？ [FYoHYq8VRt0].mp4",
        "fresh_stat": {
          "st_size": 5080341,
          "st_mtime_ns": 1792432172000000000,
          "st_ctime_ns": 1792830801517878005,
          "st_ino": 93824165,
          "st_dev": 16777229
        },
        "fresh_sha256": "d84737cd6b7d53c796f66b5552f36af728f525b364df2785d85e920d0887f523",
        "hash_refreshed_utc": "2026-10-26T14:25:33.787708+00:00",
        "status": "VERIFIED",
        "remote_id": "1SHRLQBz6EU7DhC77WUlzq-tbPp1JwB9N",
        "remote_url": "https://drive.google.com/file/d/1SHRLQBz6EU7DhC77WUlzq-tbPp1JwB9N/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:22.567554+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1SHRLQBz6EU7DhC77WUlzq-tbPp1JwB9N",
            "title": "What if you dropped a bowling ball in the Mariana Trench？ [FYoHYq8VRt0].mp4",
            "mime_type": "video/mp4",
            "size": "5080341",
            "url": "https://drive.google.com/file/d/1SHRLQBz6EU7DhC77WUlzq-tbPp1JwB9N/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1SHRLQBz6EU7DhC77WUlzq-tbPp1JwB9N/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:27:48.493Z",
            "modified_time": "2026-10-19T17:49:32.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 428,
          "remote_id": "1SHRLQBz6EU7DhC77WUlzq-tbPp1JwB9N",
          "retrieval_file_id": "sediment://file_00000000bd0482078eeac34d359906eb",
          "metadata": {
            "id": "1SHRLQBz6EU7DhC77WUlzq-tbPp1JwB9N",
            "title": "What if you dropped a bowling ball in the Mariana Trench？ [FYoHYq8VRt0].mp4",
            "mime_type": "video/mp4",
            "size": "5080341",
            "url": "https://drive.google.com/file/d/1SHRLQBz6EU7DhC77WUlzq-tbPp1JwB9N/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1SHRLQBz6EU7DhC77WUlzq-tbPp1JwB9N/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:27:48.493Z",
            "modified_time": "2026-10-19T17:49:32.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:33:50.724515+00:00",
          "retrieved_bytes": 5080341,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "5080341",
          "retrieved_sha256": "d84737cd6b7d53c796f66b5552f36af728f525b364df2785d85e920d0887f523",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:33:56.413732+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you floated upwards 1 ft every second？ [oTzW-mTQd5w].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you floated upwards 1 ft every second？ [oTzW-mTQd5w].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 4762379,
        "allocated_path_bytes": 4763648,
        "mtime_ns": 1792432186000000000,
        "device": 16777229,
        "inode": 93824251,
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
        "sequence": 429,
        "proposed_destination_name": "00429__What if you floated upwards 1 ft every second？ [oTzW-mTQd5w].mp4",
        "fresh_stat": {
          "st_size": 4762379,
          "st_mtime_ns": 1792432186000000000,
          "st_ctime_ns": 1792830801519089044,
          "st_ino": 93824251,
          "st_dev": 16777229
        },
        "fresh_sha256": "2c2aaa0047c94c793068f51f9f041cbbd36edcc0642d79a77136009804de6dec",
        "hash_refreshed_utc": "2026-10-26T14:25:33.792596+00:00",
        "status": "VERIFIED",
        "remote_id": "1nRkJ4z_HwnwAHokm1XQwuTPVRi6AN_Pp",
        "remote_url": "https://drive.google.com/file/d/1nRkJ4z_HwnwAHokm1XQwuTPVRi6AN_Pp/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:20.827082+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1nRkJ4z_HwnwAHokm1XQwuTPVRi6AN_Pp",
            "title": "What if you floated upwards 1 ft every second？ [oTzW-mTQd5w].mp4",
            "mime_type": "video/mp4",
            "size": "4762379",
            "url": "https://drive.google.com/file/d/1nRkJ4z_HwnwAHokm1XQwuTPVRi6AN_Pp/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1nRkJ4z_HwnwAHokm1XQwuTPVRi6AN_Pp/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:27:44.620Z",
            "modified_time": "2026-10-19T17:49:46.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 429,
          "remote_id": "1nRkJ4z_HwnwAHokm1XQwuTPVRi6AN_Pp",
          "retrieval_file_id": "sediment://file_00000000c5a4821182f7017a32a8df2c",
          "metadata": {
            "id": "1nRkJ4z_HwnwAHokm1XQwuTPVRi6AN_Pp",
            "title": "What if you floated upwards 1 ft every second？ [oTzW-mTQd5w].mp4",
            "mime_type": "video/mp4",
            "size": "4762379",
            "url": "https://drive.google.com/file/d/1nRkJ4z_HwnwAHokm1XQwuTPVRi6AN_Pp/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1nRkJ4z_HwnwAHokm1XQwuTPVRi6AN_Pp/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:27:44.620Z",
            "modified_time": "2026-10-19T17:49:46.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:34:01.625506+00:00",
          "retrieved_bytes": 4762379,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "4762379",
          "retrieved_sha256": "2c2aaa0047c94c793068f51f9f041cbbd36edcc0642d79a77136009804de6dec",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:34:05.867065+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you funneled Niagara Falls through a straw？ [pfbzrrcQZjs].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you funneled Niagara Falls through a straw？ [pfbzrrcQZjs].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 6045501,
        "allocated_path_bytes": 6045696,
        "mtime_ns": 1792432232000000000,
        "device": 16777229,
        "inode": 93824185,
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
        "sequence": 430,
        "proposed_destination_name": "00430__What if you funneled Niagara Falls through a straw？ [pfbzrrcQZjs].mp4",
        "fresh_stat": {
          "st_size": 6045501,
          "st_mtime_ns": 1792432232000000000,
          "st_ctime_ns": 1792830801518148088,
          "st_ino": 93824185,
          "st_dev": 16777229
        },
        "fresh_sha256": "22e9d80bbe80eb281af4210f666412ca0d38d141acee255e420fed6b3a971b11",
        "hash_refreshed_utc": "2026-10-26T14:25:33.797763+00:00",
        "status": "VERIFIED",
        "remote_id": "1oaECLrmIYfCEc1_6swIdQHniniDdCfSP",
        "remote_url": "https://drive.google.com/file/d/1oaECLrmIYfCEc1_6swIdQHniniDdCfSP/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:17.479483+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1oaECLrmIYfCEc1_6swIdQHniniDdCfSP",
            "title": "What if you funneled Niagara Falls through a straw？ [pfbzrrcQZjs].mp4",
            "mime_type": "video/mp4",
            "size": "6045501",
            "url": "https://drive.google.com/file/d/1oaECLrmIYfCEc1_6swIdQHniniDdCfSP/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1oaECLrmIYfCEc1_6swIdQHniniDdCfSP/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:27:58.825Z",
            "modified_time": "2026-10-19T17:50:32.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 430,
          "remote_id": "1oaECLrmIYfCEc1_6swIdQHniniDdCfSP",
          "retrieval_file_id": "sediment://file_000000002cf08211a2ab70aa857fe094",
          "metadata": {
            "id": "1oaECLrmIYfCEc1_6swIdQHniniDdCfSP",
            "title": "What if you funneled Niagara Falls through a straw？ [pfbzrrcQZjs].mp4",
            "mime_type": "video/mp4",
            "size": "6045501",
            "url": "https://drive.google.com/file/d/1oaECLrmIYfCEc1_6swIdQHniniDdCfSP/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1oaECLrmIYfCEc1_6swIdQHniniDdCfSP/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:27:58.825Z",
            "modified_time": "2026-10-19T17:50:32.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:36:06.853401+00:00",
          "retrieved_bytes": 6045501,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "6045501",
          "retrieved_sha256": "22e9d80bbe80eb281af4210f666412ca0d38d141acee255e420fed6b3a971b11",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:36:13.108408+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you funneled the Niagara Falls through a straw？ [QZIEjvSlOMQ].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you funneled the Niagara Falls through a straw？ [QZIEjvSlOMQ].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 3066480,
        "allocated_path_bytes": 3067904,
        "mtime_ns": 1792432472000000000,
        "device": 16777229,
        "inode": 93824234,
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
        "sequence": 431,
        "proposed_destination_name": "00431__What if you funneled the Niagara Falls through a straw？ [QZIEjvSlOMQ].mp4",
        "fresh_stat": {
          "st_size": 3066480,
          "st_mtime_ns": 1792432472000000000,
          "st_ctime_ns": 1792830801518933211,
          "st_ino": 93824234,
          "st_dev": 16777229
        },
        "fresh_sha256": "e505229283f8c53c1a2ab068073b5b574d47efe95bd2ae179572d6f7fce44aad",
        "hash_refreshed_utc": "2026-10-26T14:25:33.801563+00:00",
        "status": "VERIFIED",
        "remote_id": "1_tW_zvtWj622rKFS8nyuySzQlw7KMG8E",
        "remote_url": "https://drive.google.com/file/d/1_tW_zvtWj622rKFS8nyuySzQlw7KMG8E/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:10.043269+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1_tW_zvtWj622rKFS8nyuySzQlw7KMG8E",
            "title": "What if you funneled the Niagara Falls through a straw？ [QZIEjvSlOMQ].mp4",
            "mime_type": "video/mp4",
            "size": "3066480",
            "url": "https://drive.google.com/file/d/1_tW_zvtWj622rKFS8nyuySzQlw7KMG8E/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1_tW_zvtWj622rKFS8nyuySzQlw7KMG8E/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:27:51.769Z",
            "modified_time": "2026-10-19T17:54:32.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 431,
          "remote_id": "1_tW_zvtWj622rKFS8nyuySzQlw7KMG8E",
          "retrieval_file_id": "sediment://file_00000000424c8207ac9c0f3c497d0283",
          "metadata": {
            "id": "1_tW_zvtWj622rKFS8nyuySzQlw7KMG8E",
            "title": "What if you funneled the Niagara Falls through a straw？ [QZIEjvSlOMQ].mp4",
            "mime_type": "video/mp4",
            "size": "3066480",
            "url": "https://drive.google.com/file/d/1_tW_zvtWj622rKFS8nyuySzQlw7KMG8E/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1_tW_zvtWj622rKFS8nyuySzQlw7KMG8E/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:27:51.769Z",
            "modified_time": "2026-10-19T17:54:32.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:36:17.101736+00:00",
          "retrieved_bytes": 3066480,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "3066480",
          "retrieved_sha256": "e505229283f8c53c1a2ab068073b5b574d47efe95bd2ae179572d6f7fce44aad",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:36:20.625315+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you had a mole of moles？ [lLlwvmu1ZeA].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you had a mole of moles？ [lLlwvmu1ZeA].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 7433534,
        "allocated_path_bytes": 7434240,
        "mtime_ns": 1792432222000000000,
        "device": 16777229,
        "inode": 93824133,
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
        "sequence": 432,
        "proposed_destination_name": "00432__What if you had a mole of moles？ [lLlwvmu1ZeA].mp4",
        "fresh_stat": {
          "st_size": 7433534,
          "st_mtime_ns": 1792432222000000000,
          "st_ctime_ns": 1792830801517572131,
          "st_ino": 93824133,
          "st_dev": 16777229
        },
        "fresh_sha256": "d5cf881bd05e7033be9d1397b55cc06be0b824f370bde9234fba7fa325c6db10",
        "hash_refreshed_utc": "2026-10-26T14:25:33.808146+00:00",
        "status": "VERIFIED",
        "remote_id": "1tk4SO9YzxGbJ0NeKzX9opppB0SqtJEk9",
        "remote_url": "https://drive.google.com/file/d/1tk4SO9YzxGbJ0NeKzX9opppB0SqtJEk9/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:18.755616+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1tk4SO9YzxGbJ0NeKzX9opppB0SqtJEk9",
            "title": "What if you had a mole of moles？ [lLlwvmu1ZeA].mp4",
            "mime_type": "video/mp4",
            "size": "7433534",
            "url": "https://drive.google.com/file/d/1tk4SO9YzxGbJ0NeKzX9opppB0SqtJEk9/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1tk4SO9YzxGbJ0NeKzX9opppB0SqtJEk9/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:07.698Z",
            "modified_time": "2026-10-19T17:50:22.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 432,
          "remote_id": "1tk4SO9YzxGbJ0NeKzX9opppB0SqtJEk9",
          "retrieval_file_id": "sediment://file_00000000cf288207b9598a5cc4416f21",
          "metadata": {
            "id": "1tk4SO9YzxGbJ0NeKzX9opppB0SqtJEk9",
            "title": "What if you had a mole of moles？ [lLlwvmu1ZeA].mp4",
            "mime_type": "video/mp4",
            "size": "7433534",
            "url": "https://drive.google.com/file/d/1tk4SO9YzxGbJ0NeKzX9opppB0SqtJEk9/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1tk4SO9YzxGbJ0NeKzX9opppB0SqtJEk9/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:07.698Z",
            "modified_time": "2026-10-19T17:50:22.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:36:26.319850+00:00",
          "retrieved_bytes": 7433534,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "7433534",
          "retrieved_sha256": "d5cf881bd05e7033be9d1397b55cc06be0b824f370bde9234fba7fa325c6db10",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:36:32.121844+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you had literally had all of the world_s money？ [jVy3qd70AqU].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you had literally had all of the world_s money？ [jVy3qd70AqU].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 3244125,
        "allocated_path_bytes": 3248128,
        "mtime_ns": 1792432478000000000,
        "device": 16777229,
        "inode": 93824294,
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
        "sequence": 433,
        "proposed_destination_name": "00433__What if you had literally had all of the world_s money？ [jVy3qd70AqU].mp4",
        "fresh_stat": {
          "st_size": 3244125,
          "st_mtime_ns": 1792432478000000000,
          "st_ctime_ns": 1792830801519362834,
          "st_ino": 93824294,
          "st_dev": 16777229
        },
        "fresh_sha256": "b0e46c95279dc6a14d40e1f5f6d9bcf77cfbecaa7bd852811571ffbd5f227ae0",
        "hash_refreshed_utc": "2026-10-26T14:25:33.811996+00:00",
        "status": "VERIFIED",
        "remote_id": "1C0uW3TiVfVwKXspTtBG27B1PXgq5JtTo",
        "remote_url": "https://drive.google.com/file/d/1C0uW3TiVfVwKXspTtBG27B1PXgq5JtTo/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:09.231764+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1C0uW3TiVfVwKXspTtBG27B1PXgq5JtTo",
            "title": "What if you had literally had all of the world_s money？ [jVy3qd70AqU].mp4",
            "mime_type": "video/mp4",
            "size": "3244125",
            "url": "https://drive.google.com/file/d/1C0uW3TiVfVwKXspTtBG27B1PXgq5JtTo/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1C0uW3TiVfVwKXspTtBG27B1PXgq5JtTo/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:10.902Z",
            "modified_time": "2026-10-19T17:54:38.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 433,
          "remote_id": "1C0uW3TiVfVwKXspTtBG27B1PXgq5JtTo",
          "retrieval_file_id": "sediment://file_0000000013b0821181e201022ec75f86",
          "metadata": {
            "id": "1C0uW3TiVfVwKXspTtBG27B1PXgq5JtTo",
            "title": "What if you had literally had all of the world_s money？ [jVy3qd70AqU].mp4",
            "mime_type": "video/mp4",
            "size": "3244125",
            "url": "https://drive.google.com/file/d/1C0uW3TiVfVwKXspTtBG27B1PXgq5JtTo/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1C0uW3TiVfVwKXspTtBG27B1PXgq5JtTo/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:10.902Z",
            "modified_time": "2026-10-19T17:54:38.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:36:36.677480+00:00",
          "retrieved_bytes": 3244125,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "3244125",
          "retrieved_sha256": "b0e46c95279dc6a14d40e1f5f6d9bcf77cfbecaa7bd852811571ffbd5f227ae0",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:36:40.160451+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you kept digging downward？ [r7B0MzvwDcA].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you kept digging downward？ [r7B0MzvwDcA].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 5283281,
        "allocated_path_bytes": 5283840,
        "mtime_ns": 1792432178000000000,
        "device": 16777229,
        "inode": 93824147,
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
        "sequence": 434,
        "proposed_destination_name": "00434__What if you kept digging downward？ [r7B0MzvwDcA].mp4",
        "fresh_stat": {
          "st_size": 5283281,
          "st_mtime_ns": 1792432178000000000,
          "st_ctime_ns": 1792830801517664423,
          "st_ino": 93824147,
          "st_dev": 16777229
        },
        "fresh_sha256": "d325348a0c3cc31f91e97e9495960b5141dd99226ee030777845cac8dbc7d63b",
        "hash_refreshed_utc": "2026-10-26T14:25:33.816107+00:00",
        "status": "VERIFIED",
        "remote_id": "1UFJySTCzdjkIfuxViS6oX83kQpCompIs",
        "remote_url": "https://drive.google.com/file/d/1UFJySTCzdjkIfuxViS6oX83kQpCompIs/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:21.702263+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1UFJySTCzdjkIfuxViS6oX83kQpCompIs",
            "title": "What if you kept digging downward？ [r7B0MzvwDcA].mp4",
            "mime_type": "video/mp4",
            "size": "5283281",
            "url": "https://drive.google.com/file/d/1UFJySTCzdjkIfuxViS6oX83kQpCompIs/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1UFJySTCzdjkIfuxViS6oX83kQpCompIs/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:27:37.264Z",
            "modified_time": "2026-10-19T17:49:38.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 434,
          "remote_id": "1UFJySTCzdjkIfuxViS6oX83kQpCompIs",
          "retrieval_file_id": "sediment://file_00000000ce9882119b38da7433ef089f",
          "metadata": {
            "id": "1UFJySTCzdjkIfuxViS6oX83kQpCompIs",
            "title": "What if you kept digging downward？ [r7B0MzvwDcA].mp4",
            "mime_type": "video/mp4",
            "size": "5283281",
            "url": "https://drive.google.com/file/d/1UFJySTCzdjkIfuxViS6oX83kQpCompIs/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1UFJySTCzdjkIfuxViS6oX83kQpCompIs/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:27:37.264Z",
            "modified_time": "2026-10-19T17:49:38.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:36:47.393237+00:00",
          "retrieved_bytes": 5283281,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "5283281",
          "retrieved_sha256": "d325348a0c3cc31f91e97e9495960b5141dd99226ee030777845cac8dbc7d63b",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:36:51.672249+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you literally had all the money in the world？ [saj7b5C6TCM].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you literally had all the money in the world？ [saj7b5C6TCM].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 5790859,
        "allocated_path_bytes": 5791744,
        "mtime_ns": 1792432238000000000,
        "device": 16777229,
        "inode": 93824199,
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
        "sequence": 435,
        "proposed_destination_name": "00435__What if you literally had all the money in the world？ [saj7b5C6TCM].mp4",
        "fresh_stat": {
          "st_size": 5790859,
          "st_mtime_ns": 1792432238000000000,
          "st_ctime_ns": 1792830801518443671,
          "st_ino": 93824199,
          "st_dev": 16777229
        },
        "fresh_sha256": "579c074f451897ef08c6c6e1f239f34b7f874dc4bdaf2e25ad7814d9d5342e37",
        "hash_refreshed_utc": "2026-10-26T14:25:33.820522+00:00",
        "status": "VERIFIED",
        "remote_id": "1QJh07dHH-bHvtDw-lN1d-9cHw6chy6lt",
        "remote_url": "https://drive.google.com/file/d/1QJh07dHH-bHvtDw-lN1d-9cHw6chy6lt/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:15.618878+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1QJh07dHH-bHvtDw-lN1d-9cHw6chy6lt",
            "title": "What if you literally had all the money in the world？ [saj7b5C6TCM].mp4",
            "mime_type": "video/mp4",
            "size": "5790859",
            "url": "https://drive.google.com/file/d/1QJh07dHH-bHvtDw-lN1d-9cHw6chy6lt/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1QJh07dHH-bHvtDw-lN1d-9cHw6chy6lt/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:02.775Z",
            "modified_time": "2026-10-19T17:50:38.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 435,
          "remote_id": "1QJh07dHH-bHvtDw-lN1d-9cHw6chy6lt",
          "retrieval_file_id": "sediment://file_00000000b8bc82119f6e69a3dfaa8385",
          "metadata": {
            "id": "1QJh07dHH-bHvtDw-lN1d-9cHw6chy6lt",
            "title": "What if you literally had all the money in the world？ [saj7b5C6TCM].mp4",
            "mime_type": "video/mp4",
            "size": "5790859",
            "url": "https://drive.google.com/file/d/1QJh07dHH-bHvtDw-lN1d-9cHw6chy6lt/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1QJh07dHH-bHvtDw-lN1d-9cHw6chy6lt/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:02.775Z",
            "modified_time": "2026-10-19T17:50:38.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:36:56.607422+00:00",
          "retrieved_bytes": 5790859,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "5790859",
          "retrieved_sha256": "579c074f451897ef08c6c6e1f239f34b7f874dc4bdaf2e25ad7814d9d5342e37",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:36:59.592756+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you made a jetpack using rifles？ [IdlQsjq5vKo].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you made a jetpack using rifles？ [IdlQsjq5vKo].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 7889651,
        "allocated_path_bytes": 7892992,
        "mtime_ns": 1792432192000000000,
        "device": 16777229,
        "inode": 93824215,
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
        "sequence": 436,
        "proposed_destination_name": "00436__What if you made a jetpack using rifles？ [IdlQsjq5vKo].mp4",
        "fresh_stat": {
          "st_size": 7889651,
          "st_mtime_ns": 1792432192000000000,
          "st_ctime_ns": 1792830801518693336,
          "st_ino": 93824215,
          "st_dev": 16777229
        },
        "fresh_sha256": "3961fc65194672d670462cee63a3987e11f4b3f37432ac9115deeb4a457ebbba",
        "hash_refreshed_utc": "2026-10-26T14:25:33.826919+00:00",
        "status": "VERIFIED",
        "remote_id": "1lVq4hD2Qts_Ryhe1eNZGB5n5elIg5F19",
        "remote_url": "https://drive.google.com/file/d/1lVq4hD2Qts_Ryhe1eNZGB5n5elIg5F19/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:19.977125+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1lVq4hD2Qts_Ryhe1eNZGB5n5elIg5F19",
            "title": "What if you made a jetpack using rifles？ [IdlQsjq5vKo].mp4",
            "mime_type": "video/mp4",
            "size": "7889651",
            "url": "https://drive.google.com/file/d/1lVq4hD2Qts_Ryhe1eNZGB5n5elIg5F19/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1lVq4hD2Qts_Ryhe1eNZGB5n5elIg5F19/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:30:35.660Z",
            "modified_time": "2026-10-19T17:49:52.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 436,
          "remote_id": "1lVq4hD2Qts_Ryhe1eNZGB5n5elIg5F19",
          "retrieval_file_id": "sediment://file_00000000ac8482078ec9a054338c52cc",
          "metadata": {
            "id": "1lVq4hD2Qts_Ryhe1eNZGB5n5elIg5F19",
            "title": "What if you made a jetpack using rifles？ [IdlQsjq5vKo].mp4",
            "mime_type": "video/mp4",
            "size": "7889651",
            "url": "https://drive.google.com/file/d/1lVq4hD2Qts_Ryhe1eNZGB5n5elIg5F19/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1lVq4hD2Qts_Ryhe1eNZGB5n5elIg5F19/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:30:35.660Z",
            "modified_time": "2026-10-19T17:49:52.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:37:03.328041+00:00",
          "retrieved_bytes": 7889651,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "7889651",
          "retrieved_sha256": "3961fc65194672d670462cee63a3987e11f4b3f37432ac9115deeb4a457ebbba",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:37:11.588169+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you printed all of Wikipedia？ [WQTNLuhfkwk].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you printed all of Wikipedia？ [WQTNLuhfkwk].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 3701170,
        "allocated_path_bytes": 3702784,
        "mtime_ns": 1792432538000000000,
        "device": 16777229,
        "inode": 93824181,
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
        "sequence": 437,
        "proposed_destination_name": "00437__What if you printed all of Wikipedia？ [WQTNLuhfkwk].mp4",
        "fresh_stat": {
          "st_size": 3701170,
          "st_mtime_ns": 1792432538000000000,
          "st_ctime_ns": 1792830801518085046,
          "st_ino": 93824181,
          "st_dev": 16777229
        },
        "fresh_sha256": "55d7ac17bd042a05af83c72689d12ffaf58c9f26502fc18ed103d96ddbc92ffb",
        "hash_refreshed_utc": "2026-10-26T14:25:33.830685+00:00",
        "status": "VERIFIED",
        "remote_id": "1C08aBvOlKA8GC8wEuJ4eJ_3S9O2FQ0q6",
        "remote_url": "https://drive.google.com/file/d/1C08aBvOlKA8GC8wEuJ4eJ_3S9O2FQ0q6/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:06.795017+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1C08aBvOlKA8GC8wEuJ4eJ_3S9O2FQ0q6",
            "title": "What if you printed all of Wikipedia？ [WQTNLuhfkwk].mp4",
            "mime_type": "video/mp4",
            "size": "3701170",
            "url": "https://drive.google.com/file/d/1C08aBvOlKA8GC8wEuJ4eJ_3S9O2FQ0q6/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1C08aBvOlKA8GC8wEuJ4eJ_3S9O2FQ0q6/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:28.005Z",
            "modified_time": "2026-10-19T17:55:38.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 437,
          "remote_id": "1C08aBvOlKA8GC8wEuJ4eJ_3S9O2FQ0q6",
          "retrieval_file_id": "sediment://file_00000000d35882119b5d096185dd8386",
          "metadata": {
            "id": "1C08aBvOlKA8GC8wEuJ4eJ_3S9O2FQ0q6",
            "title": "What if you printed all of Wikipedia？ [WQTNLuhfkwk].mp4",
            "mime_type": "video/mp4",
            "size": "3701170",
            "url": "https://drive.google.com/file/d/1C08aBvOlKA8GC8wEuJ4eJ_3S9O2FQ0q6/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1C08aBvOlKA8GC8wEuJ4eJ_3S9O2FQ0q6/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:28.005Z",
            "modified_time": "2026-10-19T17:55:38.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:37:16.692417+00:00",
          "retrieved_bytes": 3701170,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "3701170",
          "retrieved_sha256": "55d7ac17bd042a05af83c72689d12ffaf58c9f26502fc18ed103d96ddbc92ffb",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:37:20.907673+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you swam in a nuclear storage pool？ [EFRUL7vKdU8].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you swam in a nuclear storage pool？ [EFRUL7vKdU8].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 6749914,
        "allocated_path_bytes": 6750208,
        "mtime_ns": 1792432384000000000,
        "device": 16777229,
        "inode": 93824242,
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
        "sequence": 438,
        "proposed_destination_name": "00438__What if you swam in a nuclear storage pool？ [EFRUL7vKdU8].mp4",
        "fresh_stat": {
          "st_size": 6749914,
          "st_mtime_ns": 1792432384000000000,
          "st_ctime_ns": 1792830801519024377,
          "st_ino": 93824242,
          "st_dev": 16777229
        },
        "fresh_sha256": "8c6f896fb46a65670c7748f397704424276f63b62b92c4bbf81ed94d8f248175",
        "hash_refreshed_utc": "2026-10-26T14:25:33.836640+00:00",
        "status": "VERIFIED",
        "remote_id": "1vP-rEAG4EK0YbWt48UcAZrhC186NoCmw",
        "remote_url": "https://drive.google.com/file/d/1vP-rEAG4EK0YbWt48UcAZrhC186NoCmw/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:12.389812+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1vP-rEAG4EK0YbWt48UcAZrhC186NoCmw",
            "title": "What if you swam in a nuclear storage pool？ [EFRUL7vKdU8].mp4",
            "mime_type": "video/mp4",
            "size": "6749914",
            "url": "https://drive.google.com/file/d/1vP-rEAG4EK0YbWt48UcAZrhC186NoCmw/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1vP-rEAG4EK0YbWt48UcAZrhC186NoCmw/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:32.121Z",
            "modified_time": "2026-10-19T17:53:04.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 438,
          "remote_id": "1vP-rEAG4EK0YbWt48UcAZrhC186NoCmw",
          "retrieval_file_id": "sediment://file_0000000007c48211819e1998bbffb593",
          "metadata": {
            "id": "1vP-rEAG4EK0YbWt48UcAZrhC186NoCmw",
            "title": "What if you swam in a nuclear storage pool？ [EFRUL7vKdU8].mp4",
            "mime_type": "video/mp4",
            "size": "6749914",
            "url": "https://drive.google.com/file/d/1vP-rEAG4EK0YbWt48UcAZrhC186NoCmw/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1vP-rEAG4EK0YbWt48UcAZrhC186NoCmw/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:32.121Z",
            "modified_time": "2026-10-19T17:53:04.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:37:25.911508+00:00",
          "retrieved_bytes": 6749914,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "6749914",
          "retrieved_sha256": "8c6f896fb46a65670c7748f397704424276f63b62b92c4bbf81ed94d8f248175",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:37:29.755911+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you teleported to the Sun？ [m1aMh7z8Y7I].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you teleported to the Sun？ [m1aMh7z8Y7I].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 3373020,
        "allocated_path_bytes": 3375104,
        "mtime_ns": 1792432536000000000,
        "device": 16777229,
        "inode": 93824172,
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
        "sequence": 439,
        "proposed_destination_name": "00439__What if you teleported to the Sun？ [m1aMh7z8Y7I].mp4",
        "fresh_stat": {
          "st_size": 3373020,
          "st_mtime_ns": 1792432536000000000,
          "st_ctime_ns": 1792830801517965255,
          "st_ino": 93824172,
          "st_dev": 16777229
        },
        "fresh_sha256": "206dc35aff1298441206c0c600c1ec5800a9a27d63919a7761e3bca731f4c607",
        "hash_refreshed_utc": "2026-10-26T14:25:33.839818+00:00",
        "status": "VERIFIED",
        "remote_id": "16n2BJmZZCM-xuq1Mq8ZMCflyNBDoNo5x",
        "remote_url": "https://drive.google.com/file/d/16n2BJmZZCM-xuq1Mq8ZMCflyNBDoNo5x/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:07.626093+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "16n2BJmZZCM-xuq1Mq8ZMCflyNBDoNo5x",
            "title": "What if you teleported to the Sun？ [m1aMh7z8Y7I].mp4",
            "mime_type": "video/mp4",
            "size": "3373020",
            "url": "https://drive.google.com/file/d/16n2BJmZZCM-xuq1Mq8ZMCflyNBDoNo5x/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/16n2BJmZZCM-xuq1Mq8ZMCflyNBDoNo5x/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:24.648Z",
            "modified_time": "2026-10-19T17:55:36.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 439,
          "remote_id": "16n2BJmZZCM-xuq1Mq8ZMCflyNBDoNo5x",
          "retrieval_file_id": "sediment://file_00000000e284821199accd69239050a9",
          "metadata": {
            "id": "16n2BJmZZCM-xuq1Mq8ZMCflyNBDoNo5x",
            "title": "What if you teleported to the Sun？ [m1aMh7z8Y7I].mp4",
            "mime_type": "video/mp4",
            "size": "3373020",
            "url": "https://drive.google.com/file/d/16n2BJmZZCM-xuq1Mq8ZMCflyNBDoNo5x/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/16n2BJmZZCM-xuq1Mq8ZMCflyNBDoNo5x/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:24.648Z",
            "modified_time": "2026-10-19T17:55:36.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:37:38.642081+00:00",
          "retrieved_bytes": 3373020,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "3373020",
          "retrieved_sha256": "206dc35aff1298441206c0c600c1ec5800a9a27d63919a7761e3bca731f4c607",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:37:40.474521+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you threw a baseball at nearly light speed？ [3EI08o-IGYk].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you threw a baseball at nearly light speed？ [3EI08o-IGYk].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 6260903,
        "allocated_path_bytes": 6262784,
        "mtime_ns": 1792432396000000000,
        "device": 16777229,
        "inode": 93824072,
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
        "sequence": 440,
        "proposed_destination_name": "00440__What if you threw a baseball at nearly light speed？ [3EI08o-IGYk].mp4",
        "fresh_stat": {
          "st_size": 6260903,
          "st_mtime_ns": 1792432396000000000,
          "st_ctime_ns": 1792830801511947063,
          "st_ino": 93824072,
          "st_dev": 16777229
        },
        "fresh_sha256": "2e31af1c7f2bb72aae027243fd9da59dbc97535296d35547247120a8fa3eb56d",
        "hash_refreshed_utc": "2026-10-26T14:25:33.845506+00:00",
        "status": "VERIFIED",
        "remote_id": "1vgEPBCUHytCoH7vycHidYcbFf5t4nyau",
        "remote_url": "https://drive.google.com/file/d/1vgEPBCUHytCoH7vycHidYcbFf5t4nyau/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:11.652845+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1vgEPBCUHytCoH7vycHidYcbFf5t4nyau",
            "title": "What if you threw a baseball at nearly light speed？ [3EI08o-IGYk].mp4",
            "mime_type": "video/mp4",
            "size": "6260903",
            "url": "https://drive.google.com/file/d/1vgEPBCUHytCoH7vycHidYcbFf5t4nyau/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1vgEPBCUHytCoH7vycHidYcbFf5t4nyau/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:20.977Z",
            "modified_time": "2026-10-19T17:53:16.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 440,
          "remote_id": "1vgEPBCUHytCoH7vycHidYcbFf5t4nyau",
          "retrieval_file_id": "sediment://file_000000008ca08211b84d149b7418aa3d",
          "metadata": {
            "id": "1vgEPBCUHytCoH7vycHidYcbFf5t4nyau",
            "title": "What if you threw a baseball at nearly light speed？ [3EI08o-IGYk].mp4",
            "mime_type": "video/mp4",
            "size": "6260903",
            "url": "https://drive.google.com/file/d/1vgEPBCUHytCoH7vycHidYcbFf5t4nyau/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1vgEPBCUHytCoH7vycHidYcbFf5t4nyau/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:20.977Z",
            "modified_time": "2026-10-19T17:53:16.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:37:45.660750+00:00",
          "retrieved_bytes": 6260903,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "6260903",
          "retrieved_sha256": "2e31af1c7f2bb72aae027243fd9da59dbc97535296d35547247120a8fa3eb56d",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:37:52.451522+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you tried to hit a baseball pitched at 90_ the speed of light？ [Uj10jGq2O8o].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you tried to hit a baseball pitched at 90_ the speed of light？ [Uj10jGq2O8o].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 5930782,
        "allocated_path_bytes": 5931008,
        "mtime_ns": 1792432560000000000,
        "device": 16777229,
        "inode": 93824312,
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
        "sequence": 441,
        "proposed_destination_name": "00441__What if you tried to hit a baseball pitched at 90_ the speed of light？ [Uj10jGq2O8o].mp4",
        "fresh_stat": {
          "st_size": 5930782,
          "st_mtime_ns": 1792432560000000000,
          "st_ctime_ns": 1792830801519478084,
          "st_ino": 93824312,
          "st_dev": 16777229
        },
        "fresh_sha256": "5a9f62495265d9e148143729f382153e0aca6a6ca81963996874441aa645819e",
        "hash_refreshed_utc": "2026-10-26T14:25:33.851654+00:00",
        "status": "VERIFIED",
        "remote_id": "1aY1w12qKUmkHdtDk--ol8AQsJKRE7oAg",
        "remote_url": "https://drive.google.com/file/d/1aY1w12qKUmkHdtDk--ol8AQsJKRE7oAg/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:04.190679+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1aY1w12qKUmkHdtDk--ol8AQsJKRE7oAg",
            "title": "What if you tried to hit a baseball pitched at 90_ the speed of light？ [Uj10jGq2O8o].mp4",
            "mime_type": "video/mp4",
            "size": "5930782",
            "url": "https://drive.google.com/file/d/1aY1w12qKUmkHdtDk--ol8AQsJKRE7oAg/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1aY1w12qKUmkHdtDk--ol8AQsJKRE7oAg/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:40.261Z",
            "modified_time": "2026-10-19T17:56:00.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 441,
          "remote_id": "1aY1w12qKUmkHdtDk--ol8AQsJKRE7oAg",
          "retrieval_file_id": "sediment://file_000000007db0820787d2874af73c71af",
          "metadata": {
            "id": "1aY1w12qKUmkHdtDk--ol8AQsJKRE7oAg",
            "title": "What if you tried to hit a baseball pitched at 90_ the speed of light？ [Uj10jGq2O8o].mp4",
            "mime_type": "video/mp4",
            "size": "5930782",
            "url": "https://drive.google.com/file/d/1aY1w12qKUmkHdtDk--ol8AQsJKRE7oAg/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1aY1w12qKUmkHdtDk--ol8AQsJKRE7oAg/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:40.261Z",
            "modified_time": "2026-10-19T17:56:00.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:37:56.868786+00:00",
          "retrieved_bytes": 5930782,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "5930782",
          "retrieved_sha256": "5a9f62495265d9e148143729f382153e0aca6a6ca81963996874441aa645819e",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:38:04.254102+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you tried to print Wikipedia？ [RgBYohJ7mIk].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you tried to print Wikipedia？ [RgBYohJ7mIk].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 6222879,
        "allocated_path_bytes": 6225920,
        "mtime_ns": 1792432340000000000,
        "device": 16777229,
        "inode": 93824245,
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
        "sequence": 442,
        "proposed_destination_name": "00442__What if you tried to print Wikipedia？ [RgBYohJ7mIk].mp4",
        "fresh_stat": {
          "st_size": 6222879,
          "st_mtime_ns": 1792432340000000000,
          "st_ctime_ns": 1792830801519059085,
          "st_ino": 93824245,
          "st_dev": 16777229
        },
        "fresh_sha256": "9b4344bd3f44e51afc2d105f7946cd683f94d8dbda06e39ad07ba5a339240251",
        "hash_refreshed_utc": "2026-10-26T14:25:33.874164+00:00",
        "status": "VERIFIED",
        "remote_id": "1LxrqUnDEwjowGp-qxQGJcltoNRJKvJih",
        "remote_url": "https://drive.google.com/file/d/1LxrqUnDEwjowGp-qxQGJcltoNRJKvJih/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:14.779390+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1LxrqUnDEwjowGp-qxQGJcltoNRJKvJih",
            "title": "What if you tried to print Wikipedia？ [RgBYohJ7mIk].mp4",
            "mime_type": "video/mp4",
            "size": "6222879",
            "url": "https://drive.google.com/file/d/1LxrqUnDEwjowGp-qxQGJcltoNRJKvJih/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1LxrqUnDEwjowGp-qxQGJcltoNRJKvJih/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:36.499Z",
            "modified_time": "2026-10-19T17:52:20.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 442,
          "remote_id": "1LxrqUnDEwjowGp-qxQGJcltoNRJKvJih",
          "retrieval_file_id": "sediment://file_0000000008ec82119feea36fe6e07c45",
          "metadata": {
            "id": "1LxrqUnDEwjowGp-qxQGJcltoNRJKvJih",
            "title": "What if you tried to print Wikipedia？ [RgBYohJ7mIk].mp4",
            "mime_type": "video/mp4",
            "size": "6222879",
            "url": "https://drive.google.com/file/d/1LxrqUnDEwjowGp-qxQGJcltoNRJKvJih/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1LxrqUnDEwjowGp-qxQGJcltoNRJKvJih/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:36.499Z",
            "modified_time": "2026-10-19T17:52:20.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:38:15.032881+00:00",
          "retrieved_bytes": 6222879,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "6222879",
          "retrieved_sha256": "9b4344bd3f44e51afc2d105f7946cd683f94d8dbda06e39ad07ba5a339240251",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:38:20.477693+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you used a flamethrower as a snowblower？ [WYf9-xfm6t8].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you used a flamethrower as a snowblower？ [WYf9-xfm6t8].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 6032669,
        "allocated_path_bytes": 6033408,
        "mtime_ns": 1792432236000000000,
        "device": 16777229,
        "inode": 93824163,
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
        "sequence": 443,
        "proposed_destination_name": "00443__What if you used a flamethrower as a snowblower？ [WYf9-xfm6t8].mp4",
        "fresh_stat": {
          "st_size": 6032669,
          "st_mtime_ns": 1792432236000000000,
          "st_ctime_ns": 1792830801517842005,
          "st_ino": 93824163,
          "st_dev": 16777229
        },
        "fresh_sha256": "9d5e3a8ef69579d0043cd4a3db29fccfe1841df968f1349b22c971ca8520cc94",
        "hash_refreshed_utc": "2026-10-26T14:25:33.897559+00:00",
        "status": "VERIFIED",
        "remote_id": "1VD6Q9DnjDhAlQYlAOp9gkYTOxb3w5Nz8",
        "remote_url": "https://drive.google.com/file/d/1VD6Q9DnjDhAlQYlAOp9gkYTOxb3w5Nz8/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:16.502421+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1VD6Q9DnjDhAlQYlAOp9gkYTOxb3w5Nz8",
            "title": "What if you used a flamethrower as a snowblower？ [WYf9-xfm6t8].mp4",
            "mime_type": "video/mp4",
            "size": "6032669",
            "url": "https://drive.google.com/file/d/1VD6Q9DnjDhAlQYlAOp9gkYTOxb3w5Nz8/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1VD6Q9DnjDhAlQYlAOp9gkYTOxb3w5Nz8/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:16.364Z",
            "modified_time": "2026-10-19T17:50:36.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 443,
          "remote_id": "1VD6Q9DnjDhAlQYlAOp9gkYTOxb3w5Nz8",
          "retrieval_file_id": "sediment://file_0000000060d08207a9b397c17f234e06",
          "metadata": {
            "id": "1VD6Q9DnjDhAlQYlAOp9gkYTOxb3w5Nz8",
            "title": "What if you used a flamethrower as a snowblower？ [WYf9-xfm6t8].mp4",
            "mime_type": "video/mp4",
            "size": "6032669",
            "url": "https://drive.google.com/file/d/1VD6Q9DnjDhAlQYlAOp9gkYTOxb3w5Nz8/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1VD6Q9DnjDhAlQYlAOp9gkYTOxb3w5Nz8/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:28:16.364Z",
            "modified_time": "2026-10-19T17:50:36.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:39:22.940770+00:00",
          "retrieved_bytes": 6032669,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "6032669",
          "retrieved_sha256": "9d5e3a8ef69579d0043cd4a3db29fccfe1841df968f1349b22c971ca8520cc94",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:39:27.927298+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you used a microwave as a snowblower？ [DDNMLh1I_jY].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you used a microwave as a snowblower？ [DDNMLh1I_jY].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 3212090,
        "allocated_path_bytes": 3215360,
        "mtime_ns": 1792432466000000000,
        "device": 16777229,
        "inode": 93824087,
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
        "sequence": 444,
        "proposed_destination_name": "00444__What if you used a microwave as a snowblower？ [DDNMLh1I_jY].mp4",
        "fresh_stat": {
          "st_size": 3212090,
          "st_mtime_ns": 1792432466000000000,
          "st_ctime_ns": 1792830801512005438,
          "st_ino": 93824087,
          "st_dev": 16777229
        },
        "fresh_sha256": "de8800a447642f750079a24e6647aac16c597229bc40098012a4552f2bfe0dd8",
        "hash_refreshed_utc": "2026-10-26T14:25:33.922248+00:00",
        "status": "VERIFIED",
        "remote_id": "1UYg-TR-s47ASJE7woHCT50oZsZ9nETqa",
        "remote_url": "https://drive.google.com/file/d/1UYg-TR-s47ASJE7woHCT50oZsZ9nETqa/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:10.903996+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1UYg-TR-s47ASJE7woHCT50oZsZ9nETqa",
            "title": "What if you used a microwave as a snowblower？ [DDNMLh1I_jY].mp4",
            "mime_type": "video/mp4",
            "size": "3212090",
            "url": "https://drive.google.com/file/d/1UYg-TR-s47ASJE7woHCT50oZsZ9nETqa/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1UYg-TR-s47ASJE7woHCT50oZsZ9nETqa/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:30:39.856Z",
            "modified_time": "2026-10-19T17:54:26.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 444,
          "remote_id": "1UYg-TR-s47ASJE7woHCT50oZsZ9nETqa",
          "retrieval_file_id": "sediment://file_0000000019648211937c78f84c87737b",
          "metadata": {
            "id": "1UYg-TR-s47ASJE7woHCT50oZsZ9nETqa",
            "title": "What if you used a microwave as a snowblower？ [DDNMLh1I_jY].mp4",
            "mime_type": "video/mp4",
            "size": "3212090",
            "url": "https://drive.google.com/file/d/1UYg-TR-s47ASJE7woHCT50oZsZ9nETqa/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1UYg-TR-s47ASJE7woHCT50oZsZ9nETqa/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:30:39.856Z",
            "modified_time": "2026-10-19T17:54:26.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:39:32.671208+00:00",
          "retrieved_bytes": 3212090,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "3212090",
          "retrieved_sha256": "de8800a447642f750079a24e6647aac16c597229bc40098012a4552f2bfe0dd8",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:39:34.300567+00:00"
        }
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What would Earth_s climate be like if the land masses were rotated by 90°？ [XvvXDEtMfhw].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What would Earth_s climate be like if the land masses were rotated by 90°？ [XvvXDEtMfhw].mp4",
        "root": "/Users/ghilmankhan/Downloads/videos in mp3",
        "kind": "regular",
        "bytes": 5658060,
        "allocated_path_bytes": 5660672,
        "mtime_ns": 1792432498000000000,
        "device": 16777229,
        "inode": 93824217,
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
        "sequence": 445,
        "proposed_destination_name": "00445__What would Earth_s climate be like if the land masses were rotated by 90°？ [XvvXDEtMfhw].mp4",
        "fresh_stat": {
          "st_size": 5658060,
          "st_mtime_ns": 1792432498000000000,
          "st_ctime_ns": 1792830801518731711,
          "st_ino": 93824217,
          "st_dev": 16777229
        },
        "fresh_sha256": "3c3aec53cae1be7d81b90ce8d9e341abe1a4e125e2206d318184830341c9ad31",
        "hash_refreshed_utc": "2026-10-26T14:25:33.938674+00:00",
        "status": "VERIFIED",
        "remote_id": "1W8uWhVagk7K0Q59TvI2YAq4fAgZ9pHdd",
        "remote_url": "https://drive.google.com/file/d/1W8uWhVagk7K0Q59TvI2YAq4fAgZ9pHdd/view?usp=drivesdk",
        "upload_utc": "2026-10-26T14:32:08.412131+00:00",
        "upload_response": {
          "method": "Owner authenticated standard Drive multi-file upload into newly created private empty namespace; actual ID from bounded direct-child API listing, independent per-object metadata validation; raw original names preserved",
          "metadata": {
            "id": "1W8uWhVagk7K0Q59TvI2YAq4fAgZ9pHdd",
            "title": "What would Earth_s climate be like if the land masses were rotated by 90°？ [XvvXDEtMfhw].mp4",
            "mime_type": "video/mp4",
            "size": "5658060",
            "url": "https://drive.google.com/file/d/1W8uWhVagk7K0Q59TvI2YAq4fAgZ9pHdd/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1W8uWhVagk7K0Q59TvI2YAq4fAgZ9pHdd/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:30:47.607Z",
            "modified_time": "2026-10-19T17:54:58.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "sequence": 445,
          "remote_id": "1W8uWhVagk7K0Q59TvI2YAq4fAgZ9pHdd",
          "retrieval_file_id": "sediment://file_00000000a5708211888e76dab6531dcf",
          "metadata": {
            "id": "1W8uWhVagk7K0Q59TvI2YAq4fAgZ9pHdd",
            "title": "What would Earth_s climate be like if the land masses were rotated by 90°？ [XvvXDEtMfhw].mp4",
            "mime_type": "video/mp4",
            "size": "5658060",
            "url": "https://drive.google.com/file/d/1W8uWhVagk7K0Q59TvI2YAq4fAgZ9pHdd/view?usp=drivesdk",
            "display_url": "https://drive.google.com/file/d/1W8uWhVagk7K0Q59TvI2YAq4fAgZ9pHdd/view?usp=drivesdk",
            "file_or_folder": "file",
            "created_time": "2026-10-26T14:30:47.607Z",
            "modified_time": "2026-10-19T17:54:58.000Z",
            "parent_ids": [
              "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm"
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
          "started_utc": "2026-10-26T14:39:39.707863+00:00",
          "retrieved_bytes": 5658060,
          "status": "VERIFIED",
          "method": "Fresh authenticated complete raw remote read after upload phase ended; streamed SHA-256, no local source substitution or staging",
          "http_status": 200,
          "response_content_length": "5658060",
          "retrieved_sha256": "3c3aec53cae1be7d81b90ce8d9e341abe1a4e125e2206d318184830341c9ad31",
          "source_stable_after_retrieval": true,
          "finished_utc": "2026-10-26T14:39:49.350257+00:00"
        }
      }
    ],
    "uploaded_bytes": 107603827,
    "independently_retrieved_bytes": 107603827,
    "mapped_source_files": 20,
    "preflight": {
      "account": "kgk2930@gmail.com",
      "privacy": "OWNER_ONLY",
      "ui_used_gb": 5.02,
      "conservative_free_bytes": 9509816043,
      "storage_ui": "5.02GB of15GB; fresh owner Google One UI; Drive4.73GB Gmail302.23MB",
      "observed_at": "2026-10-26T14:25:33.650Z",
      "five_hour_used": 37,
      "weekly_used": 12,
      "paid_credits": "0",
      "context": "Batch22 verified continuation immutable; current context adequate, exact meter unavailable",
      "ownership": "Stable read-only originals; protected sessions preserved",
      "destination_folder_id": "12FkMHzKAtNYleLwX2UBmbMDMlk_6sXEf",
      "charges": "Existing allowance; paid credits zero, no upgrade/payment action",
      "mac_free_bytes": 24720560128
    },
    "postflight": {
      "batch_dir": "/Users/ghilmankhan/YIOS-local-audits/YIOS-bulk-20261025T2140Z-chat-01a174dd/batch-0023",
      "account": "kgk2930@gmail.com",
      "privacy": "OWNER_ONLY",
      "ui_used_gb": 5.12,
      "conservative_free_bytes": 9402441861,
      "storage_ui": "5.12GB of15GB; fresh owner Google One UI; Drive4.83GB Gmail302.23MB",
      "observed_at": "2026-10-26T14:40:49.631Z",
      "five_hour_used": 41,
      "weekly_used": 13,
      "paid_credits": "0",
      "context": "Batch22 verified continuation immutable; current context adequate, exact meter unavailable",
      "ownership": "Stable read-only originals; protected sessions preserved",
      "destination_folder_id": "1J2wajySRQoVPnWBrd3VXT5eoV-M-0uJm",
      "charges": "Existing allowance; paid credits zero, no upgrade/payment action",
      "mac_free_bytes": 24711217152
    },
    "permissions": "Owner-only Restricted; no changes",
    "encryption": "Google provider managed; owner-held client key not established",
    "retention": "Until explicit owner removal approval",
    "coverage": "File-level verified recovery only; no complete-package or independent-machine recovery claim"
  },
  "recovery_mapping": {
    "files": [
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you drained the oceans？ [Jpy55EgMQgY].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you drained the oceans？ [Jpy55EgMQgY].mp4",
        "bytes": 7419676,
        "fresh_sha256": "878e9d1518198312bc264c8f645925c87f8b5c50822c93caac2f86d115204f1d",
        "remote_id": "1tFKtI-vTLOmL6_PCKr0wTxE50B4llCQ9",
        "remote_url": "https://drive.google.com/file/d/1tFKtI-vTLOmL6_PCKr0wTxE50B4llCQ9/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you drained the oceans？ [aMshLs0YCTQ].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you drained the oceans？ [aMshLs0YCTQ].mp4",
        "bytes": 4446513,
        "fresh_sha256": "911525e63c0e1bc6aa08dbead51b6a6ea801a077bebf28da50228d761b2685e4",
        "remote_id": "1IqkfhEfHn-5Le4tZ54qpTaQ1sc3sy9Y1",
        "remote_url": "https://drive.google.com/file/d/1IqkfhEfHn-5Le4tZ54qpTaQ1sc3sy9Y1/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you dropped a bowling ball in the Mariana Trench？ [FYoHYq8VRt0].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you dropped a bowling ball in the Mariana Trench？ [FYoHYq8VRt0].mp4",
        "bytes": 5080341,
        "fresh_sha256": "d84737cd6b7d53c796f66b5552f36af728f525b364df2785d85e920d0887f523",
        "remote_id": "1SHRLQBz6EU7DhC77WUlzq-tbPp1JwB9N",
        "remote_url": "https://drive.google.com/file/d/1SHRLQBz6EU7DhC77WUlzq-tbPp1JwB9N/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you floated upwards 1 ft every second？ [oTzW-mTQd5w].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you floated upwards 1 ft every second？ [oTzW-mTQd5w].mp4",
        "bytes": 4762379,
        "fresh_sha256": "2c2aaa0047c94c793068f51f9f041cbbd36edcc0642d79a77136009804de6dec",
        "remote_id": "1nRkJ4z_HwnwAHokm1XQwuTPVRi6AN_Pp",
        "remote_url": "https://drive.google.com/file/d/1nRkJ4z_HwnwAHokm1XQwuTPVRi6AN_Pp/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you funneled Niagara Falls through a straw？ [pfbzrrcQZjs].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you funneled Niagara Falls through a straw？ [pfbzrrcQZjs].mp4",
        "bytes": 6045501,
        "fresh_sha256": "22e9d80bbe80eb281af4210f666412ca0d38d141acee255e420fed6b3a971b11",
        "remote_id": "1oaECLrmIYfCEc1_6swIdQHniniDdCfSP",
        "remote_url": "https://drive.google.com/file/d/1oaECLrmIYfCEc1_6swIdQHniniDdCfSP/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you funneled the Niagara Falls through a straw？ [QZIEjvSlOMQ].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you funneled the Niagara Falls through a straw？ [QZIEjvSlOMQ].mp4",
        "bytes": 3066480,
        "fresh_sha256": "e505229283f8c53c1a2ab068073b5b574d47efe95bd2ae179572d6f7fce44aad",
        "remote_id": "1_tW_zvtWj622rKFS8nyuySzQlw7KMG8E",
        "remote_url": "https://drive.google.com/file/d/1_tW_zvtWj622rKFS8nyuySzQlw7KMG8E/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you had a mole of moles？ [lLlwvmu1ZeA].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you had a mole of moles？ [lLlwvmu1ZeA].mp4",
        "bytes": 7433534,
        "fresh_sha256": "d5cf881bd05e7033be9d1397b55cc06be0b824f370bde9234fba7fa325c6db10",
        "remote_id": "1tk4SO9YzxGbJ0NeKzX9opppB0SqtJEk9",
        "remote_url": "https://drive.google.com/file/d/1tk4SO9YzxGbJ0NeKzX9opppB0SqtJEk9/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you had literally had all of the world_s money？ [jVy3qd70AqU].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you had literally had all of the world_s money？ [jVy3qd70AqU].mp4",
        "bytes": 3244125,
        "fresh_sha256": "b0e46c95279dc6a14d40e1f5f6d9bcf77cfbecaa7bd852811571ffbd5f227ae0",
        "remote_id": "1C0uW3TiVfVwKXspTtBG27B1PXgq5JtTo",
        "remote_url": "https://drive.google.com/file/d/1C0uW3TiVfVwKXspTtBG27B1PXgq5JtTo/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you kept digging downward？ [r7B0MzvwDcA].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you kept digging downward？ [r7B0MzvwDcA].mp4",
        "bytes": 5283281,
        "fresh_sha256": "d325348a0c3cc31f91e97e9495960b5141dd99226ee030777845cac8dbc7d63b",
        "remote_id": "1UFJySTCzdjkIfuxViS6oX83kQpCompIs",
        "remote_url": "https://drive.google.com/file/d/1UFJySTCzdjkIfuxViS6oX83kQpCompIs/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you literally had all the money in the world？ [saj7b5C6TCM].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you literally had all the money in the world？ [saj7b5C6TCM].mp4",
        "bytes": 5790859,
        "fresh_sha256": "579c074f451897ef08c6c6e1f239f34b7f874dc4bdaf2e25ad7814d9d5342e37",
        "remote_id": "1QJh07dHH-bHvtDw-lN1d-9cHw6chy6lt",
        "remote_url": "https://drive.google.com/file/d/1QJh07dHH-bHvtDw-lN1d-9cHw6chy6lt/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you made a jetpack using rifles？ [IdlQsjq5vKo].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you made a jetpack using rifles？ [IdlQsjq5vKo].mp4",
        "bytes": 7889651,
        "fresh_sha256": "3961fc65194672d670462cee63a3987e11f4b3f37432ac9115deeb4a457ebbba",
        "remote_id": "1lVq4hD2Qts_Ryhe1eNZGB5n5elIg5F19",
        "remote_url": "https://drive.google.com/file/d/1lVq4hD2Qts_Ryhe1eNZGB5n5elIg5F19/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you printed all of Wikipedia？ [WQTNLuhfkwk].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you printed all of Wikipedia？ [WQTNLuhfkwk].mp4",
        "bytes": 3701170,
        "fresh_sha256": "55d7ac17bd042a05af83c72689d12ffaf58c9f26502fc18ed103d96ddbc92ffb",
        "remote_id": "1C08aBvOlKA8GC8wEuJ4eJ_3S9O2FQ0q6",
        "remote_url": "https://drive.google.com/file/d/1C08aBvOlKA8GC8wEuJ4eJ_3S9O2FQ0q6/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you swam in a nuclear storage pool？ [EFRUL7vKdU8].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you swam in a nuclear storage pool？ [EFRUL7vKdU8].mp4",
        "bytes": 6749914,
        "fresh_sha256": "8c6f896fb46a65670c7748f397704424276f63b62b92c4bbf81ed94d8f248175",
        "remote_id": "1vP-rEAG4EK0YbWt48UcAZrhC186NoCmw",
        "remote_url": "https://drive.google.com/file/d/1vP-rEAG4EK0YbWt48UcAZrhC186NoCmw/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you teleported to the Sun？ [m1aMh7z8Y7I].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you teleported to the Sun？ [m1aMh7z8Y7I].mp4",
        "bytes": 3373020,
        "fresh_sha256": "206dc35aff1298441206c0c600c1ec5800a9a27d63919a7761e3bca731f4c607",
        "remote_id": "16n2BJmZZCM-xuq1Mq8ZMCflyNBDoNo5x",
        "remote_url": "https://drive.google.com/file/d/16n2BJmZZCM-xuq1Mq8ZMCflyNBDoNo5x/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you threw a baseball at nearly light speed？ [3EI08o-IGYk].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you threw a baseball at nearly light speed？ [3EI08o-IGYk].mp4",
        "bytes": 6260903,
        "fresh_sha256": "2e31af1c7f2bb72aae027243fd9da59dbc97535296d35547247120a8fa3eb56d",
        "remote_id": "1vgEPBCUHytCoH7vycHidYcbFf5t4nyau",
        "remote_url": "https://drive.google.com/file/d/1vgEPBCUHytCoH7vycHidYcbFf5t4nyau/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you tried to hit a baseball pitched at 90_ the speed of light？ [Uj10jGq2O8o].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you tried to hit a baseball pitched at 90_ the speed of light？ [Uj10jGq2O8o].mp4",
        "bytes": 5930782,
        "fresh_sha256": "5a9f62495265d9e148143729f382153e0aca6a6ca81963996874441aa645819e",
        "remote_id": "1aY1w12qKUmkHdtDk--ol8AQsJKRE7oAg",
        "remote_url": "https://drive.google.com/file/d/1aY1w12qKUmkHdtDk--ol8AQsJKRE7oAg/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you tried to print Wikipedia？ [RgBYohJ7mIk].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you tried to print Wikipedia？ [RgBYohJ7mIk].mp4",
        "bytes": 6222879,
        "fresh_sha256": "9b4344bd3f44e51afc2d105f7946cd683f94d8dbda06e39ad07ba5a339240251",
        "remote_id": "1LxrqUnDEwjowGp-qxQGJcltoNRJKvJih",
        "remote_url": "https://drive.google.com/file/d/1LxrqUnDEwjowGp-qxQGJcltoNRJKvJih/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you used a flamethrower as a snowblower？ [WYf9-xfm6t8].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you used a flamethrower as a snowblower？ [WYf9-xfm6t8].mp4",
        "bytes": 6032669,
        "fresh_sha256": "9d5e3a8ef69579d0043cd4a3db29fccfe1841df968f1349b22c971ca8520cc94",
        "remote_id": "1VD6Q9DnjDhAlQYlAOp9gkYTOxb3w5Nz8",
        "remote_url": "https://drive.google.com/file/d/1VD6Q9DnjDhAlQYlAOp9gkYTOxb3w5Nz8/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What if you used a microwave as a snowblower？ [DDNMLh1I_jY].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What if you used a microwave as a snowblower？ [DDNMLh1I_jY].mp4",
        "bytes": 3212090,
        "fresh_sha256": "de8800a447642f750079a24e6647aac16c597229bc40098012a4552f2bfe0dd8",
        "remote_id": "1UYg-TR-s47ASJE7woHCT50oZsZ9nETqa",
        "remote_url": "https://drive.google.com/file/d/1UYg-TR-s47ASJE7woHCT50oZsZ9nETqa/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      },
      {
        "source_absolute": "/Users/ghilmankhan/Downloads/videos in mp3/xkcd Channel/What would Earth_s climate be like if the land masses were rotated by 90°？ [XvvXDEtMfhw].mp4",
        "restore_relative": "machine-a/Downloads/videos in mp3/xkcd Channel/What would Earth_s climate be like if the land masses were rotated by 90°？ [XvvXDEtMfhw].mp4",
        "bytes": 5658060,
        "fresh_sha256": "3c3aec53cae1be7d81b90ce8d9e341abe1a4e125e2206d318184830341c9ad31",
        "remote_id": "1W8uWhVagk7K0Q59TvI2YAq4fAgZ9pHdd",
        "remote_url": "https://drive.google.com/file/d/1W8uWhVagk7K0Q59TvI2YAq4fAgZ9pHdd/view?usp=drivesdk",
        "backup_priority": "A_ORIGINAL_MEDIA",
        "required_companions": "Preserve source parent package; links/references may require unselected external dependencies",
        "status": "VERIFIED",
        "duplicate_of_verified": null
      }
    ]
  },
  "cumulative_before_this_control": {
    "mapped_source_paths": 453,
    "uploaded_bytes_including_controls": 4641558318,
    "verified_bytes_including_controls": 4641558318,
    "remaining_payload_bytes": 7358441682,
    "remaining_plan_files": 99
  }
}
```
