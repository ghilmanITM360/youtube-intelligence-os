import pathlib, markdown
ws = pathlib.Path(__file__).resolve().parents[1]
css = "body{font-family:system-ui,sans-serif;max-width:1000px;margin:24px auto;padding:0 16px;line-height:1.5;color:#1a1a1a}table{border-collapse:collapse;width:100%;font-size:14px;margin:12px 0}th,td{border:1px solid #ccc;padding:6px 8px;vertical-align:top;text-align:left}th{background:#f1f1f1}code{background:#f4f4f4;padding:1px 4px}h1,h2{border-bottom:1px solid #ddd;padding-bottom:4px}a{color:#0b5cd5}"
src = (ws/"audit_strict/STRICT_STATE_AUDIT_2026-11-19.md").read_text()
body = markdown.markdown(src, extensions=["tables"])
(ws/"audit_strict/STRICT_STATE_AUDIT_2026-11-19.html").write_text(f"<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><title>Strict State Audit</title><style>{css}</style><p><a href='../START_HERE.html'>&larr; START HERE</a></p>{body}")
S = ws/"readable/site"
def L(f, t): return f"<li><a href='readable/site/{f}'>{t}</a></li>"
secs = [
("Pehle yeh padho (audit)", [("../audit_strict/STRICT_STATE_AUDIT_2026-11-19.html","Strict State Audit - abhi ki haqeeqat, folder by folder, final table"),
 ("audit__19_FINAL_ACCEPTANCE_REPORT.html","Pichla audit: aakhri faisla (55.5/100, REJECTED)"),
 ("audit__18_GAP_ANALYSIS_AND_CORRECTION_PLAN.html","Gap aur correction plan"),
 ("audit__02_REQUIREMENT_TRACEABILITY_MATRIX.html","36 hidayaat: hui ya nahi")]),
("Six channels", [("02_FINANCE_CHANNEL_MASTER_INVENTORY__MASTER_INVENTORY.html","Channel inventory"),
 ("03_PRIMARY_REFERENCE_CHANNELS__STRENGTH_MATRIX_AND_LEARNINGS.html","Six channels ki strength matrix"),
 ("05_FRESH_COMPETITOR_DATA__REFRESH_STATUS_AND_MISSING_DATA.html","Data refresh aur jo missing hai"),
 ("audit__04_FINANCE_CHANNEL_COVERAGE_AUDIT.html","Coverage audit")]),
("Topics", [("09_TOPIC_DISCOVERY__TOPIC_VALIDATION_ROUND1_2026-11-18.html","Topic round 1"),
 ("17_TOPIC_VALIDATION__PHASE_TEN_FINAL_TOPIC_VALIDATION_2026-11-18.html","Final topic validation"),
 ("17_TOPIC_VALIDATION__L3_L4_VALIDATION_2026-11-19.html","L3/L4 validation"),
 ("09_TOPIC_DISCOVERY__PRIMARY_DATA_PULL_2026-11-18.html","Sarkari sources se numbers")]),
("Calendar, packaging, strategy", [("19_30_DAY_CONTENT_CALENDAR__PHASE_ELEVEN_30_DAY_CALENDAR_2026-11-18.html","30 din ka calendar"),
 ("19_30_DAY_CONTENT_CALENDAR__P0_FIX_CALENDAR_ADDENDUM_2026-11-19.html","Calendar addendum"),
 ("18_CONTENT_PACKAGING__PHASE_NINE_TOPIC_TITLE_THUMBNAIL_PACKAGING_2026-11-18.html","Title/thumbnail packaging"),
 ("23_FINAL_STRATEGY__FINAL_STRATEGIC_RECOMMENDATION_2026-11-18.html","Final strategy")]),
("Draft scripts (gate WARN)", [("productions__new-finance-channel-v1-rent-01__V1_RENT_SCRIPT.html","V1 Rent"),
 ("productions__new-finance-channel-v2-airfares-01__V2_AIRFARES_SCRIPT.html","V2 Airfares"),
 ("productions__new-finance-channel-l3-jobs-01__L3_JOBS_SCRIPT.html","L3 Jobs")]),
("Records", [("DECISION_LOG.html","Decision log"),("RESEARCH_CHANGELOG.html","Changelog"),("index.html","Poora reader (61 pages)")]),
]
h = "".join(f"<h2>{t}</h2><ul>"+"".join(L(f,x) if not f.startswith("../") else f"<li><a href='{f[3:]}'>{x}</a></li>" for f,x in items)+"</ul>" for t,items in secs)
(ws/"START_HERE.html").write_text(f"<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><title>New Finance Channel - START HERE</title><style>{css}</style><h1>New Finance Channel - START HERE</h1><p><b>Haal:</b> 55.5/100 pichle audit mein; strict audit ke mutabiq six channels mein se 0 poori tarah analyse hue, 0 topics fully validated. Corrections aapki approval ka intezar kar rahi hain.</p>{h}")
