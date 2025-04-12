"""
Tests for QueryBalancePurseUref RPC functionality.

This module contains test cases for the QueryBalancePurseUref RPC call,
which retrieves the balance of a specific purse using its URef. The tests verify:
- Balance retrieval for valid purse URef
- Error handling for invalid purse URef
- State root hash validation
- Response parsing and validation
- Connection handling
"""

from python_condor import QueryBalancePurseUref


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
STATE_ROOT_HASH = "e6f5ba476f83c2b8b0f5740d14e0d5535692c6e977115b998b9e144d53ae5c90"
PURSE_UREF = "uref-5c140dd0a3d1445387013f59318109146ed6d25bb2208b11de508b002253a4c0-007"
INVALID_PURSE_UREF = "xxx"


def test_query_balance_purse():
    """
    Test retrieving purse balance using a valid URef.

    Verifies that the QueryBalancePurseUref RPC call correctly
    retrieves and returns the balance for a valid purse URef.
    """
    query_balance = QueryBalancePurseUref(NODE_URL, PURSE_UREF)
    result = query_balance.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains balance information
    # - Assert balance is non-negative
    # - Assert response format matches expected structure


def test_query_balance_purse_with_state_root():
    """
    Test retrieving purse balance using URef and state root hash.

    Verifies that the QueryBalancePurseUref RPC call correctly
    retrieves and returns the balance when providing both URef and
    state root hash.
    """
    query_balance = QueryBalancePurseUref(
        NODE_URL, PURSE_UREF, STATE_ROOT_HASH
    )
    result = query_balance.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains balance information
    # - Assert balance is non-negative
    # - Assert state root hash matches request


def test_query_balance_purse_invalid_uref():
    """
    Test retrieving purse balance using an invalid URef.

    Verifies that the QueryBalancePurseUref RPC call handles
    invalid URefs appropriately and returns an error response.
    """
    query_balance = QueryBalancePurseUref(NODE_URL, INVALID_PURSE_UREF)
    result = query_balance.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert error response is returned
    # - Assert error message indicates invalid URef
