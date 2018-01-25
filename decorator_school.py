""" Decorator School

Kinds of Functions
==================

    Identity function: The output is the same as the input.

    Higher-order functions: Use other functions as input data or
    output data.

    Pure functions: Give the same output for the same input every
    time AND it has no side-effects.

    Decorator functions: A higher-order function with a single
    function in and single function out.

How variables work
==================

    Variable lookup:
        locals() -> enclosing -> globals() -> __builtins__ -> NameError
    Variable assignments always go into locals()
    At the module level, locals and globals are the same dictionary.

    Assigning words:    =   with...as   import  class   def
      existing objects--^---^            ^------^-------^-- new objects

"""

import time

def add_logging(orig_func):
    def logging_func(x):
        'Wrapper around functions that logs inputs and outputs.'
        print '%s() called with %r' % (orig_func.__name__, x)
        answer = orig_func(x)
        print 'the answer is', answer
        return answer
    logging_func.__name__ = orig_func.__name__
    logging_func.__doc__ = orig_func.__doc__
    return logging_func

def add_caching(orig_func):
    "Cache arguments and return values."
    cache = {}
    def caching_func(x):
        "Wrapper around functions that caches arguments and return values."
        if x in cache:
            return cache[x]
        else:
            result = orig_func(x)
            cache[x] = result
            return result
    caching_func.__name__ = orig_func.__name__
    caching_func.__doc__ = orig_func.__doc__
    caching_func.cache = cache
    return caching_func

@add_logging
def square(x):
    "Return a value times itself."
    return x * x

@add_caching
def big_func(x):
    "Simulate a big, slow, expensive function."
    time.sleep(3)
    return -x
