""" Review a handful of looping idioms.

"""

names = 'grant shannon bethany mark'.split()
colors = 'orange green pink'.split()
cities = 'austin dallas chicago dallas austin chicago'.split()

print 'Task: show the colors in uppercase'

for i in range(len(colors)):
    print colors[i].upper()

for color in colors:
    print color.upper()

print '\nTask: show the names with index of each name'

for i in range(len(names)):
    print '%d -> %s' % (i + 1, names[i])

for i, name in enumerate(names, 1):
    print '%d -> %s' % (i, name)

print '\nTask: show the colors in reverse order'

for i in range(len(colors)-1, -1, -1):
    print colors[i]

for color in reversed(colors):
    print color

print '\nTask: associate the names with colors'

n = min(len(names), len(colors))
for i in range(n):
    print '%s -> %s' % (names[i], colors[i])

for name, color in zip(names, colors):
    print '%s -> %s' % (name, color)

print '\nTask: show the colors in title case in alphabetical order'

for color in sorted(colors):
    print color.title()

print '\nTask: show the colors in upper case ordered by their length'

for color in sorted(colors, key=len):
    print color.upper()

print '\nTask: show each city once in alphabetical order'

for city in sorted(set(cities)):
    print city














