import pytest

from python_condor import DeployHeader


# todo
# ===== DeployHeader =====
account = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chain_name = "integration-test"
header = DeployHeader(account, chain_name)


# === add_body_hash ===
def test_header_add_body_hash():
    assert not hasattr(header, "body_hash")
    header.add_body_hash(
        "7dca5f79b9d4c7e5fc0f15a34f22b9bb03ae1012071105ce499c2962c64d261d")
    assert header.body_hash is not None

# === to_bytes() ===


def test_header_to_bytes():
    result = header.to_bytes()
    assert result == "xxx"


# ==== byteHash()
def test_header_byteHash():
    result = header.byteHash()
    assert result == "xxx"


# ==== to_json()
def test_header_to_json():
    result = header.to_json()
    assert result == "xxx"
