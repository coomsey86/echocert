#!/usr/bin/env bash
set -euo pipefail

echo "== EchoCert smoke test =="

# temp workspace
TMPDIR="$(mktemp -d)"
trap 'rm -rf "$TMPDIR"' EXIT

# record
python echocert.py record \
  --prompt simulator/inputs/prompt.json \
  --output simulator/outputs/out_A.json \
  --receipt "$TMPDIR/receipt.json"

# diff
python echocert.py diff \
  "$TMPDIR/receipt.json" \
  simulator/receipts/receipt_B.json \
  --out "$TMPDIR/delta.json"

# verify
python echocert.py verify "$TMPDIR/receipt.json"
python echocert.py verify "$TMPDIR/delta.json"

echo "SMOKE TEST PASSED"
