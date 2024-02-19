#Multiple inheritance............................................................

class Car:                          #Engine
    def func(self):
        print("Engine")

class Car1:                         #Body
    def func1(self):
        print("Body")

class Car2(Car, Car1):              #Seats, Engine, Body
    def func2(self):
        print("Seats")
        
carObj = Car()              
carObj.func()               

carObj1 = Car1()            
carObj1.func1()             

carObj2 = Car2()
carObj2.func2()
carObj2.func()
carObj2.func1()

#Multi level inheritance.........................................................

class Phone:                        #Camera
    def function(self):
        print("Camera")
        

class Phone1(Phone):                #WI-FI, Camera
    def function1(self):
        print("WI-FI")
        
class Phone2(Phone1):               #Bluetooth, WI-FI, Camera
    def function2(self):
        print("Bluetooth")
        

myObj = Phone()         
myObj.function()        # 

myObj1 = Phone1()
myObj1.function1()
myObj1.function()

myObj2 = Phone2()
myObj2.function2() 
myObj2.function1()
myObj2.function()