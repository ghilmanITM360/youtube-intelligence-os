#!/usr/bin/env python3
"""Editable WI-0081 provisional animatic; original PIL composition + project art."""
from pathlib import Path
import csv, json, subprocess, math
from PIL import Image,ImageDraw,ImageFont,ImageOps
R=Path(__file__).resolve().parents[1]; O=R/'animatic'; W,H=1080,1920
sel={r['asset_id']:r['filename'] for r in csv.DictReader((R/'assets/qa/review_selection.csv').open())}
font='/System/Library/Fonts/Helvetica.ttc'; bold='/System/Library/Fonts/Helvetica.ttc'
def F(s): return ImageFont.truetype(font,s)
def txt(d,s,y,size=70,color='#171717',x=540): d.text((x,y),s,font=F(size),fill=color,anchor='mt',align='center')
def asset(im,id,box):
 p=R/sel[id]; a=Image.open(p).convert('RGBA'); bbox=a.getchannel('A').getbbox(); a=a.crop(bbox) if bbox else a
 a.thumbnail((box[2],box[3]),Image.Resampling.LANCZOS); im.alpha_composite(a,(int(box[0]-a.width/2),int(box[1]-a.height/2)))
def line(d,p,w=8,fill='#111111'):d.line(p,fill=fill,width=w,joint='curve')
def cup(d,x,y,scale=1,spoon=True,phase=0):
 def P(a,b): return (int(x+a*scale),int(y+b*scale))
 d.ellipse((*P(155,32),*P(240,135)),outline='#111111',width=max(2,int(7*scale)))
 d.polygon([P(0,0),P(160,0),P(147,170),P(15,170)],fill='white'); d.polygon([P(8,48),P(153,48),P(145,160),P(19,160)],fill='#C4C4C4')
 line(d,[P(0,0),P(15,165),P(145,165),P(160,0)],max(2,int(7*scale)))
 line(d,[P(5,47),P(155,47)],max(2,int(5*scale)))
 if spoon:
  line(d,[P(85,125),P(110+phase*9,-75)],max(2,int(7*scale)))
  d.ellipse((*P(72,113),*P(98,137)),outline='#111111',width=max(2,int(5*scale)))
def human(im,x=280,y=1040,h=560,pose='CHR-P04'):
 asset(im,pose,(x,y,h,h))
def stage(im,phase=0):
 d=ImageDraw.Draw(im); human(im,300,1010,720,'CHR-P04'); cup(d,485,1050,2.0,True,phase)
 # independent arm joins shoulder to spoon grip
 line(d,[(450,990),(485+2*(110+phase*9),900)],9)
 d.ellipse((685+phase*18-10,890,685+phase*18+10,910),fill='#111111')
def base(): return Image.new('RGBA',(W,H),'white')
# time, scene, spoken excerpt, illustrative type
S=[(0,3.5,'Could you boil a cup of water just by stirring it?','stir'),(3.5,7.9,'Short answer: no. But the spoon does try.','no'),(7.9,13.7,'Stirring adds energy; motion turns to heat.','energy'),(13.7,18.4,'A quarter liter of water at twenty degrees.','volume'),(18.4,23.5,'Lifting it eighty degrees takes 84,000 joules.','energycalc'),(23.5,27.6,'In two minutes: 700 watts going in.','watts'),(27.6,31.6,'Seven hundred-watt light bulbs.','bulbs'),(31.6,34.4,'About what a microwave draws to heat a mug.','microwave'),(34.4,37.3,'About one horsepower.','horse'),(37.3,41.0,'Niagara Falls warms water about a tenth of a degree.','niagara'),(41.0,47.7,'A hard stir adds well under one watt.','spoon'),(47.7,54.4,'Seven hundred needed, under one delivered.','compare'),(54.4,60.4,'The cup leaks heat away as fast as the spoon adds it.','loss'),(60.4,67.2,'Stir far faster than any hand; water cavitates.','fast'),(67.2,73.1,'Pressure drops behind the spoon and vapor bubbles form.','cavitation'),(73.1,79.1,'Unlike boiling, low pressure forms bubbles; splashing cools.','boil'),(79.1,84.9,'Stirring, dipping, or leaving tea alone: similar cooling.','tea'),(84.9,92.3,'Ordinary spoon, open cup? No. Near room temperature.','verdict'),(92.3,98.32,'A spoon is for dissolving sugar.','sugar')]
def render(kind,phase=0):
 im=base(); d=ImageDraw.Draw(im)
 if kind in ('stir','no','energy','loss','fast','verdict','sugar'):
  stage(im,phase);d=ImageDraw.Draw(im)
  title={'stir':'CAN STIRRING BOIL WATER?','no':'NO.','energy':'MOTION TO HEAT','loss':'HEAT IN  ≈  HEAT OUT','fast':'FASTER?','verdict':'NEAR ROOM TEMPERATURE','sugar':'A SPOON’S JOB'}[kind];txt(d,title,260,61,'#BC3544' if kind=='no' else '#161616')
  if kind=='energy':txt(d,'A LITTLE ENERGY',400,52)
  if kind=='sugar':
   
   if phase == 0: d.rectangle((595,1170,635,1210),outline='#111111',width=5,fill='white')
   txt(d,'DISSOLVE SUGAR',1470,62)
  if kind=='verdict':txt(d,'≈ 20 °C',490,96)
 elif kind in ('volume','energycalc','watts'):
  cup(d,380,815,2.2,False);txt(d,{'volume':'250 mL  •  20 °C','energycalc':'20 °C TO 100 °C','watts':'84,000 J  ÷  120 s'}[kind],380,67)
  txt(d,{'volume':'¼ LITER','energycalc':'≈ 84,000 J','watts':'≈ 700 W'}[kind],1350,105,'#BC3544')
 elif kind=='bulbs':
  txt(d,'700 W = 7 × 100 W',300,72)
  for i in range(7): asset(im,'BLB-01',(190+(i%4)*235,780+(i//4)*320,170,250))
 elif kind=='microwave':
  txt(d,'ABOUT A MICROWAVE',320,69);asset(im,'MWV-01',(540,980,760,500));txt(d,'≈ 700 W',1400,100)
 elif kind=='horse':
  txt(d,'≈ 1 HORSEPOWER',330,72);asset(im,'HRS-01',(540,1000,800,550))
 elif kind=='niagara':
  txt(d,'NIAGARA FALLS',280,68);asset(im,'NIA-01',(540,980,870,800));asset(im,'NIA-02',(540,980,870,800));txt(d,'≈ +0.1 °C',1480,92,'#BC3544')
 elif kind=='spoon':
  txt(d,'A HARD STIR',330,74);cup(d,350,830,2.5,True,phase);txt(d,'UNDER 1 W',1450,92,'#BC3544')
 elif kind=='compare':
  txt(d,'SAME POWER SCALE',290,68);txt(d,'700 W NEEDED',460,78);txt(d,'UNDER 1 W DELIVERED',1250,66)
  d.rectangle((140,650,940,760),fill='#B93B49'); d.rectangle((140,1430,142,1540),fill='#111111');line(d,[(140,1600),(940,1600)],5)
  txt(d,'0',1630,42,x=140);txt(d,'700 W',1630,42,x=900)
 elif kind=='cavitation':
  txt(d,'CAVITATION',290,78);txt(d,'LOW PRESSURE MAKES VAPOR',420,55)
  # direction right, bubbles confined to trailing left of spoon bowl
  line(d,[(720,730),(720,1060)],14);d.ellipse((620,1020,820,1110),fill='white',outline='#111111',width=9)
  for x,y,r in [(596,1062,12),(565,1050,9),(540,1077,8),(580,1090,7)]:d.ellipse((x-r,y-r,x+r,y+r),outline='#111111',width=5)
  line(d,[(720,900),(850,900)],7);line(d,[(850,900),(820,880)],7);line(d,[(850,900),(820,920)],7)
  txt(d,'SPOON MOVES RIGHT',1330,58)
 elif kind=='boil':
  txt(d,'CAVITATION  ≠  BOILING',300,65);asset(im,'CAV-03',(540,1000,700,570));txt(d,'BOILING: HEAT THROUGHOUT',1450,55)
 elif kind=='tea':
  txt(d,'ONE TEA EXPERIMENT',270,65)
  for x in (240,540,840):cup(d,x-75,790,0.9,False)
  for x,s in [(240,'STIR'),(540,'DIP'),(840,'WAIT')]:txt(d,s,1050,47,x=x)
  txt(d,'SIMILAR COOLING RATES',1370,59)
 return im.convert('RGB')
for i,(start,end,words,kind) in enumerate(S,1):
 im=render(kind);im.save(O/'scenes'/f'S{i:02}.png')
# independently editable source remains build_animatic.py; shot-level stills are review assets
sheet=Image.new('RGB',(5*216,4*420),'white');sd=ImageDraw.Draw(sheet)
for i,(start,end,words,kind) in enumerate(S,1):
 im=Image.open(O/'scenes'/f'S{i:02}.png');im.thumbnail((205,365));x=((i-1)%5)*216;y=((i-1)//5)*420;sheet.paste(im,(x,y));sd.text((x+5,y+367),f'S{i:02} {start:04.1f}s',fill='black',font=F(20))
sheet.save(O/'output/STORYBOARD.png')
with (O/'SHOT_LIST.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['shot','start_s','end_s','narration','visual','editable_scene','project_asset_ids']);
 for i,(a,b,n,k) in enumerate(S,1):w.writerow([f'S{i:02}',a,b,n,k,f'scenes/S{i:02}.png', {'stir':'CHR-P04','no':'CHR-P04','energy':'CHR-P04','bulbs':'BLB-01','microwave':'MWV-01','horse':'HRS-01','niagara':'NIA-01 NIA-02','boil':'CAV-03','loss':'CHR-P04','fast':'CHR-P04','verdict':'CHR-P04','sugar':'CHR-P04'}.get(k,'original PIL scene layers')])
# ffconcat still sequence; looping a second pose makes stirring visibly move.
with (O/'scenes/concat.txt').open('w') as f:
 f.write('ffconcat version 1.0\n')
 for i,(a,b,n,k) in enumerate(S,1):
  dur=b-a
  if k in ('stir','energy','fast','sugar'):
   render(k,1).save(O/'scenes'/f'S{i:02}b.png')
   t=0
   while t<dur-1e-6:
    sub=min(.4,dur-t); name=f'S{i:02}'+('b' if int(t/.4)%2 else '')+'.png';f.write(f"file '{name}'\nduration {sub:.4f}\n");t+=sub
  else:f.write(f"file 'S{i:02}.png'\nduration {dur:.4f}\n")
 f.write("file 'S19.png'\n")
print('Generated 19 scene cards and shot list')
