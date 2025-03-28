from result import Ok
from cl_list import CLList
from cl_number import CLU32
from cl_option import CLOption


class JH:
    a = 1


jh = JH()
b = jh.__getattribute__("a")
# print(b)
cv = JH
cv.__name__
print(JH.__name__)

b = CLList([CLOption(CLU32(13)), CLOption(CLU32(2)), CLOption(CLU32(3))])
# print(b.to_json())

bytes_len_hex = '{:02x}'.format(
    int(3)).ljust(8, '0')

print("bytes_len_hex:", bytes_len_hex)

d = int(3).to_bytes(4, byteorder='little')
print(d.hex())

e = int(3).to_bytes(4)
print(e.hex())


tag = '{:02x}'.format(11)
print("tag:", tag)

f = int(11).to_bytes(1, byteorder='little')
print("f is:", f.hex())


class MyObj(object):
    pass


a = MyObj()
# print(len(a))


a = {"a": 1, "b": 2}
items = list(a.items())
print(items[0])
print(type(items[0]))
# keys = a.keys()
# print(keys[0])
a = Ok("hello")
print("a.value:", a.value)
