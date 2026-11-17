import csv, hashlib, shutil, subprocess, sys
from pathlib import Path
from PIL import Image

asset, source, mode, *args = sys.argv[1:]
attempt = 1
if args and args[-1].startswith('attempt='):
    attempt = int(args.pop().split('=')[1])
suffix = '' if attempt == 1 else f'-v{attempt}'
root = Path(__file__).resolve().parents[2]
native = root / 'assets/raw' / (asset + '-new' + suffix + '_native.png')
delivery = root / 'assets/gen' / (asset + suffix + '.png')
if native.exists() or delivery.exists():
    raise SystemExit('Refusing to overwrite an existing version')
shutil.copyfile(source, native)
subprocess.run([sys.executable, str(root / 'assets/qa/normalize.py'), str(native), str(delivery), mode, *args], check=True)
im, raw = Image.open(delivery), Image.open(native)
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
with (root / 'assets/MANIFEST.csv').open('a', newline='') as f:
    csv.writer(f).writerow([asset, str(delivery.relative_to(root)), digest(delivery), *im.size, im.mode,
        'generated', attempt, 'PENDING_QUALITY', 'New generation; native ' + str(native.relative_to(root)) + '; QA pending',
        digest(native), *raw.size])
