colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']
sentence = 'The quick brown fox jumped over the lazy dog.'

# Indexing
print(sentence[0])
print(sentence[4])
print(colors[1])
print(sentence[-1])
print(sentence[-6])

# Slicing
print(colors[1:4])
print(sentence[4:9])
print(sentence[4:])
print(sentence[:9])
print(sentence[::2])
print(colors[::2])
print(sentence[4:-1:2])

# Can reassign values in a list
colors[1] = 'Black'
colors[2:] = ['Black'] * 4

# Cannot reassign values in a string
# sentence[16:19] = 'cat' # Error: Python strings are immutable
new_sentence = sentence[0:16] + 'cat' + sentence[19:]
print(new_sentence)

# Splitting
print(sentence.split(' '))
print('32:56:99'.split(':'))
print(sentence.split('he'))

# Joining
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple']
print(' - '.join(colors))
print(' - '.join(colors).split(' - '))

# Iteration

# For loop
for color in colors:
    print('Is ' + color + ' your favorite?')

for number in [1, 2, 3, 4, 5]:
    double = number * 2
    print('Twice ' + str(number) + ' is ' + str(double))

modifiers = ['Dark', 'Light']
for c in colors:
    for m in modifiers:
        print(m + ' ' + c)

for v in 'aeiou':
    print('My favorite vowel is ' + v)

# While loop
countdown = 10
while countdown >= 0:
    print(str(countdown))
    countdown -= 1

# Note that the while loop consumes the list
names = ['Daniel', 'James', 'Peter', 'Sean']
while names:
    print('Welcome, Mr. ' + names.pop())

# Python's push is called append
names.append('Larry')
names.append('Moe')
names.append('Curly')
print(names)

card_vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

for s in card_suits:
    for v in card_vals:
        print (v + ' of ' + s)

number = 1
while number < 1000000000000:
    print(number)
    number *= 2
