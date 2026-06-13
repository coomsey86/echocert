#!/usr/bin/env bash
set -euo pipefail

echo "== EchoCert tamper test =="

TMPDIR="$(mktemp -d)"
trap 'rm -rf "$TMPDIR"' EXIT

mkdir -p "$TMPDIR/examples"
echo "Explain EchoCert in one sentence." > "$TMPDIR/examples/prompt.txt"
echo "EchoCert creates tamper-evident AI audit receipts." > "$TMPDIR/examples/output.txt"

python echocert.py record \
  --from-files \
  --prompt "$TMPDIR/examples/prompt.txt" \
  --output "$TMPDIR/examples/output.txt" \
  --receipt "$TMPDIR/receipt.json" \
  --label TamperTest

echo " " >> "$TMPDIR/receipt.json"

if python echocert.py verify "$TMPDIR/receipt.json"; then
  echo "ERROR: tampered file verified successfully"
  exit 1
else
  echo "Tamper correctly detected"
fi

echo "TAMPER TEST PASSED"
