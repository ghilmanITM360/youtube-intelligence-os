# YIOS Visual Forensics Intelligence Standard v1.0

The project's reusable methodology for video visual forensics. It covers:
- CT-scan, deep and frame-by-frame review;
- motion and animation reconstruction;
- channel visual DNA.

It is a method, not evidence. It does not change any video's status.

- **Skill (loaded automatically by trigger words):** [`.claude/skills/visual-ct-scan/SKILL.md`](../../.claude/skills/visual-ct-scan/SKILL.md). It contains:
  - 14 reference modules in `references/`;
  - 7 templates in `templates/`;
  - mode routing and the YIOS status bridge.
- **Four owner-supplied master prompts, byte-identical:** [`source-prompts/`](source-prompts/). Their SHA-256 values are in [`SOURCE_PROMPT_MANIFEST.json`](SOURCE_PROMPT_MANIFEST.json).
  - The owner's chat-typed "WORLD-CLASS VISUAL FORENSIC ANALYSIS" prompt is **not** archived as a byte-verified file. Its requirements are mapped in reference 14.
- **[Invocation examples](SKILL_INVOCATION_EXAMPLES.md):** inventory, 1 fps overview, deep review, Short CT scan, long-form adaptive CT scan, reconstruction and channel comparison.
- **[Install report](VISUAL_FORENSICS_STANDARD_INSTALL_REPORT.md):** hashes, routing, smoke test and preservation checks.
- **Validator (read-only):** `python3 -I research/visual-forensics/validate_install.py .`

Status authority stays with the per-Video-ID visual ledger of the active run and its receipts. Source MP4s, derived frames and competitor media are never committed.
