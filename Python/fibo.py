def fib(n):
    a,  b = 0,  1
    while b < n:
        print(b)
        a,  b = b,  a + b

def fib2(n):
    a,  b = 0,  1
    result = []
    while b < n:
        result.append(b)
        a,  b = b,  a + b
    return result

# Code below allows different behaviour from command line execution and import
# Useful for testing the module code!
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))