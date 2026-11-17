"""Triage of forensic support images, preflight screenshots and document-embedded images (2026-10-04).

Evidence for each verdict: every image was shown in a programmatic contact sheet that was opened and
reviewed (1,012 640x360 frames in 11 sheets; 174 larger images in 6 sheets; the 2 preflight images, the 2
document images and the dock-strip screenshot individually) and a pHash screen against all 2,281
thumbnails found no match within distance 10. Folder/file-name patterns document the rule; none of these
images is a video thumbnail.
"""
import csv, os, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
rows = []
for r in csv.DictReader((HERE / 'asset-inventory.csv').open()):
    loc, role = r['location'], r['role']
    base = os.path.basename(loc)
    if role == 'FORENSIC_SUPPORT_IMAGE_PENDING_REVIEW':
        if (r['width'], r['height']) == ('640', '360'):
            cls, sub, note = 'VIDEO_FRAME', 'VIDEO_FRAME', 'Frame/keyframe extracted from the analysed video (shot_frames, shot_triplets or reference_frames); not a thumbnail'
        elif re.search(r'montage|atlas|contact_sheet|overview|triplets|range_|dense_|refined_boundaries', base):
            cls, sub, note = 'CONTACT_SHEET', 'CONTACT_SHEET', 'Forensic contact sheet / montage / atlas of video frames'
        elif re.search(r'audio_envelope|spectrogram|temporal_average', base):
            cls, sub, note = 'FORENSIC_SUPPORT_IMAGE', 'ANALYSIS_OUTPUT', 'Audio or temporal analysis plot; not a thumbnail'
        elif 'seven_title_cards' in base:
            cls, sub, note = 'CONTACT_SHEET', 'CONTACT_SHEET', 'Montage of eight in-video title-card frames; not a video thumbnail'
        else:
            cls, sub, note = 'FORENSIC_SUPPORT_IMAGE', 'OTHER', 'Forensic support image'
        status = 'INSPECTED_CONTACT_SHEET'
    elif role == 'ACQUISITION_SCREENSHOT_PENDING_REVIEW':
        cls, sub, status, note = 'UI_OR_PREFLIGHT_IMAGE', 'UI_SCREENSHOT', 'INSPECTED_NATIVE', 'Desktop app screenshot of a coding-assistant session (Apify budget discussion); no YouTube thumbnail visible'
    elif role == 'IMAGE_UNCLASSIFIED' and 'image1.png' in loc:
        cls, sub, status, note = 'DOCUMENT_EMBEDDED_IMAGE', 'ANALYSIS_OUTPUT', 'INSPECTED_NATIVE', 'Spreadsheet/chart screenshot embedded in a PRIVATE_REPO_ONLY report; contains no thumbnail'
    elif role == 'IMAGE_UNCLASSIFIED':
        cls, sub, status, note = 'DOCUMENT_EMBEDDED_IMAGE', 'OTHER', 'INSPECTED_NATIVE', 'Blank white docProps thumbnail of the DOCX; not a video thumbnail'
    else:
        continue
    rows.append(dict(Asset_ID=r['asset_id'], Source_Path=loc, Evidence_Class=cls, Support_Subclass=sub, Inspection_Status=status, Is_Thumbnail='NO', Notes=note))
with (HERE / 'asset-triage.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
from collections import Counter
print(len(rows), Counter((r['Evidence_Class'], r['Support_Subclass']) for r in rows))
