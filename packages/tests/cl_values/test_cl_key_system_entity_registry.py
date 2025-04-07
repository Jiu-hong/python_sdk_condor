import pytest
from python_condor import CLKey


# ===== CLKey - system_entity_registry =====

clkey_system_entity_registry = CLKey(
    "system-entity-registry-0000000000000000000000000000000000000000000000000000000000000000")


def test_clkey_system_entity_registry_serialize():
    result = clkey_system_entity_registry.serialize().hex()
    assert result == "0a0000000000000000000000000000000000000000000000000000000000000000"


def test_clkey_system_entity_registry_string_value():
    result = clkey_system_entity_registry.value()
    assert result == "system-entity-registry-0000000000000000000000000000000000000000000000000000000000000000"


def test_clkey_system_entity_registry_cl_value():
    result = clkey_system_entity_registry.cl_value()
    assert result == "210000000a00000000000000000000000000000000000000000000000000000000000000000b"


def test_clkey_system_entity_registry_to_json():
    result = clkey_system_entity_registry.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_system_entity_registry_invalid_inner_value():
    with pytest.raises(ValueError, match="value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "system-entity-registry-1234")
