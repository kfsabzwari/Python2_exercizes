"""How Python Works -- Magic Methods

Function        Dunder Method           Raymond Adjective   Actual Adjective
--------------  -------------           -----------------   ----------------
len(s)          s.__len__()             lenable             sizeable
hash(s)         s.__hash__()            hashable            hashable
abs(x)          x.__abs__()
hex(x)          x.__hex__()

Operator        Dunder Method           Raymond Adjective   Actual Adjective
--------------  -------------           -----------------   ----------------
s + t           s.__add__(t)            plusable            addable
s * t           s.__mul__(t)            starable            multiplicable
s ** t          s.__pow__(t)
s % t           s.__mod__(t)
s == t          s.__eq__(t)
s < t           s.__lt__(t)
s > t           s.__gt__(t)
s <= t          s.__le__(t)
s != t          s.__ne__(t)
s == t          s.__cmp__(t)                                comparable
s in t          s.__contains__(t)       inable              container
s[i]            s.__getitem__(i)        bracketable         indexable
s(t, u)         s.__call__(t, u)        parenable           callable
s.t             s.__getattribute__('t') dotable             ???

Statement       Dunder Method           Raymond Adjective   Actual Adjective
--------------  -------------           -----------------   ----------------
for x in s:     s.__iter__()            forable             iterable
                s.__getitem__(i)
with s as t:    t = s.__enter__()       withable            context manager
                s.__exit__(*exception)
while s:        s.__bool__()            whilable
print s         sys.stdout.write(s.__str__())  printable    printable

"""
