"""Generate (never auto-merge) perceptual-hash near-duplicate candidates among thumbnails."""
import csv, numpy as np
from pathlib import Path
HERE = Path(__file__).resolve().parent
U = {r['Thumbnail_ID']: r for r in csv.DictReader((HERE / 'thumbnail-universe.csv').open()) if r['Thumbnail_ID']}
F = list(csv.DictReader((HERE / 'visual-features.csv').open()))
b = lambda h: np.unpackbits(np.frombuffer(bytes.fromhex(h), dtype=np.uint8))
P = np.array([b(r['PHash']) for r in F]); D = np.array([b(r['DHash']) for r in F])
dp = (P[:, None, :] != P[None, :, :]).sum(2); dd = (D[:, None, :] != D[None, :, :]).sum(2)
out = []
for i, j in zip(*np.triu_indices(len(F), 1)):
    if dp[i, j] <= 10 and dd[i, j] <= 14:
        a, c = U[F[i]['Thumbnail_ID']], U[F[j]['Thumbnail_ID']]
        same_ch = a['Channel_ID'] == c['Channel_ID']
        res = 'SAME_CREATIVE_DIFFERENT_RESOLUTION' if (a['Width'], a['Height']) != (c['Width'], c['Height']) and dp[i, j] <= 4 else 'OTHER_SIMILARITY'
        out.append(dict(Candidate_ID=f'VFC-{len(out)+1:03d}', Thumbnail_ID_A=a['Thumbnail_ID'], Video_ID_A=a['Video_ID'], Channel_A=a['Channel_ID'],
                        Thumbnail_ID_B=c['Thumbnail_ID'], Video_ID_B=c['Video_ID'], Channel_B=c['Channel_ID'], Same_Channel=same_ch,
                        PHash_Distance=int(dp[i, j]), DHash_Distance=int(dd[i, j]), Similarity_Score=round(1 - (dp[i, j] + dd[i, j]) / 128, 4),
                        Candidate_Type=res, Title_A=a['Title'], Title_B=c['Title'], Reviewer_Status='CANDIDATE', Visual_Family_ID='', Review_Notes=''))
with (HERE / 'visual-family-candidates.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, list(out[0])); w.writeheader(); w.writerows(out)
print(len(out))
