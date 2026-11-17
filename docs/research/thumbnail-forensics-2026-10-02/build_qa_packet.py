"""Build adversarial-QA reviewer packets: python3 build_qa_packet.py B002-04 [seq,seq,...]
Default rows = qa_select.pick(batch). Writes <scratch>/audit/<batch>/qa_packet_<tag>.json (tag = 'S' sample or 'F' full)."""
import json, sys
from pathlib import Path
from qa_select import pick, SCR, HERE

bid = sys.argv[1]
rows = {r['Thumbnail_ID']: r for r in json.loads((HERE / f'audit-batch-{bid}.json').read_text())}
inp = {i['Thumbnail_ID']: i for i in json.loads((SCR / bid / 'input.json').read_text())}
want = [r['Thumbnail_ID'] for r in rows.values() if r['seq'] in {int(x) for x in sys.argv[2].split(',')}] if len(sys.argv) > 2 else pick(bid)
out = []
for t in sorted(want, key=lambda t: rows[t]['seq']):
    i = inp[t]
    out.append(dict(seq=rows[t]['seq'], view_path=i['View_Path'], title=i['Title'], channel=i['Channel_Name'], niche=i['Niche_Label'], format=i['Format'], native_size=i['Native_Size'], audit_row=rows[t]))
tag = 'F' if len(sys.argv) > 2 else 'S'
(SCR / bid / f'qa_packet_{tag}.json').write_text(json.dumps(out, indent=1))
print(bid, [o['seq'] for o in out])
