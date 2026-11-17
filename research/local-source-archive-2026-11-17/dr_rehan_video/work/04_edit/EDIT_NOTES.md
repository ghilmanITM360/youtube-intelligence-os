# Edit notes (2026-11-02)

## Draft v4: new hook (`renders/draft_v4.mp4`, 6:45.3, −14.1 LUFS)
- **Opening:** on a blurred dawn bedroom, a big monitor number rolls DOWN 158 → 72 and lands under "You're": the falling reading turns out to be her age. It then flashes white and punches in, and the iris opens onto her hand while the 72 shrinks aside.
- **More drama, faster pace:**
  - punch-ins on BUT and on LOWER;
  - a 12-step camera shake on "the room spins", with a harder plate spin (10°, blur) and a red vignette;
  - SFX: 11 clicks on the roll, a punch on 72 and BUT, a glitch and a boom on "the room".
- **⚠️ DOCTOR CHECK:** the roll numbers (158…72) and the SYS readout (158 → 129) are illustrative, not from Dr. Rehan.
- **Open:** a check contrast flag at 382.8 s (O01) and at 292.7 s (U01). Both are mid-animation text; the settled frames read fine.

## Draft v3: the pictures tell "Two Mornings"
- **Stills:** the 15 approved v3 cast/location images (`02_assets/generated/v3/`). `prep_plates.py` crops them and bakes in the grades, writing to `hf/assets/plates/`; the originals are untouched and their SHA-256 values are printed on every run. The grades are:
  - the dawn look (matched to L1b);
  - VIP `DEEP` for night;
  - VIP `Golden_Years` for the warm morning.
- **Hook (H01), told in pictures:**
  - an eyelid "slit" opens on her hand (ring, watch), and "72" lands;
  - an iris opens into her blue dawn bedroom; the push-in goes toward the bedside monitor while a code-drawn SYS readout ticks 158 → 129 (illustrative numbers);
  - BUT: a VIP red film burn, the VIP punch sound and the boom;
  - "stand up": her window silhouette rises in from below;
  - "the room spins": the plate tilts 6°, smears, and a ghost copy slides off it (double vision);
  - "Even lower? / a second look?": the night hallway, with the light closing in on the curled rug;
  - "After 65": a split screen, the garden ("Protect the heart") against the hallway ("Avoid dangerous drops"), opening from the centre line.
- **The rest of the story:**
  - I01: the GP room behind the titles; Margaret in her coat at the door, then the cuff on her arm.
  - J01: her kitchen, then a dive toward the table and her notebook.
  - J02: her notebook sketch sits, rises and turns dizzy, then the cuff card (⚠️ the J02 line is still a DOCTOR CHECK).
  - B02: the balance over the night hallway, which warms into her sunny bedroom on "fit the person".
  - O01: the MIRROR. The same bedroom and the same framing as the hook; the blue dawn dissolves into warm sun. Then her dizzy sketch next to the three warning signs, and on "better protection" the garden, Lily running and a VIP warm light leak.
- **Motion:**
  - every plate enters through a keyframed mask (slit, iris, wipe-up, pencil "draw", centre-split);
  - every plate has a slow push and a deterministic handheld drift, after the Cinecom "Real Handheld Movement" preset.
- **VIP assets used:**
  - the `DEEP` and `Golden_Years` LUTs;
  - the "Old Film" red burn and the "35mm light leak" (screen blend);
  - the Punch Hole 15 sound and the tmp_glitch_05 sound (kept low).
  - Not used:
    - the glitch *pictures*, which are too digital for this audience;
    - the "Film Overlay Effect" and "VINTAGE Film PROJECTOR" overlays, which have YouTube subscribe watermarks burned in;
    - the Premiere `.prfpset` presets, which can't run here (their moves were rebuilt in GSAP).
- **Not yet generated:** the 41 S story shots. The images above are cast and location sheets, so some are small crops. The hand, window and coat crops are about 400–560 px wide and are shown as cards or behind scrims, not as full-frame hero shots.
- ⚠️ **Licences:** the VIP pack (LUTs, film burns, punch hole, glitch) came from a "free resources" bundle with no licence file. Confirm before publishing.

## Draft v2: what changed since v1
- Transitions (every scene change, 0.9 s):
  - narrator scenes arrive with a soft feathered sweep, a light streak on its edge (red; cobalt in MC scenes), and the type settles out of a zoom-blur;
  - the doctor arrives through a soft radial iris from his face, settling from a 1.12 zoom-blur;
  - the outgoing scene pushes forward and blurs underneath;
  - the END card now sweeps in too (in v1 it was a hard cut).
- Ambient motion in the narrator scenes: two soft light orbs drift, the background slowly pushes in, the grain moves every frame.
- Light 3D:
  - "rise" text tips up from the bottom (rotationX);
  - the DR2/DR5 split cards swing in on Y.
- Sound:
  - whoosh2 was silent in v1 (its sound starts at 1.7 s); it is now cued so its peak lands mid-wipe;
  - a soft whoosh also plays into each doctor segment.
- Captions never join two scenes any more ("…however In plain words" is fixed).
- Asset prompts: 60 blocks (`02_assets/asset_prompts.md`).


Rebuild: `python3 build.py` → `cd hf && npx hyperframes check` → `npx hyperframes render --quality draft -o ../renders/draft_vN.mp4`.
`build.py` holds the whole EDL, every on-screen line and its anchor word; edit text there, not in `hf/compositions/` (those are regenerated).

## Decisions taken by default (change if needed)
- Hook: **H01 (A)**. The alternates B and C are in `03_narration_audio/` but not used.
- J02: "Doctor check" **cut in the edit** (17.95–19.85 s). Not needed if J02 is re-recorded.
- U01 ⚠️ is **in** the draft so the pacing can be judged. It comes out (−39 s) if Dr. Rehan doesn't approve it.

## Trims to Dr. Rehan's recording
- T1 0:58.24–0:59.33 "fall out" false start (masked with a 1.08 cut-zoom).
- T2 (1:29.6–1:32.4) **not touched**. Still needs a listen.

## Sound
- VO normalised to −14 LUFS; the doctor is at −13.2 LUFS (as recorded). The final master target is −14 LUFS / −1 dBTP (not done yet).
- Music bed: "Documentary Cinematic Violin – Life Goes On" (Infraction, user's folder). It drops out 1.5 s before "And never change…" and returns for the subscribe/end card.
- SFX: whoosh on every narrator wipe, a low boom on "BUT", and a riser into the intro.
- ⚠️ **Licences to confirm before publishing:**
  - `ES_*` files are Epidemic Sound (they need an active subscription on the channel);
  - the TENET pack ("free giveaway") has no licence file;
  - Infraction tracks normally need a credit line.

## Known limits (v1, still true in v2)
- No light-3D moment yet, no matte "text behind the doctor", no grain on the footage.
- Captions are Whisper output with hand fixes:
  - hyperlipidemia, INTERHEART, beta blockers;
  - "flexible cardia" is shown as "…" ⚠️.
  - "hybrid" stays as he says it until HYVET is confirmed.
- The handwriting face is macOS "Bradley Hand" (local copy in `hf/assets/fonts/`). Its licence must be checked for publishing, or it should be swapped for Caveat (OFL).
