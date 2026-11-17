from pathlib import Path
from PIL import Image, ImageFilter
import numpy as np, json
root=Path(__file__).resolve().parents[2];gen=root/'assets/gen'; out={}
def image(name):return Image.open(gen/(name+'.png')).convert('RGBA')
def ink(im):
 a=np.array(im).astype(int);return (a[:,:,:3].max(2)<80)&(a[:,:,3]>200)
def dilate(mask):return np.array(Image.fromarray(mask.astype('uint8')*255).filter(ImageFilter.MaxFilter(3)))>0
m1,m2=ink(image('MUG-01')),ink(image('MUG-02'))
out['MUG-01_vs_MUG-02']={'ink_pixels_1':int(m1.sum()),'ink_pixels_2':int(m2.sum()),'fraction_1_within_1px':float((m1&dilate(m2)).sum()/max(m1.sum(),1)),'fraction_2_within_1px':float((m2&dilate(m1)).sum()/max(m2.sum(),1))}
def centered(im):
 canvas=Image.new('RGBA',(1000,1000));canvas.alpha_composite(im,((1000-im.width)//2,(1000-im.height)//2));return canvas
base=centered(image('SPN-01'))
for id,angle in [('SPN-02',-20),('SPN-03',20)]:
 expected=np.array(base.rotate(angle,resample=Image.Resampling.BICUBIC).getchannel('A'))>128
 actual=np.array(centered(image(id)).getchannel('A'))>128
 out[id]={'silhouette_iou':float((expected&actual).sum()/max((expected|actual).sum(),1)),'required_min':.97,'note':'Canvas-centered comparison; pivot placement not independently established'}
for id in ('WTR-01-v4','WTR-02-v4','WTR-03-v4'):
 a=np.array(image(id));rgb=a[:,:,:3]; mask=(a[:,:,3]>250)&(rgb[:,:,0]>160)&(np.ptp(rgb.astype(int),axis=2)<8)
 if mask.any():
  colors,counts=np.unique(rgb[mask].reshape(-1,3),axis=0,return_counts=True);out[id]={'dominant_gray':colors[counts.argmax()].tolist()}
out['not_checked']=['THM-02 pivot through all rotations','water clipping against the selected MSK-01','actual prop stage geometry']
(root/'assets/qa/prop_checks_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
