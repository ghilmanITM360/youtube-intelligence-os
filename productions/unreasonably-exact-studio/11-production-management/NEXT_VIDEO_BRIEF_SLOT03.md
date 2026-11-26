# Next video: initial project brief for Slot 03

**Title (V3 lineup):** *Why Does a Radio Signal Take a Whole Day to Reach Voyager 1?*
**Format:** vertical Short, 1080×1920.
**Status:** BRIEF ONLY. **Production is not started.** It waits for (1) the recorded narration and (2) an owner production directive.

**Why it is next.** In the reusable-first order (playbook §15.5: 07 → 03 → 09 → 05 → 10 → 06 → 04 → 08 → 01), Slot 03 comes right after Slot 07 and reuses the most from it. It also creates the Voyager and DSN-dish assets that Slot 06 (*How Do You Repair Voyager 1…*) needs.

## 1. The story chain (from the working draft)

1. Signal leaves at light speed.
2. It is not slowed.
3. Radio and light are the same kind of wave, at the same speed in near vacuum.
4. The Moon is about 1 s away (the bridge from Slot 07).
5. Voyager has reached about one light-day.
6. A reply doubles the wait.
7. The exact delay changes over time.

Source: `productions/unreasonably-exact-script-rewrite-v3/revised_scripts_v3/SCRIPT_03_VOYAGER_SIGNAL.md` in the GitHub repo (177 words; header `channel: UNREGISTERED`).

## 2. Applicable reusable assets (from `04-shared-assets/` and `05-animation-engine/`)

| Need in Slot 03 | Reuse | Status |
|---|---|---|
| Earth, transmitting | `UE_EARTH_SURFACE_001`, `UE_EARTH_CLOUDS_001`, `UE_EARTH_NIGHT_LIGHTS_001` with the `space.draw_sphere` globe renderer | APPROVED_IN_FILM (Slot 07) |
| The Moon, as the 1-second comparison | `UE_MOON_GLOBE_001`, plus the Slot 07 pulse-to-Moon beat as a visual callback | APPROVED_IN_FILM |
| Signal pulse travelling | `space` light-pulse bead, `photons.py`, `timeline.ModelClock` (compressed model time with a "Slowed down" or "Sped up" disclosure) | APPROVED_IN_FILM (code) |
| A 24 h clock | `stopwatch.draw_stopwatch(value, full=…)`, driven by model time. A 24 h face variant is a small code change | code; reused |
| Deep-space environment | `camera.starfield`, `Layer2_5D` parallax, `common.data_background` | APPROVED_IN_FILM (code) |
| Ruler and scale bar | `space.py` ruler / scale bar | APPROVED_IN_FILM (code) |
| Typography, disclosures, captions | Comic Neue (OFL), the `DISCLOSURES` table pattern, `captions_v2.py` | APPROVED_IN_FILM |
| Sound | Slot 07 synthesized SFX approach (`audio/sfx_v3`, rights-clear) and the mix and automation method (`sound_design_v3.py`) | method reused; music to be decided (see §6) |
| Observatory and telescope | optional cameo (Earth station); the real station is a DSN dish, not an optical telescope | APPROVED_IN_FILM; probably not used |

## 3. Required new assets

| Asset | Owner of the work | Method (Claude–Codex protocol) | Complexity |
|---|---|---|---|
| **Voyager 1 master** (bus, 3.7 m high-gain dish, magnetometer boom, RTG boom) | Codex (art) + Claude (tests) | Reference sprint on NASA/JPL Voyager photos and models (public domain). One master run with `-i` 2–3 refs, then layer cuts (dish, booms) by editing the master | M |
| **Deep Space Network 70 m dish** (Goldstone or Canberra) master + layers (dish, mount) | Codex + Claude rig (elevation pivot, measured) | Master, then layer cut; rig JSON like RIG_002 | M |
| Vertical light-time ruler (1.3 s Moon, 8.3 min Sun, ~4 h Neptune, ~24 h Voyager) | Claude (code) | New `graphs` or `space` primitive; one label per beat (playbook §15 phone-first rule) | S |
| Radio-wave vs light visual (same wave, same speed) | Claude (code) | Wavefront or EM-strip primitive in `optics.py` / `photons.py` | S |
| Day/night "tomorrow" cue | Claude (code) | Earth terminator rotation (existing `lon0` spin) | S |

## 4. Scientific research requirements (verify at gate G0, before shot design)

1. **The light-day milestone (time-sensitive).** The draft says "In November 2026, NASA confirmed that Voyager 1 had reached one light-day from Earth." This needs a primary NASA/JPL source with the date, and a note on whether the figure is Earth or Sun distance. The script itself already says "Check mission distance again before release."
2. **One light-day** is 299,792.458 km/s × 86,400 s ≈ **25.90 billion km**. The draft says "nearly twenty-six billion kilometres", which needs checking against the measured distance on the release date.
3. **The round trip** is about 2 days, plus the spacecraft's turnaround and processing time. The draft already says "any time spent preparing the reply adds to the wait".
4. **Radio vs light speed.** Both are electromagnetic waves, effectively at c in the interplanetary near-vacuum. Note that plasma dispersion is negligible for this point. Sources: NASA EMS pages (the draft cites them).
5. **Why the delay changes:**
   - Earth's orbit changes the distance by up to about ±1 AU, roughly ±8.3 light-minutes;
   - Voyager recedes at about 17 km/s.
   Both need sourced figures.
6. **Comparison rungs** for the ruler: Moon about 1.28 s (Slot 07, claim C01), Sun about 8.3 min, Neptune about 4 h (at the release date's geometry).
7. All of these go into a `SCIENTIFIC_CLAIMS_LEDGER.csv`, in the same format as Slot 07, with each claim's source, value and on-screen wording.

## 5. Potential animation systems

- **Light-time ruler push.** A vertical ruler with a nested or broken scale, one rung per beat. The camera rides `Layer2_5D` from Earth up the ruler, and the disclosure "Not to scale" appears once when it begins. The Moon-to-Voyager ratio is about 67,000:1, so no literal trail is possible (playbook §15).
- **Model-clock pulse.** The pulse position is a pure function of model time, and the 24 h clock reads model time. A self-check asserts that the clock reads 24 h when the pulse arrives, in the same way as the P11 stopwatch assert.
- **Reply bounce.** A second pulse returns, and the clock continues to about 48 h. The point that "Any time spent preparing the reply adds to the wait" is a visible gap.
- **DSN dish rig.** The dish slews in elevation (measured pivot, monotonic slew, no overshoot), using the P04 observatory rig pattern.
- **Voyager in black space.** A slow parallax drift; the high-gain dish points to Earth.
- **The Slot 07 callback.** The 1.28 s laser beat, in the same visual language, as the "a little over a second" rung.

## 6. Narration requirements

1. The **script must be approved** first. It is a working draft: science, read-aloud and production approval are all pending.
2. A **human recording**, in WAV of 44.1 kHz or more, is delivered before shot design. **No picture timing is designed on estimates** (lesson from Slot 02 V14).
3. **Word timestamps** come from whisper.cpp (Slot 02 method). The beat map follows the Slot 07 `NARRATION_BEAT_MAP.csv` columns.
4. **Length.** The V3 lineup estimates 1:11 at 150 wpm before pauses; playbook §15 estimates about 97 s.
5. **Music.** Decide before the mix: either a track with licence evidence on file, or no music (the Slot 02 approach). If an unlicensed track is supplied again, the same two-master rule applies.

## 7. Production complexity

- **Class: S (small).** There is no character and one idea (playbook §15 table).
- **New art:** two master families (Voyager, DSN dish). Everything else is library reuse or code.
- **Estimate [E]:** about one production day after narration lock, with a single owner review round, if the reference sprint and the Codex masters run on day one.
- **Risks:**
  - the time-sensitive distance claim;
  - label-heavy ruler beats on a phone;
  - Voyager hardware accuracy, since antenna and booms are often drawn wrong.

## 8. What happens next

When the owner sends the narration and a production directive, start at playbook §14, phase 1, plus §21.2: reference sprint, Codex masters, proofs, cut. Until then, do nothing beyond this brief.
