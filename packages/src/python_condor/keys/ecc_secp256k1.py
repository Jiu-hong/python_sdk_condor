"""ECC SECP256k1 cryptographic operations module.

This module provides functionality for SECP256k1 elliptic curve cryptography operations,
including key pair generation, signing, and signature verification.
"""

from typing import Tuple
import base64
import hashlib

import ecdsa
from ecdsa import SigningKey
from ecdsa.util import sigencode_string_canonize


# Default ECC + associated Casper specific hashing function
_CURVE = ecdsa.SECP256k1
_HASH_FN = hashlib.sha256
_SECP256k1_PREFIX = int(2).to_bytes()


def get_key_pair(private_key_bytes: bytes = None) -> Tuple[bytes, bytes]:
    """Generate an SECP256K1 key pair.

    Args:
        private_key_bytes: Optional entropy source for key pair generation.

    Returns:
        A tuple containing (private key, public key) as 32 byte arrays.
    """
    if private_key_bytes is None:
        sk = SigningKey.generate(curve=_CURVE, hashfunc=_HASH_FN)
    else:
        sk = SigningKey.from_string(
            private_key_bytes, curve=_CURVE, hashfunc=_HASH_FN)

    return _get_key_pair(sk)


def get_key_pair_from_pem_file(fpath: str) -> Tuple[bytes, bytes]:
    """Get an SECP256K1 key pair from a PEM file.

    Args:
        fpath: Path to the PEM file containing the private key.

    Returns:
        A tuple containing (private key, public key) as byte arrays.
    """
    sk = _get_signing_key_from_pem_file(fpath)
    private_key_bytes = sk.to_string()
    public_key_bytes = _SECP256k1_PREFIX + \
        sk.verifying_key.to_string("compressed")

    return (private_key_bytes, public_key_bytes)


def get_pvk_pem_from_bytes(private_key_bytes: bytes) -> bytes:
    """Convert a private key from bytes to EC PEM format.

    Args:
        private_key_bytes: The private key in bytes format.

    Returns:
        The PEM formatted EC private key as bytes.

    Raises:
        Exception: If conversion fails.
    """
    try:
        # Create ASN.1 structure for EC private key
        asn1_sequence = (
            b'\x30\x2e' +  # SEQUENCE, length 46
            b'\x02\x01\x01' +  # INTEGER (1)
            b'\x04\x20' + private_key_bytes +  # OCTET STRING (32 bytes)
            b'\xa0\x07' +  # [0]
            b'\x06\x05' +  # OBJECT IDENTIFIER
            b'\x2b\x81\x04\x00\x0a'  # secp256k1 OID
        )

        # Convert to base64
        b64_data = base64.b64encode(asn1_sequence).decode('ascii')

        # Format PEM
        pem = f"-----BEGIN EC PRIVATE KEY-----\n{b64_data}\n-----END EC PRIVATE KEY-----"
        return bytes(pem, 'utf-8')

    except Exception as e:
        raise Exception(f"Error converting bytes to PEM: {str(e)}")


def get_pvk_from_pem_file(fpath: str) -> bytes:
    """Get an SECP256K1 private key from a PEM file.

    Args:
        fpath: Path to the PEM file containing the private key.

    Returns:
        The private key as bytes.
    """
    sk = _get_signing_key_from_pem_file(fpath)
    return sk.to_string()


def get_signature(msg: bytes, sk_bytes: bytes) -> bytes:
    """Create an SECP256K1 digital signature.

    Args:
        msg: The message bytes to sign.
        sk_bytes: The private key bytes to sign with.

    Returns:
        The digital signature as bytes.
    """
    sk = SigningKey.from_string(
        sk_bytes, curve=_CURVE, hashfunc=_HASH_FN)
    return _SECP256k1_PREFIX + sk.sign_deterministic(msg, sigencode=sigencode_string_canonize)


def get_signature_from_pem_file(msg: bytes, fpath: str) -> bytes:
    """Create an SECP256K1 digital signature using a private key from a PEM file.

    Args:
        msg: The message bytes to sign.
        fpath: Path to the PEM file containing the private key.

    Returns:
        The digital signature as bytes.
    """
    sk = _get_signing_key_from_pem_file(fpath)
    return _SECP256k1_PREFIX + sk.sign_deterministic(msg, sigencode=sigencode_string_canonize)


def is_signature_valid(msg: bytes, sig: bytes, pbk_bytes: bytes) -> bool:
    """Verify an SECP256K1 digital signature.

    Args:
        msg: The original message that was signed.
        sig: The digital signature to verify.
        pbk_bytes: The public key bytes to verify against.

    Returns:
        True if the signature is valid, False otherwise.
    """
    vk = ecdsa.VerifyingKey.from_string(
        pbk_bytes[1:], hashfunc=_HASH_FN, curve=_CURVE)
    return vk.verify(sig[1:], msg)


def _get_key_pair(sk: SigningKey) -> Tuple[bytes, bytes]:
    """Generate a key pair from a signing key.

    Args:
        sk: The signing key to derive the key pair from.

    Returns:
        A tuple containing (private key, public key) as bytes.
    """
    private_key_bytes = sk.to_string()
    return private_key_bytes, _SECP256k1_PREFIX + sk.verifying_key.to_string("compressed")


def _get_signing_key_from_pem_file(fpath: str) -> SigningKey:
    """Read a signing key from a PEM file.

    Args:
        fpath: Path to the PEM file containing the private key.

    Returns:
        The SigningKey object.

    Raises:
        Exception: If the file cannot be read or the key is invalid.
    """
    with open(fpath) as fstream:
        return SigningKey.from_pem(fstream.read(), _HASH_FN)
