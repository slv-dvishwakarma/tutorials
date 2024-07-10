# Creating an empty dictionary
empty_dict = {}
print("1. Empty dictionary:", empty_dict)

# Creating a dictionary with initial values
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("\n2. Dictionary with initial values:", my_dict)

# Accessing values using keys
print("\n3. Accessing values using keys:")
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])

# Adding a new key-value pair
my_dict['gender'] = 'Female'
print("\n4. After adding a new key-value pair:", my_dict)

# Updating an existing value
my_dict['age'] = 35
print("\n5. After updating an existing value:", my_dict)

# Deleting a key-value pair
del my_dict['city']
print("\n6. After deleting a key-value pair:", my_dict)

# Checking if a key exists
print("\n7. Checking if a key exists:")
print("'name' in my_dict:", 'name' in my_dict)
print("'city' in my_dict:", 'city' in my_dict)

# Getting the list of keys and values
print("\n8. Getting the list of keys and values:")
print("Keys:", list(my_dict.keys()))
print("Values:", list(my_dict.values()))

# Getting the list of key-value pairs (items)
print("\n9. Getting the list of key-value pairs:")
print("Items:", list(my_dict.items()))

# Iterating over key-value pairs
print("\n10. Iterating over key-value pairs:")
for key, value in my_dict.items():
    print(key, ":", value)

# Clearing all key-value pairs
my_dict.clear()
print("\n11. After clearing all key-value pairs:", my_dict)

# Creating a dictionary with default values
from collections import defaultdict
default_dict = defaultdict(int)
default_dict['a'] += 1
default_dict['b'] += 2
print("\n12. Dictionary with default values:", dict(default_dict))

# Merging dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print("\n13. Merged dictionary:", merged_dict)

# Creating a dictionary from keys and default value
keys = ['a', 'b', 'c']
default_value = 0
dict_from_keys = dict.fromkeys(keys, default_value)
print("\n14. Dictionary created from keys:", dict_from_keys)

# Getting the value for a key with a default value if key doesn't exist
print("\n15. Getting value for a key with default value if key doesn't exist:")
print("Value for key 'd':", dict_from_keys.get('d', 'Key not found'))

# Counting occurrences of elements using a dictionary
my_list = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
count_dict = {}
for item in my_list:
    count_dict[item] = count_dict.get(item, 0) + 1
print("\n16. Counting occurrences of elements using a dictionary:", count_dict)

# Creating a dictionary with comprehension
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict_comp = {k: v for k, v in zip(keys, values)}
print("\n17. Dictionary created with comprehension:", dict_comp)

# Filtering dictionary based on conditions
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = {k: v for k, v in my_dict.items() if v % 2 == 0}
print("\n18. Filtered dictionary based on conditions:", filtered_dict)

# Sorting a dictionary by keys
my_dict = {'b': 3, 'a': 1, 'c': 2}
sorted_dict_keys = dict(sorted(my_dict.items()))
print("\n19. Dictionary sorted by keys:", sorted_dict_keys)

# Sorting a dictionary by values
sorted_dict_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("\n20. Dictionary sorted by values:", sorted_dict_values)

# Reversing keys and values in a dictionary
reversed_dict = {v: k for k, v in my_dict.items()}
print("\n21. Dictionary with reversed keys and values:", reversed_dict)

# Creating a nested dictionary
nested_dict = {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}
print("\n22. Nested dictionary:", nested_dict)

# Accessing values in a nested dictionary
print("\n23. Accessing values in a nested dictionary:")
print("Value of 'a' -> 'x':", nested_dict['a']['x'])
print("Value of 'b' -> 'y':", nested_dict['b']['y'])

# Updating values in a nested dictionary
nested_dict['a']['x'] = 10
nested_dict['b']['y'] = 20
print("\n24. After updating values in a nested dictionary:", nested_dict)

# Deleting a key-value pair in a nested dictionary
del nested_dict['b']['x']
print("\n25. After deleting a key-value pair in a nested dictionary:", nested_dict)

# Flattening a nested dictionary
import itertools
flattened_dict = dict(itertools.chain.from_iterable(d.items() for d in nested_dict.values()))
print("\n26. Flattened nested dictionary:", flattened_dict)

# Creating a dictionary with maximum and minimum values
max_min_dict = {'a': 10, 'b': 20, 'c': 30}
max_key = max(max_min_dict, key=max_min_dict.get)
min_key = min(max_min_dict, key=max_min_dict.get)
print("\n27. Dictionary with maximum and minimum values:")
print("Key with maximum value:", max_key)
print("Key with minimum value:", min_key)

# Checking if all elements in a dictionary are True
all_true_dict = {'a': True, 'b': True, 'c': False}
print("\n28. Checking if all elements in a dictionary are True:", all(all_true_dict.values()))

# Checking if any element in a dictionary is True
print("\n29. Checking if any element in a dictionary is True:", any(all_true_dict.values()))

# Creating a dictionary of dictionaries
dict_of_dicts = {1: {'a': 1, 'b': 2}, 2: {'c': 3, 'd': 4}}
print("\n30. Dictionary of dictionaries:", dict_of_dicts)

# Updating dictionaries using unpacking
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2)
print("\n31. Updated dictionary using unpacking:", dict1)

# Creating a dictionary with default value factory
from collections import defaultdict
def default_value():
    return 'N/A'

default_dict = defaultdict(default_value)
default_dict['a'] = 1
print("\n32. Dictionary with default value factory:", dict(default_dict))

# Creating a dictionary with keys sorted by length
words = ['apple', 'banana', 'orange', 'kiwi']
sorted_keys_dict = {k: 'fruit' for k in sorted(words, key=len)}
print("\n33. Dictionary with keys sorted by length:", sorted_keys_dict)
