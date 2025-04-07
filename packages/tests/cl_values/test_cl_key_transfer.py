import pytest
from python_condor import CLKey


# ===== CLKey - trasfer =====
clkey_transfer = CLKey(
    "transfer-199957ab005a1bdc246691cb8bfba69ad9a7ee3fd856ad25ff51bb63406584ad")


def test_clkey_transfer_serialize():
    result = clkey_transfer.serialize().hex()
    assert result == "03199957ab005a1bdc246691cb8bfba69ad9a7ee3fd856ad25ff51bb63406584ad"


def test_clkey_transfer_string_value():
    result = clkey_transfer.value()
    assert result == "transfer-199957ab005a1bdc246691cb8bfba69ad9a7ee3fd856ad25ff51bb63406584ad"


def test_clkey_transfer_cl_value():
    result = clkey_transfer.cl_value()
    assert result == "2100000003199957ab005a1bdc246691cb8bfba69ad9a7ee3fd856ad25ff51bb63406584ad0b"


def test_clkey_transfer_to_json():
    result = clkey_transfer.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_transfer_invalid_inner_value():
    with pytest.raises(ValueError, match="value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "transfer-1234")
