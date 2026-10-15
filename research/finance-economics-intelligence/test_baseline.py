"""Comparison invariants protect against misleading performance labels."""
import unittest
from build_baseline import compare, date, format_of


class ComparisonTests(unittest.TestCase):
    def row(self, ident, views=100, age=30, fmt='LONG_FORM'):
        return dict(Video_ID=ident, Channel_ID='channel', Format=fmt, Views=views,
                    Age_days=age, Metric_snapshot_date='2026-09-12')

    def test_unknowns_are_not_ranked(self):
        for field, value in [('Age_days',''), ('Age_days',6), ('Format','UNKNOWN'), ('Views',None)]:
            row=self.row('target'); row[field]=value
            self.assertEqual(compare(row, [self.row(str(i)) for i in range(10)])[0], 'INSUFFICIENT_DATA')

    def test_format_and_channel_do_not_mix(self):
        peers=[self.row(str(i),fmt='SHORTS') for i in range(10)]
        self.assertEqual(compare(self.row('target'),peers)[0],'INSUFFICIENT_DATA')
        peers=[dict(self.row(str(i)),Channel_ID='other') for i in range(10)]
        self.assertEqual(compare(self.row('target'),peers)[0],'INSUFFICIENT_DATA')

    def test_thresholds_and_ties(self):
        peers=[self.row(str(i)) for i in range(5)]
        for views,tier in [(200,'STRONG'),(50,'TYPICAL'),(49,'WEAK'),(100,'TYPICAL')]:
            self.assertEqual(compare(self.row('target',views),peers)[0],tier)

    def test_sparse_and_zero_baseline(self):
        self.assertEqual(compare(self.row('target'),[self.row(str(i)) for i in range(4)])[0],'INSUFFICIENT_DATA')
        self.assertEqual(compare(self.row('target'),[self.row(str(i),0) for i in range(5)])[0],'INSUFFICIENT_DATA')

    def test_source_parsing(self):
        self.assertIsNone(date('(date only)'))
        self.assertEqual(format_of(None),'UNKNOWN')
        self.assertEqual(format_of('Short'),'SHORTS')
        self.assertEqual(format_of('video'),'LONG_FORM')


if __name__=='__main__': unittest.main()
