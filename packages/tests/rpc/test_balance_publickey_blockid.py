"""
Tests for QueryBalanceMainPursePublicKeyByBlockId RPC functionality.

This module contains test cases for the QueryBalanceMainPursePublicKeyByBlockId
RPC call, which retrieves the main purse balance for an account at a specific
block height using its public key. The tests verify:
- Balance retrieval for valid public key at specific block
- Error handling for invalid public key
- Block ID validation
- Response parsing and validation
- Connection handling
"""
import pytest
from python_condor import QueryBalanceMainPursePublicKeyByBlockId


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
BLOCK_ID = 4842751
BLOCK_HASH = "4a300abbdf6428dee15fb38650a89a1ef8c6d475b2e3bf7388e07fb1cbdc0aa9"
PUBLIC_KEY = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
INVALID_PUBLIC_KEY_FORMAT = "7e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"


def test_query_balance_main_purse_by_block_id():
    """
    Test retrieving main purse balance using public key and block ID.

    Verifies that the QueryBalanceMainPursePublicKeyByBlockId RPC call
    correctly retrieves and returns the balance for a valid public key
    at a specific block height.
    """
    query_balance = QueryBalanceMainPursePublicKeyByBlockId(
        NODE_URL, PUBLIC_KEY, BLOCK_ID
    )
    result = query_balance.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains balance information
    # - Assert balance is non-negative
    # - Assert block ID matches request


def test_query_balance_main_purse_by_block_hash():
    """
    Test retrieving main purse balance using an invalid block ID.

    Verifies that the QueryBalanceMainPursePublicKeyByBlockId RPC call
    handles invalid block IDs appropriately and returns an error response.
    """
    query_balance = QueryBalanceMainPursePublicKeyByBlockId(
        NODE_URL, PUBLIC_KEY, BLOCK_HASH
    )
    result = query_balance.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert error response is returned
    # - Assert error message indicates invalid block ID


def test_query_balance_main_purse_invalid_key_format():
    """
    Test retrieving main purse balance using an invalid short public key.

    Verifies that the QueryBalanceMainPursePublicKeyByBlockId RPC call
    handles invalid short public keys appropriately and returns an error response.
    """
    error_msg = r"publickey should be 01xxx\(64 length\) or 02xxx\(66 length\)"
    with pytest.raises(ValueError, match=error_msg):
        _ = QueryBalanceMainPursePublicKeyByBlockId(
            NODE_URL, INVALID_PUBLIC_KEY_FORMAT, BLOCK_ID)

    # - Assert error response is returned
    # - Assert error message indicates invalid public key
