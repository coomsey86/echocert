# EchoCert — Digital Evidence Integrity

## One-line pitch

EchoCert is a local-first desktop and mobile evidence-integrity system that helps people preserve digital originals, create SHA-256 receipts and later verify whether files still match.

---

## The problem

Important digital evidence is now routinely created on phones and computers, but the evidence trail around it is often weak.

Common problems include:

- Photos and videos are copied, compressed, re-exported or edited.
- Documents are renamed or changed with no clear integrity record.
- Screenshots are easy to dispute.
- Field workers need a simple way to preserve what they captured.
- Small organisations often cannot justify heavyweight forensic tooling.
- AI-assisted work can be copied or changed without a reliable record of the original output.

The technical question is often simple:

**Is this later file the same digital file that was recorded earlier?**

---

## What EchoCert does

EchoCert creates a practical integrity trail around digital files.

The wider product direction includes:

- Preserve original files where possible
- Generate SHA-256 hashes
- Create structured integrity receipts
- Re-hash files later and compare the result
- Produce human-readable reports
- Build evidence packs
- Record case/project metadata
- Support field photo/video capture on mobile
- Keep core workflows local-first

---

## Two interfaces, one evidence model

### EchoCert Elite — Windows desktop

The controlled-pilot build is intended for professional evidence, reporting, verification, case and evidence-pack workflows.

### EchoCert Mobile — Android companion

The development companion is intended for field capture and fast verification. Photo and video capture → original preservation → receipt creation → re-hash verification has been demonstrated on a physical Android device.

> **One platform. Two interfaces. One evidence format.**

---

## Honest evidence claims

EchoCert is built to be useful without pretending a hash proves more than it does.

A matching SHA-256 digest can strongly support that the checked bytes are unchanged from the bytes represented by the recorded digest.

EchoCert does **not** by itself prove:

- that a photograph or video depicts a true event
- who created the file
- legal ownership or authorship
- independently trusted time when only a local device clock was used
- a complete chain of custody
- court admissibility, regulatory approval or forensic accreditation
- that an AI output is true

Where a timestamp is unanchored local system time, that should be disclosed clearly.

---

## Who could use it

Potential markets include:

- Legal support and dispute preparation
- Compliance and internal audit
- Inspection and field documentation
- Property and condition reporting
- Insurance-support documentation
- Construction and trades
- Investigators and consultants
- Researchers
- AI governance and AI-assisted workflow records
- Small organisations needing straightforward local-first evidence tools

---

## Why the desktop + mobile combination matters

Many evidence workflows start in the field but are reviewed, packaged or reported later on a computer.

EchoCert is being designed around that reality:

**Capture in the field → preserve and receipt → verify → review/package on desktop.**

The product aims to make cryptographic integrity usable without requiring the end user to understand cryptography.

---

## Commercial direction

EchoCert may be offered through:

- Professional desktop licences
- Mobile companion access
- Controlled pilots
- Evidence-pack and verification services
- Business/team licensing
- Managed integrity workflows
- Integration or licensed components where appropriate

Commercial success depends on pilot validation, security hardening, UX quality and distribution. The product should earn adoption through reliable real-world use rather than inflated claims.

---

## Public repository boundary

This repository is a source-available public demonstration of core receipt and verification concepts. It does not contain the full private EchoCert Elite or Android product, client material, private keys, production signing infrastructure or protected implementation details.

AI prompt/output receipt auditing remains a supported EchoCert use case and part of the project's history, but EchoCert is no longer positioned solely as an LLM audit tool.

See [`PRIVATE_PUBLIC_BOUNDARY.md`](PRIVATE_PUBLIC_BOUNDARY.md).
