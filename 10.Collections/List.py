
list1 = [3, 4, 6, 7, 8, 9, 10, 11]
list2 = ["n", "c", "r", "w", "q", "s"]
list3 = [3, 5, 2, "A", "f", "G", True, False, [2, 4, "A", True]]

list1[2] = 100                  # Change elements
print(list1)                    # [3, 4, 100, 7, 8, 9, 10, 11]

print(len(list1))               # List length

list2.insert(2, "APPLE")        # Insert elements
print(list2)                    # ['n', 'c', 'APPLE', 'r', 'w', 'q', 's']

list2.append(450)               # Insert elements last
print(list2)                    # ['n', 'c', 'APPLE', 'r', 'w', 'q', 's', 450]

list2.remove("n")               # Remove elements
print(list2)                    # ['c', 'APPLE', 'r', 'w', 'q', 's', 450]

list1.pop()                     # Remove last element
print(list1)                    # [3, 4, 100, 7, 8, 9, 10]

list1.sort()                    # Sort elements
print(list1)                    # [3, 4, 7, 8, 9, 10, 100]

list1.clear()                   # Clear elements
print(list1)

# del list1                       # Delete list
# print(list1)                    # NameError: name 'list1' is not defined

#..............................................................................................

a, b , c, d = [4, 2, 6, 7]
print(a, b, c, d)

x, y, *z = [4, 5, 2, 6, 7, 2, 4]
print(x)        # 4
print(y)        # 5
print(z)        # [2, 6, 7, 2, 4]

x, *y, z = [4, 5, 2, 6, 7, 2, 4]
print(x)        # 4
print(y)        # [5, 2, 6, 7, 2]
print(z)        # 4

#...............................................................................................

