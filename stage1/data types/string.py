

# Strings in Python

# String = text data (letters, words, sentences).

# Python me string ko quotes me likhte hain:

# Single quotes: 'hello'

# Double quotes: "hello"

# Multi-line: '''hello''' or """hello"""

print ("hello world")  # Simple string print
print ('hello world')  # Simple string print
print ('''hello world''')  # Multi-line string print
print ("""hello world""")  # Multi-line string print

#          ----------Immutable nature of Strings----------

# Matlab: ek baar string ban gayi, usko directly change nahi kar sakte.

# Agar change karoge, Python nayi string create karega.


name = "Javeria"
print(name.upper())  #JAVERIA
print(name.lower()) #javeria
print (name) #Javeria


a = 1
b = 2
c= "5"
print (a + b + int(c) ) #8
# print (a + b + c ) # Error



# String Operations

# Concatenation (join):
first_name = "Javeria"
last_name = "Qureshi"
full_name = first_name + " " + last_name  # Space bhi add kiya
print(full_name)  # Output: Javeria Qureshi

#REPITITION
print ("I LOVE HAZRAT MUHAMMAD SALLALAHU ALAIHI WASSALAM ❤ " * 100)


# Indexing (single character):
name = "Javeria"
print(name[0])  # Output: J (first character)
print(name[-1])  # Output: a (last character)
print(name[2])  # Output: v (third character)
print(name[-3])  # Output: r (third last character)
print(name[1])  # Output: a (second character)


# Slicing (substring):

print("python"[0:3])   # Pyt
print("python "[2:])    # thon


# Apna naam ek variable me store karo aur uska first letter print karo.

my_name = "Javeria"
print(my_name[0])  # Output: J

# Apni favourite city ka naam likho aur usko uppercase aur lowercase me print karo.
favcity = "Makkah  and Madinah"
print (favcity.upper())
print (favcity.lower())


# Ek sentence lo "I love Python" aur usme "Python" ko "Coding" se replace karo.
sentence = "I love Python❤"
new_sentence = sentence.replace("Python", "Coding")
print(new_sentence)  # Output: I love Coding




# Ek string "abcdefg" lo aur uska sirf middle part print karo
new2:str = "abcefghijklmnopqrstuvwxyz"
print (new2 [8:18])
