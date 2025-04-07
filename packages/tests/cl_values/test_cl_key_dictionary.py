import pytest
from python_condor import CLKey


# ===== CLKey - dictionary =====

clkey_dictionary = CLKey(
    "dictionary-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a")


def test_clkey_dictionary_serialize():
    result = clkey_dictionary.serialize().hex()
    assert result == "092a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"


def test_clkey_dictionary_string_value():
    result = clkey_dictionary.value()
    assert result == "dictionary-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"


def test_clkey_dictionary_cl_value():
    result = clkey_dictionary.cl_value()
    assert result == "21000000092a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0b"


def test_clkey_dictionary_to_json():
    result = clkey_dictionary.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_dictionary_invalid_inner_value():
    with pytest.raises(ValueError, match="value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "dictionary-1234")
