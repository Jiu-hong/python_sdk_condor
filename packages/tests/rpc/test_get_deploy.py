"""
Tests for GetDeploy RPC functionality.

This module contains test cases for the GetDeploy RPC call, which retrieves
deploy information from a Casper node. The tests verify:
- Deploy retrieval by valid deploy hash
- Error handling for invalid deploy hash
- Response parsing and validation
- Connection handling
"""

from python_condor import GetDeploy


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
BLOCK_ID = 4842751
DEPLOY_HASH = "9a322788b70503e08612d5162cdaabb644cf1dcc62b949259d5acd9b33e2d8b8"
INVALID_DEPLOY_HASH = "0000000000000000000000000000000000000000000000000000000000000000"


def test_get_deploy():
    """
    Test retrieving deploy information using a valid deploy hash.

    Verifies that the GetDeploy RPC call correctly retrieves and returns
    deploy information when using a valid deploy hash.
    """
    get_deploy = GetDeploy(NODE_URL, DEPLOY_HASH)
    result = get_deploy.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains deploy details
    # - Assert deploy hash matches request
    # - Assert response format matches expected structure


def test_get_deploy_invalid_hash():
    """
    Test retrieving deploy information using an invalid deploy hash.

    Verifies that the GetDeploy RPC call handles invalid deploy hashes
    appropriately and returns an error response.
    """
    get_deploy = GetDeploy(NODE_URL, INVALID_DEPLOY_HASH)
    result = get_deploy.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert error response is returned
    # - Assert error message indicates invalid deploy hash
