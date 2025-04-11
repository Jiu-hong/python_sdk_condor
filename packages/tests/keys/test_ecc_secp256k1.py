from python_condor.keys.ecc_secp256k1 import get_pvk_pem_from_bytes, is_signature_valid, get_signature_from_pem_file, get_key_pair, get_signature, get_key_pair_from_pem_file


fpath = "/Users/jh/mywork/python_sdk_condor/work/secret_key2.pem"
hash_bytes = bytes.fromhex(
    "dda8b363afd37be8bb770437a15f55ed8796eb32ae5332700d21e94dfb64aac7")
sig_bytes = bytes.fromhex(
    "025321beb8c8ffabe5c2b884ec978b5e64eba99d61f4e5c11f4a12bdb497cdee332bbbab186eca62ec3019309954353f4ab5cea1f3137c0b537e2abadcd1e06e92")
private_key_hex = "85f45a4fe1f86bc4f11900465e2a669f89e04c758631bf6428bb995a2fdfbb5e"
public_key_hex = "0203b3eb6ae40e21a9436b956aa8a3af5b7336340cfc6ec035db7aec6a4ff1cda22f"


def test_get_key_pair_from_pem_file():
    private_key, public_key = get_key_pair_from_pem_file(fpath)

    assert private_key.hex() == private_key_hex
    assert public_key.hex() == public_key_hex


def test_get_signature():
    private_key, _public_key = get_key_pair_from_pem_file(fpath)
    sig = get_signature(hash_bytes, private_key)
    assert sig == sig_bytes


def test_get_signature_from_pem_file():
    sig = get_signature_from_pem_file(hash_bytes, fpath)
    assert sig == sig_bytes


def test_get_key_pair():
    private_key_bytes = bytes.fromhex(private_key_hex)
    private_key, _public_key = get_key_pair(private_key_bytes)
    assert private_key == private_key_bytes
    sig = get_signature(hash_bytes, private_key)
    assert sig == sig_bytes


def test_is_signature_valid():
    _private_key, public_key = get_key_pair_from_pem_file(fpath)
    assert is_signature_valid(hash_bytes, sig_bytes, public_key)


# todo
def test_get_pvk_pem_from_bytes():
    private_key, _public_key = get_key_pair_from_pem_file(fpath)

    a = get_pvk_pem_from_bytes(private_key)
    print("a:", a)
