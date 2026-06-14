#!/usr/bin/env bash
set -e

echo "Running EchoCert public MVP demo..."
python3 echocert_mvp.py tamper-demo
python3 echocert_mvp.py verify receipts/original.json
python3 echocert_mvp.py report receipts/original.json --out reports/audit_report.html

echo
echo "Demo complete. Open reports/audit_report.html in your browser."
