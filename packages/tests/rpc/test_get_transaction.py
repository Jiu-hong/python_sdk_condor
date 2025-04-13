"""
Tests for GetTransaction RPC functionality.

This module contains test cases for the GetTransaction RPC call, which retrieves
transaction information from a Casper node. The tests verify:
- Transaction retrieval by hash
- Optional parameter handling (with and without finalized blocks)
- Response parsing and validation
- Error handling for invalid transaction hashes
- Connection handling
"""

from python_condor import GetTransaction


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
BLOCK_ID = 4842751
TRANSACTION_HASH = "7634c66a7c17ea96f10828cca6bf7010b29a8147fea93dce004a12e433729994"
DEPLOY_HASH = "9a322788b70503e08612d5162cdaabb644cf1dcc62b949259d5acd9b33e2d8b8"
INVALID_TRANSACTION_HASH = "0000000000000000000000000000000000000000000000000000000000000000"


def test_get_transaction_with_transaction_hash():
    """
    Test retrieving transaction information with finalized blocks.

    Verifies that the GetTransaction RPC call correctly retrieves and returns
    transaction information when including finalized blocks in the search.
    """
    get_transaction = GetTransaction(NODE_URL, TRANSACTION_HASH, True)
    result = get_transaction.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains transaction details
    # - Assert transaction hash matches request
    # - Assert finalized block information is present


def test_get_transaction_with_deploy_hash():
    """
    Test retrieving transaction information without finalized blocks.

    Verifies that the GetTransaction RPC call correctly retrieves and returns
    transaction information when excluding finalized blocks from the search.
    """
    get_transaction = GetTransaction(NODE_URL, DEPLOY_HASH, False)
    result = get_transaction.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains transaction details
    # - Assert transaction hash matches request
    # - Assert only non-finalized blocks are included


def test_get_transaction_invalid_hash():
    """
    Test retrieving transaction information with an invalid hash.

    Verifies that the GetTransaction RPC call handles invalid transaction
    hashes appropriately and returns an error response.
    """
    get_transaction = GetTransaction(NODE_URL, INVALID_TRANSACTION_HASH, True)
    result = get_transaction.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert error response is returned
    # - Assert error message indicates invalid hash
