from python_condor import CLList
from python_condor import CLMap
from python_condor import CLU32, CLU8
from python_condor import CLOption
from python_condor import CLTuple1, CLTuple2
from python_condor import NoneHolder
from python_condor import ContractCallBuilder
from python_condor import CLTuple3, CLString, CLBool, CLURef,  KeyAlgorithm, PutTransction

initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chainname = "integration-test"


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
    by_package_hash("40ad74eb43330f7fb496d6ea49df990e6583f51a01a7204a17a6217dbeb715d7"). \
    entry_point("test2"). \
    from_publickey(initiatorAddr). \
    payment(2500000000).build()

transaction_result = PutTransction(url, transaction_json).run()
print(transaction_result)
