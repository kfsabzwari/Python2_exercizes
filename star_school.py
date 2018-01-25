""" Learn common argument passing techniques in Python.

"""

def mypow(base, exp):
    "Emulate the builtin pow() function."
    return base ** exp

print mypow(2, 5)           # Positional arguments --> the order matters.
print mypow(exp=5, base=2)  # Keyword arguments --> the name matters.
print mypow(2, exp=5)       # Hybrid arguments --> positional BEFORE keywords.

# Cheap luggage --> Tuples are compact and fast ordered collections.
# TSA demands you unpack BEFORE the function call.
# 1 star unpacks any SEQUENCE into POSITIONAL arguments.

arguments = (2, 5)
print mypow(arguments[0], arguments[1])
print mypow(*arguments)

# Expensive luggage --> Bigger and slower, but uses named access.
# The TSA still demands unpacking.
# 2 stars unpacks MAPPING into KEYWORD arguments.

arguments = {'exp': 5, 'base': 2}
print mypow(exp=arguments['exp'], base=arguments['base'])
print mypow(**arguments)

def f(a, b, c=0, d=0):      # Optional (default) arguments to AFTER requirements.
    return a + b + c + d

def f(a, b, *c, **d):       # Variable length argument lists.
    print a
    print b
    print c                 # 1 star PACKS the POSITIONAL args into a TUPLE
    print d                 # 2 stars PACKS the KEYWORD args into a DICT

f(10, 20, 30, 40, 50, x=1, y=2, z=3)

# Most common way to write a wrapper function.
# 1. Save the original function.
# 2. Build a wrapper to add new functionality.
# 3. Change the name to refer to the new wrapper function.

orig_pow = mypow

def logging_pow(*args, **kwargs):
    "Wrap function to log inputs and outputs."
    print 'function called with:', args, kwargs
    answer = orig_pow(*args, **kwargs)
    print 'the answer is', answer
    return answer

mypow = logging_pow

x = mypow(2, 5)
y = mypow(exp=5, base=2)
z = mypow(2, exp=5)
print x, y, z






    
