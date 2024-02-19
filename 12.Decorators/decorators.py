
def new(func):
    def inside(a,b):
        if b==0:
            a, b = b, a
            return func(a, b)
    return inside

@new                    # divide = new(divide)
def divide(a, b): 
    return a/b


print(divide(5, 0))