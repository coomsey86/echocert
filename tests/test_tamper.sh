#!/usr/bin/env bash
set -euo pipefail

echo "== EchoCert tamper test =="

TMPDIR="$(mktemp -d)"
trap 'rm -rf "$TMPDIR"' EXIT

# record
python echocert.py record \
  --prompt simulator/inputs/prompt.json \
  --output simulator/outputs/out_A.json \
  --receipt "$TMPDIR/receipt.json"

# tamper with receipt
echo " " >> "$TMPDIR/receipt.json"

# verify should fail
if python echocert.py verify "$TMPDIR/receipt.json"; then
  echo "ERROR: tampered file verified successfully"
  exit 1
else
  echo "Tamper correctly detected"
fi

echo "TAMPER TEST PASSED"
