
x = "Ann's Car"
y = 'My Car'
z = 'John\'s Boat'

print(x)
print(y)
print(z)

#............................................................................................

p = "apple phones"

print(p.capitalize())       # Apple phones
print(p.upper())            # APPLE PHONES
print(p.lower())            # apple phones
print(p.title())            # Apple Phones  

print(p[0])                 # a
print(p[1])                 # p
print(p[2])                 # p

print(p[2:8])               # ple ph
print(p[2:])                # ple phones
print(p[:8])                # apple ph
print(p[:])                 # apple phones

print(p.replace('p', 'd'))  # addle dhones
print(p.split(" "))         # ['apple', 'phones']
print(p.split("h"))         # ['apple p', 'ones']

#Join elements................................................................................

a = "Jack Jill"
b = a.split(" ")
print(b)
c = " and ".join(b)         # Jack and Jill
print(c)