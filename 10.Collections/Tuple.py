x = (3, 5, 6, 7, 8, 9, 10, 1, 2, 3)
y = (3, 4.5, "a", "G", True)

# x[2] = 50             # Cannot change elements
                        # TypeError: 'tuple' object does not support item assignment

z = x + y
print(z)                # (3, 5, 6, 7, 8, 9, 10, 1, 2, 3, 3, 4.5, 'a', 'G', True)

print(max(x))           # 10
print(min(x))           # 1

# del z                   # Delete tuple
# print(z)                # NameError: name 'z' is not defined

#Tuple is speed than list.................................................................

import timeit

x = [4,56,8,4,32,45,89,43,23]

print(max(x))
print(min(x))

list_time = timeit.timeit(stmt="[4,6,8,4,2,4,6,8,5,4]")
tuple_time = timeit.timeit(stmt="(4,6,8,4,2,4,6,8,5,4)")
set_time = timeit.timeit(stmt="{4,6,8,4,2,4,6,8,5,4}")

print(list_time)
print(tuple_time)
print(set_time)