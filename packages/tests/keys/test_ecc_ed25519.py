from python_condor.keys.ecc_ed25519 import get_pvk_from_pem_file, get_pvk_pem_from_bytes, is_signature_valid, get_key_pair, get_signature_from_pem_file, get_signature, get_key_pair_from_pem_file


fpath = "/Users/jh/mywork/python_sdk_condor/work/secret_key.pem"
hash_bytes = bytes.fromhex(
    "a7fbf607ec1d8763970356f1a93def392ff9c821749935599cbcddf662db9a22")
sig_bytes = bytes.fromhex(
    "01ad201f94332b9adffcfec8a8532c893f48e989bc8aa99d262c6982a94cd21db11649840407cdb12cb29519a2f434b7c30f0ff032231a402e9ad5915435646109")
private_key_hex = "dd92fc760b6dce746eca6b29a25909eb8c8baadc4022c2eb6d12112a1933a26d"
public_key_hex = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"


def test_get_key_pair_from_pem_file():
    private_key, public_key = get_key_pair_from_pem_file(fpath)
    assert private_key.hex(
    ) == private_key_hex
    assert public_key.hex() == public_key_hex


def test_get_signature():
    private_key, _public_key = get_key_pair_from_pem_file(fpath)
    sig = get_signature(hash_bytes, private_key)
    assert sig == sig_bytes


def test_get_signature_from_pem_file():
    sig = get_signature_from_pem_file(hash_bytes, fpath)
    assert sig == sig_bytes


def test_get_key_pair():
    private_key_bytes = bytes.fromhex(
        private_key_hex)
    private_key, _public_key = get_key_pair(private_key_bytes)
    sig = get_signature(hash_bytes, private_key)
    assert sig == sig_bytes


def test_is_signature_valid():
    _private_key, public_key = get_key_pair_from_pem_file(fpath)
    assert is_signature_valid(hash_bytes, sig_bytes, public_key)


def test_get_pvk_pem_from_bytes():
    pem_file = get_pvk_pem_from_bytes(bytes.fromhex(private_key_hex))

    with open(fpath, "rb") as fstream:
        as_pem = fstream.read()

    assert as_pem == pem_file[:-1]


def test_get_pvk_from_pem_file():
    private_key = get_pvk_from_pem_file(fpath)
    assert private_key == bytes.fromhex(private_key_hex)
