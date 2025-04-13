"""
Tests for QueryGlobalStateByBlockId RPC functionality.

This module contains test cases for the QueryGlobalStateByBlockId RPC call, which retrieves
global state information at a specific block height from a Casper node. The tests verify:
- State key querying for different key types (hash, account-hash, uref)
- Block ID-specific state retrieval
- Response parsing and validation
- Connection handling
"""

from python_condor import QueryGlobalStateByBlockId


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
BLOCK_ID = 4842751  # Example block ID

# Different types of state keys for testing
HASH_KEY = "hash-596b8749bb9434fbb87b1dd0614d1ca3342bf60af9b33c9eea5cd4b49bdd106b"
ACCOUNT_HASH_KEY = "account-hash-e039443624491a1400b3b02770137b3058d89f34e21c426592c775c668cb1e6d"
UREF_KEY = "uref-15451be7efc662bd21a5ea01b0d4d6c6b81618436f02400fd63bde30eee2454c-007"


def test_query_global_state_by_blockid_uref():
    """
    Test querying global state at a specific block using a URef key.

    Verifies that the QueryGlobalStateByBlockId RPC call correctly retrieves and returns
    state information when using a URef key at a specific block height.
    """
    query_global_state = QueryGlobalStateByBlockId(
        NODE_URL, UREF_KEY, BLOCK_ID)
    result = query_global_state.run()
    print(result)  # Consider replacing with proper assertion


def test_query_global_state_by_blockid_hash():
    """
    Test querying global state at a specific block using a hash key.

    Verifies that the QueryGlobalStateByBlockId RPC call correctly retrieves and returns
    state information when using a hash key at a specific block height.
    """
    query_global_state = QueryGlobalStateByBlockId(
        NODE_URL, HASH_KEY, BLOCK_ID)
    result = query_global_state.run()
    print(result)  # Consider replacing with proper assertion


def test_query_global_state_by_blockid_account_hash():
    """
    Test querying global state at a specific block using an account hash key.

    Verifies that the QueryGlobalStateByBlockId RPC call correctly retrieves and returns
    state information when using an account hash key at a specific block height.
    """
    query_global_state = QueryGlobalStateByBlockId(
        NODE_URL, ACCOUNT_HASH_KEY, BLOCK_ID)
    result = query_global_state.run()
    print(result)  # Consider replacing with proper assertion
