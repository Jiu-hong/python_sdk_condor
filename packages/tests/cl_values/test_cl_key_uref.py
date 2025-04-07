import pytest
from python_condor import CLKey


# ===== CLKey - account_hash =====

clkey_uref = CLKey(
    "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007")


def test_clkey_uref_serialize():
    result = clkey_uref.serialize().hex()
    assert result == "02fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f07"


def test_clkey_uref_string_value():
    result = clkey_uref.value()
    assert result == "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007"


def test_clkey_uref_cl_value():
    result = clkey_uref.cl_value()
    assert result == "2200000002fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f070b"


def test_clkey_uref_to_json():
    result = clkey_uref.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_uref_invalid_inner_length():
    with pytest.raises(ValueError, match="value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "uref-1234-002")


def test_clkey_uref_invalid_inner_suffix():
    with pytest.raises(ValueError, match="uref should end with '000 - 007'"):
        _ = CLKey(
            "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f")
