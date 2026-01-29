"""
EchoCert — Deterministic Forensic Audit Engine

Records LLM prompts and outputs as immutable artifacts,
produces deterministic diffs, and cryptographically seals
all evidence for replay and verification.

Non-goals:
- No truth evaluation
- No alignment scoring
- No model introspection
- No safety judgments
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict


# =========================
# CANONICALIZATION
# =========================

def canonical_json(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


# =========================
# RECEIPT MODEL
# =========================

@dataclass(frozen=True)
class Receipt:
    prompt: str
    output: str
    metadata: Dict[str, Any]

    def to_canonical_json(self) -> str:
        payload = {
            "prompt": self.prompt,
            "output": self.output,
            "metadata": self.metadata,
        }
        return canonical_json(payload)

    def hash(self) -> str:
        return sha256_text(self.to_canonical_json())


# =========================
# DIFF ENGINE
# =========================

def compare_receipts(left: Receipt, right: Receipt) -> Dict[str, Dict[str, Any]]:
    left_payload = json.loads(left.to_canonical_json())
    right_payload = json.loads(right.to_canonical_json())

    delta: Dict[str, Dict[str, Any]] = {}

    for key in sorted(set(left_payload) | set(right_payload)):
        lval = left_payload.get(key)
        rval = right_payload.get(key)
        if lval != rval:
            delta[key] = {"left": lval, "right": rval}

    return delta


# =========================
# FORENSIC UTILITIES
# =========================

def write_hash_file(path: str) -> None:
    with open(path, "rb") as f:
        digest = sha256_bytes(f.read())
    with open(path + ".sha256", "w") as f:
        f.write(digest + "\n")


def verify_artifact(path: str) -> None:
    with open(path, "rb") as f:
        data = f.read()

    with open(path + ".sha256") as f:
        expected = f.read().strip()

    actual = sha256_bytes(data)

    if actual != expected:
        raise SystemExit("❌ HASH MISMATCH — artifact altered")

    print("✅ VERIFIED:", path)


def build_context(prev_hash: str | None) -> Dict[str, Any]:
    return {
        "python": sys.version.split()[0],
        "os": platform.system(),
        "echocert_version": "0.1.0",
        "canonicalization": "v1",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "prev_receipt_hash": prev_hash,
        "non_claims": [
            "no_truth_evaluation",
            "no_alignment_scoring",
            "no_model_introspection",
            "no_safety_judgment",
        ],
    }


def load_prev_receipt_hash(path: str) -> str | None:
    sha = path + ".sha256"
    if os.path.exists(sha):
        with open(sha) as f:
            return f.read().strip()
    return None


# =========================
# CLI
# =========================

def main() -> None:
    parser = argparse.ArgumentParser(
        description="EchoCert — Deterministic Forensic Audit Engine"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # record
    record = sub.add_parser("record", help="Create and seal a receipt")
    record.add_argument("--prompt", required=True)
    record.add_argument("--output", required=True)
    record.add_argument("--receipt", required=True)

    # diff
    diff_cmd = sub.add_parser("diff", help="Diff two receipts")
    diff_cmd.add_argument("left")
    diff_cmd.add_argument("right")
    diff_cmd.add_argument("--out", help="Write diff to file and seal it")

    # verify
    verify_cmd = sub.add_parser("verify", help="Verify artifact integrity")
    verify_cmd.add_argument("path")

    args = parser.parse_args()

    if args.command == "record":
        with open(args.prompt) as f:
            prompt = f.read()
        with open(args.output) as f:
            output = f.read()

        prev = load_prev_receipt_hash(args.receipt)
        context = build_context(prev)

        receipt = Receipt(
            prompt=prompt,
            output=output,
            metadata=context,
        )

        with open(args.receipt, "w") as f:
            f.write(receipt.to_canonical_json())

        write_hash_file(args.receipt)
        print("📜 Receipt recorded + sealed:", args.receipt)

    elif args.command == "diff":
        with open(args.left) as f:
            left = Receipt(**json.load(f))
        with open(args.right) as f:
            right = Receipt(**json.load(f))

        delta = compare_receipts(left, right)

        envelope = {
            "added": {},
            "removed": {},
            "changed": delta,
        }

        if args.out:
            with open(args.out, "w") as f:
                json.dump(envelope, f, indent=2, sort_keys=True)
            write_hash_file(args.out)
            print("🧾 Diff written + sealed:", args.out)
        else:
            print(json.dumps(envelope, indent=2, sort_keys=True))


    elif args.command == "verify":
        verify_artifact(args.path)


# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":
    main()

