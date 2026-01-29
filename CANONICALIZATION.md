# EchoCert — Canonicalization Specification

This document defines the canonicalization rules used by EchoCert to ensure
deterministic hashing of receipts.

## Scope
Canonicalization applies only to valid JSON values. EchoCert does not infer,
coerce, or normalize non-JSON types.

## Rules

1. Objects
- Keys are sorted lexicographically at every level.
- Canonicalization is applied recursively.

2. Arrays
- Order is preserved.
- Arrays are not re-sorted or modified.
- Index position is semantically meaningful.

3. Primitives
- Strings, numbers, booleans, and null are encoded as-is.
- No implicit normalization or casting is performed.

4. Timestamps
- Treated as first-class data.
- Included explicitly by the caller.
- Not normalized or adjusted.

5. Metadata
- Caller-controlled.
- Canonicalized structurally like any other JSON object.
- Hashed as provided.

## Non-Goals
- No semantic inference
- No intent detection
- No evaluation or scoring
- No hidden defaults

Canonicalization stabilizes representation only.
Meaning is external to the artifact.
