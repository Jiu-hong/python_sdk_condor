from python_condor import CLList, CLMap, CLU32, CLU8, CLOption, CLTuple1, CLTuple2, NoneHolder
from python_condor import CLTuple3, CLString, CLBool, CLURef, ContractCallBuilder, KeyAlgorithm, PutTransction

initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chainname = "integration-test"
f = open("wasm", "r")
module_bytes = f.read()

url = "http://node.integration.casper.network:7777/rpc"
builder = ContractCallBuilder([("secret_key.pem", KeyAlgorithm.ED25519)])
transaction_json = builder.runtime_args({"arg1": CLTuple3((CLString("hello"), CLBool(True), CLURef(
    "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007"))),
    "arg2": CLOption(None, CLString(NoneHolder())),
    "arg3": CLTuple1(CLString("helloworld")),
    "arg4": CLTuple2((CLString("helloworld"), CLBool(True))),
    "arg5": CLTuple3(
    (CLU32(1), CLOption(None, CLString(NoneHolder())), CLOption(CLBool(True)))),
    "arg6": CLList([CLOption(CLString("hello")), CLOption(CLString("world"))]),
    "arg7": CLMap({CLU8(3): CLOption(CLString("Jim")), CLU8(
        2): CLOption(CLString("Jack")), CLU8(4): CLOption(CLString("Jane")), CLU8(1): CLOption(CLString("Jill"))})
}). \
    chainname(chainname). \
    by_contract_hash("b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6"). \
    entry_point("test2"). \
    from_publickey(initiatorAddr). \
    payment(2500000000).build()

transaction_result = PutTransction(url, transaction_json).run()
print(transaction_result)
