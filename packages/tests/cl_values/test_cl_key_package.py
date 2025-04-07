import pytest
from python_condor import CLKey


# ===== CLKey - package =====

clkey_package = CLKey(
    "package-6464646464646464646464646464646464646464646464646464646464646464")


def test_clkey_package_serialize():
    result = clkey_package.serialize().hex()
    assert result == "106464646464646464646464646464646464646464646464646464646464646464"


def test_clkey_package_string_value():
    result = clkey_package.value()
    assert result == "package-6464646464646464646464646464646464646464646464646464646464646464"


def test_clkey_package_cl_value():
    result = clkey_package.cl_value()
    assert result == "210000001064646464646464646464646464646464646464646464646464646464646464640b"


def test_clkey_package_to_json():
    result = clkey_package.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_package_invalid_inner_value():
    with pytest.raises(ValueError, match="value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "package-1234")
