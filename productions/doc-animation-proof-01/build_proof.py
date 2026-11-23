"""Build the silent document proof from a reviewed, claim-bound render plan."""
import argparse
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1 = HERE.parent / 'new-original-video-v1-rent-01'
GATE = ROOT / 'CHANNEL_VISUAL_AUDIT/CHANNEL_001/CLOSURE2/tools'
sys.path[:0] = [str(V1 / 'tools'), str(GATE)]
import claim_gate


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON key {key!r}')
        result[key] = value
    return result


def load_json(path):
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_keys)


def backend_value(value):
    # The renderer uses tuples for RGB and coordinate sequences.
    return tuple(map(backend_value, value)) if isinstance(value, list) else value


def build_beats(renderer, document, plan, spec, capture_directory):
    """Translate only authorized calls, with no independently authored copy or amounts."""
    operations = {
        name: getattr(renderer, name)
        for name in claim_gate.RENDER_OPS - {'document'}
    }
    result = []
    for scene in plan['scenes']:
        beat = renderer.Beat(scene['start'], scene['end'], scene['description'], scene['narration'])
        for item in scene['items']:
            op = item['op']
            if op == 'document':
                beat.add(document.document_item(spec, scene['start'], capture_directory))
                continue
            element = operations[op](
                *map(backend_value, item['args']),
                **{key: backend_value(value) for key, value in item['kwargs'].items()},
            )
            beat.add(*(element if op == 'source' else [element]))
        result.append(beat)
    return result


def render_proof(renderer, beats, output, duration):
    path = output / 'DOC_PROOF_60s.mp4'
    if path.exists():
        raise ValueError(f'output already exists: {path}')
    ffmpeg = shutil.which('ffmpeg')
    if not ffmpeg:
        raise ValueError('ffmpeg is required for MP4 rendering')
    command = [
        ffmpeg, '-v', 'error', '-n', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
        '-s', '1920x1080', '-r', str(renderer.FPS), '-i', '-',
        '-vf', 'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p',
        '-c:v', 'libx264', '-preset', 'medium', '-crf', '17',
        '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
        '-an', str(path),
    ]
    count = round(duration * renderer.FPS)
    last_time = None
    with subprocess.Popen(command, stdin=subprocess.PIPE) as process:
        for frame in range(count):
            time = quantize(frame / renderer.FPS, renderer.CFPS)
            if time != last_time:
                pixels = renderer.render(beats, time).tobytes()
                last_time = time
            process.stdin.write(pixels)
    if process.returncode:
        raise subprocess.CalledProcessError(process.returncode, command)
    print(f'rendered {count} frames -> {path}')


def quantize(time, fps):
    return math.floor(time * fps + 1e-6) / fps


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--check', action='store_true', help='validate without producing outputs')
    modes.add_argument('--still', help='comma-separated seconds to render')
    parser.add_argument('--input-dir', type=Path, default=HERE)
    parser.add_argument('--output-dir', type=Path, default=HERE / 'out_verified')
    options = parser.parse_args(argv)

    try:
        folder = options.input_dir
        register = load_json(folder / 'claims.json')
        storyboard = load_json(folder / 'scenes.json')
        plan = load_json(folder / 'render_plan.json')
        spec = load_json(folder / 'doc_spec.json')
        relative = Path(spec['source']['file'])
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('document.source.file must be a relative capture path inside the input directory')
        capture = (folder / relative).read_bytes()
        report = claim_gate.authorize_render(register, storyboard, plan, spec, capture)
        print(f'claim gate: {report}')
        if not report.ok:
            return 1

        # Stage only bytes that passed the gate. The original may change after preflight.
        import doc_scene

        with TemporaryDirectory(prefix='claim-bound-capture-') as temporary:
            snapshot = Path(temporary) / relative
            snapshot.parent.mkdir(parents=True, exist_ok=True)
            snapshot.write_bytes(capture)
            doc_scene.validate_spec(spec, temporary)
            if options.check:
                print('resolved plan and document spec valid')
                return 0

            import v1r4_render as renderer

            renderer.NUMFONT = 'caveatbrush_CaveatBrush-Regular.ttf'
            renderer.PLAINFONT = 'atkinsonhyperlegible_AtkinsonHyperlegible-Regular.ttf'
            beats = build_beats(renderer, doc_scene, plan, spec, temporary)
            duration = plan['scenes'][-1]['end']
            output = options.output_dir
            if options.still is not None:
                times = [float(value) for value in options.still.split(',')]
                if any(not 0 <= time < duration for time in times):
                    raise ValueError(f'still time must be in [0, {duration})')
                stills = output / 'stills'
                stills.mkdir(parents=True, exist_ok=True)
                for time in times:
                    renderer.render(beats, quantize(time, renderer.CFPS)).save(stills / f'p_{time:g}.png')
            else:
                output.mkdir(parents=True, exist_ok=True)
                render_proof(renderer, beats, output, duration)
            document_start = next(
                scene['start'] for scene in plan['scenes']
                if any(item['op'] == 'document' for item in scene['items'])
            )
            events = [{
                'event': event, 'scene_local_s': time, 'global_s': round(document_start + time, 3),
                'content_frame_24': frame, 'global_content_frame_24': frame + round(document_start * 24),
            } for event, time, frame in doc_scene.event_table(spec)]
            (output / 'timing_track.json').write_text(json.dumps({
                'note': 'Planned narration timing only. No recorded speech was validated.',
                'clauses': plan['planned_clauses'], 'doc_scene_t0_s': document_start, 'doc_events': events,
                'render_plan_sha256': claim_gate.payload_digest(plan),
            }, indent=1) + '\n', encoding='utf-8')
    except (KeyError, TypeError, ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f'RENDER REFUSED: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
