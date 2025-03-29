from datetime import datetime, timezone
import json
from time import time

from cl_number import CLU32, CLU64
from cl_string import CLString
a = {"initiator_addr":
     {"PublicKey": "01366d77126a722e1adce6ad0bf2fbdbcdc573eb5c9c338a1097f1837f3dc4ef88"
      }},
b = {"timestamp": "2025-03-19T09:47:13.625Z", }
c = datetime.now(timezone.utc).replace(
    tzinfo=None).isoformat(timespec='milliseconds')+"Z"
# serialize
# timestamp=time()
# CLU64(int(self.timestamp * 1000)).serialize()
# print("c is:", c)
d = datetime.now(timezone.utc).timestamp()
# print("d is:", d)
e = time()
# print("e is:", e)

base = datetime.now(timezone.utc)
# print("base", base)
# json
eee = base.replace(
    tzinfo=None).isoformat(timespec='milliseconds')+"Z"
# serialize
serial_timestamp = base.timestamp()
serial = CLU64(int(base.timestamp() * 1000)).serialize()

# 2025-03-19T09:47:13.625Z
# 2025-03-23T23:59:55.765Z


def to_json():
    result = {}
    # result = {"PaymentLimited": {
    #     "payment_amount": self.payment_amount, "gas_price_tolerace": self.gas_price_tolerance, "standard_payment": self.standard_payment}}
    result["pricing_mode"] = {
        "PaymentLimited": {
            "payment_amount": 123,
            "gas_price_tolerance": 456,
            "standard_payment": True
        }}
    return result


# result = {}
# b = result["initiator_addr"] = {"PublicKey": 98765}
# print("result", result)
# a = to_json()
# print("a", a)
# # print(a['pricing_mode']['PaymentLimited'])
# # c = {result.items() + a.items()}
# c = {**result, **a}
# print("c ", c)

# dt = datetime.fromisoformat('2023-04-01T05:00:30.001000').timestamp()
#                            2025-03-19T09:47:13.625Z
dt = datetime.fromisoformat('2025-03-24T00:49:13.133Z').timestamp()
print(dt)
# dt2 = datetime.now(timezone.utc)
# print(dt2.timestamp())
# mine = datetime.now(timezone.utc)
# print(mine)
# f = open("wasm", "r")
# print(f.read())

# 0400000061726731040000002a00000004
# arg1: u32(42)
# a = CLString("arg1").serialize()
# print("a is ", a)

# b = CLU32(42).serialize().hex()
# print("b is", b)

# c = CLU32(42).cl_value()
# print("C is, ", c)

a = {"a": 1, "b": 2}
# a["key1"] = 1
# a["key2"] = 2
print(a, type(a))
b = json.dumps(a)
print(b, type(b))
v = {}
v["key1"] = 3
v["key2"] = 4

v["key0"] = a
print(json.dumps(v))
my_dict = {}
my_dict["cl_type"] = "hello"
my_dict["parsed"] = "xxxxxx"

a = (1, my_dict)
print(json.dumps(a))
