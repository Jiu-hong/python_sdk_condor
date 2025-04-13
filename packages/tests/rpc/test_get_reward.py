"""
Tests for GetReward RPC functionality.

This module contains test cases for the GetReward RPC call, which retrieves
reward information for validators and delegators from a Casper node. The tests verify:
- Reward retrieval for validators
- Reward retrieval for delegators
- Era-specific reward information
- Response parsing and validation
- Connection handling
"""

from python_condor import GetReward


# Test data setup
NODE_URL = "http://node.integration.casper.network:7777/rpc"
VALIDATOR_KEY = "0115c9b40c06ff99b0cbadf1140b061b5dbf92103e66a6330fbcc7768f5219c1ce"
DELEGATOR_KEY = "01005e50796e225c0f6aa0d61c0fa0bda5af8aa23c194414bf2bbed1e0a774f2a6"
TEST_ERA = 17430


def test_get_reward():
    """
    Test retrieving reward information for a validator and delegator.

    Verifies that the GetReward RPC call correctly retrieves and returns
    reward information for a specific validator and delegator pair at a
    given era.
    """
    get_reward = GetReward(NODE_URL, VALIDATOR_KEY, DELEGATOR_KEY, TEST_ERA)
    result = get_reward.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains reward information
    # - Assert reward amounts are non-negative
    # - Assert era matches requested era


def test_get_validator_only_reward():
    """
    Test retrieving reward information for a validator only.

    Verifies that the GetReward RPC call correctly retrieves and returns
    reward information for a validator without a delegator at a given era.
    """
    get_reward = GetReward(NODE_URL, VALIDATOR_KEY, None, TEST_ERA)
    result = get_reward.run()
    print(result)  # Consider replacing with proper assertions:
    # - Assert response contains validator reward information
    # - Assert reward amounts are non-negative
    # - Assert era matches requested era
