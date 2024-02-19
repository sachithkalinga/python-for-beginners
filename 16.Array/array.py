"""
All value should be same type
"""

from array import *   # dont need array.array

"""
import array
a = array.array('I',[2, 5, 6, 2, 6, 7])

"""

a = array('I',[2, 5, 6, 2, 6, 7])         # I = Data type (Positive integer only)
print(a)

b = array('i',[-2, 5, -6, 2, 6, 7])       # i = Any integer
print(b)


x = array('i',[3, 9, 0, 5, 2, 1, 8])
print(x)

print("\n")
print(x[0])
print(x[-1])
print(x[1:3])
print(x[0:7:2])

print("\n")

x.append(600)               # Single value add last
print(x)

x.extend([200, 500, 300])   # Many value add last
print(x)

x.insert(2, 150)            # 150 value added to index[2]
print(x)

x.pop()                     # Remove last value
print(x)

x.pop(0)                    # Remove index[0] value
print(x)

x.remove(600)               # Remove value 600
print(x)

#Add arrays..........................................................................................
print("\n")

x = array("i",[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = array("i",[9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

z = x+y                     # x and y should be same data type
print(z)                    # array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

#....................................................................................................
print("\n")

ary = array("I", [3, 5, 2, 6, 1])
for i in ary:
    print(i)
