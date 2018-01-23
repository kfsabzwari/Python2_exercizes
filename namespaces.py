"""Namespaces in Pythn

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
