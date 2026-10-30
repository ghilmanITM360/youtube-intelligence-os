"""Rebuilds must preserve published CSV bytes and reject malformed audit packets."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import build_audit_966 as builder


class BuilderPreservation(unittest.TestCase):
    def test_only_changed_csv_record_is_replaced(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            original = b'Video_ID,analysis\r\na,"unchanged"\r\nb,"old\nvalue"\r\n'
            path = base / 'projection.csv'
            path.write_bytes(original)
            rows = [{'Video_ID': 'a', 'analysis': 'unchanged', 'new_jsonl_field': 'kept in ledger'},
                    {'Video_ID': 'b', 'analysis': 'updated'}]
            with patch.object(builder, 'BASE', base):
                builder.csv_out(path.name, rows)
                self.assertEqual(b'Video_ID,analysis\r\na,"unchanged"\r\nb,updated\n', path.read_bytes())
                before = path.read_bytes()
                builder.csv_out(path.name, rows)
                self.assertEqual(before, path.read_bytes())

    def test_csv_identity_drift_fails_before_write(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            path = base / 'projection.csv'
            original = b'Video_ID,analysis\na,original\n'
            path.write_bytes(original)
            with patch.object(builder, 'BASE', base), self.assertRaises(AssertionError):
                builder.csv_out(path.name, [{'Video_ID': 'b', 'analysis': 'replacement'}])
            self.assertEqual(original, path.read_bytes())

    def test_validation_companions_and_legitimate_packets(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            (base / 'a_VALIDATION.json').write_text('{"status":"PASS"}')
            (base / 'b_VALIDATION.json').write_text('{"batch_id":"real","reviews":[{"Video_ID":"a"}]}')
            self.assertEqual({'a': ('real', {'Video_ID': 'a'})}, builder.load_batches(base))
            (base / 'malformed.json').write_text('{"batch_id":"must-not-disappear"}')
            with self.assertRaises(KeyError):
                builder.load_batches(base)
            (base / 'malformed.json').unlink()
            (base / 'malformed_VALIDATION.json').write_text('{"batch_id":"also-must-not-disappear"}')
            with self.assertRaises(KeyError):
                builder.load_batches(base)

    def test_duplicate_audit_id_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            packet = '{"batch_id":"real","reviews":[{"Video_ID":"a"}]}'
            for name in ('a.json', 'b.json'):
                (base / name).write_text(packet)
            with self.assertRaises(AssertionError):
                builder.load_batches(base)
