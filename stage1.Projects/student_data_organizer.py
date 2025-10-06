
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









# ---------- STUDENT DATA ORGANIZER ----------

# Step 1: User se basic info lena
print("======== STUDENT DATA ORGANIZER ========")

# Name input with proper formatting
name = input("Enter your name: ").strip().title()

# Age input with safety (only numbers)
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a valid number for age.")

# University fixed value (string)
university = "Virtual University"

# Step 2: Subjects list (mutable)
subjects = ["Python", "Math", "AI", "Data Science"]

# Step 3: Convert subjects list into tuple (immutable snapshot)
subject_tuple = tuple(subjects)

# Step 4: Skills set (unique values only)
skills = {"Python", "Git", "AI", "Python"}  # "Python" repeat remove ho jayegi

# Step 5: Print all details
print("\n----- STUDENT CARD -----")
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"University : {university}")
print(f"Subjects   : {', '.join(subjects)}")
print(f"Skills     : {', '.join(sorted(skills))}")

# Step 6: Identity vs Equality check
a = subjects
b = subjects.copy()

print("\n----- MEMORY CHECK -----")
print("a == b:", a == b)  # Values compare
print("a is b:", a is b)  # Memory compare

# Step 7: Modify subjects (demonstrate mutability)
subjects.append("Machine Learning")
print("\nUpdated subjects list:", subjects)
print("Original tuple (unchanged):", subject_tuple)

# Step 8: Remove duplicates from random marks (using set)
random_marks = [85, 90, 90, 95, 85]
unique_marks = sorted(list(set(random_marks)))  # Sorted unique list

print("\nMarks entered:", random_marks)
print("Unique sorted marks:", unique_marks)

# Step 9: Display summary neatly
print("\n======== SUMMARY REPORT ========")
print(f"Student {name} (Age {age}) from {university} has {len(subjects)} subjects and {len(skills)} unique skills.")
print("All data processed successfully.")

print("\n======== END ========")