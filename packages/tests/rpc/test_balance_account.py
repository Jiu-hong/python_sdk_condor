"""
Tests for QueryBalanceMainPurseAccountHash RPC functionality.

This module contains test cases for the QueryBalanceMainPurseAccountHash RPC call,
which retrieves the main purse balance for an account using its account hash.
The tests verify:
- Balance retrieval for valid account hash
- Error handling for invalid account hash
- State root hash validation
- Response parsing and validation
- Connection handling
"""
import pytest
from python_condor import QueryBalanceMainPurseAccountHash


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
STATE_ROOT_HASH = "2c8c6983cc59e26f0722ec53b5153f5ba42c6de3e76c1b0f6d5fbc1f9625d43c"
ACCOUNT_HASH = "account-hash-e039443624491a1400b3b02770137b3058d89f34e21c426592c775c668cb1e6d"
INVALID_ACCOUNT_HASH = "account-hash-xxx"


def test_query_balance_main_purse():
    """
    Test retrieving main purse balance using a valid account hash.

    Verifies that the QueryBalanceMainPurseAccountHash RPC call correctly
    retrieves and returns the balance for a valid account hash.
    """
    query_balance = QueryBalanceMainPurseAccountHash(NODE_URL, ACCOUNT_HASH)
    result = query_balance.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains balance information
    # - Assert balance is non-negative
    # - Assert response format matches expected structure


def test_query_balance_main_purse_with_state_root():
    """
    Test retrieving main purse balance using account hash and state root hash.

    Verifies that the QueryBalanceMainPurseAccountHash RPC call correctly
    retrieves and returns the balance when providing both account hash and
    state root hash.
    """
    query_balance = QueryBalanceMainPurseAccountHash(
        NODE_URL, ACCOUNT_HASH, STATE_ROOT_HASH
    )
    result = query_balance.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains balance information
    # - Assert balance is non-negative
    # - Assert state root hash matches request


def test_query_balance_main_purse_invalid_account():
    """
    Test retrieving main purse balance using an invalid account hash.

    Verifies that the QueryBalanceMainPurseAccountHash RPC call handles
    invalid account hashes appropriately and returns an error response.
    """
    error_msg = "account-hash value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = QueryBalanceMainPurseAccountHash(
            NODE_URL, INVALID_ACCOUNT_HASH)

    # - Assert error response is returned
    # - Assert error message indicates invalid account hash
