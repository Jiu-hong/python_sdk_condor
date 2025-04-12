"""Tests for CL (Casper) public key functionality.

This module contains test cases for the CLPublicKey class, which handles public keys
in the Casper network. It tests both ED25519 and SECP256K1 public key formats,
including:
- Serialization
- Value retrieval
- CL value representation
- JSON representation
- Account hash generation
- Format validation
"""

import pytest

from python_condor import CLPublicKey

# Test data
ED25519_PUBLIC_KEY = "0119bf44096984cdfe8541bac167dc3b96c85086aa30b6b6cb0c5c38ad703166e1"
SECP256K1_PUBLIC_KEY = "020233e54d818925bad633b837e0cece45f4e3d4498d0da04957047d3abd378679c7"
INVALID_PUBLIC_KEY = "123456"

# Expected values
ED25519_ACCOUNT_HASH = "290ee54c1c974a8f90e3178eba65405b2d7af8392a65c629c145d0a0ee8bb1dd"
SECP256K1_ACCOUNT_HASH = "5978e0e5aea2d9b13f5af353fb333b7084f950c0be0655ea93298d2b57a973f7"


def test_ed25519_public_key_serialization():
    """Test serialization of ED25519 public key."""
    public_key = CLPublicKey(ED25519_PUBLIC_KEY)
    result = public_key.serialize().hex()
    assert result == ED25519_PUBLIC_KEY


def test_ed25519_public_key_value():
    """Test value retrieval of ED25519 public key."""
    public_key = CLPublicKey(ED25519_PUBLIC_KEY)
    result = public_key.value()
    assert result == ED25519_PUBLIC_KEY


def test_ed25519_public_key_cl_value():
    """Test CL value representation of ED25519 public key."""
    public_key = CLPublicKey(ED25519_PUBLIC_KEY)
    result = public_key.cl_value()
    assert result == "210000000119bf44096984cdfe8541bac167dc3b96c85086aa30b6b6cb0c5c38ad703166e116"


def test_ed25519_public_key_to_json():
    """Test JSON representation of ED25519 public key."""
    public_key = CLPublicKey(ED25519_PUBLIC_KEY)
    result = public_key.to_json()
    assert result == "PublicKey"


def test_ed25519_public_key_account_hash():
    """Test account hash generation for ED25519 public key."""
    public_key = CLPublicKey(ED25519_PUBLIC_KEY)
    result = public_key.get_account_hash()
    assert result == ED25519_ACCOUNT_HASH


def test_secp256k1_public_key_account_hash():
    """Test account hash generation for SECP256K1 public key."""
    public_key = CLPublicKey(SECP256K1_PUBLIC_KEY)
    result = public_key.get_account_hash()
    assert result == SECP256K1_ACCOUNT_HASH


def test_invalid_public_key_format():
    """Test public key format validation."""
    with pytest.raises(ValueError, match=r"Public key should be 01xxx\(64 length\) or 02xxx\(66 length\)"):
        _ = CLPublicKey(INVALID_PUBLIC_KEY)
