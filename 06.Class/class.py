class Car:
    def say():
        print("Hello")
        
car1 = Car()
car1.say()        #def say(self):   self needed

#.................................................................................

class Lap:
    def say(self, name):
        print("Hello " + name)
        
phone1 = Lap()
phone1.say("MSI") 

phone2 = Lap()
phone2.say("HP")

#Self keyword......................................................................

class Phone:
    ram = "12 GB"
    camera = "48 Mp"
    def say(self):
        
        self.display = "Gorilla glass"
        self.resolution = "4K"
        print("Hello ")
        
newPhone = Phone()
newPhone.say()

print(newPhone.ram)               #ram

print(newPhone.display)           #self.display
print(newPhone.resolution)        #self.resolution

