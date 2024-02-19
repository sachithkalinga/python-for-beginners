
#iter() and next() functions.....................................................................

lst = {3, 5, 8}

itr = iter(lst)
print(next(itr))
print(next(itr))
print(next(itr))

#...............................................................................................
print("\n")

x = {2, 5, 2, 6, 7, 4, 8}

itr = iter(x)

while True:
    try:
        print(next(itr))
    except StopIteration:
        break