from python_condor.transaction_builder import ContractCallBuilder
from python_condor import TransactionScheduling, PricingMode, TransactionTarget, TransactionEntryPoint, TransactionV1Payload, CLTuple3, CLString, CLBool, CLURef, TransactionV1, KeyAlgorithm, PutTransction
import json

initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chainname = "integration-test"
# chainname = "casper-test"
builder = ContractCallBuilder([("secret_key.pem", KeyAlgorithm.ED25519)])
transaction_json = builder.args({"arg1": CLTuple3((CLString("hello"), CLBool(True), CLURef(
    "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007")))}). \
    chainname(chainname). \
    by_package_name("accesscontractpackage"). \
    entry_point("test2"). \
    from_publickey(initiatorAddr). \
    payment(2500000000).build()
# url = "https://node.testnet.casper.network/rpc"
url = "http://node.integration.casper.network:7777/rpc"
a = PutTransction(url, transaction_json)
print(a.run())
