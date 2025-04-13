"""
Tests for SessionModuleBytes functionality.

This module contains test cases for the SessionModuleBytes class, which represents
module bytes sessions in Casper transactions. The tests verify:
- Module bytes session creation with bytes and arguments
- Byte serialization
- JSON serialization
"""

from python_condor import SessionModuleBytes, CLU256, CLString


# Test data setup
MODULE_BYTES = "01234567"
RUNTIME_ARGS = {
    "arg1": CLU256(123),
    "arg2": CLString("hello")
}


def create_test_session_module_bytes() -> SessionModuleBytes:
    """
    Create a test session module bytes with sample data.

    Returns:
        SessionModuleBytes: A configured test session
    """
    return SessionModuleBytes(MODULE_BYTES, RUNTIME_ARGS)


# Expected test results
EXPECTED_BYTES = "00040000000123456702000000040000006172673102000000017b070400000061726732090000000500000068656c6c6f0a"

EXPECTED_JSON = {
    'session': {
        'ModuleBytes': {
            'module_bytes': MODULE_BYTES,
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


def test_session_module_bytes_to_bytes():
    """
    Test byte serialization of a session module bytes.

    Verifies that the session module bytes correctly serializes to the expected byte format.
    """
    session_module_bytes = create_test_session_module_bytes()
    result = session_module_bytes.to_bytes().hex()
    assert result == EXPECTED_BYTES


def test_session_module_bytes_to_json():
    """
    Test JSON serialization of a session module bytes.

    Verifies that the session module bytes correctly serializes to the expected JSON structure.
    """
    session_module_bytes = create_test_session_module_bytes()
    result = session_module_bytes.to_json()
    assert result == EXPECTED_JSON
