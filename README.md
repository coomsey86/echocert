# EchoCert

EchoCert is a local-first AI audit receipt tool.

It records:
- the prompt
- the AI output
- timestamp and metadata
- a SHA-256 integrity hash
- a client-ready HTML audit report

The goal is simple:

**Create evidence that an AI interaction has not been altered after the fact.**

---

## What it does

- Creates deterministic JSON receipts
- Seals receipts with SHA-256 hashes
- Verifies whether files were modified later
- Produces diff reports between two receipts
- Generates HTML audit reports for clients
- Runs locally with Python

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

## Example Use Cases

### AI Evidence

Store prompts and outputs for future verification.

### Compliance

Keep evidence of AI-assisted workflows.

### Internal Audits

Compare outputs between versions.

### Research

Track prompt evolution over time.

---

## Commercial Services

Potential service offerings:

- AI Audit Reports
- Evidence Packs
- Prompt Review
- AI Workflow Reviews
- Business AI Documentation

Example offer:

**EchoCert Quick Audit** — customer sends one AI prompt/output, you return an integrity report and evidence notes.

---

## Important

EchoCert does NOT:

- Prove truth
- Prove authorship ownership by itself
- Inspect model internals
- Replace legal advice

It is an evidence and audit tool.

---

## Status

Version: 0.3

Public working prototype with receipt, verification, diff, and HTML report generation.
