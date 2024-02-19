
import os

print(os.getcwd())

os.chdir(r"C:\Users\Sachith\Desktop\Python\Assets")   # \
print(os.getcwd())

print(os.listdir())

# os.mkdir("Hello")

# os.rmdir("Hello/Python")

# os.rename("for os module.txt", "welcome.txt")

a = list(dir(os))

for i in a:
    print(i)