# V12 tool and library usage

**What actually rendered V12:** the existing Python + Cairo frame renderer (`tools/v12.py` + `tools/v12_shots.py`), PIL/numpy for rig building, and ffmpeg for encoding, mixing, caption overlay and QA. The renderer was **not migrated**, as the brief asks. A 49-second full render makes iteration cheap.

**None of the 16 listed repositories was installed, cloned into the project or run.** They were reviewed from their README/docs (`research/LIBRARY_REVIEW.md`). The table below separates what was *used as an idea* from what was merely *read*.

| Repo | Status | What V12 took from it (re-implemented in Cairo) |
|---|---|---|
| mromidev/claude-animated-shorts | ideas applied | No dead holds: slow creep on held shots (F1/G1 reset; that frame was the freezedetect hit at 21.9 s). Foreground element passing near the lens (A1 near-cloud wipe). Smooth eased camera glides. |
| lemomo-ai/lemo-opuscar | ideas applied | One world-to-screen function for overlays (`cam.proj` places figure, aircraft and drop line in A1). Lens placed in screen space from the tips' projected position. Poses blend through easing, never an `if` switch (lift curve). Its docs are CC BY-NC; nothing copied. |
| alexgreensh/anidoodle | idea applied | Marks are *drawn on*, not faded: `grow_arrow` (trim-path arrows), streamline trim reveal, graph axes and curve drawn on. |
| storytold/effectcraft (+ getartcraft page) | idea applied | Trim-path with moving offset for flow: travelling markers along streamlines. |
| hi-nikola/hand-drawn-explainer-video-nikola | idea applied | Accumulating "semantic islands": the equal-time trail keeps every earlier mark while new ones arrive. |
| openai/whisper | **not used** | Not installed. Phrase timing comes from the existing `audio/phrases.json` alignment, unchanged since V9. Word-level timing would need Whisper installed with the owner's agreement. |
| kajisho5/ffmpeg-skill | checklist only | Deliverable checks done with plain ffmpeg (decode, freezedetect, EBU R128). |
| heygen-com/hyperframes | principle only | Its "every frame a pure function of t" contract is already how `draw(c, t)` works. A HyperFrames skill is available locally but was not used. |
| AgriciDaniel/claude-shorts | read | Clean, minimal caption style for the optional caption export. |
| iart-ai/motion-skills | read | Thin index. |
| kurbaitaev/ghost-editor, zenstory-ai/video-recap-skills | read | Live-action tools, not relevant. |
| cloudai-x/threejs-skills | read | No three.js in this production. 2.5D comes from the Cairo pinhole camera. |
| zhuyansen/awesome-claude-video-skills | read | Discovery list only. |
| blixvip/MotionClone | **unreachable** | GitHub returns 404 for the repo and the user (2026-11-25). |

**HumanCraft guides and local xkcd What If analysis:** read for principles (`research/VISUAL_REFERENCE_NOTES.md`). No competitor art or composition was traced.
