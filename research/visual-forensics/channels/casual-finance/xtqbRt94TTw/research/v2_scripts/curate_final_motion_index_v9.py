"""Curated motion retrieval catches up with independently audited PDF decision."""
from pathlib import Path
import csv,json
R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
stats=json.loads((R/'session_20261105/pdf_complete_compound_integration_v15_stats.json').read_text());assert stats['PDF_native_distinct_observations']==47
rows=list(csv.DictReader((R/'production_v1/motion_camera_facial_index_PARTIAL_v8.csv').open()))
row=next(x for x in rows if x['id']=='EP0054')
row.update(motion_status='BOUNDED_CONTIGUOUS_NATIVE_COMPOUND_OBSERVED;SOURCE_MECHANISM_AND_SETTLE_UNKNOWN',path='Retained-viewer uneven page-position updates;Table1enters1622/full1623;wholeviewer/pageenlarge/reframe1625;cropremnantsleave1633/1636/1639;hostadded1642.',
 easing='UNKNOWN_SOURCE_PRESET;NO_SOURCE_UI_OPERATION_INFERRED',duration_note='1596–1642 is47frame before/compound context, not one animation duration. Group enlargement first visible1625, still transforms through endpoint; no exact settle.',
 curated_motion_review='integrated_v4/document_zoom_track_v2.json',curated_observed_change='Coarse full-composition-cut claim rejected after47distinct native frame observations; main document/page anchors retained with traversal/scale/crop and additivehost.',
 timing_scope='Aggregate1596–1642 all47distinct native source frames accounted by31newearly+16qualifiedreuses; bounded semantic adjudication, not global all-frame motion pass',validation='Independent actual-return-byte audits and47frame coverage/phase audit PASS; source mechanism/settle/hearing unverified')
p=R/'production_v1/motion_camera_facial_index_PARTIAL_v9.csv';assert not p.exists()
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('Motionv9curationalignedwithv15;766rows;globalmotionstillpartial')
