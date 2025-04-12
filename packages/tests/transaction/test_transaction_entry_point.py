"""
Tests for TransactionEntryPoint functionality.

This module contains test cases for the TransactionEntryPoint class, which represents
entry points in CasperLabs transactions. The tests verify:
- Entry point creation for all supported types
- Byte serialization
- JSON serialization
- Input validation for entry point types and names
"""

import pytest

from python_condor import TransactionEntryPoint


# Test data setup
CUSTOM_ENTRY_POINT_NAME = "test2"


def create_test_entry_point(entry_point_type: str, name: str = None) -> TransactionEntryPoint:
    """
    Create a test entry point with sample data.

    Args:
        entry_point_type: Type of entry point (Call, Custom, Transfer, etc.)
        name: Optional name for Custom entry point

    Returns:
        TransactionEntryPoint: A configured test entry point
    """
    return TransactionEntryPoint(entry_point_type, name)


# Expected test results
EXPECTED_CALL_BYTES = "010000000000000000000100000000"
EXPECTED_CALL_JSON = {'entry_point': 'Call'}

EXPECTED_CUSTOM_BYTES = "020000000000000000000100010000000a00000001050000007465737432"
EXPECTED_CUSTOM_JSON = {'entry_point': {'Custom': CUSTOM_ENTRY_POINT_NAME}}

EXPECTED_TRANSFER_BYTES = "010000000000000000000100000002"
EXPECTED_TRANSFER_JSON = {'entry_point': 'Transfer'}

EXPECTED_ADD_BID_BYTES = "010000000000000000000100000003"
EXPECTED_ADD_BID_JSON = {'entry_point': 'Add_Bid'}

EXPECTED_WITHDRAW_BID_BYTES = "010000000000000000000100000004"
EXPECTED_WITHDRAW_BID_JSON = {'entry_point': 'Withdraw_Bid'}

EXPECTED_DELEGATE_BYTES = "010000000000000000000100000005"
EXPECTED_DELEGATE_JSON = {'entry_point': 'Delegate'}

EXPECTED_UNDELEGATE_BYTES = "010000000000000000000100000006"
EXPECTED_UNDELEGATE_JSON = {'entry_point': 'Undelegate'}

EXPECTED_REDELEGATE_BYTES = "010000000000000000000100000007"
EXPECTED_REDELEGATE_JSON = {'entry_point': 'Redelegate'}

EXPECTED_ACTIVATE_BID_BYTES = "010000000000000000000100000008"
EXPECTED_ACTIVATE_BID_JSON = {'entry_point': 'Activate_Bid'}

EXPECTED_CHANGE_PUBLIC_KEY_BYTES = "010000000000000000000100000009"
EXPECTED_CHANGE_PUBLIC_KEY_JSON = {'entry_point': 'ChangePublicKey'}


def test_entry_point_call_to_bytes():
    """Test byte serialization of Call entry point."""
    entry_point = create_test_entry_point("Call")
    result = entry_point.to_bytes().hex()
    assert result == EXPECTED_CALL_BYTES


def test_entry_point_call_to_json():
    """Test JSON serialization of Call entry point."""
    entry_point = create_test_entry_point("Call")
    result = entry_point.to_json()
    assert result == EXPECTED_CALL_JSON


def test_entry_point_custom_to_bytes():
    """Test byte serialization of Custom entry point."""
    entry_point = create_test_entry_point("Custom", CUSTOM_ENTRY_POINT_NAME)
    result = entry_point.to_bytes().hex()
    assert result == EXPECTED_CUSTOM_BYTES


def test_entry_point_custom_to_json():
    """Test JSON serialization of Custom entry point."""
    entry_point = create_test_entry_point("Custom", CUSTOM_ENTRY_POINT_NAME)
    result = entry_point.to_json()
    assert result == EXPECTED_CUSTOM_JSON


def test_entry_point_transfer_to_bytes():
    """Test byte serialization of Transfer entry point."""
    entry_point = create_test_entry_point("Transfer")
    result = entry_point.to_bytes().hex()
    assert result == EXPECTED_TRANSFER_BYTES


def test_entry_point_transfer_to_json():
    """Test JSON serialization of Transfer entry point."""
    entry_point = create_test_entry_point("Transfer")
    result = entry_point.to_json()
    assert result == EXPECTED_TRANSFER_JSON


def test_entry_point_add_bid_to_bytes():
    """Test byte serialization of Add_Bid entry point."""
    entry_point = create_test_entry_point("Add_Bid")
    result = entry_point.to_bytes().hex()
    assert result == EXPECTED_ADD_BID_BYTES


def test_entry_point_add_bid_to_json():
    """Test JSON serialization of Add_Bid entry point."""
    entry_point = create_test_entry_point("Add_Bid")
    result = entry_point.to_json()
    assert result == EXPECTED_ADD_BID_JSON


def test_entry_point_withdraw_bid_to_bytes():
    """Test byte serialization of Withdraw_Bid entry point."""
    entry_point = create_test_entry_point("Withdraw_Bid")
    result = entry_point.to_bytes().hex()
    assert result == EXPECTED_WITHDRAW_BID_BYTES


def test_entry_point_withdraw_bid_to_json():
    """Test JSON serialization of Withdraw_Bid entry point."""
    entry_point = create_test_entry_point("Withdraw_Bid")
    result = entry_point.to_json()
    assert result == EXPECTED_WITHDRAW_BID_JSON


def test_entry_point_delegate_to_bytes():
    """Test byte serialization of Delegate entry point."""
    entry_point = create_test_entry_point("Delegate")
    result = entry_point.to_bytes().hex()
    assert result == EXPECTED_DELEGATE_BYTES


def test_entry_point_delegate_to_json():
    """Test JSON serialization of Delegate entry point."""
    entry_point = create_test_entry_point("Delegate")
    result = entry_point.to_json()
    assert result == EXPECTED_DELEGATE_JSON


def test_entry_point_undelegate_to_bytes():
    """Test byte serialization of Undelegate entry point."""
    entry_point = create_test_entry_point("Undelegate")
    result = entry_point.to_bytes().hex()
    assert result == EXPECTED_UNDELEGATE_BYTES


def test_entry_point_undelegate_to_json():
    """Test JSON serialization of Undelegate entry point."""
    entry_point = create_test_entry_point("Undelegate")
    result = entry_point.to_json()
    assert result == EXPECTED_UNDELEGATE_JSON


def test_entry_point_redelegate_to_bytes():
    """Test byte serialization of Redelegate entry point."""
    entry_point = create_test_entry_point("Redelegate")
    result = entry_point.to_bytes().hex()
    assert result == EXPECTED_REDELEGATE_BYTES


def test_entry_point_redelegate_to_json():
    """Test JSON serialization of Redelegate entry point."""
    entry_point = create_test_entry_point("Redelegate")
    result = entry_point.to_json()
    assert result == EXPECTED_REDELEGATE_JSON


def test_entry_point_activate_bid_to_bytes():
    """Test byte serialization of Activate_Bid entry point."""
    entry_point = create_test_entry_point("Activate_Bid")
    result = entry_point.to_bytes().hex()
    assert result == EXPECTED_ACTIVATE_BID_BYTES


def test_entry_point_activate_bid_to_json():
    """Test JSON serialization of Activate_Bid entry point."""
    entry_point = create_test_entry_point("Activate_Bid")
    result = entry_point.to_json()
    assert result == EXPECTED_ACTIVATE_BID_JSON


def test_entry_point_change_public_key_to_bytes():
    """Test byte serialization of ChangePublicKey entry point."""
    entry_point = create_test_entry_point("ChangePublicKey")
    result = entry_point.to_bytes().hex()
    assert result == EXPECTED_CHANGE_PUBLIC_KEY_BYTES


def test_entry_point_change_public_key_to_json():
    """Test JSON serialization of ChangePublicKey entry point."""
    entry_point = create_test_entry_point("ChangePublicKey")
    result = entry_point.to_json()
    assert result == EXPECTED_CHANGE_PUBLIC_KEY_JSON


def test_entry_point_invalid_type():
    """Test validation of entry point type."""
    with pytest.raises(ValueError, match=r"Invalid input: somegthingelse. Allowed values are: \('Call', 'Custom', 'Transfer', 'Add_Bid', 'Withdraw_Bid', 'Delegate', 'Undelegate', 'Redelegate', 'Activate_Bid', 'ChangePublicKey'\)"):
        _ = TransactionEntryPoint("somegthingelse")


def test_entry_point_custom_empty_name():
    """Test validation of Custom entry point name."""
    with pytest.raises(ValueError, match="Entrypoint name cannot be empty for Custom."):
        _ = TransactionEntryPoint("Custom")
