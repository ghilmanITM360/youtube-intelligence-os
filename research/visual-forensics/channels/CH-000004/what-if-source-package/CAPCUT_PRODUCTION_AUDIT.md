# CapCut Production-Pipeline Audit

Repository: `/Users/ghilmanislam360/GhilmanProjects/video data of what if` (not a git repository — no commit/branch history exists to check; this audit relies entirely on the working tree as found, 2026‑09‑21).

Scope: 2,461 files / 171 directories. 1,420 jpg + 582 png (2,002 extracted evidence frames), 223 md, 155 csv, 32 json, 14 mp4, 13 py, 8 wav, 6 aac. No `.js`/`.sh`/`.ts` files anywhere. No `graphify-out/` graph existed prior to this audit and none was built for it (the corpus is 2,000+ raw frame images and would need expensive vision-based extraction that isn't needed to answer this brief — direct file reads and code inspection were used instead).

Method: this audit was produced by five parallel read-only research passes (each independently re-reading the actual files, not trusting prior doc claims) plus direct reads of the top-level manifests, plus live web research against CapCut's official help center for Part 6. Every claim below is anchored to a file path, and quoted lines are verbatim from the repository. Nothing in the repository was modified, generated, or deleted to produce this report — this file is the one new artifact, added at the end, per the audit brief's own instruction to "produce the complete audit."

---

## Part 1 — What this system actually is

**It is (C) a production-intelligence brain built from (B) forensic video analysis, with (A) the raw forensic database underneath it, plus one hand-authored generalization dry-run.** It is **not** (D) a script-to-video planner, **not** (E) a prompt generator, **not** (F) a CapCut production assistant, and **not** (G) an automated editor — none of those exist as running software anywhere in the repository.

Concretely, four layers exist, cleanly separated on disk:

1. **`videos/`** — 14 raw source MP4s (already-published "what if" shorts/videos downloaded from YouTube).
2. **`video_forensics_output/<slug>/`** (×14) — per-video *forensic reconstruction* of each existing video: extracted frames/contact sheets, a shot/state/motion timeline, a Whisper transcript with word-level timing, an audio/visual sync table, and — critically — a `03_capcut/CAPCUT_REBUILD.md` and `04_image_to_video/{IMAGE_PROMPTS,ANIMATION_PROMPTS,I2V_REBUILD}.md` per video. These read like production instructions, but every one of them is keyed to real measured timestamps/state IDs from *that one already-existing video's own* `TIMELINE.csv` (e.g. `how_long_could_you_drive_towards_the_sunset/03_capcut/CAPCUT_REBUILD.md:70`: `## S04 — 00:13.833-00:31.417 / SOURCE STATES: F04.0 → F04.1 → ...`). They are retrospective rebuild sheets, not forward planning tools.
3. **`production_intelligence_brain/`** — an aggregation of the 14 forensic outputs into 8 master CSVs, 7 "production DNA" statistics docs, a "reconstruction system," 6 "pattern" CSVs, and 4 "blueprints," all cross-checked by a real 656-line validator (`validator/validate_brain.py`). This is the (C) production-intelligence brain: a rigorously self-audited, internally consistent statistical/structural model of what the 14 source videos actually do (shot durations, transition types, motion vocabulary, asset reuse). It is genuinely well-built for what it is.
4. **`generalization_tests/test_a_coffee_heart_visual_translation/`** — one hand-run dry-run (almost certainly by a prior Claude/LLM session, not code) that took a brand-new script and manually produced a full planning package by reading the brain's docs. This is the closest thing in the repo to an answer for the audit's central question, and it is discussed in depth in Part 14 below.

**The pipeline the brief hypothesized — source video → transcript → sentences → shots → visual state → asset → motion → A/V sync → editing rule → production DNA → reconstruction blueprint → new-video generation — is real only through "production DNA."** It stops there. `reconstruction blueprint → new-video generation` does not exist as code; it exists, once, as a single hand-authored document set (`generalization_tests/`), outside the brain's own canonical structure, that a human/LLM must redo from scratch for every new script.

**Confirmed:** zero generation code exists anywhere in the repository. `grep -rn "def generate" --include="*.py" .` returns no matches repository-wide. All 13 `.py` files are read/validate/hash-only:
- `production_intelligence_brain/validator/validate_brain.py` (656 lines) — checks foreign-key integrity, timestamp arithmetic, CSV column counts, and JSON manifest/index consistency across the 8 master CSVs. Never writes production content.
- `production_intelligence_brain/validator/_canonical_files.py` — file enumeration/hashing helper.
- `production_intelligence_brain/validator/build_release_manifest.py` — writes exactly one output, `RELEASE_MANIFEST.json`, containing only path/size/sha256 of files already on disk.
- `video_forensics_output/<slug>/00_source/verify.py` (present in only **7 of 14** video folders — see Part 15) — asserts that pre-existing markdown/CSV files conform to structural expectations (e.g. exactly 14 sequential `IMG` headers in `IMAGE_PROMPTS.md`). It reads and validates content that a human/LLM already wrote; it does not produce that content.

---

## Part 2 — Can a new script be understood?

**No parser exists — implemented or otherwise — that segments a script into hook/setup/question/explanation/escalation/example/comparison/statistic/metaphor/joke/tension/reveal/payoff/conclusion/CTA.** This was checked directly:

- The master data's only text field, `MASTER_SENTENCES.TEXT` (604 rows), is a raw string column with **no rhetorical-type column** (`production_intelligence_brain/01_master_data/MASTER_SENTENCES.csv`, header: `VIDEO_SLUG,SENTENCE_ID,START_SEC,END_SEC,TEXT,FIRST_WORD_ID,LAST_WORD_ID,WORD_COUNT,CONFIDENCE,NOTES`).
- The closest thing to a semantic tag anywhere in the brain is `MASTER_STATES.VISUAL_FUNCTION` — but it is uncontrolled free text (398 distinct values across 581 rows: e.g. `"emergency escalation"`, `"Setup illustration"`, `"PAYOFF (full ring achieved)"`), confirmed by direct inspection to be per-row prose, not a fixed taxonomy — it cannot be reliably filtered or joined as a category.
- `grep`-confirmed: the words "hook"/"payoff"/"setup" appear **zero times** inside `production_intelligence_brain/05_blueprints/*.md`, the one folder whose names (`NEW_VIDEO_BLUEPRINT.md`, `NARRATION_TO_VISUAL_BLUEPRINT.md`) most suggest this capability. Those blueprints map narration *timing* to visual *timing* only — their decision tree branches on "Is it a cut between states? / Is it an animation/reveal?", never on what the sentence *means*.
- `production_intelligence_brain/testing/GENERALIZATION_TEST_PROTOCOL.md` — the brain's own designed test for exactly this question — ends with: **"No unseen test has been executed yet. This protocol is ready; awaiting a genuinely unseen script or reference video from the user."** The brain's own author never ran its own generalization test through the canonical protocol.

**Is existing corpus data sufficient to build a segmenter?** Partially, and only as *training signal*, not as a ready classifier. The 604 sentences + word-level timing + `VISUAL_FUNCTION` free-text tags are a usable (small) labeled dataset if someone manually normalizes `VISUAL_FUNCTION` into a fixed taxonomy first — but that normalization doesn't exist, and 604 sentences from 14 short videos is a thin training set for a general-purpose rhetorical classifier. In practice, the realistic path (and the one the repo's own dry-run actually used, see Part 14) is an LLM performing this segmentation by reasoning directly over the script text — zero-shot, not trained on this corpus. That is **manual/LLM reasoning**, not an implemented capability of this repository.

**Verdict for Part 2: NOT PRESENT as implemented code. TECHNICALLY POSSIBLE WITH EXTENSION** (an LLM prompt/step bolted on top — cheap to add, see Part 16), but nothing in the current repo does this today, automatically or otherwise.

---

## Part 3 — Script → visual mapping

**No explicit, machine-usable narration-type → visual-type mapping exists anywhere in the repository.** This is the single most consistent finding across all five sub-audits. Evidence:

- `production_intelligence_brain/02_production_dna/*.md` (7 files) are exclusively descriptive corpus statistics, and each ends with an explicit **"What is NOT supported by current data"** section. `VISUAL_DNA.md`: *"No color palette... claim about 'consistent color coding for semantic meaning' would be unsupported and is omitted."* `MOTION_DNA.md`: *"no field distinguishing 'reveal' vs 'transition' vs 'emphasis'... was not derived from any column."*
- `production_intelligence_brain/03_reconstruction_system/RECONSTRUCTION_INDEX.json` contains the *one* real decision table in the whole brain — `decision_criteria.use_capcut_when` / `use_i2v_when` (e.g. "Visual progression or growth" → I2V; "Cutting between static states" → CapCut). This is genuine, but it governs *how to render a shot once chosen* (CapCut layer-ops vs. AI image-to-video), not *what shot to invent from a sentence's meaning*.
- `04_patterns/*.csv` (6 files, 2,540 rows) are raw per-event rows or frequency aggregates (e.g. `TRANSITION_PATTERNS.csv`: `STATE_CHANGE,581,76,DURING_WORD`) — statistics, not IF/THEN rules. None has a `TRIGGER_CONDITION` or `RULE` column.

**Capability matrix — is each mapping the brief asked about present as data, derivable, or absent?**

| Narration signal | Explicit mapping present? | Statistically derivable from corpus? |
|---|---|---|
| Question → visual setup | No | Weakly — `VISUAL_FUNCTION` free text sometimes says "Setup illustration" but isn't linked to question-form sentences by any column |
| Number → number graphic | No | No — no numeral/graphic linkage column exists |
| Comparison → side-by-side scene | No | No |
| Scale → zoom animation | No | Weakly — `MASTER_MOTIONS.ACTION`/`AMPLITUDE` describe zoom-like motions post hoc, not triggered by "scale" language |
| Danger/escalation → escalation visual | No | Weakly — `VISUAL_FUNCTION` contains ad hoc strings like `"emergency escalation"` on specific rows, uncontrolled |
| Punchline → visual gag | No | No — no humor/joke labeling anywhere |
| Explanation → labelled diagram | No | No |
| Transition (narrative) → camera movement | Partial | `NARRATION_TO_VISUAL_BLUEPRINT.md`'s decision tree covers *when* to cut/animate once a shot boundary is already decided — real but narrow |

**Verdict: DOCUMENTED ONLY at best, mostly NOT PRESENT.** The brain would have to be extended with new classification logic (almost certainly an LLM-based tagger) before any of this matrix could be automated; the existing corpus is too small (604 sentences, 14 videos, single niche) and too unstructured (free-text `VISUAL_FUNCTION`) to statistically derive these mappings without that new logic.

---

## Part 4 — Image-prompt generation

**No code generates image prompts. Real, high-quality image-generation-style prompt *text* exists in two places, both hand-authored, both retrospective or one-off:**

1. **Per-video `04_image_to_video/IMAGE_PROMPTS.md`** (14 files, one per source video) — genuine Midjourney/SDXL-style prose (style, composition, palette, camera language), e.g. `how_long_could_you_drive_towards_the_sunset/04_image_to_video/IMAGE_PROMPTS.md:11`: *"Flat 2D vector illustration, 9:16 vertical. A white chalkboard/whiteboard panel fills the frame..."* But every one of these was written by **describing an already-extracted real frame** (`SOURCE STATE: F01.0`) — the prompt was produced by looking at the answer and writing it down, the reverse of what a new-script generator needs. Cross-corpus grep confirms **zero** hits anywhere in `video_forensics_output/` for "negative prompt", "style reference", "consistency reference", "seed" (as a real generator parameter), "midjourney", "dall-e", "stable diffusion", or "sdxl" — none of the standard prompt-engineering metadata fields the brief asks about (negative prompts, consistency references, seeds) exist as structured data anywhere.
2. **`generalization_tests/test_a_coffee_heart_visual_translation/IMAGE_PROMPTS.md`** — the one genuinely *forward* example, covered fully in Part 14. It does include aspect ratio, composition bounding boxes (as %), style, line-weight, and negative prompts, and is real production-quality prose. But it was written by an LLM reasoning from the brain's documentation in a single session — no code produced it, and it exists once, for one script.

**Which repository fields would feed each prompt field, if a generator were built?**

| Prompt field | Feeding repo field(s) | Gap |
|---|---|---|
| Composition/framing | `MASTER_STATES.LITERAL_FRAME_DESCRIPTION` (dense prose description of an existing frame) | Retrospective only — no field exists for an *unrendered* new scene |
| Camera angle / static vs. motion | `MASTER_STATES.CAMERA_STATE`, `MASTER_MOTIONS.CAMERA` (corpus is 89.8% locked/static camera, zero fades — a real, reusable house-style fact) | Usable as a **prior**, not a generator |
| Illustration style / line weight / palette | `02_production_dna/VISUAL_DNA.md` (e.g. "red reserved exclusively for rejection marks") | Real, reusable **style facts**, but scattered across prose docs, not a structured `STYLE_BIBLE.json` (see Part 11 — doesn't exist yet) |
| Aspect ratio | `SOURCE_VIDEO_INDEX.csv.ASPECT_RATIO` (8 portrait 9:16, 6 landscape 16:9) | Present as corpus statistic, not a per-new-scene decision field |
| Asset type / transparency / format | `MASTER_ASSETS.TYPE`, `MEDIA_FORMAT_NEEDED`, `TRANSPARENT_BG` | Real and reusable as defaults *once an asset's TYPE is known* — but nothing infers TYPE from a new script sentence |
| Negative prompt, consistency refs, seed, text-safe zones | **No column, no field, anywhere** | 100% new work |

**Verdict: DATA EXISTS BUT NO GENERATOR**, with one **PROPOSED-and-manually-demonstrated-once** example (`generalization_tests/`). The building blocks (locked-camera default, zero-fade rule, asset-format defaults, aspect-ratio priors) are real and would meaningfully seed a generator's system prompt — but nothing assembles them automatically today.

---

## Part 5 — Animation / image-to-video prompts

**Same verdict, slightly worse: even the one hand-authored generalization test found zero real I2V need.** `generalization_tests/test_a_coffee_heart_visual_translation/I2V_DECISIONS.md` states plainly: `I2V_REQUIRED = 0` — every one of that script's motions was executed as a CapCut layer/mask operation, not an AI-video-generation call. This is *consistent* with the source corpus: `production_intelligence_brain/03_reconstruction_system/CAPCUT_PRODUCTION_SYSTEM.md` documents **zero fade/cross-dissolve transitions exist anywhere in the 14-video corpus — every one of 186 shot boundaries is an exact 0.0s hard cut**, and 89.8% of states report a locked/static camera. The 14 source videos this brain was built from are, empirically, *not* an image-to-video-heavy production style — they're mostly static-frame-cut-static-frame with CapCut-native keyframe motion. This is a genuinely important, well-evidenced fact for anyone building a new pipeline off this corpus: **don't assume I2V is even the right tool** for videos in this house style.

Where animation prompt *text* does exist (per-video `04_image_to_video/ANIMATION_PROMPTS.md` and `I2V_REBUILD.md`, plus the test's `ANIMATION_PROMPTS.md`), it is short (≤500 char), keyed to `SOURCE_STATE`→`TARGET_STATE` pairs pulled from `MOTION_EVENTS.csv`/`MOTIONS.csv`, e.g. `how_long_could_you_drive_towards_the_sunset/04_image_to_video/ANIMATION_PROMPTS.md:101`. Every per-video `I2V_REBUILD.md` explicitly states, e.g.: *"No image, video, or audio has actually been generated or rendered as part of this analysis — this document is a build specification only."* Nothing has ever actually been rendered by this repository — zero image/video/audio output files exist anywhere outside the original 14 source MP4s and their extracted evidence frames.

**Can master motion/state/sync data support this automatically?** The motion vocabulary is real and could seed a rules engine (`MASTER_MOTIONS.ACTION/DIRECTION_OR_PATH/SPEED/AMPLITUDE/RELATIONSHIP`, `RELATIONSHIP` categories like `STATE_REPLACEMENT`/`SEQUENTIAL`/`SIMULTANEOUS_COUPLED`), and `MASTER_AUDIO_VISUAL_SYNC.csv` (1,421 rows) genuinely captures word-boundary sync timing (`OFFSET_MS`, `SYNC_RELATION` e.g. `ON_WORD_START`). But these are all **free-text/loose-categorical fields describing already-observed motions**, not numeric position/scale/rotation/opacity keyframe vectors, and not tied to any mechanism for choosing a motion for content that doesn't exist yet.

**Verdict: DATA EXISTS BUT NO GENERATOR.** The one real transferable asset here is negative: strong evidence that this corpus's house style barely needs I2V at all, which should directly shape the target architecture (favor a CapCut-native-keyframe generator over an I2V pipeline — see Part 16).

---

## Part 6 — CapCut compatibility audit (fresh official research, 2026‑09‑21)

### A. Officially supported import formats
Per `capcut.com/help` (official help center): **video** MP4/MOV/MKV; **images** JPEG/PNG/GIF; **audio** MP3/WAV/M4A; **subtitles** SRT (primary) or plain TXT with SRT-style timecodes, **UTF‑8 required**, and — important constraint — **subtitle file import (SRT/TXT) is only available on CapCut Desktop and CapCut Web, not the Mobile app** (mobile can view/edit subtitles synced in from desktop/web via CapCut Cloud, but cannot initiate the import itself).

### B. Native CapCut operations (officially documented)
- **Keyframes**: position, scale, rotation, opacity, color, volume — free on all platforms, with ease‑in/ease‑out interpolation.
- **Mask keyframes** and **custom curve easing editors** — CapCut Pro only.
- Text/caption styling, overlays, transitions, effects, auto-captioning (~30+ languages) — all standard native features.
- **Native AI generation is now in-app**: CapCut ships its own AI image generator (Seedream 5.0 by ByteDance, Nano Banana Pro by Google — text-to-image and image-to-image) and its own AI video tools (Seedance for text/image-to-video, "CapCut Video Studio" for text-to-video). These are genuinely useful for this project's goals but are **manual, in-UI features** — not something an external pipeline can call.

### C. Direct automation — does not officially exist
- **No public API for project generation, timeline editing, or batch export/automation.** CapCut's "Open Platform" is scoped to building plugins that run *inside* the editor UI; it does not expose server-side/headless project-generation endpoints.
- **No confirmed official project-interchange format.** The official help center states plainly that Premiere Pro projects (`.prproj`) *cannot* be imported — CapCut's own recommended workaround is "render your Premiere sequence to MP4 and import the video file." Third-party claims that CapCut added XML import in 2025 are **contradicted by other sources and not confirmed on capcut.com** — treat XML/EDL import as **unconfirmed and unreliable**, not as a supported path.
- **CapCut's actual native project format (`draft_content.json` + a folder of asset/material JSONs) is undocumented by ByteDance.** It has been reverse-engineered by the community (e.g. the `capcut-cli` project, ~3,700 lines of unofficial schema documentation covering CapCut 6.x–9.x / JianYing 5.9.0), is version-dependent, and recent versions are reportedly partially encrypted with "unclear legal posture" around decryption. **This is a real, working, but entirely unofficial and fragile automation path** — it can break on any CapCut update, and Anthropic/this audit does not treat undocumented-format manipulation as a recommended production dependency without the user explicitly accepting that risk.

**Bottom line for Part 6: there is no officially supported way to programmatically generate or edit a CapCut project.** Anything beyond "hand the editor MP4/MOV/PNG/JPG/WAV/MP3 + a valid SRT (desktop/web only)" is either manual in-app work or an unofficial, versioned, reverse-engineered file-format hack.

Sources: [CapCut Help Center](https://www.capcut.com/help), [How Do I Import Subtitles?](https://www.capcut.com/help/how-to-import-subtitles), [How Do I Export a Premiere Pro Project to CapCut?](https://www.capcut.com/help/how-to-export-pro-project), [CapCut AI Features](https://www.capcut.com/help/ai-features), community `draft_content.json` schema notes (capcut-cli / renezander030 gists — unofficial).

---

## Part 7 — Can this project create an actual CapCut project? (levels)

| Level | Description | Possible now? | Implemented now? | Notes |
|---|---|---|---|---|
| **0** | Research only | Yes | Yes | This audit; the brain's DNA docs are research on the *existing* corpus |
| **1** | Editing recommendations | Yes | Partially | `03_reconstruction_system/*` gives real but narrow rules (hard-cuts-only, locked-camera default, CapCut-vs-I2V heuristic) |
| **2** | Scene-by-scene production document | Yes, by hand/LLM | Demonstrated once | `generalization_tests/test_a_coffee_heart_visual_translation/` — full document for one script, zero automation |
| **3** | Generated production assets (images+animations+VO+music/SFX+subtitles) | Not automated | No | Zero image/video/audio assets exist anywhere for any *new* script; per-video `I2V_REBUILD.md` files confirm nothing has ever been rendered even for the *existing* 14 videos |
| **4** | CapCut-ready import package (assets/ + audio/ + captions/ + timeline.json + docs) | Not automated; format not defined | No | No `timeline.json` schema, no `.srt` file, exists anywhere in the repo (confirmed by repo-wide grep/find) |
| **5** | Semi-automatic CapCut assembly | No | No | No tooling touches CapCut at all |
| **6** | Actual editable CapCut project generated automatically | Technically feasible only via the undocumented `draft_content.json` format | No | Not recommended without explicit user risk acceptance (Part 6.C) |
| **7** | Fully automated final CapCut render/export | Not supported by CapCut itself for external automation | No | CapCut has no export/render API; a Level 6 hack still requires a human to open CapCut and hit Export |

**Recommendation:** target **Level 4** as the real deliverable (a well-specified, versioned intermediate package + a deterministic build-instruction doc), with **Level 2** quality bar for every scene, not just a proof-of-concept scene. Level 6 is possible only through unofficial reverse-engineered file manipulation and should be offered as an optional, clearly-labeled "experimental/unsupported" path, never the default.

---

## Part 8 — Timeline generation

**No universal intermediate timeline schema exists anywhere in the repository.** `find . -iname "timeline.json"` returns zero results repo-wide. (Per-video `02_analysis/TIMELINE.csv` files exist, but those describe the *already-analyzed source video's* frame-level IN/OUT boundaries — a forensic record, not a forward-authoring schema, and not JSON.)

Mapping the brief's proposed schema fields against what the master data can actually populate for a **new** script:

| Timeline field | Populatable from existing brain data? | Source / gap |
|---|---|---|
| `start_time` / `end_time` / `duration` | New script: **no** (no real audio exists until VO is recorded); existing corpus: yes, from `MASTER_SHOTS`/`MASTER_STATES`/`MASTER_WORDS.START_SEC/END_SEC` | Confirmed present for the 14 source videos only |
| `narration` | Yes, trivially — it's the script itself | — |
| `scene_type` / `shot_type` | No | No shot-type enum exists anywhere (no wide/close/etc. column) |
| `image_asset` / `video_asset` | No (would be the *output* of a not-yet-built generator) | — |
| `motion` | Partially, as free text/categoricals from `MASTER_MOTIONS` for the *existing* corpus | No numeric vectors |
| `position` / `scale` / `rotation` / `opacity` | No structured numeric fields anywhere; `LITERAL_FRAME_DESCRIPTION` gives approximate % positions in unstructured prose only | Would need parsing/new inference |
| `keyframes` | No | — |
| `transition_in` / `transition_out` | Yes, for existing corpus (`MASTER_SHOTS.TRANSITION_IN/OUT`) — and a real, reusable fact: **100% hard cuts, 0% fades** | Reusable as a default rule for new content |
| `caption` / `caption_style` | Yes (text) / No (style) | `MASTER_SENTENCES.TEXT`, `MASTER_WORDS` give the text; no styling data exists |
| `sfx` / `music` | **No — schema slot exists but is empty.** `MASTER_AUDIO_EVENTS.TYPE` only ever contains `NARRATION`/`PAUSE`/`SILENCE` across all 29 rows; zero SFX or music events were ever detected in any of the 14 source videos | This is a real, load-bearing gap — the corpus has no SFX/music vocabulary to learn from at all |
| `sync_event` | Yes, well-populated (`MASTER_AUDIO_VISUAL_SYNC.csv`, 1,421 rows) — the most complete field in the whole brain | — |
| `prompt` / `animation_prompt` | No structured column; only unstructured markdown prose per video | — |

**No existing schema in the repo already accomplishes this** — there is no JSON Schema, dataclass, or pydantic model for any of the 8 master CSVs (`grep -rl "pydantic|dataclass|jsonschema|BaseModel"` returns zero hits repo-wide; `validator/schemas/` contains only `brain_manifest.schema.json` and `release_manifest.schema.json`, i.e. schemas for the *manifest* files, not the production data). A new `timeline.json` schema would be genuinely new work, not a duplicate of anything present.

**Verdict: NOT PRESENT.** Building it is straightforward (the field list above is basically the spec), but it does not exist today in any form, for either new or existing content.

---

## Part 9 — CapCut build instructions (deterministic assembly spec)

**This is the one thing the repository does closest to well, but only manually and only once.** `generalization_tests/test_a_coffee_heart_visual_translation/production_pack/PRODUCTION_READY_VISUAL_PACK.md` (1,417 lines) and `visual_01_execution_pack/VISUAL_01_CAPCUT_BUILD.md` give genuinely near-mechanical instructions: explicit track numbers, 24fps frame counts, exact keyframe positions with named interpolation ("frame 0 hidden → frame 4 fully past the stroke's right end... interpolation LINEAR"), and word-onset trigger tables. A human editor could plausibly follow this by hand.

The per-video `03_capcut/CAPCUT_REBUILD.md` files (×14, for the *existing* source videos) are similarly precise, but for a video that already exists and was already measured frame-by-frame — they are reconstruction sheets, not a generator's output.

**What's missing to make this a real "assembly spec" capability, not a one-off document:**
1. A machine-parseable version of these instructions (the brief's own `00:00.000–00:02.400 / Add scene_001.png / Scale 105%...` example format) — currently these are prose markdown, not structured data an assembly script could consume.
2. Real timing — every duration in `generalization_tests/` is explicitly labeled **ESTIMATED**, because no voiceover audio was ever recorded for the test script (`TEST_A_MANIFEST.json`: `"absolute_timestamps_used": false`). A real pipeline needs either a TTS voiceover step or a recorded-VO ingestion step before real timing can exist.
3. Automation — nothing currently converts a `PRODUCTION_READY_VISUAL_PACK.md`-style doc into the structured per-clip instruction list the brief describes. This would be new code on top of the Part 8 timeline schema.

**Verdict: DOCUMENTED ONLY**, at a genuinely high quality bar for one example. This is very close to "an editor could semi-automatically follow this," which makes it the best evidence in the repo that a real generator, once built, could hit a useful quality bar.

---

## Part 10 — Captions

**No `.srt` file exists anywhere in the repository** (`find . -iname "*.srt"` — zero results, confirmed twice independently). What exists:

- `MASTER_WORDS.csv` (7,864 rows) and per-video `05_audio/semantic/TRANSCRIPT_WORDS.csv` — real Whisper word-level timing (`START_SEC`/`END_SEC` per word), which is exactly the raw material SRT generation needs.
- `MASTER_SENTENCES.csv` (604 rows) — sentence-level timing and text, a reasonable unit for caption-block segmentation.
- Known data-quality caveat, explicitly documented by the brain itself: **26 word rows have a 10ms timestamp overlap** from Whisper alignment rounding (`production_intelligence_brain/BRAIN_SUMMARY.md`) — harmless for captioning, but worth handling in any generator (clamp/round).

**Can the project automatically generate a valid UTF‑8 `.srt` for a new video?** Not today — no code does this anywhere — but the *inputs* an SRT generator would need (word timing) are exactly what this corpus is best at capturing, for the **existing** 14 videos. For a **new** script, the same gap as everywhere else applies: there is no real audio/timing until a voiceover is recorded (TTS or human), at which point word-level alignment (the same Whisper step this project already uses) would need to be re-run on the *new* audio — this is a straightforward, well-precedented extension, not a hard problem, but it is 100% new code (there's no SRT writer function anywhere in the 13 `.py` files).

Caption *styling*, emphasis/highlighted words, and animation instructions are **not present as structured data anywhere** — this would be new design work, informed by nothing in the current corpus (the source videos' actual on-screen caption styling was never forensically captured as a separate structured field).

**Verdict: NOT PRESENT as code; DATA EXISTS (word timing) that directly supports building it; straightforward to add** (see Part 16 — this is one of the cheapest wins).

---

## Part 11 — Visual consistency system

**None of `STYLE_BIBLE.md`, `CHARACTER_BIBLE.md`, `ENVIRONMENT_BIBLE.md`, `COLOR_RULES.md`, `ASSET_REGISTRY.json`, or `PROMPT_TEMPLATE.md` exist anywhere in the repository** (confirmed by filename search). The one partial exception: `generalization_tests/test_a_coffee_heart_visual_translation/production_pack/DR_REHAN_CHARACTER_MASTER.md` — a single hand-authored character-consistency doc for *one* recurring character in the one test script. It is real and reasonably well-specified, but it's a one-off artifact for one test, not a reusable, corpus-wide bible.

**Does current production DNA contain enough evidence to build these bibles?** Yes, partially, for style/color rules specifically — this is one of the stronger latent capabilities in the repo:
- `02_production_dna/VISUAL_DNA.md` contains real, corpus-wide, measured style facts (e.g. "red reserved exclusively for rejection marks," locked-camera-default, zero-fade-transitions) that are exactly the kind of content a `STYLE_BIBLE.md`/`COLOR_RULES.md` needs.
- `01_master_data/MASTER_ASSETS.csv` (448 rows, `TYPE`/`MEDIA_FORMAT_NEEDED`/`TRANSPARENT_BG`/`REUSE_STATUS` columns) is a reasonable seed for an `ASSET_REGISTRY.json`, though it currently describes assets *observed in the source videos*, not a registry for new-content assets.
- No `CHARACTER_BIBLE.md`-equivalent exists at the brain level — none of the 14 source videos appears to feature a recurring illustrated character (they're mostly abstract/diagrammatic), so there's no corpus precedent for character consistency at all. The one character-consistency example that exists (`DR_REHAN_CHARACTER_MASTER.md`) was invented for the test script, not derived from the corpus.

**Verdict: DATA EXISTS BUT NO GENERATOR/ASSEMBLER.** Extracting `VISUAL_DNA.md` + `MASTER_ASSETS.csv` into the structured bible files the brief proposes is low-effort, high-value new work — genuinely one of the best "smallest clean extension" candidates in this whole audit (see Part 16).

---

## Part 12 — Motion language

Cross-referencing the brief's proposed vocabulary against what's **actually observed and documented** in `02_production_dna/MOTION_DNA.md`, `04_patterns/MOTION_PATTERNS.csv` (438 real motion rows), and `03_reconstruction_system/CAPCUT_PRODUCTION_SYSTEM.md`:

| Vocabulary term | Genuinely supported by repository observation? |
|---|---|
| static / locked camera | **Yes — dominant.** 89.8% of states report a locked/static camera |
| Hard cut | **Yes — near-universal.** 100% of the 186 measured shot boundaries are exact 0.0s hard cuts |
| Fade / dissolve / wipe (as a *transition*) | **No — explicitly disconfirmed.** Zero fade transitions were found anywhere in the corpus; the brain's own docs state this as a corrected fact (an earlier draft wrongly claimed uniform "CUT" transitions and was fixed) |
| Object slide / object scale ("STATE_REPLACEMENT") | Yes — `MASTER_MOTIONS.RELATIONSHIP` has real categories including `STATE_REPLACEMENT`, `SEQUENTIAL`, `SIMULTANEOUS_COUPLED` |
| Reveal / mask reveal | Yes — asset "reveal" motions are common in the sample data (e.g. `A01`: "Reveal the first TAP word cloud") |
| Push-in / pull-out / pan / tilt / punch zoom | **Weakly supported.** A handful of motions have zoom/pan-like `ACTION`/`DIRECTION_OR_PATH` values, but this is not the corpus's dominant behavior — the corpus is overwhelmingly static-camera, hard-cut-between-states, not camera-move-heavy |
| Parallax / shake / bounce / pop / diagram build | **Not confirmed as a named category anywhere** — these terms do not appear as `RELATIONSHIP`/`ACTION` values in the data; they may occur as informal motion descriptions but were not found labeled as such |
| Sequential asset entrance | Yes — `SEQUENTIAL` is a real `RELATIONSHIP` value |

**Do not invent style patterns not supported by the data** (per the brief's own instruction): the corpus is honestly a **hard-cut, locked-camera, discrete-state-replacement house style**, not a fluid-camera-movement or fade-heavy style. Any new-script generator built off this brain should default to that house style rather than assuming generic "cinematic" motion language — this is one of the most concrete, well-evidenced, genuinely reusable facts in the entire audit.

**Verdict: PARTIALLY IMPLEMENTED as documented vocabulary** (real, corpus-grounded, and already written down in `MOTION_DNA.md`/`CAPCUT_PRODUCTION_SYSTEM.md`) but **NOT PRESENT as code** — nothing selects from this vocabulary automatically for new content.

---

## Part 13 — Prompt engine

**None of the six proposed functions (`generate_image_prompt`, `generate_animation_prompt`, `generate_edit_instruction`, `generate_caption_block`, `generate_sfx_instruction`, `generate_capcut_instruction`) exist anywhere in the repository** — confirmed by the zero-result `grep -rn "def generate"` scan. This section is therefore a forward design note, not an audit finding; see Part 16 for the concrete proposal, which reuses the exact repository data fields cataloged in Parts 4/5/8/9/10 as each function's inputs.

---

## Part 14 — End-to-end dry run: what already happened, read honestly

The repository already contains an end-to-end dry run that is *more thorough* than what this audit would otherwise need to newly perform: `generalization_tests/test_a_coffee_heart_visual_translation/`, built around a script about coffee and heart health / caffeine response — functionally the same test case the audit brief itself proposes. This section reports what that test actually shows, since re-doing it from scratch would duplicate real, already-existing work.

**Genuine new-topic test, confirmed:** `TRAINING_OVERLAP.md` searched the 604-sentence training corpus for `caffeine`, `energy drink`, `blood pressure`, `cardiac`, `doctor`, `patient` — zero hits on all — and concludes: *"The supplied coffee/heart script is not one of the 14 training/reference scripts... This is a genuine different-niche generalisation input."*

**Coverage:** the *whole* 5-shot / 22-state / 17-motion script got full planning depth — `SHOT_PLAN.csv`, `VISUAL_STATES.csv`, `MOTIONS.csv`, `ASSETS.csv`, `BASE_IMAGES.csv` all have complete rows, and `IMAGE_PROMPTS.md`/`ANIMATION_PROMPTS.md`/`CAPCUT_BUILD.md` give complete per-shot instructions — this is not a "one scene as proof of concept, rest left shallow" situation. `visual_01_execution_pack/` adds one further layer of copy-paste/frame-level granularity to shot 1 only, as a demonstration of maximum format depth, not because shots 2–5 were left thin.

**Real image prompt quality (verbatim), e.g. `IMAGE_PROMPTS.md` IMG01:**
> "A vertical 9:16 illustration, 2160 × 3840 pixels, on a completely flat off-white background. Simple thin black hand-drawn linework... Centred in the upper third of the frame, spanning 36–64% of the image width and 18–30% of the image height, draw a simple coffee mug seen from the side... Do NOT include: any text, letters, numbers, words or labels; any arrows, lines, branches or connectors; any people or figures... any red; any colour other than the single brown coffee band."

This is genuinely production-grade prompt engineering — composition as percentage bounding boxes, explicit style/line-weight constraints, and a real negative prompt.

**Zero I2V need found:** `I2V_DECISIONS.md`: `I2V_REQUIRED = 0` — every motion executed as a CapCut layer/mask op, consistent with Part 5's finding about the source corpus's house style.

**Self-audit caught real errors** (this is a strength, not a weakness, of the process): `TEST_A_SELF_AUDIT.md` flagged motion/reveal density as "~1.6–1.7× corpus density" as a **CONCERN**; `revision_1/` re-measured against the corpus's per-shot *distribution* rather than its mean and found the true figure was "high-normal, not anomalous" (~p90) — a self-corrected measurement error, transparently logged in `revision_1/REVISION_1_CHANGELOG.md`. Separately, `revision_1` caught and fixed an undeliverable prompt instruction ("two pixel-identical stick figures," which is not reliable to ask an image model for) by switching to "generate one figure, duplicate it in the editor."

**What was NOT produced, at all:** zero image files, zero video files, zero audio files exist anywhere in `generalization_tests/` (confirmed by file-type scan — every one of the ~55 files is markdown/CSV/JSON text). No `.srt`, no `.draft`, no `timeline.json` (confirmed by repo-wide grep, zero hits). Every mention of "generator" in the test's own files is prospective ("can be pasted into an image generator") — nothing was actually run through one.

**Attribution:** high confidence this was produced entirely by **manual/LLM reasoning over the brain's markdown documentation**, not by running any code — the only executable code in the repository (`validator/*.py`) never references `generalization_tests/` at all, and `TEST_A_MANIFEST.json` explicitly labels its own timing as estimated "because no voice track recorded, no measured timestamp appears anywhere in this test."

### What this audit adds beyond the existing test (light dry-run of the brief's own coffee/caffeine example)

Applying the same process the repository's own test already demonstrated, to the brief's literal one-liner ("Coffee is not simply good or bad for your heart. The important question is how your body responds to caffeine.") — briefly, without re-doing the full 1,400-line production pack the existing test already built for a near-identical premise:

1. **Script segmentation** (manual reasoning, not implemented code): Sentence 1 = *reframe/tension* ("not simply good or bad" sets up a false binary to dismantle — a hook-adjacent move). Sentence 2 = *reveal/thesis* (the real question — individual caffeine response).
2. **Story beats**: Setup (binary framing) → Reveal (reframe to the real variable) → [implicit next beat, not in the one-liner: explanation/mechanism → individual-variation example → conclusion/CTA].
3. **Scene/shot list** (by analogy to the existing test's SH01 pattern): Shot 1 — coffee cup + heart icon, ambiguous/conflicted visual (mirrors the existing test's IMG01 mug+heart composition almost exactly). Shot 2 — the same two icons with a "?" or a branching visual replacing the binary red/green marks, cueing "it depends."
4. **Visual descriptions / image prompts**: could reuse the existing test's actual IMG01 prompt almost verbatim (same subject: coffee mug + heart, same flat off-white line-art house style) — strong evidence the corpus's style rules generalize at least within this one sub-topic, since it's nearly the same premise.
5. **Animation/I2V prompts, durations, camera, SFX, music, transitions, CapCut timeline**: by the corpus's own well-evidenced house style (Parts 5, 12), the honest default is hard-cut, locked-camera, CapCut-native layer motion, no fades, no confirmed SFX/music vocabulary to draw on.

**Explicit attribution of every piece above:** step 1–2 (segmentation/beats) = **manual reasoning**, no implemented parser. Step 3 (scene list) = **manual reasoning**, informed by the *existing* test's already-built pattern (reused structured data: none — reused prior document's prose). Step 4 (image prompt) = **existing structured/documented data**, specifically the near-identical prior test's own prompt text — a genuine reuse. Step 5 (motion/timeline/CapCut) = **production DNA** (documented corpus statistics: hard-cut-only, locked-camera, no SFX/music evidence) applied by **manual reasoning**, not automated. **Newly inferred logic**: the mapping from "reframe/tension" and "reveal/thesis" sentence types to specific visual choices — that classification itself is 100% new reasoning performed in this audit, with no repository component doing it.

This dry run reinforces every finding above rather than contradicting them: the corpus's statistical/stylistic priors (Parts 3, 4, 5, 12) are strong enough to make manual/LLM planning fast and plausible-looking, but nothing in the repository performs any step of this automatically.

---

## Part 15 — Gap analysis

| Capability | Current state | Why missing | Available supporting data | New code needed | New data needed | External tool needed | CapCut limitation? | Priority | Effort | Risk |
|---|---|---|---|---|---|---|---|---|---|---|
| Script semantic segmentation | Not present | Never built; brain's own generalization test protocol never run | 604 labeled `TEXT` rows + free-text `VISUAL_FUNCTION` (weak) | LLM-based segmenter (prompt, not training) | A fixed rhetorical-type taxonomy (new) | LLM API | No | High | Low | Low |
| Automatic scene/shot planning | Not present (manual only, demonstrated once) | No code layer above the brain's docs | `MASTER_SHOTS`/`STATES` structure as a *format* to target; corpus pacing stats | Script→shot planner (LLM-driven) | None new beyond segmentation output | LLM API | No | High | Medium | Medium (quality variance) |
| Image-prompt generation | Data exists, no generator; one manual example | `LITERAL_FRAME_DESCRIPTION`/`VISUAL_FUNCTION` are retrospective, not generative | `VISUAL_DNA.md` style facts, `MASTER_ASSETS` type/format defaults, the test's real prompt example | Prompt-template + style-bible assembler | `STYLE_BIBLE`/`ASSET_REGISTRY` (extract from DNA docs — see Part 11) | Image-gen model (external, user-chosen) | No | High | Low–Medium | Low |
| Image generation (actual pixels) | Not present | Never run — even for the 14 existing videos | — | API integration to chosen image model | — | Image-gen API/account | No | Medium (depends on scope) | Low (integration only) | Cost/quality risk |
| Asset consistency | Not present as system; one-off character doc exists | No `STYLE_BIBLE`/`ASSET_REGISTRY` extracted yet | `VISUAL_DNA.md`, `MASTER_ASSETS.csv` | Extraction script (DNA docs → JSON bibles) | None new | None | No | High | Low | Low |
| Animation-prompt generation | Data exists, no generator | Motion data is retrospective/free-text | `MOTION_DNA.md`, `MASTER_MOTIONS` categoricals, CapCut-vs-I2V decision table | Motion-decision + prompt assembler | None new | Optional I2V model | No | Medium (corpus rarely needs I2V) | Low–Medium | Low |
| Animation/I2V generation (actual video) | Not present | Never run | — | API integration | — | I2V API/account | No | Low (corpus shows minimal need) | Low (integration only) | Cost/quality risk |
| Voiceover | Not present | Out of scope of existing forensic work | Corpus has real Whisper alignment *methodology* to reuse for the new VO | TTS integration + re-run word-alignment (Whisper, already used in this project) | New recorded/TTS audio per script | TTS API or human VO | No | High (blocks all real timing) | Low–Medium | Low |
| SFX | Not present, and **no corpus precedent at all** | Zero SFX events in all 14 source videos | None | New rule-authoring (no corpus data to learn from) | New — must be designed, not derived | Sound library | No | Low–Medium | Medium | Medium (inventing without evidence) |
| Music | Not present, and **no corpus precedent at all** | Same as SFX | None | Same as SFX | Same as SFX | Music library | No | Low–Medium | Medium | Medium |
| Caption/SRT generation | Not present as code; strong supporting data | No SRT writer exists | Full word-level timing exists (for existing videos); same Whisper method applies to new VO | SRT writer (small, standard) | New VO timing (depends on VO step) | None (stdlib) | Desktop/Web only, not Mobile | High | Very low | Low |
| Universal timeline schema | Not present | Never designed | Field-by-field mapping already done in Part 8 | New schema + populator | None new beyond above | None | No | High (blocks Parts 4/5/9 automation) | Low–Medium | Low |
| CapCut handoff (Level 4 package) | Not present | Depends on timeline schema | Part 9's manual example shows target quality bar | Package assembler (folder + docs) | None new | None | No | High | Medium | Low |
| Direct CapCut automation (Level 6) | Not present; only via undocumented format | No official API | community `draft_content.json` schema (unofficial, versioned) | Unofficial writer, version-pinned | None new | Reverse-engineered format library, version-locked | **Yes — no official API exists** | Low (optional, opt-in) | High | **High** (breaks on CapCut updates; unclear legal posture) |

---

## Part 16 — Ideal future architecture (smallest clean extension)

**Reuse, don't rebuild.** The brain (`production_intelligence_brain/`) is genuinely solid at what it does — validated, self-audited, honest about its own limitations — and should stay exactly as-is as the *style/statistics reference layer*. The per-video forensic outputs and the coffee/heart generalization test should be kept as worked examples / few-shot references for the new LLM-driven steps below, not reprocessed. Nothing here proposes touching `validator/`, `01_master_data/`, `02_production_dna/`, `04_patterns/`, or the 14 forensic folders.

The brief's proposed architecture is directionally right; here it is annotated against what already exists vs. what's new:

```
NEW TOPIC → RESEARCH → SCRIPT                         [user-provided, out of scope]
    ↓
SEMANTIC SCRIPT SEGMENTER                              [NEW — LLM step, Part 2/15]
    ↓
STORY / VISUAL PLANNER                                 [NEW — LLM step, informed by 05_blueprints/*
    ↓                                                    + generalization_tests/ as few-shot examples]
SHOT PLANNER                                            [NEW — targets the Part 8 schema]
    ↓
PRODUCTION-DNA RETRIEVAL                                [EXISTS — 02_production_dna/, 04_patterns/,
    ↓                                                    03_reconstruction_system/ — reuse as-is]
IMAGE PROMPT ENGINE                                     [NEW — assembler over STYLE_BIBLE (extract
    ↓                                                    from VISUAL_DNA.md) + ASSET_REGISTRY (extract
    ↓                                                    from MASTER_ASSETS.csv) + shot plan]
IMAGE GENERATION                                        [NEW — external API integration; or manual
    ↓                                                    in CapCut's own native AI image tool, Part 6]
ANIMATION PROMPT ENGINE                                 [NEW — but corpus evidence says most shots
    ↓                                                    won't need this; default to CapCut-native
    ↓                                                    keyframes per MOTION_DNA.md's real vocabulary]
IMAGE-TO-VIDEO GENERATION                               [NEW, low-priority per corpus evidence]
    ↓
VOICEOVER                                                [NEW — TTS or human VO, then re-run the
    ↓                                                    project's existing Whisper alignment method]
CAPTIONS                                                 [NEW — small SRT writer over word timing]
    ↓
AUDIO/SFX PLAN                                           [NEW — no corpus precedent; design from
    ↓                                                    scratch, mark low-confidence]
UNIVERSAL TIMELINE                                       [NEW — schema from Part 8, standalone,
    ↓                                                    CapCut-independent]
CAPCUT HANDOFF                                           [NEW — Level 4 package: assets/ + audio/ +
    ↓                                                    captions/ + timeline.json + a generated,
    ↓                                                    structured version of the Part 9 build doc]
EDITOR REVIEW → FINAL VIDEO                              [human, in CapCut, using officially-supported
                                                           import: MP4/MOV/PNG/JPG/WAV/MP3/SRT]
```

**Phased recommendation, shortest-safest-path first:**

- **Phase 0 (near-zero effort, pure extraction, no new logic):** Extract `STYLE_BIBLE.md`/`COLOR_RULES.md` from `02_production_dna/VISUAL_DNA.md`, and `ASSET_REGISTRY.json` from `MASTER_ASSETS.csv`. This is reformatting existing, already-validated facts — highest value-per-hour in the whole gap analysis, and it directly unblocks Part 11 and de-risks the Image Prompt Engine.
- **Phase 1 (script understanding + planning, LLM-driven, no rendering):** Build the Semantic Script Segmenter and Shot Planner as LLM prompts/steps, using `05_blueprints/*`, `03_reconstruction_system/RECONSTRUCTION_INDEX.json`'s decision table, and `generalization_tests/test_a_coffee_heart_visual_translation/` as a worked few-shot example. Output: populate the new Part-8 timeline schema, text-only, no assets yet. This is exactly what the repo's own `testing/GENERALIZATION_TEST_PROTOCOL.md` was designed to evaluate — running a real test through *that* protocol (not just informally, as `test_a` did) would validate this phase cheaply.
- **Phase 2 (prompt engines):** Build `generate_image_prompt`/`generate_animation_prompt`/`generate_caption_block` as assemblers over Phase 0's bibles + Phase 1's shot plan, in the demonstrated style of Part 14's real example prompts. Default motion decisions to the corpus's real house style (hard-cut, locked-camera) per Part 12, not generic assumptions.
- **Phase 3 (captions + timeline):** SRT writer over VO word-timing (reuse the existing Whisper-alignment approach); populate the full `timeline.json` schema from Part 8.
- **Phase 4 (Level 4 CapCut handoff package):** Assemble the folder structure from Part 7, generating a structured (not just prose) build-instruction file in the style already proven at Part 9's quality bar.
- **Phase 5, optional and clearly labeled experimental:** a `draft_content.json` writer for direct CapCut project generation (Level 6), version-pinned, with an explicit fallback to the Level 4 package if the CapCut version doesn't match — only build this if the user explicitly wants to accept the fragility documented in Part 6.C.

**Do not build:** a new video-forensics pipeline (the existing one is solid and out of scope), a new validator (the existing 656-line one is sufficient for the data it governs), or SFX/music generation ahead of having *any* corpus evidence to ground it — flag that as manual sound-design work rather than false-automating it.

---

## Part 17 — Final verdict

**Can this project currently create CapCut videos?**
**NO.** No code renders, assembles, or exports anything. Zero image/video/audio output files exist anywhere in the repository beyond the original 14 source MP4s and their extracted analysis frames.

**Can it create a CapCut-ready production package?**
**NO**, as an automated capability. **PARTIAL**, as a manually-demonstrated one-time capability — `generalization_tests/test_a_coffee_heart_visual_translation/` is a genuine, high-quality, whole-script production document (Level 2, bordering on Level 3 planning) for one new script, produced entirely by hand/LLM reasoning, never automated, never rendered.

**Can it generate scene-by-scene image prompts?**
**PARTIAL.** Not automatically (no generator code exists), but the underlying corpus data (`VISUAL_DNA.md`, `MASTER_ASSETS.csv`, `LITERAL_FRAME_DESCRIPTION`) and one worked manual example are strong enough that a human/LLM can do it well today, and a real generator is a comparatively small build (Part 16, Phase 0–2).

**Can it generate high-quality, consistent image prompts automatically?**
**NO.** No `STYLE_BIBLE`/`ASSET_REGISTRY`/`PROMPT_TEMPLATE` exists to enforce consistency, and no code assembles prompts at all. The one manual example is high-quality but was authored by hand for a single script, with no consistency mechanism beyond the author's own care.

**Can it generate animation/image-to-video prompts?**
**PARTIAL**, and the honest evidence says this matters less than the brief assumed — the source corpus and the one worked test example both show minimal genuine I2V need (`I2V_REQUIRED = 0` in the test; zero fades, 89.8% locked camera in the corpus). What animation-prompt text exists is retrospective/manual, not generated.

**Can existing motion intelligence drive those prompts?**
**PARTIAL.** Real, well-evidenced motion vocabulary and a real CapCut-vs-I2V decision table exist (`MOTION_DNA.md`, `RECONSTRUCTION_INDEX.json`), usable as a rules-engine seed — but nothing executes those rules automatically today.

**Can it generate SRT captions?**
**NO**, as implemented code (zero `.srt` files exist, zero SRT-writing code exists). **YES**, as a near-trivial extension — the exact input data (word-level timing) this needs is already the project's strongest asset, for content once a voiceover exists.

**Can it generate an editable CapCut project directly?**
**NO**, through any officially supported mechanism (Part 6 confirms no public CapCut API/timeline-editing interface exists). **Technically possible only** through the unofficial, undocumented, version-fragile `draft_content.json` format — not recommended as a default path.

**Can it eventually become: TOPIC/SCRIPT → IMAGES → ANIMATIONS → AUDIO → CAPTIONS → EDIT PLAN → CAPCUT?**
**Yes, plausibly** — and this repository is a genuinely strong *foundation* for that goal specifically because of its unusual intellectual honesty (every DNA/blueprint doc explicitly disclaims what isn't measured, the validator is real and rigorous, and the one manual test case proves the target quality bar is achievable). What's missing is entirely the *automation layer* on top: a script segmenter, a shot planner, prompt-assembly engines over newly-extracted style/asset bibles, a universal timeline schema, a real caption writer, and a package assembler — none of which requires touching or rebuilding anything that already works. Every missing piece maps to genuinely reusable existing data (catalogued field-by-field in Parts 3–10 and the gap table in Part 15); nothing needs to be re-derived from the source videos.

---

## Required capability table

| Capability | Existing Data | Existing Implementation | Current Status | CapCut Compatible | Missing Work | Evidence |
|---|---|---|---|---|---|---|
| Script analysis | Weak (604 sentences, no taxonomy) | None | NOT PRESENT | N/A | LLM segmenter + taxonomy | `05_blueprints/*.md` (no hook/payoff logic found) |
| Scene generation | Weak (shot/state structure as a *format* only) | None | NOT PRESENT | N/A | LLM shot planner | `01_master_data/MASTER_SHOTS.csv` schema |
| Shot planning | Weak (same as above) | None | NOT PRESENT | N/A | Planner targeting Part 8 schema | Same |
| Image prompts | Strong (style facts, one full worked example) | None (manual only) | DATA EXISTS, NO GENERATOR | N/A (prompts feed external image models) | Bible extraction + assembler | `generalization_tests/.../IMAGE_PROMPTS.md`, `02_production_dna/VISUAL_DNA.md` |
| Image generation | N/A | None | NOT PRESENT | Native AI tool exists in CapCut UI (manual) | API integration | Part 6.B (Seedream/Nano Banana Pro) |
| Animation prompts | Moderate (motion vocab, decision table) | None (manual only) | DATA EXISTS, NO GENERATOR | N/A | Assembler | `03_reconstruction_system/RECONSTRUCTION_INDEX.json` |
| Image-to-video | Weak (corpus rarely uses it) | None | NOT PRESENT / LOW PRIORITY | Native AI tool exists in CapCut UI (manual) | API integration (optional) | `I2V_DECISIONS.md`: `I2V_REQUIRED=0` |
| Motion planning | Strong (real, evidenced vocabulary) | Documented only | PARTIALLY IMPLEMENTED (as rules, not code) | Yes — maps directly to native keyframes | Rule-execution code | `02_production_dna/MOTION_DNA.md` |
| Voiceover | None | None | NOT PRESENT | Yes (WAV/MP3 import) | TTS/VO integration + realignment | — |
| SFX | **None — no corpus precedent** | None | NOT PRESENT | Yes (audio import) | Design from scratch | `MASTER_AUDIO_EVENTS.csv`: 0 SFX rows ever |
| Music | **None — no corpus precedent** | None | NOT PRESENT | Yes (audio import) | Design from scratch | Same file, 0 music rows |
| Captions/SRT | Strong (word-level timing) | None | NOT PRESENT, but low-effort | Yes (Desktop/Web only, not Mobile) | Small SRT writer | `MASTER_WORDS.csv`; official subtitle-import docs |
| Timeline | Strong (field-by-field mapping exists, Part 8) | None | NOT PRESENT | N/A (internal format) | New schema + populator | This audit, Part 8 |
| CapCut handoff | Moderate (one manual Level-2/3 example) | None | DOCUMENTED ONLY | Yes, for the file types it would contain | Package assembler | `generalization_tests/.../production_pack/` |
| Editable CapCut project | None (format undocumented by CapCut) | None | NOT PRESENT | **No official mechanism** | Unofficial `draft_content.json` writer (risky) | Part 6.C |
| Final automated render | None | None | NOT PRESENT | **No CapCut export API** | Not automatable without CapCut cooperation | Part 6.C |

---

## File-by-file trace (representative chains; ✂ marks where the chain breaks)

**Existing-video reconstruction (fully connected, for the 14 source videos only):**
`videos/<file>.mp4` → `00_source/verify.py` (SHA-256/ffprobe check) → `01_evidence/frames/*.png` + `02_analysis/TIMELINE.csv` (manual/LLM forensic analysis, no extraction code) → `01_master_data/MASTER_SHOTS.csv`/`MASTER_STATES.csv`/`MASTER_MOTIONS.csv` (manual aggregation, cross-checked by `validator/validate_brain.py`) → `02_production_dna/*.md` (regenerated statistics) → `03_reconstruction_system/*.md` (rule extraction) → **✂ no code consumes these to produce `03_capcut/CAPCUT_REBUILD.md` or `04_image_to_video/*.md`** — those per-video files were themselves manually/LLM-authored directly from the frame evidence, not generated from the master tables → CapCut (human editor, manually, never executed in this repo).

**New-script attempt (the brief's own hypothesized chain, as it actually exists today):**
New script text (user-supplied) → **✂ no segmenter exists** → `05_blueprints/*.md` + `02_production_dna/*.md` + `03_reconstruction_system/RECONSTRUCTION_INDEX.json` (read manually by an LLM) → `generalization_tests/test_a_coffee_heart_visual_translation/SHOT_PLAN.csv` etc. (hand-authored) → `IMAGE_PROMPTS.md`/`ANIMATION_PROMPTS.md`/`CAPCUT_BUILD.md` (hand-authored) → **✂ no image/video ever generated** → **✂ no timeline.json ever produced** → **✂ no CapCut project ever created**.

**`MASTER_MOTIONS.csv` → (hypothetical, does not currently exist) motion vocabulary → scene motion selection → animation prompt → image-to-video generator → CapCut clip:** breaks after step 1. `MASTER_MOTIONS.csv` → `04_patterns/MOTION_PATTERNS.csv` (aggregation exists) → **✂ no motion-selection code exists** → (manual selection only, demonstrated once in `generalization_tests/ANIMATION_PROMPTS.md`) → **✂ no generator was ever invoked** → **✂ no CapCut clip exists**.

---

## Recommendation — shortest, safest path from the current repository

Do not rebuild the brain. Do not re-run forensic analysis. Do not touch `validator/`, the 14 forensic folders, or `01_master_data/`–`05_blueprints/` — they are validated, internally consistent, and correctly scoped to what they are (a corpus analysis, not a generator). The one thing worth formally closing out first is cheap: actually run a test through `production_intelligence_brain/testing/GENERALIZATION_TEST_PROTOCOL.md` using its own `UNSEEN_SCRIPT_INPUT_TEMPLATE.md`/`TEST_RESULT_SCHEMA.json` (the informal `generalization_tests/test_a_coffee_heart_visual_translation/` folder did the work but never went through the canonical protocol/schema the brain's own author designed for it) — this reconciles the one real internal inconsistency this audit found, at near-zero cost.

From there, build only the automation layer, in the five phases laid out in Part 16, each one a thin new component sitting on top of existing, unmodified data: (0) extract style/asset bibles from `VISUAL_DNA.md`/`MASTER_ASSETS.csv`; (1) LLM-driven script segmenter + shot planner targeting a new timeline schema; (2) prompt-assembly engines defaulting to the corpus's real house style (hard-cut, locked-camera, minimal I2V); (3) an SRT writer over VO word-timing; (4) a Level-4 CapCut handoff package assembler. Treat direct CapCut project generation (Level 6, via the unofficial `draft_content.json` format) as an optional, explicitly-labeled experimental feature, never the default path, because no official CapCut API for this exists (confirmed against the official help center, 2026‑09‑21) and the only working method is a version-fragile, undocumented reverse-engineering effort maintained outside ByteDance.
