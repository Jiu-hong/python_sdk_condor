"""
Tests for SessionPackageHash functionality.

This module contains test cases for the SessionPackageHash class, which represents
package hash sessions in CasperLabs transactions. The tests verify:
- Package hash session creation with hash, version, entrypoint, and arguments
- Byte serialization
- JSON serialization
- Input validation for package hash and entrypoint
"""

import pytest

from python_condor import SessionPackageHash, CLU256, CLString


# Test data setup
PACKAGE_HASH = "051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef6"
ENTRYPOINT = "apple"
RUNTIME_ARGS = {
    "arg1": CLU256(123),
    "arg2": CLString("hello")
}


def create_test_session_package_hash() -> SessionPackageHash:
    """
    Create a test session package hash with sample data.

    Returns:
        SessionPackageHash: A configured test session
    """
    return SessionPackageHash(PACKAGE_HASH, None, ENTRYPOINT, RUNTIME_ARGS)


# Expected test results
EXPECTED_BYTES = "03051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef600050000006170706c6502000000040000006172673102000000017b070400000061726732090000000500000068656c6c6f0a"

EXPECTED_JSON = {
    'session': {
        'StoredVersionedContractByHash': {
            'hash': PACKAGE_HASH,
            'version': None,
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


def test_session_package_name_to_bytes():
    """
    Test byte serialization of a session package hash.

    Verifies that the session package hash correctly serializes to the expected byte format.
    """
    session_package_hash = create_test_session_package_hash()
    result = session_package_hash.to_bytes().hex()
    assert result == EXPECTED_BYTES


def test_session_package_name_to_json():
    """
    Test JSON serialization of a session package hash.

    Verifies that the session package hash correctly serializes to the expected JSON structure.
    """
    session_package_hash = create_test_session_package_hash()
    result = session_package_hash.to_json()
    assert result == EXPECTED_JSON


def test_session_package_name_package_name_empty():
    """
    Test package hash validation.

    Verifies that the session package hash correctly validates the package hash format.
    """
    with pytest.raises(ValueError, match=r"package-hash should only contain alphabet and number\(64 length\)"):
        _ = SessionPackageHash("", None, ENTRYPOINT, RUNTIME_ARGS)


def test_session_package_name_entrypoint_empty():
    """
    Test entrypoint validation.

    Verifies that the session package hash correctly validates the entrypoint.
    """
    with pytest.raises(ValueError, match="The entrypoint shouldn't be empty."):
        _ = SessionPackageHash(PACKAGE_HASH, None, "", RUNTIME_ARGS)
