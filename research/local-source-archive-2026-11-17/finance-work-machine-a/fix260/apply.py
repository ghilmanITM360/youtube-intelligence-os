import json, hashlib
B='audit-batches/'
p=json.load(open(B+'NICK_260.json')); r=json.load(open(B+'NICK_260_READ_RECEIPTS.json'))
ca=p['reviews'][0]['script']['claim_audit']
c17,c20=ca[16],ca[19]; assert c17['claim_id']=='C17' and c20['claim_id']=='C20'
old={'C17':dict(c17),'C20':dict(c20),'analysis':p['reviews'][0]['script']['analysis']}
c17['assessment']=('[PRIMARY_SOURCE_DIRECTLY_INSPECTED] CORRECTED 2026-11-01 (corrections/NICK_260/NICK_260_CORRECTION_2026-11-01.json). '
 'NYFX25Q4: NY Fed HHDC 2025Q4 data workbook (released 2026-02-10, before the 2026-04-07 upload), sheet "Page 12 Data" '
 '(Percent of Balance 90+ Days Delinquent by Loan Type), row 25:Q4, CC = 12.70% (25:Q3 12.41%). The creator\'s 12.7% stock share is VERIFIED; '
 '"more than one in eight" (12.5%) is consistent. The original verdict confused it with the different flow measure '
 '("Page 14 Data", new seriously delinquent balances, 25:Q4 CC = 7.13% annualised). Original verdict "Unsupported as stated" is superseded.')
c17['source_ids']=['NYFX25Q4','NYF4Q']
c20['assessment']=('[PRIMARY_SOURCE_DIRECTLY_INSPECTED] CORRECTED 2026-11-01 (partial). NYFX25Q4 "Page 14 Data" (new seriously delinquent balances, '
 'annualised percent of balance), student loans: 25:Q3 = 14.26%, 25:Q4 = 16.19%. The "14.3%" matches the 2025Q3 value (released November 2025) and is '
 'historically accurate for that quarter, but at the 2026-04-07 upload the 2025Q4 report (16.19%, released 2026-02-10) was already public, so the figure '
 'was not the latest and understates it. NYFPDF25Q4: the report states outstanding student loan debt of $1.66 trillion in 2025Q4, not $1.696 trillion '
 '(the $1.696T may be a Department of Education federal-portfolio figure, not checked). [ANALYST_RECALL_NOT_REVERIFIED] SAVE court loss and wind-down consistent; '
 '"fastest since 2000", 43 million borrowers, $39,633 average and 7 million in default not checked. UNVERIFIED_CREATOR_ASSERTION for the unchecked parts.')
c20['source_ids']=['NYFX25Q4','NYFPDF25Q4']
a=p['reviews'][0]['script']['analysis']
s_old='Unsupported: 30.9% panic sellers, 12.7% 90+ delinquency stock, the version-two outcomes.'
assert a.count(s_old)==1
p['reviews'][0]['script']['analysis']=a.replace(s_old,'Unsupported: 30.9% panic sellers, the version-two outcomes. Corrected 2026-11-01 from the NY Fed 2025Q4 data workbook: the 12.7% card 90+ delinquency stock is verified (12.70%); the 14.3% student-loan transition rate matches 2025Q3 but was not the latest at upload (2025Q4 16.19%); $1.696T vs NY Fed $1.66T.')
src=[('NYFX25Q4','https://www.newyorkfed.org/medialibrary/interactives/householdcredit/data/xls/HHD_C_Report_2025Q4.xlsx','HHD_C_Report_2025Q4.xlsx','1969610624cf0c45a84a47018ccc9d464113dc4f6921ec85d0f07e833925bd55',
  'NY Fed Household Debt and Credit Report 2025Q4 data workbook; sheets "Page 12 Data" and "Page 14 Data", rows 25:Q3 and 25:Q4',
  'Page 12 CC 90+ share of balance: 25:Q3 12.41, 25:Q4 12.7016. Page 14 new seriously delinquent (annualised): CC 25:Q4 7.1293; student loan 25:Q3 14.26, 25:Q4 16.19.'),
 ('NYFPDF25Q4','https://www.newyorkfed.org/medialibrary/interactives/householdcredit/data/pdf/HHDC_2025Q4.pdf','HHDC_2025Q4.pdf','9f635fa98b092ab4c7a969ffe1ee7266d10f81892d8402ed2488e3bdc347d05b',
  'NY Fed Household Debt and Credit Report 2025Q4 PDF ("2025: Q4 (RELEASED FEBRUARY 2026)")',
  'Outstanding student loan debt $1.66 trillion in 2025Q4; 9.6% of student loan balances 90+ days delinquent.')]
D='/Users/ghilmankhan/finance-work-machine-a/quality260/'
for sid,url,fn,sha,loc,find in src:
    assert hashlib.sha256(open(D+fn,'rb').read()).hexdigest()==sha
    r['primary_source_receipts'].append({'source_id':sid,'url':url,'source_date':'2026-02-10','access_scope':'DIRECT_FETCH_OF_PRIMARY_DATA',
     'source_confidence':'PRIMARY_SOURCE_DIRECTLY_INSPECTED','locator':loc+'; SHA-256 '+sha+'; durable copy '+D+fn,'finding':find,
     'limitations':'Added by the 2026-11-01 correction; the original NYF4Q search-summary receipt is retained unchanged.','publication_applicability':'BEFORE_PUBLICATION','accessed':'2026-11-01'})
json.dump(p,open(B+'NICK_260.json','w'),indent=1,ensure_ascii=False); open(B+'NICK_260.json','a').write('\n')
json.dump(r,open(B+'NICK_260_READ_RECEIPTS.json','w'),indent=1,ensure_ascii=False); open(B+'NICK_260_READ_RECEIPTS.json','a').write('\n')
json.dump({'correction_id':'NICK_260_CORRECTION_2026-11-01','video_id':'mErWx9GiVUc','nick':'NICK_260','upload_date':'2026-04-07',
 'basis':'NICK_260_264_QUALITY_ADDENDUM_2026-11-01.md; sources re-opened and re-hashed in this correction',
 'original_packet':{'commit':'c70a81acc70ffe5fe75b30753a4ac66d382014c9','blob':'dcb4e1830bed3000364863e26b3a6e6aaed770d8','sha256':'46c6a074c7d7cfa420880c19ccb5d57eb9398194f0bc234085406f504dfcda54','copy':'corrections/NICK_260/ORIGINAL_NICK_260.json'},
 'original_receipts':{'blob':'b0a548ce0945001f6560ce901bf5562e092fbc9a','sha256':'ae1a3499224d3dca05ed68a7b86cb6ee3d9443174e121129589b86bbb0e6519a','copy':'corrections/NICK_260/ORIGINAL_NICK_260_READ_RECEIPTS.json'},
 'rulings':{'C17':'VERIFIED (was UNSUPPORTED): 12.70% stock share of card balances 90+ days delinquent, 2025Q4; 7.13% is the separate annualised flow measure.',
            'C20':'PARTIAL: 14.3% = 2025Q3 student-loan flow into serious delinquency (14.26%), historically accurate but not latest at upload (2025Q4 16.19%, public 2026-02-10); $1.696T does not match NY Fed $1.66T; other parts unchecked.'},
 'not_used_as_proof':'Post-upload sources (2026Q1 report, Liberty Street Economics Aug 2026) are not used to date any ruling.',
 'unchanged':'Transcript, Text_SHA256, K01 tier, thumbnail, statuses, accepted count, all other claims and rows.',
 'before':old,'after':{'C17':c17,'C20':c20,'analysis':p['reviews'][0]['script']['analysis']},'sources_added':[s[0] for s in src]},
 open('corrections/NICK_260/NICK_260_CORRECTION_2026-11-01.json','w'),indent=1,ensure_ascii=False)
print('ok')
