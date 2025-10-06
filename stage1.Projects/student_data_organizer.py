
#_______________STUDENT___DATA___ORGANIZER_______________#


name = input ("Enter your name:").title()
age  = int(input("Enter your age:"))
university = "GIAIC"




# Step 2: Store subjects in a list
subjects = ["Python", "Math", "AI", "Data Science"]

# Step 3: Convert subjects list to a tuple (immutable record)
subject_tuple = tuple(subjects)

# Step 4: Make a set of skills to avoid duplicates
skills = {"Python", "Git", "AI", "Python"}  # "Python" repeated, but set removes duplicates

# Step 5: Display all info neatly
print("\n----- STUDENT CARD -----")
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"University : {university}")
print(f"Subjects   : {subject_tuple}")
print(f"Skills     : {skills}")

# Step 6: Identity vs Equality check
a = subjects
b = subjects.copy()

print("\n----- MEMORY CHECK -----")
print("a == b:", a == b)  # same values
print("a is b:", a is b)  # different memory location

# Step 7: Add a new subject and show updated list
subjects.append("Machine Learning")
print("\nUpdated subjects:", subjects)

# Step 8: Remove duplicates from a random list using set
random_marks = [85, 90, 90, 95, 85]
unique_marks = list(set(random_marks))
print("Unique Marks:", unique_marks)
