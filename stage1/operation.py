# . What are Operators?

# Operators are symbols that perform actions on values or variables.

#  Types of Operators
# Arithmetic Operators

# Used for basic math.

a = 10
b = 3

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division (gives float)
print(a // b) # Floor division (removes decimal)
print(a % b)  # Modulus (remainder)
print(a ** b) # Exponentiation (power)



# Comparison Operators

# Compare two values, return True or False.

x = 10
y = 5

print(x == y)  # Equal to
print(x != y)  # Not equal to
print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater or equal
print(x <= y)  # Less or equal



a = 10
b = 5

print(a > 3 and b < 10)  # True if both true
print(a > 20 or b < 10)  # True if any one true
print(not(a > 3))        # Reverse the result



# is → check karta hai kya dono variables same memory object ko point kar rahe hain.

# == → check karta hai kya dono variables ke values same hain



a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True  (values same)
print(a is b)  # False (different memory)
print(a is c)  # True  (same object)
