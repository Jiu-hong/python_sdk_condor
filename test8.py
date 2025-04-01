import json
from python_condor import CLBool
from python_condor.cl_values.cl_number import CLI32, CLI64, CLU128, CLU16, CLU256, CLU32, CLU512, CLU64, CLU8
a = CLBool(True)
print("a:", a.cl_value())


a = CLI32(123)
print("serialize:", a.serialize(), a.serialize().hex())
print("value:", a.value())
print("cl_value:", a.cl_value())
print("to_json", a.to_json())

a = CLI64(123)
print("serialize:", a.serialize(), a.serialize().hex())
print("value:", a.value())
print("cl_value:", a.cl_value())
print("to_json", a.to_json())

a = CLU8(123)
print("serialize:", a.serialize(), a.serialize().hex())
print("value:", a.value())
print("cl_value:", a.cl_value())
print("to_json", a.to_json())

a = CLU16(123)
print("serialize:", a.serialize(), a.serialize().hex())

a = CLU32(123)
print("serialize:", a.serialize(), a.serialize().hex())
print("value:", a.value())
print("cl_value:", a.cl_value())
print("to_json", a.to_json())

a = CLU64(123)
print("serialize:", a.serialize(), a.serialize().hex())
print("value:", a.value())
print("cl_value:", a.cl_value())
print("to_json", a.to_json())
a = CLU128(123)
print("serialize:", a.serialize(), a.serialize().hex())
print("value:", a.value())
print("cl_value:", a.cl_value())
print("to_json", a.to_json())

a = CLU256(123)
print("serialize:", a.serialize(), a.serialize().hex())
print("value:", a.value())
print("cl_value:", a.cl_value())
print("to_json", a.to_json())

a = CLU512(123)
print("serialize:", a.serialize(), a.serialize().hex())
print("value:", a.value())
print("cl_value:", a.cl_value())
print("to_json", a.to_json())

# a = CLBool("True")
a = None
print(type(a))
if a is None:
    print("here")
else:
    print("there")

a = {}
a["key1"] = "hello"
a["key2"] = None
print(a)
print(json.dumps(a))
x = bytearray("null", encoding="utf-8")
print(x.hex())
a = CLBool(True)
print("type a is:", type(a).__class__.__name__)
