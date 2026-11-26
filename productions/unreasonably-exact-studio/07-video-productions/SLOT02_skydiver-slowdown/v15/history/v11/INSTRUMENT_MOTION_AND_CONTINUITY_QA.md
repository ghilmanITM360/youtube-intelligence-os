# Instrument motion and continuity QA — V11

## The device

- **Artwork:** Codex V11 wrist compositions, which show the sleeve, cuff, hand and the device on the wrist with a **blank** face.
  - `wrist/mounted_reference.png`: third-person forearm
  - `wrist/pov_reference.png`: first person
- **Face (code, `tools/instrument11.py`):**
  - a graduated band from light (SLOW) to deep blue (FAST)
  - 9 ticks with no numerals
  - labels **SLOW**, **FAST** and **↓ DOWN SPEED**
  - a tapered charcoal needle with a cap
- **Measured face ellipses:**
  - mounted: centre (853, 409), rx 84, ry 81, rotation −4°
  - POV: centre (829, 497), rx 76, ry 85, rotation −18°
  - Gridded sheets: `qa/G_mounted.png`, `qa/G_pov.png`
- **Needle mapping:** angle = −120° + 240° × v / 90 m/s, measured clockwise from 12 o'clock. It is one function, used in every view.
- **Not an altimeter.** The owner's reference photos show altitude instruments. This device is an illustrative downward-speed indicator: no numbers and no altitude marks.
- **Retired:**
  - V10 4-mark "clock" dial, long strap and standalone close-up
  - V9 semicircular gauge
  - Codex V11 standalone front/oblique/side device studies (they have no wrist)

## Where it appears (always on a wrist)

| Shot | Time (s) | View | Wrist visible | Needle source |
|---|---|---|---|---|
| B1/D1/model shots | — | Side pose: small device baked on the near wrist | yes | (too small to read) |
| B2 | 8.33–9.05 | Gaze: head dips toward the wrist | yes | — |
| B3 | 9.05–11.15 | Arm, cuff and hand with device; push-in ×2.4 to a readable face (**2.1 s**, previously two 0.9 s inserts) | yes, whole shot | qualitative preview 74→66 m/s, tagged "later in the fall" |
| F1–K1, M1 | 20.9–46.6, 52.2–54.5 | Circular **wrist inset**: cut-away of the mounted forearm with the device | yes | model `v(t)` |
| K1 zoom card | 42.0–46.6 | Same inset on the card | yes | model `v(t)` |
| M2 | 54.45–55.35 | Gaze to the wrist | yes | — |
| N1 | 55.35–57.16 | **First person:** your own forearm over the ground, push-in ×2.1 | yes | model `v(t)` |
| O1 | 57.16–59.35 | Same POV: tilt from the wrist down to the approaching ground; the arm leaves frame | yes, until it exits | model `v(t)` |

The device is never enlarged without its wearer. Its screen size changes only through camera framing; it keeps its size relative to the wrist.

## Speedometer sequence (brief §07), as built

1. **Context:** M1 side tracking, downward-speed arrow shortening, "downward speed decreasing".
2. **Gaze:** M2 head dips toward the wrist.
3. **Arm and instrument:** N1 first-person forearm with the device, the ground far below.
4. **Push-in:** to a readable face, while hand, cuff and sleeve stay in frame.
5. **Needle:** falls with the model (model 60→90 s, roughly 72→64 m/s).
6. **Return to the ground:** O1 tilts down and the ground grows as altitude falls.

The total is 7.2 s (52.19–59.35 s), all within the existing narration phrases 20–22. The runtime is unchanged.

## Needle continuity (verified)

- `tools/v11.py --check` asserts:
  - model time is monotonic
  - v ≥ 0
  - the needle never rises after 47.71 s
  - v > 0 once the fall starts (from 21.2 s)
- **At the reset (F1):** v = 0, so the needle sits at SLOW and the label reads "speed: zero".
- **During acceleration (H1–K1):** the needle rises.
- **Maximum:** model peak 81.0 m/s at model 20 s, which is film 43.6 s. That is STATE 2 ("balanced: top speed") on the zoom card, and the card's inset shows the needle at its highest.
- **During the slowdown:** it decreases and stays above zero. The lowest modelled value shown is about 51 m/s.
- **Across cuts:** no resets. Every model-driven view reads the same `state(model_t(t))`.
- **Exception:** B3 is a preview of a later moment and is labelled "later in the fall". It is not part of the model timeline.

## Open issues

- **Codex candidate art, not approved:**
  - the device face is blank in the art
  - straps and housing are baked into the wrist drawing, so the strap cannot move independently
- **No three-quarter view of the device** is used. The side view is only the tiny baked device on the side pose.
- The Codex side and oblique device studies exist, but **without a wrist**, so they were not used.
- **The wrist inset text "SPEED (your wrist)" is small on a phone**, and the dial labels are illegible in the inset. The inset is read by needle position only.
