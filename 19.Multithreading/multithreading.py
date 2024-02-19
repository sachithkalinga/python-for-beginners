import threading
from time import sleep

def func1():
    for i in range(50):
        print("Good")
        sleep(0.3)

def func2():
    for i in range(50):
        print("Bye")
        sleep(0.3)

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
sleep(0.2)
t2.start()