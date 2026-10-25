# Shot Design Blueprint

Rebuilt from the validated `01_master_data/` tables. The prior version of this
document was generic graphic-design boilerplate (specific pt sizes, hex color
codes, DPI/stroke-width rules, fixed fade/animation durations) with no
supporting column anywhere in the schema — none of it was measured from this
corpus. It is replaced below with only what the data actually supports.

## Camera and Composition (measured)

- **Support:** 581 states (`MASTER_STATES.CAMERA_STATE`).
- 522/581 states (89.8%) report a LOCKED- or STATIC-family camera state — the
  corpus overwhelmingly uses a fixed, non-moving frame; illustrated content
  changes within the frame rather than through camera movement. See
  `VISUAL_DNA.md` for the full distribution.
- The one sustained exception is `worlds-largest-cities-what-if` S02, a single
  ~79s continuously-panned map shot (`CAMERA_STATE` values `PAN`/`PUSH-IN`/
  `HOLD`) — a deliberate outlier, not representative of the corpus norm.

## Shot Transitions (measured)

- **Support:** 186 internal shot-to-shot boundaries (`MASTER_SHOTS`, all 14
  videos).
- Every shot boundary measures a `0.0s` gap — no fade, cross-dissolve, or hold
  frame exists anywhere in this corpus; every transition is a hard cut at
  1-frame resolution. See `DECISION_RULES.md` §7 and
  `04_patterns/TRANSITION_PATTERNS.csv` (`TYPICAL_DURATION_SEC` = `0.000` for
  all 82 transition-text groupings).
- Do not add a fade/cross-dissolve duration when reconstructing shots in this
  style.

## Shot and Motion Duration (measured)

- **Shot duration** (n=200): mean 10.54s, median 7.77s, range 1.54–78.91s (see
  `EDITING_DNA.md`).
- **Motion duration by RELATIONSHIP type** (n=438): `STATE_REPLACEMENT` avg
  1.60s, `SEQUENTIAL` avg 3.51s, `SIMULTANEOUS_COUPLED` avg 4.26s,
  `SIMULTANEOUS_INDEPENDENT` avg 4.50s, `PERSISTENT_LOOP` avg 9.42s,
  `CAMERA_SUBJECT_COUPLED` avg 7.66s — see `DECISION_RULES.md` §3. Use the
  RELATIONSHIP-appropriate average, not a single fixed animation-duration
  range.
- **Motion-to-speech alignment**: 99.5% of motion starts and 98.8% of motion
  ends occur during or immediately adjacent to an active spoken word — trigger
  animation starts on the nearest word boundary rather than a fixed delay
  (`DECISION_RULES.md` §4).

## Asset Presentation (measured)

- **Support:** 448 assets (`MASTER_ASSETS`).
- Per-type format/transparency/recreation-method breakdown (e.g. CHARACTER
  assets 96% transparent PNG, ENVIRONMENT assets 88% opaque full-frame
  plates) is in `ASSET_CREATION_SYSTEM.md` — use that instead of a generic
  "match DPI/stroke width" rule, since the schema has no DPI, stroke-width, or
  lighting-direction field to measure those claims against.

## What is NOT supported by current data

- No color palette, hex value, or hue-coding convention exists anywhere in
  the schema (`MASTER_STATES`, `MASTER_ASSETS`) — any specific background,
  text, or accent color claim would be invented, not measured, and is
  omitted. `LITERAL_FRAME_DESCRIPTION` text does describe some frames as
  black-and-white line art or "off-white portrait field," but this is
  per-state prose, not a coded palette rule that generalizes across the
  corpus.
- No typography measurement (point size, weight, font) exists in the schema —
  the prior "48-72pt titles / 28-40pt body" figures were not derived from any
  column and are omitted.
- No fixed reveal/hold animation timing (e.g. "fade-in over 0.3-0.5s", "hold
  0.5-1.0s after animation") is supported — use the measured
  RELATIONSHIP-based motion durations above instead.
