# Visual forensics reviewer brief — video Uumnx2Fo6cE (Casual Finance, "The New American Housing Crisis Has Landed")

You are one of 7 parallel reviewers. You will LOOK at images and WRITE one JSON file. You change nothing else.

ROOT = /Users/ghilmankhan/YIOS-local-audits/2026-10-24-Uumnx2Fo6cE-deep-ct-scan
Your shard folder: ROOT/agents/shard_N (N given in your prompt). Write ONLY: ROOT/agents/shard_N/OUT_shard_N.json (and optional crops under ROOT/agents/shard_N/crops/). Do NOT touch the source MP4, any other file, the Git repo, or other shards. No installs, no network.

## What the video is
920.7 s, 1280x720, 24 fps CFR (frame i has PTS (i+1)/24 s). A whiteboard-style explainer: flat white canvas (#FCFCFC-ish), hand-drawn stick-figure presenter(s) with simple faces, doodle props (houses, buildings, dollar bills, documents), and third-party screenshots (news articles, charts, Yahoo-Finance-style dark-mode transcripts, filings) cut in as rectangles. Editing is mostly single-frame hard replacements (a composition changes on exactly one frame), with some motion intervals.

## What you are given (all under your shard folder + ROOT)
- machine_states.csv — your states (id, frames, times, entry/exit episode ids, child micro/motion episode ids, `asr_text_unverified` = automated local Whisper wording overlapping the state; NEVER treat it as verified speech).
- machine_episodes.csv — the 'episodes' (frame-change events) assigned to you, with measured class, kind, net-change metrics, and which boundary sheet + row shows them.
- Boundary sheets: ROOT/boundary_sheets/bsheet_NNN.jpg (listed per episode in machine_episodes.csv columns `sheet`,`sheet_row` (0-based row)). Each row = decoded native frames (downscaled to 256x144 tiles) for one episode: single-frame events show pre-4, pre-1, change, change+1/post+1, post+1, stable+8, and a red 'net diff' overlay; motion episodes (>=3 frames) show pre-1, 4 evenly spaced frames across the motion, stable, and overlay. Read the header of each row (EP id, class, frame range, seconds).
- State sheets: ROOT/agents/shard_N/state_sheets/ss_NN.jpg — 6 states per sheet (3x2), each a 640x360 view of that state's stable frame, labelled with state id, frame range and seconds. Sheet k holds states (k-1)*6 .. k*6-1 of your machine_states.csv in order.
- If you must read small on-screen text, you may extract native-resolution frames: `ffmpeg -v error -ss <seconds> -i "/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/The New American Housing Crisis Has Landed.mp4" -frames:v 1 -vf "crop=..." ROOT/agents/shard_N/crops/<name>.png` (frame i is at (i+1)/24 s; use a time slightly after the state start). Limit: at most 40 crops for your shard; prefer cropping to the text region. Then Read the png.

## What to produce (JSON file OUT_shard_N.json)
{
 "shard": N,
 "episodes": [ one object for EVERY episode listed in your machine_episodes.csv, in order ],
 "states":   [ one object for EVERY state in your machine_states.csv, in order ]
}

### episode object
{"ep": <int>, "verdict": "CONFIRMED" | "RECLASSIFIED" | "CODEC_ARTIFACT" | "UNVERIFIED",
 "type": one of FULL_REPLACE | PARTIAL_REPLACE | ADDITIVE_ENTRY | ELEMENT_EXIT | ELEMENT_SWAP | POSE_SWAP | EXPRESSION_CHANGE | TEXT_CHANGE | HIGHLIGHT_ADD | NUMBER_OR_LABEL_CHANGE | ZOOM_OR_SCALE | PAN_OR_SCROLL | CHARACTER_ANIMATION | OBJECT_MOTION | DRAW_ON_OR_REVEAL | WIPE_OR_FADE | PROGRESS_BAR_OR_COUNTER | CODEC_ARTIFACT | OTHER,
 "desc": "<=35 words: exactly what visibly changes between pre-1 and change/post frames, with WHERE (left/centre/right, top/bottom) and WHAT (object names). Specific, not generic.",
 "shot_boundary": "YES" | "NO" | "AMBIGUOUS"  (YES only if the whole scene/subject is replaced by an unrelated composition; this is an INFERRED label),
 "motion": null for single-frame events; for episodes with n>=3 frames an object {"path":"where/how things move","easing":"linear|ease-in|ease-out|ease-in-out|stepped|overshoot|UNKNOWN","duration_note":"..."},
 "confidence": "HIGH"|"MEDIUM"|"LOW"}
Rules: verdict CONFIRMED = the sheet shows a real visual change of the measured class; RECLASSIFIED = real change but the measured class/kind was wrong (say so in desc and set type to the truth); CODEC_ARTIFACT = no content change visible, diffuse noise at an I-frame; UNVERIFIED = you cannot tell from the frames. Never mark CONFIRMED for a change you cannot see. For micro events (kind MICRO_EVENT) the desc must name the tiny element that changed (e.g. 'a small red arrow appears at upper right').

### state object (every field required; plain strings; be specific to THIS state)
{"id":"S0123",
 "objects":"every visible object/figure/text block, each with approximate position as fractions of frame width/height (x 0-1 left→right, y 0-1 top→bottom) and relative scale",
 "background":"canvas colour or cut-in screenshot description",
 "illustration":"line quality, fill style, character face/pose/expression when a character is present (describe, do not name competitor characters); objects' drawing style",
 "typography":"font style class (serif/sans/handwritten/marker/mono/UI), relative size (% of frame height), colour, weight, alignment; 'none' if no text",
 "readable_text":"verbatim text you could actually read (quote it) — empty string if none",
 "unreadable_text":"text present but NOT confidently readable at the resolution you viewed (say what kind: article body, axis labels, table cells) — empty string if none",
 "hierarchy":"focal order: what the eye hits first/second and why (size, colour, contrast, position)",
 "camera_motion":"STATIC 2D | PAN | ZOOM | SCROLL | ... as observed from the episodes in/around this state; never invent lens/camera gear",
 "entry_exit":"how the state begins and ends (hard replace, additive, motion), citing episode ids",
 "story_function":"INFERRED role (e.g. establishing source, showing a number, comparison payoff, CTA) tied to the ASR wording but labelled as inference",
 "evidence":"which parts are OBSERVED vs INFERRED",
 "confidence":"HIGH|MEDIUM|LOW",
 "continuity":"which earlier/later states reuse the same assets/layout (cite state ids if you recognise them, else describe the asset)",
 "recon":"ORIGINAL production instructions (2-4 sentences): how an editor would build an equivalent composition with NEW original assets — layer order, placement, scale, timing, entry behaviour. Do not copy the source's characters/artwork/screenshots/logos/text.",
 "prompt":"ONE self-contained original image-generation prompt (30-70 words) for an equivalent composition with original art: flat hand-drawn whiteboard style, specific objects/positions/colours from THIS state. It must NOT contain: the names Dave/Casual Finance/Redfin/Yahoo/Lennar/Census/any brand or real person's name, logos, or quoted source text.",
 "family":"one of F1 character-only | F2 character+prop | F3 object/icon cluster | F4 full-bleed screenshot/document | F5 screenshot+character | F6 chart/graph | F7 text card | F8 dark-UI capture | F9 full-bleed drawn scene | F10 title/end card | F11 other composite (if none fit use 'F12:<short label>')"}

## Standards
- Truth labels: only describe what you can see. Small text you cannot read goes in unreadable_text; do not guess numbers. If the whole state is a screenshot of dense text, say so; quote only headline-size text you can read.
- Be unique: neighbouring states often share a layout, so name what is DIFFERENT (counts of objects, positions, which highlight is yellow, which pose) rather than copying sentences. Do not pad. A state that is 1-3 frames long (a flicker/animation frame) may be briefly described but must still identify the visible content and why it is that short (e.g. 'animation frame of ...').
- Speed matters but accuracy first: look at every boundary sheet and every state sheet in your shard. Do not skip.
- Do not use the words 'Dave', 'Casual Finance' or any third-party brand inside `prompt` or `recon`.
- Keep a running self-check: len(episodes)==rows in machine_episodes.csv, len(states)==rows in machine_states.csv, ids match exactly. Write the JSON in 3-4 chunks if needed (build a Python dict in several script runs saved to partial files, then merge) — valid JSON is mandatory; verify with `python3 -c "import json;json.load(open(...))"` and print the counts.
- When finished reply with ONLY: shard number, counts of episodes/states, number of CODEC_ARTIFACT / RECLASSIFIED / UNVERIFIED verdicts, and any structural problems you noticed (e.g. two states that look identical, a state sheet tile that was blank). Do not paste the JSON in your reply.
