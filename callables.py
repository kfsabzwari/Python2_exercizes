""" Learn all about things that can be called in Python.

"""

# One way to make a function is to use "def"
# 1) makes a function
# 2) attaches metadata: __name__ and __doc__
# 3) does an assignment

def square(x):
    'Return a value times itself.'
    return x * x

print map(square, range(10))

# Another way is to use "lambda"

pow2 = lambda x: x**2
pow2.__name__ = 'pow2'
pow2.__doc__ = 'Return value to second power'

print map(pow2, range(10))

# One use case is "anonymous functions"
print map(lambda x: x**2, range(10))
# Other use cases: promises, deferreds, thunks, freeze/thaw.
# These are common in callback style programming.

# Callables can be user-defined.
# Any class that defines __call__ can make a callable.

class ToUpper(object):
    def __init__(self, word):
        self.word = word
    def __call__(self):
        return self.word.upper()

gmj, sej, bmj, mrj = map(ToUpper, ['grant', 'shannon', 'bethany', 'mark'])

print gmj()
print sej()
print bmj()
print mrj()

# Types are callable -- used to make an instance.
# Types have unbound methods which are callable.
# Instances have bound methods which are callable.

class Dog(object):
    def __init__(self, name):
        self.name = name
    def talk(self):
        return 'Woof! %s is barking' % self.name
    def fetch(self, thing):
        return '%s is fetching the %s' % (self.name, thing)
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)

from pprint import pprint
pprint(map(Dog, ['Roscoe', 'Loki', 'Tesla']))

d = Dog('Rex')
pprint(map(d.fetch, ['bone', 'stick', 'frisbee']))
#            ^-- Bound methods are callable.
pprint(map(Dog.talk, map(Dog, ['Roscoe', 'Loki', 'Tesla'])))
#              ^-- Unbound methods are callable.

print map(str.upper, ['red', 'green', 'blue'])
#             ^-- Unbound method.
print map('abracadabra'.find, 'abcdef')
#                       ^-- Bound method.

# Operator module replaces syntax with functions.

def negate(x):
    return -x

print map(negate, range(5, 10))
print map(lambda x: -x, range(5, 10))

from operator import neg

print map(neg, range(5, 10))
#         ^-- arithmetic negation operator

from collections import namedtuple
Color = namedtuple('Color', ['red', 'green', 'blue'])

colors = [Color(255, 255, 0), Color(255, 0, 0), Color(255, 0, 255)]
pprint(colors)

def get_last(seq):
    return seq[-1]

print map(get_last, colors)
print map(lambda seq: seq[-1], colors)

class ItemGetter(object):
    def __init__(self, index):
        self.index = index
    def __call__(self, seq):
        return seq[self.index]

print map(ItemGetter(-1), colors)

from operator import itemgetter
print map(itemgetter(-1), colors)
#            ^-- square brackets operator

def get_green(obj):
    return obj.green

print map(get_green, colors)
print map(lambda obj: obj.green, colors)

class AttrGetter(object):
    def __init__(self, name):
        self.name = name
    def __call__(self, obj):
        return getattr(obj, self.name)

print map(AttrGetter('green'), colors)

from operator import attrgetter
print map(attrgetter('green'), colors)
#           ^-- dot operator



