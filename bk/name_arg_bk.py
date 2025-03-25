# export class NamedArg implements ToBytes {
#   constructor(public name: string, public value: CLValue) {}

#   public toBytes(): ToBytesResult {
#     const name = toBytesString(this.name);
#     const value = CLValueParsers.toBytesWithType(this.value);
#     return Ok(concat([name, value.unwrap()]));
#   }

from cl_list import CLList
from cl_number import *
from cl_publickey import CLPublicKey
from cl_string import CLString


class NamedArg:
    def __init__(self, args):
        self.args = args

    def __serialize__(self):
        inner_serialize = ''
        print(self.args)
        for name, value in self.args.items():
            s_name = CLString(name).serialize()
            inner_serialize += s_name
            s_value = value.cl_value()
            inner_serialize += s_value
        list_length = '{:02x}'.format(
            len(self.args)).ljust(8, '0')
        return list_length + inner_serialize


#     amount: CLValueBuilder.u256(123),
# owner: CLValueBuilder.u256(456),
# recipient: CLValueBuilder.string("hello")
a = NamedArg({"amount": CLU256(123), "owner": CLU256(
    456), 'recipient': CLString("hello")})
print(a.__serialize__())
a = NamedArg({"arg1": CLU32(42), "arg2": CLU32(43)})
print("a is:", a.__serialize__())
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
