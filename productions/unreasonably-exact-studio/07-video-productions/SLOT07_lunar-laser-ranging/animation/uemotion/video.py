"""Deterministic clip renderer: scene(cv, ctx) is a pure function of time; frames are rendered in parallel (fork pool),
streamed to ffmpeg (h264 / yuv420p), with proof frames (start / middle / end PNG), frame statistics and ffprobe output."""
import json, math, multiprocessing as mp, os, subprocess
from dataclasses import dataclass, field
import numpy as np
from PIL import Image
from . import tokens as T
from .canvas import Canvas
from .timeline import ClockSet, ModelClock
from .narration import MASTER_WAV
from .captions import CaptionRenderer


@dataclass
class ClipSpec:
    id: str; name: str; n0: float; duration: float; scene: callable
    model: ModelClock = None
    captions: bool = False
    audio: bool = True                 # also write a separate muxed audio-slice preview (master is only read)
    cues: dict = field(default_factory=dict)       # name -> narration_t ; extra evidence frames are dumped at these
    ss: int = 2
    blur: tuple = (1, 0.0)             # (temporal samples, shutter as a fraction of a frame): time-sampled motion blur, free because scenes are pure functions of t

_G = {}
def _init(spec, scale, fps):
    import cv2
    cv2.setNumThreads(0); _G.update(spec=spec, scale=scale, fps=fps, caps=CaptionRenderer())

def render_frame(spec, i, scale, fps, caps=None):
    """one frame as a PIL RGB image: pure function of (spec, i, fps, scale). Motion blur = mean of `samples` sub-frame renders
    spread over `shutter` frames (captions are drawn once, sharp, at the frame time)."""
    clocks = ClockSet(spec.n0, spec.model); S_, shutter = spec.blur; acc = None
    for k in range(S_):
        off = 0.0 if S_ == 1 else (k / (S_ - 1) - 0.5) * shutter
        ctx = clocks.at((i + off) / fps, frame=i, fps=fps, scale=scale)
        cv = Canvas(scale=scale, ss=spec.ss, bg=T.BG); spec.scene(cv, ctx)
        a = np.asarray(cv.to_image().convert('RGB'), np.float32); acc = a if acc is None else acc + a
    im = Image.fromarray((acc / S_ + 0.5).astype(np.uint8))
    if spec.captions:
        cv = Canvas(scale=scale, ss=spec.ss, bg=None); (caps or CaptionRenderer()).draw(cv, clocks.at(i / fps).n)
        top = cv.im.resize(cv.out_size, Image.BOX) if cv.ss > 1 else cv.im
        im = Image.alpha_composite(im.convert('RGBA'), top).convert('RGB')
    return im

def _work(i):
    s = _G['spec']; return i, np.asarray(render_frame(s, i, _G['scale'], _G['fps'], _G['caps']), np.uint8).tobytes()


def render_clip(spec, out_dir, scale=0.5, fps=30, workers=None, quiet=False):
    os.makedirs(out_dir, exist_ok=True)
    N = int(round(spec.duration * fps)); sz = (int(round(T.DESIGN_W * scale)), int(round(T.DESIGN_H * scale)))
    mp4 = os.path.join(out_dir, '%s.mp4' % spec.name)
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '%dx%d' % sz, '-r', str(fps), '-i', '-',
                           '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '14', '-preset', 'medium', '-movflags', '+faststart', mp4], stdin=subprocess.PIPE)
    from . import space; space.warm()
    ctx = mp.get_context('fork'); pool = ctx.Pool(workers or max(1, (os.cpu_count() or 4) - 1), initializer=_init, initargs=(spec, scale, fps))
    stats = dict(mean_luma=[], max_luma=[], diff=[]); prev = None; keep = {}
    want = {0, N // 2, N - 1}
    for name, nt in spec.cues.items():
        want.add(min(N - 1, max(0, int(round((nt - spec.n0) * fps)))))
    try:
        for i, buf in pool.imap(_work, range(N), chunksize=3):
            ff.stdin.write(buf)
            a = np.frombuffer(buf, np.uint8).reshape(sz[1], sz[0], 3)
            g = a.astype(np.float32) @ np.array([0.2126, 0.7152, 0.0722], np.float32)
            stats['mean_luma'].append(float(g.mean())); stats['max_luma'].append(float(g.max()))
            gs = g[::4, ::4]; stats['diff'].append(float(np.abs(gs - prev).mean()) if prev is not None else 0.0); prev = gs
            if i in want: keep[i] = Image.fromarray(a.copy())
            if not quiet and i % 60 == 0: print('  %s frame %d/%d' % (spec.id, i, N), flush=True)
    finally:
        pool.close(); pool.join(); ff.stdin.close(); ff.wait()
    assert ff.returncode == 0, 'ffmpeg failed'
    for tag, i in (('start', 0), ('middle', N // 2), ('end', N - 1)): keep[i].save(os.path.join(out_dir, '%s_%s.png' % (spec.name, tag)))
    cue_files = {}
    for name, nt in spec.cues.items():
        i = min(N - 1, max(0, int(round((nt - spec.n0) * fps)))); fn = 'cue_%s_%s.png' % (spec.name, name); keep[i].save(os.path.join(out_dir, fn)); cue_files[name] = (nt, i, fn)
    probe = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-count_frames', '-show_entries',
                            'stream=codec_name,pix_fmt,width,height,r_frame_rate,nb_read_frames,duration', '-of', 'json', mp4], capture_output=True, text=True)
    pj = json.loads(probe.stdout)['streams'][0]
    audio_mp4 = None
    if spec.audio:
        audio_mp4 = os.path.join(out_dir, '%s_audio_preview.mp4' % spec.name)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', mp4, '-ss', '%.3f' % spec.n0, '-t', '%.3f' % spec.duration, '-i', MASTER_WAV,
                        '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-shortest', audio_mp4], check=True)
    d = np.array(stats['diff'][1:]); res = dict(frames=N, fps=fps, size=sz, mp4=mp4, audio_preview=audio_mp4, ffprobe=pj, cue_frames=cue_files,
                                              diff_mean=float(d.mean()), diff_max=float(d.max()), diff_min=float(d.min()),
                                              static_frames=int((d < 0.02).sum()), max_luma=float(max(stats['max_luma'])),
                                              max_mean_luma_step=float(np.abs(np.diff(stats['mean_luma'])).max()), stats=stats)
    json.dump({k: v for k, v in res.items() if k != 'stats'} | dict(stats_series=stats), open(os.path.join(out_dir, '%s_frame_stats.json' % spec.name), 'w'))
    return res
