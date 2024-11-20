import hashlib
import ecdsa

message = b'2087ec3b9d362ec95c64eb8430df29ad228054194fba3a6265cdf12ac92e85ff'

digest = hashlib.sha256()
digest.update(message)
hash = digest.digest()

# sk = ecdsa.SigningKey.from_string(
#     private_key_buffer, curve=ecdsa.SECP256k1)

pem_content = '''
-----BEGIN EC PRIVATE KEY-----
MC4CAQEEIK9Lz05wPb+8f+Og8ja90LwObm5vohY+zsw6BQSWebUZoAcGBSuBBAAK
-----END EC PRIVATE KEY-----
'''
sk = ecdsa.SigningKey.from_pem(pem_content)
signature = sk.sign_digest_deterministic(hash, hashfunc=hashlib.sha256)

print(signature.hex())
