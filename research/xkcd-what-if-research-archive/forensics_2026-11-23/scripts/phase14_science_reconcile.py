"""Phase 14 reconciliation of science rows after the Codex independent review (F04, F05, F10, F11). Adds two columns to the claim CSVs
(independent_check_2026_11_23, reconcile_note_2026_11_23) and revises SC02 / E09g rows. Pre-edit copies live in versions_before_reconcile_2026-11-23/.
usage: python3 -I scripts/phase14_science_reconcile.py (idempotent from the backed-up originals)"""
import csv, os
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = A + '/versions_before_reconcile_2026-11-23/'
def load(n): return list(csv.DictReader(open(V + n)))
def save(n, rows):
    w = csv.DictWriter(open(A + '/' + n, 'w', newline=''), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
CODEX = {
 'SC02': "CODEX PARTIAL (hand calculation 5.95337 g at constant density; read /67/): AGREE that 5.95 is below a literal 'over 6'. Article text (re-read here): 'over six gees' at t=100 years; footnote [10] says Earth material would compress under its own weight, so gravity grows slightly faster than a constant-density estimate. Self-compression is not modelled here.",
 'SC03': "CODEX PARTIAL (899 kWh/month -> 106.3 MJ/day, 212.6 MJ for two days, US-average assumption): AGREE that OPEN is defensible; flash total, ground-delivered and recoverable energy differ; original audio and source not checked.",
 'SC05': "CODEX PARTIAL (equations reproduce 1.995e42 J and 1.738e41 J; Sun models 2.28e41 / 5.70e41 J): AGREE relation-dependent; M25 is far outside any earthquake experience.",
 'E09g': "CODEX PARTIAL (read /13/: 'five petawatts' and 'double the world's average electricity'; IEA 2012 chart about 19,550 TWh = 2.23 TW): AGREE on the wording discrepancy; audio not listened to; intended correction not inferred.",
}
NOTE = {
 'SC02': "RECONCILED: verdict changed CONSISTENT_WITH_CAVEAT -> QUALIFIED. (1) Constant-density model: 5.953 g, i.e. 0.8% below 6.00; 'approximately 6 g' is supported, the literal claim 'over 6 g' is NOT reproduced by this model. (2) The original article says 'over six gees' and its footnote says compression under self-weight raises gravity above the naive estimate; that effect is not computed here, so the model cannot refute the article's literal wording either. (3) The on-screen '6G' label matches the rounded value. Open: a self-compression model (e.g. a polytrope with the Earth's compressibility) to see whether g exceeds 6.00.",
 'SC03': "RECONCILED: unchanged OPEN_DEFINITIONS_ORIGINAL_SOURCE_REQUIRED. Quantity must be named (total flash energy / energy delivered at ground / recoverable electricity); household basis 899 kWh/month US average is an assumption; the spoken wording is ASR/catalog only; no original-source comparison. See 07_SC03_LIGHTNING_REWORK.md.",
 'SC05': "RECONCILED: both magnitude-energy relations and both Sun binding-energy models reproduce independently (Codex). They are TOY extrapolations: the relations apply to different magnitude types (Gutenberg-Richter Ms versus energy-magnitude Mw) and were fitted to earthquakes of magnitude at most about 9.5; M25 is 15 magnitude units beyond. The result flips (above or below the Sun's binding energy) with the relation chosen, so no physically definitive solar outcome follows and none is claimed.",
 'E09g': "RECONCILED: article and ASR agree on 'five petawatts' and 'double the world's average electricity'. Arithmetic: 5 PW = 5,000 TW. Article-era (2012) world electricity as average power: about 2.2 TW (IEA chart read by Codex, 19,550 TWh), about 2.5 TW (EIA net generation 21.6 PWh) and about 2.6 TW (UN yearbook 22,695 TWh; EIA and UN figures from search summaries, not read in full), so 5 PW is about 1,900 to 2,250 times the average; with the modern 2023 figure used earlier (3.36 TW) it is 1,486 times, an era mismatch. Under none of these is it 2x. 5 TW would be about 2x, an arithmetic observation, NOT a claim about what the authors meant; units need the authors' confirmation. Video audio not listened to.",
}
for name in ('07_SCIENCE_CLAIM_CHECKS.csv', '07e_EPISODE_CLAIM_CHECKS.csv'):
    rows = load(name)
    for r in rows:
        k = r['claim_id']
        r['independent_check_2026_11_23'] = CODEX.get(k, 'NONE (same-model self-review only)')
        r['reconcile_note_2026_11_23'] = NOTE.get(k, '')
        if k == 'SC02': r['verdict'] = 'QUALIFIED'
        if k == 'E09g':
            r['assumptions'] += '; article-era (2012) benchmarks added in reconcile note'
            r['recomputed'] = 'optical 1.80 PW; at 36% efficiency 5.0 PW; 5 PW = 5,000 TW; 2012 world average electricity about 2.2 to 2.6 TW -> about 1,900 to 2,250x; 2023 (3.36 TW) -> 1,486x; 5 TW would be about 2x'
            r['constants_status'] = 'F+S (2012 EIA and UN totals via search summaries; IEA chart value from the Codex review)'
    save(name, rows)
print('ok')
