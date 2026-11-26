"""Usage: strip.py OUT.png T1 T2 ...  -> renders stills (tools/v13.py --stills) and tiles those frames at 270x480."""
import subprocess, sys
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]
out, ts = sys.argv[1], [float(x) for x in sys.argv[2:]]
subprocess.run([sys.executable, str(ROOT / 'tools/v13.py'), '--stills', *map(str, ts)], check=True, capture_output=True)
ims = [Image.open(ROOT / f'qa/stills/t{t:06.2f}.png').resize((270, 480)) for t in ts]
s = Image.new('RGB', (270 * len(ims), 480)); [s.paste(im, (270 * i, 0)) for i, im in enumerate(ims)]; s.save(out)
