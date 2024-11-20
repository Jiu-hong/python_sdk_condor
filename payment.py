# StoredContractByHash serializes such that the first byte within
# the serialized buffer is 1u8. This is followed by the byte representation
# of the remaining fields.


from cl_number import CLU256, CLU512
from cl_string import CLString
from name_arg import NamedArg


# amount should be decimal motes
def serialize_payment(amount):
    ModuleBytesTag = '00'
    # # modulebytes 0 -> '00000000'
    result = ModuleBytesTag + \
        '00000000' + \
        NamedArg({"amount": CLU512(amount)}).__serialize__()
    return result


a = serialize_payment(300000000000)
print(a)

# expect 00000000000100000006000000616d6f756e74060000000500b864d94508
# actual 00000000000100000006000000616d6f756e74060000000500b864d94508
#                 "ModuleBytes": {
#                     "module_bytes": "",
#                     "args": [
#                         [
#                             "amount",
#                             {
#                                 "cl_type": "U512",
#                                 "bytes": "04005ed0b2",
#                                 "parsed": "3000000000"
#                             }
#                         ]
#                     ]
#                 }
