import pickle

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)

personObj = Person("Kevin", 28)
personObj.display()

#Store class..............................................................................

with open(f"24.Pickle Module\class.pickle", "wb") as cp:
    pickle.dump(personObj, cp)

#Load class...............................................................................

with open(f"24.Pickle Module\class.pickle", "rb") as cp:
    person_data = pickle.load(cp)

person_data.display()