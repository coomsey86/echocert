# EchoCert

![Status](https://img.shields.io/badge/status-active%20pilot%20development-blue)
![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-BSL%201.1-orange)
![Mode](https://img.shields.io/badge/mode-local--first-green)

**Local-first digital evidence integrity for files, photos, video and AI records.**

EchoCert creates tamper-evident integrity records using SHA-256, structured receipts and human-readable reports. It is designed to help people preserve an original digital file, record what was checked, and later verify whether the file still matches the recorded hash.

> **Problem:** important digital evidence is easy to copy, rename, edit, compress, re-export, lose or dispute.
>
> **EchoCert answer:** preserve the original where possible, create an integrity receipt, and make later verification simple and explicit.

---

## Current product direction — July 2026

EchoCert is being developed as one local-first evidence ecosystem with two interfaces:

### EchoCert Elite — Windows desktop

The private controlled-pilot build, **EchoCert Elite v0.9.4**, has demonstrated:

- SHA-256 hashing of files
- Structured JSON receipts
- PDF and TXT reports
- Evidence Pack ZIP creation
- Receipt/file verification
- Case and project metadata
- Local document storage
- UTC/local timestamp recording with timezone information
- Explicit clock-source / timestamp-status disclosure
- Windows installation and clean-machine testing

Desktop is intended to remain the professional command centre for certification, reporting, evidence packs, case workflows, audit work and later team/business features.

### EchoCert Mobile — Android companion

A private Android development build has been physically tested on a Samsung device for:

- Photo capture
- Video capture
- Preservation of the captured original in the app evidence folders
- Automatic SHA-256 integrity receipt creation
- One-tap re-hash verification
- Clear integrity-confirmed results when the later file matches

The mobile app is a development companion, not a public production release.

**Core principle:**

> **One platform. Two interfaces. One evidence format.**

---

## What the public repository contains

This repository is the **public demonstration and documentation layer** of EchoCert.

It demonstrates the earlier AI prompt/output receipt workflow and the core integrity concepts that continue into the wider product:

1. Capture or select a record/file.
2. Generate a deterministic receipt.
3. Seal relevant data with SHA-256.
4. Verify later whether the stored data still matches.
5. Produce a human-readable report for review.

The public repository does **not** contain the full EchoCert Elite controlled-pilot build, the Android commercial/development build, customer evidence, private keys, signing infrastructure or protected production workflows.

See [`PRIVATE_PUBLIC_BOUNDARY.md`](PRIVATE_PUBLIC_BOUNDARY.md).

---

## What EchoCert can help establish

EchoCert is designed to help answer practical integrity questions such as:

- What file or record was checked?
- What SHA-256 digest was recorded for it?
- What metadata and timestamp were recorded at that moment?
- Does the later file still produce the same digest?
- Has a stored receipt or record changed since it was sealed?

A matching SHA-256 digest is strong evidence that the checked bytes are unchanged from the bytes represented by the recorded digest.

---

## What EchoCert does **not** prove by itself

EchoCert is deliberately conservative about its claims.

It does **not** by itself prove:

- that a photograph or video depicts a true real-world event
- who created a file
- legal ownership or authorship
- that a local system clock was independently trustworthy
- an independently trusted creation time unless an external timestamp authority is used
- a complete chain of custody without the surrounding process and evidence
- court admissibility, regulatory approval or forensic accreditation
- that an AI output is true

Where the timestamp comes only from the local device clock, that limitation should be stated clearly rather than hidden.

---

## Current and intended use cases

EchoCert is aimed at people and teams who need clearer digital evidence records, including:

- Legal support and dispute preparation
- Compliance and internal audit
- Inspection and field documentation
- Property and condition records
- Insurance-support documentation
- Construction and trades
- Investigators and consultants
- Researchers
- AI governance and AI-assisted workflow records
- Small organisations that need local-first evidence handling

AI prompt/output auditing remains a supported use case and part of the project's technical history, but it is **not the whole product**.

---

## Public demo features

The code in this repository currently demonstrates:

- Deterministic JSON receipt creation
- SHA-256 integrity hashing
- Receipt verification
- Diff reports between records
- Human-readable HTML audit reports
- Local Python operation
- Evidence-pack style workflow concepts

### Quick start

Clone:

```bash
git clone https://github.com/coomsey86/echocert.git
cd echocert
```

Create demo files:

```bash
python echocert.py init-demo
```

Create a receipt:

```bash
python echocert.py record --from-files --prompt examples/prompt.txt --output examples/output.txt --receipt receipts/receipt.json --label Demo
```

Verify the receipt:

```bash
python echocert.py verify receipts/receipt.json
```

Generate a human-readable HTML report:

```bash
python echocert_report.py receipts/receipt.json --out reports/audit_report.html
```

On Windows, `run_demo.bat` runs the public demo workflow.

---

## Product development priorities

The current focus is not feature-count for its own sake. The priority is:

1. **Simplify the user experience**
2. **Preserve originals safely**
3. **Harden integrity and verification workflows**
4. **Test failure cases and edge cases**
5. **Validate the product with real pilot users**
6. **Improve desktop/mobile interoperability**
7. **Add stronger timestamp/provenance options where justified**
8. **Remain standards-first and avoid unnecessary proprietary lock-in**

Future interoperability may include trusted timestamp services and standards such as C2PA / Content Credentials where they genuinely strengthen the evidence model.

---

## Licensing

This public repository is **source-available under the Business Source License 1.1 (BSL 1.1)**. It should not be described simply as unrestricted open source.

Commercial or production use requires a separate commercial licence under the current licence terms. See [`LICENSE`](LICENSE) and [`LICENSING.md`](LICENSING.md).

---

## Product documents

- [`PRODUCT.md`](PRODUCT.md) — current product definition
- [`PITCH.md`](PITCH.md) — commercial positioning
- [`PILOT.md`](PILOT.md) — pilot direction
- [`ROADMAP.md`](ROADMAP.md) — public roadmap
- [`FAQ.md`](FAQ.md) — common questions and limits
- [`LICENSING.md`](LICENSING.md) — licensing overview
- [`SECURITY.md`](SECURITY.md) — repository security guidance
- [`PRIVATE_PUBLIC_BOUNDARY.md`](PRIVATE_PUBLIC_BOUNDARY.md) — public/private split

---

## Status

**Public repository:** working demonstration of EchoCert's receipt, verification, diff and reporting foundations.

**Private product development:** EchoCert Elite v0.9.4 is controlled-pilot ready; the Android companion has passed physical-device photo/video capture, receipt and re-verification tests.

The next proof point is real-world pilot validation, security hardening and UX refinement — not simply adding more features.
