# EchoCert — Receipt Model

EchoCert receipts are immutable, standalone artifacts representing a single
prompt/output snapshot.

## Immutability
- Receipts are never modified after creation.
- Any change results in a new receipt.

## Versioning
- Receipt schema/version is explicit.
- New versions produce new receipts.
- Old receipts are never rewritten.

## Core Fields (Conceptual)
- receipt_id
- timestamp_utc
- engine_id
- model_id
- prompt_hash
- output_hash
- metadata

## Hashing
- All hashes are derived from canonicalized JSON.
- A receipt-of-receipt hash may be computed for tamper evidence.

## Deltas
- Deltas are derived by deterministic structural comparison of receipts.
- No heuristics, weighting, or interpretation.
- Added / removed / changed fields are reported explicitly.

## Non-Goals
- No truth or correctness claims
- No alignment judgments
- No model introspection

Receipts are evidence.
Interpretation is external.
