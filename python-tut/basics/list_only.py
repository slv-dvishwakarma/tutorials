# Define a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements in a list
print("Accessing elements:")
print("First element:", my_list[0])     # Output: 1
print("Last element:", my_list[-1])      # Output: 5
print("Slice from index 1 to 3:", my_list[1:3])   # Output: [2, 3]
print()

# List length
print("List length:")
print("Length of the list:", len(my_list))   # Output: 5
print()

# List concatenation
print("List concatenation:")
new_list = my_list + [6, 7, 8]
print("Concatenated list:", new_list)    # Output: [1, 2, 3, 4, 5, 6, 7, 8]
print()

# List repetition
print("List repetition:")
repeated_list = my_list * 2
print("Repeated list:", repeated_list)    # Output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print()

# List methods
print("List methods:")
# Append: Adds an element to the end of the list
my_list.append(6)
print("Appended list:", my_list)    # Output: [1, 2, 3, 4, 5, 6]
# Extend: Extends the list by appending elements from the iterable
my_list.extend([7, 8, 9])
print("Extended list:", my_list)    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Insert: Inserts an element at a specified position
my_list.insert(2, 10)
print("Inserted list:", my_list)    # Output: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]
# Remove: Removes the first occurrence of a value from the list
my_list.remove(5)
print("Removed list:", my_list)     # Output: [1, 2, 10, 3, 4, 6, 7, 8, 9]
# Pop: Removes and returns the last element from the list
popped_element = my_list.pop()
print("Popped element:", popped_element)    # Output: 9
print("List after pop:", my_list)           # Output: [1, 2, 10, 3, 4, 6, 7, 8]
# Index: Returns the index of the first occurrence of a value in the list
index_of_10 = my_list.index(10)
print("Index of 10:", index_of_10)          # Output: 2
# Count: Returns the number of occurrences of a value in the list
count_of_3 = my_list.count(3)
print("Count of 3:", count_of_3)            # Output: 1
# Reverse: Reverses the elements of the list in place
my_list.reverse()
print("Reversed list:", my_list)            # Output: [8, 7, 6, 4, 3, 10, 2, 1]
# Sort: Sorts the elements of the list in place
my_list.sort()
print("Sorted list:", my_list)              # Output: [1, 2, 3, 4, 6, 7, 8, 10]
print()

# List slicing
print("List slicing:")
print("Elements from index 1 to 4:", my_list[1:5])    # Output: [2, 3, 4, 6]
print("Every second element:", my_list[::2])         # Output: [1, 3, 6, 8]
print("Reverse the list:", my_list[::-1])            # Output: [10, 8, 7, 6, 4, 3, 2, 1]
print()

# List comprehension
print("List comprehension:")
squared_numbers = [x ** 2 for x in my_list]
print("Squared numbers:", squared_numbers)    # Output: [1, 4, 9, 16, 36, 49, 64, 100]
print()

# Membership test
print("Membership test:")
print("Is 3 in the list?", 3 in my_list)      # Output: True
print("Is 20 not in the list?", 20 not in my_list)  # Output: True
print()

# Nested lists
print("Nested lists:")
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Element at row 2, column 3:", nested_list[1][2])   # Output: 6
print()

# List copying
print("List copying:")
copied_list = my_list.copy()
print("Copied list:", copied_list)
print()

# List clearing
print("List clearing:")
my_list.clear()
print("Cleared list:", my_list)   # Output: []
