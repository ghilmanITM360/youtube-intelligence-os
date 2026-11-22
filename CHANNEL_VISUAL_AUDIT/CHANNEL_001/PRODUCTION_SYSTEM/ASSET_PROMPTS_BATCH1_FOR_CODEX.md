# Codex asset prompt package, batch 1 (CasuallyFinance visual system)
Status: **prompts only. No image below has been generated.** Output dir: `CHANNEL_VISUAL_AUDIT/CHANNEL_001/PRODUCTION_SYSTEM/assets_codex/` (create). After generation: run `python3 import_assets.py assets_codex/` (validates RGBA, transparent corners, size) then review frames visually before registering.

## Global art-direction block (paste at the top of every prompt)
Flat hand-drawn explainer style, as in a doodle whiteboard cartoon. Clean thick black outline (about 3 to 4 percent of asset height), slightly wobbly marker line, flat fills with at most one soft shade, no gradients, no glow, no photorealism, no text unless stated. Transparent background (PNG RGBA), subject centred with 4 percent padding, no cast shadow, no drop shadow. Palette: outline #0E0E0E, skin #D3AD82, hair #6C4E36, money green #58682F / #309050, gold #EBBE32, accent red #C8282D, sky blue #CDE1F5. Canvas 2048 x 2048 unless stated. Do not copy any existing brand, logo or real person.
Negative: no background, no frame, no watermark, no signature, no extra fingers, no 3D render, no photo texture, no text.

## Character identity (CHAR_STICK_01): consistency rules
Egg-shaped head about 1.1 x wider than tall; scribbly brown hair cap swept to the viewer's left; two small solid-black oval eyes; one-stroke mouth; skin #D3AD82; body is a single thin black line (8 px at 1080 scale), thin line arms and legs, no hands detail, no clothes. Same head size and body length in every pose. **Heads and arms must be separate layers** so they can be swapped (see file list).

| id | purpose | exact description | layers/variants | file |
|---|---|---|---|---|
| A001 | model sheet, consistency anchor | CHAR_STICK_01 full body, front, neutral face, arms relaxed, 2048x2048 | single | `char_master_sheet.png` |
| A002 | expression library | head only (hair + face), 5 expressions: neutral, worried (brows up, wavy mouth), happy (smile), shocked (round mouth, wide eyes), sweating (blue drop right of face). Each 1024x1024, identical head outline | 5 files | `char_head_{neutral,worried,happy,shocked,sweat}.png` |
| A003 | pose library | arms+torso+legs without head, 5 poses: shrug, arms down, one arm up, pointing right, hands on hips. Neck anchor at exact centre top of canvas so any head aligns | 5 files | `char_body_{shrug,down,up,point,hips}.png` |
| A004 | chart prop | landscape card 2048x1600: pale blue #CDE1F5 rectangle with thick uneven black border, dotted x and y axes (bottom and left), THREE thick wavy jagged line charts: red, green, cyan, overlapping, 3 to 5 peaks each, line width about 5 percent of height. No text, no numbers | single | `prop_chart_screen.png` |
| A005 | money sacks | two olive green tied sacks, left one behind right one, slightly tilted toward each other, bold yellow $ on each, black outline, 2048x1600 | single | `prop_moneybag_pair.png` |
| A006 | question mark disc | solid black circle with a white hand-drawn question mark (marker style, not a font), 1024x1024 | single | `prop_qcircle.png` |
| A007 | cartoon Earth | round Earth with simple continents, big cartoon eyes and small mouth; variants: neutral, sweating (blue drops), burning (orange/red flames around the lower half as separate layer). Flat style as above | body, face_neutral, face_sweat, flames | `prop_earth_{body,face_neutral,face_sweat,flames}.png` |
| A008 | dollar sign | chunky green $ with thick black stroke, 1024x1536 | single | `prop_dollar_sign.png` |

Acceptance criteria (every asset): RGBA with fully transparent corners; subject fills 85 to 92 percent of the canvas; outline weight consistent with CHAR_STICK_01; head in A002 swaps onto every A003 body without visible seam at 1080 px scale; palette within 10 percent of the listed hexes; no text artifacts; passes side-by-side visual check against reference thumbnail (human or independent reviewer).
Do-not-assume: until files exist in `assets_codex/` and pass `import_assets.py` plus a visual check, they are NOT_AVAILABLE and renders keep the code_v0 assets.
