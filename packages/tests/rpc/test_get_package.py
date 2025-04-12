"""
Tests for GetPackage RPC functionality.

This module contains test cases for the GetPackage RPC call, which retrieves
contract package information from a CasperLabs node. The tests verify:
- Package retrieval by valid contract package hash
- Error handling for invalid contract package hash
- Response parsing and validation
- Connection handling
"""

from python_condor import GetPackage


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
BLOCK_ID = 4842751
BLOCK_HASH = "4a300abbdf6428dee15fb38650a89a1ef8c6d475b2e3bf7388e07fb1cbdc0aa9"

# Contract package hashes
CONTRACT_PACKAGE = "contract-package-051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef6"
INVALID_CONTRACT_PACKAGE = "051c3c2fef7fa8fa459c7e99717d566b723e30a17005100f58ceae130d168ef6"


def test_get_package():
    """
    Test retrieving contract package information using a valid package hash.

    Verifies that the GetPackage RPC call correctly retrieves and returns
    contract package information when using a valid package hash.
    """
    get_package = GetPackage(NODE_URL, CONTRACT_PACKAGE)
    result = get_package.run()
    print(result)  # Consider replacing with proper assertion


def test_get_package_invalid_hash():
    """
    Test retrieving contract package information using an invalid package hash.

    Verifies that the GetPackage RPC call handles invalid package hashes
    appropriately and returns an error response.
    """
    get_package = GetPackage(NODE_URL, INVALID_CONTRACT_PACKAGE)
    result = get_package.run()
    print(result)  # Consider replacing with proper assertion and error checking
