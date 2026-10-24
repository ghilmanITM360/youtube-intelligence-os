import json,sys
R="/Users/ghilmankhan/YIOS-local-audits/2026-10-24-Uumnx2Fo6cE-deep-ct-scan/agents/shard_1/p/"
PRES="Presenter: hand-drawn stick figure at right (x~0.72-0.97, y~0.2-0.95), round peach head, black scribble hair, dot eyes, curved mouth, thin black limbs, long brown pointer stick"
def E(ep,v,t,d,sb,conf,motion=None):
    return dict(ep=ep,verdict=v,type=t,desc=d,shot_boundary=sb,motion=motion,confidence=conf)
def S(id,objects,background,illustration,typography,readable,unreadable,hierarchy,entry_exit,story,evidence,conf,continuity,recon,prompt,family,camera="STATIC 2D"):
    return dict(id=id,objects=objects,background=background,illustration=illustration,typography=typography,readable_text=readable,unreadable_text=unreadable,hierarchy=hierarchy,camera_motion=camera,entry_exit=entry_exit,story_function=story,evidence=evidence,confidence=conf,continuity=continuity,recon=recon,prompt=prompt,family=family)
def dump(name,eps,sts):
    json.dump(dict(eps=eps,sts=sts),open(R+name+".json","w"),indent=1)
    print(name,len(eps),len(sts))
