# EchoCert — Product Definition

EchoCert is a deterministic forensic audit engine for LLM outputs.

## What EchoCert does
- Records prompts and outputs as immutable artifacts
- Produces deterministic structural diffs
- Cryptographically seals all artifacts
- Supports chain-of-custody
- Verifies integrity via replay

## What EchoCert does NOT do
- No truth evaluation
- No alignment scoring
- No safety judgement
- No model introspection
- No probabilistic analysis

## Design principle
Evidence, not interpretation.

EchoCert exists to prove *what changed, when, and whether it was altered* — nothing more.
