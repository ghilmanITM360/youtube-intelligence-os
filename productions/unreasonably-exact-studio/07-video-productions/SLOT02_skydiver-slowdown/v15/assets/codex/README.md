# V9 illustrated asset delivery

73 image-generated artwork layers, made with the built-in image_gen tool in 13 calls (including replacements and one rejected rear sheet). These are generated illustrations, not human-authored drawings. Procedural work here only splits, registers, resizes and assembles the generated pixels; it does not draw replacement character or equipment art.

## Contents

- CH-01 side: 15 PNG layers, existing640×400 origin and pivots.
- CH-02 three_quarter:15 layers, existing640×400 origin and pivots.
- CH-03 back:15 layers, existing640×400 origin and pivots.
- CH-04 closeup:7 layers including separate eyes/lids/brows and neutral/open mouths.
- CH-05 wrist:4 layers, new640×400 rig; dial centre350,198 in attachment.json.
- CH-06 pov:2 gloves, existing360×240 origin, 1440×960 PNGs.
- IN-01 instrument:4 layers, existing280×207 origin,1120×828 PNGs, cap/needle pivot140,139; needle points up.
- AC-01 aircraft_side.png and aircraft_propeller.png, matching640×400 origin, propeller centre602,220.
- EN-01 clouds:6 cumulus and3 wisps, each640×400 origin.

Each640×400 part is exported2560×1600. Instrument and POV retain their actual smaller rig canvases instead of silently changing their origins. Sizes are4× delivery exports resampled from the generated originals; they are not claimed to be native4× generation detail.

Every character/insert directory has a proposed rig.json and layered.svg. The SVG embeds one PNG per named group; it is a layered raster carrier, not vector-traced editable Bézier artwork. No PSD supplied.

## Integration handoff to Claude

The canonical V9 rigs, renderer, film, terrain, forces and audio have NOT been overwritten. Proposed PNG references are in this package's rig.json files. Copy the selected rig into rigs/<view>/rig.json when integrating. Preserve original rigs as backups.

PNG loader replacement for tools/rig_renderer.py drawing(file), keeping its existing2× internal draw scale:

```python
if str(file).lower().endswith('.png'):
    im = Image.open(ROOT/file).convert('RGBA')
    im = im.resize((im.width//2, im.height//2), Image.Resampling.LANCZOS)
else:
    im = Image.open(io.BytesIO(cairosvg.svg2png(url=str(ROOT/file), scale=2))).convert('RGBA')
x, y, r, b = im.getchannel('A').getbbox()
```

Retain the existing crop/surface return and draw() function. Using alpha.getbbox() is necessary because generated PNGs may contain nonzero RGB under zero alpha. Test renderer in ../../tools/check_codex_assets.py demonstrates this loader without modifying the live renderer.

Instrument now has housing/dial_face/needle/cap rather than plate/pointer. Change the animation channel from pointer to needle. Place wrist instrument by aligning cap140,139 to wrist dial_center350,198 with an appropriate uniform scale (suggest0.35). The wrist rig is a new view; do not replace the established standalone instrument framing with the whole wrist accidentally.

Closeup: neutral mouth is active; mouth_open is an alternate file, not an always-visible extra rig layer. Eyes support ±6px translation; lids are a blink replacement as before. Layered SVG hides lids by default.

After integration rerun tools/v9.py --check --render and tools/boards_v9.py. This delivery did not rerender the V9 film because the requested division of work assigns animation/editing to Claude.

## Verification and limits

All73 PNGs were opened and checked for RGBA mode, declared dimensions, alpha0 background and substantial opaque artwork. Rest and simultaneous min/max FK-limit montages were rendered using the proposed rigs for side/back/three_quarter, and open/blink/+6px eye movement for closeup; previews were visually inspected. Obvious clipping/stray fragments from grid splitting and rear forearm/hand registration errors were corrected. Registration is based on alpha connected components and anatomical endpoint transforms, not tracing the procedural SVG drawings. Original SVGs supply only pivots and reference bounds.

The generated style has slight tonal variation and line-weight variation; exact hexadecimal colour uniformity is not certified. Main views use separate generated heads, so identity consistency is costume/proportion based, not a claim of pixel-identical facial construction. Limb joint caps can remain visible as seams. The requested exact8–12px overlap at every point through every independent joint combination has not been certified; rest and combined extremes are supplied for the animator's final seam review. The main purpose is to replace procedural artwork with actual generated illustration pixels, with candid provenance.

sources/ preserves selected raw generation output. manifest.json records per-layer source name and registration metadata; manifest.csv records hashes. PROMPTS.md records the normalized prompt set and generation IDs. Source pose/orientation adjustments, separation, resampling and PNG assembly are reproducible with tools/package_codex_assets.py in the V9 project. No image API key or paid external API workflow was used.
