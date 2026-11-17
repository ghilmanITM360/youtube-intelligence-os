# FINAL QA: Calf_Pain_PAD_FINAL.mp4

Run 2026-10-12 on the delivered file. Every result below was measured from `Calf_Pain_PAD_FINAL.mp4` itself, not from a draft.

## Technical: PASS
| Check | Result |
|---|---|
| Container / video | MP4, H.264 High, **1080×1920**, **30 fps** CFR, `yuv420p` (BT.709, TV range), 1818 frames, **60.600 s** |
| Audio | AAC-LC 48 kHz stereo 192 kb/s, **60.581 s** (source MP3 is 60.581 s, SHA-256 `b419bad2…be2bce2b`) |
| Full decode (`ffmpeg -f null`) | 0 errors |
| Black frames (`blackdetect` d≥0.1 s) | 0 |
| Frozen picture (`freezedetect` n=0.003) | 0 stretches ≥2.5 s and 0 ≥1.5 s |
| Audio identity / sync vs source MP3 | Envelope cross-correlation **0.9997**, best lag **0 ms**. Speech pauses land at the same timestamps (1.0967 s vs 1.0966 s) |
| Loudness | −11.8 LUFS vs source −11.7 LUFS. Voice untouched: no speed, pitch or edit changes |
| Fonts | Kalam 700 bundled from npm (`@fontsource/kalam`) and awaited with `delayRender`; no fallback glyphs seen in frames |
| SRT | 39 cues, contiguous 0.000 → 60.580 s, parses with ffmpeg |

Remotion's own AAC encode added a 2048-sample (42.7 ms) priming delay. `build_final.sh` therefore discards it and re-muxes the **original MP3**, which is what gives the 0 ms result above.

## Visual QA: method and outcome
- **Three full drafts** were rendered at 540×960 and reviewed on 1 fps contact sheets for every scene.
- **Motion strips** at 3–10 fps were checked for the hook walk, calf close-up, lens transition, clinic board build and finale, plus the 2.55–3.0 s caption handoff on the final file.
- **40 full-resolution frames** from the final file make up `CONTACT_SHEET.png`.

Defects found and fixed before the final render:
1. The S3 "close-up" was really a medium shot → re-framed at z 2.9–3.25 on the calf, with a slower limping walk.
2. The doctor's pointing arm read as a stick → replaced with a coat sleeve plus an articulated pointing hand.
3. Body-map artery lines ran into the patient's mouth → the carotids now end at the neck.
4. The clinic opening was static for about 2 s and the doctor covered the right board panel → a medium shot on the doctor first, then the board, which was resized and moved.
5. Captions collided with board text (S9, S13) and with clouds (S10) → titles hidden or background dimmed behind captions, clouds raised.
6. The "EARLY WARNING SIGN" text overflowed its stamp → box widened.
7. Outgoing and incoming captions overlapped for about 0.2 s at every handoff → the shared `Label` now finishes fading at `until`. Verified on the final file.

| Requirement | Outcome |
|---|---|
| Character consistency | PASS. One parametric rig with two `Look`s. Same face, hair, palette, outfit and proportions in all 13 shots, including the board minis, the badge and the body map |
| Real animation | PASS. Procedural walk cycle with knee bend and arm swing, limp, a one-leg calf clutch with hop, sitting, calf rubbing (IK), standing and walking off, waving, pointing (IK), head shake, crouch with magnifier, blinks, loudness-driven lip-sync, a pumping personified muscle, flowing blood cells, growing plaque, O₂ bubbles, gauges, signal pings, line boil |
| Retention | PASS. Frame 0 is the patient mid-stride. "CALF PAIN" pops at 0.22 s. A new visual beat comes every ≈1–2 s, and freezedetect finds no 1.5 s static hold. The final frame shows doctor, magnifier, "ALWAYS, ALWAYS / INVESTIGATE" |
| Narrative coverage | PASS. All 39 caption units have a matching visual (map below), including the last word "investigate" (≈60.0–60.4 s) |
| Safe zones | Captions are placed at y 300–560, and the footer note at y 1440 (inside 230–1480). Checked by layout, not with a live YouTube UI overlay |

### Narration → visual map (real audio times)
| Audio | Visual |
|---|---|
| 0.0–4.3 | Park: walk → calf glow → limp → clutch → bench → relief (green) → concern; "CALF PAIN / EASES WITH REST / DON'T IGNORE", red circle on calf, "?" |
| 4.3–5.9 | Dr. Rahim slides in waving, "Dr. Rahim" tag pops, patient surprised |
| 5.9–10.3 | Calf close-up walking with pain pulsing on each step, cramp shake, doctor's hand points; "INTERMITTENT CLAUDICATION = pain that comes & goes"; stops → pain fades; magnifier lens opens into the leg |
| 10.3–13.6 | Artery plaque grows (cross-section inset), cell flow thins downstream, calf muscle glows, "DURING ACTIVITY" badge |
| 13.6–15.7 | Personified muscle working → strained; NEEDS vs GETS O₂ bars; O₂ gauge falls to LOW |
| 15.7–19.0 | Park cycle PAIN → REST → RELIEF → WALK → loop, acted out by the same patient |
| 19.0–25.5 | Leg: early-signal pings, more plaque, "PERIPHERAL ARTERIAL DISEASE (PAD)"; zoom out to body map, artery tree draws to the heart, pulse travels, heart beats, brain + ↑ arrow, "CARDIOVASCULAR RISK" |
| 25.5–32.9 | Clinic: doctor "THE SIGNAL DOCTORS WATCH MOST", board writes CLAUDICATION, builds WALKING = PAIN panel then RESTING = RELIEF panel, doctor points to each |
| 32.9–35.9 | Doctor medium shot (dimmed background) "CLINICALLY SIGNIFICANT"; cut to panel, red calf circle, "EARLY WARNING SIGN" stamp |
| 35.9–42.6 | Dusk park: patient seated but still in pain, rubbing calf; "usually: eases with rest" struck through → "CONTINUOUS PAIN / EVEN AT REST", clock spins; doctor arrives concerned; "may signal severe BLOOD-FLOW LOSS" |
| 42.6–50.6 | Anatomy: near-occluded artery, trickle flow; "SERIOUS / PERSISTENT PAIN AT REST → seek prompt medical assessment"; pull-out; doctor presents; blood-flow gauge drops; tired muscle face "→ muscles affected" |
| 50.6–55.3 | Research papers pop and get checked; body map with calf pain, heart beating harder, ↑ arrow grows, brain icon; "ELEVATED CARDIOVASCULAR RISK" |
| 55.3–60.6 | Clinic: patient limps in, doctor shakes head "DON'T DISMISS leg pain when walking", raises finger, crouches with a magnifier showing the narrowed artery; "ALWAYS, ALWAYS / INVESTIGATE"; patient nods |

## Medical accuracy
Checked against the AHA "Top Things to Know: 2024 Lower Extremity PAD Guideline" page (read in the browser; the fetch tool got HTTP 403). That page says PAD is associated with increased MI, stroke and death, lists claudication and chronic limb-threatening ischemia (CLTI) as separate clinical subsets, and says detection relies on history, exam and the resting ABI.

On screen:
- Claudication is shown as walking pain that eases with rest.
- Rest pain is worded "may signal severe blood-flow loss" and "persistent pain at rest → seek prompt medical assessment". It is never presented as a CLTI diagnosis.
- "Not every cramp is PAD. A clinician can tell." is shown from 57.6 s.
- Risk is shown as direction only (↑). There are no statistics, no gore and no stock footage.

## Audio / transcript discrepancies (flagged, voice unaltered)
| Time | Supplied script | ASR (faster-whisper small.en) | Handling |
|---|---|---|---|
| 41.5 s | "critical demischemia" | "critical nimischemia" | Almost certainly "critical limb ischemia". **SRT shows `critical [limb] ischemia`** with the brackets marking an inference. The screen avoids the term (see above). **Unresolved: a human listen is recommended.** |
| 5.2 s | Dr. Rahim | "Rahin" | Treated as an ASR error |
| 26.9 s | "watch the most" | "watch the mode most" | Possible narrator stumble; SRT follows the script |
| 28.6 s | "that is, calf pain" | "There is calf pain" | SRT follows the script |
| 15.2 s | "run low on oxygen" | "low in oxygen" | SRT follows the script |
| 42.6 s | "which is a serious" | "It is a serious" | SRT follows the script |

SRT wording follows the supplied script. SRT timing comes from ASR word starts on the real MP3. No human listening pass was done.

## Remaining limitations (genuine, not blocking)
- Lip-sync is driven by the loudness envelope, not phoneme-accurate.
- There is slight foot sliding in walk cycles during speed changes.
- In the finale the magnifier sits over the shin/knee rather than exactly on the calf glow, because of the crouch's reach limit.
- In the final 3 s the footer note slightly overlaps the patient's shins (it stays readable thanks to its outline).
- During the S8 board push-in the doctor is partly cropped at the right edge (intentional framing).
- The video is narration only: no music or SFX were added, since none licensed were available.
- The intermediates `project/out/` (92 MB) and the alignment venv `.asr-venv/` (214 MB) can be deleted; `npm run final` rebuilds the MP4.
