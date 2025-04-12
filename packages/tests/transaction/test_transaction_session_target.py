"""
Tests for TransactionSessionTarget functionality.

This module contains test cases for the TransactionSessionTarget class, which represents
session targets in CasperLabs transactions. The tests verify:
- Session target creation with install/upgrade flag
- Byte serialization
- JSON serialization
"""

from python_condor import TransactionSessionTarget


# Test data setup
MODULE_BYTES = "000102030405"
RUNTIME = "VmCasperV1"


def create_test_session_target(is_install: bool = True) -> TransactionSessionTarget:
    """
    Create a test session target with sample data.

    Args:
        is_install: Whether this is an install/upgrade target

    Returns:
        TransactionSessionTarget: A configured test target
    """
    return TransactionSessionTarget(RUNTIME, MODULE_BYTES, is_install)


# Expected test results
EXPECTED_INSTALL_BYTES = (
    "040000000000000000000100010000000200020000000300110000001b000000020101000000000000000000010000000006000000000102030405"
)

EXPECTED_INSTALL_JSON = {
    'target': {
        'Session': {
            'is_install_upgrade': True,
            'module_bytes': MODULE_BYTES,
            'runtime': RUNTIME
        }
    }
}

EXPECTED_NO_INSTALL_BYTES = (
    "040000000000000000000100010000000200020000000300110000001b000000020001000000000000000000010000000006000000000102030405"
)

EXPECTED_NO_INSTALL_JSON = {
    'target': {
        'Session': {
            'is_install_upgrade': False,
            'module_bytes': MODULE_BYTES,
            'runtime': RUNTIME
        }
    }
}


def test_target_session_install_to_bytes():
    """Test byte serialization of install session target."""
    target = create_test_session_target(is_install=True)
    result = target.to_bytes().hex()
    assert result == EXPECTED_INSTALL_BYTES


def test_target_session_install_to_json():
    """Test JSON serialization of install session target."""
    target = create_test_session_target(is_install=True)
    result = target.to_json()
    assert result == EXPECTED_INSTALL_JSON


def test_target_session_no_install_to_bytes():
    """Test byte serialization of non-install session target."""
    target = create_test_session_target(is_install=False)
    result = target.to_bytes().hex()
    assert result == EXPECTED_NO_INSTALL_BYTES


def test_target_session_no_install_to_json():
    """Test JSON serialization of non-install session target."""
    target = create_test_session_target(is_install=False)
    result = target.to_json()
    assert result == EXPECTED_NO_INSTALL_JSON
