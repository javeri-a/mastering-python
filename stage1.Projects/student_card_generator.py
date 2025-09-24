#________________STUDENT__CARD__GENERATOR___________________

print("__________STUDENT CARD__________")
name : str = "Javeria qureshi"
print(f"Name       : {name.title()}")


age : str = "20"
print(f"Age        : {age}")

course : str = "Agent AI Developer"
print(f"Course     : {course.upper()}")

university :str = "virtual university"
print(f"University : {university.title()}")




#________________STUDENT__CARD__GENERATOR___________________

print("---------- STUDENT CARD ----------")

# User input
name: str = input("Enter your name: ")
age: str = input("Enter your age: ")
course: str = input("Enter your course: ")
university: str = input("Enter your university: ")

# Output with formatting
print("\n---------- GENERATED CARD ----------")
print(f"Name       : {name.title()}")
print(f"Age        : {age}")
print(f"Course     : {course.upper()}")
print(f"University : {university.title()}")
print("------------------------------------")
