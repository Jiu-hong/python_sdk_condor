import json

from result import Err, Ok
from python_condor import CLOption, EntityTarget, NoneHolder, TransactionScheduling, PricingMode,  TransactionEntryPoint, TransactionV1Payload, CLTuple3, CLString, CLBool, CLURef, TransactionV1, KeyAlgorithm, PutTransction
from python_condor.cl_values.cl_key import CLKey
from python_condor.cl_values.cl_number import CLU32, CLU64
from python_condor.cl_values.cl_result import CLResult
from python_condor.cl_values.cl_tuple import CLTuple2

initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chainname = "integration-test"


args = {
    "arg1": CLKey("account-hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20"),
    "arg2": CLKey("hash-0102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f20"),
    "arg3": CLKey("bid-addr-03da3cd8cc4c8f34e7731583e67ddc211ff9b5c3f2c52640582415c2cce9315b2a8af7b77811970792f98b806779dfc0d1a9fef5bad205c6be8bb884210d7d323c"),
    "arg4": CLKey("bid-addr-00306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1"),
    "arg6": CLKey(
        "balance-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"),
    "arg7": CLKey(
        "bid-306633f962155a7d46658adb36143f28668f530454fe788c927cecf62e5964a1"),
    "arg9": CLKey(
        "checksum-registry-0000000000000000000000000000000000000000000000000000000000000000"),
    "arg10": CLKey(
        "deploy-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"),
    "arg11": CLKey(
        "dictionary-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"),
    "arg12": CLKey("era-summary-0000000000000000000000000000000000000000000000000000000000000000"),
    "arg13": CLKey("era-42"),
    "arg14": CLKey("package-6464646464646464646464646464646464646464646464646464646464646464"),
    "arg15": CLKey(
        "system-entity-registry-0000000000000000000000000000000000000000000000000000000000000000"),
    "arg16": CLKey(
        "transfer-199957ab005a1bdc246691cb8bfba69ad9a7ee3fd856ad25ff51bb63406584ad"),
    "arg17": CLKey(
        "unbond-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"),
    "arg18": CLKey(
        "withdraw-2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2a"),
    "arg19": CLResult(Ok(CLOption(CLTuple2((CLString("hello"), CLU64(123))))),
                      Err(CLU32(NoneHolder())), True),
    "arg20": CLKey(
        "byte-code-v1-wasm-6565656565656565656565656565656565656565656565656565656565656565"),
    "arg21": CLKey(
        "byte-code-v2-wasm-6565656565656565656565656565656565656565656565656565656565656565"),
    "arg22": CLKey(
        "byte-code-empty-6565656565656565656565656565656565656565656565656565656565656565")
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
