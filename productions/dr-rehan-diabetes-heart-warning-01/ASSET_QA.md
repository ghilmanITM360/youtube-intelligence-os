# Asset QA log

Review is AI visual/evidence review, not owner or clinician approval. Full AV QA impossible without MP3. Native SVGs remain editable. Medical source mapping is in MEDICAL_CLAIMS_QA.md.

- S01: reviewed 360×640 states A/B. Fixed caption/background collision using quiet caption fields. Home set, concerned expression, attached hand at chest and symptom lines readable. Emergency-help panel accompanies acute concern. No glucose/ECG results. Grammar comparison CE01/02/03: furnished plate, simple expressive figure, minimal change between states. PASS with owner/art direction pending.

Automated check: tools/validate.py checks existence, dimensions, alpha, source hashes, layer IDs, duplicate IDs, storyboard/map agreement, file-size ceiling, prohibited audio/video and focused credential patterns. It does not establish medical correctness or exhaustive secret scanning.
