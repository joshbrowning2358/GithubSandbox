import sys
x = open("test.csv")
print(type(x))
d = x.read()
print(d)
# Hard to read this way because we just get a string...
print(d[0])

s = "Hello, world"
print(str(s))
print(repr(s))
print(str(1.0/7.0))
print(repr(1.0/7.0))
print(str(1/7))
print(repr(1/7))
x, y = (100.1, 200)
s = "The value of x is " + repr(x) + " and the value of y is " + repr(y)
print(s)
s = "The value of x is " + str(x) + " and the value of y is " + str(y)
print(s)

# Write a table of squares and cubes
for x in range(1, 11):
	print(repr(x).rjust(2), repr(x*x).rjust(3),)
	print(repr(x**3).rjust(4))

for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# rjust is a method on strings that just adds spaces to justify, if
# possible:
print("abc".rjust(2))
print("abc".rjust(5))
print("abc".center(5))

print("123".zfill(3))
print("123".zfill(6))
print("-3.14".zfill(8))

print("We are the {} who say {}".format("knights", "Ni!"))
# Throws an error
# print("We are the {} who say {}".format("knights")
print("We are the {0} who say {1}".format("knights", "Ni!"))
print("We are the {1} who say {0}".format("knights", "Ni!"))
print("This {food} is {adjective}".format(food = "spam",
	adjective = "horrible"))
# Throws error
# print("This {food} is {adjective}".format("spam", "horrible"))

import math
print("The value of pi is {}".format(math.pi))
print("The value of pi is {!r}".format(math.pi))
print("The value of pi is {0:.3f}".format(math.pi))

table = {'Jack': 1234, 'John': 2345, 'Myself': 3456}
for name, phone in table.items():
	print("{0:10} => {1:4}".format(name, phone))