
# Splitting strings.........................................................................

user = "Ann John Alex"
print(user.split())            # ['Ann', 'John', 'Alex']

address = "One Apple Park Way, Cupertino, CA 95014, United States"
print(address.split(","))


path = "apple.com/shop/buy-mac/imac"
print(path.split("/"))                       # ['apple.com', 'shop', 'buy-mac', 'imac']

split = path.split("/")
first_element = split[0]
print(first_element)                         # apple.com
print(first_element.split("."))              # ['apple', 'com']


# Update Strings.............................................................................

answer = "The answer is Canada"
update_answer = answer.replace("Canada", "USA")
print(update_answer)

#............................................................................................

youtube = "snoop"
fb = "dogg"

print("Subscribe " + youtube + fb)
print("Subscribe {}".format(youtube) + " {}".format(fb))
print(f"Subscribe {youtube} {fb}")
print("Subscribe",youtube,fb)

#Reverse string................................................................................

name = "Snoop Dogg"[::-1]
print(name)                 # ggoD poonS


#Remove whitespace from string...............................................................

name = "      John    "
print(name)
print(name.strip())