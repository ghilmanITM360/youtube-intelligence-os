# Claude–Codex asset production protocol

**Version 1.0 · 2026-11-26 · written from the Slot 07 production record.** Every command and number below comes from the Slot 07 files named next to it: `07-video-productions/SLOT07_lunar-laser-ranging/`, shortened to `S07/`. Anything not tried in Slot 07 is labelled **PROPOSED**.

**Purpose.** A Claude session can commission, check and correct artwork from Codex **without the owner copying prompts between apps**. Claude writes the brief and starts Codex from the shell. Codex draws. Claude measures the result and accepts or rejects it.

**Roles.**
- **Claude** is the art director, compositor and rigger. It writes briefs, picks references, runs every acceptance test, cuts and registers layers, measures pivots and builds rigs.
- **Codex** is the illustrator. It produces one image per run with its built-in `image_gen` tool.
- **The owner** approves the art as seen in a film. Codex never self-approves, and Claude never marks owner approval.

---

## 1. Codex CLI discovery and version compatibility

Two Codex binaries existed on this Mac. **Only one of them works with the configured model.**

| Binary | Version (`--version`, 2026-11-26) | Works? |
|---|---|---|
| `codex` on PATH (`~/.local/bin/codex`) | `codex-cli 0.153.4` | **No.** It is too old to use the configured model. |
| Bundled with the ChatGPT app: `/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex` | `codex-cli 0.171.0-alpha.13.2` | **Yes.** All 16 successful Slot 07 runs used it. |

Check both before the first run of a session:

```bash
which codex; codex --version
C=/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex; $C --version
$C exec --help | grep -E -- '-i, --image|-c, --config|-C, --cd|-s, --sandbox|--skip-git-repo-check'
```

Each run log's header records the binary, model and settings, so the log proves what actually ran. Example from `S07/codex_handoff/runs/B5PR2/codex.log`:

```
OpenAI Codex v0.171.0-alpha.13.2
workdir: …/SLOT07_lunar-laser-ranging/codex_handoff
model: gpt-6.1-terra   provider: openai   approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: high
```

**Do not use the computer-use GUI to drive Codex** when the CLI is available. The CLI is reproducible and logged, and it needs no screen control. Slot 07 Batch 0 used the CLI because the GUI tool was not available (`S07/CODEX_PROGRESS.csv`).

## 2. Model and reasoning-effort configuration

- **Model.** `~/.codex/config.toml` sets `model = "gpt-6.1-terra"`. Leave it there; do not pass `-m` unless the owner changes the model.
- **Reasoning effort.** The same config file sets `model_reasoning_effort = "low"`. That default was one root cause of the failed early batches (root cause **R3** in `S07/ASSET_GENERATION_FAILURE_ROOT_CAUSE_AUDIT.md`). **Every art run overrides it:** `-c model_reasoning_effort="high"`.
- **Reading the config.** Read only the keys you need, for example `grep -E '^(model|model_reasoning_effort) ' ~/.codex/config.toml`. **Never print, copy or commit the whole file or `~/.codex/auth*`.** They can hold account tokens. Run logs contain paths and prompts, not credentials, but check before committing any log.

## 3. The run command (verified)

Two forms were used in Slot 07, and both are reproducible.

**Form A, the helper script** `S07/tools/codex_run.sh`. It also exists in `05-animation-engine/codex/`.

```bash
tools/codex_run.sh RUN_ID "brief text" ref1.png [ref2.jpg ...]
# expands to:
cd codex_handoff && mkdir -p runs/RUN_ID && \
/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex exec -C . \
  -c model_reasoning_effort="high" --skip-git-repo-check -s workspace-write \
  -i ref1.png -i ref2.jpg -- "$(cat runs/COMMON_RULES.txt)

brief text" < /dev/null > runs/RUN_ID/codex.log 2>&1
```

**Form B, parallel runs from brief files**, used for R2a, B3M, B4M and B5M, four at once. This is taken from the session transcript:

```bash
run(){ id=$1; shift; f=runs/$(ls runs | grep "^${id}_" | head -1)
  nohup $C exec -C . -c model_reasoning_effort="high" --skip-git-repo-check -s workspace-write "$@" \
    -- "$(cat runs/COMMON_RULES.txt; echo; cat $f)" > runs/$id/codex.log 2>&1 < /dev/null & echo "$id pid $!"; }
run B4M -i references/observatory/observatory_apo-3p5m-apollo-ranging_night-exterior_wikimedia_d70050914-15.jpg \
        -i references/observatory/observatory_vlt-ut-enclosure_bi-parting-leaves-open-day-exterior_wikimedia_paranal-opendome.jpg \
        -i references/observatory/observatory_wiyn-3p5m-enclosure_dusk-exterior_noirlab_wiynsunset.jpg
```

Each flag has a reason:

| Flag | Why |
|---|---|
| `-C .` inside `codex_handoff/` | Codex sees the references, guides and its own `runs/` folder, not the whole project. |
| `-s workspace-write` | Codex may write inside the work directory and temp only. |
| `--skip-git-repo-check` | The workspace is not a git repository. |
| `-i FILE` (repeatable) | Attaches reference images. This was the fix for root cause **R1**, where no reference image reached the generator. |
| prompt after `--`, stdin `< /dev/null` | Prevents Codex from waiting on stdin. The log shows "Reading additional input from stdin..." and then continues. |
| `nohup … &` with one log per run | Up to four runs ran in parallel. Each took 1–4 minutes (file times, `S07/codex_handoff/runs/`). |

Each Codex log shows `hook: SessionStart Failed` and `hook: UserPromptSubmit Failed`. These come from the user's own Codex hook setup. **They did not block any run**, so ignore them unless a run stops early.

## 4. Single-deliverable task design

**The rule: one run produces one deliverable.** It may be several layers, but only when they are cut from the same canvas in one stated operation.

The evidence:
- Batches 0, 0b, 1 and 2 were multi-asset runs. Each asked for research, three or four images and nine documents at reasoning effort `low`. They produced **zero approved images**.
- The 16 single-deliverable runs that followed (R2a, B3M, B4M, B5M, B5L, R2b, B1c, B5L2, B4L, B4L2, B4P, B5C, B5P, B5PA, B5PR, B5PR2) produced **13 usable candidates and 3 rejects**. Seven of them supplied artwork that is in the final V3 film.

Every prompt is `COMMON_RULES.txt` followed by one brief. `S07/codex_handoff/runs/COMMON_RULES.txt` is reproduced in `09-production-templates/codex-handoff/COMMON_RULES_TEMPLATE.txt`. Its seven rules:
1. Call `view_image` on every attached reference first.
2. Use `image_gen`, in **edit mode on the master** whenever a master exists.
3. Draw one view of one subject. No insets, no reference sheet, no text.
4. Produce a native size only.
5. Follow the stated style, with one sun at the upper left.
6. Run the validator. If it fails, make **at most one** edit that names only that defect.
7. Write only inside your run folder, plus a NOTES.md of at most 12 lines. Do not judge acceptance.

The brief, saved as `runs/<ID>_<NAME>.txt` or passed inline, always states:

| Field | Example (run B4L2) |
|---|---|
| Deliverable path, transparency, canvas | `runs/B4L2/obs_building_slit_open.png`, transparent, 1024x1536, SAME canvas/position as `OBS_building_closed_candidate.png` |
| The single defect or goal, with Claude's evidence | "the building layer's dome is CLOSED, so the telescope layer is hidden" |
| What to change and what to keep | "cut the vertical slit … keep everything else pixel-for-pixel" |
| The acceptance test Claude will run | IoU vs the closed layer, slit open and dark |

**Wording rules,** from root causes R4–R6, R11 and R14:
- Never write "the same as" or "matching". Attach the image instead and say "redraw THIS object".
- Never ask for numbers the generator cannot measure, such as "tilted 30°" or "apex at centre". Give a **construction guide image** instead, for example `guides_construction/RETRO_004_side_guide_23deg.png`.
- Ask only for native sizes: **1254x1254, 1536x1024 or 1024x1536**. A request for 1024x1024 arrived as 1254x1254 (run B5C).
- Generate small parts on their **own tight canvas**, never as a small object on a large empty canvas. Run B5L2 failed that way, with no alpha 0 anywhere on the canvas.
- Do not ask an image model for measurements (pivots, recess centres) or for geography (coastlines). Claude measures. Maps come from NASA data.

## 5. Reference-image attachment

1. **Collect the real evidence before any generation.** Slot 07 saved 173 references; `S07/research/REFERENCE_MANIFEST.csv` has 150 with local files. Each reference is indexed with its source URL, licence and what it influences (`S07/codex_handoff/references/<family>/REFERENCE_INDEX.md`).
2. Attach **2–3 decisive photographs** per run with `-i`, not the whole folder.
3. **Verify the references were inspected.** Count `view_image` in the log before reading the result:
   ```bash
   grep -c view_image runs/<ID>/codex.log     # Slot 07 runs: 2-5 per run; 0 means reject unread
   ```
   NOTES.md must also have one line per reference saying what was seen in it.
4. References are **reference use only**. Several are CC BY-SA, such as the Wikimedia observatory photos, and they never appear in a film. NASA photos are public domain.

## 6. Master-image editing workflow

1. **Make the master first.** Produce one approved master per object or environment: B4M (observatory), B5M (astronaut), B3M (lunar terrain), B5P (astronaut carrying the reflector, as one composition).
2. **Derive every other view or layer by editing the master.** Load it with `view_image`, then call `image_gen` in edit mode on it. Text-only regeneration made each view reinvent the hardware (root cause **R2**).
3. **Cut layers from the master canvas.** Use the same size and origin, and paint the hidden areas. Examples: B4L (building, telescope, leaves, ridge), B4P (sky plate), B5L (torso and two arms with overlap sleeves), B5PA/B5PR (astronaut only, reflector only).
4. **Generate interactions as one composition, then cut one layer per run** (lesson R15).

## 7. Output directory organisation

```
codex_handoff/
  runs/COMMON_RULES.txt         the fixed rules prepended to every prompt
  runs/<ID>_<NAME>.txt          the brief (form B)
  runs/<ID>/                    Codex writes ONLY here: deliverable PNG(s), NOTES.md
  runs/<ID>/codex.log           full log (header = binary/model/effort; view_image/image_gen calls)
  runs/_rejected/<ID>_<file>    Claude moves failed deliverables here (never deleted)
  references/<family>/          real-world evidence + REFERENCE_INDEX.md
  guides_construction/          Claude's construction guides, defect evidence, promoted candidates
  deliveries/batch*/            the early multi-asset batches (historical)
assets/rigs/<rig>/              Claude-promoted layers + RIG_xxx.json (what the film loads)
```

**Run IDs:**
- `B<batch><family letter>` for masters and layers: M = master, L = layers, P = plate or pose, C = component.
- `R<n><letter>` for repairs.
- A suffix `2` marks a one-defect correction of the run with the same name.

## 8. Generation logs

Claude reads three things before looking at the image:
1. the log header (binary, model, reasoning effort);
2. the `view_image` count;
3. NOTES.md (native size, assumptions, validator output).

A run with no `view_image`, or with the wrong effort level, is rejected unread.

**Record every verdict.** The verdict goes in the run-results tables of `S07/ASSET_GENERATION_FAILURE_ROOT_CAUSE_AUDIT.md`, plus `S07/CODEX_PROGRESS.csv` and `S07/ASSET_GENERATION_TRACKER.csv`. **PROPOSED:** keep one row per run in a single `qa/codex_runs.csv` (run, ask, Claude-measured result, verdict, where used). In Slot 07 the record is split across three files.

## 9. Artwork acceptance tests (Claude runs all of them; the result is the verdict, not Codex's self-report)

| Test | Tool / threshold | Source |
|---|---|---|
| Format and alpha | `python tools/validate_asset.py FILE --canvas WxH` checks: RGBA; four corners alpha 0; RGB under zero alpha; semi-transparent share; one large component | `05-animation-engine/validators/validate_asset.py` |
| Stray pixels | view on a **magenta backing** at full size | root-cause audit, "my own inspection" |
| Layer registration | silhouette **IoU ≥ 0.97** vs the master or candidate. Restacked layers must be coherent (mean abs diff < 3/255 inside the master alpha) | lessons R12, R15; B5L 0.978, B4L2 0.992, B5PA/B5PR restack 0.983 |
| Geometry | measure angles on the alpha, **±3°** of target (RETRO_004: 23.6° vs a 23° guide) | R5, R10 |
| Count and placement | count repeated features; never trust Codex for them (the 10×10 cubes came out 9×9) | R16 |
| Rig | rotate each part ±25° about its pivot in a rendered moving test. No gap or tear (P05 near shoulder: worst 86 px of 15,361) | R8, R17 |
| In-shot | render the proof clip and review the moving output, not a still | `S07/renders/proofs/*/PROOF_REPORT.md` |

Verdict labels: `CANDIDATE` (passes Claude's tests), `REJECTED` (moved to `runs/_rejected/`), and `APPROVED_IN_FILM` (used in a film the owner accepted). Only the owner turns art into "approved".

## 10. Correction loops

1. Write **one edit per defect**. Name the defect, attach Claude's evidence image, and say what must not change.
2. **After every edit, re-measure all earlier passes**, not only the named defect. Run R2b fixed the base but broke the tilt (23.6° became 14.7°); that is lesson R13.
3. If a one-defect edit makes Codex redraw the whole object, stop asking Codex. Run B5PR2 scored IoU 0.327. **Composite the detail in code from an already approved part** (lesson R16: Claude placed the 100 cube instances itself).
4. **Before commissioning corrective art, test whether it is really a rig problem** (lesson R17). The P05 shoulder gap was fixed by rig v2 skinning, which made the B5C shoulder piece unnecessary.
5. **Repair the single defect; never regenerate a whole asset family for one defect.** Accept small deterministic repairs in code, such as re-centring by translation or an alpha erode, and document them. The source file stays untouched.

## 11. Registration and rigging handoff

Claude, not Codex, produces the rig data, measured on the delivered layers. An extract from the format, as used in `S07/assets/rigs/observatory/RIG_002_observatory.json`:

```json
{"rig": "RIG_002_TELESCOPE_DOME",
 "note": "All layers share one 1024x1536 canvas (Codex runs B4M master, B4L layers, B4L2 slit-open building, B4P plate). Pivots measured by Claude 2026-11-26.",
 "layers": {"plate": {"file": "obs_sky_mountains_plate.png", "source": "Codex B4P", "z": 0},
            "telescope": {"file": "obs_telescope.png", "source": "Codex B4L", "z": 35, "pivot_altitude": [490, 920],
                          "aperture": [590, 700], "tube_lean_deg_in_file": 24.4, "clip": "slit mask"}},
 "slit": {"centre_x": 492, "rows": [633, 1000], "half_width_at_960": 103}}
```

Every layer records:
- its file;
- its source run;
- its z-order;
- its pivot or offsets, in canvas pixels;
- any clip mask.

The rig is promoted into `assets/rigs/<name>/` only after the proof clip passes. The proof clips were P04 for the observatory, P05 for the arms and P06 for the carry.

## 12. Session checklist (copy into the run brief folder)

- [ ] Use the bundled CLI, version checked; the PATH `codex` does not work with the configured model.
- [ ] Pass `-c model_reasoning_effort="high"` on every run.
- [ ] Attach 2–3 decisive references with `-i`, indexed with source and licence.
- [ ] Commission the master first; every derivation is an edit of the master.
- [ ] One deliverable per run, native size, tight canvas for small parts.
- [ ] `grep -c view_image` > 0, read NOTES.md, run the validator, check on magenta, measure.
- [ ] Record the verdict. Move rejects to `_rejected/`, never delete them.
- [ ] One defect per correction; re-measure earlier passes afterwards.
- [ ] Claude measures pivots and writes the rig JSON; run a moving rig test before use.
- [ ] Never print or commit Codex config or auth files.
