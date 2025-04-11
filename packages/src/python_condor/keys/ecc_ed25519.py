"""ED25519 cryptographic operations module.

This module provides functionality for ED25519 elliptic curve cryptography operations,
including key pair generation, signing, and signature verification.
"""

import base64
from typing import Tuple

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519


# Length of ED25519 private key in bytes
_PVK_LENGTH = 32
_ED25519_PREFIX = int(1).to_bytes()


def get_key_pair(private_key_bytes: bytes = None) -> Tuple[bytes, bytes]:
    """Generate an ED25519 key pair.

    Args:
        private_key_bytes: Optional seed used for deterministic key pair generation.

    Returns:
        A tuple containing (private key, public key) as 32 byte arrays.
    """
    if private_key_bytes is None:
        sk = ed25519.Ed25519PrivateKey.generate()
    else:
        sk = ed25519.Ed25519PrivateKey.from_private_bytes(private_key_bytes)

    return _get_key_pair(sk)


def get_key_pair_from_pem_file(fpath: str) -> Tuple[bytes, bytes]:
    """Generate an ED25519 key pair from a PEM file.

    Args:
        fpath: Path to the PEM file containing the private key.

    Returns:
        A tuple containing (private key, public key) as byte arrays.
    """
    pvk = get_pvk_from_pem_file(fpath)
    return get_key_pair(pvk)


def get_pvk_pem_from_bytes(pvk: bytes) -> bytes:
    """Convert a private key to PEM format.

    Args:
        pvk: Private key in bytes format.

    Returns:
        The private key in PEM format as bytes.
    """
    private_key = ed25519.Ed25519PrivateKey.from_private_bytes(pvk)
    return private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )


def get_pvk_from_pem_file(fpath: str) -> bytes:
    """Get a private key from a PEM file.

    Args:
        fpath: Path to the PEM file containing the private key.

    Returns:
        The private key as bytes.
    """
    with open(fpath, "r") as fstream:
        as_pem = fstream.readlines()

    # Decode bytes
    pvk_b64 = [i for i in as_pem if i and not i.startswith("-----")][0].strip()
    pvk = base64.b64decode(pvk_b64)

    return len(pvk) % _PVK_LENGTH == 0 and pvk[:_PVK_LENGTH] or pvk[-_PVK_LENGTH:]


def get_signature(msg: bytes, pvk: bytes) -> bytes:
    """Create an ED25519 digital signature.

    Args:
        msg: The message bytes to sign.
        pvk: The private key to sign with.

    Returns:
        The digital signature as bytes.
    """
    sk = ed25519.Ed25519PrivateKey.from_private_bytes(pvk)
    return _ED25519_PREFIX + sk.sign(msg)


def get_signature_from_pem_file(msg: bytes, fpath: str) -> bytes:
    """Create an ED25519 digital signature using a private key from a PEM file.

    Args:
        msg: The message bytes to sign.
        fpath: Path to the PEM file containing the private key.

    Returns:
        The digital signature as bytes.
    """
    return get_signature(msg, get_pvk_from_pem_file(fpath))


def is_signature_valid(msg_hash: bytes, sig: bytes, pbk_bytes: bytes) -> bool:
    """Verify an ED25519 digital signature.

    Args:
        msg_hash: The original message hash that was signed.
        sig: The digital signature to verify.
        pbk_bytes: The public key bytes to verify against.

    Returns:
        True if the signature is valid, False otherwise.
    """
    vk = ed25519.Ed25519PublicKey.from_public_bytes(pbk_bytes[1:])
    try:
        vk.verify(sig[1:], msg_hash)
    except InvalidSignature:
        return False
    return True


def _get_key_pair(sk: ed25519.Ed25519PrivateKey) -> Tuple[bytes, bytes]:
    """Generate a key pair from a signing key.

    Args:
        sk: The signing key to derive the key pair from.

    Returns:
        A tuple containing (private key, public key) as bytes.
    """
    pk = sk.public_key()
    return (
        sk.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption()
        ),
        _ED25519_PREFIX + pk.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
    )
