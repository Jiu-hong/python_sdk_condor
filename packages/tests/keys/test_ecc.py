from python_condor.keys.ecc import KeyAlgorithm, get_pvk_pem_file_from_bytes, get_pvk_pem_from_hex_string, get_key_pair_from_hex_string, get_key_pair_from_bytes, get_pvk_pem_from_bytes, is_signature_valid, get_signature_from_pem_file, get_key_pair, get_signature, get_key_pair_from_pem_file


f1path = "/Users/jh/mywork/python_sdk_condor/work/secret_key.pem"
hash_bytes_1 = bytes.fromhex(
    "a7fbf607ec1d8763970356f1a93def392ff9c821749935599cbcddf662db9a22")
sig_bytes_1 = bytes.fromhex(
    "01ad201f94332b9adffcfec8a8532c893f48e989bc8aa99d262c6982a94cd21db11649840407cdb12cb29519a2f434b7c30f0ff032231a402e9ad5915435646109")
private_key_hex_1 = "dd92fc760b6dce746eca6b29a25909eb8c8baadc4022c2eb6d12112a1933a26d"
public_key_hex_1 = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
public_key_hex_2 = "0203b3eb6ae40e21a9436b956aa8a3af5b7336340cfc6ec035db7aec6a4ff1cda22f"


f2path = "/Users/jh/mywork/python_sdk_condor/work/secret_key2.pem"
hash_bytes_2 = bytes.fromhex(
    "dda8b363afd37be8bb770437a15f55ed8796eb32ae5332700d21e94dfb64aac7")
sig_bytes_2 = bytes.fromhex(
    "025321beb8c8ffabe5c2b884ec978b5e64eba99d61f4e5c11f4a12bdb497cdee332bbbab186eca62ec3019309954353f4ab5cea1f3137c0b537e2abadcd1e06e92")
private_key_hex_2 = "85f45a4fe1f86bc4f11900465e2a669f89e04c758631bf6428bb995a2fdfbb5e"


# === ed25519
def test_get_key_pair():
    private_key, public_key = get_key_pair(KeyAlgorithm.ED25519)
    print("private_key:", private_key.hex())
    print("public_key:", public_key.hex())


def test_get_key_pair_from_bytes():
    private_key, public_key = get_key_pair_from_bytes(
        bytes.fromhex("4a2a3b6b7357cc7aff1bd080c72dfef2a3f37ed9f1bdadbf2369fc7fd4906323"), KeyAlgorithm.ED25519)
    assert public_key.hex() == "014faf586a6236c18cdbbfdee699d965ff2e5a918ac3bff0676a700d6f326c32fb"


def test_get_key_pair_from_base64():
    # get_key_pair_from_base64()
    # todo
    pass


def test_get_key_pair_from_hex_string():
    private_key, public_key = get_key_pair_from_hex_string(
        "4a2a3b6b7357cc7aff1bd080c72dfef2a3f37ed9f1bdadbf2369fc7fd4906323", KeyAlgorithm.ED25519)
    assert public_key.hex() == "014faf586a6236c18cdbbfdee699d965ff2e5a918ac3bff0676a700d6f326c32fb"


def test_get_key_pair_from_pem_file():
    private_key, public_key = get_key_pair_from_pem_file(
        f1path, KeyAlgorithm.ED25519)
    assert private_key.hex(
    ) == private_key_hex_1
    assert public_key.hex() == public_key_hex_1


def test_get_pvk_pem_from_bytes():
    pem_file = get_pvk_pem_from_bytes(bytes.fromhex(
        private_key_hex_1), KeyAlgorithm.ED25519)
    with open(f1path, "rb") as fstream:
        as_pem = fstream.read()

    assert as_pem == pem_file[:-1]


def test_get_pvk_pem_from_hex_string():
    pem_file = get_pvk_pem_from_hex_string(
        private_key_hex_1, KeyAlgorithm.ED25519)
    with open(f1path, "rb") as fstream:
        as_pem = fstream.read()

    assert as_pem == pem_file[:-1]


def test_get_pvk_pem_file_from_bytes():
    name = get_pvk_pem_file_from_bytes(bytes.fromhex(
        private_key_hex_1), KeyAlgorithm.ED25519)
    # print("name:", name)

    private_key, public_key = get_key_pair_from_pem_file(
        name, KeyAlgorithm.ED25519)
    assert private_key.hex(
    ) == private_key_hex_1
    assert public_key.hex() == public_key_hex_1


def test_get_signature():
    private_key, public_key = get_key_pair_from_pem_file(
        f1path, KeyAlgorithm.ED25519)
    sig = get_signature(hash_bytes_1, KeyAlgorithm.ED25519, private_key)

    assert sig == sig_bytes_1


def test_get_signature_from_pem_file():
    sig = get_signature_from_pem_file(
        hash_bytes_1, f1path, KeyAlgorithm.ED25519)
    assert sig == sig_bytes_1


def test_is_signature_valid():
    _private_key, public_key = get_key_pair_from_pem_file(
        f1path, KeyAlgorithm.ED25519)
    assert is_signature_valid(
        hash_bytes_1, KeyAlgorithm.ED25519, sig_bytes_1, public_key)


# === SECP256K1
def test_get_key_pair_secp256k1():
    private_key, public_key = get_key_pair(KeyAlgorithm.SECP256K1)
    print("private_key:", private_key.hex())
    print("public_key:", public_key.hex())


def test_get_key_pair_from_bytes_secp256k1():
    private_key, public_key = get_key_pair_from_bytes(
        bytes.fromhex("2fee2f3400be052335a53dfac33b7f94b5329727e3ba3b7ebb726820ff039a32"), KeyAlgorithm.SECP256K1)
    assert public_key.hex() == "0202c8025b9d253d0bf5f48a96e8fdcecce3fd03731e7cdc47c6c7d297e75bc3ab11"


def test_get_key_pair_from_base64():
    # get_key_pair_from_base64()
    # todo
    pass


def test_get_key_pair_from_hex_string_secp256k1():
    private_key, public_key = get_key_pair_from_hex_string(
        "2fee2f3400be052335a53dfac33b7f94b5329727e3ba3b7ebb726820ff039a32", KeyAlgorithm.SECP256K1)
    assert public_key.hex() == "0202c8025b9d253d0bf5f48a96e8fdcecce3fd03731e7cdc47c6c7d297e75bc3ab11"


def test_get_key_pair_from_pem_file_secp256k1():
    private_key, public_key = get_key_pair_from_pem_file(
        f2path, KeyAlgorithm.SECP256K1)
    assert private_key.hex(
    ) == private_key_hex_2
    assert public_key.hex() == public_key_hex_2


def test_get_pvk_pem_from_bytes_secp256k1():
    # todo
    pass


def test_get_pvk_pem_from_hex_string_secp256k1():
    # todo
    pass


def test_get_pvk_pem_file_from_bytes_secp256k1():
    # todo
    pass


def test_get_signature_secp256k1():
    private_key, public_key = get_key_pair_from_pem_file(
        f2path, KeyAlgorithm.SECP256K1)
    sig = get_signature(hash_bytes_2, KeyAlgorithm.SECP256K1, private_key)

    assert sig == sig_bytes_2


def test_get_signature_from_pem_file_secp256k1():
    sig = get_signature_from_pem_file(
        hash_bytes_2, f2path, KeyAlgorithm.SECP256K1)
    assert sig == sig_bytes_2


def test_is_signature_valid_secp256k1():
    _private_key, public_key = get_key_pair_from_pem_file(
        f2path, KeyAlgorithm.SECP256K1)
    assert is_signature_valid(
        hash_bytes_2, KeyAlgorithm.SECP256K1, sig_bytes_2, public_key)
