from cl_number import CLU256, CLU512


def myfunc(*a: str) -> bytes:
    print("*a is:", *a)
    print("a is:", a)
    # return int(a).to_bytes(1, byteorder="little")


a = myfunc("1", "2")
print(a)

a = ("e1", "e2", "e3")
print("===")
print(type(a[0]))
print("====hello")
# print(type(*a))

content = bytearray("helloworld", encoding="utf-8").hex()
print(content)
content1 = bytearray("helloworld-helloworld", encoding="utf-8").hex()
print(content1)

a = 1024
# b = a.to_bytes(byteorder='little')
# b = bytearray(a, byteorder='little')
# print("b:", b.hex())
l = a.bit_length()
print("l is:", l)


def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0:  # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value

    return val                         # return positive value as is


hex_string = '0x01'  # or whatever... '0x' prefix doesn't matter
out = twos_comp(int(hex_string, 16), 256)

print("out:", out)
x = 123

v = x.to_bytes(x.bit_length(), byteorder='little')
print("v is:", v.hex())
b = CLU256(123)
print("b to_json:", b.to_json())
print("type:", type(b))
print(b.serialize().hex())
c = CLU512(123)
print("c to_json:", c.to_json())
print("type:", type(c))
print(c.serialize().hex())
