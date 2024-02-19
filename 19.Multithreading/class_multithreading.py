from threading import *
from time import sleep

class A(Thread):                # Inherit Thread class
    def run(self,):             # Should be run because the Thread class
        for i in range(5):
            print("Hello", current_thread().getName())
            sleep(1)

class B(Thread):                 # Inherit Thread class
    def run(self,):              # Should be run because the Thread class
        for i in range(5):
            print("World!", current_thread().getName())
            sleep(1)


myObjA = A()
myObjB = B()
myObjA.start()
sleep(0.2)
myObjB.start()

myObjA.join()       # Bye command execute final
myObjB.join()

print("Bye! ", current_thread().getName())