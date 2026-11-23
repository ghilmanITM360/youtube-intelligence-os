from pathlib import Path
import ctypes.util,io,json,hashlib,subprocess
f=ctypes.util.find_library
ctypes.util.find_library=lambda n:'/opt/homebrew/lib/libcairo.2.dylib' if n=='cairo' else f(n)
import cairosvg
from PIL import Image,ImageDraw,ImageFont
P=Path(__file__).parent
src=(P.parent/'master_candidate/master_refined.svg').read_text()
head=src.split('<!-- ears, original warm face shape -->')[1].split('<!-- face features -->')[0]
# Local, deterministic deviations to the shared face and hair contours.
head=head.replace('C 365 170 492 80 652 83','C 358 173 487 74 652 83').replace('C 815 86 936 176 938 322','C 818 91 940 170 938 322').replace('C 500 647 382 574 370 444','C 493 651 385 578 370 444').replace('C 823 91 854 109 858 140','C 826 88 853 113 858 140')
ink='#1f2430'
features={
'neutral':'<path d="M 493 348 Q 521 329 548 343 M 742 343 Q 773 334 797 349 M 625 480 Q 649 476 675 480"/>',
'smile':'<path d="M 493 348 Q 521 331 548 343 M 742 343 Q 773 334 797 349 M 615 469 Q 648 508 688 466"/>',
'worried':'<path d="M 493 345 Q 520 316 548 332 M 742 332 Q 768 318 797 347 M 620 494 Q 635 476 650 487 Q 664 497 681 483"/>',
'surprised':'<path d="M 490 319 Q 520 298 550 315 M 740 315 Q 771 299 801 320"/><ellipse cx="650" cy="484" rx="21" ry="27"/>',
'smirk':'<path d="M 490 329 Q 519 307 549 327 M 742 347 Q 770 337 797 349 M 619 481 Q 652 490 683 464"/>'}
base='<ellipse cx="521" cy="393" rx="13" ry="20" fill="#1f2430" stroke="none"/><ellipse cx="773" cy="393" rx="13" ry="20" fill="#1f2430" stroke="none"/>'
def svg(w,h,content):return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{content}</svg>'
def write(name,s,w,h):
 (P/(name+'.svg')).write_text(s)
 data=cairosvg.svg2png(bytestring=s.encode(),output_width=w*2,output_height=h*2)
 Image.open(io.BytesIO(data)).convert('RGBA').resize((w,h),Image.Resampling.LANCZOS).save(P/(name+'.png'))
for name,feat in features.items():
 content=f'<g transform="translate(-261 40) scale(0.94)" stroke="{ink}" stroke-linecap="round" stroke-linejoin="round">{head}<g fill="none" stroke-width="18">{feat}</g>{base}</g>'
 write('rig_head_'+name,svg(700,700,content),700,700)
# Shared body from the established master: all poses keep neck, torso, legs and footwear fixed.
body=src.split('<!-- neck, torso and hands -->')[1].split('<!-- ears, original warm face shape -->')[0]
body=body.replace(body[body.index('<path d="M 550 1118'):body.index('<!-- white sneakers -->')],'')
legs='<g fill="none" stroke-width="45"><path d="M 612,1152 C 615,1300 603,1480 594,1748"/><path d="M 688,1152 C 686,1328 699,1509 705,1748"/></g>'
arms={
'down':'<path d="M 611 718 C 567 830 552 983 548 1134 M 689 718 C 732 834 747 985 752 1134"/><path d="M 550 1118 C 525 1117 513 1135 514 1154 C 515 1176 528 1189 547 1189 C 566 1189 580 1173 579 1153 C 578 1135 568 1119 550 1118 Z M 750 1118 C 725 1119 720 1136 721 1154 C 722 1174 733 1189 752 1189 C 772 1189 785 1173 785 1154 C 784 1135 771 1117 750 1118 Z" fill="#d99060" stroke-width="19"/>',
'shrug':'<path d="M 610 720 C 571 776 536 848 496 891 C 449 880 404 854 367 825 M 690 720 C 730 780 760 849 803 891 C 850 881 899 854 934 825"/><path d="M 371 826 C 350 845 324 834 315 820 Q 305 801 327 802 L 352 802 Q 340 781 352 778 Q 366 782 380 800 Q 389 811 382 821 Z M 930 826 C 951 845 977 834 986 820 Q 996 801 974 802 L 949 802 Q 961 781 949 778 Q 935 782 921 800 Q 912 811 919 821 Z" fill="#d99060" stroke-width="19"/>',
'point':'<path d="M 611 718 C 567 830 552 983 548 1134 M 689 718 C 749 742 790 775 834 788 C 924 788 1015 786 1100 786"/><path d="M 550 1118 C 525 1117 513 1135 514 1154 C 515 1176 528 1189 547 1189 C 566 1189 580 1173 579 1153 C 578 1135 568 1119 550 1118 Z M 1085 766 Q 1094 749 1115 757 L 1166 764 Q 1182 766 1181 776 Q 1180 785 1164 785 L 1134 785 Q 1154 794 1147 806 Q 1134 818 1108 806 L 1085 801 Z" fill="#d99060" stroke-width="19"/>'}
for name,a in arms.items():
 w=1500 if name=='point' else 1300; shift=100 if name=='point' else 0
 c=f'<g transform="translate({shift} -600)" stroke="{ink}" stroke-linecap="round" stroke-linejoin="round">{legs}<g fill="none" stroke-width="45">{a}</g>{body}</g>'
 write('rig_body_'+name,svg(w,1300,c),w,1300)
anchors={'units':'pixels','heads':{n:{'chin':[350,651]} for n in features},'bodies':{n:{'neck':[750 if n=='point' else 650,70]} for n in arms},'note':'Place head chin at body neck; chin overlaps neck stub. Body y=0 corresponds to master y=600. Point has 100px horizontal padding.'}
(P/'rig_anchors.json').write_text(json.dumps(anchors,indent=2))
def composite(pose,expression):
 b=Image.open(P/f'rig_body_{pose}.png'); h=Image.open(P/f'rig_head_{expression}.png'); canvas=Image.new('RGBA',(1500,1900)); bx=100 if pose!='point' else 0
 canvas.alpha_composite(b,(bx,600)); canvas.alpha_composite(h,(400,19)); return canvas
master=composite('down','neutral');master.save(P/'master_provisional.png')
# Scene-scale contact sheet: same placement at 510 px body figure height, actual 1920x1080 pixels.
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',28)
sheet=Image.new('RGB',(1920,1080),'#fdfdfb');d=ImageDraw.Draw(sheet)
for i,(pose,ex) in enumerate([('down','neutral'),('shrug','worried'),('point','surprised'),('down','smile'),('down','smirk')]):
 im=composite(pose,ex); im.thumbnail((440,550),Image.Resampling.LANCZOS); x=15+i*380;sheet.paste(im,(x+35,185),im);d.text((x+25,765),pose+' / '+ex,fill='#333333',font=font)
d.text((35,35),'V1 Rent — provisional character family, equal scene scale',fill='#333333',font=font)
sheet.save(P/'character_consistency.jpg',quality=94)
# Original versus controlled refinement at equal scale.
compare=Image.new('RGB',(1920,1080),'#fdfdfb');dr=ImageDraw.Draw(compare)
for x,img,label in [(220,Image.open(P.parent/'master_candidate/master_refined.png'),'Previous master'),(1040,master,'Controlled refinement')]:
 img.thumbnail((650,800),Image.Resampling.LANCZOS);compare.paste(img,(x,135),img);dr.text((x,65),label,fill='#333333',font=font)
compare.save(P/'master_comparison_1080p.jpg',quality=94)
# Full-resolution preview: deliberately held poses; smooth, small position motion, explicit pose switching.
seq=[('down','neutral'),('shrug','worried'),('point','surprised'),('down','smile'),('shrug','smirk')]
frames=[]
for i,(pose,ex) in enumerate(seq):
 img=composite(pose,ex);img.thumbnail((650,780),Image.Resampling.LANCZOS)
 for j in range(60):
  plate=Image.new('RGB',(1920,1080),'#fdfdfb');y=155+round(3*__import__('math').sin(j/60*6.283));plate.paste(img,(640,y),img);d=ImageDraw.Draw(plate);d.text((55,45),f'V1 RENT  |  {pose.upper()}  /  {ex.upper()}  |  provisional',font=font,fill='#555555');frames.append(plate)
proc=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s','1920x1080','-r','30','-i','-','-an','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(P/'character_motion_preview.mp4')],stdin=subprocess.PIPE)
for frame in frames:proc.stdin.write(frame.tobytes())
proc.stdin.close();assert proc.wait()==0
for name in ['rig_body_down','rig_body_shrug','rig_body_point']+['rig_head_'+x for x in features]+['master_provisional']:
 im=Image.open(P/(name+'.png'));print(name,im.size,im.getbbox())
