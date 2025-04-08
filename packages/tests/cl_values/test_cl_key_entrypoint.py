import pytest
from python_condor import CLKey


# ===== CLKey - entry-point-v1-entity-contract =====
clkey_entrypoint = CLKey(
    "entry-point-v1-entity-contract-53c02487fa9a4bb1cd3e27b849e942cddb97caacb357e5b6bc86f702b2e32dbb-3eba75fc27f0ec2786e09c09d72d61e4c28a86d44d8efc9911460d5438396481")


def test_clkey_entrypoint_serialize():
    result = clkey_entrypoint.serialize().hex()
    assert result == "17000253c02487fa9a4bb1cd3e27b849e942cddb97caacb357e5b6bc86f702b2e32dbb3eba75fc27f0ec2786e09c09d72d61e4c28a86d44d8efc9911460d5438396481"


def test_clkey_entrypoint_string_value():
    result = clkey_entrypoint.value()
    assert result == "entry-point-v1-entity-contract-53c02487fa9a4bb1cd3e27b849e942cddb97caacb357e5b6bc86f702b2e32dbb-3eba75fc27f0ec2786e09c09d72d61e4c28a86d44d8efc9911460d5438396481"


def test_clkey_entrypoint_cl_value():
    result = clkey_entrypoint.cl_value()
    assert result == "4300000017000253c02487fa9a4bb1cd3e27b849e942cddb97caacb357e5b6bc86f702b2e32dbb3eba75fc27f0ec2786e09c09d72d61e4c28a86d44d8efc9911460d54383964810b"


def test_clkey_entrypoint_to_json():
    result = clkey_entrypoint.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_entrypoint_length_invalid():
    with pytest.raises(ValueError, match="Key not valid. It should have vm version, a hash address and a entrypoint hash."):
        _ = CLKey(
            "entry-point-v1-entity-contract-3eba75fc27f0ec2786e09c09d72d61e4c28a86d44d8efc9911460d5438396481")


def test_clkey_entrypoint_version_invalid():
    with pytest.raises(ValueError, match="vm version should be v1"):
        _ = CLKey(
            "entry-point-v2-entity-contract-53c02487fa9a4bb1cd3e27b849e942cddb97caacb357e5b6bc86f702b2e32dbb-3eba75fc27f0ec2786e09c09d72d61e4c28a86d44d8efc9911460d5438396481")
