from python_condor import NoneHolder, CLString


# ===== CLString =====

clstring = CLString("helloworld")


def test_clstring_serialize():
    result = clstring.serialize().hex()
    assert result == "0a00000068656c6c6f776f726c64"


def test_clstring_value():
    result = clstring.value()
    assert result == "helloworld"


def test_clstring_cl_value():
    result = clstring.cl_value()
    assert result == "0e0000000a00000068656c6c6f776f726c640a"


def test_clstring_to_json():
    result = clstring.to_json()
    assert result == "String"

# ==== NoneHolder


result_holder_clstring = CLString(NoneHolder())


def test_result_holder_to_json():
    result = result_holder_clstring.to_json()
    assert result == "String"
