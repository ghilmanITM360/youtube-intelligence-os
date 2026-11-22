# doc_scene spec (authentic document scene)
`doc_scene.document_item(spec, t0, base_dir)` -> `dyn` item for any beat in the existing v1r4_render engine. `validate_spec` raises `SpecError` with every problem listed. Example: `productions/doc-animation-proof-01/doc_spec.json`; tests: `CHANNEL_VISUAL_AUDIT/CHANNEL_001/CLOSURE2/tests/`.

```
source: {file, sha256, url, publisher, title, published, retrieved, rights, claim_ids[]}   # all required; sha256 is verified against the file
viewport: {x, y, w, h}            # clipping frame on the 1920x1080 canvas (leave room for the 2-line source tag below)
camera: [{t, crop:[x,y,w,h]}...]  # crop in SOURCE pixels, same aspect as viewport (else SpecError); smoothstep between keys; hold = repeat key
timing: {legible_s}               # first moment the target passage is readable; marks may not start earlier
duration_s
required_context: [{rect, why, annotation?}]   # rects that must stay inside the crop while that mark is visible
annotations: [{id, kind: highlight|underline|ellipse|arrow, mode: instant|progressive,
               rect:[x,y,w,h] (document px) | from,to (arrow), start_s, complete_s, exit_s?, passage, claim_id, stroke_doc_px?}]
```
Rules: instant => complete_s == start_s; progressive => complete_s > start_s (highlight sweeps left-to-right, underline/ellipse/arrow draw along their path); persistence = default until exit_s or end; geometry is document-local, so every zoom/pan transforms image and marks together. Choose onset/complete from the verified narration clause (observed modes: mark on the number, or mark at the clause start; no universal delay). `event_table(spec)` lists onset/complete/exit frames at 24 fps for QA. Source tag (publisher, title, published, retrieved) is drawn under the viewport at 38 px, wrapped. Not supported: rotation, perspective, text-edit of the source, automatic passage location (coordinates come from the capture).
