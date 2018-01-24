"""Circuitous (TM)                                      # Project Name

Apply advanced circle analytic theoretical results      # Elevator Pitch
to practical applications for cutting edge distributed
circle management tasks to make the world a better place.

"""

# Waterfall:    Requirements -> Design -> Coding -> Testing -> Deploy
# Agile:        Much different. Learning process.
#               Tight loops of design, code, test, deploy, repeat.

# New-style classes inherit from "object"
# The purpose of inheritance is code re-use.
# One class uses the methods and attribute of another.
# inheritance is optional.
# You can always live without by duplicating data and methods.
# The dot (.) operator in Python is controlled by
#   __getattribute__  __setattr__  __delattr__
# The reason to inherit from object is to reuse its customized methods
# for acessign the dot.

# Aim to write a docstring first, efore writing the code.
# "A problem well defined is half-solved."

# "self" is not a language requirement. It is a cultural convention.

# Common to omit docstring for dunder methods because users usually
# don't see them.
# Second reason docstrings are sometimes omitted, is that their
# meaning is already well-known.

# Usually when moving data from one namespace to another, we usually
# keep the same name.
# Don't put the name of the class in a method name: area_of_circle NO!

# Factor out magic constants by giving them names.
# D.R.Y. -- Do Not Repeat Yourself
# ^-- There should be a single source of truth.
# ^-- Every essential idea should be expressed exactly once in the code.

# The usual naming convention for constants is all upper snake case.
# YAGNI,RN -- You ain't gonna need it, right now.
# "Code is your enemy"

# "self" does not mean "you". It means "you" or one of your "children".

import math
from collections import namedtuple

Version = namedtuple('Version', ['major', 'minor', 'micro'])

class Circle(object):  # New-style class. Inheritance from object.
    """Create a circle instance from a radius.

    As part of an advanced circle analytics toolkit.

    """
    # Flyweight design pattern saves memory by eliminating dicts
    # in favor of fixed-width slots. (This is your memory bazooka.)
    __slots__ = ['diameter']

    # Class variables have information SHARED by all instances.
    version = Version(0, 1, 0)
    
    def __init__(self, radius):
        # Instance variables have information UNIQUE to each instance.
        self.radius = float(radius)

    def area(self):  # Regular methods have "self"
        "Perform quadrature of a planar shape of uniform revolution."
        # Class local reference used when you
        # need "self" to really be "you".
        p = self.__perimeter()
        radius = p / 2.0 / math.pi
        return math.pi * radius**2.0

    def perimeter(self):
        """ Compute the closed line integral for locus of 2-D points
            equidistant from a single point.

        """
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter  # Name mangling prefixes name of class.

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.radius)

    # Reprogram dot to NOT bind "self".
    # Use case: add regular functions to class
    # (solve human factors find-ability problem)
    @staticmethod
    def angle_to_grade(angle):
        "Convert an inclinometer reading in degrees to percent grade."
        return math.tan(math.radians(angle)) * 100.0

    # angle_to_grade = staticmethod(angle_to_grade)
    # ^-- replaced by "@staticmethod" syntax

    # Reprogram dot to add "cls" as first argument, type(self).
    # Use case: add alternative constructors.
    @classmethod
    def from_bbd(cls, bbd):
        "Create a new circle from bounding box diagonal."
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    # from_bbd = classmethod(from_bbd)
    # ^-- replaced by "@classmethod" syntax

    # Reprogram the dot to convert attribute to method call.
    # Use case: c.radius becomes c.get_radius()
    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    # radius = property(get_radius, set_radius)
    # ^-- replaced by "@property" and "@radius.setter" syntax
    



