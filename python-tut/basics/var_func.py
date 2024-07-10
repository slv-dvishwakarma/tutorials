# Understand what is a variable and function, how to define and use it . Extra good to have how stored in RAM 
# Without using a function
# We have two numbers stored in variables
a1 = 5
b1 = 3

# First addition
result1 = a1 + b1

# Second addition with new variables
a2 = 2
b2 = 7
result2 = a2 + b2

# Third addition with new variables
a3 = 9
b3 = 8
result3 = a3 + b3

# Print the results
print("Result of first addition:", result1)  # Output: Result of first addition: 8
print("Result of second addition:", result2)  # Output: Result of second addition: 8
print("Result of third addition:", result3)  # Output: Result of third addition: 8

# Using a function
# Define a function called add_numbers
# Using a function
# Define a function called add_numbers
def add_numbers(a, b):
    # Inside the function, add the two numbers and return the result
    return a + b

# Print the results
print("Result of first addition using function:", add_numbers(5,3))  # Output: Result of first addition using function: 8
print("Result of second addition using function:", add_numbers(2,7))  # Output: Result of second addition using function: 8
print("Result of third addition using function:", add_numbers(9,8))  # Output: Result of third addition using function: 8

# TODO : params , repetion, questionaire , argument ensure one understand , also one showld understand its store in RAM app, ... Can skip for now but extra good to have

