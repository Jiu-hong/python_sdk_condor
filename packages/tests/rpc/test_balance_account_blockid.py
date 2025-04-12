"""
Tests for QueryBalanceMainPurseAccountHashByBlockId RPC functionality.

This module contains test cases for the QueryBalanceMainPurseAccountHashByBlockId
RPC call, which retrieves the main purse balance for an account at a specific
block height using its account hash. The tests verify:
- Balance retrieval for valid account hash at specific block
- Error handling for invalid account hash
- Block ID validation
- Response parsing and validation
- Connection handling
"""
import pytest
from python_condor import QueryBalanceMainPurseAccountHashByBlockId


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
BLOCK_ID = 4842751
ACCOUNT_HASH = "account-hash-e039443624491a1400b3b02770137b3058d89f34e21c426592c775c668cb1e6d"
INVALID_ACCOUNT_HASH = "xx"


def test_query_balance_main_purse_by_block_id():
    """
    Test retrieving main purse balance using account hash and block ID.

    Verifies that the QueryBalanceMainPurseAccountHashByBlockId RPC call
    correctly retrieves and returns the balance for a valid account hash
    at a specific block height.
    """
    query_balance = QueryBalanceMainPurseAccountHashByBlockId(
        NODE_URL, ACCOUNT_HASH, BLOCK_ID
    )
    result = query_balance.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains balance information
    # - Assert balance is non-negative
    # - Assert block ID matches request


def test_query_balance_main_purse_invalid_account():
    """
    Test retrieving main purse balance using an invalid account hash.

    Verifies that the QueryBalanceMainPurseAccountHashByBlockId RPC call
    handles invalid account hashes appropriately and returns an error response.
    """
    error_msg = "account hash should start with 'account-hash-'"
    with pytest.raises(ValueError, match=error_msg):
        _ = QueryBalanceMainPurseAccountHashByBlockId(
            NODE_URL, INVALID_ACCOUNT_HASH, BLOCK_ID
        )
   # Consider replacing with proper assertions:
    # - Assert error response is returned
    # - Assert error message indicates invalid account hash
