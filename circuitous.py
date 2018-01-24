"""Circuitous (TM)                                      # Project Name

Apply advanced circle analytic theoretical results      # Elevator Pitch
to practical applications for cutting edge distributed
circle management tasks to make the world a better place.

"""

import math
from collections import namedtuple

Version = namedtuple('Version', ['major', 'minor', 'micro'])

class Circle(object):
    """Create a circle instance from a radius.

    As part of an advanced circle analytics toolkit.

    """
    version = Version(0, 1, 0)
    __slots__ = ['diameter']
    
    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        "Perform quadrature of a planar shape of uniform revolution."
        p = self.__perimeter()
        radius = p / 2.0 / math.pi
        return math.pi * radius**2.0

    def perimeter(self):
        """ Compute the closed line integral for locus of 2-D points
            equidistant from a single point.

        """
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.radius)

    def angle_to_grade(angle):
        "Convert an inclinometer reading in degrees to percent grade."
        return math.tan(math.radians(angle)) * 100.0

    angle_to_grade = staticmethod(angle_to_grade)

    def from_bbd(cls, bbd):
        "Create a new circle from bounding box diagonal."
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    from_bbd = classmethod(from_bbd)

    # Cry! Cry! Cry!
    # Fairy God Mother

    def get_radius(self):
        return self.diameter / 2.0

    def set_radius(self, radius):
        self.diameter = radius * 2.0

    """ I wish, I wish that EVERYWHERE someone wrote c.radius that MAGICALLY
        c.get_radius() would be called without me changing ANY code
        (including my own), AND I wish that EVERYWHERE someone set
        c.radius = value that MAGICALLY c.set_radius(value) would be
        called without me changging ANY code (including my own)

    """
    radius = property(get_radius, set_radius)
    



