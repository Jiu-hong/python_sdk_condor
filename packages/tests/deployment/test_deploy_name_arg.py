import pytest

from python_condor import DeployNamedArg, CLU256, CLString


# ===== DeployNamedArg =====

deploy_named_arg = DeployNamedArg({"amount": CLU256(123), "owner": CLU256(
    456), 'recipient': CLString("hello")})


def test_deploy_named_arg_to_bytes():
    result = deploy_named_arg.serialize().hex()
    assert result == "0300000006000000616d6f756e7402000000017b07050000006f776e65720300000002c8010709000000726563697069656e74090000000500000068656c6c6f0a"


def test_deploy_named_arg_to_json():
    result = deploy_named_arg.to_json()
    assert result == [('amount', {'cl_type': 'U256', 'bytes': '017b', 'parsed': 123}), ('owner', {
        'cl_type': 'U256', 'bytes': '02c801', 'parsed': 456}), ('recipient', {'cl_type': 'String', 'bytes': '0500000068656c6c6f', 'parsed': 'hello'})]


# === check DeployNamedArg incorrect value==
def test_deploy_named_arg_to_json():

    with pytest.raises(ValueError, match="The value for NamedArg should be CLValue."):
        _ = DeployNamedArg({"amount": 123})
