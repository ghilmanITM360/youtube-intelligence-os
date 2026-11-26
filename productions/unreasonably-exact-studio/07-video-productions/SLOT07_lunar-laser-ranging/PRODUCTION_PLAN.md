# Production plan: Slot 07

## Facts about the recording (MEASURED)

- 92.53 s, 245 words, 35 phrases, 30 sentences, 24 kHz mono. Overall 159 wpm, but bursts of about 236 wpm between 34 pauses (12 of them 1.0 s or longer, longest 1.41 s). It is a **generated** voice, not the owner's.
- No lead-in (first word at 0.01 s). Film length proposed: 0.5 s head pad + 92.53 s + 1.5 s tail = **about 94.5 s**, which matches the playbook's S-class Short (about 95 s).
- Two ASR decodes give identical words. Word times from them disagree by 0.64 s median and clump at phrase starts, so `tools/align_slot07.py` uses audio-energy phrase edges (+-0.02 s) and estimated word edges (+-0.12 s).

## Gates (playbook section 18.4): definitions only

G0 Contract, G1 Narration (human listen), G2 Animatic (watched at phone size, owner approves), G3 Asset tests, G4 Rig proof, G5 Look-dev, G6 Science proof, G7 Audio proof, G8 Full render. **Whether a gate has passed is recorded only in `MASTER_PRODUCTION_DASHBOARD.md`.** Mapping of gates to files and human steps: `MASTER_STANDARDS_CROSSWALK.md` section 2.

## Owner decisions (SETTLED 2026-11-26; none blocks research)

1. **Voice**: the supplied generated narration is the production timing reference; original WAV preserved. The human listening check (G1) is still mandatory before publication and is **NOT PERFORMED**.
2. **C06**: keep the recorded wording with the approved visual clarification (footprint inset at B20, binding).
3. **B29b**: keep it, it is in the recording.
4. **Scale**: a clearly identified not-to-scale Earth-Moon schematic is allowed where necessary.
5. Web, browser, image-reference research and Codex coordination are authorised; ordinary research and planning decisions are not re-asked.

Still open for the owner (do not block research): the caption band / safe-area criteria (G5), and the approval of the beat map, **illustrated** storyboard and manifest for G0.

## Order of work (stable plan; progress is in the dashboard)

1. Close reference gaps for the nine asset families; professional animation study (HumanCraft method).
2. Look-dev (vision card, three treatments, one chosen language) and ANIMATIC_V1_REFERENCE_INFORMED.
3. Complete the 34 Codex briefs (16 mandatory fields, assembly diagrams, path-audited).
4. Contact Codex (computer use), Batches 0-5 in `CODEX_HANDOFF.md`; verify actual outputs after each batch.
5. In parallel, Claude builds the procedural components (`animation/uemotion`) and the code-only proofs.
6. Rigs and proofs P01-P13; failing proofs are repaired before the scene enters final production.
7. Scientific and creative QA (HumanCraft scorecard), full assembly, audio, captions, review.

## Estimates (ESTIMATE, not forecast, from the playbook section 19)

Class S Short: about 1-2 working days of agent work after the shared library exists, 2 owner review rounds.
