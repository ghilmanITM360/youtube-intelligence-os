# Deep-VF addendum v3 (proof attempt 3, prompt pack v2, rules v3 / held-out v9, alkJ7; LOCAL ONLY)

Earlier files are not edited. Unchanged results:
- v7: 19/23;
- v8: 32/34;
- proof attempt 2 (`proof_v1/`).

## 1. Proof attempt 3 (`proof_v1_attempt3/PROOF_RESULTS_attempt3.md`)
- **What changed:**
  - 9:16: a short question pops at f6 (0.25 s);
  - MELTING pops together with drips on the moon;
  - STEAM pops together with wisps rising from it.
- **Machine checks:** both 16:9 and 9:16 pass every one (P1–P7, the native-colour red pop, clipping) plus the 2 new checks:
  - opening inside the first second;
  - label backed by a state change (≥ 2240 px changed outside the label box).
- **Disclosed:** one clause of the new check (post-encode next frame == 0) was dropped after the first run because of x264 residue. The pre-encode check is still exact.
- **Not accepted yet:** P8 human playback and P9 are **PENDING_HUMAN**; AV is pending.

## 2. Prompt pack v2 (`../PROMPT_PACK_v2/STYLE_BIBLE_AND_PROMPTS_v2.md`)
- **Two separate assets for the cards:**
  - opening card, 48 f;
  - end screen, 240 f.
- **New scene classes:** DARK_FIELD, MAP_FILL (plus a TINT variant) and the GLOW plate.
- **Red circle:** a 1-frame pop spec (GFX-004), which replaces write-on.
- **New motion rules:**
  - labels must be backed by a state change;
  - Shorts must open within 24 f.
- **Branding:** original only (teal #1F6F78, NIB, TARDI). Nothing has been generated.

## 3. Rules v3 / held-out v9 (`FROZEN_RULES_v3.md`, `heldout_v9/RESULTS.md`)
- **Freeze:** 2026-11-08T23:26:29Z.
- **v3 changes:**
  - MAP_FILL is added as a C2 condition;
  - the Short camera budget counts device instances, so merged moves count once.
- **Picks:** 19gun1mffWs (map pick) and FKXVs4UteSc (scroll pick).
- **Score:** 9/9 scorable = 100%. Counting the undefined check as a non-pass gives 9/10 = 90%, which still holds. FKXV's M1 is UNDEFINED because there is no frozen Short JOURNEY_LADDER limit.
- **Feature-present cases: 0/0.**
  - The maps are grey, not MAP_FILL.
  - No multi-move camera instance appears.
  - **Both v3 changes are UNTESTED**, which is a coverage gap.
- **Parent overlap:**
  - 19gun is 99% ASR overlap with gp5G (never viewed);
  - FKXV is 95% with e3uk (v7), so it is **not independent**.
- **Finding:** FKXV is a ladder **Short**: a persistent magnitude ruler with 9 ruler scrolls and camera at 0.083. This is descriptive support for the journey claim, not a validation.

## 4. alkJ7xScBiw (`ACQUISITION_alkJ7xScBiw_BLOCKED.md`)
- **Authorized but BLOCKED:** no approved acquisition tool (yt-dlp) is on this Mac, and nothing was installed.
- **2026 long stratum:** UNCOVERED.
- **Long journey arm:** UNTESTED.

## 5. Counts (deduplicated by video ID)
| Set | Long | Shorts |
|---|---|---|
| Unique videos visually examined (v2: 32 + 24, plus v9 19gun and FKXV) | 32 | 26 |
| **Total unique** | **58** | |
| Visual gates passed (held-outs, all evaluated rules) | 6 | 2 (alBQ, 19gun) + FKXV passed all scorable checks, with 1 undefined |
| Full AV passed | 0 | 0 |

- **58 now. It would be 59 with alkJ7 once it is acquired.**
- If alkJ7 is not a journey video, a 60th video is needed: a fresh journey long. None exists locally.
- A feature-present test of the v3 changes needs Shorts that actually contain saturated maps or a film strip. None is identifiable by title in the remaining pool of 11.
