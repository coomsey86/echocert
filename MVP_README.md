# EchoCert Public-Safe MVP

**Creator:** Paul McCombs / Coomsy  
**Project:** EchoCert / Echo Framework

EchoCert is a public-safe demonstration of tamper-evident AI evidence receipts.

It records an AI prompt and AI output, creates a deterministic JSON receipt, seals it with a SHA-256 hash, verifies whether the receipt has changed, and generates a simple audit report.

## What this proves

EchoCert proves **integrity**.

It can show whether a recorded AI prompt/output receipt has remained unchanged since it was signed.

## What this does not prove

EchoCert does not prove that the AI output is true, safe, lawful, or accurate. It does not replace legal, compliance, or security advice.

## Files

- `echocert_mvp.py` - compact public-safe MVP
- `run_mvp_demo.bat` - Windows demo runner
- `run_mvp_demo.sh` - Mac/Linux demo runner

## Quick demo

```bash
python echocert_mvp.py tamper-demo
python echocert_mvp.py verify receipts/original.json
python echocert_mvp.py report receipts/original.json --out reports/audit_report.html
```

Then open:

```text
reports/audit_report.html
```

## Manual receipt

```bash
python echocert_mvp.py record --prompt "Explain a refund policy simply." --output "Customers can request a refund within 30 days." --model demo-model --label demo --out receipts/demo.json
python echocert_mvp.py verify receipts/demo.json
python echocert_mvp.py report receipts/demo.json --out reports/demo_report.html
```

## Tamper test

Run:

```bash
python echocert_mvp.py tamper-demo
```

This creates:

- `receipts/original.json` - valid receipt
- `receipts/tampered.json` - altered receipt

The original should verify. The tampered version should fail because the AI output was changed from `30 days` to `60 days` while keeping the old hash.

## Public-safe boundary

This MVP intentionally exposes only the safe demonstration layer:

- canonical JSON
- SHA-256 hashing
- verification
- report output

It does not expose any private memory systems, advanced ingestion pipeline, commercial logic, signing keys, private token systems, or proprietary Echo Framework internals.
