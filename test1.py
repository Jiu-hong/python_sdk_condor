# const namedArg = new NamedArg("arg1", CLValue.newCLUInt32(42))
from cl_number import CLI32, CLU32
from named_args import NamedArg


named_arg = NamedArg("arg1", CLU32(42))
# expected
# 0400000061726731040000002a00000004
# 0400000061726731040000002a00000004
print(named_arg.to_byte_with_named_arg().hex())
