# EchoCert Public Demo Usage

This page explains how to run the **public repository demo**.

It does not document the complete private EchoCert Elite or EchoCert Mobile products. See [`README.md`](README.md) for the current product overview.

---

## Windows

Double-click:

```text
run_demo.bat
```

Then open:

```text
reports/audit_report.html
```

---

## Mac / Linux

Run:

```bash
bash run_demo.sh
```

Then open:

```text
reports/audit_report.html
```

---

## Manual public-demo flow

```bash
python echocert.py init-demo
python echocert.py record --from-files --prompt examples/prompt.txt --output examples/output.txt --receipt receipts/receipt.json --label Demo
python echocert.py verify receipts/receipt.json
python echocert_report.py receipts/receipt.json --out reports/audit_report.html
```

The public demo currently uses synthetic AI prompt/output files because they are safe and easy to reproduce publicly.

The same core concepts — structured receipts, SHA-256 integrity and later verification — form part of the broader EchoCert file/photo/video evidence direction.

---

## What the public report shows

Depending on the demo version, the report may include:

- recorded prompt/example input
- recorded output
- timestamp metadata
- SHA-256 integrity information
- verification status

---

## Important limit

EchoCert checks digital integrity. It does not by itself prove that content is true, establish legal ownership/authorship, provide an independently trusted timestamp when only local device time is used, or guarantee admissibility/accreditation.
