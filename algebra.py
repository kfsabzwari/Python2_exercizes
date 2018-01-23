""" Algebra Package from Algetech

    Fancy, expensive math package for wealthy people
    who have forgotten all math since the 7th grade.

    >>> area(1)
    3.1415

    Copyright (c) 2018 Algetech Software
    All Rights Reserved

"""

from __future__ import division
import math

PI = 3.1415

def area(radius):
    """ Compute the area of a circle.

        >>> area(100)
        31415.0
        >>> area('hello')
        Traceback (most recent call last):
          ...
        TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'

    """
    return PI * radius**2.0

def average(seq):
    """ Compute the arithmetic mean.

        >>> average([10, 20, 60])
        30.0
        >>> average([10, 20, 61])
        30.333333333333332

    """
    # https://en.wikipedia.org/wiki/Arithmetic_mean
    return sum(seq) / len(seq)

def area_triangle(base, height):
    """ Compute area of triangle given base and height.

        >>> area_triangle(30, 40)
        600.0
        >>> area_triangle(-10, 100)
        Traceback (most recent call last):
          ...
        RuntimeError: Imaginary numbers not supported in Kronecker product spaces

    """
    if base < 0.0 or height < 0.0:
        raise RuntimeError('Imaginary numbers not supported in Kronecker product spaces')
    return base * height / 2.0

def quadratic(a, b, c):
    """ Find the two roots of the quadratic equation.

        ax^2 + bx + c = 0

    Written in Python as:

        a*x**2 + b*x + c = 0.0

    For example:

        >>> x1, x2 = quadratic(8, -14, -15)
        >>> x1
        2.5
        >>> x2
        -0.75
        >>> 8*x1**2 - 14*x1 - 15
        0.0
        >>> 8*x2**2 - 14*x2 - 15
        0.0

    """
    discriminant = b ** 2.0 - 4.0 * a * c
    r = math.sqrt(discriminant)
    denominator = 2.0 * a
    x1 = (-b + r) / denominator
    x2 = (-b - r) / denominator
    return x1, x2

if __name__ == '__main__':
    import doctest
    print doctest.testmod()
















