# First Pass Lock

This records the blind first pass exactly as generated, before any user
feedback. Nothing in this directory is to be revised until a user-corrected
version is produced as a separate, later artifact — the point of the lock is to
make `BLIND FIRST PASS` vs `USER-CORRECTED VERSION` a real comparison.

**Locked at:** 2026-09-17T06:14:30Z
**Brain:** Production Intelligence Brain v1.0.0 (frozen; unmodified by this test)
**Script SHA-256:** `28893099c3e4cc997580c7fc78dc7f029abadadd3aa68dce9eeb2eee5289fe2b`
**Status:** FIRST_PASS_COMPLETE — AWAITING_HUMAN_REVIEW

## SHA-256 of every first-pass output

| File | Bytes | SHA-256 |
|---|---|---|
| `ANIMATION_PROMPTS.md` | 5063 | `28853933dae0c4bdcbb41c93a45a2e9fa500f0d28f5053764e69e20b9332cdb1` |
| `ASSETS.csv` | 9607 | `d655f3d87bd233a86c9d4eb4e207d0d2815bc0539eb8877afcb71bb4d895d1fc` |
| `BASE_IMAGES.csv` | 3911 | `47305db0d6d5b28a04c889c6f7c37829cef6192129a4d3efaf4d3557c1c7f967` |
| `CAPCUT_BUILD.md` | 9582 | `dbd954d430bbccca60503b9fbd6af6d4e5bc90988bfa62b73e2b417e3a68fe1f` |
| `FINAL_VISUAL_PRODUCTION_PLAN.md` | 37749 | `f066723ecec9a4c7925f3fd6e7062f2288bc05be818555e13c11e774df0b2b6d` |
| `I2V_DECISIONS.md` | 4460 | `1649baa5360330d7cff465178d00a05d2711c9130ded6412a54abc4206a4146b` |
| `IMAGE_PROMPTS.md` | 16328 | `3440fe61f813c457994e748b562eb72381d7cc3364edecc60f65f5bc02eafa6d` |
| `MOTIONS.csv` | 8796 | `6b6fcb4080c3dbef782ff2927849b3a5b9f198014471af4cebb7ff5d0d40c3e3` |
| `NARRATION_BEATS.csv` | 3741 | `43ffd4e50ba800697876a00344cd89b562c1c3e8cad2ad9745e8780633d668ad` |
| `SCRIPT_CANONICAL.txt` | 706 | `28893099c3e4cc997580c7fc78dc7f029abadadd3aa68dce9eeb2eee5289fe2b` |
| `SHOT_PLAN.csv` | 3459 | `d5e6242f20a4f4806058a4d22c34c4fd00e930aac2cfb594cd5f06cdd4fc2ad5` |
| `STORYBOARD.md` | 22922 | `b61e9763d351c5f84aa77046028db6dda5672c6943d02717117836432b33d94d` |
| `TEST_A_MANIFEST.json` | 3874 | `22c56474e203bfa968cf1a1af26c97c3948309ecbe2a47732832252f1936ea9b` |
| `TEST_A_SELF_AUDIT.md` | 8322 | `5476e1d75ff92887ef893c7355c60ce4e7e31c9b5e598389f66db7f40e01150d` |
| `TEXT_OVERLAYS.csv` | 1682 | `6182504bdf17f3fbc41b78cdaeb2454d8da64a790e25ed6bdbaf49cb71ed35fb` |
| `TRAINING_OVERLAP.md` | 2653 | `ab4d1290beb5458868f71c27abd9d4262331458d6947af4249b247267edcb8b1` |
| `VISUAL_STATES.csv` | 20291 | `67ca101a5a573587acded1cb0576a78625b65941e41a3d0dc168661431bb89ff` |
| `VISUAL_STORY.md` | 4345 | `9b0180419c6a08bfb7677dd0b0371e497a5f4c3462a29f9e1d2d78546661c277` |

## Verify

```bash
cd "generalization_tests/test_a_coffee_heart_visual_translation"
shasum -a 256 *.csv *.md *.json *.txt
```

Compare against the table above. Any difference means the first pass has been
edited and is no longer the blind baseline.
