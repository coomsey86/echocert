# EchoCert Public Demo Pitch

## One-line explanation

EchoCert is a local-first digital evidence integrity system. This public demo uses safe AI prompt/output examples to demonstrate the same receipt, SHA-256 verification and tamper-detection foundations used by the wider product.

---

## The wider problem

Important digital files — photos, videos, documents and AI-assisted records — can be copied, edited, renamed, compressed, re-exported or disputed later.

People need a simple way to preserve an integrity record and check later whether a digital file or receipt still matches what was recorded.

---

## What this public demo shows

The repository's safe demo workflow currently uses prompt/output records because they are easy to reproduce without exposing real customer or legal evidence.

The demo shows how EchoCert can:

1. Record example data.
2. Create a deterministic JSON receipt.
3. Generate SHA-256 integrity data.
4. Verify the record later.
5. Detect a changed record.
6. Produce a human-readable report.

---

## How this relates to the current product

The private product direction is broader than the public AI demo:

- **EchoCert Elite** — Windows desktop evidence, receipt, verification, report and evidence-pack workflow.
- **EchoCert Mobile** — Android field-capture companion for photo/video capture and re-verification.

AI prompt/output auditing remains one supported use case rather than the entire product.

---

## The value

EchoCert does not claim that a SHA-256 hash proves truth, authorship or an independently trusted time.

It helps answer a narrower and useful integrity question:

**Does the digital file or record checked later still match the integrity value recorded earlier?**

---

## Public-safe statement

This repository exposes demonstration code, documentation and public-safe integrity concepts only. It does not expose the complete private EchoCert Elite/Mobile builds, customer evidence, credentials, signing infrastructure or protected production implementation details.

See [`PRIVATE_PUBLIC_BOUNDARY.md`](PRIVATE_PUBLIC_BOUNDARY.md).
