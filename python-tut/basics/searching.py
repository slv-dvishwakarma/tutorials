# Define a list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Original list
print("Original list:", my_list)

# Searching methods

# Method 1: Using the index() method to find the index of an element
element = 5
try:
    index = my_list.index(element)
    print("\nMethod 1: Using index() method to find the index of an element:")
    print(f"Index of {element}: {index}")
except ValueError:
    print(f"\nMethod 1: Element {element} not found in the list.")

# Method 2: Using list comprehension to find all occurrences of an element
element = 5
indices = [i for i, x in enumerate(my_list) if x == element]
print("\nMethod 2: Using list comprehension to find all occurrences of an element:")
if indices:
    print(f"Indices of {element}: {indices}")
else:
    print(f"Element {element} not found in the list.")

# Method 3: Using the count() method to count occurrences of an element
element = 5
count = my_list.count(element)
print("\nMethod 3: Using count() method to count occurrences of an element:")
print(f"Number of occurrences of {element}: {count}")

# Method 4: Using a generator expression to search for an element
element = 5
found = any(x == element for x in my_list)
print("\nMethod 4: Using a generator expression to search for an element:")
if found:
    print(f"Element {element} found in the list.")
else:
    print(f"Element {element} not found in the list.")

# Method 5: Using the in keyword to check if an element exists in the list
element = 8
print("\nMethod 5: Using 'in' keyword to check if an element exists in the list:")
if element in my_list:
    print(f"Element {element} found in the list.")
else:
    print(f"Element {element} not found in the list.")

# Method 6: Using the bisect module for binary search (requires a sorted list)
import bisect
sorted_list = sorted(my_list)
element = 5
index = bisect.bisect_left(sorted_list, element)
print("\nMethod 6: Using bisect module for binary search (requires a sorted list):")
if index < len(sorted_list) and sorted_list[index] == element:
    print(f"Element {element} found at index {index}.")
else:
    print(f"Element {element} not found in the list.")

# Method 7: Using linear search algorithm
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

element = 5
index = linear_search(my_list, element)
print("\nMethod 7: Using linear search algorithm:")
if index != -1:
    print(f"Element {element} found at index {index}.")
else:
    print(f"Element {element} not found in the list.")

# Method 8: Using list comprehension to find indices of multiple elements
elements_to_find = [3, 5]
indices = [i for i, x in enumerate(my_list) if x in elements_to_find]
print("\nMethod 8: Using list comprehension to find indices of multiple elements:")
print(f"Indices of {elements_to_find}: {indices}")

# Method 9: Using set intersection to find common elements between two lists
other_list = [5, 6, 7, 8, 9]
common_elements = set(my_list) & set(other_list)
print("\nMethod 9: Using set intersection to find common elements between two lists:")
print("Common elements:", common_elements)

# Method 10: Using filter() function to find elements meeting a condition
condition = lambda x: x % 2 == 0
filtered_elements = list(filter(condition, my_list))
print("\nMethod 10: Using filter() function to find elements meeting a condition:")
print("Filtered elements (even numbers):", filtered_elements)
