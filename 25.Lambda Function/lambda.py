# Define a lambda function that returns the square of a number
square = lambda x: x ** 2

# Call the lambda function with an argument
result = square(5)

# Print the result
print(result)


###########################################################################################################
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use a lambda function with the `map` function to double each number in the list
doubled_numbers = list(map(lambda x: x * 2, numbers))

# Print the doubled numbers
print(doubled_numbers)
