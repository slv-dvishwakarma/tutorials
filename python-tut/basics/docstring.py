# Example 1: Defining a function with a docstring
def greet():
    """This function greets the user."""
    print("Hello!")

# Accessing the docstring using __doc__
print("Docstring of greet function:")
print(greet.__doc__)

# Example 2: Defining a function with parameters and a docstring
def greet_with_name(name):
    """This function greets the user with the specified name."""
    print("Hello,", name)

# Accessing the docstring using __doc__
print("\nDocstring of greet_with_name function:")
print(greet_with_name.__doc__)

# Example 3: Defining a function with default parameter value and a docstring
def greet_with_default(name="world"):
    """This function greets the user with the specified name, or 'world' if no name is provided."""
    print("Hello,", name)

# Accessing the docstring using __doc__
print("\nDocstring of greet_with_default function:")
print(greet_with_default.__doc__)

# Example 4: Defining a function with return value and a docstring
def add(x, y):
    """This function returns the sum of two numbers."""
    return x + y

# Accessing the docstring using __doc__
print("\nDocstring of add function:")
print(add.__doc__)

# Example 5: Defining a function with multiple return values and a docstring
def divide(x, y):
    """This function divides two numbers and returns the quotient and remainder."""
    quotient = x // y
    remainder = x % y
    return quotient, remainder

# Accessing the docstring using __doc__
print("\nDocstring of divide function:")
print(divide.__doc__)

# Example 6: Exploring functions using dir()
print("\nAttributes of the divide function:")
print(dir(divide))

# Example 7: Defining a function with no docstring
def func_without_docstring():
    pass

# Accessing the docstring using __doc__
print("\nDocstring of func_without_docstring function:")
print(func_without_docstring.__doc__)

# Example 8: Defining a function with multiline docstring
def multiline_docstring():
    """
    This is a multiline docstring.
    It provides detailed information about the function.
    """
    pass

# Accessing the docstring using __doc__
print("\nDocstring of multiline_docstring function:")
print(multiline_docstring.__doc__)

# Example 9: Defining a function with a Unicode docstring
def unicode_docstring():
    """This is a Unicode docstring: 😊"""
    pass

# Accessing the docstring using __doc__
print("\nDocstring of unicode_docstring function:")
print(unicode_docstring.__doc__)

# Example 10: Defining a function with annotations
def annotated_function(x: int, y: int) -> int:
    """This function takes two integers as input and returns an integer."""
    return x + y

# Accessing the annotations using __annotations__
print("\nAnnotations of annotated_function:")
print(annotated_function.__annotations__)

# Example 11: Defining a function with lambda expression
add_lambda = lambda x, y: x + y

# Accessing the docstring using __doc__
print("\nDocstring of add_lambda function:")
print(add_lambda.__doc__)

# Example 12: Using help() to access docstring
print("\nUsing help() to access docstring of add_lambda function:")
help(add_lambda)

# Example 13: Defining a function with *args
def sum_all(*args):
    """This function calculates the sum of all the arguments."""
    total = 0
    for num in args:
        total += num
    return total

# Accessing the docstring using __doc__
print("\nDocstring of sum_all function:")
print(sum_all.__doc__)

# Example 14: Defining a function with **kwargs
def print_info(**kwargs):
    """This function prints key-value pairs."""
    for key, value in kwargs.items():
        print(key, ":", value)

# Accessing the docstring using __doc__
print("\nDocstring of print_info function:")
print(print_info.__doc__)

# Example 15: Defining a function with both *args and **kwargs
def mixed_arguments(arg1, arg2, *args, **kwargs):
    """This function demonstrates mixed arguments."""
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("Additional positional arguments:", args)
    print("Additional keyword arguments:", kwargs)

# Accessing the docstring using __doc__
print("\nDocstring of mixed_arguments function:")
print(mixed_arguments.__doc__)

# Example 16: Defining a recursive function
def factorial(n):
    """This function calculates the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Accessing the docstring using __doc__
print("\nDocstring of factorial function:")
print(factorial.__doc__)

# Example 17: Using help() to access docstring of recursive function
print("\nUsing help() to access docstring of factorial function:")
help(factorial)

# Example 18: Defining a generator function
def fibonacci(n):
    """This generator function generates Fibonacci sequence up to n."""
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

# Accessing the docstring using __doc__
print("\nDocstring of fibonacci generator function:")
print(fibonacci.__doc__)

# Example 19: Using help() to access docstring of generator function
print("\nUsing help() to access docstring of fibonacci generator function:")
help(fibonacci)

# Example 20: Defining a function with side effects
def modify_list(lst):
    """This function modifies a list by appending an element."""
    lst.append(4)

# Accessing the docstring using __doc__
print("\nDocstring of modify_list function:")
print(modify_list.__doc__)

# Example 21: Using help() to access docstring of function with side effects
print("\nUsing help() to access docstring of modify_list function:")
help(modify_list)



# Example 21: Defining a class with a docstring
class MyClass:
    """This is a simple class definition."""
    pass

# Accessing the docstring using __doc__
print("Docstring of MyClass class:")
print(MyClass.__doc__)

# Example 22: Defining a class with methods and a docstring
class Person:
    """This class represents a person."""
    
    def __init__(self, name, age):
        """Initializer method to initialize name and age."""
        self.name = name
        self.age = age

    def greet(self):
        """Method to greet the person."""
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")

# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Accessing the docstring using __doc__
print("\nDocstring of Person class:")
print(Person.__doc__)

# Accessing the docstring of the greet method
print("\nDocstring of greet method in Person class:")
print(Person.greet.__doc__)

# Example 23: Defining a class with class variables and a docstring
class Dog:
    """This class represents a dog."""
    
    species = "Canis lupus familiaris"

    def __init__(self, name):
        """Initializer method to initialize name."""
        self.name = name

# Creating instances of the Dog class
dog1 = Dog("Buddy")
dog2 = Dog("Max")

# Accessing the docstring using __doc__
print("\nDocstring of Dog class:")
print(Dog.__doc__)

# Example 24: Defining a class with class methods and a docstring
class MathOperations:
    """This class performs mathematical operations."""
    
    @classmethod
    def add(cls, x, y):
        """Class method to add two numbers."""
        return x + y
    
    @staticmethod
    def multiply(x, y):
        """Static method to multiply two numbers."""
        return x * y

# Accessing the docstring using __doc__
print("\nDocstring of MathOperations class:")
print(MathOperations.__doc__)

# Accessing the docstring of the add class method
print("\nDocstring of add class method in MathOperations class:")
print(MathOperations.add.__doc__)

# Accessing the docstring of the multiply static method
print("\nDocstring of multiply static method in MathOperations class:")
print(MathOperations.multiply.__doc__)

# Example 25: Defining a class with inheritance and a docstring
class Animal:
    """This is a base class representing an animal."""
    
    def speak(self):
        """Method to make the animal speak."""
        pass

class Dog(Animal):
    """This class represents a dog."""
    
    def speak(self):
        """Method to make the dog bark."""
        print("Woof!")

class Cat(Animal):
    """This class represents a cat."""
    
    def speak(self):
        """Method to make the cat meow."""
        print("Meow!")

# Creating instances of the Dog and Cat classes
dog = Dog()
cat = Cat()

# Accessing the docstring using __doc__
print("\nDocstring of Animal class:")
print(Animal.__doc__)

# Accessing the docstring of the speak method in Dog class
print("\nDocstring of speak method in Dog class:")
print(Dog.speak.__doc__)

# Accessing the docstring of the speak method in Cat class
print("\nDocstring of speak method in Cat class:")
print(Cat.speak.__doc__)

# Example 26: Defining a class with properties and a docstring
class Circle:
    """This class represents a circle."""
    
    def __init__(self, radius):
        """Initializer method to initialize radius."""
        self.radius = radius
    
    @property
    def diameter(self):
        """Property to get the diameter of the circle."""
        return 2 * self.radius
    
    @property
    def area(self):
        """Property to get the area of the circle."""
        return 3.14 * self.radius**2

# Creating an instance of the Circle class
circle = Circle(5)

# Accessing the docstring using __doc__
print("\nDocstring of Circle class:")
print(Circle.__doc__)

# Accessing the docstring of the diameter property
print("\nDocstring of diameter property in Circle class:")
print(Circle.diameter.__doc__)

# Accessing the docstring of the area property
print("\nDocstring of area property in Circle class:")
print(Circle.area.__doc__)
