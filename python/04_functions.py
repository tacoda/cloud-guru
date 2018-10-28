# Built-in functions

print("Hello, world!")
print(len("Hello, world!"))
print(abs(-11))
print(bin(143))
print(round(3.14159))
print(sum([1, 2, 3]))
print(max([1, 2, 3]))
print(min([1, 2, 3]))

for x in range(10):
    print(x)

print(sorted('abracadabra'))
print(list(reversed(sorted('abracadabra'))))
print(''.join(reversed(sorted('abracadabra'))))

print('This is a long string'.split(' '))
print("Apples, oranges, and bananas".find('an')) # Returns index where it first appears
print("Hello, {0}, and welcome to {1}".format("Bob", "Python"))
print('Hello, {0}, and welcome to {1}'.format("George", "Python"))

a_list = 'This is a long string'.split(' ')
print(a_list)
a_list.sort() # Sorts in-place
print(a_list)
a_list.reverse() # Also in-place
print(a_list)
a_list.remove('long') # Searches for an item and removes it
print(a_list)
b_list = a_list # Reference, not a copy
c_list = a_list.copy()
c_list.append('Owls')

# Defining our own functions

def noop():
    pass # Does nothing

def greet(name):
    print("Hello, {0}".format(name))

greet("Billy")

def product(numbers):
    p = 1
    for n in numbers:
        p *= n
    return p

print(product([1, 2, 3, 4]))

def combine_and_sort(first, second):
    return sorted(first + second)

print(combine_and_sort([1, 3, 5], [2, 4, 6]))

def igpay(word):
    vowels = 'aeiouAEIOU'
    if word[0] in vowels:
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'

print(igpay('dinosaur'))
print(igpay('allosaurus'))
print(igpay('tyranosaurus'))
print(igpay('Earl'))

def numerus(roman):
    values = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'm': 1000
    }
    total = 0
    prev = 0
    for l in roman:
        cur = values.get(l, 0)
        if prev < cur:
            total -= prev
            cur -= prev
        total += cur
        prev = cur
    return total

print(numerus('mmcvi'))
print(numerus('xiv'))
print(numerus('xvii'))
print(numerus('mmciv'))
print(numerus('mmxlix'))
