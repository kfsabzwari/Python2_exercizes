"""Namespaces in Python

Only three ways to create a new namespace in Python:

    1. modules (filename.py)
    2. classes (class statement)
    3. functions (def statement)

Looking up variable names:

    1. locals()
    2. Enclosing function scope(s)
    3. globals()
    4. Builtins -- __builtins__
    5. raise NameError

Looking up object attributes:

    1. Instance dictionary
        vars(inst)
    2. Class dictionary
        vars(type(inst))
    3. Search base classes
        vars(base) for base in type(inst).mro()     (new-style, iterative)
        vars(base) for base in type(inst).__bases__ (old-style, recursive)
    4. raise AttributeError

"""

from pprint import pprint

print '###########################################################'
print 'locals() and globals()'

a = 1

def b(c):
    d = 2
    print 'Locals in b:', locals()

print 'Globals:', globals()
b(3)

print '###########################################################'
print 'def in for'

funcs = []

for count in range(3):
    def display_count():
        print 'Count:', count
    funcs.append(display_count)

for func in funcs:
    func()

print '###########################################################'
print 'vars(obj) and dir(obj)'

class E(object):

    def __init__(self, f):
        self.f = f

    def g(self):
        h = 4
        print 'Locals in E.g:', locals()

print 'Vars of E:', vars(E)
print E.__dict__
e = E(5)
print 'Vars of e:', vars(e)
print e.__dict__
print 'Dir of e:'
pprint(dir(e))
print e.f
e.g()

print '###########################################################'
print '=, def, class, import'

def f(x):
    y = x ** 2
    def g(z):
        pass
    class T:
        pass
    import random
    print 'Locals in f:'
    pprint(locals())

f(5)

print '###########################################################'
print 'assign in class'

class Foo(object):
    bar = 1

    def get_bar(self):
        return Foo.bar  # bar --> NameError

f = Foo()
print 'bar:', f.get_bar()

print '###########################################################'
print 'Inheritance'

class I(E):
    j = 6

    def g(self):
        k = 7
        print 'Locals in I.g:', locals()

i = I(7)
print i.j
print i.f
i.g()
E.g(i)
print type(i)
print i.__class__
print type(i).__bases__
print type(i).mro()

print '###########################################################'
print 'def in def -- Enclosing scope.'

def f(x):           # x in enclosing scope
    y = x ** 2      # y in enclosing scope
    def g(z):       # z in locals
        return x, y, z, w, len  # w in globals, len in __builtins__
    print g(10)

w = 5

f(2)

print '###########################################################'
print 'Closures'

def f(x):
    y = x ** 2
    def g(z):
        return x, y, z, w, len
    return g














