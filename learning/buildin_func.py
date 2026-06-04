# abs()
print(abs(-10))                     # 10

# all()
print(all([True, 1, "abc"]))        # True

# any()
print(any([False, 0, "", 5]))       # True

# ascii()
print(ascii("café"))                # 'caf\xe9'

# bin()
print(bin(10))                      # 0b1010

# bool()
print(bool(""))                     # False

# bytearray()
b = bytearray(b"abc")
b[0] = 65
print(b)                            # bytearray(b'Abc')

# bytes()
b = bytes("hello", "utf-8")
print(b)

# callable()
def f(): pass
print(callable(f))                  # True

# chr()
print(chr(65))                      # A

# complex()
print(complex(2, 3))                # (2+3j)

# dict()
d = dict(name="Abhay", age=20)
print(d)

# dir()
print(dir(str))

# divmod()
print(divmod(17, 5))                # (3,2)

# enumerate()
for i, v in enumerate(["a", "b"]):
    print(i, v)

# eval()
print(eval("2 + 3"))                # 5

# filter()
nums = [1,2,3,4]
print(list(filter(lambda x: x%2==0, nums)))

# float()
print(float("3.14"))

# format()
print(format(1234.567, ".2f"))      # 1234.57

# frozenset()
fs = frozenset([1,2,3])

# getattr()
class A:
    x = 10
print(getattr(A, "x"))

# hasattr()
print(hasattr(A, "x"))

# hash()
print(hash("hello"))

# help()
# help(str)

# hex()
print(hex(255))                     # 0xff

# id()
a = [1,2]
print(id(a))

# input()
# name = input("Enter name: ")

# int()
print(int("123"))

# isinstance()
print(isinstance(5, int))

# issubclass()
print(issubclass(bool, int))

# iter()
it = iter([1,2,3])
print(next(it))

# len()
print(len("hello"))

# list()
print(list("abc"))

# locals()
print(locals())

# map()
print(list(map(lambda x:x*2,[1,2,3])))

# max()
print(max([1,5,3]))

# min()
print(min([1,5,3]))

# next()
it = iter([10,20])
print(next(it))

# oct()
print(oct(10))                      # 0o12

# ord()
print(ord("A"))                     # 65

# pow()
print(pow(2, 3))                    # 8
print(pow(2, 3, 5))                # 3

# print()
print("Hello")

# repr()
print(repr("hello"))

# reversed()
print(list(reversed([1,2,3])))

# round()
print(round(3.14159, 2))

# set()
print(set([1,2,2,3]))

# setattr()
class B: pass
b = B()
setattr(b, "name", "Abhay")
print(b.name)

# slice()
s = slice(1,4)
print([10,20,30,40,50][s])

# sorted()
print(sorted([4,1,3]))

# str()
print(str(123))

# sum()
print(sum([1,2,3]))

# tuple()
print(tuple([1,2,3]))

# type()
print(type(10))


# zip()
a = [1,2,3]
b = ["a","b","c"]
print(list(zip(a,b)))