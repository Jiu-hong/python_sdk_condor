"""Tests for ECC (Elliptic Curve Cryptography) functionality.

This module contains test cases for both ED25519 and SECP256K1 key algorithms,
covering key pair generation, PEM file operations, signature creation and validation.
Each test verifies a specific aspect of the cryptographic operations supported by
the python_condor library.
"""

from python_condor import (
    KeyAlgorithm,
    get_pvk_from_pem_file,
    get_pvk_pem_file_from_bytes,
    get_pvk_pem_from_hex_string,
    get_key_pair_from_hex_string,
    get_key_pair_from_bytes,
    get_pvk_pem_from_bytes,
    is_signature_valid,
    get_signature_from_pem_file,
    get_key_pair,
    get_signature,
    get_key_pair_from_pem_file
)

# Test data for ED25519
ED25519_TEST_KEY_PATH = "/Users/jh/mywork/python_sdk_condor/work/secret_key.pem"
ED25519_TEST_HASH = bytes.fromhex(
    "a7fbf607ec1d8763970356f1a93def392ff9c821749935599cbcddf662db9a22")
ED25519_TEST_SIGNATURE = bytes.fromhex(
    "01ad201f94332b9adffcfec8a8532c893f48e989bc8aa99d262c6982a94cd21db11649840407cdb12cb29519a2f434b7c30f0ff032231a402e9ad5915435646109"
)
ED25519_PRIVATE_KEY = "dd92fc760b6dce746eca6b29a25909eb8c8baadc4022c2eb6d12112a1933a26d"
ED25519_PUBLIC_KEY = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"

# Test data for SECP256K1
SECP256K1_TEST_KEY_PATH = "/Users/jh/mywork/python_sdk_condor/work/secret_key2.pem"
SECP256K1_TEST_HASH = bytes.fromhex(
    "dda8b363afd37be8bb770437a15f55ed8796eb32ae5332700d21e94dfb64aac7")
SECP256K1_TEST_SIGNATURE = bytes.fromhex(
    "025321beb8c8ffabe5c2b884ec978b5e64eba99d61f4e5c11f4a12bdb497cdee332bbbab186eca62ec3019309954353f4ab5cea1f3137c0b537e2abadcd1e06e92"
)
SECP256K1_PRIVATE_KEY = "85f45a4fe1f86bc4f11900465e2a669f89e04c758631bf6428bb995a2fdfbb5e"
SECP256K1_PUBLIC_KEY = "0203b3eb6ae40e21a9436b956aa8a3af5b7336340cfc6ec035db7aec6a4ff1cda22f"

# === ED25519 Tests ===


def test_get_key_pair():
    """Test generation of a new ED25519 key pair."""
    private_key, public_key = get_key_pair(KeyAlgorithm.ED25519)
    print("private_key:", private_key.hex())
    print("public_key:", public_key.hex())


def test_get_key_pair_from_bytes():
    """Test creating an ED25519 key pair from private key bytes."""
    test_private_key = bytes.fromhex(
        "4a2a3b6b7357cc7aff1bd080c72dfef2a3f37ed9f1bdadbf2369fc7fd4906323")
    expected_public_key = "014faf586a6236c18cdbbfdee699d965ff2e5a918ac3bff0676a700d6f326c32fb"

    private_key, public_key = get_key_pair_from_bytes(
        test_private_key, KeyAlgorithm.ED25519)
    assert public_key.hex() == expected_public_key


def test_get_key_pair_from_hex_string():
    """Test creating an ED25519 key pair from a hex string private key."""
    test_private_key = "4a2a3b6b7357cc7aff1bd080c72dfef2a3f37ed9f1bdadbf2369fc7fd4906323"
    expected_public_key = "014faf586a6236c18cdbbfdee699d965ff2e5a918ac3bff0676a700d6f326c32fb"

    private_key, public_key = get_key_pair_from_hex_string(
        test_private_key, KeyAlgorithm.ED25519)
    assert public_key.hex() == expected_public_key


def test_get_key_pair_from_pem_file():
    """Test loading an ED25519 key pair from a PEM file."""
    private_key, public_key = get_key_pair_from_pem_file(
        ED25519_TEST_KEY_PATH, KeyAlgorithm.ED25519)
    assert private_key.hex() == ED25519_PRIVATE_KEY
    assert public_key.hex() == ED25519_PUBLIC_KEY


def test_get_pvk_pem_from_bytes():
    """Test creating a PEM file content from ED25519 private key bytes."""
    pem_file = get_pvk_pem_from_bytes(bytes.fromhex(
        ED25519_PRIVATE_KEY), KeyAlgorithm.ED25519)
    with open(ED25519_TEST_KEY_PATH, "rb") as fstream:
        as_pem = fstream.read()
    assert as_pem == pem_file[:-1]


def test_get_pvk_pem_from_hex_string():
    """Test creating a PEM file content from ED25519 private key hex string."""
    pem_file = get_pvk_pem_from_hex_string(
        ED25519_PRIVATE_KEY, KeyAlgorithm.ED25519)
    with open(ED25519_TEST_KEY_PATH, "rb") as fstream:
        as_pem = fstream.read()
    assert as_pem == pem_file[:-1]


def test_get_pvk_pem_file_from_bytes():
    """Test creating and saving an ED25519 PEM file from private key bytes."""
    name = get_pvk_pem_file_from_bytes(bytes.fromhex(
        ED25519_PRIVATE_KEY), KeyAlgorithm.ED25519)
    private_key, public_key = get_key_pair_from_pem_file(
        name, KeyAlgorithm.ED25519)
    assert private_key.hex() == ED25519_PRIVATE_KEY
    assert public_key.hex() == ED25519_PUBLIC_KEY


def test_get_signature():
    """Test creating an ED25519 signature using a private key."""
    private_key, public_key = get_key_pair_from_pem_file(
        ED25519_TEST_KEY_PATH, KeyAlgorithm.ED25519)
    sig = get_signature(ED25519_TEST_HASH, KeyAlgorithm.ED25519, private_key)
    assert sig == ED25519_TEST_SIGNATURE


def test_get_signature_from_pem_file():
    """Test creating an ED25519 signature using a PEM file."""
    sig = get_signature_from_pem_file(
        ED25519_TEST_HASH, ED25519_TEST_KEY_PATH, KeyAlgorithm.ED25519)
    assert sig == ED25519_TEST_SIGNATURE


def test_is_signature_valid():
    """Test validating an ED25519 signature."""
    _private_key, public_key = get_key_pair_from_pem_file(
        ED25519_TEST_KEY_PATH, KeyAlgorithm.ED25519)
    assert is_signature_valid(
        ED25519_TEST_HASH, KeyAlgorithm.ED25519, ED25519_TEST_SIGNATURE, public_key)


def test_get_pvk_from_pem_file():
    """Test extracting an ED25519 private key from a PEM file."""
    private_key = get_pvk_from_pem_file(ED25519_TEST_KEY_PATH)
    assert private_key == bytes.fromhex(ED25519_PRIVATE_KEY)


# === SECP256K1 Tests ===

def test_get_key_pair_secp256k1():
    """Test generation of a new SECP256K1 key pair."""
    private_key, public_key = get_key_pair(KeyAlgorithm.SECP256K1)
    print("private_key:", private_key.hex())
    print("public_key:", public_key.hex())


def test_get_key_pair_from_bytes_secp256k1():
    """Test creating a SECP256K1 key pair from private key bytes."""
    test_private_key = bytes.fromhex(
        "2fee2f3400be052335a53dfac33b7f94b5329727e3ba3b7ebb726820ff039a32")
    expected_public_key = "0202c8025b9d253d0bf5f48a96e8fdcecce3fd03731e7cdc47c6c7d297e75bc3ab11"

    private_key, public_key = get_key_pair_from_bytes(
        test_private_key, KeyAlgorithm.SECP256K1)
    assert public_key.hex() == expected_public_key


def test_get_key_pair_from_hex_string_secp256k1():
    """Test creating a SECP256K1 key pair from a hex string private key."""
    test_private_key = "2fee2f3400be052335a53dfac33b7f94b5329727e3ba3b7ebb726820ff039a32"
    expected_public_key = "0202c8025b9d253d0bf5f48a96e8fdcecce3fd03731e7cdc47c6c7d297e75bc3ab11"

    private_key, public_key = get_key_pair_from_hex_string(
        test_private_key, KeyAlgorithm.SECP256K1)
    assert public_key.hex() == expected_public_key


def test_get_key_pair_from_pem_file_secp256k1():
    """Test loading a SECP256K1 key pair from a PEM file."""
    private_key, public_key = get_key_pair_from_pem_file(
        SECP256K1_TEST_KEY_PATH, KeyAlgorithm.SECP256K1)
    assert private_key.hex() == SECP256K1_PRIVATE_KEY
    assert public_key.hex() == SECP256K1_PUBLIC_KEY


def test_get_pvk_pem_from_bytes_secp256k1():
    """Test creating a PEM file content from SECP256K1 private key bytes."""
    pem_file = get_pvk_pem_from_bytes(bytes.fromhex(
        SECP256K1_PRIVATE_KEY), KeyAlgorithm.SECP256K1)
    with open(SECP256K1_TEST_KEY_PATH, "rb") as fstream:
        as_pem = fstream.read()
    assert as_pem == pem_file


def test_get_pvk_pem_from_hex_string_secp256k1():
    """Test creating a PEM file content from SECP256K1 private key hex string."""
    pem_file = get_pvk_pem_from_hex_string(
        SECP256K1_PRIVATE_KEY, KeyAlgorithm.SECP256K1)
    with open(SECP256K1_TEST_KEY_PATH, "rb") as fstream:
        as_pem = fstream.read()
    assert as_pem == pem_file


def test_get_pvk_pem_file_from_bytes_secp256k1():
    """Test creating and saving a SECP256K1 PEM file from private key bytes."""
    name = get_pvk_pem_file_from_bytes(bytes.fromhex(
        SECP256K1_PRIVATE_KEY), KeyAlgorithm.SECP256K1)
    private_key, public_key = get_key_pair_from_pem_file(
        name, KeyAlgorithm.SECP256K1)
    assert private_key.hex() == SECP256K1_PRIVATE_KEY
    assert public_key.hex() == SECP256K1_PUBLIC_KEY


def test_get_signature_secp256k1():
    """Test creating a SECP256K1 signature using a private key."""
    private_key, public_key = get_key_pair_from_pem_file(
        SECP256K1_TEST_KEY_PATH, KeyAlgorithm.SECP256K1)
    sig = get_signature(SECP256K1_TEST_HASH,
                        KeyAlgorithm.SECP256K1, private_key)
    assert sig == SECP256K1_TEST_SIGNATURE


def test_get_signature_from_pem_file_secp256k1():
    """Test creating a SECP256K1 signature using a PEM file."""
    sig = get_signature_from_pem_file(
        SECP256K1_TEST_HASH, SECP256K1_TEST_KEY_PATH, KeyAlgorithm.SECP256K1)
    assert sig == SECP256K1_TEST_SIGNATURE


def test_is_signature_valid_secp256k1():
    """Test validating a SECP256K1 signature."""
    _private_key, public_key = get_key_pair_from_pem_file(
        SECP256K1_TEST_KEY_PATH, KeyAlgorithm.SECP256K1)
    assert is_signature_valid(
        SECP256K1_TEST_HASH, KeyAlgorithm.SECP256K1, SECP256K1_TEST_SIGNATURE, public_key)


def test_get_pvk_from_pem_file_secp256k1():
    """Test extracting a SECP256K1 private key from a PEM file."""
    private_key = get_pvk_from_pem_file(
        SECP256K1_TEST_KEY_PATH, KeyAlgorithm.SECP256K1)
    assert private_key == bytes.fromhex(SECP256K1_PRIVATE_KEY)
