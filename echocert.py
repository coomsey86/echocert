"""EchoCert records prompts and outputs as static artifacts and hashes them for tamper-evident receipts.

Non-goals: it does not evaluate truth, intent, alignment, safety, or model internals.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from typing import Any, Dict


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def canonical_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


@dataclass(frozen=True)
class Receipt:
    prompt: str
    output: str
    metadata: Dict[str, Any]

    def to_canonical_json(self) -> str:
        payload = {"prompt": self.prompt, "output": self.output, "metadata": self.metadata}
        return canonical_json(payload)

    def hash(self) -> str:
        return sha256_text(self.to_canonical_json())

    def receipt_of_receipt(self) -> str:
        return sha256_text(self.hash())


def compare_receipts(left: Receipt, right: Receipt) -> Dict[str, Dict[str, Any]]:
    left_payload = json.loads(left.to_canonical_json())
    right_payload = json.loads(right.to_canonical_json())
    delta: Dict[str, Dict[str, Any]] = {}
    for key in sorted(set(left_payload) | set(right_payload)):
        left_value = left_payload.get(key)
        right_value = right_payload.get(key)
        if left_value != right_value:
            delta[key] = {"left": left_value, "right": right_value}
    return delta
