#!/usr/bin/env python

# Reading arguments from command line (first is filename)
import sys
print sys.argv[0]
print "Arguments to function were "
print "Hello World"
print "And testing again"

the_world_is_flat = 1
if the_world_is_flat:
    print "Be careful not to fall off!"
    
# Playing around with vectors
x = (1, 2, 3)
print x[1]
print x[-1]

# Floor function
print 11 / 2
print 11. / 2
print 11 / 2.
print 11 // 2.
# Doesn't work: print 11^2
print 11 ** 2

# Types
print type(1)
print type(1.1)
from decimal import Decimal
print Decimal(-1) + Decimal(-2.2)
print (-7) // 4
print Decimal(-7) // Decimal(4)
print (-7) % 4
print Decimal(-7) % Decimal(4)
from fractions import Fraction
print Fraction(-8, 5)
print Fraction(-16, 10)
print Fraction(-8, 5) == Fraction(-16, 10)

# Strings
print "C:\some\name"
print r"C:\some\name" #"r" for raw
print 3 * "un" + "ium"
print "Py" "thon"
string1 = "Py"
# Throws error:
# string1 "thon"
# Also throws error:
# (3 * "un") "ium"
print 3 * "un" "ium"
print "un" * 3
testWord = "Hello, my name is Josh!"
print testWord[0] + testWord[4]
print testWord[-3] + testWord[3:6]
print testWord[4:]
print testWord[-5:]
print testWord[:-5]

# Back to vectors
x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print x[1]
print x[-1]
print x[:3]
print x[3:]
print x[3:5]
print x[3:111]
print len(x)

print u'Hello\u0020World !'

# Lists and vectors
x = (1, 2, 3, 4)
y = [1, 2, 3, 4]
print x
print y
print x[:]
print y[:]
z = y
z[0] = 0
print z
print y
z = x
# Throws an error (tuple doesn't support assignment)
# z[0] = 0

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print cubes
cubes.append(6 ** 3)
print cubes
# Throws an error
# cubes.append(7 ** 3, 8 ** 3)
cubes.append([7 ** 3, 8 ** 3])
print cubes
cubes[1:4] = [8, 27, 64]
print cubes
print "Length of cubes is " + str(len(cubes))
cubes[1:4] = [[8, 27, 64]]
print cubes
print "Length of cubes is " + str(len(cubes))

# Fibonacci series
a, b = 0, 1
while b < 100:
	print b
	a, b = b, a + b
a, b = 0, 1
while b < 100:
	print b,
	a, b = b, a + b