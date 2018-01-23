"Show-off the Circuitous code from the user's point of view."

from circuitous import Circle

print u'Tutorial from Circuitous\N{trade mark sign}'
print 'Circle class version: %d.%d' % Circle.version[:2]
c = Circle(10)
print 'A circle with a radius of', c.radius
print 'has an area of', c.area()
print


## Academia ######################################################

from random import random, seed  # should go at the top
n = 100
jenny = 8675309
seed(jenny)

print 'DARPA Grant Proposal to study the average area if random circles'
print 'using Circuitous (TM) version %d.%d' % Circle.version[:2]
print 'preliminary study of {n} random circles'.format(n=n)
print "seeded with Jenny's number: {jenny}".format(jenny=jenny)

#circles = []
#for i in range(n):
#    circle = Circle(random())
#    circles.append(circle)
#
#area = []
#for circle in circles:
#    area.append(circle.area())

circles = [Circle(random()) for i in range(n)]
areas = [circle.area() for circle in circles]

average_area = sum(areas)/n
print 'The average area is %.1f' % average_area
print
