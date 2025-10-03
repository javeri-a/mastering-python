# Lists in Python

# A list is a collection of items.


# You can store numbers, strings, or even other lists inside it.

# Lists are mutable, meaning you can change, add, or remove items.

# Lists are written inside square brackets [ ].


fruits = ["apple", "banana", "cherry", "kiwi"]
print(fruits)  # ['apple', 'banana', 'cherry', 'kiwi']

print(fruits[0])

fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'kiwi']

fruits.append("orange")
print(fruits)  # ['apple', 'cherry', 'kiwi', 'orange

fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'kiwi', 'orange']


# List Slicing
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[2:5])  # [30, 40, 50]
print(numbers[:4])   # [10, 20, 30, 40]
print(numbers[3:])   # [40, 50, 60, 70]
print(numbers[-3:])  # [50, 60, 70]
print(numbers[:-3])  # [10, 20, 30, 40]
print(numbers[::2])  # [10, 30, 50, 70]
print(numbers[::-1]) # [70, 60, 50, 40,
