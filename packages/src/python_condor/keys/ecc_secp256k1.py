import ecdsa
import hashlib
import typing
from ecdsa.util import sigencode_string_canonize
from ecdsa import SigningKey

# Default ECC + associated Casper specific hashing function.
_CURVE = ecdsa.SECP256k1
_HASH_FN = hashlib.sha256

_SECP256k1_PREFIX = int(2).to_bytes()


# correct
def get_key_pair(private_key_bytes: bytes = None) -> typing.Tuple[bytes, bytes]:
    """Returns an SECP256K1 key pair, each key is a 32 byte array.

    :param private_key_bytes: Entropy source to be used when geenrating key pair.
    :returns : 2 member tuple: (private key, public key)

    """
    if private_key_bytes is None:
        sk = SigningKey.generate(curve=_CURVE, hashfunc=_HASH_FN)
    else:
        sk = SigningKey.from_string(
            private_key_bytes, curve=_CURVE, hashfunc=_HASH_FN)

    return _get_key_pair(sk)


# correct
def get_key_pair_from_pem_file(fpath: str) -> typing.Tuple[bytes, bytes]:
    """Returns an SECP256K1 key pair mapped from a PEM file representation of a private key.

    :param fpath: PEM file path.
    :returns : 2 member tuple: (private key, public key)

    """
    sk = _get_signing_key_from_pem_file(fpath)
    private_key_bytes = sk.to_string()

    public_key_bytes = _SECP256k1_PREFIX + \
        sk.verifying_key.to_string("compressed")
    return (private_key_bytes, public_key_bytes)


# incorrect
def get_pvk_pem_from_bytes(pvk: bytes):
    """Returns SECP256K1 private key (pem) from bytes.

    :param pvk: A private key derived from a generated key pair.
    :returns: PEM represenation of signing key.

    """
    sk = SigningKey.from_string(pvk, curve=_CURVE)

    return sk.to_pem()


# correct
def get_signature(msg: bytes, sk_bytes: bytes) -> bytes:
    """Returns an SECP256K1 digital signature of data signed from a private key PEM file.

    :param msg: A bunch of bytes to be signed.
    :param pvk: A private key derived from a generated key pair.
    :returns: A digital signature.

    """
    sk = SigningKey.from_string(
        sk_bytes, curve=ecdsa.SECP256k1, hashfunc=hashlib.sha256)
    # return sk.sign_deterministic(msg, hashfunc=_HASH_FN)
    return _SECP256k1_PREFIX + sk.sign_deterministic(msg, sigencode=sigencode_string_canonize)


# correct
def get_signature_from_pem_file(msg: bytes, fpath: str) -> bytes:
    """Returns an SECP256K1 digital signature of data signed from a private key PEM file.

    :param msg: A bunch of bytes to be signed.
    :param fpath: PEM file path.
    :returns: A digital signature.

    """
    sk = _get_signing_key_from_pem_file(fpath)

    # return sk.sign_deterministic(msg, hashfunc=_HASH_FN)
    return _SECP256k1_PREFIX + sk.sign_deterministic(msg, sigencode=sigencode_string_canonize)


# correct
def is_signature_valid(msg: bytes, sig: bytes, pbk_bytes: bytes) -> bool:
    """Returns a flag indicating whether a signature was signed by a signing key
       associated with passed verification key.

    :param msg: A message that has apparently been signed.
    :param sig: A digital signature.
    :param pbk: Public key counterpart to generated private key.
    :returns: A flag indicating whether a signature was indeed signed by the signing key.

    """
    # vk = ecdsa.VerifyingKey.from_string(pbk_bytes, curve=_CURVE)
    vk = ecdsa.VerifyingKey.from_string(
        pbk_bytes[1:], hashfunc=_HASH_FN, curve=_CURVE)

    # return vk.verify(sig, msg, hashfunc=_HASH_FN)
    return vk.verify(sig[1:], msg)


# correct
def _get_key_pair(sk: SigningKey) -> typing.Tuple[bytes, bytes]:
    """Returns key pair from a signing key.

    """
    private_key_bytes = sk.to_string()
    return private_key_bytes, _SECP256k1_PREFIX + sk.verifying_key.to_string("compressed")


# correct
def _get_signing_key_from_pem_file(fpath: str) -> SigningKey:
    """Returns a signing key mapped from a PEM file representation of a private key.

    """
    with open(fpath) as fstream:
        return SigningKey.from_pem(fstream.read(), _HASH_FN)
