from python_condor import CLOption
from python_condor import RESULTHOLDER
from python_condor import EntityAliasTarget

from python_condor import TransactionScheduling, PricingMode,  TransactionEntryPoint, TransactionV1Payload, CLTuple3, CLString, CLBool, CLURef, TransactionV1, KeyAlgorithm, PutTransction

initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chainname = "integration-test"
f = open("wasm", "r")
module_bytes = f.read()

args = {"arg1": CLTuple3((CLString("hello"), CLBool(True), CLURef(
    "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007"))),
    "arg2": CLOption(None, CLString(RESULTHOLDER()))}
scheduling = TransactionScheduling()
initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
pricing_mode = PricingMode("Classic", 200000000000)
target1 = EntityAliasTarget("VmCasperV1", "accesscontract")
print("target1 to_bytes()", target1.to_bytes().hex())
entrypoint1 = TransactionEntryPoint("Custom", "test2")

payload = TransactionV1Payload(args, target1,
                               entrypoint1, scheduling, initiatorAddr, pricing_mode, "integration-test")

transaction = TransactionV1(
    payload, [("/Users/jh/mywork/python_sdk_condor/secret_key.pem", KeyAlgorithm.ED25519)])
url = "http://node.integration.casper.network:7777/rpc"
# print("transaction_to_json1:", json.dumps(transaction.to_json()))
a = PutTransction(url, transaction.to_json())
print(a.run())
