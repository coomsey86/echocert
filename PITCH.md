# EchoCert — Deterministic Audit Receipts for LLM Outputs

## The Problem

LLM outputs change over time due to:
- model updates
- safety tuning
- infrastructure changes

Most platforms rely on internal logs that are:
- mutable
- non-deterministic
- unverifiable by third parties

This creates risk in regulated, legal, and safety-critical contexts.

---

## What EchoCert Is

EchoCert is a deterministic audit engine that:
- treats prompts and outputs as static artifacts
- generates tamper-evident hashes
- produces immutable receipts
- enables drift and delta comparison over time

EchoCert does NOT:
- judge correctness
- evaluate alignment
- inspect model internals

It produces evidence, not opinions.

---

## Why Determinism Matters

If two parties hash the same output, they get the same result.
This enables:
- independent verification
- audit trails
- dispute resolution
- regulatory evidence

---

## Why External Audit Matters

Internal logs are controlled by the same entity that changes the model.
EchoCert creates a neutral, external audit surface.

---

## Use Cases

- Internal regression tracking
- Red-team and safety investigations
- Compliance and governance evidence
- Incident response
- Liability protection

EchoCert is infrastructure, not a policy engine.

