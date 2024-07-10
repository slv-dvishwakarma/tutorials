# Define a list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Original list
print("Original list:", my_list)

# Sorting methods

# Method 1: Using the sorted() function (Returns a new sorted list)
sorted_list = sorted(my_list)
print("\nMethod 1: Sorting using sorted() function (Returns a new sorted list):")
print("Sorted list:", sorted_list)
print("Original list (unchanged):", my_list)

# Method 2: Using the sort() method (Sorts the list in place)
my_list.sort()
print("\nMethod 2: Sorting using sort() method (Sorts the list in place):")
print("Sorted list:", my_list)

# Method 3: Sorting in reverse order
reverse_sorted_list = sorted(my_list, reverse=True)
print("\nMethod 3: Sorting in reverse order:")
print("Reverse sorted list:", reverse_sorted_list)

# Method 4: Custom sorting with a key function
# Sorting based on absolute values
abs_sorted_list = sorted(my_list, key=abs)
print("\nMethod 4: Custom sorting based on absolute values:")
print("Sorted list (based on absolute values):", abs_sorted_list)

# Method 5: Sorting a list of tuples by a specific element
# List of tuples
tuple_list = [(1, 'Alice'), (3, 'Bob'), (2, 'Charlie')]
# Sorting by the first element of each tuple
sorted_tuple_list = sorted(tuple_list, key=lambda x: x[0])
print("\nMethod 5: Sorting a list of tuples by a specific element:")
print("Sorted list of tuples (by first element):", sorted_tuple_list)

# Method 6: Sorting a list of dictionaries by a specific key
# List of dictionaries
dict_list = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 20}]
# Sorting by the 'age' key of each dictionary
sorted_dict_list = sorted(dict_list, key=lambda x: x['age'])
print("\nMethod 6: Sorting a list of dictionaries by a specific key:")
print("Sorted list of dictionaries (by age):", sorted_dict_list)

# Method 7: Stable sorting with multiple keys
# List of tuples
multiple_key_list = [(1, 2), (3, 1), (2, 3), (1, 1), (3, 2)]
# Sorting first by the first element, then by the second element
sorted_multiple_key_list = sorted(multiple_key_list, key=lambda x: (x[0], x[1]))
print("\nMethod 7: Stable sorting with multiple keys:")
print("Stable sorted list (by multiple keys):", sorted_multiple_key_list)

# Method 8: Sorting a list of strings ignoring case
string_list = ['Apple', 'banana', 'orange', 'Pineapple', 'Kiwi']
case_insensitive_sorted_list = sorted(string_list, key=str.lower)
print("\nMethod 8: Sorting a list of strings ignoring case:")
print("Case insensitive sorted list:", case_insensitive_sorted_list)

# Method 9: Sorting a list of strings by length
string_list.sort(key=len)
print("\nMethod 9: Sorting a list of strings by length:")
print("Sorted list by length:", string_list)

# Method 10: Sorting a list of strings in reverse alphabetical order
reverse_alphabetical_sorted_list = sorted(string_list, reverse=True)
print("\nMethod 10: Sorting a list of strings in reverse alphabetical order:")
print("Reverse alphabetical sorted list:", reverse_alphabetical_sorted_list)

# Method 11: Sorting a list of tuples by the second element
tuple_list.sort(key=lambda x: x[1])
print("\nMethod 11: Sorting a list of tuples by the second element:")
print("Sorted list of tuples (by second element):", tuple_list)

# Method 12: Sorting a list of dictionaries by multiple keys
dict_list.sort(key=lambda x: (x['age'], x['name']))
print("\nMethod 12: Sorting a list of dictionaries by multiple keys (age, name):")
print("Sorted list of dictionaries (by age, name):", dict_list)

# Method 13: Sorting a list of lists by the sum of elements
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
list_of_lists.sort(key=sum)
print("\nMethod 13: Sorting a list of lists by the sum of elements:")
print("Sorted list of lists (by sum):", list_of_lists)

# Method 14: Sorting a list of tuples with mixed data types
mixed_data_type_list = [(1, 'apple'), ('orange', 3.14), (5, True), ('banana', 2.7)]
mixed_data_type_list.sort(key=lambda x: str(x))
print("\nMethod 14: Sorting a list of tuples with mixed data types:")
print("Sorted list of tuples (by string representation):", mixed_data_type_list)

# Method 15: Sorting a list of objects using custom comparison
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person({self.name}, {self.age})"
    
people = [Person('Alice', 30), Person('Bob', 25), Person('Charlie', 35)]
people.sort(key=lambda x: x.age)
print("\nMethod 15: Sorting a list of objects using custom comparison (by age):")
print("Sorted list of people (by age):", people)

# Method 16: Sorting a list of objects using a method as a key
people.sort(key=Person.__repr__)
print("\nMethod 16: Sorting a list of objects using a method as a key (by name):")
print("Sorted list of people (by name):", people)

# Method 17: Sorting a list of strings based on custom sorting order
custom_order_list = ['apple', 'banana', 'orange', 'pineapple', 'kiwi']
custom_order = {'apple': 1, 'banana': 2, 'orange': 3, 'kiwi': 4, 'pineapple': 5}
custom_sorted_list = sorted(custom_order_list, key=lambda x: custom_order.get(x.lower()))
print("\nMethod 17: Sorting a list of strings based on custom sorting order:")
print("Custom sorted list:", custom_sorted_list)

# Method 18: Sorting a list of lists by the first element in descending order
list_of_lists.sort(key=lambda x: x[0], reverse=True)
print("\nMethod 18: Sorting a list of lists by the first element in descending order:")
print("Sorted list of lists (by first element in descending order):", list_of_lists)

# Method 19: Sorting a list of tuples by the last element
tuple_list.sort(key=lambda x: x[-1])
print("\nMethod 19: Sorting a list of tuples by the last element:")
print("Sorted list of tuples (by last element):", tuple_list)

# Method 20: Sorting a list of strings by the number of vowels
def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')
string_list.sort(key=count_vowels)
print("\nMethod 20: Sorting a list of strings by the number of vowels:")
print("Sorted list by number of vowels:", string_list)
