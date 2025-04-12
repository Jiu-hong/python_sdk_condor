"""
Tests for SessionContractHash functionality.

This module contains test cases for the SessionContractHash class, which represents
contract hash sessions in CasperLabs transactions. The tests verify:
- Contract hash session creation with hash, entrypoint, and arguments
- Byte serialization
- JSON serialization
- Input validation for contract hash and entrypoint
"""

import pytest

from python_condor import SessionContractHash, CLU256, CLString


# Test data setup
CONTRACT_HASH = "596b8749bb9434fbb87b1dd0614d1ca3342bf60af9b33c9eea5cd4b49bdd106b"
ENTRYPOINT = "apple"
RUNTIME_ARGS = {
    "arg1": CLU256(123),
    "arg2": CLString("hello")
}


def create_test_session_contract_hash() -> SessionContractHash:
    """
    Create a test session contract hash with sample data.

    Returns:
        SessionContractHash: A configured test session
    """
    return SessionContractHash(CONTRACT_HASH, ENTRYPOINT, RUNTIME_ARGS)


# Expected test results
EXPECTED_BYTES = "01596b8749bb9434fbb87b1dd0614d1ca3342bf60af9b33c9eea5cd4b49bdd106b050000006170706c6502000000040000006172673102000000017b070400000061726732090000000500000068656c6c6f0a"

EXPECTED_JSON = {
    'session': {
        'StoredContractByHash': {
            'hash': CONTRACT_HASH,
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


def test_session_contract_hash_to_bytes():
    """
    Test byte serialization of a session contract hash.

    Verifies that the session contract hash correctly serializes to the expected byte format.
    """
    session_contract_hash = create_test_session_contract_hash()
    result = session_contract_hash.to_bytes().hex()
    assert result == EXPECTED_BYTES


def test_session_contract_hash_to_json():
    """
    Test JSON serialization of a session contract hash.

    Verifies that the session contract hash correctly serializes to the expected JSON structure.
    """
    session_contract_hash = create_test_session_contract_hash()
    result = session_contract_hash.to_json()
    assert result == EXPECTED_JSON


def test_session_contract_hash_incorrect_hash_length():
    """
    Test contract hash validation.

    Verifies that the session contract hash correctly validates the contract hash format.
    """
    with pytest.raises(ValueError, match=r"contract-hash should only contain alphabet and number\(64 length\)"):
        _ = SessionContractHash("1234abcd", ENTRYPOINT, RUNTIME_ARGS)


def test_session_contract_hash_incorrect_entry_type():
    """
    Test entrypoint validation.

    Verifies that the session contract hash correctly validates the entrypoint.
    """
    with pytest.raises(ValueError, match="The entrypoint shouldn't be empty."):
        _ = SessionContractHash(CONTRACT_HASH, "", RUNTIME_ARGS)
