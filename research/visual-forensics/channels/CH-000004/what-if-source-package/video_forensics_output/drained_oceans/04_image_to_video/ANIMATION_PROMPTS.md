# Animation prompts

Only A06 and A10 show continuous change requiring I2V. Other A-IDs are hard cuts, discrete layer/pose replacements, or text/shape reveals; assemble those directly so generator drift does not reduce fidelity.

## A06

- Shot: S02
- Source image: IMG02
- Source/target: F02.1 to F02.2
- Duration: 0.625 s
- Moving element: water curtain inside upper display only
- Static anchors: screen border, black Mars ridge, presenter, loose paper, red top line, canvas framing
- Prompt: `Locked camera. Inside upper rectangular display only, dense straight pale-grey vertical water lines rapidly fill downward from red top line until they cover sky above black ridge. Keep border, ridge, arms-raised presenter, loose paper, red line and white page perfectly fixed. No splash, camera drift, lighting change or motion outside display.`

## A10

- Shot: S05
- Source image: IMG06
- Source/target: F04.0 to F05.0
- Duration: 2.333 s
- Moving element: radial streak field and central tapered black form
- Static anchors: lower curved black edge forms and locked frame
- Prompt: `Locked camera. Fast straight downward plunge through pale-grey tunnel: thin white radial streaks stream toward lower-center vanishing point while central tapered black form travels down and recedes slightly. Keep lower curved black edge forms fixed. No rotation, side drift, new objects, lighting change or text. End in same down-tunnel composition.`

## State-replacement handling

- A01, A02, A05, A08, A12, A15, A18, A21, A25, A26: exact editor text/shape overlays; no I2V.
- A03: replace C01 with C02 and reposition O01 in final assembly; no synthesized limb motion is evidenced.
- A04, A07, A09, A11, A13, A16, A17, A19, A20, A22, A23, A24, A27, A28, A29: hard cut at timeline timestamp; no I2V.
- A14: swap counter and C03 pose simultaneously in final assembly; no in-between animation.
