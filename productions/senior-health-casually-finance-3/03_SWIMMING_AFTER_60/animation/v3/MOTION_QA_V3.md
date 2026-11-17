# Swimming After 60 — V3 motion QA (review version)

Output: `Swimming_After_60_V3_REVIEW.mp4` (+ `_MOBILE_540x960.mp4`), built by `../project_v3.py` with `tools/anim_v3.py`
and `tools/rig.py` (`SwimRig`). V2 files and `project_v2.py` are unchanged.

## Defect (V2) and root cause
June's arms and legs were rigid SVG parts rocking ±15–18° (arms) and ±7° (legs) about fixed pivots. The near arm never left
the water, the far arm never entered it, and no elbow or knee ever bent. It read as one arm paddling, not a crawl stroke.

## V3 fix (underlying joint motion)
Both arms and both legs are redrawn every frame by `rig.SwimRig` in the same skin colour and stroke widths as the SVG parts.
The body, head and cap stay the original rasters. The far arm and far leg are drawn behind the body.

**Arms:** freestyle, alternating, half a cycle apart (never mirrored).
- Each arm runs entry → catch → pull under the body → exit at the hip → recovery over the water → entry. The upper arm
  circles the shoulder once per cycle (Catmull-Rom keys `UPPER`).
- The elbow flexes one way only. It bends 5–42° in the pull (high-elbow mid-pull, forearm vertical under the shoulder)
  and 15–30° in the recovery.
- The recovery is a relaxed near-straight arm. A hanging-forearm (high-elbow) recovery was tried in the loop test and
  rejected: the near shoulder sits at the waterline and the forearm (89 px) is longer than the upper arm (87 px), so a
  hanging forearm dipped the hand into the water mid-recovery.
- Shoulder roll: the recovering shoulder lifts 5 px and the pulling shoulder drops.

**Legs:** 6-beat flutter kick (3 kicks per leg per arm cycle), driven from the hip.
- Thigh ±7°; knee bends up to 18° at the top of the downbeat.
- Only the heels just break the surface. In the first test the far leg kicked about 50 px out of the water; this was
  reduced and re-checked.

**Body:** gentle rise and fall, 2 px twice per cycle. Forward travel is unchanged from V2 (linear, x 250 → 90).

**Cycle:** 1.5 s per arm cycle (40 cycles/min, a relaxed recreational rate). The first loop test ran at 1.2 s, which read
too brisk for the topic.

**Water (only at real contacts, all functions of phase, so they loop):**
- Foam ring and a few droplets at each hand entry.
- Bubbles trailing the pulling hand under water.
- Two bow ripples ahead of the head.
- A small spray only when a foot rises through the surface.
- The front water layer (55%) is kept from V2, so submerged limbs read as under water.

**Biomechanics references:**
- Hsu et al. 2024 (PMC11531034): freestyle arms alternate; there is a 6-beat kick and a body roll. These set the stroke
  structure and kick ratio. Joint-angle magnitudes are an animator's choice, not measured values.
- The running references (PMC2973845, PMC6424559) do not apply here.

## Red opening headline bar
- **Text:** "SWIMMING AFTER 60" / "HEART BENEFITS?". This is the same component as HIIT and Running: solid red
  (206,32,41), white Arial Black, x 60–1020 px, top at y 160 px.
- **Timing:** frames 0–73 (0–2.48 s): the first sentence and the "9.5 out of 10" rating. It enters with a 6-frame fade and a
  14 px settle, and exits with an 8-frame fade and lift at the S02 cut. It never reappears.
- **Clearances:** it does not cover the swimmer, the heart, the 9.5 badge (y ≥ 470) or the captions.
- **Wording:** an editorial hook, not a medical claim. The speaker calls swimming good for the heart and "one of the best"
  (attributed as the speaker's view in S02/S03, unchanged).

## Checks run
**Rig self-check** (`python3 tools/rig.py`, `qa/RIG_CHECK_V3.json`, 360 samples per cycle):

| Check | Result |
|---|---|
| Arm segment length error | 0.000 px |
| Loop closure (pose at p=0 vs p=1) | 0.000 px |
| Max hand step per 1/360 cycle | 4.7 px |
| Recovery hand y, max (waterline 160) | 93 (near arm), 59 (far arm): always above water |
| Pull hand y, min | 300 (near arm), 258 (far arm): always below water |
| Elbow flexion range | 3–42°, one direction only |

**Encoded-video temporal review** (decoded from the final MP4 with `tools/motion_qa_v3.py`):
- `GAIT_PHASES_V3.png` / `qa/swim_S2_PHASES.png`: 8 evenly spaced phases of one cycle (t=3.0–4.5 s), plus the frames
  either side of both hand entries and the loop boundary.
- `qa/swim_S2_SEQUENCE.png`: every frame of two cycles.
- **Observed:**
  - The two arms alternate: one recovers over the water while the other pulls under it.
  - The legs alternate.
  - The hand enters at the surface ahead of the head, with foam starting on the contact frame.
  - Bubbles follow the pull.
  - There is no pop at the entry frames or the loop boundary.
  - Limbs stay attached at the shoulder and hip.

**Before/after:** `MOTION_V2_V3.png` shows V2 (top) and V3 (bottom) at the same 8 timestamps.
`qa/swim_v2_S2_*` is the same review of V2.

**Render QA** (`RENDER_QA_V3.json`):

| Check | Result |
|---|---|
| Duration | 17.867 s, 1080×1920, 30 fps |
| Decode errors | none |
| A/V delta | 0.000 s |
| Peak | −1.0 dBFS |
| Blank frames | 0 |
| Review marks in frames | none |
| `CAPTIONS_V3.srt` | byte-identical to `CAPTIONS_V2.srt` (9 cues) |
| Audio | identical to V2: the same narration, music and SFX |

- **Frame-change flags:** 0.1 s (bar entrance) and 2.4–2.5 s (bar exit plus the planned S02 headline change). V2 had none.

## Limits / still open
- "Watching" here means frame-by-frame inspection of consecutive decoded frames. No human has viewed it at playback speed;
  the owner should watch the MP4.
- 2D side view: there is no visible body rotation (the torso raster is fixed); roll is only implied by the shoulder lift.
- The near arm passes in front of the cap at full reach.
- The face sits half under the waterline, as in V2 (breathing is not animated).
- The splashes are deliberately small; the owner may want them stronger or weaker.
- Human listening, the clinical review of S5 (joints) and the "best" ranking, and owner approval remain open from V2.
