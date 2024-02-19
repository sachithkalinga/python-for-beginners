
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a/b)

except ZeroDivisionError as e:
    print("Cannot divide by 0", e)

except ValueError as e:
    print("Please input numbers", e)

except Exception as e:
    print("Something went wrong. ", e)
    
finally:
    print("Bye!")