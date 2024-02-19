
import re

words = "Hello @ 2022..!"

y = re.findall(".", words)            # All elements
print(y)                            # ['H', 'e', 'l', 'l', 'o', ' ', '@', ' ', '2', '0', '2', '2', '.', '.', '!']

y = re.findall("\d", words)           # Digits only
print(y)                            # ['2', '0', '2', '2']

y = re.findall("\w", words)           # A-Z, a-z, 0-9
print(y)                            # ['H', 'e', 'l', 'l', 'o', '2', '0', '2', '2']

y = re.findall("\W", words)           # Not \w
print(y)                            # [' ', '@', ' ', '.', '.', '!'] 

y = re.findall("\s", words)           # White spaces
print(y)                            # [' ', ' ']

y = re.findall("\S", words)           # Not \s
print(y)                            # ['H', 'e', 'l', 'l', 'o', '@', '2', '0', '2', '2', '.', '.', '!']

#...................................................................................................................
print("\n")

phr = "Hello Regular Expressions year22..!"

z = re.findall("\w\w\w\w\w", phr)
print(z)                            # ['Hello', 'Regul', 'Expre', 'ssion', 'year2']

z = re.findall("\w{4}\d{2}", phr)   # 
print(z)                            # ['year22']

z = re.findall("\w{3}", phr)        # 
print(z)                            # ['Hel', 'Reg', 'ula', 'Exp', 'res', 'sio', 'yea', 'r22']

z = re.findall("\w{2,3}", phr)      # {min,max}
print(z)                            # ['Hel', 'lo', 'Reg', 'ula', 'Exp', 'res', 'sio', 'ns', 'yea', 'r22']

z = re.findall("\w+", phr)          # 1 or more occurrence
print(z)                            # ['Hello', 'Regular', 'Expressions', 'year22']

z = re.findall("\w*", phr)          # 0 or more occurrence
print(z)                            # ['Hello', '', 'Regular', '', 'Expressions', '', 'year22', '', '', '', '']

z = re.findall("\w?", phr)          # 0 or 1 occurrence
print(z)                            # ['H', 'e', 'l', 'l', 'o', '', 'R', 'e', 'g', 'u', 'l', 'a', 'r', '', 'E', 'x', 'p', 'r', 'e', 's', 's', 'i', 'o', 'n', 's', '', 'y', 'e', 'a', 'r', '2', '2', '', '', '', '']

z = re.findall("^\w+", phr)         # ^ Start
print(z)                            # ['Hello']

z = re.findall("\W+$", phr)         # $ End
print(z)                            # ['..!']