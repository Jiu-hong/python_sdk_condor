import hashlib
from ecdsa.util import sigencode_der
from hashlib import sha256
from ecdsa import SigningKey, SECP256k1

from ecdsa.ecdsa import Private_key


pem_content = '''
-----BEGIN EC PRIVATE KEY-----
MC4CAQEEIK9Lz05wPb+8f+Og8ja90LwObm5vohY+zsw6BQSWebUZoAcGBSuBBAAK
-----END EC PRIVATE KEY-----
'''
signing_key = SigningKey.from_pem(pem_content)  # uses SECP256k1
# print(signing_key)
# a = signing_key.to_string()
# print("a:", a)

# public_key = signing_key.public_key()
verifying_key = signing_key.get_verifying_key()
# print("public_key:", public_key)
# print("verifying_key:", verifying_key.to_string().hex())


# sk = SigningKey.generate(curve=SECP256k1)  # uses SECP256k1
# vk = sk.get_verifying_key()

print('This is the secret key {} \nThis is the public key {}'.format(
    signing_key.to_string().hex(), verifying_key.to_string().hex()))


# ======
deploy_hash = "2087ec3b9d362ec95c64eb8430df29ad228054194fba3a6265cdf12ac92e85ff"
m = hashlib.sha256()
m.update(bytes.fromhex(deploy_hash))
bytes_sha256 = m.digest()

# a = sha256(bytes.fromhex(
#     "2087ec3b9d362ec95c64eb8430df29ad228054194fba3a6265cdf12ac92e85ff")).hexdigest()
sig_1 = signing_key.sign_deterministic(
    # bytes_sha256,
    bytes.fromhex(deploy_hash),
    hashfunc=hashlib.sha256  # ,
    # sigencode=sigencode_der
)

print("sig_1:", sig_1.hex())

# expect 02a2b250cc9418d65759f9c15a93b66a758fca114b4ed65f5df27918cc3b1a3d98045fb61133d58345b566a983e3659a7884b9efbb698d7a525887c8201e1fff22
# actual   a2b250cc9418d65759f9c15a93b66a758fca114b4ed65f5df27918cc3b1a3d98fba049eecc2a7cba4a99567c1c9a658635f4ed2b45bb25e9674a966cb216421f
# actual2  30741763cd15272c431ae57b810729ae8b29a1cf707a74d1ad874af75957d45b3791d9d3d1642dda42fb5a36c69c3e5ddacbd4313d8a30398dd5371037ca0389
