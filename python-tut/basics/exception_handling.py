# Example 1: Handling multiple exceptions with separate blocks
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
except TypeError:
    print("Error: Invalid type occurred")

# Example 2: Handling exceptions with a single except block
try:
    result = 10 / 'a'
except (ZeroDivisionError, TypeError) as e:
    print(f"Error: {e}")

# Example 3: Handling specific exceptions with different blocks
try:
    result = 10 / 'a'
except ZeroDivisionError:
    print("Error: Division by zero occurred")
except TypeError:
    print("Error: Invalid type occurred")

# Example 4: Using else block with try-except
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero occurred")
else:
    print("No error occurred")

# Example 5: Using finally block with try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
finally:
    print("Finally block executed")

# Example 6: Using finally block without except
try:
    result = 10 / 2
finally:
    print("Finally block executed")

# Example 7: Handling exceptions with custom error message
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Example 8: Raising an exception with custom error message
try:
    raise ValueError("Custom error message")
except ValueError as e:
    print(f"Error: {e}")

# Example 9: Raising an exception without arguments
try:
    raise ValueError
except ValueError:
    print("Error: ValueError raised")

# Example 10: Catching exception instance
try:
    result = 10 / 0
except Exception as e:
    print("Error:", e.__class__.__name__)

# Example 11: Handling exceptions in a loop
for i in range(5):
    try:
        result = 10 / i
    except ZeroDivisionError:
        print("Error: Division by zero occurred")
    except Exception as e:
        print("Error:", e)

# Example 12: Using assert statement
x = 10
try:
    assert x == 5, "x should be 5"
except AssertionError as e:
    print(f"AssertionError: {e}")

# Example 13: Nested try-except blocks
try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Inner Error: Division by zero occurred")
except Exception as e:
    print("Outer Error:", e)

# Example 14: Accessing traceback information
import traceback

try:
    result = 10 / 0
except ZeroDivisionError:
    traceback.print_exc()

# Example 15: Using specific exceptions with else block
try:
    result = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input")
else:
    print("Square of the number:", result ** 2)

# Example 16: Catching exception in a function
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero occurred"

print("Result:", divide(10, 2))
print("Result:", divide(10, 0))

# Example 17: Using custom exception classes
class CustomError(Exception):
    pass

try:
    raise CustomError("Custom error message")
except CustomError as e:
    print(f"CustomError: {e}")

# Example 18: Re-raising an exception
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
    raise

# Example 19: Handling exceptions with context managers
with open('nonexistent_file.txt', 'r') as file:
    data = file.read()

# Example 20: Using contextlib.suppress to ignore exceptions
import contextlib

with contextlib.suppress(FileNotFoundError):
    with open('nonexistent_file.txt', 'r') as file:
        data = file.read()

# Example 21: Handling exceptions with except clause only
try:
    result = 10 / 0
except:
    print("Error occurred, but not handled specifically")

# Example 22: Handling exceptions with specific exception names
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
except Exception as e:
    print(f"Error: {e}")

# Example 23: Using multiple except blocks with specific exception names
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
except TypeError:
    print("Error: Invalid type occurred")
except Exception as e:
    print(f"Error: {e}")

# Example 24: Handling exceptions with multiple except clauses
try:
    result = 10 / 0
except (ZeroDivisionError, TypeError):
    print("Error: Division by zero or invalid type occurred")
except Exception as e:
    print(f"Error: {e}")

# Example 25: Using except clause without specifying exception names
try:
    result = 10 / 0
except:
    print("An error occurred")

# Example 26: Using except clause with specific exception names
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")

# Example 27: Using except clause with multiple specific exception names
try:
    result = 10 / 0
except (ZeroDivisionError, TypeError):
    print("Error: Division by zero or invalid type occurred")

# Example 28: Using except clause with generic exception name
try:
    result = 10 / 0
except Exception as e:
    print(f"Error: {e}")

# Example 29: Using except clause with specific and generic exception names
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
except Exception as e:
    print(f"Error: {e}")

# Example 30: Handling multiple specific exceptions with separate blocks
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
except TypeError:
    print("Error: Invalid type occurred")

# Example 31: Using else block with try-except
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero occurred")
else:
    print("No error occurred")

# Example 32: Using finally block with try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
finally:
    print("Finally block executed")

# Example 33: Using finally block without except
try:
    result = 10 / 2
finally:
    print("Finally block executed")

# Example 34: Handling exceptions with custom error message
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Example 35: Raising an exception with custom error message
try:
    raise ValueError("Custom error message")
except ValueError as e:
    print(f"Error: {e}")

# Example 36: Raising an exception without arguments
try:
    raise ValueError
except ValueError:
    print("Error: ValueError raised")

# Example 37: Catching exception instance
try:
    result = 10 / 0
except Exception as e:
    print("Error:", e.__class__.__name__)

# Example 38: Handling exceptions in a loop
for i in range(5):
    try:
        result = 10 / i
    except ZeroDivisionError:
        print("Error: Division by zero occurred")
    except Exception as e:
        print("Error:", e)

# Example 39: Using assert statement
x = 10
try:
    assert x == 5, "x should be 5"
except AssertionError as e:
    print(f"AssertionError: {e}")

# Example 40: Nested try-except blocks
try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Inner Error: Division by zero occurred")
except Exception as e:
    print("Outer Error:", e)

# Example 41: Accessing traceback information
import traceback

try:
    result = 10 / 0
except ZeroDivisionError:
    traceback.print_exc()

# Example 42: Using specific exceptions with else block
try:
    result = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input")
else:
    print("Square of the number:", result ** 2)

# Example 43: Catching exception in a function
def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero occurred"

print("Result:", divide(10, 2))
print("Result:", divide(10, 0))

# Example 44: Using custom exception classes
class CustomError(Exception):
    pass

try:
    raise CustomError("Custom error message")
except CustomError as e:
    print(f"CustomError: {e}")

# Example 45: Re-raising an exception
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero occurred")
    raise

# Example 46: Handling exceptions with context managers
with open('nonexistent_file.txt', 'r') as file:
    data = file.read()

# Example 47: Using contextlib.suppress to ignore exceptions
import contextlib

with contextlib.suppress(FileNotFoundError):
    with open('nonexistent_file.txt', 'r') as file:
        data = file.read()

# Example 48: Handling exceptions with except clause only
try:
    result = 10 / 0
except:
    print("Error occurred, but not handled specifically")



# Example 1: SyntaxError
print("Hello, World!")  # Correct syntax

# Example 2: IndentationError
def my_function():
print("Hello")  # Incorrect indentation

# Example 3: NameError
print(variable_not_defined)  # Variable not defined

# Example 4: TypeError
sum = 10 + "20"  # Adding integer and string

# Example 5: IndexError
my_list = [1, 2, 3]
print(my_list[3])  # Index out of range

# Example 6: KeyError
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])  # Key not present

# Example 7: ValueError
int("abc")  # String cannot be converted to integer

# Example 8: FileNotFoundError
file_path = 'nonexistent_file.txt'
with open(file_path, 'r') as file:
    content = file.read()  # File not found

# Example 9: ZeroDivisionError
result = 10 / 0  # Division by zero

# Example 10: AttributeError
my_list = [1, 2, 3]
print(my_list.append(4))  # append() method does not return a value

# Example 11: KeyboardInterrupt
try:
    while True:
        pass  # Infinite loop until interrupted by Ctrl+C
except KeyboardInterrupt:
    print("Program interrupted by user")

# Example 12: OverflowError
import math
print(math.exp(1000))  # Result too large to represent as a float

# Example 13: MemoryError
# Create a large list to exceed available memory
large_list = [i for i in range(10**8)]

# Example 14: FileNotFoundError (Handling)
try:
    with open(file_path, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found:", file_path)

# Example 15: IndexError (Handling)
try:
    my_list = [1, 2, 3]
    print(my_list[3])
except IndexError:
    print("Index out of range")

# Example 16: KeyError (Handling)
try:
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])
except KeyError:
    print("Key not found in dictionary")

# Example 17: ValueError (Handling)
try:
    int("abc")
except ValueError:
    print("Invalid conversion to integer")

# Example 18: ZeroDivisionError (Handling)
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero")

# Example 19: TypeError (Handling)
try:
    sum = 10 + "20"
except TypeError:
    print("Unsupported operation between int and str")

# Example 20: AttributeError (Handling)
try:
    my_list = [1, 2, 3]
    print(my_list.append(4))
except AttributeError:
    print("Attribute not found")

# Example 21: Custom Exception
class MyCustomException(Exception):
    pass

try:
    raise MyCustomException("This is a custom exception")
except MyCustomException as e:
    print("Custom Exception raised:", e)

# Example 22: Multiple Exceptions
try:
    result = 10 / 0  # ZeroDivisionError
    my_list = [1, 2, 3]
    print(my_list[5])  # IndexError
except ZeroDivisionError as e:
    print("Error:", e)
except IndexError as e:
    print("Error:", e)

# Example 23: Using else block
try:
    my_dict = {'a': 1, 'b': 2}
    value = my_dict['c']
except KeyError:
    print("Key not found")
else:
    print("Value found:", value)

# Example 24: Using finally block
try:
    file = open('existing_file.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
    print("File closed")

# Example 25: Raising an exception
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    validate_age(-10)
except ValueError as e:
    print("Error:", e)

# Example 26: Assertion Error
def validate_positive_number(num):
    assert num > 0, "Number should be positive"

try:
    validate_positive_number(-5)
except AssertionError as e:
    print("Assertion Error:", e)

# Example 27: Handling Assertion Error
try:
    validate_positive_number(-5)
except AssertionError as e:
    print("Assertion Error:", e)
    # Handle the error gracefully

# Example 28: FileNotFoundError (Handling within a function)
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found"

file_content = read_file('existing_file.txt')
print("File content:", file_content)

# Example 29: IndexError (Handling within a function)
def get_element_from_list(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return None

result = get_element_from_list([1, 2, 3], 5)
print("Result:", result)

# Example 30: Custom Exception (Handling within a function)
class NegativeValueError(Exception):
    pass

def process_value(value):
    if value < 0:
        raise NegativeValueError("Negative value encountered")
    return value

try:
    processed_value = process_value(-5)
except NegativeValueError as e:
    print("Error:", e)

# Example 31: Handling Multiple Exceptions with one except block
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)

# Example 32: Using Exception class to handle all exceptions
try:
    result = 10 / 0
except Exception as e:
    print("An error occurred:", e)

# Example 33: Handling multiple exceptions with separate except blocks
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError as e:
    print("Invalid input:", e)
except ZeroDivisionError as e:
    print("Division by zero:", e)

# Example 34: Nested try-except blocks
try:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Division by zero")
except Exception as e:
    print("An error occurred:", e)

# Example 35: Using else block with try-except
try:
    result = 10 / 2
except ZeroDivisionError as e:
    print("Division by zero:", e)
else:
    print("Result:", result)

# Example 36: Using finally block with try-except
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Division by zero:", e)
finally:
    print("Finally block executed")

# Example 37: Manually raising an exception
age = -5
if age < 0:
    raise ValueError("Age cannot be negative")

# Example 38: Handling FileNotFoundError with pathlib
from pathlib import Path

file_path = Path("nonexistent_file.txt")
try:
    with file_path.open('r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found")

# Example 39: Handling JSONDecodeError
import json

try:
    json_data = json.loads("invalid json")
except json.JSONDecodeError as e:
    print("JSON decoding error:", e)

# Example 40: Handling TimeoutError
import time

try:
    time.sleep(10)  # Simulating a long-running operation
except TimeoutError:
    print("Operation timed out")

# Example 41: Handling ModuleNotFoundError
try:
    import nonexistent_module
except ModuleNotFoundError:
    print("Module not found")

# Example 42: Handling StopIteration
numbers = [1, 2, 3]
iterator = iter(numbers)
try:
    while True:
        print(next(iterator))
except StopIteration:
    print("End of iterator")

# Example 43: Handling NotImplementedError
class BaseClass:
    def method(self):
        raise NotImplementedError("Method not implemented in base class")

try:
    obj = BaseClass()
    obj.method()
except NotImplementedError as e:
    print("NotImplementedError:", e)

