"""
Tests for TransactionRuntime functionality.

This module contains test cases for the TransactionRuntime class, which represents
runtime configuration in CasperLabs transactions. The tests verify:
- Runtime creation with default (VmCasperV1) configuration
- Byte serialization
- JSON serialization
- Input validation for runtime types
"""

import pytest

from python_condor import TransactionRuntime


# Expected test results
EXPECTED_V1_BYTES = "010000000000000000000100000000"
EXPECTED_V1_JSON = {'runtime': 'VmCasperV1'}


def test_transaction_runtime_to_bytes():
    """Test byte serialization of VmCasperV1 runtime."""
    runtime = TransactionRuntime()
    result = runtime.to_bytes().hex()
    assert result == EXPECTED_V1_BYTES


def test_transaction_runtime_to_json():
    """Test JSON serialization of VmCasperV1 runtime."""
    runtime = TransactionRuntime()
    result = runtime.to_json()
    assert result == EXPECTED_V1_JSON


def test_transaction_runtime_invalid_type():
    """Test validation of runtime type."""
    with pytest.raises(ValueError, match="Invalid input VmCasperV2. Allowed values are: VmCasperV1"):
        _ = TransactionRuntime("VmCasperV2")
