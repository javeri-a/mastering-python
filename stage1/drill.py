# This program adds two numbers provided by the user

num1 = int(input("Enter your 1st number:"))
num2 = int(input("Enter your 2nd number:"))

print("the sum is:", num1 + num2)
print("successfully added!")


name = input("Enter your name:")
city = input("Enter your city:")
print(name, "lives in", city) # using commas
print("hello! my name is " + name + " and  am from " + city) # string concatenation



# Even or Odd
num  = int(input("Enter a number:"))
if num % 2 == 0:
    print(num, "is an Even number")
else:
    print(num, "is an Odd number")
