from python_condor import CLList, CLMap, CLU32, CLU8, CLOption, CLTuple1, CLTuple2, NoneHolder, CLTuple3, CLString, CLBool, CLURef, KeyAlgorithm, PutTransaction, SessionCallBuilder
from python_condor.cl_values.cl_key import CLKey

initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chainname = "integration-test"
f = open("/Users/jh/mywork/python_sdk_condor/work/wasm", "r")
f_empty = open("/Users/jh/mywork/python_sdk_condor/work/wasm_empty", "r")
module_bytes = f.read()
module_bytes_empty = f_empty.read()
key_path = "/Users/jh/mywork/python_sdk_condor/work/secret_key.pem"

url = "http://node.integration.casper.network:7777/rpc"
builder = SessionCallBuilder([(key_path, KeyAlgorithm.ED25519)])
transaction_json = builder.runtime_args({"arg1": CLTuple3((CLString("hello"), CLBool(True), CLURef(
    "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007"))),
    "arg2": CLOption(CLString(NoneHolder())),
    "arg12": CLKey("era-001"),
    "arg13": CLKey("transfer-23df36827bab18568e8077bf1151ed29497456e6bb0896371e9c1a244bcb30c9"),
    "arg14": CLKey("era-summary-0000000000000000000000000000000000000000000000000000000000000000"),
    "arg3": CLTuple1(CLString("helloworld")),
    "arg4": CLTuple2((CLString("helloworld"), CLBool(True))),
    "arg5": CLTuple3(
    (CLU32(1), CLOption(CLString(NoneHolder())), CLOption(CLBool(True)))),
    "arg6": CLList([CLOption(CLString("hello")), CLOption(CLString("world"))]),
    "arg7": CLMap({CLU8(3): CLOption(CLString("Jim")), CLU8(
        2): CLOption(CLString("Jack")), CLU8(4): CLOption(CLString("Jane")), CLU8(1): CLOption(CLString("Jill"))})
}). \
    chainname(chainname). \
    module_bytes(module_bytes_empty, True). \
    from_publickey(initiatorAddr). \
    payment(2500000000).build()

transaction_result = PutTransaction(url, transaction_json).run()
print(transaction_result)
