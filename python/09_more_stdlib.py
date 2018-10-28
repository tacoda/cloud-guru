# import csv
#
# with open('users.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id', 'email', 'name'])
#     writer.writerow([5, 'a@email.com', 'Alice'])
#     writer.writerow([6, 'b@email.com', 'Bob'])
#     writer.writerow([7, 'c@email.com', 'Charles, AKA "Charlie"'])

import os

print(os.getenv('USER'))
print(os.path.abspath('.'))

import sys

print(sys.argv)
print(sys.platform)
print(sys.version)

# Regular expressions

import re

if re.search('tang', 'tangerines'):
    print('tang is in tangerines')

# Includes groups
angs = re.search('(.ang)', 'dangerines')
print(angs.groups())

vowels = '[aeiou]'
print(re.findall(vowels, 'dangerines'))

# Also, turtle (simple graphics)
