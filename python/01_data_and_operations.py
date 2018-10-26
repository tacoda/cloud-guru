# Numbers
12
37
-5
0
2.5
3.14159
-437.2

# Strings
'Hello, World!'
"Another string"

# Triple-quoted string for new lines
'''I can have
more than one
line'''
print('A string with\nmore than one line')
# You can also use """ for this
"My dog's name is Domino"
'My cats\'s name is Eskay'
print('A single \\ backslash')

# Lists
[1, 2, 3, 4, 5]
["milk", "eggs", "butter", "bread"]
[10.2, "different", 5, "data types"]

# Variables
age = 40
groceries = ["milk", "eggs", "butter", "bread"]
# Letters, numbers or underscores (has to start with a letter)
# Convention is lowercase and underscores
tv_show = "M.A.S.H."
# Dynamic types (variable is just a name and it points to some data: the data has the type)

# Constructors
# Can be used to create an empty value
# Mostly used to convert from one data type to another
str()
str(5)
# print("I have " + 5 + " apples.") # Error
print("I have " + str(5) + " apples.")
int()
float()
float(132)
int(3.14159)
list()
list("Hello, my dear!")
# list(5) # Error

5 + 3
8 - 2
5 * 3
-44 / 2
3 ** 5 # Exponentiation
(2 + 8) / 4

greeting = "Hello, "
name = "George"
greeting + name # Concatenation
"na " * 5 + "batman!" # Repeat

# Concatenation and repetition for lists too
['na'] * 5 + ['batman!']

seconds = 24 * 60 * 60
print(seconds)
emails = ['a@email.com', 'b@email.com', 'c@email.com']
emails += ['d@email.com', 'e@email.com']
print(emails)
print(3 ** 10 / 5)
