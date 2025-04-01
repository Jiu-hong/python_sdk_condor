import pytest

from python_condor import CLList, CLU32, CLOption, CLString


# ===== CLList =====

cllist = CLList([CLOption(CLString("hello")), CLOption(CLString("world"))])


def test_cllist_serialize():
    result = cllist.serialize().hex()
    assert result == "02000000010500000068656c6c6f0105000000776f726c64"


def test_cllist_value():
    result = cllist.value()
    assert result == ['hello', 'world']


def test_cllist_cl_value():
    result = cllist.cl_value()
    assert result == "1800000002000000010500000068656c6c6f0105000000776f726c640e0d0a"


def test_cllist_to_json():
    result = cllist.to_json()
    assert result == {'List': {'Option': 'String'}}


# === check invalid inner type
def test_cllist_invalid_inner_type():
    with pytest.raises(TypeError, match="Invalid type of input: <class 'python_condor.cl_values.cl_string.CLString'> for CLList. Allowed value is <class 'list'>"):
        _ = CLList(CLString("helloworld"))


# === check inconsistent inner elements
def test_cllist_invalid_inner_type():
    with pytest.raises(TypeError, match="types aren't consistent in the elements"):
        _ = CLList([CLString("helloworld"), CLU32(123)])
