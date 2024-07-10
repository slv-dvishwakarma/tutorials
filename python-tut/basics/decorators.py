# Example 1: Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Example 2: Decorator with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print("Hello,", name)

greet("Alice")

# Example 3: Class as a decorator
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before function call")
        self.func(*args, **kwargs)
        print("After function call")

@MyDecorator
def say_hello():
    print("Hello!")

say_hello()

# Example 4: Chaining decorators
def decorator1(func):
    def wrapper():
        print("Decorator 1 before function call")
        func()
        print("Decorator 1 after function call")
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 before function call")
        func()
        print("Decorator 2 after function call")
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()

# Example 5: Decorator with arguments using functools
import functools

def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print("Hello,", name)

greet("Alice")

# Example 6: Using functools.wraps to preserve function metadata
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function call")
        func(*args, **kwargs)
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    """A function that says hello"""
    print("Hello!")

print("Function name:", say_hello.__name__)
print("Function docstring:", say_hello.__doc__)

# Example 7: Using functools.partial to create partial functions
def power(base, exponent):
    return base ** exponent

square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)

print("Square of 5:", square(5))
print("Cube of 5:", cube(5))

# Example 8: Using functools.partialmethod to create partial methods
class MyClass:
    def __init__(self, x):
        self.x = x

    def multiply(self, y):
        return self.x * y

    multiply_by_2 = functools.partialmethod(multiply, 2)

obj = MyClass(5)
print("Result of multiply_by_2:", obj.multiply_by_2())

# Example 9: Using decorators for caching results
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print("Fibonacci sequence:", [fib(i) for i in range(10)])

# Example 10: Using decorators for class-level caching
class MyClass:
    @lru_cache(maxsize=None)
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

obj = MyClass()
print("Fibonacci sequence (cached):", [obj.fib(i) for i in range(10)])

# Example 11: Using decorators for timing functions
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci sequence:", [fibonacci(i) for i in range(10)])

# Example 12: Using decorators for logging
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

print("Result of addition:", add(3, 5))

# Example 13: Using decorators for authentication
def authenticate(func):
    def wrapper(*args, **kwargs):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "admin" and password == "123":
            return func(*args, **kwargs)
        else:
            print("Authentication failed")
    return wrapper

@authenticate
def secret_function():
    print("Secret function executed")

secret_function()

# Example 14: Using decorators for memoization
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

@memoize
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorial of 5:", factorial(5))

# Example 15: Using decorators for retrying functions
import random

def retry(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempts+1} failed:", e)
                    attempts += 1
            raise Exception("Maximum number of attempts reached")
        return wrapper
    return decorator

@retry(max_attempts=3)
def possibly_failing_function():
    if random.random() < 0.5:
        raise ValueError("Random error")
    return "Success"

print(possibly_failing_function())

# Example 16: Using decorators for validating function arguments
def validate(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) != len(types):
                raise TypeError(f"Expected {len(types)} arguments, got {len(args)}")
            for arg, arg_type in zip(args, types):
                if not isinstance(arg, arg_type):
                    raise TypeError(f"Expected {arg_type}, got {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate(int, int)
def add(x, y):
    return x + y

print("Result of addition:", add(3, 5))

# Example 17: Using decorators for enforcing function preconditions
def preconditions(*conditions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for condition in conditions:
                if not condition(*args, **kwargs):
                    raise ValueError("Precondition failed")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def positive_numbers(*args):
    return all(arg > 0 for arg in args)

@preconditions(positive_numbers)
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print("Result of multiplication:", multiply(2, 3, 4))

# Example 18: Using decorators for enforcing function postconditions
def postconditions(*conditions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for condition in conditions:
                if not condition(result):
                    raise ValueError("Postcondition failed")
            return result
        return wrapper
    return decorator

def is_even(result):
    return result % 2 == 0

@postconditions(is_even)
def add(x, y):
    return x + y

print("Result of addition:", add(3, 5))

# Example 19: Using decorators for enforcing invariants
def invariants(*conditions):
    def decorator(cls):
        old_init = cls.__init__

        def new_init(self, *args, **kwargs):
            for condition in conditions:
                if not condition(self):
                    raise ValueError("Invariant violated")
            old_init(self, *args, **kwargs)

        cls.__init__ = new_init
        return cls

    return decorator

@invariants(lambda self: self.x > 0)
class MyClass:
    def __init__(self, x):
        self.x = x

obj = MyClass(5)

# Example 20: Using decorators to enforce singleton pattern
def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

@singleton
class MySingleton:
    def __init__(self):
        print("Creating instance of MySingleton")

instance1 = MySingleton()
instance2 = MySingleton()

print(instance1 is instance2)
