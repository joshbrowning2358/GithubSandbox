import sys
# if statements
if len(sys.argv) > 1:
	x = int(sys.argv[1])
else:
	x = -999

if x < 0:
	x = 0
	print "Negative changed to zero"
elif x == 0:
	print "Zero"
elif x == 1:
	print "Single"
else:
	print "More"

# for loop
words = ["cat", "window", 'defenestrate']
for w in words:
	print w, len(w)

# Infinite loop
# words = ["cat", "window", 'defenestrate']
# for w in words:
# 	if len(w) > 6:
# 		words.insert(0, w)
# print words

words = ["cat", "window", 'defenestrate']
for w in words[:]: # Makes a copy of words to iterate over
	if len(w) > 6:
		words.insert(0, w)
print words

# range (similar to seq in R)
print range(10)
print range(5, 10)
print range(5, 10, 3)
a = ["Mary", "had", "a", "little", "lamb."]
for i in range(len(a)):
	print i, a[i],


# break
for n in range(10):
	for divisor in range(2,n):
		if n % divisor == 0:
	#		print n, "equals", divisor, "*", n/divisor
			break
	else:
		print n, " is prime"

# continue
for n in range(10):
	if n % 2 == 0:
		print n, " is even."
		continue
	print n, " is odd."

# Defining functions!
def fib(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

print "First fibonacci number", fib(1)
print "Tenth fibonacci number", fib(10)
# print "30th fibonacci number", fib(30)

def fibFast(n):
	""" Print a fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print a,
		a, b = b, a + b
	else:
		print "\n"
fibFast(2000)

def addOne(n):
	""" This function adds one to n."""
	n = n + 1
n = 100
addOne(n)
print n
x = 100
addOne(x)
print x

def fibReturn(n):
	""" Return the first n fibonacci numbers."""
	output = []
	a, b = 1, 1
	for i in range(n):
		output.append(a)
		a, b = b, a + b
	return output
print fibReturn(10)

# Default arguments
def ask_ok(prompt, retries = 4, complaint = "Yes or no, please!"):
	while True:
		ok = raw_input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no', 'nop', 'nope'):
			return False
		retries = retries - 1
		if retries < 0:
			raise IOError("refusenik user")
		print complaint

# Runs interactively:
# ask_ok("test: ")

def f(a, L = []):
	""" Appends a to a list L"""
	L.append(a)
	return(L)

print f(1)
print f(2)
print f(3)

def f(a, L = None):
	""" Appends a to a list L"""
	if L is None:
		L = []
	L.append(a)
	return(L)
print f(1)
print f(2)
print f(3)

print f(L = [1, 2], a = 3)
# Throws error (positional arg after keyword arg):
# print f(a = 1, [1, 2])

# Formal parameter like ...
def cheeseshop(kind, *arguments, **keywords):
	print "-- Do you have any", kind, "?"
	print "-- I'm sorry, we're all out of", kind
	for arg in arguments:
		print arg
	print "-" * 40
	# Sort because otherwise order is not defined
	keys = sorted(keywords.keys())
	for kw in keys:
		print kw, ":", keywords[kw]

cheeseshop("Limburger", "It's very runny, sir.",
	"It's really very, VERY runny, sir.",
	shopkeeper = 'Michael Palin',
	client = 'John Cleese',
	sketch = 'Cheese Shop Sketch')


# Passing vectors
def printText(*results):
	n = len(results)
	for i in range(n):
		print len(results), results[i],

printText("a", "b", "c")
print "\n"

myRange = [2, 4]
print range(myRange[0], myRange[1])
print range(*myRange)

def parrot(voltage, state = 'a stiff', action = 'voom'):
	print "This parrot wouldn't", action,
	print "if you put", voltage, "volts through it.",
	print "E's", state, "!"

parrot(100)
d = {"voltage": 400, "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

# Lambda functions: allows you to define a simple function inline.
def make_incrementor(n):
	return lambda x: x + n

f = make_incrementor(42)
print f(42)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key = lambda pairs: pairs[1])
print pairs