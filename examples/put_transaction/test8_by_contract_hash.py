import json

from result import Err, Ok
from python_condor import CLOption, EntityTarget, NoneHolder, TransactionScheduling, PricingMode,  TransactionEntryPoint, TransactionV1Payload, CLTuple3, CLString, CLBool, CLURef, TransactionV1, KeyAlgorithm, PutTransction
from python_condor.cl_values.cl_key import CLKey
from python_condor.cl_values.cl_number import CLU32, CLU64
from python_condor.cl_values.cl_result import CLResult
from python_condor.cl_values.cl_tuple import CLTuple2

initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chainname = "integration-test"


args = {"arg1": CLU32(1),
        # "arg1": CLKey("account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20"),
        # "arg2": CLKey("hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20"),
        # "arg3": CLKey("bid-addr-03da3cd8cc4c8f34e7731583e67ddc211ff9b5c3f2c52640582415c2cce9315b2a8af7b77811970792f98b806779dfc0d1a9fef5bad205c6be8bb884210d7d323c"),
        # "arg4": CLKey("bid-addr-00306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1"),
        # "arg5": CLKey("uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007"),
        "arg4": CLKey(
            "byte-code-v1-wasm-6565656565656565656565656565656565656565656565656565656565656565"),
        "arg2": CLKey("message-topic-entity-contract-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"),
        "arg3": CLKey("message-entity-contract-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a-0202020202020202020202020202020202020202020202020202020202020202-f"),
        "arg4": CLKey("named-key-entity-account-928d914bdcad3ca269e750f63ed3615c5d3f615cf97dba87006fd9f979dacb3c-dde6f264c89fe385a5b07c26d77284d6fddabe79653c5ca25cec39a6363e6ec7"),
        "arg5": CLKey("named-key-entity-contract-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a-2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b"),

        }
scheduling = TransactionScheduling()
initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
pricing_mode = PricingMode("Classic", 2500000000)
target1 = EntityTarget(
    "VmCasperV1", "b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6")

entrypoint1 = TransactionEntryPoint("Custom", "test2")

payload = TransactionV1Payload(args, target1,
                               entrypoint1, scheduling, initiatorAddr, pricing_mode, chainname)

transaction = TransactionV1(
    payload, [("/Users/jh/mywork/python_sdk_condor/work/secret_key.pem", KeyAlgorithm.ED25519)])
url = "http://node.integration.casper.network:7777/rpc"

# print(json.dumps(transaction.to_json()))
transaction_result = PutTransction(url, transaction.to_json()).run()
print(transaction_result)
