# Python Numbers

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))


# Python List

a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

# Python Tuple


t = (5,'program', 1+3j)


print("t[1] = ", t[1])


print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
t[0] = 10


# Python Strings


s = 'Hello world!'

print("s = ", s)

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# Strings are immutable in Python
s[5] ='d'

# Python Set

a = {5,2,3,1,4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))

# Python Dictionary

d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1]);

print("d['key'] = ", d['key']);


print("d[2] = ", d[2]);

# Conversion between data types


float(5)
int(10.6)
float('2.5')
str(25)
int('1p')

set([1,2,3])
tuple({5,6,7})
list('hello')
dict([[1,2],[3,4]])
dict([(3,26),(4,44)])


# Literal is a raw data given in a variable or constant

#Integer Literal
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)


#string


strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# Boolean literals
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)