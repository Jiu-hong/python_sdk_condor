import hashlib
from ecdsa import SigningKey, VerifyingKey
from ecdsa.util import sigencode_der, sigdecode_der, sigencode_strings, sigencode_strings_canonize, sigencode_string_canonize

path = "/Users/jh/mywork/python_sdk_condor/work/secret_key2.pem"
with open(path) as f:

    sk = SigningKey.from_pem(f.read(), hashlib.sha256)
    print("sk here:", sk)

tx = bytes.fromhex(
    "66323a7693f09160405c1c550c69b367b32b2d68925d9b2cef0780d7e681e120")
# sig = sk.sign_deterministic(tx, sigencode=sigencode_strings_canonize) #correct
sig = sk.sign_deterministic(tx, sigencode=sigencode_string_canonize)  # correct
print("sig[0]:", sig.hex())
# print("sig[1]:", sig[1].hex())

# expected signature:
# 6d6b1fe70eb741677eb3eb42e0a873647c5273e7a04ede58ab2fb04c03b44ccd
# 2398cb7d0251749fc1079afab2f5d820f080dcb7ef96874d38baa95f4914a9f8
# actual
# 6d6b1fe70eb741677eb3eb42e0a873647c5273e7a04ede58ab2fb04c03b44ccd
# dc673482fdae8b603ef865054d0a27ddca2e002ebfb218ee8717b52d87219749
