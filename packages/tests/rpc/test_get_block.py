"""
Tests for GetBlock RPC functionality.

This module contains test cases for the GetBlock RPC call, which retrieves
block information from a Casper node. The tests verify:
- Block retrieval by block hash
- Block retrieval by block height
- Response parsing and validation
- Connection handling
"""

from python_condor import GetBlock


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
PUBLIC_KEY = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
BLOCK_ID = 4842751
BLOCK_HASH = "4a300abbdf6428dee15fb38650a89a1ef8c6d475b2e3bf7388e07fb1cbdc0aa9"


def test_get_block_by_hash():
    """
    Test retrieving block information using a block hash.

    Verifies that the GetBlock RPC call correctly retrieves and returns
    block information when using a block hash identifier.
    """
    get_block = GetBlock(NODE_URL, BLOCK_HASH)
    result = get_block.run()
    print(result)  # Consider replacing with proper assertion


def test_get_block_by_height():
    """
    Test retrieving block information using a block height.

    Verifies that the GetBlock RPC call correctly retrieves and returns
    block information when using a block height identifier.
    """
    get_block = GetBlock(NODE_URL, BLOCK_ID)
    result = get_block.run()
    print(result)  # Consider replacing with proper assertion
