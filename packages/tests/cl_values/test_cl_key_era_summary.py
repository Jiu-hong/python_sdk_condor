import pytest
from python_condor import CLKey


# ===== CLKey - era_summary =====
clkey_era_summary = CLKey(
    "era-summary-0000000000000000000000000000000000000000000000000000000000000000")


def test_clkey_era_summary_serialize():
    result = clkey_era_summary.serialize().hex()
    assert result == "0b0000000000000000000000000000000000000000000000000000000000000000"


def test_clkey_era_summary_string_value():
    result = clkey_era_summary.value()
    assert result == "era-summary-0000000000000000000000000000000000000000000000000000000000000000"


def test_clkey_era_summary_cl_value():
    result = clkey_era_summary.cl_value()
    assert result == "210000000b00000000000000000000000000000000000000000000000000000000000000000b"


def test_clkey_era_summary_to_json():
    result = clkey_era_summary.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_era_summary_invalid_inner_value():
    with pytest.raises(ValueError, match="value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "era-summary-1234")
