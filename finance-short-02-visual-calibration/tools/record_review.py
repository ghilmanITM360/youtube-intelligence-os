"""Record a visual review only after the primary agent inspected the actual PNGs."""
import argparse,json,subprocess
from pathlib import Path
import build_assets as b
R=b.R
p=argparse.ArgumentParser();p.add_argument('scene',type=int);p.add_argument('finding');args=p.parse_args()
f=R/'manifests'/f'SCENE_{args.scene:02d}.json';d=json.loads(f.read_text());d['review_status']='NATIVE_MOBILE_REVIEWED';d['visual_finding']=args.finding;d['reviewer']='Primary agent visual inspection; independent human/owner approval pending';f.write_text(json.dumps(d,indent=2));b.refresh()
qa=R/'ASSET_QA.md'
if not qa.exists():qa.write_text('# Full static asset QA\n\nStructural tests do not certify artistic equivalence or audience comprehension. Owner full-package approval is pending. Native final compositions, every320px state contact and160px stress/simulated UI reviewed per scene. Source captions/attribution remain secondary at160px.\n\n')
with qa.open('a') as out:out.write(f'## Scene{args.scene:02d}\n\n{args.finding}\n\nReference: {b.REFS[args.scene]}. Broad technique is REFERENCE_SUPPORTED; the original staging is ART_DIRECTION_INFERENCE. Actual future easing/audio timing is NOT_YET_VERIFIED.\n\n')
prev=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R.parent,text=True).strip()
resume=R/'RESUME_HERE.md'
progress=json.loads((R/'PRODUCTION_PROGRESS.json').read_text());progress['latest_pre_commit_sha']=prev;progress['branch']='production/finance-short-02-assets';progress['draft_pr']='https://github.com/ghilmanITM360/youtube-intelligence-os/pull/30';(R/'PRODUCTION_PROGRESS.json').write_text(json.dumps(progress,indent=2))
with resume.open('a') as out:out.write(f'\nScene{args.scene:02d} reviewed. Current coverage:{progress["reviewed_scene_count"]}/7 reviewed,{progress["states_authored"]}/36 authored states. Previous synchronized checkpoint:{prev}. Next safe operation:scene{args.scene+1:02d} static artwork if <=7; otherwise final asset/contact/hash/clean-checkout validation. Exact current commit is `git rev-parse HEAD`; verify origin with `git ls-remote --heads origin production/finance-short-02-assets`. No self-referential commit SHA is fabricated.\n')
qa.write_text(qa.read_text().rstrip()+'\n')
resume.write_text(resume.read_text().rstrip()+'\n')
print('Recorded visual review',args.scene)
