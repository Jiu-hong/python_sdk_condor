import pytest

from python_condor import CLURef

# ===== CLURef =====
cluref = CLURef(
    "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007")


def test_cluref_serialize():
    result = cluref.serialize().hex()
    assert result == "fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f07"


def test_cluref_value():
    result = cluref.value()
    assert result == "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007"


def test_cluref_cl_value():
    result = cluref.cl_value()
    assert result == "21000000fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f070c"


def test_cluref_to_json():
    result = cluref.to_json()
    assert result == "URef"


# ====incorrect prefix
def test_cluref_incorrect_prefix():
    with pytest.raises(ValueError, match="Input prefix is ref. Expected prefix is 'uref'."):
        _ = CLURef(
            "ref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007")


# ====incorrect length
def test_cluref_incorrect_length():
    with pytest.raises(ValueError, match="Input length is 10. Expected length is 64."):
        _ = CLURef(
            "uref-1234567890-007")


# ====incorrect access right
def test_cluref_incorrect_length():
    with pytest.raises(ValueError, match="Input access right is 008. Expected access right should be between 000-007."):
        _ = CLURef(
            "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-008")
