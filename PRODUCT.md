# EchoCert — Product Definition

## Product summary

EchoCert is a **local-first digital evidence integrity system** for files, photos, video and recorded AI-assisted work.

It uses SHA-256 integrity hashing, structured receipts and human-readable reports to help users preserve an original record and later verify whether the checked digital file still matches the recorded digest.

EchoCert is being developed as one ecosystem with two interfaces:

- **EchoCert Elite** — Windows desktop professional workflow
- **EchoCert Mobile** — Android field-capture companion

The public GitHub repository remains a demonstration of the core receipt, verification and reporting concepts rather than the complete private commercial product.

---

## Core value

EchoCert helps answer five practical questions:

1. What digital file or record was checked?
2. What SHA-256 digest was recorded for it?
3. What metadata and timestamp were recorded at that point?
4. Does the later file still produce the same digest?
5. Has the receipt or record itself changed since it was sealed?

The goal is **evidence of integrity, not unsupported claims of truth or authenticity**.

---

## EchoCert Elite — desktop

The private controlled-pilot build, **v0.9.4**, has demonstrated:

- SHA-256 file hashing
- JSON receipts
- PDF and TXT reports
- Evidence Pack ZIP creation
- Receipt/file verification
- Case and project metadata
- Local evidence/document storage
- UTC and local timestamp recording
- Timezone / UTC-offset recording
- Explicit clock-source and timestamp-status disclosure
- Windows installation and clean-machine testing

Desktop is intended to remain the professional command centre for evidence certification, reporting, case workflows, audit work and future business/team features.

---

## EchoCert Mobile — Android companion

A private Android development build has been physically tested for:

- Photo capture
- Video capture
- Preservation of captured originals in local evidence storage
- Automatic SHA-256 receipt creation
- One-tap re-hash verification
- Clear integrity-confirmed results when a later file matches

The mobile app is currently a development companion, not a public production release.

---

## Public demo

The public repository demonstrates the earlier AI prompt/output workflow and the same integrity foundations used by the wider product:

- Deterministic JSON receipts
- SHA-256 hashing
- Receipt verification
- Record comparison / diffing
- Human-readable reports
- Local-first operation

AI prompt/output auditing is now best understood as **one EchoCert use case**, not the whole product identity.

---

## What EchoCert can establish

With a valid receipt and matching SHA-256 digest, EchoCert can support the statement that the later checked bytes match the bytes represented by the recorded digest.

It can also record contextual metadata and timestamps for review.

---

## What EchoCert does not establish by itself

EchoCert does not by itself prove:

- the truth of a photograph, video, document or AI output
- who created a file
- legal authorship or ownership
- that a local device clock was independently trusted
- independently trusted creation time without an external timestamp authority
- a complete chain of custody without the surrounding process
- court admissibility or regulatory approval
- forensic accreditation
- private model internals, alignment or safety

The product should state these limits clearly rather than imply more than the evidence supports.

---

## Intended users

Potential users include:

- Legal support and dispute preparation teams
- Compliance and internal audit teams
- Inspection and field-documentation workers
- Property and condition-record users
- Insurance-support workflows
- Construction and trades
- Investigators and consultants
- Researchers
- AI governance teams
- Small organisations needing local-first evidence handling

---

## Design principles

1. **Local-first by default**
2. **Preserve originals where possible**
3. **Simple enough for non-technical users**
4. **Cryptographic integrity underneath the simple workflow**
5. **Honest claims and explicit limitations**
6. **Desktop/mobile compatibility**
7. **Standards-first interoperability**
8. **Evidence should remain usable outside EchoCert**

**Evidence, not interpretation. Integrity, not hype.**

---

## Public vs private product

The public repository shows the basic concepts, demo workflow and documentation.

Private product development may include packaging, production workflows, mobile functionality, case management, enhanced reporting, signing, timestamping, interoperability and deployment features that are not exposed in the public repository.

See [`PRIVATE_PUBLIC_BOUNDARY.md`](PRIVATE_PUBLIC_BOUNDARY.md).
