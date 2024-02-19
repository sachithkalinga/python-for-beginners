def square(func):
    def wrapper(x):
        return func(x) ** 2
    return wrapper

@square
def add(args):
    a, b = args
    return a + b

print(add((3, 4)))

######################################################################################
# same code using lambda function

square = lambda func: (lambda x: func(x) ** 2)

@square
def add(args):
    a, b = args
    return a + b

print(add((3, 4)))

