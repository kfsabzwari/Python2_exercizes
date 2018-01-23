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
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        "Perform quadrature of a planar shape of uniform revolution."
        return math.pi * self.radius**2.0
