# EchoCert Simple Usage

## Windows

Double-click `run_demo.bat`.

Then open `reports/audit_report.html`.

## Mac / Linux

Run:

```bash
bash run_demo.sh
```

Then open `reports/audit_report.html`.

## Manual flow

```bash
python echocert.py init-demo
python echocert.py record --from-files --prompt examples/prompt.txt --output examples/output.txt --receipt receipts/receipt.json --label Demo
python echocert.py verify receipts/receipt.json
python echocert_report.py receipts/receipt.json --out reports/audit_report.html
```

## What the report shows

- prompt
- AI output
- timestamp metadata
- SHA-256 integrity check
- verification status

## Limit

EchoCert checks evidence integrity. It does not prove the AI answer is true or replace professional advice.
