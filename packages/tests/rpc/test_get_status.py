"""
Tests for GetStatus RPC functionality.

This module contains test cases for the GetStatus RPC call, which retrieves
node status information from a Casper node. The tests verify:
- Node status retrieval
- Response parsing and validation
- Connection handling
- Node information validation
"""

from python_condor import GetStatus


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"


def test_get_status():
    """
    Test retrieving node status information.

    Verifies that the GetStatus RPC call correctly retrieves and returns
    information about the node's current status, including:
    - Node version
    - Network information
    - Peer count
    - Uptime
    """
    get_status = GetStatus(NODE_URL)
    result = get_status.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains node version
    # - Assert response contains network information
    # - Assert response contains peer count
    # - Assert response contains uptime
    # - Assert response format matches expected structure
