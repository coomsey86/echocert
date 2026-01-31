# EchoCert

EchoCert generates tamper-evident, hash-verified receipts for LLM outputs.

It proves when an LLM response changes across:
- prompt edits
- model updates
- context / RAG changes

No eval scores. No opinions. Just cryptographic evidence.

## Example

Prompt: "Summarise this contract"

Run A hash: a91c...
Run B hash: f3e2...

Output changed → drift proven.

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
