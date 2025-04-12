"""
Tests for SessionPackageName functionality.

This module contains test cases for the SessionPackageName class, which represents
package name sessions in CasperLabs transactions. The tests verify:
- Package name session creation with name, version, entrypoint, and arguments
- Byte serialization
- JSON serialization
- Input validation for package name and entrypoint
"""

import pytest

from python_condor import SessionPackageName, CLU256, CLString


# Test data setup
PACKAGE_NAME = "my_hash"
ENTRYPOINT = "apple"
RUNTIME_ARGS = {
    "arg1": CLU256(123),
    "arg2": CLString("hello")
}


def create_test_session_package_name() -> SessionPackageName:
    """
    Create a test session package name with sample data.

    Returns:
        SessionPackageName: A configured test session
    """
    return SessionPackageName(PACKAGE_NAME, None, ENTRYPOINT, RUNTIME_ARGS)


# Expected test results
EXPECTED_BYTES = "04070000006d795f6861736800050000006170706c6502000000040000006172673102000000017b070400000061726732090000000500000068656c6c6f0a"

EXPECTED_JSON = {
    'session': {
        'StoredVersionedContractByName': {
            'name': PACKAGE_NAME,
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
    Test byte serialization of a session package name.

    Verifies that the session package name correctly serializes to the expected byte format.
    """
    session_package_name = create_test_session_package_name()
    result = session_package_name.to_bytes().hex()
    assert result == EXPECTED_BYTES


def test_session_package_name_to_json():
    """
    Test JSON serialization of a session package name.

    Verifies that the session package name correctly serializes to the expected JSON structure.
    """
    session_package_name = create_test_session_package_name()
    result = session_package_name.to_json()
    assert result == EXPECTED_JSON


def test_session_package_name_package_name_empty():
    """
    Test package name validation.

    Verifies that the session package name correctly validates the package name.
    """
    with pytest.raises(ValueError, match="The package name shouldn't be empty."):
        _ = SessionPackageName("", None, ENTRYPOINT, RUNTIME_ARGS)


def test_session_package_name_entrypoint_empty():
    """
    Test entrypoint validation.

    Verifies that the session package name correctly validates the entrypoint.
    """
    with pytest.raises(ValueError, match="The entrypoint shouldn't be empty."):
        _ = SessionPackageName(PACKAGE_NAME, None, "", RUNTIME_ARGS)
