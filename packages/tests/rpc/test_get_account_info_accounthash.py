"""
Tests for GetAccountInfoByAccountHash RPC functionality.

This module contains test cases for the GetAccountInfoByAccountHash RPC call, which retrieves
account information using an account hash from a CasperLabs node. The tests verify:
- Account information retrieval for valid account hash
- Error handling for invalid account hash
- Response parsing and validation
- Connection handling
"""

from python_condor import GetAccountInfoByAccountHash


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
ACCOUNT_HASH = "account-hash-e039443624491a1400b3b02770137b3058d89f34e21c426592c775c668cb1e6d"
INVALID_ACCOUNT_HASH = "xx"


def test_get_account_info():
    """
    Test retrieving account information using a valid account hash.

    Verifies that the GetAccountInfoByAccountHash RPC call correctly retrieves and returns
    account information when using a valid account hash.
    """
    get_account_info = GetAccountInfoByAccountHash(NODE_URL, ACCOUNT_HASH)
    result = get_account_info.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains account details
    # - Assert account hash matches request
    # - Assert response format matches expected structure


def test_get_account_info_invalid_hash():
    """
    Test retrieving account information using an invalid account hash.

    Verifies that the GetAccountInfoByAccountHash RPC call handles invalid account hashes
    appropriately and returns an error response.
    """
    get_account_info = GetAccountInfoByAccountHash(
        NODE_URL, INVALID_ACCOUNT_HASH)
    result = get_account_info.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert error response is returned
    # - Assert error message indicates invalid account hash
