# Ed25519
from cryptography.hazmat.primitives.asymmetric import ed25519, rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
private_key = ed25519.Ed25519PrivateKey.generate()

a = ed25519.Ed25519PrivateKey.from_private_bytes(bytes.fromhex(
    'a6342b0104398e84cdf61fb7b69f7c6a75fba1af895ede5540124ea1e0be7c60'))
print("hhere a =>", a)
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
MC4CAQAwBQYDK2VwBCIEIJC47X71fZp700jh531/LV2BugQSxd1/s9cEKQz3742X
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
        bytes.fromhex("6ca0f9d59827b45920a43937a044949d3bfe67f08c9b740375f1816ff9785c0e"))
    print('01'+signature.hex())


key_from_pemfile()
