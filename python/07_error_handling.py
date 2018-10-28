# User input
# input()

# name = input()

# Including a prompt
# name = input("Enter your name: ")
# print(name)

# Must convert from a string to the data type you want
# age_str = input("Enter your age: ")
# age = int(age_str)
# print(age)

# total = 0
# while True:
#     num = input("Enter a number: ")
#     if not num: break
#     total += int(num)
#     print("Total: " + str(total))

# num_inp = input("Give me a number: ")
# if not num_inp.isdigit():
#     print("Fine, be that way")
# else:
#     print(int(num_inp) * 7)

# Try & except
# try:
#     inp = input("Enter a number: ")
#     inp_int = int(inp)
# except:
#     inp_int = None
#     print("That's not a number I know about!")

# Except can refer to a specific exception
# try:
#     inp = input("Enter a number: ")
#     inp_int = int(inp)
# except ValueError:
#     inp_int = None
#     print("That's not a number I know about!")

# Can have multiple except blocks
# try:
#     inp = input("Enter a number: ")
#     inp_int = int(inp)
# except ValueError:
#     inp_int = None
#     print("That's not a number I know about!")
# except NameError:
#     print("Something when wrong with my code!")
# except:
#     print("I have no idea what went wrong...")

# Can name the exceptions
# try:
#     inp = inpt("Enter a number: ")
#     inp_int = int(inp)
# except ValueError:
#     inp_int = None
#     print("That's not a number I know about!")
# except NameError as e:
#     print("Something when wrong with my code!")
#     print(e)
# except:
#     print("I have no idea what went wrong...")

# Raising our own exceptions
# name = input("Name? ")
# if name[0] == 'R':
#     raise ValueError("I don't like you!")

# Raising after handling
# try:
#     inp = inpt("Enter a number: ")
#     inp_int = int(inp)
# except ValueError:
#     inp_int = None
#     print("That's not a number I know about!")
# except NameError as e:
#     print("Something when wrong with my code!")
#     print(e)
#     raise e
# except:
#     print("I have no idea what went wrong...")
#     raise

# Finally
# try:
#     inp = inpt("Enter a number: ")
#     inp_int = int(inp)
# except ValueError:
#     inp_int = None
#     print("That's not a number I know about!")
# except NameError as e:
#     print("Something when wrong with my code!")
#     print(e)
#     raise e
# except:
#     print("I have no idea what went wrong...")
#     raise
# finally:
#     print("All done!")

# Else will handle if there wasn't an exception call
# try:
#     inp = input("Enter a number: ")
#     inp_int = int(inp)
# except ValueError:
#     inp_int = None
#     print("That's not a number I know about!")
# except NameError as e:
#     print("Something when wrong with my code!")
#     print(e)
#     raise e
# except:
#     print("I have no idea what went wrong...")
#     raise
# else:
#     print("Somehow, everything went according to plan")
# finally:
#     print("All done!")

# Working with files
# with open("recipe.txt") as input_file:
#     recipe = input_file.read()
#
# print(recipe)

# Iterating through lines
# with open("recipe.txt") as input_file:
#     for line in input_file:
#         print("New line: " + line.strip()) # strip is like chomp

# Writing to a file
words = ['hello', 'there', 'old', 'chum']
# Traditional r: read, w: write, a: append, suffixed b: binary
with open("myfile.txt", 'w') as output_file:
    for word in words:
        output_file.write(word + '\n')

words = ['', 'see', 'you', 'later', 'alligator']
with open("myfile.txt", 'a') as output_file:
    for word in words:
        output_file.write(word + '\n')
