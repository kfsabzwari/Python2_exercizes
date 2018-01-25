""" Super-duper example!

    Using super() for cooperative multiple inheritance.

    https://rhettinger.wordpress.com/2011/05/26/super-considered-super/

"""

from abc import ABCMeta, abstractmethod

class Contract(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def check(self, value):
        print 'check contract'

class Integer(Contract):

    def check(self, value):
        print 'check value is integer'
        assert isinstance(value, int)
        super(Integer, self).check(value)
        # Contract.check(self, value)

class Positive(Contract):

    def check(self, value):
        print 'check value is positive'
        assert value > 0
        super(Positive, self).check(value)
        # Contract.check(self, value)

class PositiveInteger(Positive, Integer):
    pass

if __name__ == '__main__':
    integers = Integer()
    integers.check(5)

    positives = Positive()
    positives.check(7.89)

    posints = PositiveInteger()
