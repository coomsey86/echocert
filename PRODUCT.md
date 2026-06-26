# EchoCert — Product Definition

## Product summary

EchoCert is a local-first AI evidence and audit tool.

It helps users create tamper-evident records for AI prompts, outputs and related files. The public prototype demonstrates receipt creation, verification, diffing and report generation.

---

## Core value

EchoCert helps answer four practical questions:

1. What was the original prompt or file?
2. What was the AI output or result?
3. When was the record created?
4. Has the record changed since it was sealed?

---

## What EchoCert does

- Records prompts and outputs as evidence artefacts
- Creates deterministic JSON receipts
- Uses SHA-256 hashing for integrity checks
- Verifies whether stored records still match their receipt
- Produces comparison reports between versions
- Generates human-readable reports
- Supports evidence-pack style workflows
- Runs locally, reducing dependence on external platforms

---

## What EchoCert does not do

- No truth evaluation
- No legal authorship decision by itself
- No alignment scoring
- No safety judgement
- No private model introspection
- No replacement for professional legal, security or compliance advice

---

## Design principle

**Evidence, not interpretation.**

EchoCert exists to help prove what was recorded, when it was recorded and whether it was altered later.

---

## Public vs private product

The public repository is a demonstration build. It shows the basic workflow and product direction.

Private commercial builds may include additional workflow, packaging, reporting, signing, case-management or deployment features that are not included in the public repository.

See [`PRIVATE_PUBLIC_BOUNDARY.md`](PRIVATE_PUBLIC_BOUNDARY.md).
