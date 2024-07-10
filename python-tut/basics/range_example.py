# Example 1: range with one argument (stop)
for i in range(5):
    print(i)

# Example 2: range with two arguments (start, stop)
for i in range(2, 6):
    print(i)

# Example 3: range with three arguments (start, stop, step)
for i in range(1, 10, 2):
    print(i)

# Example 4: using range in list
my_list = list(range(5))
print("List using range:", my_list)

# Example 5: using range in tuple
my_tuple = tuple(range(1, 6))
print("Tuple using range:", my_tuple)

# Example 6: using range in set
my_set = set(range(3, 9, 2))
print("Set using range:", my_set)

# Example 7: using range in dictionary (with comprehension)
my_dict = {x: x**2 for x in range(1, 5)}
print("Dictionary using range:", my_dict)

# Example 8: iterating over range in reverse order
for i in range(10, 0, -2):
    print(i)

# Example 9: using negative step with range
reversed_list = list(range(10, 0, -1))
print("Reversed list using negative step:", reversed_list)

# Example 10: checking if a number is in a range
if 5 in range(1, 10):
    print("5 is in the range (1, 10)")

# Example 11: checking if a number is not in a range
if 15 not in range(1, 10):
    print("15 is not in the range (1, 10)")

# Example 12: combining range with len function
my_string = "hello"
for i in range(len(my_string)):
    print(my_string[i])

# Example 13: using range to generate indices for nested loops
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")

# Example 14: using range to generate arithmetic progression
arithmetic_progression = [x * 2 for x in range(1, 6)]
print("Arithmetic progression:", arithmetic_progression)

# Example 15: using range with step 0 (Error)
try:
    for i in range(1, 5, 0):
        print(i)
except ValueError:
    print("Step cannot be zero")

# Example 16: using range with negative stop and positive step
for i in range(-10, 0, 2):
    print(i)

# Example 17: using range with negative start and negative stop
for i in range(-5, -10, -1):
    print(i)

# Example 18: using range with zero start and non-zero stop
for i in range(0, 5):
    print(i)

# Example 19: using range with non-zero start and zero stop (Empty range)
empty_range = range(5, 5)
print("Empty range:", list(empty_range))

# Example 20: using range with non-integer arguments
for i in range(1.5, 5.5):
    print(i)

# Example 21: generating prime numbers using range
primes = [x for x in range(2, 50) if all(x % y != 0 for y in range(2, int(x**0.5) + 1))]
print("Prime numbers less than 50:", primes)

# Example 22: using range to iterate over ASCII values
for i in range(ord('A'), ord('Z') + 1):
    print(chr(i), end=' ')

# Example 23: using range with step greater than stop
reversed_list = list(range(10, 0, -2))
print("Reversed list using step greater than stop:", reversed_list)

# Example 24: using range with float step
float_range = [x for x in range(1, 10, 0.5)]
print("Range with float step:", float_range)

# Example 25: using range with expressions in arguments
x = 2
y = 5
for i in range(x + 1, y * 2, x):
    print(i)

# Example 26: using range with variables in arguments
start = 2
stop = 6
step = 2
for i in range(start, stop, step):
    print(i)

# Example 27: using range with negative step and smaller start than stop
reversed_list = list(range(-5, -10, -1))
print("Reversed list using negative step and smaller start than stop:", reversed_list)

# Example 28: using range with variables and expressions in arguments
start = 3
stop = 8
for i in range(start, stop, stop - start):
    print(i)

# Example 29: using range with negative step and larger start than stop
reversed_list = list(range(-5, -10, -1))
print("Reversed list using negative step and larger start than stop:", reversed_list)

# Example 30: using range with negative step and negative stop
reversed_list = list(range(-10, -20, -2))
print("Reversed list using negative step and negative stop:", reversed_list)
