# List comprehension examples
# Example 1: Squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("Example 1 - Squares of numbers from 1 to 10:", squares)

# Example 2: Even numbers from 1 to 20
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print("Example 2 - Even numbers from 1 to 20:", even_numbers)

# Example 3: Odd numbers from 1 to 20
odd_numbers = [x for x in range(1, 21) if x % 2 != 0]
print("Example 3 - Odd numbers from 1 to 20:", odd_numbers)

# Example 4: List of words and their lengths
sentence = "The quick brown fox jumps over the lazy dog"
word_lengths = [(word, len(word)) for word in sentence.split()]
print("Example 4 - List of words and their lengths:", word_lengths)

# Example 5: Uppercase version of words longer than 3 characters
uppercase_long_words = [word.upper() for word in sentence.split() if len(word) > 3]
print("Example 5 - Uppercase version of words longer than 3 characters:", uppercase_long_words)

# Set comprehension examples
# Example 6: Set of unique vowels in a sentence
vowels = {char.lower() for char in sentence if char.lower() in 'aeiou'}
print("Example 6 - Set of unique vowels in the sentence:", vowels)

# Example 7: Set of squares of even numbers from 1 to 10
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print("Example 7 - Set of squares of even numbers from 1 to 10:", even_squares)

# Example 8: Set of colors with their lengths
colors = {'red', 'green', 'blue', 'yellow'}
color_lengths = {color: len(color) for color in colors}
print("Example 8 - Set of colors with their lengths:", color_lengths)

# Dictionary comprehension examples
# Example 9: Dictionary of numbers and their squares
numbers = {x: x**2 for x in range(1, 11)}
print("Example 9 - Dictionary of numbers and their squares:", numbers)

# Example 10: Mapping names to their lengths
names = ['Alice', 'Bob', 'Charlie', 'David']
name_lengths = {name: len(name) for name in names}
print("Example 10 - Mapping names to their lengths:", name_lengths)

# Example 11: Filtering out odd numbers from a dictionary
number_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
even_numbers_dict = {key: value for key, value in number_dict.items() if value % 2 == 0}
print("Example 11 - Dictionary with only even numbers:", even_numbers_dict)

# Example 12: Dictionary of students and their grades, filtering out failing grades
grades = {'Alice': 85, 'Bob': 72, 'Charlie': 60, 'David': 45}
passing_grades = {student: grade for student, grade in grades.items() if grade >= 60}
print("Example 12 - Dictionary with passing grades:", passing_grades)

# Example 13: Combining two lists into a dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = {k: v for k, v in zip(keys, values)}
print("Example 13 - Dictionary from two lists:", combined_dict)

# Example 14: Dictionary with uppercase keys and values
words_dict = {'hello': 'world', 'python': 'programming', 'open': 'source'}
uppercase_words_dict = {key.upper(): value.upper() for key, value in words_dict.items()}
print("Example 14 - Dictionary with uppercase keys and values:", uppercase_words_dict)

# Example 15: Dictionary of ASCII values of characters in a string
ascii_values_dict = {char: ord(char) for char in sentence if char.isalpha()}
print("Example 15 - Dictionary of ASCII values of characters:", ascii_values_dict)

# Example 16: Flattened list from a list of lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in nested_list for num in sublist]
print("Example 16 - Flattened list from a list of lists:", flattened_list)

# Example 17: List of tuples with numbers and their squares
number_square_tuples = [(x, x**2) for x in range(1, 6)]
print("Example 17 - List of tuples with numbers and their squares:", number_square_tuples)

# Example 18: List of letters and their ASCII values
ascii_values_list = [(char, ord(char)) for char in 'abcdefghijklmnopqrstuvwxyz']
print("Example 18 - List of letters and their ASCII values:", ascii_values_list)

# Example 19: Nested dictionary with list comprehension
nested_dict = {outer: {inner: inner**2 for inner in range(1, 4)} for outer in range(1, 4)}
print("Example 19 - Nested dictionary with list comprehension:", nested_dict)

# Example 20: Dictionary comprehension with conditional value assignment
even_or_odd = {x: 'even' if x % 2 == 0 else 'odd' for x in range(1, 11)}
print("Example 20 - Dictionary with even/odd value assignment:", even_or_odd)
