import pytest
from python_condor import CLKey


# ===== CLKey - checksum_registry =====

clkey_checksum_registry = CLKey(
    "checksum-registry-0000000000000000000000000000000000000000000000000000000000000000")


def test_clkey_checksum_registry_serialize():
    result = clkey_checksum_registry.serialize().hex()
    assert result == "0e0000000000000000000000000000000000000000000000000000000000000000"


def test_clkey_checksum_registry_string_value():
    result = clkey_checksum_registry.value()
    assert result == "checksum-registry-0000000000000000000000000000000000000000000000000000000000000000"


def test_clkey_checksum_registry_cl_value():
    result = clkey_checksum_registry.cl_value()
    assert result == "210000000e00000000000000000000000000000000000000000000000000000000000000000b"


def test_clkey_checksum_registry_to_json():
    result = clkey_checksum_registry.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_checksum_registry_invalid_inner_value():
    with pytest.raises(ValueError, match="value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "checksum-registry-1234")
