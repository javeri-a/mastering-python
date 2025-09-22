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
 
for i in range (1, 111):
    print(i)


m1 = int(input("Enter marks for subject English:"))
m2 = int(input("Enter marks for subject Urdu:"))       
m3 = int(input("Enter marks for subject Math:"))
average = (m1 + m2 + m3) / 3 # Calculate average
print("The average is:", average) 
