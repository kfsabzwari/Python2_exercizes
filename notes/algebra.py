''' Fancy, expensive math package for wealthy people
    who have forgotten all math since the 7th grade

    Copyright (c) 2017 Fly-by-night Software
    All Rights Reserved
'''

from __future__ import division
import math

pi = 3.14157

def area(radius):
    '''Compute the area of a circle

        >>> area(10)
        314.15700000000004

    '''
    return pi * radius ** 2.0

def average(seq):
    '''Compute the arithmetic mean

        >>> average([10, 20, 61])
        30.333333333333332

    '''
    # https://en.wikipedia.org/wiki/Arithmetic_mean
    return sum(seq) / len(seq)

def area_triangle(base, height):
    ''' Compute the area of triangle given the base and height

        >>> area_triangle(30, 40)
        600.0

    '''
    if base < 0.0 or height < 0.0:
        raise RuntimeError('Imaginary numbers not supported in Kronecker product spaces')
    return base * height / 2.0

def quadratic(a, b, c):
    ''' Find the two roots the quadratic equation:

            ax^2 + bx + c = 0

        Written Python as:

            a*x**2 + b*x + c == 0.0

        For example:

            >>> x1, x2 = quadratic(a=8, b=-14, c=-15)
            >>> x1
            2.5
            >>> x2
            -0.75
            >>> 8*x1**2 -14*x1 - 15
            0.0
            >>> 8*x2**2 -14*x2 - 15
            0.0

    '''
    # https://en.wikipedia.org/wiki/Quadratic_equation
    discriminant = b**2.0 - 4.0*a*c
    r = math.sqrt(discriminant)
    x1 = (-b + r) / (2.0 * a)
    x2 = (-b - r) / (2.0 * a)
    return x1, x2

if __name__ == '__main__':
    import doctest

    print doctest.testmod()
