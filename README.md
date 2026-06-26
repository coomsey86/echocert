# EchoCert

![Status](https://img.shields.io/badge/status-public%20prototype-blue)
![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-BSL%201.1-orange)
![Mode](https://img.shields.io/badge/mode-local--first-green)

**Local-first AI evidence receipts for audit, compliance and dispute preparation.**

EchoCert creates tamper-evident records for AI-assisted work. It records the prompt, output, timestamp, metadata and a SHA-256 integrity hash, then generates reports that can be checked later.

> **Problem:** AI outputs are easy to copy, edit, lose, misquote or dispute.
>
> **EchoCert answer:** create a simple evidence record showing what existed, when it existed and whether it was altered afterwards.

---

## What EchoCert is

EchoCert is a lightweight evidence layer for AI workflows.

It helps users create records around:

- AI prompts and outputs
- Business AI decisions
- Research notes
- Compliance reviews
- Internal audit trails
- Dispute preparation files
- Client-facing evidence packs

It is **not** a truth machine and it does not inspect private model internals. It is a practical integrity and audit tool for the records around AI use.

---

## Public demo boundary

This public repository is a working demonstration of the EchoCert evidence workflow.

It shows the public concept, basic receipt generation, verification, reporting and tamper-detection flow.

The public version does **not** include private commercial logic, client systems, confidential workflows, signing infrastructure, advanced key management, proprietary scoring methods or customer evidence.

For clarity:

- **Public repository:** demonstration, documentation and evaluation.
- **Private commercial build:** production tooling, protected workflows and licensed deployments.

See [`PRIVATE_PUBLIC_BOUNDARY.md`](PRIVATE_PUBLIC_BOUNDARY.md) for the public/private split.

---

## Core workflow

1. Capture a prompt and AI output.
2. Generate a deterministic receipt.
3. Seal the receipt with a SHA-256 integrity hash.
4. Verify later whether the record still matches.
5. Produce a human-readable report for review.

---

## What it does

- Creates deterministic JSON receipts
- Seals receipts with SHA-256 hashes
- Verifies whether files or receipts were modified later
- Produces diff reports between two receipts
- Generates client-ready HTML audit reports
- Runs locally with Python
- Supports evidence pack style workflows for audits, compliance reviews and dispute preparation

---

## Who it is for

EchoCert is aimed at people and teams who need clearer records of AI-assisted work:

- AI governance teams
- Compliance teams
- Legal support and dispute preparation
- Digital evidence and audit consultants
- Researchers using AI tools
- Businesses adopting AI internally
- Freelancers and agencies producing AI-assisted client work

---

## Quick Start

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

Generate a client-ready HTML report:

```bash
python echocert_report.py receipts/receipt.json --out reports/audit_report.html
```

Open `reports/audit_report.html` in a browser. Use **Print -> Save as PDF** to create a PDF report.

---

## Windows demo

Double-click:

```text
run_demo.bat
```

This creates:

- example prompt/output files
- a sealed receipt
- a verification check
- an HTML audit report

---

## Example use cases

### AI evidence

Store prompts and outputs for future verification.

### Compliance

Keep records of AI-assisted workflows for review, audit and governance.

### Internal audits

Compare outputs between versions, tools or workflow changes.

### Research

Track prompt evolution and output changes over time.

### Dispute preparation

Create clear records showing what was generated, when it was generated and whether later tampering is detectable.

---

## Commercial services

EchoCert can support services such as:

- AI Audit Reports
- Evidence Packs
- Prompt / Output Review
- AI Workflow Reviews
- Business AI Documentation
- Compliance-support documentation

Example offer:

**EchoCert Quick Audit** — customer sends one AI prompt/output pair, you return an integrity report and evidence notes.

Commercial or production use requires a separate commercial licence. See [`LICENSE`](LICENSE) and [`LICENSING.md`](LICENSING.md).

---

## Product documents

- [`PRODUCT.md`](PRODUCT.md) — product overview
- [`PITCH.md`](PITCH.md) — short commercial pitch
- [`PILOT.md`](PILOT.md) — pilot offer structure
- [`ROADMAP.md`](ROADMAP.md) — public roadmap
- [`LICENSING.md`](LICENSING.md) — licensing overview
- [`SECURITY.md`](SECURITY.md) — security and public repository safety
- [`PRIVATE_PUBLIC_BOUNDARY.md`](PRIVATE_PUBLIC_BOUNDARY.md) — what stays public vs private

---

## Important limits

EchoCert does **not**:

- Prove that an AI output is true
- Prove legal authorship ownership by itself
- Inspect private model internals
- Replace legal advice
- Replace professional compliance review

It is an evidence and audit tool. It helps prove integrity, continuity and tamper detection around AI records.

---

## Status

Version: Public working prototype.

This repo demonstrates receipt creation, verification, diffing and HTML report generation while keeping private commercial material out of the public release.
