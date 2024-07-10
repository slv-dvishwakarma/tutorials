# Define a list
my_list = [1, 2, 3, 4, 5]

# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

# List methods
print("List methods:")
# Append
my_list.append(6)
print("Appended list:", my_list)    # Output: [1, 2, 3, 4, 5, 6]
# Extend
my_list.extend([7, 8, 9])
print("Extended list:", my_list)    # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Insert
my_list.insert(2, 10)
print("Inserted list:", my_list)    # Output: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]
# Remove
my_list.remove(5)
print("Removed list:", my_list)     # Output: [1, 2, 10, 3, 4, 6, 7, 8, 9]
# Pop
popped_element = my_list.pop()
print("Popped element:", popped_element)    # Output: 9
print("List after pop:", my_list)           # Output: [1, 2, 10, 3, 4, 6, 7, 8]
# Index
index_of_10 = my_list.index(10)
print("Index of 10:", index_of_10)          # Output: 2
# Count
count_of_3 = my_list.count(3)
print("Count of 3:", count_of_3)            # Output: 1
# Reverse
my_list.reverse()
print("Reversed list:", my_list)            # Output: [8, 7, 6, 4, 3, 10, 2, 1]
# Sort
my_list.sort()
print("Sorted list:", my_list)              # Output: [1, 2, 3, 4, 6, 7, 8, 10]
print()

# Tuple methods
print("Tuple methods:")
# Tuples are immutable, so they have fewer methods compared to lists
# Count
count_of_3 = my_tuple.count(3)
print("Count of 3 in tuple:", count_of_3)  # Output: 1
# Index
index_of_4 = my_tuple.index(4)
print("Index of 4 in tuple:", index_of_4)  # Output: 3
print()

# List vs Tuple comparison
print("List vs Tuple comparison:")
# List is mutable, Tuple is immutable
# This means lists can be modified after creation, while tuples cannot
# Lists use square brackets [], Tuples use parentheses ()
# Lists are generally used when we have a collection of similar items that might need to be changed or updated, 
# while Tuples are used when we have a collection of heterogeneous items that should remain constant.
# Example:
# List of student names
students_list = ["Alice", "Bob", "Charlie"]
# Tuple of student details (name, age, grade)
student_tuple = ("Alice", 20, "A")
print("List of students:", students_list)
print("Tuple of student details:", student_tuple)
