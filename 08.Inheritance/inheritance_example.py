
class Fruits:
    number_of_items = None
    unite_price = None
    def set_value(self, x, y):
        self.number_of_items = x
        self.unite_price = y
        
        
class Apple(Fruits):
    def price(self):
        print("For apple ", self.number_of_items*self.unite_price)
        
class Banana(Fruits):
    def price(self):
        print("For apple ", self.number_of_items*self.unite_price)
        
class Mango(Fruits):
    def price(self):
        print("For apple ", self.number_of_items*self.unite_price)
        

myObj1 = Apple()
myObj2 = Banana()
myObj3 = Mango()

myObj1.set_value(12, 40)
myObj2.set_value(20, 50)
myObj3.set_value(18, 78)

myObj1.price()
myObj2.price()
myObj3.price()