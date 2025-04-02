from python_condor import CLU512, CLPublicKey, TransactionSessionTarget, TransactionScheduling, PricingMode,  TransactionEntryPoint, TransactionV1Payload, TransactionV1, KeyAlgorithm, PutTransction


initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chainname = "integration-test"
f = open("wasm", "r")
module_bytes = f.read()


args = {"target": CLPublicKey(
    "01bb63a712307a193309f181820a10ac8287dc3c853a659e0b5220f7f7732c8c61"), "amount": CLU512(2500000000)}
scheduling = TransactionScheduling()
initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
pricing_mode = PricingMode("Classic", 2500000000)

f = open("wasm", "r")
module_bytes = f.read()
target1 = TransactionSessionTarget("VmCasperV1", module_bytes)

entrypoint1 = TransactionEntryPoint("Call")

payload = TransactionV1Payload(args, target1,
                               entrypoint1, scheduling, initiatorAddr, pricing_mode, "integration-test")

transaction = TransactionV1(
    payload, [("/Users/jh/mywork/python_sdk_condor/secret_key.pem", KeyAlgorithm.ED25519)])
url = "http://node.integration.casper.network:7777/rpc"


transaction_result = PutTransction(url, transaction.to_json()).run()
print(transaction_result)
