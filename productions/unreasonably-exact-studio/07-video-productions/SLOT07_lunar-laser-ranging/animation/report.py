"""PROOF_REPORT.md writer. Programmatic facts are filled automatically from the render + checks; the human review
(defects found by viewing frames, corrections, re-test) is read from proofs/notes/<ID>.json written by the reviewer."""
import json, os

NOTES = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'proofs', 'notes')

def write(pid, mod, out, results, checks, args):
    info = mod.INFO; notes = {}
    p = os.path.join(NOTES, pid + '.json')
    if os.path.exists(p): notes = json.load(open(p))
    L = []; A = L.append
    A('# %s\n' % info['title'])
    A('**Status: candidate.** %s\n' % notes.get('status_note', 'Reviewed as still frames and frame-difference statistics only; the moving clip was not watched in real time. Not approved (only the owner approves).'))
    A('Beats / timing: %s\n' % info['beats'])
    A('## Expected behaviour\n\n%s\n' % info['expected'])
    A('## Files\n')
    for name, r in results.items():
        A('- `%s` (%dx%d, %d fps, %d frames, %s %s)' % (os.path.basename(r['mp4']), r['size'][0], r['size'][1], r['fps'], r['frames'], r['ffprobe']['codec_name'], r['ffprobe']['pix_fmt']))
        if r.get('audio_preview'): A('- `%s` (same video + slice of the master voice, preview only; master untouched)' % os.path.basename(r['audio_preview']))
        A('- `%s_start.png`, `%s_middle.png`, `%s_end.png`, `%s_frame_stats.json`' % (name, name, name, name))
        for k, (nt, i, fn) in r['cue_frames'].items(): A('- `%s` (cue "%s", narration_t %.2f s, frame %d)' % (fn, k, nt, i))
    for extra in info.get('extra_files', []): A('- `%s`' % extra)
    A('- `PROOF_REPORT.md` (this file)\n')
    A('Source: `animation/proofs/%s.py` + package `animation/uemotion/`.\n' % mod.__name__.split('.')[-1])
    A('## How to re-render\n\n```\ncd %s\n~/.venvs/uepipe/bin/python animation/render_proofs.py %s%s\n```\nDeterministic: every element is a pure function of time; any `--fps` / `--scale` works (`--scale 1.0` = 1080x1920 final into `%s_1080/`).\n' % (
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), pid, '' if args.scale == 0.5 else ' --scale %s' % args.scale, pid))
    A('## What was checked programmatically\n')
    A('| check | result | detail |\n|---|---|---|')
    for name, r in results.items():
        pj = r['ffprobe']
        ok = pj['codec_name'] == 'h264' and pj['pix_fmt'] == 'yuv420p' and int(pj['nb_read_frames']) == r['frames']
        A('| %s: container | %s | %s, %s, %sx%s, r_frame_rate %s, decoded frames %s of %d expected |' % (name, 'PASS' if ok else 'FAIL', pj['codec_name'], pj['pix_fmt'], pj['width'], pj['height'], pj['r_frame_rate'], pj['nb_read_frames'], r['frames']))
        A('| %s: frame-to-frame change | info | mean abs diff %.3f, max %.3f, min %.3f (0-255 luma, 1/4 res); frames with ~no change: %d of %d; max pixel luma %.0f; max step of mean luma %.2f |' % (
            name, r['diff_mean'], r['diff_max'], r['diff_min'], r['static_frames'], r['frames'], r['max_luma'], r['max_mean_luma_step']))
    for name, ok, detail in checks: A('| %s | %s | %s |' % (name, 'PASS' if ok else 'FAIL', str(detail).replace('|', '/')))
    A('\n## Start / middle / end frames\n')
    for name in results:
        A('%s\n' % name)
        for tag in ('start', 'middle', 'end'): A('![%s %s](%s_%s.png)' % (name, tag, name, tag))
        A('')
    A('## Defects I found by viewing frames\n')
    for d in notes.get('defects', ['(not yet reviewed)']): A('- %s' % d)
    A('\n## Corrections made\n')
    for d in notes.get('corrections', ['(none yet)']): A('- %s' % d)
    A('\n## Re-test result\n')
    for d in notes.get('retest', ['(not yet re-tested)']): A('- %s' % d)
    A('\n## Scientific verification\n\n%s\n' % info['science'])
    if info.get('open_issues') or notes.get('open_issues'):
        A('## Known defects still open\n')
        for d in info.get('open_issues', []) + notes.get('open_issues', []): A('- %s' % d)
        A('')
    A('---\nStatus words used: `candidate`. Nothing here is `approved`.')
    open(os.path.join(out, 'PROOF_REPORT.md'), 'w').write('\n'.join(L) + '\n')
    print('wrote', os.path.join(out, 'PROOF_REPORT.md'))
