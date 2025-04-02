
from python_condor.constants.base import TAG
from python_condor.constants.cons_jsonname import JsonName
from python_condor.utils import serialize_string
from python_condor.cl_values import *

JSONNAME = JsonName()


class DeployNamedArg:
    def __init__(self, args):
        for arg_value in args.values():
            if not hasattr(arg_value, "tag"):
                raise ValueError("The value for NamedArg should be CLValue.")
        self.args = args

    def serialize(self) -> bytes:
        inner_serialize = b''
        for name, value in self.args.items():

            s_name = serialize_string(name)
            inner_serialize += s_name
            s_value = bytes.fromhex(value.cl_value())
            inner_serialize += s_value

        list_length = int(len(self.args)).to_bytes(4, "little")
        return list_length + inner_serialize

    def to_json(self):
        args_list = []
        for key, value in self.args.items():
            my_dict = {}
            my_dict[JSONNAME.CL_TYPE] = value.to_json()
            my_dict[JSONNAME.BYTES] = value.serialize().hex()
            my_dict[JSONNAME.PARSED] = value.value()
            args_list.append((key, my_dict))
        return args_list


a = DeployNamedArg({"amount": CLU256(123), "owner": CLU256(
    456), 'recipient': CLString("hello")})
# print(a.serialize())
# 0300000006000000616d6f756e74200000007b0000000000000000000000000000000000000000000000000000000000000007050000006f776e657220000000c8010000000000000000000000000000000000000000000000000000000000000709000000726563697069656e74090000000500000068656c6c6f0a
# expect 0300000006000000616d6f756e7402000000017b07050000006f776e65720300000002c8010709000000726563697069656e74090000000500000068656c6c6f0a
# actual 0300000006000000616d6f756e7402000000017b07050000006f776e65720300000002c8010709000000726563697069656e74090000000500000068656c6c6f0a
#   RuntimeArgs.fromMap({
#     pks: ACCOUNT_PUBKEYS,
#   })
# const pk1String1 =
#   "01d0ee8f3827c8b28817e5d3a02a8041b6c488e5880dab0d56d904f3f3356fcd9c";
# const pk1 = CLPublicKey.fromHex(pk1String1);

# // user=3
# const pk2String2 =
#   "012108a170b4e14ddc9b3d7872779d07f5c9d3268fe5f5363f9e10c4af1880e5ae";
# const pk2 = CLPublicKey.fromHex(pk2String2);

# const ACCOUNT_PUBKEYS = new CLList([pk1, pk2]);
# expect 01000000 03000000 706b7346000000 02000000 01d0ee8f3827c8b28817e5d3a02a8041b6c488e5880dab0d56d904f3f3356fcd9c 012108a170b4e14ddc9b3d7872779d07f5c9d3268fe5f5363f9e10c4af1880e5ae 0e16
# actual 0100000003000000706b73460000000200000001d0ee8f3827c8b28817e5d3a02a8041b6c488e5880dab0d56d904f3f3356fcd9c012108a170b4e14ddc9b3d7872779d07f5c9d3268fe5f5363f9e10c4af1880e5ae0e
# a = NamedArg({"pks": CLList([CLPublicKey(
#     "01d0ee8f3827c8b28817e5d3a02a8041b6c488e5880dab0d56d904f3f3356fcd9c"), CLPublicKey(
#     "012108a170b4e14ddc9b3d7872779d07f5c9d3268fe5f5363f9e10c4af1880e5ae")])})
# print(a.__serialize__())
