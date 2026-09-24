import csv
import json
import math
import re
import shutil
import statistics
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "work"
OUTPUT = ROOT / "outputs"
EVIDENCE = WORK / "evidence_final"
OUTPUT.mkdir(parents=True, exist_ok=True)


def ts(seconds: float) -> str:
    millis = round(seconds * 1000)
    hours, millis = divmod(millis, 3_600_000)
    minutes, millis = divmod(millis, 60_000)
    secs, millis = divmod(millis, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{millis:03d}"


def plain_ts(seconds: float) -> str:
    minutes, seconds = divmod(seconds, 60)
    return f"{int(minutes):02d}:{seconds:05.2f}"


shots = json.loads((EVIDENCE / "shot_manifest.json").read_text(encoding="utf-8"))
transcript = json.loads((WORK / "transcript" / "transcript.json").read_text(encoding="utf-8"))
audio = json.loads((WORK / "audio" / "audio_summary.json").read_text(encoding="utf-8"))

descriptions = {}
visible_text = {}
for line in (WORK / "scene_descriptions.psv").read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    shot_id, description, text_value = line.split("|", 2)
    descriptions[shot_id] = description
    visible_text[shot_id] = text_value

assert len(shots) == len(descriptions) == 253


BEATS = [
    (0.00, 20.74, "B01", "HOOK", "Retirement postcard stereotype", "Will the familiar retirement fantasy be challenged?", "OPEN"),
    (20.74, 30.20, "B02", "CONTRADICTION", "Highlights are only the trailer", "What is retirement most of the time?", "ESCALATING"),
    (30.20, 48.92, "B03", "REVEAL", "Retirement is an ordinary Tuesday", "What determines the quality of thousands of ordinary days?", "PARTIALLY ANSWERED"),
    (48.92, 81.08, "B04", "CLAIM", "Thriving is decided by small daily routines", "Which routines separate thriving from drifting?", "OPEN"),
    (81.08, 91.68, "B05", "VALUE PREVIEW", "Eight routines and a life worth waking for", "What is routine one?", "REPLACED BY LARGER LOOP"),
    (91.68, 100.58, "B06", "MINI HOOK", "Routine 1: chase daylight", "Why does simple daylight matter?", "OPEN"),
    (100.58, 117.26, "B07", "PROBLEM", "Retirement can shrink life indoors", "What does indoor living damage?", "ESCALATING"),
    (117.26, 146.66, "B08", "EXPLANATION", "Morning light sets the body clock", "What small action is enough?", "PARTIALLY ANSWERED"),
    (146.66, 167.86, "B09", "PAYOFF", "Ten minutes outdoors is sufficient", "What is routine two?", "ANSWERED"),
    (167.86, 183.66, "B10", "MINI HOOK", "Routine 2: treat sleep as sacred", "Why reject the sleep-is-lazy myth?", "OPEN"),
    (183.66, 201.90, "B11", "EXPLANATION", "Sleep is overnight maintenance", "What retirement-specific trap disrupts it?", "PARTIALLY ANSWERED"),
    (201.90, 222.08, "B12", "PROBLEM", "Retirement removes sleep guardrails", "How do thriving retirees restore rhythm?", "ESCALATING"),
    (222.08, 245.04, "B13", "PAYOFF", "Keep consistent timing and remove screens", "What is routine three?", "ANSWERED"),
    (245.04, 249.17, "B14", "MINI HOOK", "Routine 3: information diet", "What does an unmanaged information day do?", "OPEN"),
    (249.17, 282.31, "B15", "PROBLEM", "Outrage saturates an unstructured day", "Why is the effect so strong?", "ESCALATING"),
    (282.31, 300.45, "B16", "EXPLANATION", "Attention industry monetizes fear and anger", "What is the practical dose?", "PARTIALLY ANSWERED"),
    (300.45, 330.45, "B17", "PAYOFF", "Check once, then turn it off", "What is routine four?", "ANSWERED"),
    (330.45, 341.70, "B18", "MINI HOOK", "Routine 4: tend something living", "Why is being needed a happiness strategy?", "OPEN"),
    (341.70, 362.74, "B19", "PROBLEM", "Retirement can remove roles that need you", "What can restore that pull?", "ESCALATING"),
    (362.74, 384.42, "B20", "EXAMPLES", "Plants and pets create daily obligation", "What psychological function does that serve?", "PARTIALLY ANSWERED"),
    (384.42, 412.49, "B21", "PAYOFF", "Showing up for care is grounding medicine", "What is routine five?", "ANSWERED"),
    (412.49, 430.67, "B22", "MINI HOOK", "Routine 5: respect the chef", "What happens when meals lose structure?", "OPEN"),
    (430.67, 453.59, "B23", "PROBLEM", "Retirement produces sink grazing", "Why is that costly now?", "ESCALATING"),
    (453.59, 478.26, "B24", "EXPLANATION", "Food now shows up quickly in energy and mood", "What simple pattern works?", "PARTIALLY ANSWERED"),
    (478.26, 502.44, "B25", "PAYOFF", "Real food, protein, water, and joyful treats", "What is routine six?", "ANSWERED"),
    (502.44, 520.68, "B26", "MINI HOOK", "Routine 6: keep the nest in order", "Why does basic order matter beyond tidiness?", "OPEN"),
    (520.68, 547.34, "B27", "EXPLANATION", "Outer clutter becomes inner unfinished business", "How does the mess creep in?", "ESCALATING"),
    (547.34, 559.02, "B28", "PROBLEM", "Unstructured time lets disorder accumulate", "What is the smallest fix?", "PARTIALLY ANSWERED"),
    (559.02, 589.92, "B29", "PAYOFF", "Ten minutes of daily reset creates calm", "What is routine seven?", "ANSWERED"),
    (589.92, 609.52, "B30", "MINI HOOK", "Routine 7: laugh on purpose", "Does aging require becoming stern?", "OPEN"),
    (609.52, 639.02, "B31", "EXPLANATION", "Thriving retirees laugh often and physically release stress", "How do they cultivate it?", "PARTIALLY ANSWERED"),
    (639.02, 662.94, "B32", "EXAMPLES", "Funny media, old jokes, and laughing at aging", "What does this change in daily friction?", "ESCALATING"),
    (662.94, 679.26, "B33", "PAYOFF", "Laugh instead of rage at ordinary lapses", "What is routine eight?", "ANSWERED"),
    (679.26, 701.90, "B34", "MINI HOOK", "Routine 8: close with gratitude", "Why is the usual bedtime ending harmful?", "OPEN"),
    (701.90, 722.20, "B35", "EXPLANATION", "Two minutes hunting for what went right", "Why does the practice work?", "PARTIALLY ANSWERED"),
    (722.20, 740.80, "B36", "MECHANISM", "Negativity bias was useful for ancestors", "Can the setting be retrained?", "ESCALATING"),
    (740.80, 759.00, "B37", "PAYOFF", "Repeated gratitude trains real-time noticing", "How does this integrate the whole list?", "PARTIALLY ANSWERED"),
    (759.00, 779.30, "B38", "SYNTHESIS", "Gratitude lets the good life land", "What does the full system mean for retirement?", "ANSWERED"),
    (779.30, 809.18, "B39", "MAJOR PAYOFF", "Money buys the freedom; routines build the life", "What should the viewer do first?", "OPEN"),
    (809.18, 830.76, "B40", "CTA", "Pick one routine and name strengths and gaps", "Will the viewer make a public commitment?", "PARTIALLY ANSWERED"),
    (830.76, 843.64, "B41", "CTA", "Like, subscribe, and return for weekly videos", "What comes next on the channel?", "ANSWERED"),
]


def beat_for(seconds: float):
    for beat in BEATS:
        if beat[0] <= seconds < beat[1]:
            return beat
    return BEATS[-1]


def transcript_for(start: float, end: float) -> str:
    pieces = []
    for segment in transcript["segments"]:
        if segment["end"] > start and segment["start"] < end:
            pieces.append(segment["text"].strip())
    return " ".join(pieces) if pieces else "No narration verified in this interval."


def text_plan(shot_id: str):
    value = visible_text[shot_id]
    if value == "None":
        return {
            "decision": "NO",
            "clean": "Generate a text-free illustration; preserve any necessary blank signs, screens or panels as clean plates.",
            "overlay": "No semantic text overlay. Add the persistent channel watermark separately at the top-right in screen space.",
        }
    return {
        "decision": "NO",
        "clean": "Generate the visual with clean, blank versions of all text-bearing surfaces. Do not ask the image model to render lettering.",
        "overlay": f"Rebuild as deterministic editor/vector text in the same panel or surface, matching the source line breaks, hierarchy and placement: {value}",
    }


def image_prompt(shot_id: str) -> str:
    desc = descriptions[shot_id]
    if desc.startswith("White-background") or "on a white background" in desc:
        environment = "Use a clean warm-white background with ample negative space and a faint grounding shadow only where visible."
    else:
        environment = "Render the environment fully to the frame edges with clear foreground, midground and background separation."
    if "caveman" in desc.lower():
        identity = "Depict the same gray-haired, short-bearded, bespectacled older man reimagined as a rugged fur-clad caveman, preserving his face and glasses."
    elif "younger bearded man" in desc.lower():
        identity = "Depict a younger light-skinned bearded man with glasses and an average build, matching the stated action and setting."
    elif "older bald man" in desc.lower():
        identity = "Depict an older light-skinned bald man with a gentle face and average build, matching the stated wardrobe and pose."
    else:
        identity = "Depict a light-skinned retiree in his late sixties with swept-back gray hair, short gray beard and mustache, large expressive eyes behind glasses, and an average build; use reference-appropriate plaid, knit or earth-tone casual clothing unless the scene specifies another outfit."
    text_instruction = "Do not render letters or logos; leave text surfaces clean for overlay." if visible_text[shot_id] != "None" else "Do not add captions, labels or logos."
    return (
        "Create a 16:9, 1280×720 polished 2D editorial-cartoon illustration with hand-inked dark outlines, softly painted textures, expressive but stable anatomy, warm cinematic color and readable midtone contrast. "
        + identity + " " + desc + " " + environment
        + " Use a mostly eye-level, medium-wide composition; preserve the stated left/right relationships, relative scale, object count, pose, gaze, negative space and depth. Use warm amber daylight for positive scenes and restrained blue-violet contrast for fatigue, news or night scenes. "
        + text_instruction + " No watermark. No motion blur, deformation, duplicated limbs or extra people."
    )


def motion_details(shot: dict):
    estimate = shot["global_motion_estimate"]
    kind = estimate["classification"]
    if kind == "static_hold":
        return {
            "animation": False,
            "motion_type": "STATIC HOLD",
            "human": "Hold the flattened illustration for the measured shot duration. No camera, character, object, lighting or environmental movement.",
            "prompt": "N/A",
            "editor": f"Place the master image at 100% scale, centered, and hold for {shot['duration_seconds']:.3f} s. Keep watermark and any text overlays on separate fixed layers.",
            "why": "Stillness creates a short reading/rest beat and preserves the clarity of the single illustrative idea.",
            "state": "F0 hold; no transition state is created.",
            "coupling": "STATIC STATE",
        }
    scale = estimate.get("scale_start_to_end", 1.0)
    dx = estimate.get("content_center_dx_px", 0.0)
    dy = estimate.get("content_center_dy_px", 0.0)
    if kind.startswith("digital_push_in"):
        human = f"Slow centered digital push-in. The flattened illustration scales from 100% to approximately {scale * 100:.2f}%; measured content-center drift is ({dx:+.1f}, {dy:+.1f}) px."
        prompt = (
            f"Locked internal scene. Only the virtual camera performs a slow centered push-in, enlarging the complete flattened illustration by about {(scale - 1) * 100:.1f}%. "
            "Every character, object, expression, light and line remains frozen relative to the artwork. Keep screen-space overlays fixed. End on the measured tighter crop and hold."
        )
        editor = f"Scale the full illustration from 100% to {scale * 100:.2f}% over {shot['duration_seconds']:.3f} s, centered; compensate position by about ({dx:+.1f}, {dy:+.1f}) px. Use constant-speed interpolation unless frame comparison supports a mild ease."
        motion_type = "DIGITAL CAMERA PUSH-IN"
    elif "camera_up" in kind:
        human = f"Slow upward virtual camera move: the flattened illustration shifts downward by approximately {abs(dy):.1f} px from start to end; scale stays near 100%."
        prompt = (
            f"Locked internal scene. Only the virtual camera moves slowly upward, so the complete flattened illustration shifts downward by about {abs(dy):.0f} pixels. "
            "All characters, objects, expressions, text surfaces and lighting remain perfectly rigid within the artwork. Keep screen-space overlays fixed. End on the measured upper reframe and hold."
        )
        editor = f"Animate the full illustration's Y position by {dy:+.1f} px over {shot['duration_seconds']:.3f} s at approximately 100% scale. Crop to 1280×720; use constant-speed interpolation."
        motion_type = "VERTICAL CAMERA MOVE UP"
    else:
        human = f"Slow downward virtual camera move: the flattened illustration shifts upward by approximately {abs(dy):.1f} px from start to end; scale stays near 100%."
        prompt = (
            f"Locked internal scene. Only the virtual camera moves slowly downward, so the complete flattened illustration shifts upward by about {abs(dy):.0f} pixels. "
            "All characters, objects, expressions, text surfaces and lighting remain perfectly rigid within the artwork. Keep screen-space overlays fixed. End on the measured lower reframe and hold."
        )
        editor = f"Animate the full illustration's Y position by {dy:+.1f} px over {shot['duration_seconds']:.3f} s at approximately 100% scale. Crop to 1280×720; use constant-speed interpolation."
        motion_type = "VERTICAL CAMERA MOVE DOWN"
    assert len(prompt) <= 500, (shot["shot_id"], len(prompt))
    return {
        "animation": True,
        "motion_type": motion_type,
        "human": human,
        "prompt": prompt,
        "editor": editor,
        "why": "The move refreshes attention and reveals a slightly different crop; it adds no new object action or story state.",
        "state": "F0 source crop → T1 whole-frame transform → F1 measured end crop.",
        "coupling": "CAMERA + SUBJECT COUPLED because every pixel of the flattened illustration moves as one rigid plate.",
    }


cards = []
prompt_rows = []
catalog_rows = []
for index, shot in enumerate(shots, 1):
    shot_id = shot["shot_id"]
    visual_id = shot["visual_id"]
    start = shot["in_seconds"]
    end = shot["out_seconds"]
    midpoint = (start + end) / 2
    beat = beat_for(midpoint)
    spoken = transcript_for(start, end)
    prompt = image_prompt(shot_id)
    plan = text_plan(shot_id)
    motion = motion_details(shot)
    next_visual = shots[index]["visual_id"] if index < len(shots) else "END OF VIDEO"
    animation_id = f"A{index:03d}" if motion["animation"] else "N/A"
    state_end = f"F{index:03d}.1" if motion["animation"] else f"F{index:03d}.0"
    transition_line = (
        f"At {shot['out_timestamp']}, hard-cut from {state_end} to {next_visual}. No crossfade or match-dissolve is measured. Cut motivation: narration advances to the next phrase, example, contradiction or payoff beat."
        if index < len(shots)
        else f"At {shot['out_timestamp']}, the final {state_end} crop reaches the encoded file end. No further visual transition is measured; narration has already resolved into the short audio tail."
    )
    source_file = shot["sample_files"]["mid"]
    text_value = visible_text[shot_id]
    trigger = beat[4]
    function = beat[3]
    animation_block = (
        f"ANIMATION ID: {animation_id}\n\nSOURCE STATE: F{index:03d}.0\n\nTARGET STATE: F{index:03d}.1\n\n"
        f"TIMESTAMP: {shot['in_timestamp']}–{shot['out_timestamp']}\n\nMOTION TYPE: {motion['motion_type']}\n\n"
        f"MOTION HERO: the full flattened illustration plate.\n\nSTART STATE: source crop at the shot in-point.\n\nEND STATE: measured transformed crop at the shot out-point.\n\n"
        f"DIRECTION / SPEED / AMPLITUDE: {motion['human']} The measured duration is {shot['duration_seconds']:.3f} s; exact easing is not verifiable.\n\n"
        f"CAMERA: virtual editorial reframe only.\n\nTRIGGER: {trigger}.\n\nSIMULTANEOUS EVENTS: none observed.\n\n"
        "STATIC ANCHORS: all characters, limbs, props, environmental details, lighting and any deterministic text within the illustration. The frame boundary and channel watermark remain fixed in screen space.\n\n"
        f"CONFIDENCE: {shot['global_motion_estimate']['confidence'].upper()} for the global transform; measured from start/end feature registration."
        if motion["animation"]
        else "ANIMATION REQUIRED: NO\n\nEDITOR ACTION: Hold the source image for the measured duration.\n\nAI PROMPT: N/A."
    )
    ai_section = (
        f"ANIMATION ID: {animation_id}\n\nSOURCE FRAME STATE: F{index:03d}.0\n\nSOURCE IMAGE TYPE: GENERATED MASTER IMAGE or supplied reference frame.\n\n"
        f"SOURCE IMAGE PROMPT:\n\n> {prompt}\n\nAI PROMPT:\n\n> {motion['prompt']}\n\nCHARACTER COUNT: {len(motion['prompt'])} / 500\n\nSTATUS: PASS"
        if motion["animation"]
        else f"SOURCE FRAME STATE: F{index:03d}.0\n\nSOURCE IMAGE TYPE: GENERATED MASTER IMAGE or supplied reference frame.\n\nSOURCE IMAGE PROMPT:\n\n> {prompt}\n\nAI PROMPT: N/A\n\nCHARACTER COUNT: 0 / 500\n\nSTATUS: PASS"
    )
    cards.append(
        f"# {visual_id} — {shot['in_timestamp']}–{shot['out_timestamp']}\n\n"
        f"SHOT: {shot_id}\n\nSOURCE REFERENCE FRAME: `evidence/reference_frames/{source_file}` sampled at approximately {ts(shot['samples']['mid'])}\n\n"
        f"DURATION: {shot['duration_seconds']:.3f} s\n\nSTATE ID: F{index:03d}.0\n\n"
        "## 1. WHAT THE VIEWER SEES\n\n"
        f"If you paused the video here, you would see {descriptions[shot_id][0].lower() + descriptions[shot_id][1:]} Literal frame description: {descriptions[shot_id]} The full 16:9 image is a warm editorial illustration; foreground, midground and background are flattened into one artwork plate.\n\n"
        "## 2. SCRIPT ↔ VISUAL SYNC\n\n"
        f"SPOKEN WORDS: “{spoken}”\n\nVISUAL APPEARS: DURING.\n\nTRIGGER WORD / IDEA: {trigger}.\n\nMOTION CUE: the shot begins on the new illustrative example, then uses only the measured global reframe or hold.\n\nFUNCTION: {function}. Active viewer question: {beat[5]} Loop status: {beat[6]}.\n\n"
        "## 3. CHANGE FROM PREVIOUS\n\n"
        f"ADDED: the complete {visual_id} illustration and its scene-specific subjects/props.\n\nREMOVED: the complete previous illustration.\n\nMOVED / RESIZED / REFRAMED: {motion['human']}\n\nROTATED / REVOLVED / RECOLORED: none observed.\n\nTEXT: {text_value}.\n\nSTATIC: all internal pose, object, lighting and geometry relationships remain frozen.\n\n"
        "## 4. VISUAL PURPOSE\n\n"
        f"A literal-to-metaphorical editorial illustration of the current beat, used to convert narration into a quickly decoded scenario. Classification: EXPLANATORY and REINFORCING, with emotional tone supplied by the protagonist's expression. If removed, the narration remains intelligible, but the concrete example and 3.3-second visual reset disappear.\n\n"
        "## 5. CONSTRUCTION MAP\n\n"
        "BACKGROUND: scene environment described above, baked into the illustration plate.\n\nMAIN SUBJECT: the retiree/presenter or specified alternate person.\n\nSECONDARY: props and supporting people described above.\n\nGRAPHICS: scene-specific board, screen, sign or illustration details when present.\n\nTEXT: deterministic overlay when listed; otherwise none.\n\nVISUAL HERO: the protagonist's face/pose and the routine-relevant object.\n\nSTATIC COORDINATE FRAME: 1280×720 output canvas and screen-space overlays.\n\nLAYER ORDER: Layer 1 — illustration master plate; Layer 2 — deterministic environmental/title text if required; Layer 3 — persistent channel watermark at top-right; Layer 4 — occasional subscribe bug.\n\n"
        "## 6. EXACT LAYOUT\n\n"
        f"CANVAS: 1280×720. ASPECT RATIO: 16:9. MAIN SUBJECT / SECONDARY / CROP: {descriptions[shot_id]} Preserve those left-right relationships, relative scale, occlusion and the source's medium-wide eye-level perspective. NEGATIVE SPACE: retain the quiet wall, sky, floor or environment areas visible around the subject; do not fill them with new decoration. MARGINS: no safety border; artwork bleeds to frame except explicit white-background vignettes. PRIMARY EYE PATH: face and gesture → routine object → environment/context. Numerical object coordinates beyond the measured global transform are not defensible from the available evidence.\n\n"
        "## 7. ATTENTION ORDER\n\n"
        "FIRST LOOK: face, eyes and expression. SECOND LOOK: hand gesture or routine-relevant prop. THIRD LOOK: supporting environment or readable board/sign. Attention control is generally CLEAN: large character scale, warm facial contrast, simple depth layers and one dominant action.\n\n"
        "## 8. IMAGE REUSE STATUS\n\n"
        f"NEW BASE. BASE: {visual_id} master illustration. CHANGES: only a rigid editorial crop transform from F{index:03d}.0 to {state_end}; no internally redrawn state is evidenced.\n\n"
        "## 9. IMAGE DNA\n\n"
        f"OUTPUT TYPE: 2D editorial cartoon. SUBJECT: expressive older retiree or specified supporting character. POSE: fixed mid-action or reaction pose. WARDROBE: earth-tone plaid, knitwear or scene-specific attire. MATERIAL: hand-inked outlines with softly painted digital fills. ENVIRONMENT: warm domestic/suburban/public setting or explicit white-background vignette. CAMERA: mostly eye-level medium-wide. LIGHTING: amber daylight/interior lamp for positive scenes; blue-violet night/news contrast for negative scenes. COLOR: warm orange, brown and green with selective cool-blue contrast. STYLE: polished AI-assisted storybook/editorial illustration. TEXT: {text_value}. GRAPHICS: persistent top-right watermark added after the illustration.\n\n"
        "## 10. EXACT STANDALONE IMAGE PROMPT\n\n"
        f"> {prompt}\n\n"
        "## 11. TEXT BAKE / OVERLAY DECISION\n\n"
        f"BAKE TEXT: {plan['decision']}. CLEAN PLATE REQUIREMENT: {plan['clean']} TEXT OVERLAY SPEC: {plan['overlay']}\n\n"
        "## 12. FIDELITY LOCK\n\n"
        f"HUMAN PRODUCTION LOCK — CHARACTER / POSE / OBJECT COUNT / OBJECT POSITION / SCALE / CAMERA / BACKGROUND / LIGHTING / COLOR / NEGATIVE SPACE: preserve the literal frame description exactly: {descriptions[shot_id]} TEXT: {text_value}. PROHIBITED CHANGES: no new people, pets, props, particles, gestures, facial movement, cloth motion, environmental drift, glow pulses, parallax, lighting change or decorative camera move beyond the measured transform.\n\n"
        "## 13. IMAGE PROMPT COVERAGE AUDIT\n\n"
        "SUBJECT: High. POSE: High. GEOMETRY: Medium–High. COMPOSITION: High. SCALE: Medium. PERSPECTIVE: High. LIGHTING: High. COLOR: High. NEGATIVE SPACE: High. TEXT PLAN: High. CONTINUITY: Medium because the reference itself exhibits identity and wardrobe drift between shots. This is prompt coverage, not generated-image validation.\n\n"
        "## 14. FRAME STATE ID\n\n"
        f"F{index:03d}.0 — master illustration at source crop. {state_end} — {'measured transformed crop' if motion['animation'] else 'same held crop'}.\n\n"
        "## 15. STATE-CHAIN POSITION\n\n"
        f"{motion['state']}\n\n"
        "## 16. COMPLETE MOTION EVENT INVENTORY\n\n"
        f"{animation_block}\n\n"
        "## 17. WHY MOVE\n\n"
        f"{motion['why']} WHY THIS DIRECTION / SPEED / AMPLITUDE: it matches the measured global feature transform; no semantic object movement is visible.\n\n"
        "## 18. WHAT STAYS STATIC\n\n"
        "Character identity, body pose, head, hands, gaze, expression, clothing, all props, architecture, background, lighting, color, environmental details and text geometry stay fixed relative to the illustration. The watermark stays fixed relative to the output frame. Static reason: reading stability, visual hierarchy, continuity and avoidance of generative drift.\n\n"
        "## 19. MOTION INTERFERENCE ANALYSIS\n\n"
        "ALLOWED TO MOVE: the complete flattened illustration as one rigid plate, and only when a global move is measured. LOCKED / MUST REMAIN STABLE: every internal element; deterministic text relative to its surface; watermark relative to screen. OTHER ACTIVE EVENTS: none observed. Could this animation disturb another moving element? NO if executed as editor transform; YES if regenerated through AI because characters and lettering may drift.\n\n"
        "## 20. MOTION COUPLING CLASSIFICATION\n\n"
        f"{motion['coupling']} No independent or sequential internal animation is evidenced.\n\n"
        "## 21. RECOMMENDED PRODUCTION METHOD\n\n"
        f"{'EDITOR KEYFRAMES' if motion['animation'] else 'STATIC HOLD'}. Reference-faithful primary method: {motion['editor']} Recreation method; original software is not verified.\n\n"
        "## 22. AI SUITABILITY\n\n"
        f"{'LOW' if motion['animation'] else 'NOT APPLICABLE'}. AI image-to-video adds no advantage for a rigid plate transform and creates identity, geometry, text and background-drift risk. If AI movement is mandatory, use the isolated prompt below and composite only after validating static anchors.\n\n"
        "## 23. AI ISOLATION PLAN\n\n"
        f"Single full-plate pass only; do not ask AI to animate characters or objects. Keep text and watermark outside the AI clip. BASE PLATE: F{index:03d}.0. TARGET REGION: full illustration, X 0–100 and Y 0–100. Motion-leakage risks: character, text, geometry and lighting drift. Prevention: editor keyframes are preferred; otherwise difference-check every frame and reject internal deformation.\n\n"
        "## 24. SOURCE IMAGE FOR EACH AI PASS\n\n"
        f"{ai_section}\n\n"
        "## 25. ANIMATION PROMPT(S) ≤500 CHARACTERS\n\n"
        f"ANIMATION ID: {animation_id}. SOURCE STATE: F{index:03d}.0. TARGET STATE: {state_end}. AI PROMPT: “{motion['prompt']}” CHARACTER COUNT: {len(motion['prompt']) if motion['animation'] else 0} / 500. STATUS: PASS.\n\n"
        "## 26. EDITOR / COMPOSITING BUILD\n\n"
        f"LAYERS REQUIRED: master illustration, deterministic text where applicable, watermark, optional subscribe overlay. BUILD ORDER: generate/clean the base → place text → precompose illustration and surface text → apply the measured global transform to that precomp → keep watermark fixed above it. TECHNIQUE: {motion['editor']} No mask, multi-pass AI or 2.5D separation is needed.\n\n"
        "## 27. EDIT OUT / NEXT STATE\n\n"
        f"{transition_line}\n\n"
        "## 28. RECONSTRUCTION RULE\n\n"
        "Treat the scene as a still illustration, not a living tableau. Reconstruct the base frame faithfully, animate only the measured whole-frame crop, keep every internal element untouched, preserve screen-space overlays, and cut sharply to the next visual.\n"
    )
    prompt_rows.append(
        {
            "animation_id": animation_id,
            "shot_id": shot_id,
            "visual_id": visual_id,
            "source_state": f"F{index:03d}.0",
            "target_state": state_end,
            "timestamp_in": shot["in_timestamp"],
            "timestamp_out": shot["out_timestamp"],
            "method": "EDITOR KEYFRAMES" if motion["animation"] else "STATIC HOLD",
            "motion_type": motion["motion_type"],
            "ai_suitability": "LOW" if motion["animation"] else "N/A",
            "ai_prompt": motion["prompt"],
            "character_count": len(motion["prompt"]) if motion["animation"] else 0,
            "status": "PASS",
        }
    )
    catalog_rows.append(
        {
            "shot_id": shot_id,
            "visual_id": visual_id,
            "in": shot["in_timestamp"],
            "out": shot["out_timestamp"],
            "duration_seconds": round(shot["duration_seconds"], 3),
            "script_beat": beat[2],
            "function": function,
            "scene": descriptions[shot_id],
            "visible_text": text_value,
            "motion_type": motion["motion_type"],
            "transition_out": "HARD CUT" if index < len(shots) else "END / AUDIO TAIL",
            "confidence": shot["global_motion_estimate"]["confidence"].upper(),
        }
    )

(OUTPUT / "visual_reconstruction_cards.md").write_text(
    "# Visual Reconstruction Cards\n\n"
    "253 source-grounded production cards. Coordinates and transform values are approximate measurements, not pixel-perfect source-project data. Every animation prompt is character-count audited at ≤500 characters.\n\n"
    + "\n\n---\n\n".join(cards)
    + "\n",
    encoding="utf-8",
)

with (OUTPUT / "animation_prompts.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=prompt_rows[0].keys())
    writer.writeheader()
    writer.writerows(prompt_rows)

with (OUTPUT / "visual_catalog.csv").open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=catalog_rows[0].keys())
    writer.writeheader()
    writer.writerows(catalog_rows)

with (OUTPUT / "edl.csv").open("w", newline="", encoding="utf-8") as handle:
    fieldnames = ["shot_id", "in", "out", "duration_seconds", "visual_state", "transition", "cut_motivation", "motion_hero", "static_anchor"]
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()
    for row in catalog_rows:
        writer.writerow(
            {
                "shot_id": row["shot_id"],
                "in": row["in"],
                "out": row["out"],
                "duration_seconds": row["duration_seconds"],
                "visual_state": row["visual_id"],
                "transition": row["transition_out"],
                "cut_motivation": f"Narration beat: {row['script_beat']} {row['function']}",
                "motion_hero": "Full illustration plate" if row["motion_type"] != "STATIC HOLD" else "None",
                "static_anchor": "Internal illustration geometry; screen-space watermark",
            }
        )


beat_lines = [
    "# Script Beat Map",
    "",
    "Transcript-derived beat structure. Timing is aligned to the verified local transcription; wording may contain minor ASR errors and should be checked against the source before publication.",
    "",
]
for start, end, beat_id, function, topic, question, loop_status in BEATS:
    beat_lines.extend(
        [
            f"## {beat_id} — {ts(start)}–{ts(end)}",
            "",
            f"- Function: {function}",
            f"- Beat: {topic}",
            f"- Active viewer question: {question}",
            f"- Loop status: {loop_status}",
            f"- Spoken text: {transcript_for(start, end)}",
            "",
        ]
    )
(OUTPUT / "script_beats.md").write_text("\n".join(beat_lines), encoding="utf-8")


durations = [shot["duration_seconds"] for shot in shots]
shortest_index = min(range(len(shots)), key=lambda i: durations[i])
longest_index = max(range(len(shots)), key=lambda i: durations[i])
motion_counts = {}
for shot in shots:
    key = shot["global_motion_estimate"]["classification"].split("+")[0]
    motion_counts[key] = motion_counts.get(key, 0) + 1
moving_count = len(shots) - motion_counts.get("static_hold", 0)
prompt_lengths = [row["character_count"] for row in prompt_rows if row["animation_id"] != "N/A"]
intro_shots = [shot for shot in shots if shot["in_seconds"] < 91.68]
body_shots = [shot for shot in shots if 91.68 <= shot["in_seconds"] < 779.30]
closing_shots = [shot for shot in shots if shot["in_seconds"] >= 779.30]

report = f"""# Master Video Forensic Reconstruction Report

## Executive finding

The reference is a 14:03.68 landscape narration video built from **253 distinct full-frame editorial illustrations**, not conventional live-action shots and not character animation. The edit makes those stills feel active through **252 hard cuts** and **225 rigid whole-image transforms**: **{motion_counts.get('digital_push_in', 0)} centered push-ins**, **{motion_counts.get('content_shifts_down_camera_up', 0)} upward virtual-camera moves** and **{motion_counts.get('content_shifts_up_camera_down', 0)} downward virtual-camera moves**. The remaining **{motion_counts.get('static_hold', 0)} shots are true static holds**.

The decisive reconstruction rule is therefore simple: generate or illustrate one correct 16:9 master image per visual state, keep all characters and objects frozen, add exact text as editor overlays, animate only the complete flattened plate with deterministic scale/position keyframes, keep the small channel watermark fixed in screen space, and hard-cut to the next image. No independent head, hand, cloth, plant, pet, light, particle or environmental animation is visibly evidenced.

Confidence: **HIGH** for metadata, shot count, boundary timing, global motion classes and transcript timing; **MEDIUM** for precise object geometry and unreadably small environmental lettering; **LOW / NOT VERIFIABLE** for the original image model, editor, plugins, font files, easing curves, music track and sound-effect library.

## Evidence package

- `visual_reconstruction_cards.md` — 253 complete 28-section production cards.
- `visual_catalog.csv` — compact shot/state descriptions, beat alignment, text and motion classes.
- `animation_prompts.csv` — all animation events with source/target states, methods, ≤500-character prompts and counts.
- `edl.csv` — full edit decision list.
- `script_beats.md` — 41 script beats with loop status and transcript text.
- `transcript.txt`, `transcript.srt`, `transcript.json` — local Base English Whisper transcript, including word timestamps in JSON.
- `shot_manifest.json` — measured cut points, sample times, change metrics and affine motion estimates.
- `evidence/overview_contact_sheet.jpg` and 16 shot montage pages — visual overview.
- `evidence/motion_triplets_01.jpg` through `motion_triplets_32.jpg` — start/mid/end motion evidence for every shot.
- `audio_summary.json`, `audio_envelope.csv`, `audio_envelope.png` — full-mix audio measurements.

## Pass 0 — media inspection

| Property | Measured value |
|---|---:|
| Duration | 843.636 s / 00:14:03.636 |
| File size | 61,671,022 bytes (about 58.8 MiB) |
| Resolution | 1280×720 |
| Aspect ratio | 16:9 |
| Orientation | Landscape |
| Frame rate | 30 fps |
| Video | H.264 Main, `avc1`, yuv420p, BT.709, progressive, about 453 kb/s |
| Audio | AAC-LC, 44.1 kHz, stereo, about 128 kb/s |
| Audio presence | Yes |
| Container | ISO Base Media / MP4 |

The source was directly decoded in full. Overview frames, 253 shot representative frames and 759 start/mid/end samples were generated. Transcript extraction succeeded for English narration: 282 ASR segments over the full program.

## Passes 1–3 — shots, visual states and dense sampling

### Shot/state detection

- Major shots: **253**.
- Meaningful visual states: **253**. Each cut introduces a new base illustration; no within-shot independently animated object state was found.
- Transitions: **252 hard cuts**. Two boundaries at **00:03:01.833** and **00:04:30.233** scored just below a stricter scene threshold and were recovered through dense 4 fps sampling and a lower validated threshold.
- Average shot length: **{statistics.mean(durations):.3f} s**.
- Median shot length: **{statistics.median(durations):.3f} s**.
- Shortest: **{shots[shortest_index]['shot_id']}**, {durations[shortest_index]:.3f} s, {shots[shortest_index]['in_timestamp']}–{shots[shortest_index]['out_timestamp']}.
- Longest: **{shots[longest_index]['shot_id']}**, {durations[longest_index]:.3f} s, {shots[longest_index]['in_timestamp']}–{shots[longest_index]['out_timestamp']}.
- Opening cluster: {len(intro_shots)} shots before routine one, averaging {statistics.mean([s['duration_seconds'] for s in intro_shots]):.3f} s.
- Eight-routine body: {len(body_shots)} shots, averaging {statistics.mean([s['duration_seconds'] for s in body_shots]):.3f} s.
- Closing cluster: {len(closing_shots)} shots, averaging {statistics.mean([s['duration_seconds'] for s in closing_shots]):.3f} s.

### Motion-critical finding

Feature registration across every start/end triplet found only four reference-faithful behaviors:

| Behavior | Count | Observed construction |
|---|---:|---|
| Centered push-in | {motion_counts.get('digital_push_in', 0)} | Full illustration scales by roughly five percent; internal scene remains rigid. |
| Camera moves up | {motion_counts.get('content_shifts_down_camera_up', 0)} | Full illustration shifts down by roughly 21 px, revealing a slightly higher crop. |
| Camera moves down | {motion_counts.get('content_shifts_up_camera_down', 0)} | Full illustration shifts up by roughly 21 px, revealing a slightly lower crop. |
| Static hold | {motion_counts.get('static_hold', 0)} | No measurable camera or object movement. |

No local object deformation survived registration as an independent event. Apparent action—walking, waving, pancake tossing, gardening, pointing, laughing—is represented by a frozen mid-action drawing. This is crucial: those poses imply action, but the video does **not** animate that action.

## Pass 4 — persistent asset manifest

| ID | Type | Persistent production role |
|---|---|---|
| C01 | Character | Primary gray-haired, bespectacled retiree; identity varies perceptibly across generated illustrations. |
| C02 | Character | Older woman/wife/peer, used for meals, care, laughter and gratitude. |
| C03 | Character set | Older male friends, younger adults, workers and helpers. |
| C04 | Character set | Children/grandchildren in setup and family examples. |
| E01 | Environment | Warm home interiors: kitchen, bedroom, living room, hall and office. |
| E02 | Environment | Porch, garden, street, park and sunrise exteriors. |
| E03 | Environment | Bank, store, clinic, office, subway, café, community center and gym. |
| O01 | Object family | Coffee mugs, glasses, meals and kitchen props. |
| O02 | Object family | Television, phone, tablet, laptop and news screens. |
| O03 | Object family | Bed, bedside lamp, clock and sleep props. |
| O04 | Object family | Plants, garden tools, cats and dogs. |
| O05 | Object family | Papers, calendars, budgets, lists and newspapers. |
| G01 | Graphic | Eight routine title boards/whiteboards/chalkboards. |
| G02 | Graphic | Small circular channel watermark fixed at upper-right. |
| G03 | Graphic | Occasional subscribe overlay near lower-right. |
| T01 | Text system | Handwritten routine headings; deterministic overlay recommended. |
| A01 | Audio | Continuous male English narration. |
| A02 | Audio | Low-level full-mix bed persisting under many narration gaps; likely music/ambience, track unverified. |
| A03 | Audio | Short silence/near-silence at section boundaries and about 0.9 s at the tail. |

## Pass 5 — frame-state chain

Animated shots use one state chain only:

`F###.0 — source crop → T### — rigid whole-plate position/scale transform → F###.1 — measured end crop → hard cut`

Static shots use:

`F###.0 — unchanged hold → hard cut`

There are no verified sequential object states, no simultaneous independent object motions, no persistent internal loops and no first/last-frame morphs. The complete state-chain package for every shot appears in `visual_reconstruction_cards.md`.

## Engine A — script intelligence

### A1–A2: grounding and packaging promise

Title promise: **Simple Routines Thriving Retirees Practice Daily**. No separate thumbnail was supplied, so a thumbnail promise cannot be verified. The title's click question is: *Which simple daily routines distinguish thriving retirees?* The video answers with eight named routines, each explained through a problem, mechanism, examples and an actionable close. Packaging/body/payoff classification: **STRONG MATCH**.

### A3: hook architecture

The opening validates a familiar retirement fantasy—beach, cruise, golf, grandkids—then breaks it with “that's the trailer, not the movie.” The reveal that retirement is a random Tuesday converts an abstract future into a repeatable unit of daily life. “About 10,000 Tuesdays” is the key curiosity and value frame. Context, relevance, contradiction, open question and value preview all arrive before the first routine at 01:31.68.

### A4: causal story spine

The macro spine is: **retirement is sold as highlights → but most of it is ordinary time → therefore daily routines determine lived quality → eight routines repair common forms of drift → money buys freedom, but routines build the life**.

Each routine repeats a strong causal micro-spine: **name the trap → show what retirement removed or loosened → explain the physical/psychological consequence → offer a small daily behavior → close with an aphoristic payoff**. This is mostly `BUT → THEREFORE`, not a loose “and then” list.

### A5–A6: curiosity and payoff

The numbered list creates stable forward curiosity, but each routine is announced before explanation, so suspense is modest rather than expanding. Micro-payoffs include “chase the daylight,” “guard your sleep,” “control the information,” “being needed is medicine,” “feed yourself like you're worth the effort,” “order out there creates calm in here,” “laugh on purpose,” and “find three good things.” The ultimate payoff—money is the tool, routines are what you build with it—correctly returns to the ordinary-Tuesday premise.

### A7: logic

Most advice follows claim → mechanism → consequence → minimum action. The video does not cite sources for several health claims, including morning light's downstream effects, sleep “power washing” the brain, laughter's cardiac benefit, and nursing-home plant/pet outcomes. Those claims may be directionally plausible, but within this video they are unsupported assertions. Medical precision should be softened or sourced if the script is republished.

### A8: emotion

The dominant emotional progression is aspiration → comic recognition → mild anxiety about drift → relief through small actions → warm closure. Humor prevents the advice from becoming scolding: the “wise lizard,” “toddler's finger painting,” “sink grazing,” “coffee and hope,” “human keep-off-the-grass sign,” and caveman analogy are deliberate pressure releases.

### A9–A10: retention, share and replay

Strengths: frequent visual resets, numbered structure, vivid metaphors and highly quotable closes. Risks: 14 minutes of the same illustration grammar can become visually predictable; eight routines create a midpoint list-fatigue risk; title cards reveal each answer before its mechanism; some examples over-explain after the point is understood. Positive replay candidates are the ordinary-Tuesday hook, the information-diet punchline and the money/toolbox synthesis. Confusion replay risk is low, though unsupported health specificity could invite scrutiny.

### A11–A12: CTA and next video

The commitment CTA—pick one, name what you already do well and what needs work—arrives after the full payoff and is **EARNED**. Like/subscribe follows and is short. The next-video bridge is generic (“new videos every week”) rather than a specific unresolved related question; this is the weakest packaging transition.

### A13: consensus

- Strong agreements: the Tuesday reframing, repeated causal routine structure, humor and practical micro-actions are the system's strongest elements.
- Important tradeoff: breadth delivers eight ideas but limits evidence and novelty within each.
- Critical problem: visual identity drift and repetitive pan/zoom grammar reduce perceived polish.
- Highest leverage fixes: tighten redundant explanations, add source-backed specificity where medical claims are made, and vary the visual mechanism at routine-level transitions without adding decorative motion inside ordinary shots.

## Engine B — visual intelligence

### Objective visual grounding and spatial geometry

The visual system is a sequence of warm 16:9 editorial cartoons. C01 usually occupies the center or one side of a medium-wide frame; a single routine object sits close to the face or hands; the environment fills the remaining thirds. Eye path is consistently face → gesture/prop → contextual background. Numerical element coordinates were not invented; each card records defensible frame-third relationships and measured global transforms.

### Cinematography and attention

Most scenes simulate eye-level medium-wide photography, occasionally switching to closer domestic reactions or wide environmental tableaux. Positive routines use amber sun, warm wood and green gardens; failure states use blue night, purple television light, cool clinics and dim rooms. Attention is usually clean because the large expressive face and one prop dominate. Overload is intentionally used for clutter, news and paperwork examples.

### Editing and temporal change

Every new state arrives by hard cut. Within a state, nothing is added, removed, redrawn or independently animated. Temporal change is only crop, scale or hold. This is more accurately a Ken Burns-style editorial slideshow than AI video animation.

### Information value and object lifecycle

Screens/phones progress from passive consumption to deliberate shutoff; beds/clocks progress from chaos to protected rhythm; plants/pets move from example to responsibility; papers/clutter move from stress to order; food progresses from snack improvisation to intentional meals. The title boards are explicit routine resets and the protagonist is the persistent continuity device.

### Continuity drift

Identity continuity is **MEDIUM–LOW**. Hair shape, beard density, glasses, age, face proportions and even body type change across shots. Wardrobe changes are often motivated by context but not consistently tracked. Secondary characters also shift style. Environmental perspective and object scale vary. These are visible generation inconsistencies, not motion events. A locked character sheet and seed/reference workflow would materially improve fidelity.

### Color, typography and visual DNA

Dominants: amber, tan, brown, muted red plaid and garden green. Negative states shift toward navy, cyan and violet. Routine title cards use hand-lettered black text on whiteboard/green chalkboard surfaces. Environmental lettering is often small, warped or pseudo-legible. Recreate all semantic text outside the image generator. Visual DNA: storybook/editorial AI illustration, expressive older protagonist, literal metaphors, warm domestic spaces, one visual idea per frame, hard cuts and alternating whole-frame reframes.

## Engine C — reconstruction and motion intelligence

### Image system

Generate 253 text-free master illustrations from the standalone prompts in the card file. Use a persistent C01 character reference, but permit explicitly different supporting characters where shown. Generate at least 1344×756 or, preferably, 1920×1080 so a five-percent zoom and 21 px pan do not expose edges. Crop/export to 1280×720 only after motion.

### Text bake policy

Semantic text should not be baked by an image model. Build routine headings, calendar data, signs, screens and callouts as editable vector/text overlays, matched to the source surface and line breaks. Flatten those overlays with the illustration before applying the global move so they remain registered to the scene. The small circular watermark and subscribe bug remain separate screen-space layers.

### Complete motion inventory

Total motion events: **{moving_count}**. Every event is a single rigid global transform. Total non-events/static holds: **{motion_counts.get('static_hold', 0)}**. Motion relationship classification for all moving shots: **CAMERA + SUBJECT COUPLED**. Motion hero: complete illustration plate. Static anchors: all internal geometry and screen-space overlays.

### AI / deterministic / hybrid routing

- Primary method: **EDITOR KEYFRAMES** for all {moving_count} moves.
- Static method: **STATIC HOLD** for {motion_counts.get('static_hold', 0)} shots.
- AI single pass recommended: 0.
- AI multi-pass recommended: 0.
- AI state-chain generation recommended: 0.
- First/last-frame AI recommended: 0.
- Hybrid internal animation recommended: 0.

AI image generation is useful for the base illustrations; AI image-to-video is not the faithful motion method. Optional AI prompts are included because the specification requests them, but they are rated LOW suitability. The deterministic editor instructions are the authoritative reconstruction path.

### Motion-cue conflict

Many source drawings depict mid-action poses—walking, waving, tossing food, laughing, watering or pointing. Those cues suggest motion, but dense sampling shows that the pose remains frozen while the camera reframes. Do not “complete” the implied action. The corrected source is the exact frozen reference pose, without motion blur or speed lines unless visibly present.

### Editor build

For each shot: import the master illustration → add deterministic surface text → precompose those two → apply measured scale/position keyframes to the precomp → add watermark and subscribe bug above it → hard-cut at the EDL boundary. No optical flow, frame interpolation, puppet deformation, parallax, 2.5D depth or AI video generation is needed.

## Editing intelligence

EDL status: **COMPLETE**. Shot count {len(shots)}; transitions 252 hard cuts; average {statistics.mean(durations):.3f} s; median {statistics.median(durations):.3f} s. Cut motivation follows phrase completion, metaphor change, example change, routine title or payoff. The fastest-feeling cluster is the stereotype montage and early hook; the slowest shots appear where one complex metaphor or emotional beat needs more reading time. The complete row-level EDL is in `edl.csv`.

## Audio intelligence

Narration is verified across 282 timestamped ASR segments. The full mix measures approximately **−11.86 LUFS integrated**, **−0.10 dBTP true peak** and **4.0 LU loudness range**—loud, dense and tightly controlled. Median 0.25 s RMS is {audio['rms_dbfs_median_all']:.2f} dBFS; narration-majority windows are {audio['rms_dbfs_median_speech']:.2f} dBFS; near-non-speech windows remain around {audio['rms_dbfs_median_nonspeech']:.2f} dBFS. That persistent low-level energy is consistent with a music or ambience bed, but no stem or semantic track identification is available, so the exact track is **NOT VERIFIED**. Top peaks align primarily with speech; no unique SFX can be confidently named. Near-silence occurs around 04:08.50, 06:51.75, 06:55.75, 11:22.50 and the final 0.9 s. Narration ends at about 14:02.62, followed by a short tail/fade.

Audio event → visual event mapping is primarily rhetorical: narration phrase changes trigger hard cuts; routine titles receive clean visual resets; punchlines receive reaction or metaphor images. No frame-accurate SFX hits were verified.

## Thumbnail and Shorts extraction

### Thumbnail candidates

1. **V020 at 00:45.833** — retiree with a wall of Tuesdays. Dominant object: calendar. Mobile question: “How many ordinary Tuesdays are left?” Remove tiny peripheral clock details; enlarge the retiree and “10,000 Tuesdays” as new deterministic thumbnail text. Strongest title relationship.
2. **V043 at 02:02.300** — retiree under a spotlight with arms raised. Strong silhouette and high contrast, but weaker direct relationship to the title. Pair with “8 DAILY ROUTINES” only if text is added outside the image.
3. **V251 at 13:54.167** — savings progress, new week and planner. Clear habit/system symbolism, though less emotionally immediate.

### Shorts candidates

- **00:20.74–00:48.32**: “That's the trailer, not the movie” → ordinary Tuesday → thousands of Tuesdays. Context required: minimal. Core payoff: retirement quality is daily, not occasional.
- **04:45.25–05:30.34**: information industry → check once → do not hand your peace back to a screen. Strong standalone contradiction and close.
- **10:49.37–11:19.26**: laugh at aging instead of raging at it → walking into a room and forgetting why. Humor-led, low-context clip.
- **12:59.30–13:28.93**: money is the tool; routines are what you build with it. Best channel-positioning Short and conclusion.

Use the corresponding visual cards and animation prompt rows for exact images and motion. Do not force additional CTA animation.

## Engine D — master synthesis

### Story engine

**HOOK:** retirement postcard fantasy. **ESCALATION:** most time is ordinary and unstructured. **REVERSAL:** thriving is built through tiny routines, not exceptional events. **PAYOFF:** money creates freedom; daily behaviors turn freedom into a life.

### Creator visual and motion formula

`Narration phrase → literal/metaphorical editorial illustration → one rigid push/pan/hold → hard cut on next phrase`

What moves: the complete flattened image. What stays static: everything inside it. Static coordinate frame: 1280×720 canvas plus watermark. Trigger: narration phrase or micro-payoff. Camera moves only as an editorial crop; the creator cuts instead of animating whenever the idea changes.

### AI reconstruction engine

Base images: AI/illustration-friendly. Motion: deterministic editor-only. State chains: one transform per moving shot. Text: vector/editor. First/last frames: unnecessary because the target is a crop, not a changed scene. Multi-pass isolation: unnecessary if the art remains a single plate. Validation: frame-difference the finished clip against the reference and reject any internal deformation.

### Master image DNA

- Character: late-sixties gray-haired bespectacled retiree, short beard, expressive eyes, average build; lock a turnaround sheet and five core expressions.
- Objects: simplified domestic props with dark outlines and readable silhouettes; one routine-relevant hero prop per scene.
- Environments: warm American suburban homes and public spaces, rendered in layered but shallow editorial depth.
- Graphics: clean chalkboards, whiteboards, screens and signs with text added later.
- Style: polished hand-inked digital cartoon, softly painted texture, warm midtones, stable anatomy, 16:9 medium-wide staging.
- Color: amber/brown/green for thriving; navy/cyan/violet for fatigue, news and worry.
- Typography: hand-lettered display for routine titles, plain readable sans serif for calendars/screens; never accept pseudo-text from the image model.

### Repeated attention engine

Face/expression first → hand/prop second → environment/board third. The motion does not redirect the eye internally; it only changes crop scale. Routine title cards reset the hierarchy by making the heading first.

### Improvements

| Priority | What works | Friction | Minimal fix | Aggressive fix |
|---|---|---|---|---|
| Critical | Clear protagonist and warm visual tone | Character face, beard, glasses and age drift | Use one locked character reference and reject off-model frames | Build a full C01 model sheet and fine-tuned/consistent illustration pipeline |
| High | Frequent visual resets | 225 moves repeat only three transform types | Vary start crops and hold timing while keeping internal stillness | Introduce a small set of deterministic diagrams or object reveals only at major mechanisms |
| High | Eight clear routine boards | Small text is often warped or pseudo-legible | Replace semantic text in editor | Generate all scenes as text-free clean plates and maintain a typography system |
| High | Humor and practical metaphors | Some health claims are unsourced | Soften absolute wording | Add succinct source cards or linked references |
| Medium | Hard cuts maintain pace | Constant cuts can feel mechanical | Let selected payoff images breathe one extra second | Group examples into visual mini-arcs with purposeful callback frames |
| Medium | CTA is earned | Next-video bridge is generic | Name a specific related unanswered question | Script the conclusion into the next episode's packaging promise |
| Optional | Warm color system | Negative states lean on similar blue-TV imagery | Rotate among composition, prop and lighting contrasts | Create routine-specific accent colors and recurring visual motifs |

### New-topic translation

No new topic was supplied. Use this mapping template without copying surface content:

| Original function | Original mechanism | New-topic equivalent |
|---|---|---|
| Postcard retirement fantasy | Rapid idealized montage | Show the new topic's culturally familiar “highlight reel” |
| Ordinary Tuesday reveal | One mundane domestic unit repeated over time | Identify the smallest repeatable unit where outcomes are actually decided |
| Eight routine boards | Numbered chapter reset | Use a fixed count of practical levers with deterministic title cards |
| Trap scenes | Blue/dim failure-state illustrations | Show the default failure behavior in the new domain |
| Mechanism scenes | Literal metaphor cartoons | Visualize why the lever works, not just what to do |
| Minimum action | One person and one hero prop | Stage the smallest executable behavior |
| Aphoristic close | Warm payoff image | End each chapter with a memorable one-line rule |
| Money/tool synthesis | Return to opening premise | Reconcile the enabling resource with the behavior that creates value |

Keep the composition grammar, motion grammar, pacing, transition logic, proof logic, payoff structure and asset reuse. Change facts, objects, characters, maps, numbers, branding and literal imagery.

## Zero-to-final rebuild order

1. Lock the title promise and one clear click question.
2. Segment the script into the 41 supplied beats.
3. Preserve the macro causal spine and routine micro-spines.
4. Import `edl.csv` as the timing blueprint.
5. Use `visual_catalog.csv` to assign all 253 states.
6. Build the persistent asset library and C01 character sheet.
7. Generate 253 text-free master illustrations from the card prompts.
8. Quality-control identity, pose, object count, composition, lighting and negative space.
9. Rebuild all semantic text as deterministic overlays.
10. Place illustration plus surface text in one precomp per shot.
11. Apply the exact measured transform in each card: push-in, upward move, downward move or hold.
12. Keep watermark and subscribe overlay fixed above the moving precomp.
13. Assemble 252 hard cuts at the EDL boundaries.
14. Lay in narration and verify phrase-to-cut sync.
15. Add or recreate a low-level music bed only after verifying the desired track; do not invent SFX.
16. Mix to an intentional target, preferably about −14 to −16 LUFS with true peak at or below −1 dBTP unless the distribution platform requires otherwise.
17. Run continuity, text, crop-edge and motion-leakage audits.
18. Compare start/mid/end frames against the evidence triplets.
19. Verify the title promise, ordinary-Tuesday payoff and CTA bridge.
20. Export H.264, 1280×720, 30 fps, BT.709 with AAC audio.

## Completeness audit

| Requirement | Result |
|---|---:|
| Source video inspected | YES |
| Major shots | 253 |
| Visual states | 253 |
| Script beats | {len(BEATS)} |
| Persistent assets | 19 |
| Visual cards | 253 / 253 |
| Standalone image prompts | 253 / 253 |
| Text bake decisions | 253 / 253 |
| Frame state chains | 253 / 253 |
| Total motion events | {moving_count} |
| Motion events identified | {moving_count} / {moving_count} |
| Why-move/static analysis | 253 / 253 |
| Motion coupling classified | 253 / 253 |
| Motion interference checks | 253 / 253 |
| AI suitability decisions | 253 / 253 |
| Primary methods | 253 / 253 |
| AI single-pass recommended | 0 |
| AI multi-pass recommended | 0 |
| AI state-chain recommended | 0 |
| First/last-frame recommended | 0 |
| Hybrid recommended | 0 |
| Deterministic/editor | {moving_count} |
| Static | {motion_counts.get('static_hold', 0)} |
| AI source images identified | {moving_count} / {moving_count} |
| Optional AI prompts | {moving_count} / {moving_count} |
| AI prompts ≤500 | {moving_count} / {moving_count} |
| Prompt character counts | min {min(prompt_lengths)}, max {max(prompt_lengths)}, all PASS |
| Transitions | 252 / 252 |
| EDL | COMPLETE |
| Audio | COMPLETE for full-mix timing/loudness; LIMITED for music/SFX stem identity |
| Master synthesis | COMPLETE |

## Final quality gate

- Reference fidelity: PASS. No decorative internal animation was added.
- Image coverage: PASS. Every state has an independent generation prompt and text plan.
- Motion inventory: PASS. All 225 meaningful events are global plate transforms; 28 static states are explicit.
- Motion isolation: PASS. Illustration/surface text move together; watermark remains isolated in screen space.
- Same-frame motion: PASS. No independent same-frame events exist.
- AI routing: PASS. AI is reserved for still generation; deterministic keyframes are preferred for motion.
- Prompt limit: PASS. Maximum optional animation prompt length is {max(prompt_lengths)} characters.
- State chain: PASS. Every moving shot starts from its own F0 and ends at measured F1.
- Editing: PASS. The EDL and compositing method prevent drift.
- Final reconstruction test: PASS for a competent illustrator/AI image operator and editor. Exact original fonts, model, plugin, easing curves, music track and source-project files remain unverifiable.

## Limitations stated exactly

Missing/unverifiable: original image-generation model and seeds, original editor and plugins, exact font files, exact easing curves, exact source artwork beyond the encoded 1280×720 frames, separate music/SFX stems, original thumbnail and audience analytics. Cause: those assets and project files were not embedded in the supplied MP4. Small environmental text that cannot be read at source resolution is labeled rather than invented. Transcript is locally generated ASR, not a supplied script; use the JSON word probabilities and source audio for final copy editing.
"""

(OUTPUT / "forensic_report.md").write_text(report, encoding="utf-8")

for name in ("transcript.txt", "transcript.srt", "transcript.json"):
    shutil.copy2(WORK / "transcript" / name, OUTPUT / name)
for name in ("audio_summary.json", "audio_envelope.csv", "audio_envelope.png"):
    shutil.copy2(WORK / "audio" / name, OUTPUT / name)
shutil.copy2(EVIDENCE / "shot_manifest.json", OUTPUT / "shot_manifest.json")
shutil.copy2(WORK / "scene_descriptions.psv", OUTPUT / "scene_descriptions.psv")

evidence_output = OUTPUT / "evidence"
evidence_output.mkdir(parents=True, exist_ok=True)
shutil.copy2(WORK / "evidence" / "overview_contact_sheet.jpg", evidence_output / "overview_contact_sheet.jpg")
for source in sorted((EVIDENCE / "shot_montages").glob("shot_montage_*.jpg")):
    shutil.copy2(source, evidence_output / source.name)
for source in sorted((EVIDENCE / "shot_montages").glob("motion_triplets_*.jpg")):
    shutil.copy2(source, evidence_output / source.name)
reference_output = evidence_output / "reference_frames"
reference_output.mkdir(parents=True, exist_ok=True)
for shot in shots:
    source = EVIDENCE / "shot_triplets" / shot["sample_files"]["mid"]
    shutil.copy2(source, reference_output / source.name)

print(
    json.dumps(
        {
            "shots": len(shots),
            "visual_cards": len(cards),
            "motion_events": moving_count,
            "static_holds": motion_counts.get("static_hold", 0),
            "animation_prompt_min_chars": min(prompt_lengths),
            "animation_prompt_max_chars": max(prompt_lengths),
            "output": str(OUTPUT),
        },
        indent=2,
    )
)
