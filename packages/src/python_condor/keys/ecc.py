"""ECC cryptographic operations module.

This module provides a unified interface for different ECC algorithms (ED25519 and SECP256K1),
including key pair generation, signing, and signature verification.
"""

import base64
import enum
import tempfile
from typing import Tuple

from ..keys import ecc_ed25519 as ed25519
from ..keys import ecc_secp256k1 as secp256k1


class KeyAlgorithm(enum.Enum):
    """Enumeration over set of supported key algorithms."""
    ED25519 = 1
    SECP256K1 = 2


# Map: Key algo Type -> Key algo Implementation
ALGOS = {
    KeyAlgorithm.ED25519: ed25519,
    KeyAlgorithm.SECP256K1: secp256k1,
}

# Default key algorithm
DEFAULT_KEY_ALGO = KeyAlgorithm.ED25519


def get_key_pair(algo: KeyAlgorithm = DEFAULT_KEY_ALGO) -> Tuple[bytes, bytes]:
    """Generate an ECC key pair.

    Args:
        algo: Type of ECC algorithm to use for key pair generation.

    Returns:
        A tuple containing (private key, public key) as 32 byte arrays.
    """
    pvk, pbk = ALGOS[algo].get_key_pair()
    return (pvk, pbk)


def get_key_pair_from_bytes(
    pvk: bytes,
    algo: KeyAlgorithm = DEFAULT_KEY_ALGO
) -> Tuple[bytes, bytes]:
    """Generate a key pair from a byte array representation of a private key.

    Args:
        pvk: A private key in bytes format.
        algo: Type of ECC algorithm used to generate the private key.

    Returns:
        A tuple containing (private key, public key) as byte arrays.
    """
    pvk, pbk = ALGOS[algo].get_key_pair(pvk)
    return (pvk, pbk)


def get_key_pair_from_base64(
    pvk_b64: str,
    algo: KeyAlgorithm = DEFAULT_KEY_ALGO
) -> Tuple[str, bytes]:
    """Generate a key pair from a base64 representation of a private key.

    Args:
        pvk_b64: Base64 encoded private key.
        algo: Type of ECC algorithm used to generate the private key.

    Returns:
        A tuple containing (private key, public key).
    """
    return get_key_pair_from_bytes(base64.b64decode(pvk_b64), algo)


def get_key_pair_from_hex_string(
    pvk_hex: str,
    algo: KeyAlgorithm = DEFAULT_KEY_ALGO
) -> Tuple[bytes, bytes]:
    """Generate a key pair from a hexadecimal string encoded private key.

    Args:
        pvk_hex: Hexadecimal string encoded private key.
        algo: Type of ECC algorithm used to generate the private key.

    Returns:
        A tuple containing (private key, public key) as byte arrays.
    """
    return get_key_pair_from_bytes(bytes.fromhex(pvk_hex), algo)


def get_key_pair_from_pem_file(
    fpath: str,
    algo: KeyAlgorithm = DEFAULT_KEY_ALGO
) -> Tuple[bytes, bytes]:
    """Generate a key pair from a PEM file.

    Args:
        fpath: Path to the PEM file containing the private key.
        algo: Type of ECC algorithm used to generate the private key.

    Returns:
        A tuple containing (private key, public key) as byte arrays.
    """
    pvk, pbk = ALGOS[algo].get_key_pair_from_pem_file(fpath)
    return (pvk, pbk)


def get_pvk_pem_from_bytes(
    pvk: bytes,
    algo: KeyAlgorithm = DEFAULT_KEY_ALGO
) -> bytes:
    """Convert a private key to PEM format.

    Args:
        pvk: Private key in bytes format.
        algo: Type of ECC algorithm used to generate the private key.

    Returns:
        The private key in PEM format as bytes.
    """
    return ALGOS[algo].get_pvk_pem_from_bytes(pvk)


def get_pvk_pem_from_hex_string(
    pvk: str,
    algo: KeyAlgorithm = DEFAULT_KEY_ALGO
) -> bytes:
    """Convert a hexadecimal string encoded private key to PEM format.

    Args:
        pvk: Private key as a hexadecimal string.
        algo: Type of ECC algorithm used to generate the private key.

    Returns:
        The private key in PEM format as bytes.
    """
    return ALGOS[algo].get_pvk_pem_from_bytes(bytes.fromhex(pvk))


def get_pvk_pem_file_from_bytes(
    pvk: bytes,
    algo: KeyAlgorithm = DEFAULT_KEY_ALGO
) -> bytes:
    """Create a temporary file containing a private key in PEM format.

    Args:
        pvk: Private key in bytes format.
        algo: Type of ECC algorithm used to generate the private key.

    Returns:
        Path to the temporary file containing the private key in PEM format.
    """
    with tempfile.NamedTemporaryFile("wb", delete=False) as temp_file:
        with open(temp_file.name, "wb") as fstream:
            fstream.write(get_pvk_pem_from_bytes(pvk, algo))
        return temp_file.name


def get_signature(
    msg_hash: bytes,
    algo: KeyAlgorithm,
    pvk: bytes,
) -> bytes:
    """Create a digital signature for a message hash.

    Args:
        msg_hash: Message hash to be signed.
        algo: Type of ECC algorithm to use for signing.
        pvk: Private key to sign with.

    Returns:
        The digital signature as bytes.
    """
    return ALGOS[algo].get_signature(msg_hash, pvk)


def get_signature_from_pem_file(
    msg_hash: bytes,
    fpath: str,
    algo: KeyAlgorithm = DEFAULT_KEY_ALGO
) -> bytes:
    """Create a digital signature using a private key from a PEM file.

    Args:
        msg_hash: Message hash to be signed.
        fpath: Path to the PEM file containing the private key.
        algo: Type of ECC algorithm used to generate the private key.

    Returns:
        The digital signature as bytes.
    """
    pvk, _ = get_key_pair_from_pem_file(fpath, algo)
    return get_signature(msg_hash, algo, pvk)


def is_signature_valid(
    msg_hash: bytes,
    algo: KeyAlgorithm,
    sig: bytes,
    vk: bytes
) -> bool:
    """Verify a digital signature.

    Args:
        msg_hash: The original message hash that was signed.
        algo: Type of ECC algorithm used to generate the signature.
        sig: The digital signature to verify.
        vk: The verifying key (public key).

    Returns:
        True if the signature is valid, False otherwise.
    """
    return ALGOS[algo].is_signature_valid(msg_hash, sig, vk)


def get_pvk_from_pem_file(
    fpath: str,
    algo: KeyAlgorithm = DEFAULT_KEY_ALGO
) -> bytes:
    """Get a private key from a PEM file.

    Args:
        fpath: Path to the PEM file containing the private key.
        algo: Type of ECC algorithm used to generate the private key.

    Returns:
        The private key as bytes.
    """
    pvk, _ = ALGOS[algo].get_key_pair_from_pem_file(fpath)
    return pvk


# Synonym
get_key_pair_from_seed = get_key_pair_from_bytes
