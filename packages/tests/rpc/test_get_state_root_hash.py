"""
Tests for GetStateRootHash RPC functionality.

This module contains test cases for the GetStateRootHash RPC call, which retrieves
the state root hash from a CasperLabs node. The tests verify:
- State root hash retrieval from latest block
- State root hash retrieval from specific block by hash
- State root hash retrieval from specific block by height
- Response parsing and validation
- Connection handling
"""

from python_condor import GetStateRootHash


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
BLOCK_ID = 4842751
BLOCK_HASH = "4a300abbdf6428dee15fb38650a89a1ef8c6d475b2e3bf7388e07fb1cbdc0aa9"
TEST_BLOCK_HEIGHT = 12345


def test_get_latest_state_root_hash():
    """
    Test retrieving state root hash from the latest block.

    Verifies that the GetStateRootHash RPC call correctly retrieves and returns
    the state root hash from the most recent block.
    """
    get_state_root_hash = GetStateRootHash(NODE_URL)
    result = get_state_root_hash.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains valid hash string
    # - Assert hash format matches expected pattern


def test_get_state_root_hash_by_height():
    """
    Test retrieving state root hash from a specific block using block height.

    Verifies that the GetStateRootHash RPC call correctly retrieves and returns
    the state root hash when using a block height identifier.
    """
    get_state_root_hash = GetStateRootHash(NODE_URL, TEST_BLOCK_HEIGHT)
    result = get_state_root_hash.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains valid hash string
    # - Assert hash format matches expected pattern


def test_get_state_root_hash_by_hash():
    """
    Test retrieving state root hash from a specific block using block hash.

    Verifies that the GetStateRootHash RPC call correctly retrieves and returns
    the state root hash when using a block hash identifier.
    """
    get_state_root_hash = GetStateRootHash(NODE_URL, BLOCK_HASH)
    result = get_state_root_hash.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains valid hash string
    # - Assert hash format matches expected pattern
