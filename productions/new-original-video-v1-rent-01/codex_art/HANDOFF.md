# V1 Rent — initial original art test, pending independent review

The owner directed a fictional male renter; `CODEX_HANDOFF.md` and `STORYBOARD.md` still say Mara. Do not silently treat those as reconciled. Character design has not been independently approved and no production registry was changed. All files are in this staging folder.

| ID | Candidate | Intended use | Self-review and limitations |
|---|---|---|---|
| CH-MASTER | `candidates/v1_ch_master_front.png` | Identity anchor | Front only; not the handoff's 4096×2048 three-view sheet. Same pixels as neutral. Independent review pending. |
| CH-P1 | `candidates/v1_ch_p1_neutral_closed.png` | A/B/E/F, complete explaining sprite | Full figure and hands visible. Closed mouth only; open state absent. |
| CH-P3 | `candidates/v1_ch_p3_bill_closed.png` | A/E/E2, full sprite holding blank paper | Targeted edit of the master. Hands visibly touch paper; paper is baked into sprite, so cannot move or receive text behind the fingers separately. Closed mouth only. |
| BG-ROOM | `candidates/v1_bg_room.png` | A/E/F background | Opaque 1920×1080; table removed in targeted edit. Soft shading and interior detail exceed the flat handoff in places. |
| BG-TABLE | `candidates/v1_bg_room_table.png` | Separate foreground table | RGBA; independently generated from the room reference, visually similar rather than pixel-identical to original. |

Source images preserved in `originals/`. Built-in image generation produced character 1024×1536, upscaled to 1365×2048 with Lanczos; the 2048 pixels are not native generation detail. Room 1672×941 resized to 1920×1080. Candidate alpha ranges and SHA-256 hashes are in `qa/validation.json`; alpha channel/range checks do not certify edge quality. Character edges were inspected over the room at 1080p, without obvious dark halos at this size; inspect at other scales before production. Colors contain slight shading despite the flat-color direction. Scene examples place the 620px-high character around x=480 y=340; compositions are test staging, not a locked storyboard.

`qa/character_consistency.jpg` compares the poses in the room; `qa/pose_switch_preview.mp4` is a simple two-still hard-cut staging test, not a renderer integration, rig, lip-sync, timing or reference-motion validation. It is 1920×1080, 30 fps, 90 frames, 3 s; ffprobe counted frames and ffmpeg decoded fully. Original bill is blank, no source evidence is simulated.

Generation prompts: master was requested as an original fictional early-30s male renter with side-parted curls, olive overshirt, cream tee and jeans, full-body on transparent background, flat editorial ink; bill pose was a targeted same-identity edit adding a blank page held with both hands; room was a sparse cream apartment with sofa/window/plant, followed by a table-removal edit; table was generated separately using that room as reference. Outputs are candidates, not approved artwork.

Next: independent reviewer decides identity/style and whether the more detailed character fits. Then resolve 3/4 views, two mouth states, a separable bill/hand solution if needed, and only storyboard-required remaining assets. The target owner should update Mara references and approve the new identity before expansion. No review has been sent from this session; supply this folder to Claude. No claim is made about approval, registry import, source capture, narration accuracy or release readiness.
