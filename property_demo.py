""" Goal: become a black-belt with properties.

Basics:
    What does property do?      Converts attribute acess like a.x
                                into a method call like a.get_x()

    How does property work?     It reprograms the dot operator to change
                                the usual attribute lookup process.

    What can go wrong?          If you don't inherit from object,
                                you don't get the reprogrammable dot.

"""

from __future__ import division

class PriceRange(object):

    def __init__(self, symbol, low, high):
        self.symbol = symbol
        self.low = float(low)
        self.high = float(high)

    def get_midpoint(self):
        return (self.low + self.high) / 2.0

    midpoint = property(get_midpoint)

    def get_low(self):
        return self._low

    def set_low(self, value):
        self._low = float(value)

    low = property(get_low, set_low)

    def get_high(self):
        return self._high

    def set_high(self, value):
        self._high = float(value)

    high = property(get_high, set_high)

    

if __name__ == '__main__':
    p = PriceRange('CSCO', 42, 43)
    
