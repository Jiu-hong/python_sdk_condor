"""ECC cryptographic operations package.

This package provides a unified interface for different ECC algorithms (ED25519 and SECP256K1),
including key pair generation, signing, and signature verification.
"""

from .ecc import (
    KeyAlgorithm,
    get_key_pair,
    get_key_pair_from_bytes,
    get_key_pair_from_hex_string,
    get_key_pair_from_pem_file,
    get_pvk_from_pem_file,
    get_pvk_pem_file_from_bytes,
    get_pvk_pem_from_bytes,
    get_pvk_pem_from_hex_string,
    get_signature,
    get_signature_from_pem_file,
    is_signature_valid,
)
