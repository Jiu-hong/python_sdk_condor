from python_condor import TransactionScheduling, PricingMode, TransactionTarget, TransactionEntryPoint, TransactionV1Payload, CLTuple3, CLString, CLBool, CLURef, TransactionV1, KeyAlgorithm, PutTransction
import json

from python_condor.entity_target import EntityTarget
from python_condor.transaction_builder import ContractCallBuilder
from python_condor.transaction_stored_target import TransactionStoredTarget

args = {"arg1": CLTuple3((CLString("hello"), CLBool(True), CLURef(
    "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007")))}
scheduling = TransactionScheduling()

initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
pricing_mode = PricingMode("Classic", 2500000000)
target1 = EntityTarget(
    "VmCasperV1", "b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6")
# print("target1 to_bytes()", target1.to_bytes().hex())
# entrypoint1 = TransactionEntryPoint("Custom", "test2")
entrypoint1 = TransactionEntryPoint("Custom", "test2")

# chain_name = "casper-test"
chain_name = "integration-test"
payload = TransactionV1Payload(args, target1,
                               entrypoint1, scheduling, initiatorAddr, pricing_mode, chain_name)
# print("payload:", payload.to_json())

transaction = TransactionV1(
    payload, [("secret_key.pem", KeyAlgorithm.ED25519)])
transaction_json = transaction.to_json()

# print("transaction_to_json1:", transaction_json)
# url = "https://node.testnet.casper.network/rpc"
url = "http://node.integration.casper.network:7777/rpc"
a = PutTransction(url, transaction_json)
print(a.run())

# a = ContractCallBuilder()
