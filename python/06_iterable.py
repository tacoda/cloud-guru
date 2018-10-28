# Binary data
b = bytes()
print(b)

greeting = b"Hello, world!"
print(greeting)
for c in greeting:
    print(c)

# Can't modify bytes, but can modify byte arrays
ba = bytearray()
print(ba)

data = bytearray()
data += b"Hi, how are you?"
print(data)
data[0] = 120
print(data)

# Tuples
fruits = ("Apple", "Orange", "Lemon", "Tomato")
print(fruits[0])
for f in fruits:
    print("Would you like a nice {0}?".format(f))

# Can't modify a tuple
# Can easily swap to a list and back again
list(fruits)
tuple(list(fruits))

# A tuple is immutable, but the data inside can be mutable, like lists

# Sets
veggies = {"Asparagus", "Onion", "Carrot"}
# Can't index, but can iterate
veggies.pop()
veggies.add("Radish")

# Easily swap between types
list(set(tuple(veggies)))

# Intersection, union, and other set operations

# Frozen sets
# A set you can't modify
frozen = frozenset(veggies)
# frozen.pop() # Error

# Iterables are consumed the same way (like a for loop)
colors = {
    'Red': (255, 0, 0),
    'Yellow': (255, 255, 0),
    'Purple': (255, 0, 255)
}
for (name, rgb) in colors.items():
    print(name, rgb)

# Can track an index by calling enumerate (on lots of things)
for (i, c) in enumerate(fruits):
    print(i, c)

# Zip stops when either iterable runs out
for (f, v) in zip(fruits, veggies):
    print(f, v)

haystack = ['hey'] * 20
haystack[6] = 'needle'

# Continue and break as expected
idx = None
for (i, v) in enumerate(haystack):
    print('Looking...')
    if v == 'needle':
        idx = i
        print('FOUND IT!!')
        break

for (i, v) in enumerate(haystack):
    print('Looking...')
    if v == 'hey':
        continue
    idx = i
    print('FOUND IT!!')
    break

# Else happens if it goes through entire iterable without 'break'ing
haystack = ['hey'] * 20
for (i, v) in enumerate(haystack):
    print('Looking...')
    if v == 'hey':
        continue
    idx = i
    print('FOUND IT!!')
    break
else:
    print("Couln't find it...:(")

# List comprehensions
powers = []
for i in range(1, 21):
    powers.append(2 ** i)
print(powers)

powers = [ 2 ** i for i in range(1, 21) ]
print(powers)
