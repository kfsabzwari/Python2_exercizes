""" Monkey patching is making variable assignment into someone else's
    namespace. Einstein would call it, "spooky action at a distance".

    Legitimate use cases:

    * Fix erroneous constants
    * Improve bad error messages
    * Make functions more robust (expand the input domain to cover more cases)
    * Temporarily aid debugging or logging to monitor the execution of code
    * Testing

    Illegitimate use cases:

    * If you ever monkey your own code, you're living in a state of sin
    and deserve all the maintenance problems that ensue.

"""

import algebra
import math

algebra.PI = math.pi                            # Monkey-patch

orig_area_triangle = algebra.area_triangle      # Step 1: save original function

def better_area_triangle(base, height):         # Step 2: write a wrapper function
    "Wrapper to improve the error message."
    try:
        return orig_area_triangle(base, height) # Re-use wrapped function
    except RuntimeError:
        raise ValueError('negative base or height not supported')
	
algebra.area_triangle = better_area_triangle    # Step 3: monkey patch

orig_sqrt = math.sqrt                           # Step 1: Save the original function

def better_sqrt(x):                             # Step 2: Write a wrapper function
    "Wrap math.sqrt() to add support for negative values."
    if x >= 0.0:
        return orig_sqrt(x)
    else:
        return orig_sqrt(-x) * 1j

math.sqrt = better_sqrt                         # Step 3: Monkey patch

if __name__ == '__main__':
    print u'My sources tell me that \N{greek small letter pi} =', algebra.PI
    print 'and that the unit circle has area', algebra.area(1)

    print 'The area of the 1st triangle is', algebra.area_triangle(7, 5)
    try:
        print 'The area of the 2nd triangle is', algebra.area_triangle(-5, 10)
    except ValueError:
        print 'Doh! Sorry for the negative input'

    print u'The solutions to 12x\N{superscript two} + 23x + 10 = 0 are:'
    print algebra.quadratic(a=12, b=23, c=10)
    print u'The solutions to 12x\N{superscript two} + 8x + 10 = 0 are:'
    print algebra.quadratic(12, 8, 10)

