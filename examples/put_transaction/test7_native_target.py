from python_condor import CLU512, CLPublicKey, KeyAlgorithm, PutTransaction, NativeBuilder

initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chainname = "integration-test"


args = {"target": CLPublicKey(
    "01bb63a712307a193309f181820a10ac8287dc3c853a659e0b5220f7f7732c8c61"), "amount": CLU512(2500000000)}
key_path = "/Users/jh/mywork/python_sdk_condor/work/secret_key.pem"
url = "http://node.integration.casper.network:7777/rpc"
builder = NativeBuilder([(key_path, KeyAlgorithm.ED25519)])
transaction_json = builder.runtime_args(args). \
    chainname(chainname). \
    entry_point("Transfer"). \
    from_publickey(initiatorAddr). \
    payment(2500000000).build()


transaction_result = PutTransaction(url, transaction_json).run()
print(transaction_result)
