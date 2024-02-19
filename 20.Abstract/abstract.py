from abc import ABC, abstractmethod

class Phone(ABC):
    @abstractmethod
    def func(self):
        pass

# obj1 = Phone()       # Abstract class cannot create objects

class Samsung(Phone):
    def func(self):
        pass

obj2 = Samsung()