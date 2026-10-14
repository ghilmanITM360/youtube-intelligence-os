# Why Raising Rates Costs the Fed Money — static artwork handoff

All seven scene groups and36 meaningful static states are authored. The147-word narration at editable_sources/original/APPROVED_NARRATION.txt is unchanged.53seconds and five proposed cuts remain provisional; align to the owner's future audio before any animation. This package contains no audio, video, temporal evaluator or rig.

## Open and assemble

Start with SCENE_OVERVIEW.png, then SCENE_01.png through SCENE_07.png and assets/exports/SCENE_XX_CONTACT.png. The latter show every state, including policy evidence, paused Treasury route and the later historical comparison. Individual editable assets are under assets/characters,supporting_characters,props,environments,diagrams,evidence_overlays. Each asset has a transparent PNG derivative except documentary rectangles and the white canvas. Native composition SVGs and all36 state SVGs live in assets/scene_compositions.

ASSET_REGISTER.csv is the actual inventory; ASSET_REQUIREMENTS.csv is the preserved earlier estimate. FULL_STORYBOARD.csv supersedes the earlier18-state plan for production. A repeated narration phrase in sub-states belongs to the same approved parent phrase; do not repeat those words in the audio. The increase to36 states exposes semantic builds, not36 authored scenes or a cut quota. Source Shorts42.3–79.5states/min include caption changes and are not an optimal-motion prescription.

SCENE_ASSET_MAP.csv defines each visible layer, z order, placement, uniform scale and local pivot. FULL_STORYBOARD lists enters/exits/switches/repositions/holds. These are future editorial suggestions, not implemented animation. Use simple POSITION_XY,SCALE,ROTATE,OPACITY,POSE_SWITCH,EXPRESSION_SWITCH,TRACE_REVEAL,SOURCE_HIGHLIGHT and additive reveal. A full layout replacement marked without a cut requires a designed transition; its continuity has not been playback-tested.

## Attachments and editable expressions

Asset-register editable_subparts_json gives actual child IDs for legs,torso,arms,head,hair,eyes,brows,mouth and held paper/thumb. Optional FACE_* overlays align to host-local100,65 after original features are hidden. Eyes/brows/mouth can be edited independently. Near-hand/pivot coordinates are in anchor_pivot_json. Host body/head proportions are invariant across the eight full-body pose/expression assemblies.

Bill paper stays behind its thumb, together in the host parent. Scene07 shield and wrench use separate foreground HAND_GRIP layers. World anchor=placement+uniform_scale×local_anchor; static hand/prop distances are under2.5source pixels. Animate attached parents together and retest contact if either object rotates. Do not claim this static check establishes continuous physics.

## Financial and documentary constraints

0.25percentage point=0.0025 as an incremental rate; about3T×0.0025=about7.5B/year only at constant balances. IORB3.90% is distinct from the target range3.75–4.00%. Wednesday7Oct2026 reserves3,022,066million must not be replaced by the weekly average. H41 negative233,587million is the cumulative deferred balance, not a negative cash remittance or a loss caused only by this hike. Future earnings must cover the balance before normal Treasury remittances resume.2021 preliminary remittance107.4B is not net income107.8B. Preserve the final CAN qualifier.

Eight documentary SVG wrappers use exact pixels from five financial insert topics(A policy,B IORB,C reserves,C deferred,E2021). FRED is a preserved corroborating alternative, not an additional independent source.24 accepted crops include context/alternatives; the24 are not24 video inserts. ARTICLE_SOURCE_REGISTER and CROP_MANIFEST retain URL,date,units,source hashes and crop coordinates. Original screenshot/PDF pixels remain unchanged, highlights are separate paths. Concise official factual evidence is attributed; no government endorsement or blanket rights claim for logos/site artwork is made. Creator reference frames and private comparisons are intentionally absent from the Git production package.

## Portability and reproduction

SVGs and existing PNGs need no local font or dependency to use. Display lettering is original paths with semantic data-text; edit the text in tools/build_assets.py and rebuild the affected scene. It is not an installed handwriting font. Documentary type remains original pixels. Contact-sheet UI labels use system sans-serif; exact contact-sheet raster appearance may vary.

For optional rebuilds use Python3.12+ with requirements-assets.txt and Node22+ with package-lock.json. Commands from this directory:

```sh
python3 -m pip install -r requirements-assets.txt
npm ci --ignore-scripts
python3 tools/build_assets.py --scene 3
node tools/export_assets.cjs 3
python3 tools/build_assets.py --refresh
python3 tools/verify_assets.py --complete
node tools/verify_exports.cjs
node tools/build_review.cjs
```

Only rebuild a changed scene. A source edit resets that scene's visual-review marker. Do not run record_review.py until the new files are actually inspected. Rebuild does not perform video rendering. Same-runtime SVG→PNG equality was checked; pixel identity between different libvips/SVG renderer versions is not promised. No proprietary macOS font is distributed.

Current static native/320/160 review findings are in ASSET_QA.md. Main quantities/relationships survive reduction; fine attribution, documentary context and expression detail are limited at160px. Owner approval of the complete artwork, subsequent audio alignment and a separately authorized animation phase remain the next gates.
