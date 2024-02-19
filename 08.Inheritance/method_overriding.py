
class Animal:
    def leg(self):
        print("4 Legs")
        
class Spider(Animal):
    def skin(self):
        print("Black")
        
    def leg(self):              #leg method overridden
        print("8 Legs")
        
myObj = Spider()
myObj.skin()
myObj.leg()