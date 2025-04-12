"""
Tests for GetPeers RPC functionality.

This module contains test cases for the GetPeers RPC call, which retrieves
information about connected peers from a CasperLabs node. The tests verify:
- Peer list retrieval
- Response parsing and validation
- Connection handling
- Network connectivity status
"""

from python_condor import GetPeers


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"


def test_get_peers():
    """
    Test retrieving connected peer information.

    Verifies that the GetPeers RPC call correctly retrieves and returns
    information about connected peers, including their network addresses
    and connection status.
    """
    get_peers = GetPeers(NODE_URL)
    result = get_peers.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains peer list
    # - Assert each peer has required fields (address, port, etc.)
    # - Assert response format matches expected structure
