#!/usr/bin/env python3
"""Validate and summarise source-reviewed claim records for Covenant Pilot 001.

This is a transparent bookkeeping tool, not an automated truth checker,
independent peer review, or a test of changes in human wellbeing.

Usage:
    python pilot001_check.py PILOT_001_CLAIM_REVIEWS.csv
    python pilot001_check.py PILOT_001_CLAIM_REVIEWS_SYNTHETIC.csv
"""
import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
import sys

FIELDS = (
    "study_id", "record_type", "arm", "response_id", "claim_id",
    "verdict", "source_id", "reviewer_id"
)
ALLOWED_TYPES = {"observed", "synthetic"}
ALLOWED_VERDICTS = {"supported", "contradicted", "unsupported", "unassessed"}


def evaluate(path: Path) -> dict:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None:
            raise ValueError("Missing CSV header")
        if list(reader.fieldnames) != list(FIELDS):
            raise ValueError("CSV columns must match, in order: " + ",".join(FIELDS))
        rows = list(reader)

    if not rows:
        return {
            "status": "no_data",
            "records": 0,
            "claim": "No reviews recorded; no result or impact can be inferred."
        }

    seen = set()
    types = set()
    arm_count = defaultdict(Counter)
    responses = defaultdict(set)
    for lineno, raw in enumerate(rows, start=2):
        if None in raw or any(value is None for value in raw.values()):
            raise ValueError(f"Line {lineno}: unexpected extra or missing columns")
        row = {k: v.strip() for k, v in raw.items()}
        if not row["study_id"] or not row["response_id"] or not row["claim_id"]:
            raise ValueError(f"Line {lineno}: missing study, response or claim ID")
        if not row["reviewer_id"]:
            raise ValueError(f"Line {lineno}: missing reviewer ID")
        if row["record_type"] not in ALLOWED_TYPES:
            raise ValueError(f"Line {lineno}: record_type must be observed or synthetic")
        if row["arm"] not in {"A", "B"}:
            raise ValueError(f"Line {lineno}: arm must be A or B")
        if row["verdict"] not in ALLOWED_VERDICTS:
            raise ValueError(f"Line {lineno}: unknown verdict {row['verdict']!r}")
        if row["verdict"] in {"supported", "contradicted"} and not row["source_id"]:
            raise ValueError(f"Line {lineno}: supported or contradicted claim needs a source_id")
        key = (row["study_id"], row["response_id"], row["claim_id"])
        if key in seen:
            raise ValueError(f"Line {lineno}: duplicate study/response/claim review {key}")
        seen.add(key)
        types.add(row["record_type"])
        arm_count[row["arm"]][row["verdict"]] += 1
        responses[row["arm"]].add(row["response_id"])

    if len(types) > 1:
        raise ValueError("Synthetic and observed records may not be combined. Use separate files.")
    record_type = next(iter(types))
    summary = {}
    for arm in ("A", "B"):
        counts = arm_count[arm]
        assessed = sum(counts[v] for v in ("supported", "contradicted", "unsupported"))
        summary[arm] = {
            "responses": len(responses[arm]),
            "claims_assessed": assessed,
            "supported_as_labeled_by_reviewers": counts["supported"],
            "contradicted_as_labeled_by_reviewers": counts["contradicted"],
            "unsupported_as_labeled_by_reviewers": counts["unsupported"],
            "unassessed": counts["unassessed"],
            "reviewer_labeled_support_rate_pct": round(100 * counts["supported"] / assessed, 1) if assessed else None,
        }

    return {
        "status": "synthetic_example_not_evidence" if record_type == "synthetic" else "descriptive_claim_review_only",
        "record_type": record_type,
        "records": len(rows),
        "by_arm": summary,
        "interpretation": "The percentages are reviewer labels, not automatically verified truth.",
        "limitations": [
            "No independent verification of reviewer identity or source contents is performed.",
            "No human comprehension, wellbeing, autonomy or environmental outcome is measured.",
            "No causal or statistical significance claim is supported by these data alone.",
            "Never combine synthetic demonstrations with observed records."
        ],
        "impact_claim": "No demonstrated benefit from the Covenant or Pilot 001."
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="CSV of claim-level reviewer assessments")
    args = parser.parse_args()
    try:
        result = evaluate(args.input)
    except (OSError, ValueError, csv.Error) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
