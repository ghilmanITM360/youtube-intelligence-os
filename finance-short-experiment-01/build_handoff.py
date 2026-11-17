"""Write the preliminary storyboard and verify this isolated Phase 1 handoff.

Uses existing text and read-only source hashes. Never decodes competitor media.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
from PIL import Image

ROOT = Path(__file__).resolve().parent
script = (ROOT / 'FINAL_SCRIPT.md').read_text().split('## Complete narration\n\n')[1].split('\n## Direction')[0].strip()
paragraphs = script.split('\n\n')
assert len(paragraphs) == 12

# Each row describes a meaningful information change; held scenes can span rows.
designs = [
('01_offer','The apparent no-interest promise can still produce a bill.', 'Remy looks from a teal offer to a coral receipt, eyebrows raised.', 'None', 'Offer; interest receipt', 'Abstract checkout close-up', 'No chart; the promise and bill are juxtaposed.', 'An offer with a second financial consequence.', 'Start on meaningful hero; reveal receipt on “bill”; no logo intro.', 'Reuse thumbnail A head, offer and receipt grammar.', 'F1', 'DEFERRED INTEREST', 'Keep headline and receipt near center; no dollar amount.'),
('01_offer','The purchase and twelve-month condition are hypothetical.', 'Remy brings a sofa into the living-room layout and reads the card.', 'None', 'Sofa; store-card offer; calendar', 'Simple living room', 'Calendar strip labeled illustrative 12-month offer; not actual account dates.', 'A household purchase starts a contractual clock.', 'Sofa slides to a settled position; reveal condition as it is spoken.', 'New sofa and room modules; reusable Remy and offer.', 'F2', 'Illustrative offer • U.S. store card', 'Do not portray a named retailer or real customer.'),
('02_condition','The full-payment condition controls the outcome.', 'Remy points directly at IF, gaze following fingertip.', 'None', 'Offer', 'Isolated offer', 'One condition highlighted.', 'IF behaves like a switch between possible outcomes.', 'Local push to IF; brief hold; do not animate unrelated props.', 'Reuse thumbnail A hero; later custom pointing pose.', 'F2;F4', 'IF PAID IN FULL', 'Make full condition legible in video even when thumbnail text is small.'),
('03_ledger','Accruing interest and being charged interest are different events.', 'Remy pulls the offer aside to reveal a separate interest ledger.', 'None', 'Offer; balance card; interest receipt', 'Abstract ledger workspace', 'Two separate labeled areas: promotional balance; interest accruing.', 'An accumulating receipt waits beside the purchase balance.', 'Sequential entry reveals; keep CHARGED absent until triggered.', 'Custom two-ledger layout; reuse receipt and offer.', 'F3', 'ACCRUING • NOT YET CHARGED', 'Entries are schematic, not scaled money or secret undisclosed debt.'),
('04_outcomes','Full compliant payoff avoids the accrued interest charge.', 'Remy transfers the last payment token, then relaxes.', 'None', 'Payment token; promotional balance card; receipt', 'Same ledger workspace', 'Paid-in-full branch; accrued-interest entries cleared with WAIVED.', 'The conditional switch cancels the waiting receipt.', 'Directed token transfer, balance clears, receipt masks out; hold payoff.', 'Reuse ledger; new token and relieved expression.', 'F4', 'PAID IN FULL + TERMS MET / INTEREST WAIVED', 'Terms include required timely payments. Label prevents unconditional payoff claim.'),
('04_outcomes','Leaving a promotional balance at expiration can trigger accumulated interest.', 'Return to alternative scenario; Remy stops as the calendar turns.', 'None', 'Calendar; remaining balance card; receipt', 'Same ledger, explicitly alternative path', 'Branch label IF BALANCE REMAINS; accrued receipt joins bill.', 'A waiting charge is released at expiry.', 'Show ALTERNATIVE first; turn page, then transfer receipt; no explosion.', 'Reuse props; custom concerned pose and branch state.', 'F5', 'ALTERNATIVE: BALANCE REMAINS AT EXPIRY', 'Avoid suggesting the same shopper simultaneously takes both paths.'),
('05_history','The interest relates to balances carried through the promotional period.', 'Remy follows a line back to the sofa purchase.', 'None', 'Receipt; calendar strip; sofa mini silhouette', 'Schematic time strip', 'Balance cards decrease with payments; interest entries accumulate separately.', 'A line traces the purchase history backward.', 'Trace backward from bill to purchase; reveal prior balance cards sequentially.', 'Custom time/ledger composition using existing props.', 'F6', 'Based on balances carried • schematic', 'Never draw constant original principal after payments; no invented chart units.'),
('05_history','On-time minimum payments do not necessarily finish the promotional payoff.', 'Remy places payment checkmarks but notices a remaining balance.', 'None', 'Payment tokens; calendar; promotional balance card', 'Same time strip', 'Payment checkmarks and an explicitly nonempty balance card.', 'A checklist can be complete while the payoff is incomplete.', 'Checkmark reveals followed by remaining-balance highlight.', 'Reuse modules; new checkmark symbol only.', 'F7', 'MINIMUM PAID ≠ PROMOTION PAID OFF', 'Use “may” in supporting copy; do not claim all minimum schedules fail.'),
('06_comparison','True zero-percent introductory APR has different retrospective treatment.', 'Remy separates the two offer types with open hands.', 'None', 'Two offer panels; receipt; clock', 'Split comparison stage', 'Deferred: accrues during offer; true 0%: no promo-period interest, later interest possible.', 'Two doors with different rules, not identical promises.', 'Build panels one at a time; cross out retrospective receipt only on true-zero side.', 'Custom comparison layout; reuse offer/receipt and new open-hand pose.', 'F8', 'TRUE 0% INTRO APR / Interest may start after promotion', 'Do not label a deferred-interest offer 0% APR. Keep this contrast readable.'),
('06_comparison','The promotional expiry and ordinary monthly due date are distinct checks.', 'Remy circles the promotional deadline and checks the promotional balance.', 'None', 'Two calendar cards; balance card', 'Simple statement checklist', 'Distinct labels for promotion expiry and payment due; no fabricated dates.', 'Two clocks can govern one bill.', 'Reveal due-date card, then highlight separate expiry card.', 'Reuse calendars; custom two-date arrangement.', 'F9', 'PROMOTION EXPIRY / MONTHLY PAYMENT DUE', 'No personalized due date or repayment instruction.'),
('07_callback','Return to the original deferred-interest purchase.', 'Remy sits beside the newly arrived sofa and looks toward purchase day.', 'None', 'Sofa; clock; offer', 'Living room', 'Purchase-day marker; no numeric scale.', 'The sofa arrives before any interest is charged.', 'Return to established room; clock settles; short breath.', 'Reuse room and sofa; later seated/leaning pose if needed.', 'F3;F10', 'DEFERRED INTEREST', 'Re-establish deferred-interest scope after the zero-percent comparison.'),
('07_callback','Deferred interest was accruing from purchase day, conditional on later payoff.', 'Remy notices the waiting receipt, then looks back at IF.', 'None', 'Clock; schematic receipt; offer', 'Hero B with offer-condition callback', 'No new chart or claim.', 'The waiting receipt completes the opening question.', 'Receipt reveal, subtle backward clock movement, then hold ending.', 'Reuse thumbnail B groups and A condition token.', 'F3;F4;F10', 'Waived when payoff conditions are met', 'No CTA; no inevitable charge or fake financial amount.'),
]
fields=['beat','composition','start_sec_provisional','end_sec_provisional','timing_status','narration','intended_viewer_understanding','main_character_action_or_reaction','supporting_characters','objects_props','environment','diagram_chart','visual_metaphor','expected_keyframe_motion','reusable_vs_custom_artwork','claim_ids','onscreen_text_qualifier','accuracy_or_layout_note','existing_motion_evidence_refs']
audit_refs=['E01;E12;E20','E04;E15;E17;E24','E07;E25;E27','E02;E13;E14;E16;E20;E21;E26','E06;E10;E19;E22','E03;E10;E19','E08;E09;E25','E02;E20;E22;E26','E06;E11;E12;E22','E07;E27','E04;E15;E17;E24','E14;E20;E26;original clock metaphor']
time=0.0
with (ROOT/'PRELIMINARY_STORYBOARD.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields); writer.writeheader()
    for i,(narration,d) in enumerate(zip(paragraphs,designs),1):
        duration=len(narration.split())/160*60 + (0.5 if i in [3,6,9,11] else 0)
        row=dict(zip(['composition']+fields[6:],d))
        row['existing_motion_evidence_refs']=audit_refs[i-1]
        row.update(beat=i,start_sec_provisional=round(time,1),end_sec_provisional=round(time+duration,1),timing_status='PROVISIONAL_UNTIL_OWNER_MP3',narration=narration)
        writer.writerow(row); time+=duration

source=json.loads((ROOT/'SOURCE_PROVENANCE.json').read_text())
changed=[x['path'] for x in source['files'] if hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()!=x['sha256']]
source_root=Path(source['source_root'])
catalog_path=source_root/'data/extracted/forensic-analysis/casually-finance/2026-10-12/01_CHANNEL_METADATA/all-videos-metadata.csv'
catalog=list(csv.DictReader(catalog_path.open()))
patterns={
 'deferred_interest':r'deferred[- ]interest|no[- ]interest|zero[- ]percent (?:intro|interest|APR)|(?<![\d.])0% (?:intro|APR)|paid in full',
 'auto_loan_term':r'auto.loan|car.loan|car.payment|longer.loan|loan.term',
 'inflation':r'inflation|disinflation|price.level',
}
originality={key:[{'video_id':r['video_id'],'title':r['title']} for r in catalog if re.search(pattern,r['title']+' '+r['description'],re.I)] for key,pattern in patterns.items()}

rows=list(csv.DictReader((ROOT/'PRELIMINARY_STORYBOARD.csv').open()))
assert ' '.join(r['narration'] for r in rows)==' '.join(script.split('\n\n'))
assert all(all(r[k].strip() for k in fields) for r in rows)
assert not changed,changed
images={}
for name in ['A','B']:
    p=ROOT/f'thumbnail_{name}.png'
    with Image.open(p) as im:
        assert im.size==(2160,3840)
        images[name]={'path':str(p),'pixels':list(im.size),'format':im.format,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
assert len(catalog)==len({r['video_id'] for r in catalog})==206
assert not list(ROOT.rglob('*.mp4')) and not list(ROOT.rglob('*.mp3'))
result={
 'status':'PHASE_1_READY_FOR_APPROVAL','date':'2026-10-13','timezone':'Asia/Karachi',
 'spoken_words':len(script.split()),'word_count_method':'Whitespace-delimited narration words; zero-percent counts as one.',
 'estimated_runtime_seconds_including_two_seconds_pauses':{'175_wpm':round(len(script.split())/175*60+2,1),'160_wpm':round(len(script.split())/160*60+2,1)},
 'provisional_storyboard_seconds':round(time,1),'visual_beats':len(rows),'composition_groups':len({r['composition'] for r in rows}),
 'storyboard_narration_reconciles':True,'storyboard_all_required_fields_present':True,
 'images':images,'source_hashes_unchanged':len(source['files']),'source_changes':changed,
 'catalog_unique_records':len(catalog),'originality_keyword_matches':originality,
 'originality_limit':'Titles and descriptions only, plus six-source inherited Shorts analysis; no full-channel transcript novelty proof.',
 'separate_27_sequence_investigation':'READ: both exact files supplied by owner; E01–E27 mapped; PARTIALLY_SUPPORTED; 24/27 selected intervals only.',
 'financial_claims':'10 ledger items; factual statements supported in scope; F2 is hypothetical and F10 metaphorical.',
 'human_thumbnail_comprehension_test':'NOT_PERFORMED','actual_narration_runtime':'PENDING_OWNER_MP3',
 'owner_account_thumbnail_support':'NOT_VERIFIED; current platform documentation checked',
 'resource_usage':{'start_five_hour_used_percent':2,'start_weekly_used_percent':16,'midpoint_five_hour_used_percent':26,'midpoint_weekly_used_percent':20,'pre_final_five_hour_used_percent':52,'pre_final_weekly_used_percent':24,'stop_expensive_work_thresholds':{'five_hour':90,'weekly':95},'scope':'Account-wide, shared across chats; not exact task consumption.','agents':1,'paid_scraping_calls':0,'paid_asset_generation_calls':0,'video_renders':0},
}
(ROOT/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'words':len(script.split()),'seconds':round(time,1),'beats':len(rows),'sources_unchanged':len(source['files']),'images':{k:v['pixels'] for k,v in images.items()},'originality_match_counts':{k:len(v) for k,v in originality.items()}},indent=2))
