> 2026-11-21 NOTE: the character below ("Mara") is SUPERSEDED by the owner-directed male renter; see STORYBOARD.md CHARACTER_SPEC and codex_art/HANDOFF.md.

# Codex asset handoff: V1 Rent (Claude owns research, screenshots, sync, charts, type, highlights, animation, audio, render, QA)
Codex makes ONLY illustrated assets. No data screenshots, no charts, no logos, no fake articles, no real-person likeness.
Global style: flat 2D vector look, 3 px ink outline, soft flat shading, no gradients/glow. Palette: olive 5B6B3A, cream F4EDE1, ink 1F2430, coral E8604C, sky A9C7D9. Transparent PNG (RGBA), 2048 px tall character, 300 px margin-free tight crop. Filename: v1_<id>_<variant>.png. Consistency: same face, glasses, bob, cardigan in all poses; same line weight.

Character: Mara Ellis, original fictional early-30s American renter. Oval face, short dark bob, round tortoise glasses, olive cardigan, white tee, jeans, white sneakers. NOT the Casual Finance character, no resemblance to any real person.

| Asset ID | Used in scenes | Prompt | Dimensions | Layers/variants | Acceptance |
|---|---|---|---|---|---|
| CH-MASTER | all | Character master sheet: Mara front, 3/4 left, 3/4 right, neutral | 4096x2048 | 1 sheet, transparent | face/outfit identical across views; approve before any pose |
| CH-P1 | A,B,E,F | Neutral, mouth closed + mouth open | 2048h | 2 variants | matches master, clean alpha |
| CH-P2 | A,E | Thinking, hand at chin, eyebrow up | 2048h | 2 mouth states | same |
| CH-P3 | A,E2 | Holding a rent bill (blank paper, no text) | 2048h | 2 mouth states | paper blank, so text added by Claude |
| CH-P4 | C,D | Pointing to viewer's right | 2048h | 2 mouth states | arm clean for overlay |
| CH-P5 | F | Relieved, closing laptop | 2048h | 2 mouth states | same |
| BG-ROOM | A,E,F | Cozy apartment room, table, window; flat; no text, no posters | 1920x1080 | background + separate table layer | no readable text/logos |
| PROP-HOMES | C | Row of 6 simple houses/apartment blocks, same style | 1920x400 | 6 separate PNGs | no text |
| PROP-CALENDAR | C | Blank 12-month calendar frame | 1500x900 | blank | no text (Claude adds) |
| PROP-BASKET | B | Shopping basket with generic icons (food, car, house) | 1000x1000 | basket + icons separate | no brands |

Order: 1) CH-MASTER, 2) test scene: CH-P1+CH-P3 on BG-ROOM for approval, 3) rest. Claude does QA at playback scale; a failed asset gets one correction round.
