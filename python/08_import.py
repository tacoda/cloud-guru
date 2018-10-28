# stdlib & PyPI

import math

print(math.pi)
print(math.e)

print(math.cos(math.pi))
print(math.log(math.e))

print(math.floor(-15.1))
print(math.ceil(-15.1))

import random

print(random.random())
print(random.randint(3, 18)) # Inclusive
print(random.choice(['Happy', 'Dopey', 'Doc', 'Grumpy']))
print(random.choice('aeiou'))

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards = []

for s in suits:
    for v in values:
        cards.append("{0} of {1}".format(v, s))

print(cards)
print(random.choice(cards))

# Modifies in-place
random.shuffle(cards)
print(cards)

# Can get only one part of a module
# from random import shuffle
# my_list = [1, 2, 3, 4, 5, 6]
# shuffle(my_list)
# print(my_list)

# Can alias modules
import itertools as iter

for num in iter.chain([1, 2, 3], [4, 5, 6]):
    print(num)

for (a, b, c) in iter.combinations(('Peanut Butter', 'Jelly', 'Mayo', 'Ketchup', 'Lettuce'), 3):
    print("{0}, {1} and {2} sandwich".format(a, b, c))

import time

print(time.localtime())
print(time.gmtime())

now = time.strftime("%H:%M:%S %p - %A, %B %d %Y", time.localtime())
print(now)

# time.sleep(5)

# Unix time
print(time.time())

# Higher-level time module
import datetime

print(datetime.datetime.strptime(now, "%H:%M:%S %p - %A, %B %d %Y"))

# Beware name collisions with imporing modules
# Use as to alias them
# import time
# from datetime import time as dt_time

now = datetime.datetime.now()
later = datetime.datetime.now()
print(later - now)
print(later > now)

# import gzip
# import bz2
# import zipfile

from zipfile import ZipFile

with ZipFile('files.zip') as files:
    print(files.namelist())
    files.extractall()
