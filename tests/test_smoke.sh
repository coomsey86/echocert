#!/usr/bin/env bash
set -euo pipefail

echo "== EchoCert smoke test =="

TMPDIR="$(mktemp -d)"
trap 'rm -rf "$TMPDIR"' EXIT

mkdir -p "$TMPDIR/examples"
echo "Explain EchoCert in one sentence." > "$TMPDIR/examples/prompt.txt"
echo "EchoCert creates tamper-evident AI audit receipts." > "$TMPDIR/examples/output_a.txt"
echo "EchoCert creates tamper-evident AI audit receipts with SHA-256 seals." > "$TMPDIR/examples/output_b.txt"

python echocert.py record \
  --from-files \
  --prompt "$TMPDIR/examples/prompt.txt" \
  --output "$TMPDIR/examples/output_a.txt" \
  --receipt "$TMPDIR/receipt_a.json" \
  --label SmokeA

python echocert.py record \
  --from-files \
  --prompt "$TMPDIR/examples/prompt.txt" \
  --output "$TMPDIR/examples/output_b.txt" \
  --receipt "$TMPDIR/receipt_b.json" \
  --label SmokeB

python echocert.py diff \
  "$TMPDIR/receipt_a.json" \
  "$TMPDIR/receipt_b.json" \
  --out "$TMPDIR/delta.json"

python echocert.py verify "$TMPDIR/receipt_a.json"
python echocert.py verify "$TMPDIR/receipt_b.json"
python echocert.py verify "$TMPDIR/delta.json"
python echocert_report.py "$TMPDIR/receipt_a.json" --out "$TMPDIR/audit_report.html"

test -s "$TMPDIR/audit_report.html"

echo "SMOKE TEST PASSED"
