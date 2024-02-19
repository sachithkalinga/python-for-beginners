
#Private Variables..................................................................
class myClass1:
    a = 10
    __b = 50         #private variable
    
myObject1 = myClass1()
print(myObject1.a)      
# print(myObject1.__b)        #we cannot access the __b variable.

#How to access private variable......................................................

class myClass2:
    a = 10
    __b = 50         #private variable
    
    def display(self):
        return self.__b
    
myObject2 = myClass2()
print(myObject2.a)      
print(myObject2.display())    #Now we can access the __b variable.

#Private methods.....................................................................

class myClass3:
    def message1(self):         #public method
        print("Hello!")
    def __message2(self):       #private method
        print("Welcome!")
        
myObj1 = myClass3()
myObj1.message1()
# myObj1.__message2()         #we cannot access the __message2() method.

#How to access private method.........................................................

class myClass3:
    def message1(self):         #public method
        print("Hello!")
        self.__message2()
        
    def __message2(self):       #private method
        print("Welcome!")
        
myObj1 = myClass3()
myObj1.message1()
# myObj1.__message2()         