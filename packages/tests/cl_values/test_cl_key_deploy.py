"""Tests for CL (Casper) deploy key functionality.

This module contains test cases for the CLKey class when handling deploy keys,
which represent deploy hashes in the Casper network. It tests:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Format validation
"""

import pytest
from python_condor import CLKey

# === Test Data ===
# Valid deploy key for testing
VALID_DEPLOY_KEY = "deploy-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"

# Invalid deploy key for testing validation
INVALID_DEPLOY_KEY = "deploy-1234"

# === Expected Values ===
EXPECTED = {
    "serialized": "042a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a",
    "cl_value": "21000000042a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a0b",
    "json": "Key"
}

# === Valid Deploy Key Tests ===


def test_deploy_key_serialization():
    """Test serialization of deploy key."""
    deploy_key = CLKey(VALID_DEPLOY_KEY)
    result = deploy_key.serialize().hex()
    assert result == EXPECTED["serialized"]


def test_deploy_key_value():
    """Test value retrieval of deploy key."""
    deploy_key = CLKey(VALID_DEPLOY_KEY)
    result = deploy_key.value()
    assert result == VALID_DEPLOY_KEY


def test_deploy_key_cl_value():
    """Test CL value representation of deploy key."""
    deploy_key = CLKey(VALID_DEPLOY_KEY)
    result = deploy_key.cl_value()
    assert result == EXPECTED["cl_value"]


def test_deploy_key_to_json():
    """Test JSON representation of deploy key."""
    deploy_key = CLKey(VALID_DEPLOY_KEY)
    result = deploy_key.to_json()
    assert result == EXPECTED["json"]


# === Invalid Deploy Key Tests ===
def test_invalid_deploy_key_format():
    """Test deploy key format validation."""
    error_msg = "value should be 64 length only containing alphabet and number"
    with pytest.raises(ValueError, match=error_msg):
        _ = CLKey(INVALID_DEPLOY_KEY)
