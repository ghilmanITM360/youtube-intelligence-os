import unittest, importlib.util
from pathlib import Path
P=Path(__file__).parent
class PublicationGateTests(unittest.TestCase):
 def setUp(self):
  self.assertTrue((P/'publication_preflight.py').exists(), 'Publication lacks a mandatory candidate-tree media gate')
  spec=importlib.util.spec_from_file_location('guard',P/'publication_preflight.py');self.m=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.m)
 def test_real_W2_W3_JPGs_rejected(self):
  import subprocess,json
  evidence=json.loads((P/'MEDIA_DEFECT.json').read_text())
  for x in evidence['unexpected_media'][:2]:
   data=subprocess.check_output(['git','-C',self.m.REPO,'show',x['introducing_commit']+':'+x['path']])
   self.assertTrue(self.m.violations({x['path']:data},{}))
 def test_renamed_JPEG_rejected(self):
  self.assertTrue(self.m.violations({'report.json':b'\xff\xd8\xff\xe0binary'},{}))
 def test_uppercase_and_unknown_extension_rejected(self):
  for path in ['strip.JPG','native.png','movie.mp4','payload.bin','private.index']:
   self.assertTrue(self.m.violations({path:b'not allowed'},{}))
 def test_NUL_binary_rejected(self):
  self.assertTrue(self.m.violations({'notes.md':b'abc\x00def'},{}))
 def test_nonUTF8_rejected(self):
  self.assertTrue(self.m.violations({'notes.txt':b'\x80'},{}))
 def test_symlink_and_out_of_scope_rejected(self):
  self.assertTrue(self.m.violations({'../outside.md':b'text'},{}))
 def test_exact_inherited_defect_reported_but_unchanged_allowed(self):
  import hashlib
  data=b'\xff\xd8\xffexisting';known={'old.jpg':hashlib.sha256(data).hexdigest()}
  self.assertEqual(self.m.violations({'old.jpg':data},known),[])
  self.assertTrue(self.m.violations({'old.jpg':data+b'changed'},known))
 def test_existing_versioned_text_seals_and_shell_allowed(self):
  self.assertEqual(self.m.violations({'EVIDENCE_SHA256SUMS_checkpoint_W4':b'abc  file.json\n','SHA256SUMS_roster_v1':b'abc  roster.csv\n','vf_lock.sh':b'#!/bin/sh\necho status\n'},{}),[])
 def test_valid_text_and_deletion_allowed(self):
  self.assertEqual(self.m.violations({'report.md':b'observed source','result.json':b'{"listening":0}','EVIDENCE_SHA256SUMS':b'abc  report.md\n'},{}),[])
  self.assertEqual(self.m.violations({}, {'removed.jpg':'oldhash'}),[])
if __name__=='__main__':unittest.main(verbosity=2)
