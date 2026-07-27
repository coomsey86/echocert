# EchoCert Public-Safe MVP Demo

This file documents the compact public demonstration that helped establish EchoCert's receipt and verification foundations.

It is **not the complete current EchoCert product**.

For the current product overview, start with [`README.md`](README.md).

---

## What this public MVP demonstrates

The MVP uses a safe AI prompt/output example because it can be reproduced publicly without exposing customer, legal, photo or video evidence.

It demonstrates:

- deterministic JSON receipt creation
- SHA-256 integrity hashing
- receipt verification
- tamper detection
- simple human-readable report generation

These concepts remain part of the wider EchoCert evidence-integrity product.

---

## Current wider product direction

EchoCert now comprises:

- **EchoCert Elite** — private Windows desktop professional evidence workflow
- **EchoCert Mobile** — private Android field-capture companion

The current product direction covers files, photos, video and AI-assisted records rather than only AI prompt/output auditing.

---

## What the demo can establish

The demo can show whether the recorded data still matches the integrity values represented by its receipt.

It demonstrates **integrity checking**.

---

## What it does not establish

It does not prove:

- that the content is true
- who created the content
- legal ownership/authorship
- independently trusted time when only a local clock is used
- a complete chain of custody
- court admissibility or forensic accreditation
- that an AI answer is safe, lawful or accurate

---

## Files

- `echocert_mvp.py` — compact public-safe demonstration
- `run_mvp_demo.bat` — Windows demo runner
- `run_mvp_demo.sh` — Mac/Linux demo runner

---

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

---

## Manual receipt

```bash
python echocert_mvp.py record --prompt "Explain a refund policy simply." --output "Customers can request a refund within 30 days." --model demo-model --label demo --out receipts/demo.json
python echocert_mvp.py verify receipts/demo.json
python echocert_mvp.py report receipts/demo.json --out reports/demo_report.html
```

---

## Tamper test

```bash
python echocert_mvp.py tamper-demo
```

This creates a valid example and an intentionally altered example so verification behaviour can be demonstrated safely.

---

## Public-safe boundary

This MVP intentionally exposes only demonstration material. It does not expose private EchoCert Elite/Mobile builds, client evidence, deployment credentials, signing infrastructure, private commercial source or protected production workflows.

See [`PRIVATE_PUBLIC_BOUNDARY.md`](PRIVATE_PUBLIC_BOUNDARY.md).
