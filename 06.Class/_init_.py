
class Person:
    def __init__(self):
        print("Hello Person")

person1 = Person()
person2 = Person()

#................................................................................

class Student:
    def __init__(self, name, age):
        """
            We never call __init__ method.
            It will automatically call when create object.
            Ex=> student1 = Student("John", 26)        
        """
        self.name = name
        self.age = age
        

student1 = Student("John", 26)
student2 = Student("Kevin", 45)
print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)