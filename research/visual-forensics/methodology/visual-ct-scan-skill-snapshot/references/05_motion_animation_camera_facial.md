# 05 — Motion and animation forensic grammar, facial acting, cinematography

## Event anatomy

For any meaningful moving subject/graphic/camera: initial pose/position/size; preparation/anticipation; onset; direction; amplitude; acceleration; primary movement; peak/contact; deceleration; overshoot; secondary motion; hold/settle; exit/transition; audio trigger; previous/current/next state; first and final source PTS and frames (if measurable). Do not assume smooth interpolation from one screenshot; inspect consecutive frames.

## Human and character motion

Walking/running cadence, limb lead/lag, gesture order, wrist-hand/finger path, shoulder/torso/head coupling, weight transfer, foot planting/sliding, collision/contact, bounce/fall/squash/stretch, held poses, idle loops, blinking, eyebrow changes, eye/mouth geometry, reaction timing, exaggerated replacements. Identify pose-swap vs rig-like interpolation without asserting exact rig/software.

## Object animation

Translate/scale/rotate/opacity/mask/crop/morph/particles; anchor point; speed/timing; objects entering/exiting, recurring props, collisions, appearance during narration; layer stacking, motion occlusions; static anchors and their function. Distinguish decorative micro-motion from informational change; extra motion may worsen comprehension.

## Camera and cinematic grammar

- Framing: wide/medium/close/insert/POV, angle/elevation, blocking, depth and focus, light direction/key-fill-rim cues, shadow, exposure and practicals.
- Movement: pan/tilt/truck/dolly-like, zoom/push/pull, orbit/crane-like, parallax, handheld simulation, motion match, snap/whip, stable hold.
- Track apparent background/foreground relative motion to separate camera vs subject movement; note composited digital scale as plausible alternative. **Exact focal length requires metadata or strong calibration**.
- Camera psychology—e.g. a push could emphasize significance—is a hypothesis, not observed motivation.

## Motion measurement

Measure x/y/scale/angle/opacity at multiple actual timestamps; estimate temporal ease from position curves only when enough samples exist, otherwise label slow/abrupt/eased appearance. `Linear`, `ease-in-out`, `back/overshoot`, `spring` are observed-shape descriptions unless source curve controls verified. Record artifact confidence, frame duration, variable FPS. Outlier cut detector results cannot stand in for animation frequency.

## Continuity errors / quality

Temporal flicker, clothing/face morph, palette variation, line-weight inconsistency, floating objects, geometry intersections, foot sliding, perspective jumps, missing shadows, text instability, aliasing/ringing, motion judder, inconsistent object scale and lens perspective. Distinguish intentional abstraction from probable error and provide frame receipts.

## Deliverables

Motion Event Ledger: interval start/end PTS, entity ID, property change, onset/peak/settle, trajectory, audio relation, measurements and limits. Facial Grammar: recurrence, expression map and cue synchrony. Camera Grammar: shot classes, static anchors, depth/parallax, moves, edit transitions. For unrelated media, mark facial/camera/physical categories N/A rather than inventing.
