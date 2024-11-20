from json import dumps
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey


# Generate privateKey from PEM string
privateKey = PrivateKey.fromPem("""
    -----BEGIN EC PARAMETERS-----
    BgUrgQQACg==
    -----END EC PARAMETERS-----
    -----BEGIN EC PRIVATE KEY-----
    MHQCAQEEIODvZuS34wFbt0X53+P5EnSj6tMjfVK01dD1dgDH02RzoAcGBSuBBAAK
    oUQDQgAE/nvHu/SQQaos9TUljQsUuKI15Zr5SabPrbwtbfT/408rkVVzq8vAisbB
    RmpeRREXj5aog/Mq8RrdYy75W9q/Ig==
    -----END EC PRIVATE KEY-----
""")

publicKey = privateKey.publicKey()

message = "My test message"

# Generate Signature
signature = Ecdsa.sign(message, privateKey)

# To verify if the signature is valid
print(Ecdsa.verify(message, signature, publicKey))
