# EchoCert Demo Script

A simple public demo script for video, screen recording or live walkthrough.

---

## Demo goal

Show that EchoCert can create an evidence receipt, verify it, detect tampering and produce a readable report.

Keep the demo simple. Do not use real client data or private material.

---

## 1. Opening line

"This is EchoCert — a local-first AI evidence receipt tool. It helps create a record of what an AI prompt and output looked like at the time, then checks later whether that record has changed."

---

## 2. Show the problem

"AI outputs are easy to copy, edit, lose or dispute. If a business uses AI in a report, decision or client workflow, it needs a better evidence trail than a screenshot."

---

## 3. Create demo files

Run:

```bash
python echocert.py init-demo
```

Explain:

"This creates a safe example prompt and output. No private data is used."

---

## 4. Create a receipt

Run:

```bash
python echocert.py record --from-files --prompt examples/prompt.txt --output examples/output.txt --receipt receipts/receipt.json --label Demo
```

Explain:

"EchoCert records the prompt, output, timestamp and metadata, then seals the receipt with a SHA-256 integrity hash."

---

## 5. Verify the receipt

Run:

```bash
python echocert.py verify receipts/receipt.json
```

Explain:

"The verification check confirms whether the receipt still matches the recorded data."

---

## 6. Show tamper detection

Change the demo output file or use the existing tamper demo if available.

Explain:

"Now the content has changed. EchoCert should detect that the record no longer matches. That is the point: not to prove the text is true, but to prove whether the record changed."

---

## 7. Generate the report

Run:

```bash
python echocert_report.py receipts/receipt.json --out reports/audit_report.html
```

Explain:

"The report gives a human-readable record that can be saved, reviewed or included in an evidence pack."

---

## 8. Closing line

"EchoCert is not a truth machine and it is not legal advice. It is an evidence layer for AI work: what was generated, when it was recorded and whether it changed later."

---

## Do not show publicly

- Real client records
- Legal evidence
- Personal data
- Private commercial workflows
- Secret keys, tokens or credentials
- Any private framework files
