

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
print (a + b + c ) # Error
