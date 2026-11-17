## 9. Original-production specification (transfer, not copy)
**v0.3 hard constraints (from RT1 failure, reconstruction/RT1/RT_EVALUATION.md):**
- Event budget: ≈0.33–0.5 visual events per second (20–30/min; Shorts may reach ~35/min). A 24 s piece has ~8–12 events, not 20+. Median hold 1.5–2.4 s; at most ~25 % of holds under 1 s.
- Detail contrast: characters minimal; objects/machines/maps drawn with clearly more internal detail (hatching, parts, labels) than the narrator (§2).
- Long-form: question card → cold-open premise/gag → series title card (≈2 s) at a variable 6–31 s → step canvases → end card held exactly 10 s.
- Shorts: no title/end card; landscape panels may sit in the upper half of 9:16 with empty space below (held-out Ny9m2l6h478).
Use the mechanics above with a NEW visual identity: different character design (e.g., a rounded pebble-shaped narrator with dot eyes, not a stick figure), different accent colour (e.g., teal `#1F8A8A` instead of red), different lettering (a rounded monoline sans), original topics and scripts.
1. Script → beat list: question, bound, 3–6 escalation steps, deadpan aside per 20–40 s, payoff.
2. For each beat define: canvas (light/dark/colour field), persistent anchor (scale, timer banner, map band), one new object, ≤1 label, ≤1 accent mark.
3. Timing defaults (from measured source ranges, to be validated by test): hold 1.5–2.5 s median; pops on the narration word that names the element; write-ons 6–10 frames at 24 fps; dissolves 6 frames; panel slides 8 frames.
4. Shorts: cut the long script into 45–120 s excerpts and re-lay each beat for 9:16 (stack panels vertically, keep the anchor on screen).
5. Image prompt template: "<aspect>, <canvas>, hand-drawn monoline ink illustration in <original style>, subject: <object> at <position>, persistent anchor: <anchor>, label '<text>' near <object>, accent colour only on <mark>, generous empty space, no shading unless lighting scene, no extra text".
6. Animation prompt template: "<object> appears in one frame at t=<word onset>; everything else static; <write-on> strokes left-to-right over 8 frames; camera locked except <slide/scroll> over 8 frames with slight motion blur".

