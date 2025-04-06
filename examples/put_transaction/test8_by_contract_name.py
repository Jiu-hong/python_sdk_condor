from python_condor import CLOption, EntityAliasTarget, NoneHolder, TransactionScheduling, PricingMode,  TransactionEntryPoint, TransactionV1Payload, CLTuple3, CLString, CLBool, CLURef, TransactionV1, KeyAlgorithm, PutTransction

initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chainname = "integration-test"


args = {"arg1": CLTuple3((CLString("hello"), CLBool(True), CLURef(
    "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007"))),
    "arg2": CLOption(None, CLString(NoneHolder()))}
scheduling = TransactionScheduling()
initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
pricing_mode = PricingMode("Classic", 2500000000)
target1 = EntityAliasTarget("VmCasperV1", "accesscontract")

entrypoint1 = TransactionEntryPoint("Custom", "test2")

payload = TransactionV1Payload(args, target1,
                               entrypoint1, scheduling, initiatorAddr, pricing_mode, "integration-test")

transaction = TransactionV1(
    payload, [("/Users/jh/mywork/python_sdk_condor/work/secret_key.pem", KeyAlgorithm.ED25519)])
url = "http://node.integration.casper.network:7777/rpc"


transaction_result = PutTransction(url, transaction.to_json()).run()
print(transaction_result)
