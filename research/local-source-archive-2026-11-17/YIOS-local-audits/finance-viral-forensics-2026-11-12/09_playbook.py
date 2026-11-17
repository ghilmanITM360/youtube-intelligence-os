import numpy as np,pandas as pd,re,warnings
warnings.filterwarnings('ignore')
import statsmodels.formula.api as smf
from statsmodels.stats.multitest import multipletests
L=pd.read_pickle('out/long_classified2.pkl'); T=L.title.fillna('')
fam={'F01_curiosity_mystery (Playbook title family 01)':r"(what really happened|the real reason|nobody|no one|untold|hidden|dark side|than you think|secret|truth about|what they don't|never told)",
'F02_failure_downfall (family 02)':r"(rise and fall|collapse|destroyed|what went wrong|died|dying|dead|failed|failure|bankrupt|downfall|crash|ruin)",
'F03_contradiction_irony (family 03)':r"(\bbut\b|so why|paradox|actually|ironic|yet\b|instead|wrong|myth|backwards)",
'F05_explainer_ranking (family 05)':r"(explained|how .{2,40} works|vs\.?|versus|ranked|every |complete guide|\d+ (ways|things|types|levels))",
'F09_problems_tradeoffs_utility (family 09)':r"(mistakes?|should you|worth it|trap|avoid|stop |before you|checklist|how to|don't|do this)",
'F10_conflict_stakes_whatif (family 10)':r"(what if|vs\.?|versus|war|fight|battle|if .{1,30} (disappeared|stopped|ended)|imagine)",
'F04_character_POV (family 04)':r"(\bpov\b|\bi\b|\bmy\b|you (became|woke|won|inherited)|story of)"}
rows=[]
for k,p in fam.items():
    L['f']=T.str.contains(p,case=False,regex=True).astype(float); n1=int(L.f.sum())
    m=smf.ols('logPI~f',L).fit(cov_type='cluster',cov_kwds={'groups':L.channel_id.astype('category').cat.codes}); pos=tot=0
    for cid,g in L.groupby('channel_id'):
        a=g[g.f==1].logPI;b=g[g.f==0].logPI
        if len(a)>=4 and len(b)>=4: tot+=1;pos+=a.mean()>b.mean()
    rows.append(dict(playbook_family=k,n_with=n1,n_without=len(L)-n1,median_PI_with=L[L.f==1].PI.median(),median_PI_without=L[L.f==0].PI.median(),ratio=np.exp(m.params['f']),ci_lo=np.exp(m.conf_int().loc['f',0]),ci_hi=np.exp(m.conf_int().loc['f',1]),p=m.pvalues['f'],ch_pos=pos,ch_tot=tot))
R=pd.DataFrame(rows); R['q_BH']=multipletests(R.p,method='fdr_bh')[1]; R.to_csv('out/playbook_title_family_tests.csv',index=False); print(R.round(3).to_string())
