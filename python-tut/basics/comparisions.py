# Lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]
print("List Equality:")
print("List1 equals List2:", list1 == list2)  # Output: True
print("List1 equals List3:", list1 == list3)  # Output: False

# Tuples
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (3, 2, 1)
print("\nTuple Equality:")
print("Tuple1 equals Tuple2:", tuple1 == tuple2)  # Output: True
print("Tuple1 equals Tuple3:", tuple1 == tuple3)  # Output: False

# Sets
set1 = {1, 2, 3}
set2 = {3, 2, 1}
set3 = {4, 5, 6}
print("\nSet Equality:")
print("Set1 equals Set2:", set1 == set2)  # Output: True
print("Set1 equals Set3:", set1 == set3)  # Output: False

# Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
dict3 = {'a': 1, 'c': 3}
print("\nDictionary Equality:")
print("Dict1 equals Dict2:", dict1 == dict2)  # Output: True
print("Dict1 equals Dict3:", dict1 == dict3)  # Output: False

# Membership Test
sequence = [1, 2, 3, 4, 5]
print("\nMembership Test:")
print("3 in Sequence:", 3 in sequence)  # Output: True
print("6 not in Sequence:", 6 not in sequence)  # Output: True

# Ordering Comparison
print("\nOrdering Comparison:")
print("List1 > List2:", list1 > list2)  # Output: False
print("List1 < List3:", list1 < list3)  # Output: False

# String Comparison
str1 = "hello"
str2 = "world"
print("\nString Comparison:")
print("str1 == str2:", str1 == str2)  # Output: False
print("str1 < str2:", str1 < str2)    # Output: True (lexicographical order)

# Numeric Comparison
int1 = 10
int2 = 20
print("\nNumeric Comparison:")
print("int1 == int2:", int1 == int2)  # Output: False
print("int1 < int2:", int1 < int2)    # Output: True

# Combining Comparisons
print("\nCombining Comparisons:")
print("int1 in sequence:", int1 in sequence)  # Output: True
print("tuple1 not in sequence:", tuple1 not in sequence)  # Output: True

# Additional Examples:
# More examples can be added here covering various scenarios and edge cases.
# These can include comparisons between different types, comparisons involving NaN and None, etc.


# Lists
list4 = [1, 2, 3, 4, 5]
list5 = [1, 2, 3, 4, 5]
list6 = [1, 2, 4, 3, 5]
print("\nMore List Examples:")
print("List4 equals List5:", list4 == list5)  # Output: True
print("List4 equals List6:", list4 == list6)  # Output: False

# Tuples
tuple4 = (1, 2, 3, 4, 5)
tuple5 = (1, 2, 3, 4, 5)
tuple6 = (1, 2, 4, 3, 5)
print("\nMore Tuple Examples:")
print("Tuple4 equals Tuple5:", tuple4 == tuple5)  # Output: True
print("Tuple4 equals Tuple6:", tuple4 == tuple6)  # Output: False

# Sets
set4 = {1, 2, 3, 4, 5}
set5 = {5, 4, 3, 2, 1}
set6 = {1, 2, 4, 3, 5}
print("\nMore Set Examples:")
print("Set4 equals Set5:", set4 == set5)  # Output: True
print("Set4 equals Set6:", set4 == set6)  # Output: False

# Dictionaries
dict4 = {'a': 1, 'b': 2, 'c': 3}
dict5 = {'a': 1, 'b': 2, 'c': 3}
dict6 = {'c': 3, 'b': 2, 'a': 1}
print("\nMore Dictionary Examples:")
print("Dict4 equals Dict5:", dict4 == dict5)  # Output: True
print("Dict4 equals Dict6:", dict4 == dict6)  # Output: False

# String Comparison
str3 = "hello"
str4 = "world"
print("\nMore String Examples:")
print("str3 == str4:", str3 == str4)  # Output: False
print("str3 < str4:", str3 < str4)    # Output: True (lexicographical order)

# Numeric Comparison
int3 = 10
int4 = 20
print("\nMore Numeric Examples:")
print("int3 == int4:", int3 == int4)  # Output: False
print("int3 < int4:", int3 < int4)    # Output: True

# Additional Examples:
# More examples can be added here covering various scenarios and edge cases.
# These can include comparisons between different types, comparisons involving NaN and None, etc.
