"""Run with: python -m unittest -v test_pilot001_check.py"""
import tempfile
import unittest
from pathlib import Path
from pilot001_check import evaluate

HEADER = "study_id,record_type,arm,response_id,claim_id,verdict,source_id,reviewer_id\n"

class ValidatePilot001(unittest.TestCase):
    def run_rows(self, text):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "reviews.csv"
            p.write_text(HEADER + text, encoding="utf-8")
            return evaluate(p)

    def test_empty_has_no_claim(self):
        r=self.run_rows("")
        self.assertEqual(r["status"], "no_data")
        self.assertEqual(r["records"], 0)

    def test_synthetic_is_watermarked(self):
        r=self.run_rows("DEMO,synthetic,A,a1,c1,supported,source,reviewer\n")
        self.assertEqual(r["status"], "synthetic_example_not_evidence")
        self.assertEqual(r["by_arm"]["A"]["reviewer_labeled_support_rate_pct"], 100.0)
        self.assertEqual(r["by_arm"]["B"]["reviewer_labeled_support_rate_pct"], None)
        self.assertIn("No demonstrated benefit",r["impact_claim"])

    def test_duplicate_rejected(self):
        row="S,observed,A,resp,c1,supported,source,reviewer\n"
        with self.assertRaisesRegex(ValueError,"duplicate"):
            self.run_rows(row + row)

    def test_mixed_data_rejected(self):
        with self.assertRaisesRegex(ValueError,"may not be combined"):
            self.run_rows("S,synthetic,A,x,c1,unassessed,,r\nS,observed,B,y,c2,unassessed,,r\n")

    def test_unsupported_source_rejected(self):
        with self.assertRaisesRegex(ValueError,"needs a source_id"):
            self.run_rows("S,observed,A,x,c1,supported,,r\n")

    def test_unknown_verdict_rejected(self):
        with self.assertRaisesRegex(ValueError,"unknown verdict"):
            self.run_rows("S,observed,A,x,c1,magical,source,r\n")

    def test_computes_assessed_denominator_correctly(self):
        r=self.run_rows("S,observed,A,x,c1,supported,s1,r\nS,observed,A,x,c2,unsupported,,r\nS,observed,A,x,c3,unassessed,,r\n")
        self.assertEqual(r["by_arm"]["A"]["claims_assessed"],2)
        self.assertEqual(r["by_arm"]["A"]["reviewer_labeled_support_rate_pct"],50.0)

if __name__=="__main__":
    unittest.main()
