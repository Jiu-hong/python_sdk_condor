from python_condor import CLU512, CLPublicKey, KeyAlgorithm, PutTransction, NativeBuilder

initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chainname = "integration-test"
f = open("wasm", "r")
module_bytes = f.read()

args = {"target": CLPublicKey(
    "01bb63a712307a193309f181820a10ac8287dc3c853a659e0b5220f7f7732c8c61"), "amount": CLU512(2500000000)}

url = "http://node.integration.casper.network:7777/rpc"
builder = NativeBuilder([("secret_key.pem", KeyAlgorithm.ED25519)])
transaction_json = builder.runtime_args(args). \
    chainname(chainname). \
    entry_point("Transfer"). \
    from_publickey(initiatorAddr). \
    payment(2500000000).build()

transaction_result = PutTransction(url, transaction_json).run()
print(transaction_result)
