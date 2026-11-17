"""Guard against population drift and automated features masquerading as reviews."""
import unittest
import importlib.util
from pathlib import Path

class AuditContract(unittest.TestCase):
    def test_validator_exists(self):
        self.assertTrue(Path(__file__).with_name('validate_audit_966.py').exists())

    def test_rejects_duplicate_and_substituted_ids(self):
        from validate_audit_966 import identity_errors
        self.assertTrue(identity_errors(['a','b'], ['a','a']))
        self.assertTrue(identity_errors(['a','b'], ['a','c']))
        self.assertFalse(identity_errors(['a','b'], ['b','a']))

    def test_rejects_false_full_script_completion(self):
        from validate_audit_966 import semantic_errors
        row={'Video_ID':'a','statuses':{'SCRIPT_REVIEW':'COMPLETE_EVIDENCE_BACKED'},'script':{'review_scope':'AUTOMATED_ONLY'}}
        self.assertTrue(semantic_errors(row))

    def test_missing_script_is_not_complete(self):
        from build_audit_966 import initial_statuses
        result=initial_statuses(False)
        self.assertEqual(result['SCRIPT_REVIEW'],'BLOCKED_MISSING_SOURCE')
        self.assertEqual(result['VIRALITY_REVIEW'],'NOT_STARTED')

if __name__=='__main__': unittest.main()

class ProvenanceContract(unittest.TestCase):
    def test_image_from_other_video_rejected(self):
        from validate_audit_966 import image_errors
        self.assertTrue(image_errors('aaa', {'image_path':'bbb.jpg','image_source':'https://i.ytimg.com/vi/bbb/maxresdefault.jpg'}))

    def test_missing_claim_source_rejected(self):
        from validate_audit_966 import reference_errors
        self.assertTrue(reference_errors(['DOES_NOT_EXIST.csv:aaa']))

    def test_unknown_batch_video_rejected(self):
        from build_audit_966 import batch_identity_errors
        self.assertTrue(batch_identity_errors({'a'}, {'b'}))

    def test_complete_requires_each_rubric(self):
        from validate_audit_966 import semantic_errors
        r={'Video_ID':'a','statuses':{'VIRALITY_REVIEW':'COMPLETE_LIMITED_EVIDENCE'},'virality':{'review_scope':'INDIVIDUAL_PUBLIC_EVIDENCE','source_refs':['VIDEO_MASTER.csv:a'],'analysis':'One sentence'}}
        self.assertTrue(semantic_errors(r))

class ScopeContract(unittest.TestCase):
    def test_title_scope_cannot_complete_script(self):
        from validate_audit_966 import semantic_errors
        r={'Video_ID':'a','statuses':{'SCRIPT_REVIEW':'COMPLETE_LIMITED_EVIDENCE'},'script':{'review_scope':'ACTUAL_TITLE','analysis':'x','source_refs':['x'],'beat_map':['x'],'claim_audit':'x','opening_words':'x','ending_words':'x','timing':'OPENING_WORDS_ONLY','source':{'Text_SHA256':'x'}}}
        self.assertTrue(any('scope' in e for e in semantic_errors(r)))

class ProjectionContract(unittest.TestCase):
    def test_csv_cannot_claim_more_completion_than_jsonl(self):
        from validate_audit_966 import projection_errors
        source=[{'Video_ID':'a','statuses':{'TITLE_REVIEW':'NOT_STARTED'}}]
        display=[{'Video_ID':'a','TITLE_REVIEW':'COMPLETE_LIMITED_EVIDENCE'}]
        self.assertTrue(projection_errors(source,display))
