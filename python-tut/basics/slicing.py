# https://github.com/intoli/slice/blob/master/README.md
# https://datadependence.com/2016/05/python-sequence-slicing-guide/
# Define a list
my_list = [1, 2, 3, 4, 5]

# Define a tuple
my_tuple = (6, 7, 8, 9, 10)

# Define a string
my_string = "Hello, World!"

# Original data
print("Original list:", my_list)
print("Original tuple:", my_tuple)
print("Original string:", my_string)

# Slicing methods

# Method 1: Slicing lists
print("\nMethod 1: Slicing lists:")
print("First three elements of the list:", my_list[:3])   # Output: [1, 2, 3]
print("Last two elements of the list:", my_list[-2:])    # Output: [4, 5]
print("Every second element of the list:", my_list[::2])  # Output: [1, 3, 5]

# Method 2: Slicing tuples
print("\nMethod 2: Slicing tuples:")
print("First three elements of the tuple:", my_tuple[:3]) # Output: (6, 7, 8)
print("Last two elements of the tuple:", my_tuple[-2:])  # Output: (9, 10)
print("Every second element of the tuple:", my_tuple[::2])  # Output: (6, 8, 10)

# Method 3: Slicing strings
print("\nMethod 3: Slicing strings:")
print("First five characters of the string:", my_string[:5])   # Output: Hello
print("Last six characters of the string:", my_string[-6:])    # Output: World!
print("Every second character of the string:", my_string[::2])  # Output: HloWrd

# Method 4: Combining slicing on mixed data
print("\nMethod 4: Combining slicing on mixed data:")
mixed_data = my_list + list(my_tuple) + list(my_string)
print("Mixed data:", mixed_data)
print("First three elements of mixed data:", mixed_data[:3])   # Output: [1, 2, 3]
print("Last two elements of mixed data:", mixed_data[-2:])    # Output: ['d', '!']
print("Every second element of mixed data:", mixed_data[::2])  # Output: [1, 3, 5, 6, 8, 10, 'H', 'l', ',', 'W', 'r', 'd']

# Method 5: Nested slicing
print("\nMethod 5: Nested slicing:")
nested_data = [my_list, my_tuple, my_string]
print("Nested data:", nested_data)
print("Second element of the first data structure:", nested_data[0][1])  # Output: 2
print("First three elements of the second data structure:", nested_data[1][:3])  # Output: (6, 7, 8)
print("Last four characters of the third data structure:", nested_data[2][-4:])  # Output: rld!

# Method 6: Slicing with negative step
print("\nMethod 6: Slicing with negative step:")
print("Reversed list:", my_list[::-1])  # Output: [5, 4, 3, 2, 1]
print("Reversed tuple:", my_tuple[::-1])  # Output: (10, 9, 8, 7, 6)
print("Reversed string:", my_string[::-1])  # Output: "!dlroW ,olleH"

# Method 7: Slicing with start, stop, and step
print("\nMethod 7: Slicing with start, stop, and step:")
print("Every third element of the list:", my_list[::3])  # Output: [1, 4]
print("Every third element of the tuple:", my_tuple[::3])  # Output: (6, 9)
print("Every third character of the string:", my_string[::3])  # Output: HlWl

# Method 8: Slicing with negative indices
print("\nMethod 8: Slicing with negative indices:")
print("Last three elements of the list:", my_list[-3:])  # Output: [3, 4, 5]
print("Last three elements of the tuple:", my_tuple[-3:])  # Output: (8, 9, 10)
print("Last three characters of the string:", my_string[-3:])  # Output: ld!

# Method 9: Slicing with both positive and negative indices
print("\nMethod 9: Slicing with both positive and negative indices:")
print("Elements between the 2nd and 4th index of the list:", my_list[2:-2])  # Output: [3, 4]
print("Elements between the 2nd and 4th index of the tuple:", my_tuple[2:-2])  # Output: (8,)

# Method 10: Slicing with stride
print("\nMethod 10: Slicing with stride:")
print("Alternate elements of the list:", my_list[::2])  # Output: [1, 3, 5]
print("Alternate elements of the tuple:", my_tuple[::2])  # Output: (6, 8, 10)
print("Alternate characters of the string:", my_string[::2])  # Output: HloWrd

# Method 11: Extended slicing with step and stop
print("\nMethod 11: Extended slicing with step and stop:")
print("Elements from index 1 to 5 with step 2 of the list:", my_list[1:5:2])  # Output: [2, 4]
print("Elements from index 1 to 5 with step 2 of the tuple:", my_tuple[1:5:2])  # Output: (7, 9)
print("Characters from index 1 to 5 with step 2 of the string:", my_string[1:5:2])  # Output: el

