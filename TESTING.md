# EchoCert Testing Matrix

## Determinism
- Same prompt + output → identical receipt hash
- Same receipt → identical diff

## Integrity
- Any byte change breaks verification
- Hash mismatch halts verification

## Chain-of-custody
- Receipts record previous receipt hash
- History tampering is detectable

## Negative tests
- Modified receipt → verification fails
- Modified diff → verification fails

## Platforms tested
- Windows + Git Bash
- Python 3.11+
