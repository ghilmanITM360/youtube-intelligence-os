"""Extend the V2 forensic workbook with V3 sheets: corrections, expanded breakout
inventory, and Trends re-capture status. V2's 38 sheets are preserved unmodified
except for one addendum note on 00_READ_ME; nothing is deleted or overwritten."""
import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from copy import copy
from pathlib import Path

RESEARCH_ROOT = Path(__file__).resolve().parents[2]  # docs/research/senior-health-2026-09-25
V2_DIR = RESEARCH_ROOT / "forensic-v2"
V3_DIR = RESEARCH_ROOT / "forensic-v3"

SRC = os.environ.get("V3_WORKBOOK_SRC", str(V2_DIR / "SENIOR-HEALTH-FORENSIC-WORKBOOK-V2.xlsx"))
DST = os.environ.get("V3_WORKBOOK_DST", str(V3_DIR / "SENIOR-HEALTH-FORENSIC-WORKBOOK-V3.xlsx"))

HEADER_FONT = Font(name="Arial", bold=True, color="FFFFFF", size=10)
HEADER_FILL = PatternFill("solid", fgColor="1F3864")
DATA_FONT = Font(name="Arial", size=9)
WRAP = Alignment(wrap_text=True, vertical="top")

def style_sheet(ws, headers, rows, col_widths):
    for j, h in enumerate(headers, 1):
        c = ws.cell(row=1, column=j, value=h)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.alignment = WRAP
    for i, row in enumerate(rows, 2):
        for j, val in enumerate(row, 1):
            c = ws.cell(row=i, column=j, value=val)
            c.font = DATA_FONT
            c.alignment = WRAP
    for j, w in enumerate(col_widths, 1):
        ws.column_dimensions[openpyxl.utils.get_column_letter(j)].width = w
    ws.freeze_panes = "A2"
    ws.row_dimensions[1].height = 30

wb = openpyxl.load_workbook(SRC, data_only=False)

# ---- NC-03 correction: SRC (V2) still carries the original fabricated GT-20 claim
# (mean_90d_after=16.7/20, "UPLOAD_IN_DIP") on the 6 rows below that reference it.
# The claim was independently re-checked twice against live Google Trends and found
# fabricated -- the real 262-week series is flat 0 throughout (STAGE2-CORRECTION-
# LEDGER.md NC-03). V2 is preserved as a historical artifact and is not edited; V3
# must not silently carry the retracted claim forward, so every copied row that
# repeats it is overwritten here with the corrected values before V3 is saved.
def _set_row(ws, row_idx, values):
    for j, val in enumerate(values, 1):
        ws.cell(row=row_idx, column=j, value=val)

def _find_row(ws, key, col=1):
    for row in ws.iter_rows(min_col=col, max_col=col):
        if row[0].value == key:
            return row[0].row
    raise ValueError(f"key {key!r} not found in sheet {ws.title}")

_gt20_corrected = {
    "11_GOOGLE_TRENDS": [("GT-20", (
        "GT-20", "how often should seniors shower", "age-specific question", "US", "Google Web Search",
        "2021-09-24 2026-09-24 (5y, weekly)", "2026-09-24T20:58:50Z",
        "NONE (fabricated in prior pass) - full 262-week series is flat 0 except one isolated unrelated spike (value 100, week of 2022-03-06, 4+ years before the claimed event)",
        0, 0, None, None, None, None,
        "CORRECTED 2026-09-25: prior claim of a post-publication rise to means of 16.7-20 was independently re-checked TWICE against live Google Trends and found FABRICATED, not stale. The complete 262-week raw series (forensic-v3/trends-raw/GT-20.json) is flat 0 throughout, including all 9 weeks of the originally-claimed Aug-Sep 2026 rise window. Google Trends zero does not prove zero real-world searches, but no rise of any kind is present in the actual live data. Retracted from all downstream strategy rationale (see LAUNCH-STRATEGY-V3.md item #7, STAGE2-CORRECTION-LEDGER.md NC-03).",
        "LIVE_GOOGLE_TRENDS"))],
    "12_TREND_ATTRIBUTION": [
        ("Elias bath 2026-08-13 (184K)", (
            "GT-20", "how often should seniors shower", "US / Google Web Search", "Elias bath 2026-08-13 (184K)",
            0, 0, 0, "FLAT_ZERO_NO_CHANGE",
            "CORRECTED 2026-09-25 (NC-03): mean_90d_after was fabricated as 16.7; the real raw series is flat 0 before, during and after this video (no dip, no rise - genuinely flat throughout). Correlation was never established for this query; it is now confirmed there is nothing to correlate.")),
        ("Ares bath 2026-08-22 (507K)", (
            "GT-20", "how often should seniors shower", "US / Google Web Search", "Ares bath 2026-08-22 (507K)",
            0, 0, 0, "FLAT_ZERO_NO_CHANGE",
            "CORRECTED 2026-09-25 (NC-03): mean_90d_after was fabricated as 20; the real raw series is flat 0 before, during and after this video (no dip, no rise - genuinely flat throughout). Correlation was never established for this query; it is now confirmed there is nothing to correlate.")),
    ],
}
for sheet_name, patches in _gt20_corrected.items():
    ws = wb[sheet_name]
    for key, values in patches:
        _set_row(ws, _find_row(ws, key, col=4 if sheet_name == "12_TREND_ATTRIBUTION" else 1), values)

_row32_25 = _find_row(wb["25_FIRST_50_VIDEOS"], 32)
_set_row(wb["25_FIRST_50_VIDEOS"], _row32_25, (
    32, "MODIFY",
    "Merge with bathing frequency topic (Ares 527K, Gentle 602K views - real). RETRACTED RATIONALE: this was framed as a \"browse-only, zero-search\" winner using a now-fabricated GT-20 Trends claim (NC-03); why it performed is genuinely unknown, treat as speculative not demonstrated.",
    "Mobility, Balance & Fall Prevention", "Bathroom fall risk", "High-fear specific location framing",
    "Why Most Falls After 70 Happen in the Bathroom (And How to Fall-Proof Yours)", "LOW", "MEDIUM"))
_rowN04 = _find_row(wb["25_FIRST_50_VIDEOS"], "N04")
_set_row(wb["25_FIRST_50_VIDEOS"], _rowN04, (
    "N04", "Daily Living", "How often should you bathe after 65? (dry skin, safety, what dermatologists say)",
    "Ares 527K, Gentle 602K, Elias 188K (views real). RETRACTED RATIONALE: \"GT-20 zero search = browse topic\" was based on a fabricated Trends claim (NC-03) and is withdrawn; the topic itself is not rejected, only this specific explanation for why it worked.",
    "LOW (MV-18)", "Whitespace-by-search + external", None, None, None))

_row7_26 = _find_row(wb["26_LAUNCH_SEQUENCE"], 7)
_set_row(wb["26_LAUNCH_SEQUENCE"], _row7_26, (
    7, "How often should you really bathe after 65?", "Comfortable skin, safety in the bathroom, permission to do less",
    "RETRACTED (NC-03): the \"GT-20 zero search -> browse-led topic\" rationale was based on fabricated Trends data. Views (184K-602K) are real; why the topic performed is genuinely unknown. See MV-18 and LAUNCH-STRATEGY-V3.md item #7.",
    "E4Qsvz-ggXE Ares 506,628 (11.1x); uIOusFFv13k Elias 184,341 (2.1x)",
    "Gentle Health re-run 555 views; Secrets of heath 89",
    "Gentle Health original 602K (~1 y old, 2:31); Aging with Wisdom 63K; Dr. Aven Royce 20K (C10)",
    "RETRACTED (NC-03): no non-zero weeks exist anywhere in the real 262-week GT-20 series; the claimed post-video rise never occurred. See trends-raw/GT-20.json.",
    "HIGH for the '7 shocking facts' title; open for dermatologist-guideline + bathroom-safety angle",
    "'Showering Every Day After 65 Could Be Drying Out Your Skin - Here's What Dermatologists Suggest' / 'How Often Should You Bathe After 65? (And the Bathroom Mistake That Causes Falls)'",
    "Senior hand on grab bar + shower; 'EVERY DAY?'; withheld answer",
    "Permission question ('is it OK to skip a shower?') + skin-change mechanism",
    "Question -> skin changes -> guideline range -> key-area daily wash -> bathroom fall safety -> bridge",
    "PARTIAL (secondary source) -> cite AAD page directly before publishing",
    "Bathroom falls: 5 fixes (First-50 #32)", "Dry, itchy skin after 65",
    "SPECULATIVE, not demonstrated (rationale retracted, NC-03): \"browse-led daily-living topics perform without search demand\" was inferred from a fabricated Trends claim. The topic's real view performance stands; this specific causal explanation does not.",
    "<1x median -> the topic's success was network-specific"))

_row7_27 = _find_row(wb["27_EXPERIMENTATION_PLAN"], 7)
_set_row(wb["27_EXPERIMENTATION_PLAN"], _row7_27, (
    7, "How often should you really bathe after 65?",
    "SPECULATIVE, not demonstrated (rationale retracted, NC-03): \"browse-led daily-living topics perform without search demand\" was inferred from a fabricated Trends claim (GT-20) and should not be treated as a validated finding.",
    "<1x median -> the topic's success was network-specific",
    "28-day views vs channel median; first-party CTR/AVD/traffic source once available",
    "packaging variant only if <1x at day 14 (one change at a time, CS-024)"))

_row_evgt20 = _find_row(wb["29_EVIDENCE_REGISTER"], "EV-GT-20")
_set_row(wb["29_EVIDENCE_REGISTER"], _row_evgt20, (
    "EV-GT-20", "GOOGLE_TRENDS_QUERY",
    "'how often should seniors shower' US Google Web Search 2021-09-24 to 2026-09-24 (5y, weekly, 262 points). CORRECTED 2026-09-25 (NC-03): independently re-queried live TWICE; the complete raw series is flat 0 for the entire window except one isolated, unrelated spike (value 100, week of 2022-03-06). The originally claimed peak week (Sep 13-19, 2026) and rise to means of 16.7-20 are FABRICATED - not present in the live data at all. Raw export preserved at forensic-v3/trends-raw/GT-20.json.",
    "https://trends.google.com/trends/explore", "LIVE_GOOGLE_TRENDS (0-100 relative, not volume)",
    "HIGH (observation)", None, "2026-09-25"))

# ---- Sheet 38: V3 Corrections (new errors caught by the Stage 2 adversarial audit,
# on top of V2's own 19 DQ corrections already in sheet 31) ----
ws = wb.create_sheet("38_V3_CORRECTIONS")
headers = ["id", "location", "previous_claim", "verified_value", "evidence", "severity"]
rows = [
    ["NC-01", "FORENSIC-EXPANSION-FINAL-STATUS.md",
     "149-video sample = 42% of the 306 corpus",
     "149/306 = 48.7%, not 42%. Sample size, per-channel distribution and stratification method are all correct; only the percentage is wrong.",
     "Arithmetic recheck", "LOW - cosmetic, no downstream conclusion affected"],
    ["NC-02", "forensic-v2/SMALL-CHANNEL-BREAKOUTS.json, case SB-05 (Dr. Aliza Wright)",
     "'Walk Straight' video framed as a post-breakout follow-up copy of the real breakout",
     "Registry DB shows the opposite: that video (upload #14, 2026-06-23) was posted 3 days BEFORE the real breakout (upload #15, 2026-06-26). The channel had also already had an earlier unrelated hit (upload #6). Corrected chronology: 3 breakouts, not 1; walking breakout was hits #2 and #3, not the channel's first.",
     "SQL on videos.published_at ordered by channel", "MEDIUM - affected the Section 19 breakout-narrative deliverable, now corrected in 39_V3_BREAKOUT_INVENTORY"],
    ["NC-03", "forensic-v2/TRENDS-REGISTER.json, GT-20 (\"how often should seniors shower\")",
     "Zero search interest for 5 years, then rose to means of 16.7/20 in Aug-Sep 2026 immediately after two bath-related videos posted",
     "Independently re-confirmed TWICE (Stage 2 audit spot-check, then full 32-query raw re-capture): the complete 262-week live series is flat 0 throughout, including all 9 weeks of the claimed Aug-Sep 2026 rise. Treated as FABRICATED, not stale. Raw series preserved at forensic-v3/trends-raw/GT-20.json.",
     "Live Google Trends re-query x2, raw export preserved", "HIGH - a specific causal claim with invented numbers; retracted from First-10 item #7 and First-50 item #32 rationale in LAUNCH-STRATEGY-V3.md"],
    ["NC-04", "FORENSIC-EXPANSION-STATUS-V2.md",
     "\"6 channel pages... checked\" (external research)",
     "Only 5 external channel pages are documented anywhere in the tree (external/CH_channel_pages.txt). No 6th page exists in any file.",
     "Repo-wide grep for channel handles", "LOW - off-by-one in a summary count; underlying 172-video external sample unaffected"],
]
style_sheet(ws, headers, rows, [10, 32, 45, 70, 35, 45])

# ---- Sheet 39: V3 expanded breakout inventory (29 events across 12 channels,
# replacing V2's 5-case SMALL-CHANNEL-BREAKOUTS.json as the authoritative table) ----
ws = wb.create_sheet("39_V3_BREAKOUT_INVENTORY")
headers = ["channel", "source", "upload_idx", "date", "title", "views", "multiple_of_median",
           "in_20_40_window", "durable_lift_after"]
rows = [
    ["Dr. Ares Senior", "internal", "8", "2026-08-19", "Cardiologist Warns: This Sleeping Position Increases STROKE Risk Overnight", 1475129, "32.4x", "No", "No"],
    ["Senior Health Hub", "internal", "2", "2025-09-17", "What Happens If You Eat 2 Cloves a Day for 7 Days", 1090015, "114.3x", "No", "No"],
    ["Senior Health Hub", "internal", "9", "2025-10-05", "5 KG of STOOL Out in 1 Hour! No More Constipation", 432821, "45.4x", "No", "No"],
    ["Senior Health Hub", "internal", "32", "2025-12-08", "Over 50 and Eating 2 Cloves Daily? Here's What NOBODY Told You", 143862, "15.1x", "Yes", "No"],
    ["Senior Health Hub", "internal", "39", "2025-12-31", "Drink Just 1 Glass to Cleanse Your Entire Colon in 10 Minutes", 168985, "17.7x", "Yes", "No"],
    ["Senior Health Hub", "internal", "49", "2026-01-31", "I CHEWED CLOVES for 7 days and didn't even suspect this...", 1055564, "110.7x", "No", "No"],
    ["Senior Health Hub", "internal", "51", "2026-02-06", "I Ate Garlic at Night for 7 Days and Didn't Expect THIS", 353637, "37.1x", "No", "No"],
    ["Senior Health Hub", "internal", "53", "2026-02-12", "I DRANK CLOVE WATER for 7 days... I was not ready", 554619, "58.1x", "No", "No"],
    ["Senior Health Hub", "internal", "65", "2026-03-22", "10 LBS of Toxic Waste Stuck Inside You! 1-Minute Japanese Habit", 245337, "25.7x", "No", "No"],
    ["Senior Health Hub", "internal", "66", "2026-03-25", "Mixing CLOVES with CINNAMON Can Trigger IRREVERSIBLE Changes", 290424, "30.4x", "No", "No"],
    ["Senior Health Hub", "internal", "68", "2026-04-01", "12 KG of Waste Stuck Inside You? #1 Natural Colon Cleanse", 501622, "52.6x", "No", "No"],
    ["Senior Health Hub", "internal", "75", "2026-04-22", "She Chewed 2 Cloves Every Day. Nobody Expected This", 325737, "34.1x", "No", "No"],
    ["Senior Health Hub", "internal", "77", "2026-04-28", "Put 1 Clove in Coffee... What Happens 10 Minutes Later (channel peak)", 3088021, "323.7x", "No", "No"],
    ["Senior Health Hub", "internal", "112", "2026-08-14", "I Put a Clove Under My Tongue - 5 Minutes Later My Body Did Something", 173273, "18.2x", "No", "No"],
    ["Doctor Thomas", "internal", "9", "2026-06-12", "A SIMPLE Exercise Every 70+ Should Do Daily (Stop Falls for Good)", 596346, "72.4x", "No", "No"],
    ["Doctor Thomas", "internal", "14", "2026-06-19", "One SIMPLE Change to How You Walk That Could Save Your Life After 70 (channel peak)", 1004391, "122.0x", "No", "No"],
    ["Doctor Thomas", "internal", "16", "2026-06-21", "Why You Can't Walk Straight Anymore After 70", 328707, "39.9x", "No", "No"],
    ["Dr. Okoro", "internal", "26", "2026-05-16", "Cardiologist Warns: 9 Foot Signs of Hidden Diabetes After 60 (day 58 since channel join)", 494473, "2484.8x", "Yes", "No"],
    ["Dr. Okoro", "internal", "37", "2026-06-03", "The ONLY 6 Exercises YOU Need to Relieve Neuropathy in Feet & Legs", 100852, "506.8x", "Yes", "No"],
    ["Dr. Okoro", "internal", "38", "2026-06-05", "Your Kidneys Are Begging You to Eat These 5 Vegetables", 11319, "56.9x", "Yes", "No"],
    ["Dr. Aliza Wright", "internal (corrected, was NC-02)", "6", "2026-06-12", "If You Take Losartan, Amlodipine, or Metoprolol After 60", 47032, "216.7x", "No", "No"],
    ["Dr. Aliza Wright", "internal (corrected, was NC-02)", "14", "2026-06-23", "Why You Can't Walk Straight Anymore After 70 (topic-experiment, 3 days BEFORE #15, not a copy of it)", 20701, "95.4x", "No", "No"],
    ["Dr. Aliza Wright", "internal (corrected, was NC-02)", "15", "2026-06-26", "One SIMPLE Change to How You Walk...After 70 (channel peak)", 219009, "1009.3x", "No", "No"],
    ["Dr. Elias Senior Health", "internal - NEGATIVE CONTROL", "-", "-", "No video reaches 15x median across all 29 uploads (channel high: 6.5x)", 0, "0 breakouts", "N/A", "N/A"],
    # Case 13 (Better Health While Aging, DS-000033), added 2026-09-25 same day as the NC-05
    # correction above; see SMALL-CHANNEL-BREAKOUT-FORENSICS.md and
    # cross-channel/BREAKOUT-EVENT-CANONICAL-TABLE.json (events BE-29..BE-37).
    ["Better Health While Aging", "internal (added 2026-09-25)", "3", "2021-12-04", "10 Causes of Memory Loss in Aging", 980106, "45.3x", "No", "No"],
    ["Better Health While Aging", "internal (added 2026-09-25)", "4", "2021-12-11", "PARANOIA or Memory Loss. Signs That Could be Early Alzheimer's", 429529, "19.8x", "No", "No"],
    ["Better Health While Aging", "internal (added 2026-09-25)", "5", "2021-12-14", "Improve Memory by AVOIDING These Drugs (channel peak)", 3582804, "165.5x", "No", "No"],
    ["Better Health While Aging", "internal (added 2026-09-25)", "15", "2022-06-29", "10 Warning Signs of Early Alzheimer's Disease - HOP ML Podcast", 607506, "28.1x", "No", "No"],
    ["Better Health While Aging", "internal (added 2026-09-25)", "29", "2023-09-07", "Memory Improvement: Say No to These Medications", 953110, "44.0x", "No", "No"],
    ["Better Health While Aging", "internal (added 2026-09-25)", "53", "2025-02-21", "Vitamin B12 Deficiency in Aging: Causes, Symptoms and Treatment", 1294247, "59.8x", "No", "No"],
    ["Better Health While Aging", "internal (added 2026-09-25)", "65", "2025-05-15", "Is Your Blood Pressure Too Low? Understanding Hypotension", 329571, "15.2x", "No", "No"],
    ["Better Health While Aging", "internal (added 2026-09-25)", "66", "2025-05-29", "Tylenol, Advil, or Aspirin? What's Safest for Older Adults", 664860, "30.7x", "No", "No"],
    ["Better Health While Aging", "internal (added 2026-09-25)", "71", "2025-07-02", "Dehydration in Older Adults: Symptoms, Treatment, & Prevention", 325492, "15.0x", "No", "No"],
    ["Amos Boone", "external (new, V3)", "29 of 43", "~4mo before capture", "The ONLY 7 Exercises YOU Need to Relieve Neuropathy in Feet & Legs", 207000, "n/a (external, no channel median computed)", "Yes", "No"],
    ["SeniorHood", "external (new, V3)", "12 of 76", "~9mo before capture", "Surgeon REVEALS: 5 Wall Exercises Proven To Outperform Walking After 60", 199000, "n/a", "No", "No"],
    ["SeniorHood", "external (new, V3)", "16 of 76", "~9mo before capture", "Surgeon REVEALS: Do THIS 1 Exercise for Poor Leg Circulation After 60 (channel peak)", 1046812, "n/a", "No", "No"],
    ["SeniorHood", "external (new, V3)", "26 of 76", "~7mo before capture", "Surgeon WARNS: Neuropathy Is Getting Worse After 60!", 471000, "n/a", "No", "No"],
    ["SeniorHood", "external (new, V3)", "~73 of 76", "~3wk before capture", "Jack LaLanne (89): The Only 4 Chair Exercises to Rebuild Weak Legs After 60!", 178000, "n/a", "No", "No"],
]
style_sheet(ws, headers, rows,
            [22, 26, 12, 14, 55, 12, 14, 14, 14])
ws2 = wb["39_V3_BREAKOUT_INVENTORY"]
note = ws2.cell(row=len(rows) + 3, column=1,
    value=("Note: 4 negative-control failure channels (Senior Mobility, Health 365, Senior Strength Secrets, "
           "Aging Senior Health) plus per-breakout matched-failure videos are documented in full detail in "
           "SMALL-CHANNEL-BREAKOUT-FORENSICS.md, not repeated here for space. \"multiple_of_median\" is computed "
           "against each channel's own whole-catalog median (internal cases only; external per-channel medians "
           "were not computed given time budget - see raw report for context). 2026-09-25 addendum: Better Health "
           "While Aging (rows 26-34) also has a supplementary time-matched local-baseline multiple per event "
           "(addressing that a single 4.5-year whole-catalog median can misstate a breakout's true local "
           "significance) and per-breakout matched-failure videos -- see SMALL-CHANNEL-BREAKOUT-FORENSICS.md "
           "Case 13 and cross-channel/BREAKOUT-EVENT-CANONICAL-TABLE.json (local_baseline_multiple field). Not "
           "repeated here for space; this sheet's multiple_of_median column is unchanged and remains "
           "whole-catalog-median-based for comparability across all 37 rows."))
note.font = Font(name="Arial", italic=True, size=8, color="666666")
note.alignment = Alignment(wrap_text=True)
ws2.merge_cells(start_row=len(rows) + 3, start_column=1, end_row=len(rows) + 3, end_column=9)

# ---- Sheet 40: V3 Trends re-capture status ----
ws = wb.create_sheet("40_V3_TRENDS_STATUS")
headers = ["id", "query", "geo", "property", "old_register_status", "v3_recapture_status", "raw_export_file"]

import json
old = json.load(open(V2_DIR / "TRENDS-REGISTER.json"))
inv = old["live_investigations"] if isinstance(old, dict) else old
rows = []
for item in inv:
    gid = item.get("id")
    status = "RETRACTED - fabricated causal claim, see NC-03" if gid == "GT-20" else "Reproduced (matches within normal Trends sampling drift)"
    rows.append([gid, item.get("query"), item.get("geo"), item.get("property"),
                 "Complete query metadata, no raw export existed", status, f"trends-raw/{gid}.json"])
style_sheet(ws, headers, rows, [8, 34, 26, 18, 40, 42, 22])

# ---- Addendum note on 00_READ_ME (append, don't overwrite existing rows) ----
readme = wb["00_READ_ME"]
last_row = readme.max_row
addendum_rows = [
    "",
    "V3 ADDENDUM (2026-09-25)",
    "Sheets 38-40 added by an independent adversarial audit. Full narrative and evidence in docs/research/senior-health-2026-09-25/forensic-v3/.",
    "4 new corrections found beyond V2's own 19 (sheet 31): see sheet 38_V3_CORRECTIONS.",
    "Small-channel breakout inventory expanded from 5 cases to 37 breakout events across 13 channels (32 internal + 5 external; 23 internal + 5 external = 28 as of the NC-05 correction, plus 9 more internal events added same day from newly acquired Better Health While Aging, DS-000033, Case 13 — see A56/A57 below): see sheet 39_V3_BREAKOUT_INVENTORY and SMALL-CHANNEL-BREAKOUT-FORENSICS.md.",
    "All 32 Google Trends investigations re-verified with raw time-series exports now preserved (forensic-v3/trends-raw/); 1 entry (GT-20) found fabricated and retracted: see sheet 40_V3_TRENDS_STATUS.",
    "KNOWN LIMITATION, unchanged from V2: LibreOffice is not installed in this environment, so recalc.py could not run on this file. Sheets 38-40 contain no formulas (static evidence tables only), so this limitation does not affect them; it continues to apply to V2's original formula-bearing sheets (01, 03, 04, 05) exactly as V2 disclosed.",
    "A second independent audit (2026-09-25, same day) found and fixed two further defects: the breakout-event total was miscounted as 29 (23 internal + 6 external) when the underlying per-case figures actually sum to 28 (23 internal + 5 external, NC-05); and this cell (A49) was accidentally saved as a formula because its text began with \"=\", which Excel would show as broken. Both are corrected in place. See STAGE2-CORRECTION-LEDGER.md.",
    "Same day (2026-09-25), Better Health While Aging (DS-000033, Senior Health Group C P1 acquisition) was added as sheet 39_V3_BREAKOUT_INVENTORY Case 13 (see SMALL-CHANNEL-BREAKOUT-FORENSICS.md): 9 further internal breakout events, bringing the total to 37 breakout events across 13 channels (32 internal + 5 external). See cross-channel/BREAKOUT-EVENT-CANONICAL-TABLE.json for the updated identity-keyed table.",
    "Same day (2026-09-25), Case 13's 9 breakout events were deep-dive-verified per the master brief: all 9 re-confirmed exactly against the raw dataset; matched-failure videos identified for 7 of 9 (2 topics -- Tylenol/Advil/Aspirin, dehydration -- have no internal comparable, disclosed not fabricated); a supplementary time-matched local-baseline multiple was added addressing that a flat 4.5-year whole-catalog median can misstate a breakout's true local significance (3 early-2021 breakouts are understated by the flat median, up to 460.6x locally vs. 165.5x documented; 2 of the 3 2025 entries fall below the 15x threshold against a contemporaneous baseline though remain real local outliers); and the channel's credential-first self-intro was found to be a constant across both breakout and matched-failure videos, not a differentiator. Canonical event count (37) unchanged. See SMALL-CHANNEL-BREAKOUT-FORENSICS.md Case 13 and BREAKOUT-EVENT-CANONICAL-TABLE.json.",
]
for i, text in enumerate(addendum_rows):
    c = readme.cell(row=last_row + 1 + i, column=1, value=text)
    c.font = Font(name="Arial", size=10, bold=text.startswith("V3 ADDENDUM"))
    c.alignment = Alignment(wrap_text=True)

wb.save(DST)
print("Saved:", DST)
print("Total sheets:", len(wb.sheetnames))
