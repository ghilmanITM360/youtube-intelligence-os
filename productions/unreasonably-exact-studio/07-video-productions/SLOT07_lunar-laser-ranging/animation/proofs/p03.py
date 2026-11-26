"""P03 Observatory-to-Moon transition = the SELECTED opening (treatment A, ground-level cinematic), narration 0 - 9.7 s.
Selection record: renders/proofs/OPEN/OPENING_SELECTION.md. All timing, art and checks live in proofs/opening.py."""
from uemotion import space as S
from uemotion.video import ClipSpec
from . import opening as O

INFO = dict(O.INFO, title='P03 Observatory-to-Moon transition (selected opening A)')
def check_all(out_dir, results):
    return [c for c in O.check_all(out_dir, results) if not c[0].startswith(('B:', 'C:'))]
def specs():
    s = O.specs()[0]; S.preload_real()
    return [ClipSpec('P03', 'P03_opening_A_observatory_to_moon', s.n0, s.duration, s.scene, captions=True, blur=(3, 0.5), cues=s.cues)]
