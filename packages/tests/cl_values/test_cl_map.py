import pytest

from python_condor import CLList, CLMap, CLU32, CLU8, CLOption, CLString


# ===== CLMap =====

clmap = CLMap({CLU8(3): CLOption(CLString("Jim")), CLU8(
    2): CLOption(CLString("Jack")), CLU8(4): CLOption(CLString("Jane")), CLU8(1): CLOption(CLString("Jill"))})


def test_clmap_serialize():
    result = clmap.serialize().hex()
    assert result == "040000000101040000004a696c6c0201040000004a61636b0301030000004a696d0401040000004a616e65"


def test_clmap_value():
    result = clmap.value()
    assert result == [
        {
            "key": 3,
            "value": "Jim"
        },
        {
            "key": 2,
            "value": "Jack"
        },
        {
            "key": 4,
            "value": "Jane"
        },        {
            "key": 1,
            "value": "Jill"
        },
    ]


def test_clmap_cl_value():
    result = clmap.cl_value()
    assert result == "2b000000040000000101040000004a696c6c0201040000004a61636b0301030000004a696d0401040000004a616e6511030d0a"


def test_clmap_to_json():
    result = clmap.to_json()
    assert result == {
        "Map": {
            "key": "U8",
            "value": {
                "Option": "String"
            }
        }
    }
# === check invalid inner type


def test_cllist_invalid_inner_type():
    with pytest.raises(TypeError, match="Invalid type of input: <class 'python_condor.cl_values.cl_string.CLString'> for CLList. Allowed value is <class 'list'>"):
        _ = CLList(CLString("helloworld"))


# === check inconsistent inner elements
def test_cllist_invalid_inner_type():
    with pytest.raises(TypeError, match="types aren't consistent in the elements"):
        _ = CLList([CLString("helloworld"), CLU32(123)])
