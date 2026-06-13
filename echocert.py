"""
EchoCert — local-first AI audit receipt tool.

What it does:
- records an AI prompt + AI output as a deterministic JSON receipt
- seals receipts with SHA-256 hashes
- verifies whether receipts/reports were changed later
- compares two receipts and writes a sealed diff report

What it does NOT do:
- it does not prove an AI answer is true
- it does not inspect private model internals
- it does not replace legal, compliance, or security advice
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
from pathlib import Path
from typing import Any, Dict

VERSION = "0.2.0"
CANONICALIZATION = "v1"


def canonical_json(obj: Any) -> str:
    """Return stable JSON so the same content always hashes the same way."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def read_text_or_literal(value: str, *, from_file: bool) -> str:
    if from_file:
        return Path(value).read_text(encoding="utf-8")
    return value


@dataclass(frozen=True)
class Receipt:
    prompt: str
    output: str
    metadata: Dict[str, Any]

    def to_payload(self) -> Dict[str, Any]:
        return {
            "prompt": self.prompt,
            "output": self.output,
            "metadata": self.metadata,
        }

    def to_canonical_json(self) -> str:
        return canonical_json(self.to_payload())

    def hash(self) -> str:
        return sha256_text(self.to_canonical_json())


class EchoCertError(Exception):
    pass


def write_hash_file(path: str | Path) -> str:
    path = Path(path)
    digest = sha256_bytes(path.read_bytes())
    sha_path = path.with_name(path.name + ".sha256")
    sha_path.write_text(digest + "\n", encoding="utf-8")
    return digest


def verify_artifact(path: str | Path) -> str:
    path = Path(path)
    sha_path = path.with_name(path.name + ".sha256")

    if not path.exists():
        raise EchoCertError(f"Artifact not found: {path}")
    if not sha_path.exists():
        raise EchoCertError(f"Hash file not found: {sha_path}")

    actual = sha256_bytes(path.read_bytes())
    expected = sha_path.read_text(encoding="utf-8").strip()

    if actual != expected:
        raise EchoCertError("HASH MISMATCH — artifact altered or wrong .sha256 file")

    return actual


def build_context(prev_hash: str | None = None, label: str | None = None) -> Dict[str, Any]:
    return {
        "tool": "EchoCert",
        "version": VERSION,
        "canonicalization": CANONICALIZATION,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0],
        "os": platform.system(),
        "label": label,
        "prev_receipt_hash": prev_hash,
        "non_claims": [
            "no_truth_evaluation",
            "no_alignment_scoring",
            "no_model_introspection",
            "no_legal_advice",
        ],
    }


def load_prev_receipt_hash(receipt_path: str | Path) -> str | None:
    receipt_path = Path(receipt_path)
    sha_path = receipt_path.with_name(receipt_path.name + ".sha256")
    if sha_path.exists():
        return sha_path.read_text(encoding="utf-8").strip()
    return None


def load_receipt(path: str | Path) -> Receipt:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    for key in ("prompt", "output", "metadata"):
        if key not in payload:
            raise EchoCertError(f"Invalid receipt: missing {key}")
    return Receipt(prompt=payload["prompt"], output=payload["output"], metadata=payload["metadata"])


def compare_receipts(left: Receipt, right: Receipt) -> Dict[str, Any]:
    left_payload = left.to_payload()
    right_payload = right.to_payload()
    changed: Dict[str, Dict[str, Any]] = {}

    for key in sorted(set(left_payload) | set(right_payload)):
        lval = left_payload.get(key)
        rval = right_payload.get(key)
        if lval != rval:
            changed[key] = {"left": lval, "right": rval}

    return {
        "tool": "EchoCert",
        "version": VERSION,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "left_hash": left.hash(),
        "right_hash": right.hash(),
        "changed": changed,
    }


def write_receipt(prompt: str, output: str, receipt_path: str | Path, label: str | None = None) -> str:
    receipt_path = Path(receipt_path)
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    prev = load_prev_receipt_hash(receipt_path)
    receipt = Receipt(prompt=prompt, output=output, metadata=build_context(prev, label))
    receipt_path.write_text(receipt.to_canonical_json(), encoding="utf-8")
    return write_hash_file(receipt_path)


def write_demo_files() -> None:
    Path("examples").mkdir(exist_ok=True)
    Path("receipts").mkdir(exist_ok=True)
    Path("reports").mkdir(exist_ok=True)

    Path("examples/prompt.txt").write_text(
        "Explain what EchoCert does in plain English.", encoding="utf-8"
    )
    Path("examples/output.txt").write_text(
        "EchoCert creates a timestamped receipt for an AI prompt and output, then seals it with a SHA-256 hash so later changes can be detected.",
        encoding="utf-8",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="EchoCert — local AI audit receipts")
    sub = parser.add_subparsers(dest="command", required=True)

    init_demo = sub.add_parser("init-demo", help="Create example prompt/output folders")

    record = sub.add_parser("record", help="Create and seal a receipt")
    record.add_argument("--prompt", required=True, help="Prompt text or prompt file path")
    record.add_argument("--output", required=True, help="Output text or output file path")
    record.add_argument("--receipt", default="receipts/receipt.json", help="Receipt JSON path")
    record.add_argument("--label", default=None, help="Optional case/client/session label")
    record.add_argument("--from-files", action="store_true", help="Treat --prompt and --output as file paths")

    diff_cmd = sub.add_parser("diff", help="Compare two receipts")
    diff_cmd.add_argument("left")
    diff_cmd.add_argument("right")
    diff_cmd.add_argument("--out", default="reports/diff.json", help="Diff report path")

    verify_cmd = sub.add_parser("verify", help="Verify a receipt/report against its .sha256 file")
    verify_cmd.add_argument("path")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "init-demo":
            write_demo_files()
            print("Demo files created: examples/prompt.txt and examples/output.txt")
            print("Next: python echocert.py record --from-files --prompt examples/prompt.txt --output examples/output.txt")

        elif args.command == "record":
            prompt = read_text_or_literal(args.prompt, from_file=args.from_files)
            output = read_text_or_literal(args.output, from_file=args.from_files)
            digest = write_receipt(prompt, output, args.receipt, args.label)
            print(f"Receipt recorded: {args.receipt}")
            print(f"SHA-256: {digest}")
            print(f"Hash file: {args.receipt}.sha256")

        elif args.command == "diff":
            left = load_receipt(args.left)
            right = load_receipt(args.right)
            report = compare_receipts(left, right)
            out = Path(args.out)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False), encoding="utf-8")
            digest = write_hash_file(out)
            print(f"Diff report written: {out}")
            print(f"SHA-256: {digest}")

        elif args.command == "verify":
            digest = verify_artifact(args.path)
            print(f"VERIFIED: {args.path}")
            print(f"SHA-256: {digest}")

    except EchoCertError as exc:
        raise SystemExit(f"EchoCert error: {exc}") from exc


if __name__ == "__main__":
    main()
