# Example 1: Simple if-else statement
x = 10
if x > 0:
    print("x is positive")
else:
    print("x is non-positive")

# Example 2: Nested if-else statement
y = 20
if y > 0:
    print("y is positive")
    if y % 2 == 0:
        print("y is even")
    else:
        print("y is odd")
else:
    print("y is non-positive")

# Example 3: if-elif-else ladder
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

# Example 4: Simple while loop
num = 5
while num > 0:
    print(num)
    num -= 1

# Example 5: while loop with break statement
num = 5
while num > 0:
    print(num)
    if num == 3:
        break
    num -= 1

# Example 6: while loop with continue statement
num = 5
while num > 0:
    num -= 1
    if num == 3:
        continue
    print(num)

# Example 7: while loop with else block
num = 5
while num > 0:
    print(num)
    num -= 1
else:
    print("Loop completed without break")

# Example 8: while loop with if-else inside
num = 5
while num > 0:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
    num -= 1

# Example 9: if-else with multiple conditions
x = 10
if x > 5 and x < 15:
    print("x is between 5 and 15")

# Example 10: if statement with logical operators
y = 20
if y > 10 or y % 2 == 0:
    print("y is greater than 10 or even")

# Example 11: if statement with not operator
z = 30
if not z == 0:
    print("z is not zero")

# Example 12: if statement with in operator
word = "hello"
if 'e' in word:
    print("Letter 'e' found in word")

# Example 13: if statement with not in operator
if 'z' not in word:
    print("Letter 'z' not found in word")

# Example 14: if-else with string comparison
str1 = "hello"
str2 = "world"
if str1 == str2:
    print("Strings are equal")
else:
    print("Strings are not equal")

# Example 15: if-else with list comparison
list1 = [1, 2, 3]
list2 = [1, 2, 3]
if list1 == list2:
    print("Lists are equal")
else:
    print("Lists are not equal")

# Example 16: if-else with tuple comparison
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
if tuple1 == tuple2:
    print("Tuples are equal")
else:
    print("Tuples are not equal")

# Example 17: if-else with dictionary comparison
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 2}
if dict1 == dict2:
    print("Dictionaries are equal")
else:
    print("Dictionaries are not equal")

# Example 18: if-else with set comparison
set1 = {1, 2, 3}
set2 = {1, 2, 3}
if set1 == set2:
    print("Sets are equal")
else:
    print("Sets are not equal")

# Example 19: if-else with mixed data type comparison
mixed1 = [1, 2, 3]
mixed2 = {1, 2, 3}
if mixed1 == mixed2:
    print("Mixed data types are equal")
else:
    print("Mixed data types are not equal")

# Example 20: Using if-elif-else with multiple conditions
num = 25
if num > 0 and num < 10:
    print("Number is between 0 and 10")
elif num > 10 and num < 20:
    print("Number is between 10 and 20")
else:
    print("Number is greater than or equal to 20")

# Example 21: Using break in a nested loop
for i in range(5):
    for j in range(5):
        if j == 3:
            break
        print(f"({i}, {j})")

# Example 22: Using continue in a nested loop
for i in range(5):
    for j in range(5):
        if j == 3:
            continue
        print(f"({i}, {j})")

# Example 23: Using if-else with input
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Example 24: Using if-else with string formatting
name = "Alice"
if name.startswith("A"):
    print(f"{name} starts with 'A'")
else:
    print(f"{name} does not start with 'A'")

# Example 25: Using if-else with a function
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print("Is 10 even?", is_even(10))

# Example 26: Using if-else with file operations
file_name = "example.txt"
try:
    with open(file_name, 'r') as file:
        data = file.read()
    print(f"File {file_name} opened successfully.")
except FileNotFoundError:
    print(f"File {file_name} does not exist.")

# Example 27: Using if-else with error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
else:
    print("No error occurred")

# Example 28: Using if-else with multiple comparisons
x, y, z = 10, 20, 30
if x < y < z:
    print("x is less than y, and y is less than z")
else:
    print("x is not less than y, and y is not less than z")

# Example 29: Using if-else with ternary operator
a = 5
b = 10
min_value = a if a < b else b
print("Minimum value:", min_value)

# Example 30: Using if-else with list comprehension
numbers = [1, 2, 3, 4, 5]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# Example 31: Using while loop with conditional expression
num = 5
while num > 0:
    print(num)
    num -= 1 if num != 3 else 2

# Example 32: Using break with a for loop
for i in range(10):
    if i == 5:
        print("Breaking at", i)
        break
    print(i)

# Example 33: Using continue with a for loop
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Example 34: Using else with a for loop
for i in range(5):
    print(i)
else:
    print("Loop completed without break")

# Example 35: Using if-else with exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
finally:
    print("Finally block executed")

# Example 36: Using break in nested loops
for i in range(3):
    for j in range(3):
        if j == 2:
            print("Breaking inner loop at", j)
            break
        print(f"({i}, {j})")

# Example 37: Using continue in nested loops
for i in range(3):
    for j in range(3):
        if j == 1:
            print("Continuing inner loop at", j)
            continue
        print(f"({i}, {j})")

# Example 38: Using else with nested loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
    else:
        print("Inner loop completed without break")
else:
    print("Outer loop completed without break")

# Example 39: Using if-else with range and list comprehension
numbers = [x for x in range(10) if x % 2 == 0]
print("Even numbers from 0 to 9:", numbers)

# Example 40: Using while loop with multiple conditions
num = 10
while num > 0 and num % 2 == 0:
    print(num)
    num -= 2
