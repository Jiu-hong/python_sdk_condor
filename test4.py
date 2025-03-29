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
print(type(*a))
