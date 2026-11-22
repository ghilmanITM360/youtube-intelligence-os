import pathlib
import re
import subprocess

root = pathlib.Path(__file__).resolve().parents[1]
media = pathlib.Path.home() / "workprojects/videos in mp3/CasuallyFinance"
windows = [
    ("7K991LgY3tc", 0, 28, 30, 4, "debt"),
    ("Xkk9GnnJHBg", 71, 78, 6, 7, "oil"),
    ("dPoDyl9Ys38", 0, 31, 48, 4, "bitcoin"),
    ("7uu6qaCGZsY", 145, 176, 60, 4, "credit"),
    ("OC1yu0L7jT4", 310, 341, 60, 4, "japan"),
    ("10nEByVLya0", 0, 18, 30, 4, "short"),
    ("rent", 0, 122, 90, 5, "rent"),
]
for video, start, end, stride, columns, name in windows:
    source = next(media.glob("*" + video + "*.mp4")) if video != "rent" else pathlib.Path(
        "productions/new-original-video-v1-rent-01/out_full/V1_RENT_FULL_R9b_assembled.mp4")
    rule = f"between(t,{start},{end})*not(mod(n,{stride}))"
    width, height = (160, 284) if name == "short" else (320, 180)
    log = subprocess.run([
        "ffmpeg", "-nostdin", "-hide_banner", "-i", str(source), "-an", "-vf",
        f"select='{rule}',showinfo,scale={width}:{height},tile={columns}x{12 if name=='oil' else 10}",
        "-frames:v", "1", "-y", str(root / "frames" / (name + ".jpg"))],
        capture_output=True, text=True, check=True).stderr
    frames = re.findall(r"n:\s*(\d+) pts:\s*\S+ pts_time:\s*(\S+)", log)
    (root / "measurements" / (name + "_frames.csv")).write_text(
        "sheet_index,source_pts_s\n" + "".join(f"{i},{pts}\n" for i, pts in frames))

for video, name, first, last, fps in [
    ("Xkk9GnnJHBg", "oil_entry", 1772, 1783, 24),
    ("Xkk9GnnJHBg", "oil_ring", 1799, 1817, 24),
    ("yViMyIVOHkQ", "bankruptcy_ring", 6658, 6684, 24),
    ("yViMyIVOHkQ", "cnbc_ring", 4956, 4974, 24),
    ("Im-N3K9Pnf0", "underline", 6024, 6040, 30),
    ("dPoDyl9Ys38", "yellow", 138, 168, 24),
    ("rent", "rent_correction", 7462, 7480, 30),
]:
    source = next(media.glob("*" + video + "*.mp4")) if video != "rent" else pathlib.Path(
        "productions/new-original-video-v1-rent-01/out_full/V1_RENT_FULL_R9b_assembled.mp4")
    seek = first // fps
    start, end = first - seek * fps, last - seek * fps
    log = subprocess.run([
        "ffmpeg", "-nostdin", "-hide_banner", "-ss", str(seek), "-t", "3",
        "-i", str(source), "-an", "-vf",
        f"select='between(n,{start},{end})',showinfo,scale=384:-1,tile=5x{(last-first+5)//5}",
        "-frames:v", "1", "-y", str(root / "frames" / (name + ".jpg"))],
        capture_output=True, text=True, check=True).stderr
    frames = re.findall(r"n:\s*(\d+) pts:\s*\S+ pts_time:\s*(\S+)", log)
    (root / "measurements" / (name + "_frames.csv")).write_text(
        "sheet_index,source_pts_s,frame_zero_based\n" +
        "".join(f"{i},{seek + float(pts):.6f},{first + int(i)}\n" for i, pts in frames))
