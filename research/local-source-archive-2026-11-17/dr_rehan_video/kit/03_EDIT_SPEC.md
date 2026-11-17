# 03: Edit spec (Phases 3–4)

Target feel: **modern, minimal, cinematic medical explainer**, as if a skilled editor made it in After Effects and Premiere. Clean typography, keyframed motion with real easing, mask reveals, a little light 3D, and careful sound. Never "AI-generated".

---

## 1. Tool stack (decided after auditing the repos; details in `04_TOOLS_AND_SETUP.md`)

| Job | Tool |
|---|---|
| Compositing, keyframes, masks, typography, captions, render | **HyperFrames** (HTML + GSAP → deterministic MP4). Read its skill references before building: `motion.md`, `overlays.md`, `captions.md`, `sound.md`, `look.md`, `review.md` |
| Subject matte (text and graphics *behind* Dr. Rehan) | `npx hyperframes remove-background talk.mp4 -o rehan_matte.webm` |
| Light 3D (heart, artery tube, glucose molecules) | Three.js inside HyperFrames, following **threejs-skills** (r186 API) |
| Media prep: probe, re-encode, loudness, denoise, reframe checks | **ffmpeg-skill** tools (`probe`, `loudness`, `denoise`, `fit`, `check`, `verify`) |
| Word timestamps (doctor + narrator) | faster-whisper `large-v3` (Urdu). Never an `.en` model |
| Direction, sound and rhythm rules | Lemo-Opuscar `DIRECTOR.md` §6–§11 (sound, rhythm, camera, failures, delivery checks) |
| Talking-head rules (face-safe captions, B-roll budget) | ghost-editor `SKILL.md` + `references/` (read as knowledge. The tool itself is Mac-only) |

**Not used:** AI video generators, MotionClone, avatar tools.

---

## 2. Visual direction (default recommendation: "Clinical Calm")

Propose 3 options at GATE 0. This is the default to recommend unless the references say otherwise:

- **Palette:** warm off-white `#F4F1EC`, ink navy `#14213D`, warm grey `#8A8A8A`, and **one accent, clinical red `#D64545`** (heart, danger, the key word). A sugar/diabetes sub-accent `#E0A526` only in diabetes chapters. Max 3 colours on screen.
- **Type:** Latin: a grotesk (Inter / Manrope / "Instrument Sans") plus one serif for emotional words (Instrument Serif / Fraunces). Urdu: **Noto Nastaliq Urdu** for titles (test the render) or Noto Naskh Arabic for captions (more legible at speed). Max 2 families per frame.
- **Grammar:** Swiss-style grid, lots of negative space, one idea per frame, numbers huge, labels small.
- **Texture:** subtle paper/film grain (ffmpeg grain at master, light), soft vignette. No glows, no neon, no lens flares, no "tech HUD".
- **Signature device (pick one, use it throughout):** an **ECG line** that draws on, becomes the wipe between chapters, and flatlines into silence before the key point. Or a **pipe/artery line** that the camera travels along.

Useful Lemo-Opuscar style references to study for the motion language (read `styles/<slug>/STYLE.md`; don't copy the demos): `swiss-motion`, `dataviz`, `microscope`, `whiteboard`, `caption-news`, `white-model`.

---

## 3. Layouts

### Dr. Rehan segments (his footage, 16:9)
Rotate these layouts so no layout runs longer than ~20 s:
1. **Full frame** with a light grade, plus slow keyframed **punch-ins** (scale 1.00→1.06 over 4–6 s, or a cut-zoom to 1.12 on an emphasis word). Never more than 1.15×, to avoid soft footage.
2. **Keyword pops**: 1–3 words appear on the exact spoken word (word timestamps), placed in the empty side of the frame and **never over his face**. Run face detection (mediapipe) → `face.json` and keep text outside the face box + 10% margin.
3. **Text behind subject**: big title placed *between* the background plate and his matte (`rehan_matte.webm`). Use it 2–4 times per video, on chapter titles only.
4. **Split card**: video moves to one half (wrapper transform, 0.5–0.7 s, `power2.inOut`), and a code-drawn diagram builds on the other half while he explains. Positions from HyperFrames `overlays.md` (split 960/960 landscape).
5. **Cutaway**: a full-screen graphic or plate while his voice continues (L-cut). Limit: cutaways cover **at most ~30%** of his on-camera time. Viewers trust the doctor's face.
6. **Lower third** (first appearance + once mid-video): name and title, see `05_DR_REHAN_INTRO.md`.

### Narrator segments (no presenter on screen)
Full-screen motion-graphic scenes: a generated plate with a parallax push, mask reveals, typography, code diagrams. The narrator's voice is the clock: every visual change lands on a word.

### Version B (9:16)
- Portrait layouts from `overlays.md`: **stack** (his video on top 1080×844, card or diagram below) or **face-tracked full-height crop** (crop window follows `face.json`, smoothed, no jitter).
- Captions bigger (landscape size × 1.3), inside safe areas (top 15% and bottom 20% stay clear for platform UI).
- Structure: 0–2 s text hook + strongest visual → hook line → doctor's best 20–60 s answer → 1 payoff line → end on a frame that loops or teases the full video.

---

## 4. Motion grammar: how to look hand-made, not AI

Follow HyperFrames `motion.md` exactly. The most important points:
- **Keyframed easing by role:** arrivals `expo.out` / `power4.out` (long tail), camera moves `power2.inOut`, exits `power3.in` and **40–50% shorter** than entrances. Never the same `power2.out 0.5s` on everything; that uniformity is what makes edits feel generated.
- **Overlap:** the next element starts when the previous is 30–50% done. Stagger words 60–120 ms, letters ~1 frame.
- **Masks everywhere** (the AE look): text revealed by a moving rectangle mask, wipe reveals following the ECG line, circular iris onto a detail, shape-layer transitions, track-matte style (type filled with footage or texture). Build them with `clip-path` / SVG masks animated by GSAP.
- **Generated stills are never shown flat.** Each one gets at least two of: cutout/mask reveal, 2.5D parallax (layers at different speeds), slow push or rack-focus blur, a grade to the palette, grain. Hold no still longer than ~4 s without movement.
- **Motion blur** on fast moves (`data-motion-blur="on"`).
- **Landed titles are still**: once text lands, move the camera or the background, not the text.
- **Read time:** hold any line ≥ 0.5 s + 0.3 s/word (Urdu captions: at least the spoken length + 0.6 s).
- **Variety:** at least 4 kinds of camera move and 4 kinds of text entrance across the video. No entrance repeated three times in a row.
- **Light 3D, used sparingly:** a matte, minimal heart (low-poly or clay-like, palette colours, soft studio light) rotating slowly. An artery tube showing flow and a blockage forming (shader or instanced particles). Max 3–4 short 3D moments. 3D supports the doctor; it never competes with him.

---

## 5. Captions

- Burned-in, word-timed, from whisper word timestamps (check them by ear. Whisper invents words over silence; drop them).
- Caption language as chosen at GATE 0. Max 2 lines, max ~6 words per line. The key word gets the accent colour.
- Never over his face, and never over a diagram's important part.
- Also export `.srt` for YouTube.

---

## 6. Sound design (follow Lemo `DIRECTOR.md` §6–§7 + HyperFrames `sound.md`)

- **Three layers:** voice (doctor + narrator), music bed, SFX. Duck the music −12 to −18 dB under voice.
- **Match the two voices:** same EQ, compression and loudness chain on the doctor and the narrator so they feel like one production. Light denoise on the doctor if the room is noisy (don't over-process).
- **Every visible action has a sound:** text pop = soft click, mask wipe = air whoosh, the ECG line = beep, a number counter = ticks, a 3D heart = low heartbeat. Subtle levels.
- **At least 2 real silences** (or near-silences) before key medical points. The first sound after the silence matters most.
- **J-cuts and L-cuts** at least twice: the next speaker's audio starts before the picture changes.
- Use the user's sounds from `input/references/` first.
- Master: **−14 LUFS integrated, true peak ≤ −1 dBTP** (ffmpeg-skill `loudness.py -I -14 --tp -1`).

---

## 7. Build order

1. **Prep:** copy the source into `04_edit/media/`; re-encode with keyframes every frame-second (`-g <fps>`) so seeking doesn't freeze; normalise the audio; transcribe (word level); face-track; make the matte.
2. **Align:** place each narrator MP3 by its EDL slot. Transcribe the narrator files too and confirm the words match `vo_lines.md` (flag mismatches to the user).
3. **Animatic first:** an audio-only timeline + rough blocks (no styling) → render a low-res animatic → check pacing and total length → then style.
4. **Build chapter by chapter**, one HyperFrames sub-composition per chapter (keeps tracks under the density limit).
5. **Version A complete → then Version B** (reuse components with portrait layouts).
6. Render drafts at 1080p (keep source fps; usually 25 or 30).

---

## 8. Review loop (before GATE 3)

- Contact sheet: 1 frame every 2 s; the 0.2 s strips of key animations, enlarged.
- One full-speed viewing with sound, noting the exact second of every problem.
- `npx hyperframes check` / lint; ffmpeg-skill `check.py` / `verify.py` (black frames, frozen frames, audio clipping, loudness).
- Send the user: the draft MP4s, a 10-line summary, and 2–3 specific questions (not "is it ok?").

---

## 9. 10/10 QC checklist (all must pass before final)

**Story & clarity**
- [ ] First 15 s: situation, contradiction, reason to watch, handover. Would a stranger keep watching?
- [ ] Every hook promise is paid off; every open loop closes.
- [ ] Every jargon term is explained the first time it appears.
- [ ] No new medical claim from the narrator; all `⚠️ DOCTOR CHECK` items approved.
- [ ] Dr. Rehan's meaning is unchanged; trims are listed in `EDIT_NOTES.md`.

**Picture**
- [ ] No text over his face; nothing important in the platform UI zones (Version B).
- [ ] No still image held flat; no AI-looking face anywhere; no text baked into generated images.
- [ ] Anatomy drawn correctly (code-drawn, checked against the doctor's explanation).
- [ ] No layout runs > 20 s unchanged; ≥ 4 camera-move types; ≥ 4 text-entrance types.
- [ ] Palette ≤ 3 colours per frame; fonts ≤ 2 families; Urdu renders correctly (no broken ligatures).
- [ ] No black or blank frames in transitions; no jitter in face-tracked crops.

**Sound**
- [ ] −14 LUFS, true peak ≤ −1 dBTP; doctor and narrator matched in tone and level.
- [ ] Music ducked under voice; ≥ 2 deliberate silences; ≥ 2 J/L-cuts.
- [ ] Every SFX and music track has a licence in `CREDITS.md`.

**Delivery** (`05_delivery/`)
- [ ] `RehanExplainer_16x9.mp4`, `RehanShort_XX_9x16.mp4`, `.srt` per video
- [ ] `thumbnail_frames/` (5 best frames of Dr. Rehan's expressions + 3 graphic frames for thumbnail use)
- [ ] `CREDITS.md` (fonts, music, SFX, generated images and their tool), `EDIT_NOTES.md` (trims, known limits)
- [ ] Project source + one-command render script, so the user can re-render after small text fixes.

One fix round after GATE 3: fix everything listed, re-check once, deliver. Later notes from the user are new rounds; change only what they ask.
