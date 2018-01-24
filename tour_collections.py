from collections import *
from pprint import pprint
import re

names = """tom david raymond rachel susan timothy beatrice trudy don
brandon martin darlene hailey bonnie randal suzy bryce mary rodney davin
sharon andy bill dave henry theordore sue mark daisy hank adam tim ann
""".split()
people = 'grant shannon bethany mark'.split()
foods = 'sushi lobster soup tacos'.split()
colors = 'red green blue green red purple blue red green red'.split()

## Counting ####################################################

print '\nCount 2 most common colors:'

c = Counter(colors)
print c.most_common(2)

print '\nCount 10 most common words in Hamlet:'

def words(filename):
    with open(filename) as reader:
        for line in reader:
            for match in re.finditer(r'[a-zA-Z\-\']+', line):
                word = match.group(0)
                yield word.lower()

pprint(Counter(words('notes/hamlet.txt')).most_common(10))

## Maintaining order in your kingdom ###########################

print '\nMap people to foods in people-order'

food_pref = OrderedDict()
for person, food in zip(people, foods):
    food_pref[person] = food
print food_pref

## Grouping a dictionary by feature ############################
##
## defaultdict(factory_function_of_arity_zero)
## ^-- never raises KeyError; instead, calls the factory function

print '\nGroup the names by the first letter in name'
d = defaultdict(list)
for name in names:
    feature = name[0]
    d[feature].append(name)
pprint(dict(d), width=250)

print '\nGroup the names by the last letter in name'
d = defaultdict(list)
for name in names:
    feature = name[-1]
    d[feature].append(name)
pprint(dict(d), width=250)

print '\nGroup the names by the length of the name'
d = defaultdict(list)
for name in names:
    feature = len(name)
    d[feature].append(name)
pprint(dict(d), width=250)

print '\nGroup the names by the number of vowels in the name: aeiouy'
d = defaultdict(list)
for name in names:
    # feature = name.count('a') + name.count('e') + name.count('i')
    # feature += name.count('o') + name.count('u') + name.count('y')
    # feature = sum([name.count(vowel) for vowel in 'aeiouy'])
    # feature = sum(name.count(vowel) for vowel in 'aeiuoy')
    feature = sum(1 for match in re.finditer(r'[aeiouy]', name))
    d[feature].append(name)
pprint(dict(d), width=250)

## FIFO Queue -- First in, first out ###########################
## Pronounced "deck" and is short for "double-ended" queue
## Spelled "deque"

print '\nFast append and pop at both ends of the sequence:'

q = deque()
q.append('alice')
q.append('bob')
q.append('carol')
print q.popleft()
print q.popleft()
q.appendleft('dave')
q.appendleft('eve')
pprint(q)
while q:
    print q.pop()

print '\nLast five Python shell prompt lines in day1.txt'

with open('day1.txt') as f:
    lines = (line for line in f if line.startswith('>>> '))
    last5 = deque(lines, maxlen=5)

print '\n'.join(last5)













