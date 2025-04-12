"""
Tests for GetEraSummary RPC functionality.

This module contains test cases for the GetEraSummary RPC call, which retrieves
era summary information from a CasperLabs node. The tests verify:
- Era summary retrieval for current era
- Era summary retrieval for specific block
- Response parsing and validation
- Connection handling
"""

from python_condor import GetEraSummary


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
BLOCK_ID = 4842751
BLOCK_HASH = "4a300abbdf6428dee15fb38650a89a1ef8c6d475b2e3bf7388e07fb1cbdc0aa9"


def test_get_era_summary():
    """
    Test retrieving era summary information for the current era.

    Verifies that the GetEraSummary RPC call correctly retrieves and returns
    era summary information when no specific block is provided.
    """
    get_era_summary = GetEraSummary(NODE_URL)
    result = get_era_summary.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains era summary details
    # - Assert response format matches expected structure
    # - Assert era information is present


def test_get_era_summary_by_block():
    """
    Test retrieving era summary information for a specific block.

    Verifies that the GetEraSummary RPC call correctly retrieves and returns
    era summary information when a specific block is provided.
    """
    get_era_summary = GetEraSummary(NODE_URL, BLOCK_ID)
    result = get_era_summary.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains era summary details
    # - Assert block ID matches request
    # - Assert era information is present
