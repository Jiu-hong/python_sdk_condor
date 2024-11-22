# with open("contract/cep18.wasm", mode='rb') as file:  # b is important -> binary
#     fileContent = file.read()

# print(fileContent.hex())
# import json
# a = ['foo', {'bar': ('baz', None, 1.0, 2)}]
# b = json.dumps(a)
# print("a=>", a)
# print("b=>", b)

# c = ["foo", {"bar": ["baz", None, 1.0, 2]}]
# print("d=>", json.dumps(c))

# from time import time
# from datetime import datetime, timezone, date, UTC, time as time1
# a = datetime(2019, 5, 18, 15, 17, 8, 132263).isoformat()
# print("a=>", a)
# b = datetime(2019, 5, 18, 15, 17, tzinfo=timezone.utc).isoformat()
# print("b=>", b)

# # a = int(time() * 1000)
# c2 = time()
# print("c2=>", c2)
# c1 = datetime.fromtimestamp(time(), tz=timezone.utc)
# print("c1=>", c1)
# c = c1.isoformat()
# print("c=>", c)


# # 2024-11-17T12:20:47.253Z
# output_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
# print("output-date=>", output_date)

# dt = time1(hour=12, minute=34, second=56, microsecond=0)
# d = dt.isoformat(timespec='milliseconds')
# print("d=>", d)

# t = datetime.now()
# s = t.isoformat(timespec='milliseconds')
# print("s->", s)
# now = datetime.utcnow().isoformat(timespec='milliseconds')
# print("now1=>", now)
# now = datetime.now(timezone.utc).replace(tzinfo=None)
# print("now        =>", now)
# now_format = datetime.now(timezone.utc).replace(
#     tzinfo=None).isoformat(timespec='milliseconds')+"Z"
# print("now_format:=>", now_format)

import json

from cl_list import CLList
from cl_number import CLU32
from cl_string import CLString
from cl_tuple import CLTuple2
# from cl_util import deep_type_v2
with open("./args.json") as f:
    print()
    file = f.read()

# print(type(file))

# a = file["args"]
# print(a[0][0])
# a = json.load(file["args"])
# print(a[0][0])

# a = [
#     "recipient",
#     {
#         "cl_type": "Key",
#         "bytes": "00d9758b25962f4cba82ba0047389af97a70acb7df43b391f9ffb293801bea5061",
#         "parsed": {
#             "Account": "account-hash-d9758b25962f4cba82ba0047389af97a70acb7df43b391f9ffb293801bea5061"
#         }
#     }
# ]
# b = json.loads(file)
# # print(b)
# c = b["args"][1][1]
# print(c)
# for k, v in c.items():
#     print(k, v)
# print(b["recipient"])

c = CLList([CLTuple2((CLU32(1), CLString("Hello, World!"))),
           CLString("world"), CLString("nihao"), CLList([CLString("nihao1"), CLString("nihao2")])])

print(c.cl_type())
# a = {"CLTuple2": {"CLU32": "1", "CLString": "Hello, World!"}, "CLString": "world",
#      "CLString": "nihao", "CLList": {"CLString": "nihao1", "CLString": "nihao2"}}
# print(a)
# print(json.dumps(a))
# print("deep_type_v2=>", json.dumps(a))
