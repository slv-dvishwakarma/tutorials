# Define a string
my_string = "Hello, World!"

# Accessing characters in a string
print("Accessing characters:")
print("First character:", my_string[0])      # Output: H
print("Last character:", my_string[-1])       # Output: !
print("Substring from index 7 to end:", my_string[7:])   # Output: World!
print()

# String length
print("String length:")
print("Length of the string:", len(my_string))    # Output: 13
print()

# String concatenation
print("String concatenation:")
name = "Alice"
greeting = "Hello, " + name + "!"
print(greeting)    # Output: Hello, Alice!
print()

# String repetition
print("String repetition:")
stars = "*" * 10
print(stars)    # Output: **********
print()

# String slicing
print("String slicing:")
print("Substring from index 1 to 5:", my_string[1:5])    # Output: ello
print("Every second character:", my_string[::2])         # Output: HloWrd
print("Reverse the string:", my_string[::-1])            # Output: !dlroW ,olleH
print()

# String methods
print("String methods:")
# Conversion methods
print("Uppercase:", my_string.upper())      # Output: HELLO, WORLD!
print("Lowercase:", my_string.lower())      # Output: hello, world!
print("Titlecase:", my_string.title())      # Output: Hello, World!
# Search methods
print("Find 'World':", my_string.find("World"))       # Output: 7
print("Count 'l':", my_string.count("l"))             # Output: 3
print("Starts with 'Hello':", my_string.startswith("Hello"))   # Output: True
print("Ends with 'World!':", my_string.endswith("World!"))     # Output: True
# Modification methods
print("Replace 'World' with 'Python':", my_string.replace("World", "Python"))    # Output: Hello, Python!
print("Strip whitespace from '   Hello   ':", "   Hello   ".strip())               # Output: Hello
# Splitting and joining
print("Split 'Hello, World!' by comma:", my_string.split(","))       # Output: ['Hello', ' World!']
print("Join ['Hello', ' World!'] with comma:", ",".join(['Hello', ' World!']))   # Output: Hello, World!
print()

# String formatting
print("String formatting:")
name = "Bob"
age = 30
print("My name is {} and I am {} years old.".format(name, age))   # Output: My name is Bob and I am 30 years old.
print(f"My name is {name} and I am {age} years old.")             # Output: My name is Bob and I am 30 years old. (using f-string)
print("Formatted floating point number: {:.2f}".format(3.14159))   # Output: Formatted floating point number: 3.14
print("Formatted integer with leading zeros: {:05d}".format(42))    # Output: Formatted integer with leading zeros: 00042
print()

# Escape characters
print("Escape characters:")
print("Newline:\nFirst line\nSecond line")       # Output: Newline: First line (newline) Second line
print("Tab:\tFirst column\tSecond column")        # Output: Tab:   First column    Second column
print("Backslash: C:\\Users\\Bob")                # Output: Backslash: C:\Users\Bob
print("Single quote: 'Hello'")                    # Output: Single quote: 'Hello'
print("Double quote: \"World!\"")                 # Output: Double quote: "World!"

# Raw strings
print("Raw strings:")
print(r"Backslash: C:\Users\Bob")                # Output: Backslash: C:\Users\Bob

# Multiline strings
print("Multiline strings:")
multiline_string = """This is a
multiline string
in Python."""
print(multiline_string)
