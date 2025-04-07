import pytest
from python_condor import CLKey


# ===== CLKey - era =====
clkey_era = CLKey(
    "era-42")


def test_clkey_era_serialize():
    result = clkey_era.serialize().hex()
    assert result == "052a00000000000000"


def test_clkey_era_string_value():
    result = clkey_era.value()
    assert result == "era-42"


def test_clkey_era_cl_value():
    result = clkey_era.cl_value()
    assert result == "09000000052a000000000000000b"


def test_clkey_era_to_json():
    result = clkey_era.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_era_invalid_inner_value():
    with pytest.raises(ValueError, match="era value should be int"):
        _ = CLKey(
            "era-h12")
