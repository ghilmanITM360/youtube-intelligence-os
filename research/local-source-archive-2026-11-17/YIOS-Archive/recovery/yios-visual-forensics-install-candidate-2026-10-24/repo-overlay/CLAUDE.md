# CLAUDE.md

Project rules live in `AGENTS.md`; read it first. This file only adds pointers.

## Video Visual Forensics / CT Scan — project convention

When a task asks for video forensic analysis, visual CT scan, deeper visual analysis, visual DNA, animation/editing reconstruction, scene-by-scene or frame-by-frame breakdown, invoke the project skill at `.claude/skills/visual-ct-scan/SKILL.md` and follow the specified mode and coverage gates. This skill is the project's visual methodology reference. Use its dedicated references and templates as needed; don't substitute simple 1fps contact sheets for a frame-accurate event audit, and never confuse visual, script, audio and audiovisual completion. Keep source MP4s and canonical Finance JSONL/workbooks untouched unless a separate authorized task explicitly changes their scope. Reuse the existing YIOS progress ledger; source Video ID/hash/timestamps and explicitly label facts, measurements, inferences and unavailable data. Never manufacture retention, CTR, eye-tracking, intent, AI-provenance, animation curves or historical visuals. During Finance writer handoff do not stage/commit/push unrelated visual-forensics work without a confirmed safe ownership boundary.

Mode routing: "CT scan" → `CT_SCAN`; "deep(er) visual analysis" → `DEEP`; "visual forensic(s)" → `DEEP` (ask only if the source is unknown); "recreate/reconstruct/motion reconstruction" adds `RECONSTRUCTION`; "channel visual DNA" adds `CHANNEL_DNA`. Full table in the skill's SKILL.md.
