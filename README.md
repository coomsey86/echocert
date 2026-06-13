# EchoCert

EchoCert is a local-first AI audit receipt tool.

It records:
- the prompt
- the AI output
- timestamp and metadata
- a SHA-256 integrity hash

The goal is simple:

**Create evidence that an AI interaction has not been altered after the fact.**

---

## What it does

- Creates deterministic JSON receipts
- Seals receipts with SHA-256 hashes
- Verifies whether files were modified later
- Produces diff reports between two receipts
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
python echocert.py record --from-files --prompt examples/prompt.txt --output examples/output.txt
```

Verify the receipt:

```bash
python echocert.py verify receipts/receipt.json
```

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

Version: 0.2

Public working prototype.

Built around practical AI audit receipts and integrity verification.
