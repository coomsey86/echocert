# EchoCert Public Demo Script

A simple public demo script for video, screen recording or live walkthrough.

---

## Demo goal

Show that EchoCert can create an integrity receipt, verify it, detect a changed record and produce a readable report — while explaining that the public repository is only the demonstration layer of the wider desktop/mobile product.

Keep the demo simple. Do not use real client data, legal evidence, credentials or private material.

---

## 1. Opening line

> “This is EchoCert — a local-first digital evidence integrity system. The public demo uses a safe AI prompt/output example to show the same basic receipt, SHA-256 verification and tamper-detection ideas that underpin the wider desktop and mobile product.”

---

## 2. Explain the problem

> “Important digital files can be copied, edited, renamed or disputed. EchoCert is designed to make it simple to create an integrity record and check later whether the digital record still matches.”

---

## 3. Explain why the demo uses AI text

> “This public demo deliberately uses synthetic prompt/output text so we can demonstrate the mechanism without publishing real customer, legal, photo or video evidence.”

Run:

```bash
python echocert.py init-demo
```

---

## 4. Create a receipt

Run:

```bash
python echocert.py record --from-files --prompt examples/prompt.txt --output examples/output.txt --receipt receipts/receipt.json --label Demo
```

Explain:

> “EchoCert records the demo data and metadata, then creates SHA-256 integrity information in a deterministic receipt.”

---

## 5. Verify the receipt

Run:

```bash
python echocert.py verify receipts/receipt.json
```

Explain:

> “Verification checks whether the record still matches the integrity values stored in the receipt.”

---

## 6. Show tamper detection

Change the safe demo output file or use the existing tamper demonstration.

Explain:

> “The content has changed, so the integrity check no longer matches. EchoCert is not deciding whether the text is true — it is detecting that the checked record is different.”

---

## 7. Generate the report

Run:

```bash
python echocert_report.py receipts/receipt.json --out reports/audit_report.html
```

Explain:

> “The report turns the technical integrity record into something a person can review or include in a wider evidence workflow.”

---

## 8. Connect the demo to the current product

> “The private EchoCert product now goes beyond this AI text demo. EchoCert Elite is the Windows professional workflow for files, receipts, verification, reports and evidence packs. EchoCert Mobile is the Android field companion, where photo and video capture, SHA-256 receipt creation and re-verification have been demonstrated on a physical device.”

---

## 9. State the limits clearly

> “A hash does not prove that a photo is true, who created a file, or that a local clock was independently trusted. EchoCert is an integrity tool: it helps establish whether the checked digital bytes still match the earlier recorded digest.”

---

## Closing line

> “Capture or select. Preserve. Hash. Receipt. Verify. Report. That is the EchoCert workflow.”

---

## Do not show publicly

- Real client or pilot evidence
- Private legal evidence
- Personal/sensitive data
- Private commercial source or workflows
- Passwords, keys, tokens, certificates or signing credentials
- Private deployment details
