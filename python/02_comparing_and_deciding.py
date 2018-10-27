# Booleans
True
False

# Comparison operators
5 == 5
'a string' == "a string"
'A string' != 'a string'
3 < 5
137 > 20.05
3 >= 3.0
0.1 + 0.1 + 0.1 == 0.3
"apple" < "pineapple"
"apple" in "pineapple"
"pine" in "pineapple"
"pile" in "pineapple"
5 in [1, 2, 3, 4, 5]
# in only works for iterable

if "key" in "monkey":
    print("Oook!")

if "banana" in "monkey":
    print("Nanas!")

if "monk" in "monkey":
    print("Monkey! Spit that out!")
    print("...")
    print("Yuck! Don't eat the monk!")

name = "Robin"
if name < "Robin":
    print("Go to the head of the line!")
else:
    print("Hey, no cutting in line!")

if name < "Robin":
    print("Go to the head of the line!")
elif name == "Robin":
    print("Great name!")
else:
    print("Hey, no cutting in line!")

# Falsy types: 0, '', []

name = ''
if name:
    print("Hello, " + name)
else:
    print("You forgot to enter a name!")

cart = []
if cart:
    print("Ready to check out?")
else:
    print("Start shopping!")

cart = ['bananas']
if cart:
    print("Ready to check out?")
else:
    print("Start shopping!")

True and True
False or True
not True

if name and len(name) > 2:
    print("Hello, " + name)
else:
    print("You forgot to enter a name!")

name = 'Robin'
if name: print("Hello, " + name)
# Equivalent to
name and print("Hello, " + name)

name = ''
name and print("Hello, " + name)

name = name or 'Nemo'
print(name)

name = 'Robin'
name = name or 'Nemo'
print(name)

True and not True
False or not False
"cheese" < "crackers"
[3, 2, 1] > [1, 2, 3, 4]

items = []
if len(items) < 3:
    print("Buy more!")
elif len(items) <= 5:
    print("Thanks!")
else:
    print("Discount!")
