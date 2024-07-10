# Example 1: Using iterators to iterate over a list
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

print("Using iterator to iterate over a list:")
while True:
    try:
        item = next(my_iter)
        print(item)
    except StopIteration:
        break

# Example 2: Implementing a custom iterator for a range of numbers
class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            value = self.start
            self.start += 1
            return value
        else:
            raise StopIteration

print("\nImplementing a custom iterator for a range of numbers:")
my_range = MyRange(1, 6)
for num in my_range:
    print(num)

# Example 3: Using generators to generate an infinite sequence of numbers
def count():
    num = 1
    while True:
        yield num
        num += 1

print("\nUsing generators to generate an infinite sequence of numbers:")
counter = count()
for _ in range(5):
    print(next(counter))

# Example 4: Using generators to generate Fibonacci numbers
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\nUsing generators to generate Fibonacci numbers:")
fib_seq = fibonacci()
for _ in range(10):
    print(next(fib_seq))

# Example 5: Using generator expressions to filter even numbers
even_numbers = (x for x in range(10) if x % 2 == 0)
print("\nUsing generator expressions to filter even numbers:")
print(list(even_numbers))

# Example 6: Using generator expressions to generate squares of numbers
squared_numbers = (x ** 2 for x in range(1, 6))
print("\nUsing generator expressions to generate squares of numbers:")
print(list(squared_numbers))

# Example 7: Using itertools.count to generate an infinite sequence of numbers
import itertools

print("\nUsing itertools.count to generate an infinite sequence of numbers:")
counter = itertools.count(start=1, step=2)
print([next(counter) for _ in range(5)])

# Example 8: Using itertools.cycle to cycle through a sequence of values
colors = ['red', 'green', 'blue']
color_cycle = itertools.cycle(colors)
print("\nUsing itertools.cycle to cycle through a sequence of values:")
print([next(color_cycle) for _ in range(5)])

# Example 9: Using itertools.chain to chain multiple iterables
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
combined = itertools.chain(letters, numbers)
print("\nUsing itertools.chain to chain multiple iterables:")
print(list(combined))

# Example 10: Using itertools.permutations to generate permutations
perms = itertools.permutations([1, 2, 3])
print("\nUsing itertools.permutations to generate permutations:")
print(list(perms))

# Example 11: Using itertools.combinations to generate combinations
combs = itertools.combinations([1, 2, 3], 2)
print("\nUsing itertools.combinations to generate combinations:")
print(list(combs))

# Example 12: Using itertools.product to generate Cartesian product
prod = itertools.product('AB', repeat=2)
print("\nUsing itertools.product to generate Cartesian product:")
print(list(prod))

# Example 13: Using itertools.groupby to group data based on key function
data = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
grouped_data = itertools.groupby(data, key=lambda x: x[0])
print("\nUsing itertools.groupby to group data based on key function:")
for key, group in grouped_data:
    print(key, list(group))

# Example 14: Using itertools.islice to slice an iterable
nums = range(10)
sliced_nums = itertools.islice(nums, 2, 7, 2)
print("\nUsing itertools.islice to slice an iterable:")
print(list(sliced_nums))

# Example 15: Using itertools.dropwhile to drop elements from the beginning of an iterable
nums = [1, 3, 5, 2, 4, 6]
dropped_nums = itertools.dropwhile(lambda x: x < 5, nums)
print("\nUsing itertools.dropwhile to drop elements from the beginning of an iterable:")
print(list(dropped_nums))

# Example 16: Using itertools.takewhile to take elements from the beginning of an iterable
nums = [1, 3, 5, 2, 4, 6]
taken_nums = itertools.takewhile(lambda x: x < 5, nums)
print("\nUsing itertools.takewhile to take elements from the beginning of an iterable:")
print(list(taken_nums))

# Example 17: Using itertools.filterfalse to filter elements not satisfying a condition
nums = [1, 2, 3, 4, 5]
filtered_nums = itertools.filterfalse(lambda x: x % 2 == 0, nums)
print("\nUsing itertools.filterfalse to filter elements not satisfying a condition:")
print(list(filtered_nums))

# Example 18: Using itertools.zip_longest to zip iterables of uneven lengths
letters = ['a', 'b', 'c']
numbers = [1, 2]
zipped = itertools.zip_longest(letters, numbers, fillvalue='NA')
print("\nUsing itertools.zip_longest to zip iterables of uneven lengths:")
print(list(zipped))

# Example 19: Using itertools.tee to create independent iterators from a single iterable
nums = [1, 2, 3, 4, 5]
iter1, iter2 = itertools.tee(nums)
print("\nUsing itertools.tee to create independent iterators from a single iterable:")
print("Iterator 1:", list(iter1))
print("Iterator 2:", list(iter2))

# Example 20: Using itertools.starmap to apply a function to each element of an iterable of tuples
data = [(1, 2), (3, 4), (5, 6)]
result = itertools.starmap(lambda x, y: x + y, data)
print("\nUsing itertools.starmap to apply a function to each element of an iterable of tuples:")
print(list(result))

# Example 21: Using itertools.groupby to group data based on key function
data = [('Alice', 25), ('Bob', 30), ('Alice', 35), ('Charlie', 20)]
grouped_data = itertools.groupby(data, key=lambda x: x[0])
print("\nUsing itertools.groupby to group data based on key function:")
for key, group in grouped_data:
    print(key, list(group))

# Example 22: Using itertools.islice to slice an iterable
nums = range(10)
sliced_nums = itertools.islice(nums, 2, 7, 2)
print("\nUsing itertools.islice to slice an iterable:")
print(list(sliced_nums))

# Example 23: Using itertools.dropwhile to drop elements from the beginning of an iterable
nums = [1, 3, 5, 2, 4, 6]
dropped_nums = itertools.dropwhile(lambda x: x < 5, nums)
print("\nUsing itertools.dropwhile to drop elements from the beginning of an iterable:")
print(list(dropped_nums))

# Example 24: Using itertools.takewhile to take elements from the beginning of an iterable
nums = [1, 3, 5, 2, 4, 6]
taken_nums = itertools.takewhile(lambda x: x < 5, nums)
print("\nUsing itertools.takewhile to take elements from the beginning of an iterable:")
print(list(taken_nums))

# Example 25: Using itertools.filterfalse to filter elements not satisfying a condition
nums = [1, 2, 3, 4, 5]
filtered_nums = itertools.filterfalse(lambda x: x % 2 == 0, nums)
print("\nUsing itertools.filterfalse to filter elements not satisfying a condition:")
print(list(filtered_nums))

# Example 26: Using itertools.zip_longest to zip iterables of uneven lengths
letters = ['a', 'b', 'c']
numbers = [1, 2]
zipped = itertools.zip_longest(letters, numbers, fillvalue='NA')
print("\nUsing itertools.zip_longest to zip iterables of uneven lengths:")
print(list(zipped))

# Example 27: Using itertools.tee to create independent iterators from a single iterable
nums = [1, 2, 3, 4, 5]
iter1, iter2 = itertools.tee(nums)
print("\nUsing itertools.tee to create independent iterators from a single iterable:")
print("Iterator 1:", list(iter1))
print("Iterator 2:", list(iter2))

# Example 28: Using itertools.starmap to apply a function to each element of an iterable of tuples
data = [(1, 2), (3, 4), (5, 6)]
result = itertools.starmap(lambda x, y: x + y, data)
print("\nUsing itertools.starmap to apply a function to each element of an iterable of tuples:")
print(list(result))

# Example 29: Using itertools.groupby to group data based on key function
data = [('Alice', 25), ('Bob', 30), ('Alice', 35), ('Charlie', 20)]
grouped_data = itertools.groupby(data, key=lambda x: x[0])
print("\nUsing itertools.groupby to group data based on key function:")
for key, group in grouped_data:
    print(key, list(group))

# Example 30: Using itertools.islice to slice an iterable
nums = range(10)
sliced_nums = itertools.islice(nums, 2, 7, 2)
print("\nUsing itertools.islice to slice an iterable:")
print(list(sliced_nums))

# Example 31: Using itertools.dropwhile to drop elements from the beginning of an iterable
nums = [1, 3, 5, 2, 4, 6]
dropped_nums = itertools.dropwhile(lambda x: x < 5, nums)
print("\nUsing itertools.dropwhile to drop elements from the beginning of an iterable:")
print(list(dropped_nums))

# Example 32: Using itertools.takewhile to take elements from the beginning of an iterable
nums = [1, 3, 5, 2, 4, 6]
taken_nums = itertools.takewhile(lambda x: x < 5, nums)
print("\nUsing itertools.takewhile to take elements from the beginning of an iterable:")
print(list(taken_nums))

# Example 33: Using itertools.filterfalse to filter elements not satisfying a condition
nums = [1, 2, 3, 4, 5]
filtered_nums = itertools.filterfalse(lambda x: x % 2 == 0, nums)
print("\nUsing itertools.filterfalse to filter elements not satisfying a condition:")
print(list(filtered_nums))

# Example 34: Using itertools.zip_longest to zip iterables of uneven lengths
letters = ['a', 'b', 'c']
numbers = [1, 2]
zipped = itertools.zip_longest(letters, numbers, fillvalue='NA')
print("\nUsing itertools.zip_longest to zip iterables of uneven lengths:")
print(list(zipped))

# Example 35: Using itertools.tee to create independent iterators from a single iterable
nums = [1, 2, 3, 4, 5]
iter1, iter2 = itertools.tee(nums)
print("\nUsing itertools.tee to create independent iterators from a single iterable:")
print("Iterator 1:", list(iter1))
print("Iterator 2:", list(iter2))

# Example 36: Using itertools.starmap to apply a function to each element of an iterable of tuples
data = [(1, 2), (3, 4), (5, 6)]
result = itertools.starmap(lambda x, y: x + y, data)
print("\nUsing itertools.starmap to apply a function to each element of an iterable of tuples:")
print(list(result))

# Example 37: Using itertools.groupby to group data based on key function
data = [('Alice', 25), ('Bob', 30), ('Alice', 35), ('Charlie', 20)]
grouped_data = itertools.groupby(data, key=lambda x: x[0])
print("\nUsing itertools.groupby to group data based on key function:")
for key, group in grouped_data:
    print(key, list(group))

# Example 38: Using itertools.islice to slice an iterable
nums = range(10)
sliced_nums = itertools.islice(nums, 2, 7, 2)
print("\nUsing itertools.islice to slice an iterable:")
print(list(sliced_nums))

# Example 39: Using itertools.dropwhile to drop elements from the beginning of an iterable
nums = [1, 3, 5, 2, 4, 6]
dropped_nums = itertools.dropwhile(lambda x: x < 5, nums)
print("\nUsing itertools.dropwhile to drop elements from the beginning of an iterable:")
print(list(dropped_nums))

# Example 40: Using itertools.takewhile to take elements from the beginning of an iterable
nums = [1, 3, 5, 2, 4, 6]
taken_nums = itertools.takewhile(lambda x: x < 5, nums)
print("\nUsing itertools.takewhile to take elements from the beginning of an iterable:")
print(list(taken_nums))

# Example 41: Using itertools.filterfalse to filter elements not satisfying a condition
nums = [1, 2, 3, 4, 5]
filtered_nums = itertools.filterfalse(lambda x: x % 2 == 0, nums)
print("\nUsing itertools.filterfalse to filter elements not satisfying a condition:")
print(list(filtered_nums))

# Example 42: Using itertools.zip_longest to zip iterables of uneven lengths
letters = ['a', 'b', 'c']
numbers = [1, 2]
zipped = itertools.zip_longest(letters, numbers, fillvalue='NA')
print("\nUsing itertools.zip_longest to zip iterables of uneven lengths:")
print(list(zipped))

# Example 43: Using itertools.tee to create independent iterators from a single iterable
nums = [1, 2, 3, 4, 5]
iter1, iter2 = itertools.tee(nums)
print("\nUsing itertools.tee to create independent iterators from a single iterable:")
print("Iterator 1:", list(iter1))
print("Iterator 2:", list(iter2))

# Example 44: Using itertools.starmap to apply a function to each element of an iterable of tuples
data = [(1, 2), (3, 4), (5, 6)]
result = itertools.starmap(lambda x, y: x + y, data)
print("\nUsing itertools.starmap to apply a function to each element of an iterable of tuples:")
print(list(result))
