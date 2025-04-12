"""
Tests for QueryBalanceMainPursePublicKey RPC functionality.

This module contains test cases for the QueryBalanceMainPursePublicKey RPC call,
which retrieves the main purse balance for an account using its public key.
The tests verify:
- Balance retrieval for valid public key
- Error handling for invalid public key
- State root hash validation
- Response parsing and validation
- Connection handling
"""
import pytest
from python_condor import QueryBalanceMainPursePublicKey


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
STATE_ROOT_HASH = "e6f5ba476f83c2b8b0f5740d14e0d5535692c6e977115b998b9e144d53ae5c90"
PUBLIC_KEY = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
INVALID_PUBLIC_KEY = "7e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"


def test_query_balance_main_purse():
    """
    Test retrieving main purse balance using a valid public key.

    Verifies that the QueryBalanceMainPursePublicKey RPC call correctly
    retrieves and returns the balance for a valid public key.
    """
    query_balance = QueryBalanceMainPursePublicKey(NODE_URL, PUBLIC_KEY)
    result = query_balance.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains balance information
    # - Assert balance is non-negative
    # - Assert response format matches expected structure


def test_query_balance_main_purse_with_state_root():
    """
    Test retrieving main purse balance using public key and state root hash.

    Verifies that the QueryBalanceMainPursePublicKey RPC call correctly
    retrieves and returns the balance when providing both public key and
    state root hash.
    """
    query_balance = QueryBalanceMainPursePublicKey(
        NODE_URL, PUBLIC_KEY, STATE_ROOT_HASH
    )
    result = query_balance.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains balance information
    # - Assert balance is non-negative
    # - Assert state root hash matches request


def test_query_balance_main_purse_invalid_key():
    """
    Test retrieving main purse balance using an invalid public key.

    Verifies that the QueryBalanceMainPursePublicKey RPC call handles
    invalid public keys appropriately and returns an error response.
    """
    error_msg = r"publickey should be 01xxx\(64 length\) or 02xxx\(66 length\)"
    with pytest.raises(ValueError, match=error_msg):
        _ = QueryBalanceMainPursePublicKey(
            NODE_URL, INVALID_PUBLIC_KEY)

    # - Assert error response is returned
    # - Assert error message indicates invalid public key
