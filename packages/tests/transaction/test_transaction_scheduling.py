"""
Tests for TransactionScheduling functionality.

This module contains test cases for the TransactionScheduling class, which represents
scheduling configuration in Casper transactions. The tests verify:
- Scheduling creation with default (Standard) configuration
- Byte serialization
- JSON serialization
- Input validation for scheduling types
"""

import pytest

from python_condor import TransactionScheduling


# Expected test results
EXPECTED_STANDARD_BYTES = "010000000000000000000100000000"
EXPECTED_STANDARD_JSON = {'scheduling': 'Standard'}


def test_transaction_scheduling_to_bytes():
    """Test byte serialization of standard scheduling."""
    scheduling = TransactionScheduling()
    result = scheduling.to_bytes().hex()
    assert result == EXPECTED_STANDARD_BYTES


def test_transaction_scheduling_to_json():
    """Test JSON serialization of standard scheduling."""
    scheduling = TransactionScheduling()
    result = scheduling.to_json()
    assert result == EXPECTED_STANDARD_JSON


def test_transaction_scheduling_invalid_type():
    """Test validation of scheduling type."""
    with pytest.raises(ValueError, match="Invalid input: somethingelse. Valid allowed values: Standard"):
        _ = TransactionScheduling("somethingelse")
