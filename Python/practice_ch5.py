myList = [1, 2, 3]
print type(myList)
myList.append(1)
print myList
myList.extend([1, 2, 3])
print myList
myList.insert(3, 5)
print myList
myList.remove(3)
print myList
myList.remove(3)
print myList
# Throws error, no more 3's in list
# myList.remove(3)
a = myList.pop()
print a
print myList
print myList.index(1)
print myList.count(1)
print myList.count(0)

## Lists can be efficiently used as stacks (last in, first out)
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print stack
print stack.pop()
print stack

## Lists are inefficient as queues, use deque from collections
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print queue
print queue.popleft()
print queue
print queue.popleft()
print queue

# filter, map and reduce functions

# filter's equivalent in R is calling sapply on a vector and then filtering
# by the result.
def f(x):
	return x >= 3 and x <= 10
print myList
print filter(f, myList)

# map is the equivalent of sapply
def cube(x):
	return x*x*x
print map(cube, myList)

# map also handles mapply
def add(x, y):
	return x + y
# Throws error, requires two arguments
# print map(add, myList)
print map(add, myList, myList)
# Not the same as adding the lists!
print myList + myList

# reduce is like do.call on a list:
print reduce(add, range(1, 10))

# List comprehension
squares = []
for x in range(10):
	squares.append(x**2)

squares2 = [x**2 for x in range(10)]
print squares
print squares2

points = [(x, y) for x in [1, 2, 3] for y in range(3) if x != y]
print points

vec = map(lambda x: x*2-4, range(5))
print [x**2 for x in vec]
print [x for x in vec if x >= 0]
print [abs(x) for x in vec]
print map(abs, vec)
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print [itemVal for subList in vec for itemVal in subList]
matrix = [[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12]]
print matrix

print [[i + 4*j + 1 for i in range(4)] for j in range(3)]
print [[row[i] for row in matrix] for i in range(4)]
print zip(*matrix)

# List deletion
a = [-1, 1, 2, 333, 333, 123]
del a[0]
print a
del a[2:4]
print a
del a[:]
print a
del a
# Throws an error
# print a

# Tuples
t = 12345, 54321, 'hello'
print t
# tuples of length 1
x = 'abc',
print x
print type(x)
print len(x)

# sets
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)
print fruit
print 'orange' in fruit
print 'crabgrass' in fruit
print 'orange' in basket
a = set("abracadabra")
b = set("alakazaam")
print a
print a - b
print a | b
print a & b
print a ^ b


# Dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print tel
print tel['jack']
del tel['sape']
tel['irv'] = 4127
print tel
print tel.keys()
print 'guido' in tel
print 'guido' in tel.keys()
print dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print {x: x**2 for x in (2, 4, 6)}
print dict(sape=4139, guido=4127, jack=4098)


# looping
for i, v in enumerate(['tic', 'tac', 'toe']):
	print i, v

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
print type(questions)
for q, a in zip(questions, answers):
	print 'What is your {0}?  It is {1}.'.format(q, a)
	print q, a

for i in reversed(range(10)):
	print(i)

backet = ['apple', 'orange', 'apple', 'pear', 'orange']
for f in sorted(basket):
	print f

for k, v in tel.iteritems():
	print k, "'s number is", v

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for i in raw_data:
	if not math.isnan(i):
		filtered_data.append(i)
print filtered_data

# Comparing sequences
print (1, 2, 3)              < (1, 2, 4)
print [1, 2, 3]              < [1, 2, 4]
print 'ABC' < 'C' < 'Pascal' < 'Python'
print (1, 2, 3, 4)           < (1, 2, 4)
print (1, 2)                 < (1, 2, -1)
print (1, 2, 3)             == (1.0, 2.0, 3.0)
print (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)