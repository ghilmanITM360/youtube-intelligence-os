# Revision 1 Lock

Revision 1 is frozen as of the timestamp below. It is the second experimental
artefact of Test A, and like the blind first pass it is evidence: do not edit
these files in place. A further round of human feedback produces `revision_2/`.

**Locked at:** 2026-09-17T08:09:59Z
**Blind first pass:** `../` — all 18 locked hashes verified before and after this review, zero mismatches
**Brain:** Production Intelligence Brain v1.0.0, read-only, unmodified; validator re-run after this revision: PASS
**Script SHA-256:** `28893099c3e4cc997580c7fc78dc7f029abadadd3aa68dce9eeb2eee5289fe2b` (unchanged)
**Status:** REVISION_1_COMPLETE — AWAITING_HUMAN_REVIEW

## SHA-256 of every Revision 1 output

| File | Bytes | SHA-256 |
|---|---|---|
| `CORPUS_DENSITY_BASELINE.md` | 8814 | `0ab1786a24c163e9a201dd5747a115532efda895c4de7a3ffb3b010ade9f680f` |
| `EXECUTABILITY_CHECK.md` | 5699 | `16275dd7cf8f1a3232600a5cbbbc7b989908ab7044b52ab5f67cbb32e9623e4d` |
| `MOTION_REVIEW.csv` | 16378 | `d0b7a8879a2f2dbebc9147ac9a35acd4f5d918dc0ec337fbbc94748fc4adcaa6` |
| `RELEASE_METADATA_ISSUE.md` | 2431 | `d458e118bb6823656a1ca53a338530e0001e7e42613c871667a03456c3ebfe41` |
| `REVISED_ANIMATION_PROMPTS.md` | 7150 | `8a1ee13749f25eb528e26d537411a7628f4d261a2e0249b460b944a8e05b0754` |
| `REVISED_ASSETS.csv` | 10124 | `fc1b80d16d5e511e2f79d94419243b8735a5247aed43f2e7293b774f396fa9d8` |
| `REVISED_BASE_IMAGES.csv` | 2532 | `87cebc4c68c65b01b58c494963cf566b2c8a30054d2a299214091f90fa38764d` |
| `REVISED_CAPCUT_BUILD.md` | 7685 | `3a83c812675d9028bb0751c3c2b41083ba4a8829099e6b9366418f015e42d5dd` |
| `REVISED_FINAL_VISUAL_PRODUCTION_PLAN.md` | 62186 | `0f4e8975172ef56cc00a34700fb98389740f71149f262c09560e530eae60bb40` |
| `REVISED_I2V_DECISIONS.md` | 3718 | `727f1fa7df35289f290f2ea4f64a9ec9a40b05d1a11c8173a8ab05c3b8562eed` |
| `REVISED_IMAGE_PROMPTS.md` | 18385 | `3a1778a919fe0a345f67a29106ddf21ad1b79f04d7deac310e1b7d07ebe652c8` |
| `REVISED_MOTIONS.csv` | 11080 | `b347c32075ff42f5f7b8a3eccdab93a974e7c7c61719ef22eb06be3e75bd3690` |
| `REVISED_SHOT_PLAN.csv` | 3509 | `e00ef1b818decc09c6b8de3bea4ea5bda49f7400e49019ab7e534d876e1d8601` |
| `REVISED_STORYBOARD.md` | 28077 | `c3a5edb344cdd1f490982efd49966e15271dfcd734f95e996c82dd8ba7609f18` |
| `REVISED_TEXT_OVERLAYS.csv` | 2201 | `66dd469a49e3bdcbe3d42935d9ca006d74e8c38c0e66c8ed5c8d08ae8337437b` |
| `REVISED_VISUAL_STATES.csv` | 20922 | `0ed4302880cd0a1fb89cbc018f273717ece908bf1171630137aa848acc5b0f76` |
| `REVISION_1_CHANGELOG.md` | 10247 | `e3109429c2989d291fcadf90c73ac53316721db5dbb699979090f118b982a5ef` |
| `REVISION_1_MANIFEST.json` | 2944 | `72f4d24675fa26c6f55ce321e4cf6845f048b785c9feee8801709bd8b6ef81a6` |
| `REVISION_1_SELF_AUDIT.md` | 9678 | `f9888132329818cd58a02d625237b9b1d81a8aeebcc2094ec7d34c7284085c90` |
| `STATE_REVIEW.csv` | 24195 | `968e57f3ac62939d09042f16b8e2d4dcbbe4a1b322acdede673ddd6d534b037b` |

## Verify

```bash
cd "generalization_tests/test_a_coffee_heart_visual_translation/revision_1"
shasum -a 256 *.csv *.md *.json
```

Compare against the table above. Any difference means Revision 1 has been
edited and is no longer the artefact this audit produced.

## Verify the first pass is still intact

```bash
cd "generalization_tests/test_a_coffee_heart_visual_translation"
shasum -a 256 *.csv *.md *.json *.txt
```

Compare against `FIRST_PASS_LOCK.md`. The blind pass must never change.
