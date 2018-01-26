''' Goal:  Become a black belt with properties

Basics:
    What does it do?        Coverts attribute access like a.x into method access like a.m()
    How does it work?       It reprograms the dot operator to change the usual attribute lookup process
    What can go wrong?      If you don't inherit from object(), you don't get a reprogrammable dot

Computed fields using properties:
    * Saves storage space
    * Reduces risk of data inconsistency
    * Provide a clean, consistent API for users

Data corruption bugs:
    * Very hard to find
    * The error manifests itself far removed from the actual problem

Managed attribute:
    * Controls all read and write access to a variable
    * This lets you type check or range check BEFORE the value is stored
    * This is a fantastic debugging technique
    * The error is trigger when you store the data
      rather then when you use it.

It is common to have a module of data validation utilities:
    * validate_percentage
    * validate_one_of('stock', 'bond', 'option', 'currency')
    * validate_str(minsize=3, maxsize=5, predicate=str.upper)

The @ notation is just a beautification of something we could already do:

    @deco
    def f(x):
        pass

This is just short for:

    def f(x):
        pass

    f = deco(f)

'''

from __future__ import division
from validators import validate_percentage

class PriceRange(object):

    def __init__(self, symbol, low, high):
        self.symbol = symbol
        self.low = low
        self.high = high

    @property                                      # midpoint = property(midpoint)
    def midpoint(self):
        return (self.low + self.high) / 2.0

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, low):
        validate_percentage(low)
        self._low = low

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, high):
        validate_percentage(high)
        self._high = high

p = PriceRange('CSCO', 30, 35)    
    











