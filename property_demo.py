""" Goal: become a black-belt with properties.

Basics:
    What does property do?      Converts attribute acess like a.x
                                into a method call like a.get_x()

    How does property work?     It reprograms the dot operator to change
                                the usual attribute lookup process.

    What can go wrong?          If you don't inherit from object,
                                you don't get the reprogrammable dot.

Computed fields using properties:
    * Saves storage space
    * Reduces the risk of data inconsistency
    * Provides a clean, consistent API for users

Data corruption bugs:
    * Very hard to find
    * The error manifests itself far from the actual problem

Managed attribute:
    * Controls all read and write access to a variable
    * This lets you type check or range check BEFORE the value is stored
    * This is fantastic debugging technique
    * The error is triggered when you store the data
        rather than when you use it

The @ notation is just a beautification of something we could do manually:

    @deco
    def f(x):
        pass

What we're really saying is:

    def f(x):
        pass
    f = deco(f)

"""

from __future__ import division

class PriceRange(object):

    def __init__(self, symbol, low, high):
        self.symbol = symbol
        self.low = low
        self.high = float(high)

    @property  # midpoint = property(midpoint)
#   ^-- "decorator" syntax
    def midpoint(self):
        return (self.low + self.high) / 2.0

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, value):
        self._low = float(value)

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, value):
        self._high = float(value)

    # high = property(get_high, set_high)
    # ^-- replaced by @property and @high.setter syntax


if __name__ == '__main__':
    p = PriceRange('CSCO', 42, 43)
    print p.low, p.high, p.midpoint
    p.high = '50.12'
    print p.low, p.high, p.midpoint
