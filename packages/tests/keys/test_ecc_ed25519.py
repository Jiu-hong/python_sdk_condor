
from python_condor.keys.ecc_ed25519 import get_signature, get_key_pair_from_pem_file


key_path = "/Users/jh/mywork/python_sdk_condor/work/secret_key.pem"


def test_ed25519_get_signature():
    (pv_bytes, publickey_bytes) = get_key_pair_from_pem_file(key_path)
    hash_bytes = bytes.fromhex(
        "65987ccc48ea890d82d42389377a07b721b759168255b69df28a55af6604bd61")
    sig = get_signature(hash_bytes, pv_bytes)
    print("sig:", sig.hex())
