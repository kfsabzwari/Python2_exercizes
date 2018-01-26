''' Circuitous (tm)                                          # Project name
Apply advanced circle analytic theoretical results
to practical applications for cutting edge distributed
circle management tasks to save the planet.                  # Elevator Pitch
'''

# Project name and elevator pitch
# Waterfall:   Requirements -> Design -> Coding -> Testing -> Documentation
# Agile:       Much different, it is learning process
#              Tight loops of design a little, code a little, and test a little, ship
# New-style classes inherit from object().
# The purpose of inheritance is code re-use.  One class uses the methods and attributes of another.
# Inheritance is optional.  You can always live without by duplicating data and methods.
# The dot (.) operator in Python is controlled by __getattribute__, __setattr__, and __delattr__.
# The reason to inherit from object() is to re-use its customized methods for accessing the dot.
# Aim to write docstrings first, before writing code.
# "self" is not a language requirement.  It is a cultural convention.
# It is commmon to not write docstrings for dunder method because usually users don't see them.
# A second reason dunder docstrings are sometimes omitted, is that their meaning is already well-known.
# Usually when moving data from namespace to another, we usually keep the name the same
# unless moving from one problem domain to another.
# Long method names should typically have unique prefixes to support tab completions
# Don't put the name of the class in a method name:  area_of_circle
# Factor-out magic constants by giving them names
# D.R.Y == Do Not Repeat Yourself
#        \-> There should be a single source of truth
#         \-> Every essential idea should be expressed exactly once in the code.
# Code smell:  Code that works but has issues with readability, debuggability, or maintainability.
# The usual naming convention for constants is all upper case.
# Key design principles:  loosing coupling and high cohesion
# The purpose of modules is 1) code-reuse and 2) code organization
# MVP -- Minimum viable product
# YAGNI,RN -- You ain't gonna need it, right now
# "Code is your enemy"
# Dogfooding:  Be your own first customer
# "self" does not mean "you".  It means "you" or one of your "children".
# Micro-management:  Telling someone HOW to do their job rather than WHAT do do.

import math
from collections import namedtuple

Version = namedtuple('Version', ['major', 'minor', 'micro'])

class Circle(object):
    ''' Create a circle instance from a radius

        As part of an advanced circle analytics toolkit
    '''

    __slots__ = ['diameter']            # Flyweight design pattern which saved memory by eliminating instance dicts in favor of fixed width slots

    version = Version(0, 12, 1)         # Class variables have information SHARED by all instances

    def __init__(self, radius):
        self.radius = radius            # Instance variables have information UNIQUE to each instance

    def area(self):                                     # Regular methods have "self"
        'Perform quadrature on a planar shape of uniform revolution'
        p = self.__perimeter()                          # Class local reference used when you need "self" to really be "you"
        radius = p / 2.0 / math.pi
        return math.pi * radius ** 2.0

    def perimeter(self):
        'Compute the closed line integral for the 2-D locus of points equidistant from a given point'
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter                             # Name mangling prefixes the name of the class

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.radius)

    @staticmethod                                       # Reprograms the dot to NOT add "self".
    def angle_to_grade(angle):                          # Use case is to add a regular function to a class to human factors findability problem
        'Convert an inclinometer reading in degrees to a percent grade'
        return math.tan(math.radians(angle)) * 100.0

    @classmethod                                        # Reprograms the dot to add "cls" as the first argument
    def from_bbd(cls, bbd):                             # Use case is to add alternative constructors
        'Create a new circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    @property                                           # Reprograms the dot to convert attribute like c.radius into method access
    def radius(self):
        return self.diameter / 2.0

    @radius.setter                                      # Attaches the setter function
    def radius(self, radius):
        if radius <= 0.0:
            raise ValueError('Expected a non-negative radius')
        self.diameter = radius * 2.0







