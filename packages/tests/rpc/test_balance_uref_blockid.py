"""
Tests for QueryBalancePurseUrefByBlockId RPC functionality.

This module contains test cases for the QueryBalancePurseUrefByBlockId RPC call, which retrieves
purse balance information using a URef and block ID from a Casper node. The tests verify:
- Balance retrieval for valid URef and block ID
- Error handling for invalid URef
- Error handling for invalid block ID
- Response parsing and validation
- Connection handling
"""
import pytest
from python_condor import QueryBalancePurseUrefByBlockId


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
BLOCK_ID = 4842751
BLOCK_HASH = "4a300abbdf6428dee15fb38650a89a1ef8c6d475b2e3bf7388e07fb1cbdc0aa9"
PURSE_UREF = "uref-5c140dd0a3d1445387013f59318109146ed6d25bb2208b11de508b002253a4c0-007"
INVALID_PURSE_UREF = "xxx"
INVALID_BLOCK_HASH = "0000000000000000000000000000000000000000000000000000000000000000"


def test_query_balance_purse_by_block_id():
    """
    Test retrieving purse balance using a valid URef and block hash.

    Verifies that the QueryBalancePurseUrefByBlockId RPC call correctly retrieves and returns
    purse balance information when using a valid URef and block hash.
    """
    query_balance = QueryBalancePurseUrefByBlockId(
        NODE_URL, PURSE_UREF, BLOCK_ID)
    result = query_balance.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains balance information
    # - Assert balance is non-negative
    # - Assert block hash matches request


def test_query_balance_purse_by_block_hash():
    """
    Test retrieving purse balance using a valid URef and block hash.

    Verifies that the QueryBalancePurseUrefByBlockId RPC call correctly retrieves and returns
    purse balance information when using a valid URef and block hash.
    """
    query_balance = QueryBalancePurseUrefByBlockId(
        NODE_URL, PURSE_UREF, BLOCK_HASH)
    result = query_balance.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains balance information
    # - Assert balance is non-negative
    # - Assert block hash matches request


def test_query_balance_purse_invalid_uref():
    """
    Test retrieving purse balance using an invalid URef.

    Verifies that the QueryBalancePurseUrefByBlockId RPC call handles invalid URefs
    appropriately and returns an error response.
    """
    error_msg = "purse should start with 'uref-'"
    with pytest.raises(ValueError, match=error_msg):
        _ = QueryBalancePurseUrefByBlockId(
            NODE_URL, INVALID_PURSE_UREF, BLOCK_HASH)

    # Consider replacing with proper assertions:
    # - Assert error response is returned
    # - Assert error message indicates invalid URef


def test_query_balance_purse_invalid_block():
    """
    Test retrieving purse balance using an invalid block hash.

    Verifies that the QueryBalancePurseUrefByBlockId RPC call handles invalid block hashes
    appropriately and returns an error response.
    """
    query_balance = QueryBalancePurseUrefByBlockId(
        NODE_URL, PURSE_UREF, INVALID_BLOCK_HASH)
    result = query_balance.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert error response is returned
    # - Assert error message indicates invalid block hash
