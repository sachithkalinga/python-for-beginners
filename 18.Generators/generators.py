def test():
    yield 4           # Generator

y = test()
print(next(y))

#.............................................................................................
print("\n")

def marks(a):
    for i in a:
        yield i

z = marks([2, 4, 1, 5, 3])
print(next(z))
print(next(z))
print(next(z))
print(next(z))

#.............................................................................................
# Fibonacci example (0, 1, 1, 2, 3, 5, 8, 13, .............)
print("\n")

def fib():
    a, b = 0, 1
    
    while True:
        c = a+b
        yield a
        
        a, b = b, c

y = fib()

print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))