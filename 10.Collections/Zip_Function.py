
names = ["Ann", "John", "Kevin", "Gwen"]
age = [23, 34, 15, 38]

details = list(zip(names, age))
print(details)                  #[('Ann', 23), ('John', 34), ('Kevin', 15), ('Gwen', 38)]

details = tuple(zip(names, age))
print(details)                  #(('Ann', 23), ('John', 34), ('Kevin', 15), ('Gwen', 38))

details = set(zip(names, age))
print(details)                  #{('Kevin', 15), ('Ann', 23), ('Gwen', 38), ('John', 34)}

details = dict(zip(names, age))
print(details)                  #{'Ann': 23, 'John': 34, 'Kevin': 15, 'Gwen': 38}

#.............................................................................................
print("\n")

a = ["A", "B", "C", "D", "E"]
b = ["a", "b", "c", "d", "e"]
c = [1, 2, 3, 4, 5]

sum = list(zip(a,b,c))
print(sum)                      #[('A', 'a', 1), ('B', 'b', 2), ('C', 'c', 3), ('D', 'd', 4), ('E', 'e', 5)]

sum = tuple(zip(a,b,c))
print(sum)                      #(('A', 'a', 1), ('B', 'b', 2), ('C', 'c', 3), ('D', 'd', 4), ('E', 'e', 5))

sum = set(zip(a,b,c))           #{('C', 'c', 3), ('A', 'a', 1), ('B', 'b', 2), ('E', 'e', 5), ('D', 'd', 4)}
print(sum) 

# sum = dict(zip(a,b,c))        # Dictionary cannot use because key and value cannot be separate right
# print(sum) 

#Unzip collection................................................................................................
print("\n")

unzip = list(zip(*details))     # Unzip by * mark
print(unzip)                    #[('A', 'J', 'K', 'G'), ('n', 'o', 'e', 'w'), ('n', 'h', 'v', 'e')]