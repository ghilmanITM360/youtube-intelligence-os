exec(open('/Users/ghilmankhan/workprojects/yios-recovery-status/finance-final-qa/review_sequences.py').read().split('canvas=')[0])
for mid,a,n in [('M0018',8.933333,14),('M0032',16.933333,32),('M0023',11.6,10),('M0034',21.366667,10)]:
 can=Image.new('RGB',(8*270,((n+7)//8)*510),'white');d=ImageDraw.Draw(can)
 for j in range(n):
  t=a+j/30;p=out/f'detail-{mid}-{j}.png';subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-ss',str(t),'-i',str(source),'-frames:v','1','-vf','scale=270:480','-y',str(p)],check=True)
  with Image.open(p) as im:can.paste(im,((j%8)*270,(j//8)*510+30))
  d.text(((j%8)*270,(j//8)*510),f'{mid} {t:.5f}',fill='black')
 can.save(out/f'{mid}-detail.png')
print(out)
