
for ai in range(5):
    print(f"Range is {ai}")

list = [1,2,4,6,8,9,10]
for number in list:
    print(f"List is {number}")


tp = ("Ann", "Snoop", "DMX")
for singer in tp:
    print(f"Singer is {singer}")

num_rows = 5
for i in range(0, num_rows):
	for j in range(0, num_rows-i-1):
		print(end=" ")
	for j in  range(0, i+1):
		print("*", end=" ")
	print()

#......................................................................................

nameA = ["A","B","C","D","E","F","G","H","I"]

index = 0
for name in nameA:
	print(index, name)
	index += 1
print("\n")

for index, name in enumerate(nameA, start=1):   # Same as above code
	print(index, name)
print("\n")

#.......................................................................................


for x in range(1,8):
    if x==3:
        continue			# Continue is skip the below code
    print(x)


for x in range(1,8):
    if x==3:
        break				# Break will stop the loop
    print(x)