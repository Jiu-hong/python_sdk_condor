import pytest

from python_condor import CLU32, CLBool, CLOption, CLString, CLTuple1, CLTuple2, CLTuple3, NoneHolder


# ===== CLTuple1 =====

cltuple1 = CLTuple1(CLString("helloworld"))


def test_cltuple1_serialize():
    result = cltuple1.serialize().hex()
    assert result == "0a00000068656c6c6f776f726c64"


def test_cltuple1_value():
    result = cltuple1.value()
    assert result == ('helloworld',)


def test_cltuple1_cl_value():
    result = cltuple1.cl_value()
    assert result == "0e0000000a00000068656c6c6f776f726c64120a"


def test_cltuple1_to_json():
    result = cltuple1.to_json()
    assert result == {'Tuple1': ['String']}


# === check length is not 1
def test_cltuple1_out_of_range():
    with pytest.raises(ValueError, match="Input tuple length is 2. Allowed CLTuple1 length is 1."):
        _ = CLTuple1(CLString("helloworld"), CLBool(True))


# ===== CLTuple2 =====

cltuple2 = CLTuple2((CLString("helloworld"), CLBool(True)))


def test_cltuple2_serialize():
    result = cltuple2.serialize().hex()
    assert result == "0a00000068656c6c6f776f726c6401"


def test_cltuple2_value():
    result = cltuple2.value()
    assert result == ('helloworld', True)


def test_cltuple2_cl_value():
    result = cltuple2.cl_value()
    assert result == "0f0000000a00000068656c6c6f776f726c6401130a00"


def test_cltuple2_to_json():
    result = cltuple2.to_json()
    assert result == {'Tuple2': ['String', 'Bool']}


# === check length is not 2
def test_cltuple2_out_of_range():
    with pytest.raises(ValueError, match="Input tuple length is 1. Allowed CLTuple2 length is 2."):
        _ = CLTuple2((CLString("helloworld"),))

# ===== CLTuple3 =====


cltuple3 = CLTuple3(
    (CLU32(1), CLOption(None, CLString(NoneHolder())), CLOption(CLBool(True))))


def test_cltuple3_serialize():
    result = cltuple3.serialize().hex()
    assert result == "01000000000101"


def test_cltuple3_value():
    result = cltuple3.value()
    assert result == (1, None, True)


def test_cltuple3_cl_value():
    result = cltuple3.cl_value()
    assert result == "070000000100000000010114040d0a0d00"


def test_cltuple3_to_json():
    result = cltuple3.to_json()
    assert result == {'Tuple3': [
        'U32', {'Option': 'String'}, {'Option': 'Bool'}]}


# === check out of range
def test_cltuple3_out_of_range():
    with pytest.raises(ValueError, match="Input tuple length is 1. Allowed CLTuple3 length is 3."):
        _ = CLTuple3((CLString("helloworld"),))
    with pytest.raises(ValueError, match="Input tuple length is 2. Allowed CLTuple3 length is 3."):
        _ = CLTuple3((CLString("helloworld"), CLU32(1)))


# === check invalid inner type
def test_cltuple3_invalid_inner_type():
    with pytest.raises(TypeError, match="The inner type should be CLValue"):
        _ = CLTuple3((1, 2, 3))
