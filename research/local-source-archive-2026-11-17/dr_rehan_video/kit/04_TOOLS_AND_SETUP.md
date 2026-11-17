# 04: Tools & setup (repo audit for THIS project)

I cloned and read all the repos the user collected. This is what each one is worth **for a talking-head medical explainer with a narrator layer, keyframe/mask motion and no AI video**.

## 1. Decision table

| Repo | Use? | What we take from it | Notes |
|---|---|---|---|
| **heygen-com/hyperframes** (Apache-2.0) | ✅ **Main engine** | HTML/GSAP compositing over `<video>`, deterministic render, `remove-background` (subject matte → text behind the doctor), `transcribe`, captions, talking-head card layouts (`overlays.md`), motion craft rules (`motion.md`), sound rules, review/lint | Node 22+. Win/Mac/Linux. **Turn telemetry off**: `npx hyperframes telemetry` (follow its prompt). Slow on long pieces, so build per chapter |
| **kajisho5/ffmpeg-skill** (MIT) | ✅ | probe, loudness (−14 LUFS), denoise, silence detection, fit/reframe, caption burn checks, `check`/`verify` QC | No cloud, no keys; tested on ffmpeg 6.1–9 |
| **openai/whisper** → use **faster-whisper** | ✅ | word-level timestamps for the doctor and narrator, `.srt` | Urdu needs `large-v3` (or at least `medium`). Never `*.en` models (they translate) |
| **cloudai-x/threejs-skills** (MIT) | ✅ | current three.js API for the light-3D heart/artery moments | knowledge only, no scripts; safest repo |
| **lemomo-ai/lemo-opuscar** (MIT) | 📖 knowledge | `DIRECTOR.md` §6–11 (sound layers, silences, J/L-cuts, rhythm, camera, failures, delivery checks); `styles/*/STYLE.md` for motion language (swiss-motion, dataviz, microscope, whiteboard, caption-news, white-model); `core/audio/sfx.py` idea for synthesised foley | Optional: render ONE signature animated sequence (e.g. the cold open) in a Lemo style and import it as a clip. Costs 30–60 min and many tokens. Needs ffmpeg 7+ |
| **kurbaitaev/ghost-editor** (MIT) | 📖 knowledge | face-safe caption rules (`face_track`), B-roll budget, cutout FX, sound-and-memes, style recipes (Kinetic doc, Whiteboard, Caption News, Swiss Grid, Data Story) | The tool itself is **Mac (Apple silicon) only** and built for vertical reels from raw takes. Read it; run it only if on a Mac |
| **iart-ai/motion-skills** (MIT) | 🟡 optional | `lower-thirds-skills`, `b-roll-skills`, `explainer-video-skills`, `kinetic-typography-skills` as extra craft references | It's an index of 19 packs plus marketing for iart.ai. Install only a pack you need: `npx skills add iart-ai/lower-thirds-skills` |
| **agricidaniel/claude-shorts** (MIT) | 🟡 optional | its segment-scoring rubric (hook, coherence, emotion, value density, payoff) to choose the Version B pieces | Renders with **Remotion**, which needs a paid company licence for larger companies (free for individuals and small teams; check remotion.dev/license). We build Version B in HyperFrames instead |
| **yt-dlp** (public domain) | 🟡 research only | download *reference* videos the user likes, to study pacing | Never put other creators' footage in our video |
| **blixvip/MotionClone** | ❌ | none | Windows-only, no project-wide licence, runs on the user's ChatGPT/Codex login, and copies others' animation |
| **zhuyansen/awesome-claude-video-skills** (CC0) | 📖 | the place to look if a new need appears (401 graded repos) | Its own test: Claude Code with no skill already makes a passable film. A skill earns its place by look, workflow or footage editing. That's why we chose HyperFrames + ffmpeg-skill |

## 2. Install (on the user's computer, inside Claude Code)

Requirements: **Node 22+**, **Python 3.11+**, **ffmpeg** (7+ if Lemo is used), **git**, **Chrome**.

```bash
# HyperFrames (Claude Code plugin + skills)
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
npx hyperframes skills update
npx hyperframes telemetry          # turn it off

# ffmpeg-skill
npx ffmpeg-skill

# three.js knowledge
npx skills add cloudai-x/threejs-skills

# Python tools
pip install faster-whisper mediapipe opencv-python numpy

# Knowledge-only repos (read, don't install)
git clone --depth 1 https://github.com/lemomo-ai/lemo-opuscar.git     ref/lemo-opuscar
git clone --depth 1 https://github.com/kurbaitaev/ghost-editor.git    ref/ghost-editor
```
Windows: everything above works in PowerShell. If a bash script is needed, use Git Bash or WSL.

## 3. Phase-0 setup check

Before Phase 1, run and report: `node -v`, `python --version`, `ffmpeg -version`, `npx hyperframes --version`, a 5-second test render (one text tween over the first 5 s of the doctor's video), and a 30-second Urdu transcription test. If anything fails, fix it or tell the user exactly what to install.
