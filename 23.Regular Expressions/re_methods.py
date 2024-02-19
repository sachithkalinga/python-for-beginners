import re

#findall()...............................................................................
txt = "This is python2022@gmail.com and it is xyz@gmail.com"

a = re.findall("\w+@gmail.com", txt)        # Filter e-mails
print(a)                                    # ['python2022@gmail.com', 'xyz@gmail.com']

a = re.findall("a\w+", txt)                 # 
print(a)                                    # ['ail', 'and', 'ail']

a = re.findall("\w+a\w+", txt)              # 
print(a)                                    # ['gmail', 'gmail']

a = re.findall("\w*a\w+", txt)              # 
print(a)                                    # ['gmail', 'and', 'gmail']

a = re.findall("\w?a\w+", txt)              # 
print(a)                                    # ['mail', 'and', 'mail']

#search()................................................................................

phr = "Python is a great final language"

b = re.search("Python", phr)
print(b)                                    # <re.Match object; span=(0, 6), match='Python'>

b = re.search("\wython", phr)               # P or p
print(b)                                    # <re.Match object; span=(0, 6), match='Python'>

c = re.search("f\w{4}", phr)                # <re.Match object; span=(18, 23), match='final'>
print(c)
print(c.group())                            # final
print(c.span())                             # (18, 23)
print(c.string)                             # Python is a great final language

#split().................................................................................

phr = "Python is a great final language"

print(phr.split(" "))                       # ['Python', 'is', 'a', 'great', 'final', 'language']
print(phr.split(" ",2))                     # ['Python', 'is', 'a great final language']

print(re.split("\s",phr))                   # Same as print(phr.split(" "))

#sub()...................................................................................

phr = "Python is a great final language"

y = re.sub("\s","@",phr)                    # White spaces replace with @
print(y)                                    # Python@is@a@great@final@language

y = re.sub("\s","@",phr, 2)                 # First two white spaces replace with @
print(y)                                    # Python@is@a great final language

y = re.sub("f\w{4}","first",phr)            # final word replace with first
print(y)                                    # Python is a great first language