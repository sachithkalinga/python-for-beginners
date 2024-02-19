"""
r   ---->   read only
w   ---->   write only
a   ---->   append
w+  ---->   read and write
"""

x = open('21.File Handling/text.txt', 'r')

x = open(r'21.File Handling\text.txt', 'r')    # \ can use in url by adding r in start

print(x.readline())         # read line by line
print(x.readline())
print("\n")
print(x.read())             # read all left line

x.close()                   # Close file

#...................................................................................................
print("\n")

with open("21.File Handling/sample.txt", "r") as y:     # Atomically close file

    print(y.readline())
    print(y.readline())
    print(y.readline(), end='')     # Remove empty line
    print(y.readline())
    print(y.readline(), end='')     # Remove empty line
    print(y.readline())
    print(y.readline())

    print(y.readlines())
