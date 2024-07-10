print("""
Python has several built-in data types, including:
Numeric Types: Integers (int), floating-point numbers (float), and complex numbers (complex).
Sequence Types: Lists (list), tuples (tuple), and strings (str).
Mapping Types: Dictionaries (dict).
Set Types: Sets (set).
Boolean Type: Boolean (bool).
Python also supports type conversion functions like int(), float(), str(), etc., for converting between different types.
""")
# Define variables with different data types
i, f, b, s, c = 1, 2.3, True, "Text String", 1+2j

# Print variables and their types
print("Variables and their types:")
print("i:", i, type(i))  # Output: i: 1 <class 'int'>
print("b:", b, type(b))  # Output: b: True <class 'bool'>
print("f:", f, type(f))  # Output: f: 2.3 <class 'float'>
print("s:", s, type(s))  # Output: s: Text String <class 'str'>
print("c:", c, type(c))  # Output: c: (1+2j) <class 'complex'>

# Explanation of data types
print("\nExplanation of data types:")
print("An integer (int) represents whole numbers.")
print("A boolean (bool) represents true or false values.")
print("A floating-point number (float) represents decimal numbers.")
print("A string (str) represents text.")
print("A complex number (complex) represents numbers with real and imaginary parts.")

# Check if variables belong to specific data types
print("\nCheck if variables belong to specific data types:")
print("Is 'i' an integer?", isinstance(i, int))
print("Is 'b' a boolean?", isinstance(b, bool))
print("Is 'f' a float?", isinstance(f, float))
print("Is 's' a string?", isinstance(s, str))
print("Is 'c' a complex number?", isinstance(c, complex))

# Type casting examples
print("\nType casting examples:")
# Integer to float
i_to_f = float(i)
print("Casting integer to float:", i_to_f, type(i_to_f))
# Float to integer
f_to_i = int(f)
print("Casting float to integer:", f_to_i, type(f_to_i))
# Boolean to integer
b_to_i = int(b)
print("Casting boolean to integer:", b_to_i, type(b_to_i))
# String to integer
s_to_i = int(s) if s.isdigit() else None
print("Casting string to integer (if possible):", s_to_i, type(s_to_i))