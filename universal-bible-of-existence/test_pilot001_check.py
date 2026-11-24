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
        self.assertEqual(r["by_arm"]["A"]["review_records_assessed"],2)
        self.assertEqual(r["by_arm"]["A"]["reviewer_labeled_support_rate_pct"],50.0)

    def test_second_independent_reviewer_is_allowed(self):
        r=self.run_rows("S,observed,A,x,c1,supported,s1,reviewer1\nS,observed,A,x,c1,contradicted,s2,reviewer2\n")
        self.assertEqual(r["by_arm"]["A"]["reviewers"],2)
        self.assertEqual(r["by_arm"]["A"]["responses"],1)
        self.assertEqual(r["by_arm"]["A"]["review_records_assessed"],2)

    def test_duplicate_same_reviewer_not_allowed(self):
        row="S,observed,A,x,c1,unsupported,,r1\n"
        with self.assertRaisesRegex(ValueError,"duplicate"):
            self.run_rows(row+row)

    def test_one_response_two_arms_rejected(self):
        with self.assertRaisesRegex(ValueError,"conflicting arms"):
            self.run_rows("S,observed,A,x,c1,supported,s,r1\nS,observed,B,x,c2,supported,s,r1\n")

    def test_pooled_studies_rejected(self):
        with self.assertRaisesRegex(ValueError,"Multiple study IDs"):
            self.run_rows("S1,observed,A,x,c1,supported,s,r1\nS2,observed,B,y,c2,supported,s,r2\n")

    def test_missing_reviewer_rejected(self):
        with self.assertRaisesRegex(ValueError,"missing reviewer"):
            self.run_rows("S,observed,A,x,c1,supported,s,\n")

    def test_invalid_arm_rejected(self):
        with self.assertRaisesRegex(ValueError,"arm must"):
            self.run_rows("S,observed,C,x,c1,supported,s,r\n")

    def test_missing_study_id_rejected(self):
        with self.assertRaisesRegex(ValueError,"missing study"):
            self.run_rows(",observed,A,x,c1,supported,s,r\n")

if __name__=="__main__":
    unittest.main()
