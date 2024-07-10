# Example 1: Basic arithmetic operations
addition = lambda x, y: x + y
subtraction = lambda x, y: x - y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y

print("Basic Arithmetic Operations:")
print("3 + 5 =", addition(3, 5))
print("8 - 3 =", subtraction(8, 3))
print("4 * 6 =", multiplication(4, 6))
print("10 / 2 =", division(10, 2))

# Example 2: Filtering even and odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
odd_numbers = filter(lambda x: x % 2 != 0, numbers)

print("\nFiltering Even and Odd Numbers:")
print("Even Numbers:", list(even_numbers))
print("Odd Numbers:", list(odd_numbers))

# Example 3: Mapping with lambda
squared_numbers = map(lambda x: x ** 2, numbers)
cubed_numbers = map(lambda x: x ** 3, numbers)

print("\nMapping Operations:")
print("Squared Numbers:", list(squared_numbers))
print("Cubed Numbers:", list(cubed_numbers))

# Example 4: Sorting a list of strings by their length
words = ['banana', 'apple', 'cherry', 'blueberry']
sorted_words = sorted(words, key=lambda x: len(x))

print("\nSorting by Length:")
print("Sorted Words:", sorted_words)

# Example 5: Using lambda with higher-order functions
def apply_operation(x, y, operation):
    return operation(x, y)

result1 = apply_operation(5, 3, lambda x, y: x * y)
result2 = apply_operation(10, 2, lambda x, y: x // y)

print("\nUsing Lambda with Higher-Order Functions:")
print("5 * 3 =", result1)
print("10 // 2 =", result2)

# Example 6: Conditional expressions with lambda
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print("\nConditional Expressions:")
print("Is 7 even or odd?", is_even(7))
print("Is 8 even or odd?", is_even(8))

# Example 7: Function factory with lambda
def function_factory(n):
    return lambda x: x * n

double = function_factory(2)
triple = function_factory(3)

print("\nFunction Factory:")
print("Double of 5:", double(5))
print("Triple of 5:", triple(5))

# Example 8: Using lambda to define default values in a dictionary
default_values = {'a': lambda: 0, 'b': lambda: 1, 'c': lambda: 2}
print("\nDefault Values in Dictionary:")
print("Value of 'a':", default_values['a']())
print("Value of 'b':", default_values['b']())
print("Value of 'c':", default_values['c']())

# Example 9: Filtering lists of dictionaries using lambda
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]
filtered_people = filter(lambda x: x['age'] > 30, people)

print("\nFiltering Lists of Dictionaries:")
print("People over 30:", list(filtered_people))

# Example 10: Using lambda to define custom sorting criteria
student_records = [
    {'name': 'Alice', 'grade': 'B'},
    {'name': 'Bob', 'grade': 'A'},
    {'name': 'Charlie', 'grade': 'C'}
]
sorted_students = sorted(student_records, key=lambda x: x['grade'])

print("\nCustom Sorting Criteria:")
print("Sorted Students by Grade:", sorted_students)

# Example 11: Combining lambda with built-in functions like max() and min()
max_number = max(numbers, key=lambda x: x % 3)
min_number = min(numbers, key=lambda x: abs(x - 5))

print("\nUsing Lambda with Built-in Functions:")
print("Max number with remainder 1 when divided by 3:", max_number)
print("Number closest to 5:", min_number)

# Example 12: Using lambda to handle exceptions in sorting
unsortable_list = [1, 2, 'a', 'b']
try:
    sorted_list = sorted(unsortable_list, key=lambda x: x)
    print("\nSorted List:", sorted_list)
except TypeError as e:
    print("\nError:", e)

# Example 13: Using lambda with zip() to transpose a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed_matrix = list(map(lambda x: list(x), zip(*matrix)))

print("\nTransposing a Matrix:")
for row in transposed_matrix:
    print(row)

# Example 14: Using lambda with reduce() to find the product of a list of numbers
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)

print("\nUsing Lambda with reduce():")
print("Product of Numbers:", product)

# Example 15: Using lambda with dictionary comprehensions
squared_values = {x: x ** 2 for x in range(1, 6)}

print("\nUsing Lambda with Dictionary Comprehensions:")
print("Squared Values:", squared_values)

# Example 16: Using lambda with set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set(filter(lambda x: x in set2, set1))

print("\nUsing Lambda with Set Operations:")
print("Intersection of Sets:", intersection)

# Example 17: Using lambda with string manipulations
names = ['Alice', 'Bob', 'Charlie']
uppercase_names = list(map(lambda x: x.upper(), names))

print("\nUsing Lambda with String Manipulations:")
print("Uppercase Names:", uppercase_names)

# Example 18: Using lambda with list comprehensions
squares = [x ** 2 for x in range(1, 6)]
even_squares = [x for x in squares if x % 2 == 0]

print("\nUsing Lambda with List Comprehensions:")
print("Squares:", squares)
print("Even Squares:", even_squares)

# Example 19: Using lambda with filterfalse() to get elements not satisfying a condition
from itertools import filterfalse
odd_numbers = list(filterfalse(lambda x: x % 2 == 0, numbers))

print("\nUsing Lambda with filterfalse():")
print("Odd Numbers:", odd_numbers)

# Example 20: Using lambda with any() and all() to check conditions in a list
contains_even = any(map(lambda x: x % 2 == 0, numbers))
all_even = all(map(lambda x: x % 2 == 0, numbers))

print("\nUsing Lambda with any() and all():")
print("List contains even numbers:", contains_even)
print("All numbers are even:", all_even)
