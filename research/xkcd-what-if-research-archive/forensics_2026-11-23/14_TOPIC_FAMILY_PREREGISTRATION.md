# 14 Topic-family holdout: preregistration (written 2026-11-23 BEFORE any per-family metric was computed)

Author: main session (same model family). Not independently witnessed; the file hash recorded in `14_TOPIC_FAMILY_HOLDOUT.md` fixes its text.

**Families** are assigned mechanically from the video TITLE by the first matching rule (regex, case-insensitive), in this order; no manual re-assignment after seeing results:
1. HUMAN_BODY: `human|dna|eat |eating|cannibal|survive|swim|nuclear (storage|fuel)`
2. SPACE: `moon|\bsun\b|sun.s|space|hubble|tatooine|sunset|mars|planet|wise men|black hole|visible light`
3. EARTH_WATER: `earth|ocean|water|quake|magnitude|rotat|land mass|mariana|dig|niagara|lightning|trench|sky|world|country|climate|circumference|antimatter`
4. MACHINE_OTHER: everything else.
Rows with format UNCLASSIFIED are dropped. Long and Short are analysed separately.

**Hypotheses (from the rule ledger) and acceptance bands** (family value vs the pooled value of the OTHER three families, leave-one-family-out):
- P1 (K04) words per total second: a family's median within +-15% of the rest. Long and Short separately.
- P2 (K01) opens with an attributed question: >= 80% of long scripts in each family with n >= 5.
- P3 (K09) hold share of frames: a family's median within +-5 percentage points of the rest.
A family with n < 5 videos for a metric is reported but NOT judged. A failure is recorded as a failure, not re-banded.

**Limits fixed in advance:** title keywords are a crude proxy for topic; families overlap with reuse families (a long video and its Shorts share a topic and are not independent); same coder family; this is a stability check across topic strata, not an independent holdout.
