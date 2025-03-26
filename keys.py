# Ed25519
import base64
# from cryptography.hazmat.primitives.asymmetric import ed25519, rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import ed25519
private_key = ed25519.Ed25519PrivateKey.generate()

a = ed25519.Ed25519PrivateKey.from_private_bytes(bytes.fromhex(
    'a6342b0104398e84cdf61fb7b69f7c6a75fba1af895ede5540124ea1e0be7c60'))

print("private_key:", a.private_bytes_raw().hex())
print(private_key.public_key().public_bytes_raw().hex())
public_key = a.public_key()
public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)
print("public_bytes:", public_bytes.hex())
loaded_public_key = ed25519.Ed25519PublicKey.from_public_bytes(public_bytes)

# {
#   secretKey: Uint8Array(32) [
#     166,  52,  43,   1,   4,  57, 142, 132,
#     205, 246,  31, 183, 182, 159, 124, 106,
#     117, 251, 161, 175, 137,  94, 222,  85,
#      64,  18,  78, 161, 224, 190, 124,  96
#   ],
# a6342b0104398e84cdf61fb7b69f7c6a75fba1af895ede5540124ea1e0be7c60
#
#
#   publicKey: Uint8Array(32) [
#     212, 118,  10,  36,  45, 131, 134,
#     242, 137, 144, 195, 143, 246,  78,
#     218,  27, 202, 108, 152, 228, 182,
#      70,  96, 227, 189, 189, 255,  41,
#     190, 106, 126,  84
#   ]
# }

# a = rsa.generate_private_key()


def key_from_pemfile():
    pem_content = '''-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIKvQ1YlCTlFoEMpfBNWrmCNFFmeizVFKhwxGtjSWHatE
-----END PRIVATE KEY-----'''

    # expect 01054015b0d822d8e127f2a3d508fe9d68757e5c7b3c5d3b78d42df70af9c0adbd
    # actual   054015b0d822d8e127f2a3d508fe9d68757e5c7b3c5d3b78d42df70af9c0adbd

    # pem_content = '''-----BEGIN EC PRIVATE KEY-----
    # MC4CAQEEIK9Lz05wPb+8f+Og8ja90LwObm5vohY+zsw6BQSWebUZoAcGBSuBBAAK
    # -----END EC PRIVATE KEY-----'''
    # expect 02022e51d19e789834a950ab14131b9391010e5e5f9dd2eaadc6374b8e3b9d1f73c5
    # actual
    pem_content_as_bytes = str.encode(pem_content)
    privateKey = load_pem_private_key(pem_content_as_bytes, None)
    public_key = privateKey.public_key()
    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )
    print("public_bytes:", public_bytes.hex())
    signature = privateKey.sign(
        bytes.fromhex("dbe8401b2c4022c9c5cd920047ec743d37cbf0601855777c30763860955eb0e5"))
    print('01'+signature.hex())
    sk = ed25519.Ed25519PrivateKey.from_private_bytes(privateKey)

    signature = sk.sign(bytes.fromhex(
        "dbe8401b2c4022c9c5cd920047ec743d37cbf0601855777c30763860955eb0e5"))
    print("signature is ", signature)


_PVK_LENGTH = 32


def get_pvk_from_pem_file(fpath: str) -> bytes:
    """Returns an ED25519 private key decoded from a PEM file.

    :param fpath: Path to a PEM file.
    :returns: A private key.

    """
    # Open pem file.
    with open(fpath, "r") as fstream:
        as_pem = fstream.readlines()

    # Decode bytes.
    pvk_b64 = [i for i in as_pem if i and not i.startswith("-----")][0].strip()
    pvk = base64.b64decode(pvk_b64)

    return len(pvk) % _PVK_LENGTH == 0 and pvk[:_PVK_LENGTH] or pvk[-_PVK_LENGTH:]


def get_signature_from_pem_file(msg: bytes, fpath: str) -> bytes:
    """Returns an ED25519 digital signature of data signed from a private key PEM file.

    :param msg: A bunch of bytes to be signed.
    :param fpath: PEM file path.
    :returns: A digital signature.

    """
    return get_signature(msg, get_pvk_from_pem_file(fpath))


def get_signature(msg: bytes, pvk: bytes) -> bytes:
    """Returns an ED25519 digital signature of data signed from a private key PEM file.

    :param msg: A bunch of bytes to be signed.
    :param pvk: A private key derived from a generated key pair.
    :returns: A digital signature.

    """
    sk = ed25519.Ed25519PrivateKey.from_private_bytes(pvk)

    return sk.sign(msg)


# key_from_pemfile()
sig = get_signature_from_pem_file(bytes.fromhex(
    "2fffea947c2aeaa70a7953af70917e58da259fb5e61d931829f55eebb82a74d2"), "secret_key.pem")
print("sig is:", '01'+sig.hex())

private_key = get_pvk_from_pem_file("secret_key.pem")
ek25519KeyPair = ed25519.Ed25519PrivateKey.from_private_bytes(private_key)
public_key = '01' + ek25519KeyPair.public_key().public_bytes_raw().hex()
print(public_key)

# 017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5myenv
