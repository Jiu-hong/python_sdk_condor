"""
Tests for TransactionNativeTarget functionality.

This module contains test cases for the TransactionNativeTarget class, which represents
native targets in CasperLabs transactions. The tests verify:
- Native target creation
- Byte serialization
- JSON serialization
"""

from python_condor import TransactionNativeTarget


# Test data setup
def create_test_native_target() -> TransactionNativeTarget:
    """
    Create a test native target.

    Returns:
        TransactionNativeTarget: A configured test target
    """
    return TransactionNativeTarget()


# Expected test results
EXPECTED_NATIVE_BYTES = "010000000000000000000100000000"

EXPECTED_NATIVE_JSON = {'target': "Native"}


def test_target_native_to_bytes():
    """Test byte serialization of native target."""
    target = create_test_native_target()
    result = target.to_bytes().hex()
    assert result == EXPECTED_NATIVE_BYTES


def test_target_native_to_json():
    """Test JSON serialization of native target."""
    target = create_test_native_target()
    result = target.to_json()
    assert result == EXPECTED_NATIVE_JSON
