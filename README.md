# EchoCert

EchoCert is a deterministic audit and receipt engine for large language model (LLM) outputs.

It records AI responses as static artifacts, generates tamper-evident hashes, and produces verifiable receipts that expose output drift, silent changes, and behavioral deltas over time.

EchoCert does not evaluate truth, intent, alignment, or model internals.
It produces evidence, not judgments.

## Why EchoCert exists

Modern LLM systems change over time. Most tooling attempts to *judge* those changes.

EchoCert does not.

EchoCert provides deterministic, cryptographically verifiable evidence of LLM output drift — without making claims about correctness, safety, or intent.

- Not a safety classifier
- Not a compliance authority
- Not a live agent or prompt modifier

## What EchoCert Is
- A forensic audit layer for AI outputs
- A black-box flight recorder for LLM behavior
- A reproducible, inspectable, deterministic system

## What EchoCert Is Not
- Not a model evaluator
- Not a safety classifier
- Not a compliance authority
- Not a live agent or prompt modifier

## Intended users

- AI platform teams
- Compliance & risk teams
- Legal & audit functions
- Organisations that need evidence, not opinions

EchoCert is designed to support governance, compliance, research, and accountability workflows.
