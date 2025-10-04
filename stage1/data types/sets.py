# Sets in Python

# Definition

# Set ek unordered collection hai unique elements ka.

# Matlab, ek hi value bar bar add karo to sirf ek hi store hogi.

# Syntax: {} curly braces use hote hain.


my_set = {1, 2, 3, 4, 5, 2, 3}
print(my_set)  # Output: {1, 2, 3, 4, 5} # Duplicates removed

fruits = {"apple", "banana"}
fruits.add("orange")      # Add item
fruits.remove("banana")   # Remove item
print(fruits)  # Output: {'apple', 'orange'}


A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)   # Union → {1,2,3,4,5}
print(A & B)   # Intersection → {3}
print(A - B)   # Difference → {1,2}
print(A ^ B)   # Symmetric Difference → {1,2,4,5}


cities = {"Makkah", "Madinah", "Riyadh"}
cities.add("karachi")
cities.remove ("Riyadh")
print (cities) #{' Makkah', 'karachi', 'Madinah'}
