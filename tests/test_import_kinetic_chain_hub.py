import copy
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import import_kinetic_chain_hub as K  # noqa: E402


def test_rejects_unsafe_public_value():
    with pytest.raises(K.ImportError, match="不安全"):
        K._reject_unsafe({"text": "C:\\private\\paper.pdf"})


def test_atomic_write_preserves_valid_json(tmp_path):
    target = tmp_path / "bundle.json"
    K.write_atomic(target, {"ok": True, "title": "游泳"})
    assert json.loads(target.read_text(encoding="utf-8")) == {"ok": True, "title": "游泳"}


def test_hash_ignores_generation_time_and_hash_field():
    payload = {"manifest": {"generated_at": "one", "content_hash": ""}, "records": []}
    first = K._canonical_hash(payload)
    changed = copy.deepcopy(payload)
    changed["manifest"]["generated_at"] = "two"
    changed["manifest"]["content_hash"] = "f" * 64
    assert K._canonical_hash(changed) == first
