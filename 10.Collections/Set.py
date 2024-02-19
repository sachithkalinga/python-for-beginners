
set = {4, 5, 2, 3, 1, 4, 5, 5, 1}

print(set)          # {1, 2, 3, 4, 5}
                    # No order. cant access by index. eg: x[1]

print(len(set))     # 5     Duplicate elements not counted


x = {4,56,8,4}

x.add(2)            # Add 1 element
print(x)            # {56, 8, 2, 4}

x.update([4,4,412,34,21,22])        # Add many elements
print(x)                            # {2, 34, 4, 8, 21, 22, 56, 412}

x.remove(34)                        # Remove one element
print(x)                            # {2, 4, 8, 21, 22, 56, 412}

x.clear()                           # Clear set
print(x)                            # set()

# del x                               # Delete set

print(type(x))                      # <class 'set'>

#Intersection and Union functions.............................................................

set1 = {4,3,5,3,2,5,5,4,3,2,5,8,9,5,4}
set2 = {4,7,4,2,5,7,9,9,7,6,5,4,23,2,5,8,0,2}

print(set1 & set2)                  # {2, 4, 5, 8, 9}
print(set1.intersection(set2))      # {2, 4, 5, 8, 9}

print(set1 | set2)                  # {0, 2, 3, 4, 5, 6, 7, 8, 9, 23}
print(set1.union(set2))             # {0, 2, 3, 4, 5, 6, 7, 8, 9, 23}
