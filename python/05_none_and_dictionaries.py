# None

None

# None evaluates to False

my_data = ''
if my_data is None:
    print("Not set!")

my_data = 0
if my_data is None:
    print("Not set!")

my_data = None
if my_data is None:
    print("Not set!")

my_data = 0
if my_data is not None:
    print("Anything!")

# Dictionaries

cats = {}
cats['Robin'] = 5
print(cats)

cats['Adrian'] = 2
cats['Camilla'] = 1
print(cats)

print(cats['Camilla'])
# cats['George'] # Key error

# .get will not raise an error
# Undefined indices have a value of None
print(cats.get('Bilbo'))
# Can give a default value
print(cats.get('Bilbo', 0))

# Checking keys
if 'Robin' in cats:
    print("Robin has cats")

if 'Frank' in cats:
    print("Frank has cats")

# Keys only, not values

# Iterating with a dictionary
for name in cats:
    print(name)

# Values need to be referenced via key
for name in cats:
    print("{0} has {1} cats".format(name, cats[name]))

for name in cats.keys():
    print(name)

for num_cats in cats.values():
    print(num_cats)

for (person, num_cats) in cats.items():
    print("{0} has {1} cats".format(person, num_cats))

del cats['Adrian']
print(cats)
print(cats.pop('Robin'))
print(cats)
# Pop also gives a key error, but you can also supply a default as the second parameter

countries = {
    'AF': 'Afghanistan',
    'AL': 'Albania',
    'DZ': 'Algeria'
}

for (code, country) in countries.items():
    print('<option value="{0}">{1}</option'.format(code, country))

thumbnail = None
condition = 'Cloudy'
weather = {
    'Rainy': 'rain.png',
    'Cloudy': 'clouds.png'
}
print(weather[condition])

condition = 'Stormy'
thumbnail = weather.get(condition)
print(thumbnail)

users = {
    1: {
        'name': 'Joe',
        'email': 'joe@email.com'
    },
    2: {
        'name': 'Sarah',
        'email': 'sarah@email.com'
    }
}
