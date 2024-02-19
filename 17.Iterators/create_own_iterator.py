class myIt:
    def __init__(self):
        self.y=2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        val = self.y
        self.y += 2
        return val
    
myObj = myIt()
itr = iter(myObj)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))