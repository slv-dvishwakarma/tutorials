# Example 1: Defining a simple function
def greet():
    """Function to print a simple greeting"""
    print("Hello, world!")

greet()

# Example 2: Function with parameters
def greet_with_name(name):
    """Function to greet with a specified name"""
    print("Hello,", name)

greet_with_name("Alice")

# Example 3: Function with default parameter value
def greet_with_default(name="world"):
    """Function to greet with a default or specified name"""
    print("Hello,", name)

greet_with_default()
greet_with_default("Bob")

# Example 4: Function with return value
def add(x, y):
    """Function to add two numbers"""
    return x + y

result = add(3, 5)
print("Result of addition:", result)

# Example 5: Function with multiple return values
def divide(x, y):
    """Function to perform integer division and return quotient and remainder"""
    quotient = x // y
    remainder = x % y
    return quotient, remainder

q, r = divide(10, 3)
print("Quotient:", q)
print("Remainder:", r)

# Example 6: Function with variable number of arguments (*args)
def sum_all(*args):
    """Function to sum all input numbers"""
    total = 0
    for num in args:
        total += num
    return total

print("Sum of all numbers:", sum_all(1, 2, 3, 4, 5))

# Example 7: Function with keyword arguments (**kwargs)
def print_info(**kwargs):
    """Function to print information with keyword arguments"""
    for key, value in kwargs.items():
        print(key, ":", value)

print_info(name="Alice", age=30, city="Wonderland")

# Example 8: Function with both *args and **kwargs
def mixed_arguments(arg1, arg2, *args, **kwargs):
    """Function with mixed positional and keyword arguments"""
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("Additional positional arguments:", args)
    print("Additional keyword arguments:", kwargs)

mixed_arguments(1, 2, 3, 4, name="Alice", age=30)

# Example 9: Nested functions
def outer_function():
    """Outer function with a nested inner function"""
    print("Outer function")

    def inner_function():
        """Inner function"""
        print("Inner function")

    inner_function()

outer_function()

# Example 10: Returning a function from another function
def outer_function():
    """Outer function returning an inner function"""
    def inner_function():
        """Inner function"""
        print("Inner function")
    return inner_function

fn = outer_function()
fn()

# Example 11: Function as a parameter to another function
def greet():
    """Function to print a greeting"""
    print("Hello, world!")

def call_function(func):
    """Function to call another function passed as an argument"""
    func()

call_function(greet)

# Example 12: Using lambda functions
add = lambda x, y: x + y
print("Result of addition:", add(3, 5))

# Example 13: Using lambda functions in sorted()
names = ["Alice", "Bob", "Charlie"]
sorted_names = sorted(names, key=lambda x: len(x))
print("Sorted names:", sorted_names)

# Example 14: Using lambda functions in map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

# Example 15: Using lambda functions in filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Example 16: Using lambda functions in reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product)

# Example 17: Function annotations
def add(x: int, y: int) -> int:
    """Function with type annotations for parameters and return value"""
    return x + y

print("Result of addition:", add(3, 5))

# Example 18: Accessing function annotations
print("Annotations for add function:", add.__annotations__)

# Example 19: Recursion
def factorial(n):
    """Recursive function to calculate factorial"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# Example 20: Memoization
def fib(n, memo={}):
    """Recursive Fibonacci function with memoization"""
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

print("Fibonacci sequence:", [fib(i) for i in range(1, 11)])

# Example 21: Function with side effects
def modify_list(lst):
    """Function to modify a list (side effect)"""
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print("Modified list:", my_list)

# Example 22: Function with global variables
global_var = 5

def modify_global():
    """Function to modify a global variable"""
    global global_var
    global_var = 10

modify_global()
print("Global variable:", global_var)

# Example 23: Function with nonlocal variables
def outer():
    """Function with a nonlocal variable"""
    var = 10

    def inner():
        nonlocal var
        var = 20

    inner()
    print("Inner modified var:", var)

outer()

# Example 24: Decorators without arguments
def my_decorator(func):
    """Decorator function without arguments"""
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    """Function to say hello"""
    print("Hello!")

say_hello()

# Example 25: Decorators with arguments
def repeat(n):
    """Decorator function with arguments"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    """Function to greet with a name"""
    print("Hello,", name)

greet("Alice")

# Example 26: Class as a decorator
class MyDecorator:
    """Class used as a decorator"""
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before function call")
        self.func(*args, **kwargs)
        print("After function call")

@MyDecorator
def say_hello():
    """Function to say hello"""
    print("Hello!")

say_hello()

# Example 27: Chaining decorators
def decorator1(func):
    """First decorator function"""
    def wrapper():
        print("Decorator 1 before function call")
        func()
        print("Decorator 1 after function call")
    return wrapper

def decorator2(func):
    """Second decorator function"""
    def wrapper():
        print("Decorator 2 before function call")
        func()
        print("Decorator 2 after function call")
    return wrapper

@decorator1
@decorator2
def say_hello():
    """Function to say hello"""
    print("Hello!")

say_hello()

# Example 28: Decorator with arguments
def repeat(n):
    """Decorator function with arguments"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    """Function to greet with a name"""
    print("Hello,", name)

greet("Alice")

# Example 29: Using functools.wraps to preserve function metadata
import functools

def my_decorator(func):
    """Decorator function using functools.wraps"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function call")
        func(*args, **kwargs)
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    """Function to say hello"""
    print("Hello!")

print("Function name:", say_hello.__name__)
print("Function docstring:", say_hello.__doc__)

# Example 30: Decorator with arguments using functools
def repeat(n):
    """Decorator function with arguments using functools"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    """Function to greet with a name"""
    print("Hello,", name)

greet("Alice")

# Example 31: Using functools.partial to create partial functions
import functools

def power(base, exponent):
    """Function to calculate power of a number"""
    return base ** exponent

square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)

print("Square of 5:", square(5))
print("Cube of 5:", cube(5))

# Example 32: Using generators
def fibonacci(n):
    """Generator function to generate Fibonacci sequence"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Fibonacci sequence:", list(fibonacci(10)))

# Example 33: Using generator expressions
even_numbers = (x for x in range(10) if x % 2 == 0)
print("Even numbers:", list(even_numbers))

# Example 34: Using itertools module for iterators
import itertools

# Infinite iterator
counter = itertools.count(start=1, step=2)
print("First 5 odd numbers:", list(itertools.islice(counter, 5)))

# Example 35: Using itertools.cycle
colors = ['red', 'green', 'blue']
color_cycle = itertools.cycle(colors)
print("Next 5 colors:", [next(color_cycle) for _ in range(5)])

# Example 36: Using itertools.chain
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
combined = itertools.chain(letters, numbers)
print("Combined list:", list(combined))

# Example 37: Using itertools.permutations
perms = itertools.permutations([1, 2, 3])
print("Permutations:", list(perms))

# Example 38: Using itertools.combinations
combs = itertools.combinations([1, 2, 3], 2)
print("Combinations:", list(combs))

# Example 39: Using itertools.product
prod = itertools.product('AB', repeat=2)
print("Product:", list(prod))

# Example 40: Using itertools.groupby
data = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
grouped_data = itertools.groupby(data, key=lambda x: x[0])
print("Grouped data:")
for key, group in grouped_data:
    print(key, list(group))

# Example 41: Using functools.reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product)

# Example 42: Using functools.partial to create partial functions
from functools import partial

def power(base, exponent):
    """Function to calculate power of a number"""
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print("Square of 5:", square(5))
print("Cube of 5:", cube(5))

# Example 43: Using functools.lru_cache for caching results
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    """Recursive Fibonacci function with memoization"""
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print("Fibonacci sequence:", [fib(i) for i in range(10)])

# Example 44: Using functools.partialmethod to create partial methods
import functools

class MyClass:
    """Class with a partial method"""
    def __init__(self, x):
        self.x = x

    def multiply(self, y):
        """Method to multiply with another number"""
        return self.x * y

    multiply_by_2 = functools.partialmethod(multiply, 2)

obj = MyClass(5)
print("Result of multiply_by_2:", obj.multiply_by_2())

# Example 45: Using generators to create infinite sequences
def fibonacci():
    """Generator function to generate Fibonacci sequence"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_seq = fibonacci()
print("First 10 Fibonacci numbers:", [next(fib_seq) for _ in range(10)])

# Example 46: Using generators to generate data lazily
def square_numbers(nums):
    """Generator function to square a list of numbers"""
    for num in nums:
        yield num ** 2

nums = [1, 2, 3, 4, 5]
squared_nums = square_numbers(nums)
print("Squared numbers:", list(squared_nums))

# Example 47: Using generators to process large datasets efficiently
def process_file(filename):
    """Generator function to process a large file"""
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# Example 48: Using generators to implement infinite iterators
def natural_numbers():
    """Generator function to generate natural numbers"""
    num = 1
    while True:
        yield num
        num += 1

# Example 49: Using generators for co-routines
def co_routine():
    """Generator function for a co-routine"""
    value = yield
    while value:
        print("Received:", value)
        value = yield

# Example 50: Using generators to implement custom sequence types
class FibonacciSequence:
    """Custom sequence type using a generator"""
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

fib_sequence = FibonacciSequence()
print("First 10 Fibonacci numbers:", [next(fib_sequence) for _ in range(10)])
