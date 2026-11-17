from PIL import Image, ImageDraw
from pathlib import Path
import sys
base=Path(__file__).resolve().parents[1]/'WhatIf_Complete_Extraction/00_SOURCE_AUDIT'
nums=[int(x) for x in sys.argv[1:]]
out=Image.new('RGB',(840*3,1110*((len(nums)+2)//3)),'#aaaaaa')
for k,n in enumerate(nums):
    im=Image.open(base/f'previews/page_{n:03d}.jpg');x=(k%3)*840;y=(k//3)*1110
    out.paste(im,(x,y+30));ImageDraw.Draw(out).text((x+20,y+5),f'PDF {n} / PRINTED {n-15}',fill='black')
out.save(base/'montage.jpg',quality=94)
print(base/'montage.jpg')
