# Changing directories
# The import from approach is "generally frowned upon":
from os import getcwd, chdir, listdir
getcwd()
chdir("/home/josh/Documents/Github/GithubSandbox/Python")
listdir(".")

# Importing modules
import fibo # Try running fibo from command line as well
fibo.fib(10)
print fibo.__name__

# Functions are defined, but still with prefixes fibo.fib, fibo.fib2.
# However, as above, we imported functions from os and these came directly in without requiring separate calls.

import sys
print sys.ps1
print sys.ps2
sys.ps1 = "><><><>"
# Search path for modules
print sys.path

import fibo, sys
print dir(fibo)
print dir(sys)
print dir() # objects defined currently, includes builtin functions

import __builtin__
dir(__builtin__)