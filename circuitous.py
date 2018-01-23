"""Circuitous (TM)                                      # Project Name

Apply advanced circle analytic theoretical results      # Elevator Pitch
to practical applications for cutting edge distributed
circle management tasks to make the world a better place.

"""

import math
from collections import namedtuple

Version = namedtuple('Version',['major', 'minor', 'mirco'])

class Circle(object):
    ''' Create a circle instance from a radius
    As part of an xxx
    '''
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        "Program quadrant  xxx"
        return math.pi * self.radius**2.0
