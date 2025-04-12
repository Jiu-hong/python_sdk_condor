"""
Tests for GetAccountInfoByPublicKey RPC functionality.

This module contains test cases for the GetAccountInfoByPublicKey RPC call, which retrieves
account information using a public key from a CasperLabs node. The tests verify:
- Account information retrieval for valid public key
- Error handling for invalid public key
- Response parsing and validation
- Connection handling
"""

from python_condor import GetAccountInfoByPublicKey


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
PUBLIC_KEY = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
INVALID_PUBLIC_KEY = "12345"


def test_get_account_info():
    """
    Test retrieving account information using a valid public key.

    Verifies that the GetAccountInfoByPublicKey RPC call correctly retrieves and returns
    account information when using a valid public key.
    """
    get_account_info = GetAccountInfoByPublicKey(NODE_URL, PUBLIC_KEY)
    result = get_account_info.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains account details
    # - Assert public key matches request
    # - Assert response format matches expected structure


def test_get_account_info_invalid_key():
    """
    Test retrieving account information using an invalid public key.

    Verifies that the GetAccountInfoByPublicKey RPC call handles invalid public keys
    appropriately and returns an error response.
    """
    get_account_info = GetAccountInfoByPublicKey(NODE_URL, INVALID_PUBLIC_KEY)
    result = get_account_info.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert error response is returned
    # - Assert error message indicates invalid public key
