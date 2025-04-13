"""
Tests for SessionContractName functionality.

This module contains test cases for the SessionContractName class, which represents
contract name sessions in Casper transactions. The tests verify:
- Contract name session creation with name, entrypoint, and arguments
- Byte serialization
- JSON serialization
- Input validation for contract name and entrypoint
"""

import pytest

from python_condor import SessionContractName, CLU256, CLString


# Test data setup
CONTRACT_NAME = "apple_contract"
ENTRYPOINT = "apple"
RUNTIME_ARGS = {
    "arg1": CLU256(123),
    "arg2": CLString("hello")
}


def create_test_session_contract_name() -> SessionContractName:
    """
    Create a test session contract name with sample data.

    Returns:
        SessionContractName: A configured test session
    """
    return SessionContractName(CONTRACT_NAME, ENTRYPOINT, RUNTIME_ARGS)


# Expected test results
EXPECTED_BYTES = "020e0000006170706c655f636f6e7472616374050000006170706c6502000000040000006172673102000000017b070400000061726732090000000500000068656c6c6f0a"

EXPECTED_JSON = {
    'session': {
        'StoredContractByName': {
            'name': CONTRACT_NAME,
            'entry_point': ENTRYPOINT,
            'args': [
                ('arg1', {
                    'cl_type': 'U256',
                    'bytes': '017b',
                    'parsed': 123
                }),
                ('arg2', {
                    'cl_type': 'String',
                    'bytes': '0500000068656c6c6f',
                    'parsed': 'hello'
                })
            ]
        }
    }
}


def test_session_contract_name_to_bytes():
    """
    Test byte serialization of a session contract name.

    Verifies that the session contract name correctly serializes to the expected byte format.
    """
    session_contract_name = create_test_session_contract_name()
    result = session_contract_name.to_bytes().hex()
    assert result == EXPECTED_BYTES


def test_session_contract_name_to_json():
    """
    Test JSON serialization of a session contract name.

    Verifies that the session contract name correctly serializes to the expected JSON structure.
    """
    session_contract_name = create_test_session_contract_name()
    result = session_contract_name.to_json()
    assert result == EXPECTED_JSON


def test_session_contract_name_contract_name_empty():
    """
    Test contract name validation.

    Verifies that the session contract name correctly validates the contract name.
    """
    with pytest.raises(ValueError, match="The contract name shouldn't be empty."):
        _ = SessionContractName("", ENTRYPOINT, RUNTIME_ARGS)


def test_session_contract_name_entrypoint_empty():
    """
    Test entrypoint validation.

    Verifies that the session contract name correctly validates the entrypoint.
    """
    with pytest.raises(ValueError, match="The entrypoint shouldn't be empty."):
        _ = SessionContractName(CONTRACT_NAME, "", RUNTIME_ARGS)

# # === check entrypoint incorrect type==
# def test_session_contract_name_incorrect_entry_type():
#     contract_name = "596b8749bb9434fbb87b1dd0614d1ca3342bf60af9b33c9eea5cd4b49bdd106b"
#     entrypoint = 123
#     runtime_args = {"arg1": CLU256(123), "arg2": CLString("hello")}
#     with pytest.raises(TypeError, match="The entrypoint should be of type str"):
#         _ = SessionContractName(
#             contract_name, entrypoint, runtime_args)
