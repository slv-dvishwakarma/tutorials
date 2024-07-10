# Creating an empty set
empty_set = set()
print("1. Empty set:", empty_set)

# Creating a set with initial values
my_set = {1, 2, 3}
print("\n2. Set with initial values:", my_set)

# Adding elements to a set
my_set.add(4)
print("\n3. After adding element to set:", my_set)

# Adding multiple elements to a set
my_set.update([5, 6, 7])
print("\n4. After adding multiple elements to set:", my_set)

# Removing an element from a set
my_set.remove(4)
print("\n5. After removing an element from set:", my_set)

# Discarding an element from a set
my_set.discard(5)
print("\n6. After discarding an element from set:", my_set)

# Clearing all elements from a set
my_set.clear()
print("\n7. After clearing all elements from set:", my_set)

# Creating a set from a list
my_list = [1, 2, 3, 4, 5]
set_from_list = set(my_list)
print("\n8. Set created from a list:", set_from_list)

# Union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("\n9. Union of sets:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("\n10. Intersection of sets:", intersection_set)

# Difference between sets
difference_set = set1.difference(set2)
print("\n11. Difference between sets (set1 - set2):", difference_set)

# Symmetric difference between sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("\n12. Symmetric difference between sets:", symmetric_difference_set)

# Checking if a set is a subset of another set
subset1 = {1, 2}
subset2 = {1, 2, 3}
print("\n13. Checking if a set is a subset of another set:")
print("Is subset1 a subset of subset2:", subset1.issubset(subset2))
print("Is subset2 a subset of subset1:", subset2.issubset(subset1))

# Checking if a set is a superset of another set
print("\n14. Checking if a set is a superset of another set:")
print("Is subset1 a superset of subset2:", subset1.issuperset(subset2))
print("Is subset2 a superset of subset1:", subset2.issuperset(subset1))

# Checking if two sets are disjoint
set3 = {4, 5, 6}
print("\n15. Checking if two sets are disjoint:")
print("Are set1 and set3 disjoint:", set1.isdisjoint(set3))

# Copying a set
copied_set = set1.copy()
print("\n16. Copied set:", copied_set)

# Creating a frozen set
frozen_set = frozenset(my_list)
print("\n17. Frozen set:", frozen_set)

# Iterating over a set
print("\n18. Iterating over a set:")
for item in set1:
    print(item)

# Converting set to list
set_to_list = list(set1)
print("\n19. Set converted to list:", set_to_list)

# Converting set to tuple
set_to_tuple = tuple(set1)
print("\n20. Set converted to tuple:", set_to_tuple)

# Getting the length of a set
print("\n21. Length of set1:", len(set1))

# Checking if an element is in a set
print("\n22. Checking if an element is in a set:")
print("Is 3 in set1:", 3 in set1)
print("Is 6 in set1:", 6 in set1)

# Removing and returning an arbitrary element from a set
arbitrary_element = set1.pop()
print("\n23. Removed and returned arbitrary element from set1:", arbitrary_element)
print("After popping, set1:", set1)

# Updating a set with union
set1 |= {5, 6}
print("\n24. Updated set1 with union:", set1)

# Updating a set with intersection
set1 &= {3, 4, 5}
print("\n25. Updated set1 with intersection:", set1)

# Updating a set with difference
set1 -= {3}
print("\n26. Updated set1 with difference:", set1)

# Updating a set with symmetric difference
set1 ^= {4, 5}
print("\n27. Updated set1 with symmetric difference:", set1)

# Checking if a set is empty
print("\n28. Checking if a set is empty:")
print("Is set1 empty:", not bool(set1))

# Creating a set of unique characters from a string
my_string = "hello"
unique_characters_set = set(my_string)
print("\n29. Set of unique characters from string:", unique_characters_set)

# Checking if a set contains only unique elements
repeated_set = {1, 2, 3, 1, 2, 3}
print("\n30. Checking if a set contains only unique elements:")
print("Is repeated_set containing only unique elements:", len(repeated_set) == len(set(repeated_set)))

# Creating a set of even numbers using comprehension
even_set = {x for x in range(10) if x % 2 == 0}
print("\n31. Set of even numbers using comprehension:", even_set)

# Creating a set of vowels using comprehension
vowels = {'a', 'e', 'i', 'o', 'u'}
consonants = {letter for letter in 'abcdefghijklmnopqrstuvwxyz' if letter not in vowels}
print("\n32. Set of consonants using comprehension:", consonants)

# Creating a set of common elements between two lists using intersection
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements_set = set(list1).intersection(list2)
print("\n33. Set of common elements between two lists using intersection:", common_elements_set)
