""" Teach how mixins work, what inheritance is really about,
    how to use multiple inheritance, and how to use
    ABCs (abstract base classes) to impose discipline
    on mixins.

    Mixins are all about code re-use!

    Mixins are reusable capabilities layered on top of existing
    classes.

    Mixins ROCK because:
    * They maximize code reuse
    * Can improve readability

    Mixins BITE because:
    * You should not instantiate them
    * The second floor/house depends on a particular first floor/foundation
    * Requirement documentation for what is required and provided
    * Lacks an inspector to verify the requirements

    ABCs (abstract base classes) are mixins with enforcement:
    * Add an introspectable list of requirements
    * Verify those requirements have been met
    * Keep all the advantages of mixins
    * ABCMeta will not allow instances unless the requirements are met

"""

from abc import abstractmethod, ABCMeta
from collections import Sequence

class Capper(object):
    """ WARNING: Danger! You must use in a subclass.
        Do not instantiate directly. Be sure to build
        a first floor before installing this second floor.
        MUST have an iterable of string to work. Otherwise,
        your warranty is invalid. Not liable for damages.

    """
    def uppercase(self):
        return ''.join(self).upper()

class Uncapper(object):  # Abstract base class -- Mixin with specification and inspector

    __metaclass__ = ABCMeta     # Inspector who verifies the specification

    @abstractmethod             # Specification for the first floor
    def __getitem__(self, index):
        raise IndexError

    @abstractmethod
    def __len__(self):
        return 0

    def lowercase(self):
        return ''.join(self).lower()

################################################################

class DoubleSeq(Capper, Uncapper, Sequence):

    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        return (len(self.seq) + 1) // 2

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError('index out of range')
        return self.seq[index * 2]

class TripleSeq(Capper, Uncapper):

    def __init__(self, seq):
        self.seq = seq

    def __len__(self):
        return (len(self.seq) + 1) // 3

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError('index out of range')
        return self.seq[index * 3]

if __name__ == '__main__':
    d = DoubleSeq('Hettinger')
    print len(d)
    print d[0], d[1], d[2]
    print d.uppercase()
    print d.lowercase()
    print d.count('t')
    
    print '*' * 60

    t = TripleSeq('Cisco is awesome!')
    print len(t)
    print t[0], t[1], t[2]
    print list(t)
    print t.uppercase()
    print t.lowercase()

    
# This is the last line on day 3
