# EchoCert — Minimal Receipt + Delta Example

This example shows a single immutable receipt and a deterministic delta.
No evaluation logic is involved.

---

## Receipt

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
{
  "same_engine": true,
  "same_model": true,
  "prompt_changed": false,
  "output_changed": true
}

---

### 4️⃣ Save & exit nano
- `CTRL + O` → `Enter`
- `CTRL + X`

---

### 5️⃣ Commit and push (bulk)

```bash
git add EXAMPLE.md
git commit -m "Add minimal receipt and delta example"
git push
