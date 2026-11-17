"""Pillarboxed Shorts thumbnails must not hash-match just because of their side bars."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'scripts'))
from check_channel_slop_risk import thash  # noqa: E402


def test_pillarbox_bars_do_not_make_images_match(tmp_path):
    from PIL import Image, ImageDraw
    paths = []
    for i, draw in enumerate((lambda d: d.ellipse((520, 200, 760, 520), fill=0), lambda d: d.rectangle((460, 40, 600, 300), fill=0))):
        im = Image.new('L', (1280, 720), 128); d = ImageDraw.Draw(im)
        d.rectangle((438, 0, 842, 720), fill=250); draw(d)
        im.save(tmp_path / f'{i}.png'); paths.append(tmp_path / f'{i}.png')
    assert bin(thash(paths[0]) ^ thash(paths[1])).count('1') > 5
