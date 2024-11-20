import ecdsa
from hashlib import sha256
message = b"message"
public_key = '2e51d19e789834a950ab14131b9391010e5e5f9dd2eaadc6374b8e3b9d1f73c5628db1a63b1b5d37f494bfdf1d0f33de32fd03f3a25511d4d94be9d031231c50'
# sig = '740894121e1c7f33b174153a7349f6899d0a1d2730e9cc59f674921d8aef73532f63edb9c5dba4877074a937448a37c5c485e0d53419297967e95e9b1bef630d'

vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(
    public_key), curve=ecdsa.SECP256k1, hashfunc=sha256)  # the default is sha1
print('vk:', vk)
# vk.verify(bytes.fromhex(sig), message)  # True
