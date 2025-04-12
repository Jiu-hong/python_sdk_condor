"""
Tests for DeployNamedArg functionality.

This module contains test cases for the DeployNamedArg class, which represents
named arguments in CasperLabs transactions. The tests verify:
- Named argument creation with various CLValue types
- Byte serialization
- JSON serialization
- Input validation for argument values
"""

import pytest

from python_condor import DeployNamedArg, CLU256, CLString


# Test data setup
NAMED_ARGS = {
    "amount": CLU256(123),
    "owner": CLU256(456),
    "recipient": CLString("hello")
}


def create_test_deploy_named_arg() -> DeployNamedArg:
    """
    Create a test deploy named arg with sample data.

    Returns:
        DeployNamedArg: A configured test named arg
    """
    return DeployNamedArg(NAMED_ARGS)


# Expected test results
EXPECTED_BYTES = "0300000006000000616d6f756e7402000000017b07050000006f776e65720300000002c8010709000000726563697069656e74090000000500000068656c6c6f0a"

EXPECTED_JSON = [
    ('amount', {
        'cl_type': 'U256',
        'bytes': '017b',
        'parsed': 123
    }),
    ('owner', {
        'cl_type': 'U256',
        'bytes': '02c801',
        'parsed': 456
    }),
    ('recipient', {
        'cl_type': 'String',
        'bytes': '0500000068656c6c6f',
        'parsed': 'hello'
    })
]


def test_deploy_named_arg_to_bytes():
    """
    Test byte serialization of a deploy named arg.

    Verifies that the deploy named arg correctly serializes to the expected byte format.
    """
    deploy_named_arg = create_test_deploy_named_arg()
    result = deploy_named_arg.serialize().hex()
    assert result == EXPECTED_BYTES


def test_deploy_named_arg_to_json():
    """
    Test JSON serialization of a deploy named arg.

    Verifies that the deploy named arg correctly serializes to the expected JSON structure.
    """
    deploy_named_arg = create_test_deploy_named_arg()
    result = deploy_named_arg.to_json()
    assert result == EXPECTED_JSON


def test_deploy_named_arg_incorrect_value():
    """
    Test value validation.

    Verifies that the deploy named arg correctly validates the argument values.
    """
    with pytest.raises(ValueError, match="The value for NamedArg should be CLValue."):
        _ = DeployNamedArg({"amount": 123})
