# Codex integration status (2026-11-21)
**Not sent.** From this session I have no Codex tool or CLI (`which codex` empty), and the only send mechanism available (`/send-to-project`, which posts to a Claude Project, not to Codex) works only when the owner runs that command. So the handoff has not reached Codex.

To send: give Codex the folder `productions/new-original-video-v1-rent-01/` and paste this brief:

> Read, in order: CHANNEL_VISUAL_AUDIT/CHANNEL_001/22_LONGFORM_VISUAL_DNA.md; V1_RENT_STYLE_FIDELITY_AUDIT.md sections 3 and 5 and the images in style_audit/ (reference evidence: use for proportions only, never trace or copy); then CODEX_HANDOFF_V2_LONGFORM_RIG.md. Produce the V2 rig exactly as specified (3 bodies, 5 heads, rig_anchors.json) in codex_art/v2_rig/ with qa/validation.json. Do not touch v1_assets/approved/. Do not start from the old detailed-clothing spec.

Integration when files arrive: copy to `v1r4_assets/rig/` (the renderer prefers it over `v1r4_assets/provisional/`), re-render with `tools/v1r4_render.py` and `tools/v1r5_seg2.py`, check the handoff acceptance list (head 0.31-0.38 of figure height, line 2-3%, anchors within 6 px). Placeholder art is not required to be approved for publication; baselines kept: R3 `out/` (sha a40bbccc...), R4 v1/v2/v3 in `out_r4/`.
