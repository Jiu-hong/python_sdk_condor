import pytest
from python_condor import CLKey


# ===== CLKey - deploy =====
clkey_deploy = CLKey(
    "deploy-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a")


def test_clkey_deploy_serialize():
    result = clkey_deploy.serialize().hex()
    assert result == "042a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"


def test_clkey_deploy_string_value():
    result = clkey_deploy.value()
    assert result == "deploy-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"


def test_clkey_deploy_cl_value():
    result = clkey_deploy.cl_value()
    assert result == "21000000042a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0b"


def test_clkey_deploy_to_json():
    result = clkey_deploy.to_json()
    assert result == "Key"


# === check invalid inner type
def test_clkey_deploy_invalid_inner_value():
    with pytest.raises(ValueError, match="value should be 64 length only containing alphabet and number"):
        _ = CLKey(
            "deploy-1234")
