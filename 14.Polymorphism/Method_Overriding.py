
"""
Different methods
Same name
Different Task
"""

class Parent:
    def func(self):
        print("Hello")
        
class Child(Parent):
    def func(self):                 #func() method is overriding
        print("Welcome")

myObj = Child()
myObj.func()

