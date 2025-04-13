"""
Tests for DeployHeader functionality.

This module contains test cases for the DeployHeader class, which represents
deploy headers in Casper transactions. The tests verify:
- Header creation with various parameters
- Body hash handling
- Byte serialization and hashing
- JSON serialization
- Input validation for account, chain name, timestamp, TTL, and gas price
"""

import pytest
from datetime import datetime

from python_condor import DeployHeader


# Test data setup
ACCOUNT = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
CHAIN_NAME = "integration-test"
TIMESTAMP = datetime.fromisoformat('2025-03-26T03:11:48.829Z')
TTL = 30
GAS_PRICE = 1
BODY_HASH = "7dca5f79b9d4c7e5fc0f15a34f22b9bb03ae1012071105ce499c2962c64d261d"


def create_test_deploy_header() -> DeployHeader:
    """
    Create a test deploy header with sample data.

    Returns:
        DeployHeader: A configured test header
    """
    return DeployHeader(ACCOUNT, CHAIN_NAME, TIMESTAMP, ttl=TTL, gas_price=GAS_PRICE)


# Expected test results
EXPECTED_BYTES = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f55d486fd09501000040771b000000000001000000000000007dca5f79b9d4c7e5fc0f15a34f22b9bb03ae1012071105ce499c2962c64d261d0000000010000000696e746567726174696f6e2d74657374"

EXPECTED_HASH = "a0935128f23f700d2b5a87640830967d3a14ae6652a86faf7f77e04b26c536f2"

EXPECTED_JSON = {
    'header': {
        'account': ACCOUNT,
        'timestamp': '2025-03-26T03:11:48.829Z',
        'ttl': f'{TTL}m',
        'gas_price': GAS_PRICE,
        'body_hash': BODY_HASH,
        'dependencies': [],
        'chain_name': CHAIN_NAME
    }
}


def test_header_add_body_hash():
    """
    Test adding body hash to a deploy header.

    Verifies that the body hash is correctly added and stored in the header.
    """
    header = create_test_deploy_header()
    assert not hasattr(header, "body_hash")
    header.add_body_hash(BODY_HASH)
    assert header.body_hash is not None


def test_header_to_bytes():
    """
    Test byte serialization of a deploy header.

    Verifies that the header correctly serializes to the expected byte format.
    """
    header = create_test_deploy_header()
    header.add_body_hash(BODY_HASH)
    result = header.to_bytes().hex()
    assert result == EXPECTED_BYTES


def test_header_byteHash():
    """
    Test hash generation for a deploy header.

    Verifies that the header correctly generates the expected hash.
    """
    header = create_test_deploy_header()
    header.add_body_hash(BODY_HASH)
    result = header.byteHash()
    assert result == EXPECTED_HASH


def test_header_to_json():
    """
    Test JSON serialization of a deploy header.

    Verifies that the header correctly serializes to the expected JSON structure.
    """
    header = create_test_deploy_header()
    header.add_body_hash(BODY_HASH)
    result = header.to_json()
    assert result == EXPECTED_JSON


def test_header_check_account_pattern():
    """
    Test account pattern validation.

    Verifies that the header correctly validates the account format.
    """
    with pytest.raises(ValueError, match=r"account should be 01xxx\(64 length\) or 02xxx\(66 length\)"):
        _ = DeployHeader("xxxx", CHAIN_NAME, TIMESTAMP,
                         ttl=TTL, gas_price=GAS_PRICE)


def test_header_check_chain_name():
    """
    Test chain name validation.

    Verifies that the header correctly validates the chain name.
    """
    with pytest.raises(ValueError, match="The chain_name shouldn't be empty."):
        _ = DeployHeader(ACCOUNT, "", TIMESTAMP, ttl=TTL, gas_price=GAS_PRICE)


def test_header_time():
    """
    Test timestamp validation.

    Verifies that the header correctly validates the timestamp type.
    """
    with pytest.raises(TypeError, match="time should be type datetime.datetime"):
        _ = DeployHeader(ACCOUNT, CHAIN_NAME, 1234,
                         ttl=TTL, gas_price=GAS_PRICE)


def test_header_ttl():
    """
    Test TTL validation.

    Verifies that the header correctly validates the TTL type.
    """
    with pytest.raises(TypeError, match="ttl should be type int"):
        _ = DeployHeader(ACCOUNT, CHAIN_NAME, TIMESTAMP,
                         ttl="30", gas_price=GAS_PRICE)


def test_header_gas_price():
    """
    Test gas price validation.

    Verifies that the header correctly validates the gas price type.
    """
    with pytest.raises(TypeError, match="gas_price should be type int"):
        _ = DeployHeader(ACCOUNT, CHAIN_NAME, TIMESTAMP,
                         ttl=TTL, gas_price="1")
