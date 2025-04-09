from ecdsa import SigningKey
import hashlib


def get_key_pair_from_pem_file(fpath: str):
    """Returns an SECP256K1 key pair mapped from a PEM file representation of a private key.

    :param fpath: PEM file path.
    :returns : 2 member tuple: (private key, public key)

    """
    # sk = _get_signing_key_from_pem_file(fpath)

    # return _get_key_pair(sk)
    with open(fpath) as f:
        sk = SigningKey.from_pem(f.read(), hashlib.sha256)
    public_key = sk.verifying_key.to_string("compressed")
    # sk.verifying_key.to_string("compressed")
    print("sk:", sk.to_string().hex())
    print("public_key:", public_key)
    return (sk, public_key)


path = "/Users/jh/mywork/python_sdk_condor/work/secret_key2.pem"
get_key_pair_from_pem_file(path)
