from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

pem_content = '''
-----BEGIN EC PRIVATE KEY-----
MC4CAQEEIK9Lz05wPb+8f+Og8ja90LwObm5vohY+zsw6BQSWebUZoAcGBSuBBAAK
-----END EC PRIVATE KEY-----
'''
# expect 02022e51d19e789834a950ab14131b9391010e5e5f9dd2eaadc6374b8e3b9d1f73c5
# actual
pem_content_as_bytes = str.encode(pem_content)

loaded_private_key = serialization.load_pem_private_key(
    pem_content_as_bytes,
    # or password=None, if in plain text
    password=None,
)

public_key = loaded_private_key.public_key()
print("public_key:", public_key)
public_numbers = public_key.public_numbers()
print("public_numbers:", public_numbers)
public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
# print("public_bytes:", public_bytes.splitlines())
print("public_bytes,", public_bytes)
print()


# class SECP256K1(EllipticCurve):
#     name = "secp256k1"
#     key_size = 256
signature = loaded_private_key.sign(
    bytes.fromhex(
        "2087ec3b9d362ec95c64eb8430df29ad228054194fba3a6265cdf12ac92e85ff"),
    ec.ECDSA(hashes.SHA3_256()))
print(signature.hex())
# -----BEGIN PUBLIC KEY-----
# MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAELlHRnniYNKlQqxQTG5ORAQ5eX53S6q3G
# N0uOO50fc8VijbGmOxtdN/SUv98dDzPeMv0D86JVEdTZS+nQMSMcUA==
# -----END PUBLIC KEY-----
