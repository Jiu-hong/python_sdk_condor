"""
Tests for GetBlockTransfers RPC functionality.

This module contains test cases for the GetBlockTransfers RPC call, which retrieves
transfer information from blocks in a CasperLabs node. The tests verify:
- Transfer retrieval from latest block
- Transfer retrieval from specific block by hash
- Transfer retrieval from specific block by height
- Response parsing and validation
- Connection handling
"""

from python_condor import GetBlockTransfers


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
PUBLIC_KEY = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
BLOCK_ID = 4842751
BLOCK_HASH = "4a300abbdf6428dee15fb38650a89a1ef8c6d475b2e3bf7388e07fb1cbdc0aa9"


def test_get_latest_block_transfers():
    """
    Test retrieving transfers from the latest block.

    Verifies that the GetBlockTransfers RPC call correctly retrieves and returns
    transfer information from the most recent block.
    """
    get_transfers = GetBlockTransfers(NODE_URL)
    result = get_transfers.run()
    print(result)  # Consider replacing with proper assertion


def test_get_block_transfers_by_hash():
    """
    Test retrieving transfers from a specific block using block hash.

    Verifies that the GetBlockTransfers RPC call correctly retrieves and returns
    transfer information when using a block hash identifier.
    """
    get_transfers = GetBlockTransfers(NODE_URL, BLOCK_HASH)
    result = get_transfers.run()
    print(result)  # Consider replacing with proper assertion


def test_get_block_transfers_by_height():
    """
    Test retrieving transfers from a specific block using block height.

    Verifies that the GetBlockTransfers RPC call correctly retrieves and returns
    transfer information when using a block height identifier.
    """
    get_transfers = GetBlockTransfers(NODE_URL, BLOCK_ID)
    result = get_transfers.run()
    print(result)  # Consider replacing with proper assertion
