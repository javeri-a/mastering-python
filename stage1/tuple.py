# . What is a Tuple?

# Tuple ek data type hai Python me.

# Ye list ki tarah hota hai, lekin immutable (badal nahi sakte).

# Brackets: ()


my_tuple = (1, 2, 3, 4, 5)
print (my_tuple) #(1, 2, 3, 4, 5)





# animals = ("cat", "dog", "lion")

# print(animals[0])   # cat
# print(animals[-1])  # lion


colors = ("red", "black", "pink")
print(colors[0])   
print (colors [1])# red
print (colors [-1])  # pink
print (colors [-2])  # black
print (colors) #('red', 'black', 'pink')

# Tuple me hum elements ko change nahi kar sakte.

# Tuple Slicing
letters = ("a", "b", "c", "d", "e")

print(letters[1:4])   # ('b', 'c', 'd')
print(letters[:3])    # ('a', 'b', 'c')

# Tuple Methods
# .count() → Kitni dafa element repeat hua.

# .index() → Element ki position.

num = (1, 2, 3, 1, 4, 1)
print  (num.count(1))  #ye count kr k batata hai 1 kitnidafa aya hai
print (num.index(4))  #ye batata hai 4 kis index pr hai

# Tuple Unpacking
student = ("Javeria", 20, "Agent AI Developer", "Virtual University")
name, age, course, university = student
print(name)        # Javeria
print(age)         # 20 
print(course)      # Agent AI Developer
print(university)  # Virtual University
print(student)  # ('Javeria', 20, 'Agent AI Developer', 'Virtual University')
print (name, age, course, university) #Javeria 20 Agent AI Developer Virtual University


# Ek tuple banao weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun") aur Wednesday print karo.
week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print (week [2])


# Apna naam tuple me store karo (first_name, last_name) aur dono print karo.
name1 = ("javeria" , "qureshi")
print (name1 [0])
print (name1 [1])
print (name1 [-1])
print (name1 [-2])



# Student record as a tuple
student = ("Javeria Qureshi", 20, "Agent AI Developer", "Virtual University")

# Printing formatted Student Card
print("------------------------------")
print("       STUDENT ID CARD        ")
print("------------------------------")
print(f"Name      : {student[0]}")
print(f"Age       : {student[1]}")
print(f"Course    : {student[2].upper()}")
print(f"University: {student[3].title()}")
print("------------------------------")
print("Note: Course in uppercase, University in title case")
print("------------------------------")