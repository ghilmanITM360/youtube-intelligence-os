# QA checklist before owner review

Each line needs an evidence file. "Done" without evidence is not done.

**Narration and science**
- [ ] G0 science: every on-screen number is in `SCIENTIFIC_CLAIMS_LEDGER.csv` with a source; the model code asserts it.
- [ ] Narration locked: raw WAV read-only with its SHA-256; word times; beat map.

**Art and rigs**
- [ ] Art: every asset has passed `validate_asset.py`, a magenta check and a measured test; the Codex log shows `view_image`.
- [ ] Rigs: a moving rotation test, with no gap or tear, and pivots in the rig JSON.

**Picture**
- [ ] Opening (G-open): frame-difference check over 0–7 s; no unmotivated hold over 0.5 s.
- [ ] Each mechanism has a proof clip with asserts, and its `PROOF_REPORT.md` shows PASS.
- [ ] Text (G-text): one disclosure table; no persistent badges; minimum type 34 design units.
- [ ] Captions: SRT plus a burned version; collision check; the Shorts-UI safe band.

**Sound**
- [ ] Mix (G-mix): voice-minus-music 18–24 dB in voiced windows; −16 LUFS, ≤ −1 dBTP; a cue sheet with a reason per cue; a rights-clear master built alongside.

**Reviews**
- [ ] Three independent reviews (decoded frames across the whole film; science asserts; ffprobe/loudness/frames), each with its own file.
- [ ] Human gates listed as NOT PERFORMED until the owner does them: listening, real-time viewing, muted-viewer test, licence, acceptance.
