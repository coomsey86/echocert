#!/usr/bin/env bash
set -e

echo "Running EchoCert demo..."
python3 echocert.py init-demo
python3 echocert.py record --from-files --prompt examples/prompt.txt --output examples/output.txt --receipt receipts/receipt.json --label Demo
python3 echocert.py verify receipts/receipt.json
python3 echocert_report.py receipts/receipt.json --out reports/audit_report.html

echo "Demo complete. Open reports/audit_report.html in your browser."
