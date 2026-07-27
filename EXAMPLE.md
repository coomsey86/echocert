# EchoCert — Legacy Public Receipt + Delta Example

This is a small historical/public-safe example from EchoCert's earlier AI prompt/output audit workflow.

It remains useful for demonstrating deterministic receipts and change detection, but it should not be read as the complete current EchoCert product. See [`README.md`](README.md) for the current desktop/mobile evidence-integrity direction.

---

## Example receipt

```json
{
  "receipt_id": "7c3e9b",
  "timestamp_utc": 1738101234.12,
  "engine_id": "echocert-core-v0.1.0",
  "model_id": "example-llm",
  "prompt_hash": "a91d3f",
  "output_hash": "f03b8c",
  "metadata": {
    "source": "demo"
  }
}
```

## Example deterministic delta

```json
{
  "same_engine": true,
  "same_model": true,
  "prompt_changed": false,
  "output_changed": true
}
```

No truth evaluation or model judgement is involved. The example simply illustrates how a stored record can represent integrity values and how a later comparison can identify a change.
