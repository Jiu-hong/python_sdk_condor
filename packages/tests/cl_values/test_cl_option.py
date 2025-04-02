import pytest

from python_condor import CLString, CLOption, NoneHolder


# ===== CLOption(CLString) =====

cloption_string = CLOption(CLString("helloworld"))


def test_cloption_string_serialize():
    result = cloption_string.serialize().hex()
    assert result == "010a00000068656c6c6f776f726c64"


def test_cloption_string_value():
    result = cloption_string.value()
    assert result == "helloworld"


def test_cloption_string_cl_value():
    result = cloption_string.cl_value()
    assert result == "0f000000010a00000068656c6c6f776f726c640d0a"


def test_cloption_string_to_json():
    result = cloption_string.to_json()
    assert result == {"Option": "String"}


# ==== NoneHolder
result_holder_cloption_string = CLOption(CLString(NoneHolder()))


def test_result_holder_to_json():
    result = result_holder_cloption_string.to_json()
    assert result == {"Option": "String"}


# ===== CLOption(None) =====
cloption_none = CLOption(None, CLString(NoneHolder()))


def test_cloption_string_serialize():
    result = cloption_none.serialize().hex()
    assert result == "00"


def test_cloption_string_value():
    result = cloption_none.value()
    assert result == None


def test_cloption_string_cl_value():
    result = cloption_none.cl_value()
    assert result == "01000000000d0a"


def test_cloption_string_to_json():
    result = cloption_none.to_json()
    assert result == {"Option": "String"}
