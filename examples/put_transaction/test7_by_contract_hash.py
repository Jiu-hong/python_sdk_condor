import json
from result import Err, Ok
from python_condor import CLList, CLMap, CLU32, CLU8, CLOption, CLTuple1, CLTuple2, NoneHolder
from python_condor import CLTuple1, CLTuple3, CLString, CLBool, CLURef, ContractCallBuilder, KeyAlgorithm, PutTransaction
from python_condor.cl_values.cl_result import CLResult

initiatorAddr = "017e037b8b5621b9803cad20c2d85aca9b5028c5ee5238923bb4a8fc5131d539f5"
chainname = "integration-test"

keys = [("/Users/jh/mywork/python_sdk_condor/work/secret_key.pem",
         KeyAlgorithm.ED25519),
        ("/Users/jh/mywork/python_sdk_condor/work/secret_key2.pem",
         KeyAlgorithm.SECP256K1)]
url = "http://node.integration.casper.network:7777/rpc"
builder = ContractCallBuilder(keys)
transaction_json = builder.runtime_args({
    "map_value": CLMap({CLU8(3): CLOption(CLString("Jim"))}),
    "map_empty_value": CLMap({}, {CLOption(CLU32(NoneHolder())): CLString(NoneHolder())}),
    "list_value": CLList([CLOption(CLString("hello")), CLOption(CLString("world"))]),
    "list_empty_value": CLList([], CLList([CLBool(NoneHolder())])),
    "option_value": CLOption(CLString("hello")),
    "option_empty_value": CLOption(CLString(NoneHolder())),
    "result_ok": CLResult(
        Ok(CLOption(CLTuple2((CLString("hello"), CLU32(123))))),
        Err(CLU32(NoneHolder())),
        True
    ),
    "result_err": CLResult(
        Ok(CLU32(NoneHolder())),
        Err(CLOption(CLTuple2((CLString("hello"), CLU32(123))))),
        False
    ),
    "tuple3_value": CLTuple3((
        CLString("hello"),
        CLBool(True),
        CLURef(
            "uref-fb6d7dd568bb45bd7433498c37fabf0883f8e5700c08a6541530d3425f66f17f-007")
    )),
    # "tuple3_empty_value": CLTuple3((
    #     CLString(NoneHolder()),
    #     CLBool(NoneHolder()),
    #     CLURef(NoneHolder())
    # )),
    # "tuple2_empty_value": CLTuple2((
    #     CLString(NoneHolder()),
    #     CLBool(NoneHolder()),
    # )),
    # "tuple1_empty_value": CLTuple1((
    #     CLString(NoneHolder())
    # ))
}). \
    chainname(chainname). \
    by_contract_hash("b5d048d4e3f892181c791f5362b33a6d3a36c720913fdc17bc099cab61923ee6"). \
    entry_point("test2"). \
    from_publickey(initiatorAddr). \
    payment(2500000000).build()

v = CLMap({}, {CLBool(NoneHolder()): CLString(NoneHolder())})
# print("transaction_json:", json.dumps(transaction_json))
transaction_result = PutTransaction(url, transaction_json).run()
print(transaction_result)
