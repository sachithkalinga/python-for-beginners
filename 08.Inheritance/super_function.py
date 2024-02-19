
class Parent:
    def parentFunction(self):
        print("Hello")
        
class Child(Parent):
    def childFunction(self):
        super().parentFunction()   #super function
        print("Welcome")
        

myObj = Child()
myObj.childFunction()
myObj.parentFunction()             #We can use super() in Child class