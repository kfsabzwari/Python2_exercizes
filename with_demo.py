""" Goal: Become a black belt with the with-statement.

What does it do?

    On the day that you are born,
        make all of your funeral arrangements.

"""

# How to open and close files -- TheOldWay(TM)

f = open('notes/hamlet.txt')
try:
    play = f.read()
    print len(play)
finally:
    f.close()

# How to open and close files -- TheNewWay(TM)

with open('notes/hamlet.txt') as f:
    play = f.read()
    print len(play)

## Protecting critical regions #################################

import threading

printer_lock = threading.Lock()

# How to use locks -- TheOldWay(TM)

printer_lock.acquire()
try:
    print 'inside your critical region'
finally:
    printer_lock.release()

# How to use locks -- TheNewWay(TM)

with printer_lock:
    print 'inside your critical region'

## How to make a context manager ###############################

class CM(object):
    "A generic demonstration-only context manager."

    def __init__(self, x):
        self.x = x
        print 'Initializing with x=', x

    def __enter__(self):
        print 'Entering with x=', self.x
        return 42

    def __exit__(self, exc_type, exc_inst, exc_tb):
        print 'Exiting with x=', self.x
        print 'Exception type:', exc_type
        if exc_type is not None and isinstance(exc_inst, KeyError):
            print 'Caught a KeyError'
            print 'The arguments are', exc_inst.args
            print 'Return True to indicate the exception was handled'
            return True
        print 'Returning None which is a falsey value'

print '\nCase 1: Normal case with no exceptions'
print 'start'
with CM(10) as y:
    print 'In the beginning'
    print 'In the middle with y=', y
    print 'At the end'
print 'finish'

print '\nCase 2: Case with a handled exception'
print 'start'
with CM(10) as y:
    print 'In the beginning'
    print 'In the middle with y=', y
    raise KeyError('henry')
    print 'Never gets here'
print 'finish'

print '\nCase 3: Case with an unhandled exception'
print 'start'
try:
    with CM(10) as y:
        print 'In the beginning'
        print 'In the middle with y=', y
        raise IndexError(5)
        print 'Never gets here'
    print 'Never gets here either'
except IndexError:
    print 'Caught the IndexError outside the with-statement'
print 'finish\n'

################################################################

import os

class File(object):

    def __init__(self, filename):
        self.filename = filename
        self._fileno = os.open(filename, os.O_RDONLY)
        self.closed = False

    def close(self):
        os.close(self._fileno)
        self.closed = True

    def __repr__(self):
        status = 'closed' if self.closed else 'open'
        return '<%s file %r>' % (status, self.filename)

    def read(self):
        blocks = []
        while True:
            data = os.read(self._fileno, 4096)
            if data == '':
                break
            blocks.append(data)
        return ''.join(blocks)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_inst, exc_tb):
        self.close()

def myopen(filename):
    return File(filename)

# How to open and close files -- TheOldWay(TM)

f = myopen('notes/hamlet.txt')
try:
    play = f.read()
    print len(play)
finally:
    f.close()

# How to open and close files -- TheNewWay(TM)

with myopen('notes/hamlet.txt') as f:
    play = f.read()
    print len(play)

## How locks were implemented (roughly) ########################

import thread  # Low-level C-API just for demonstration.

class Lock(object):

    def __init__(self):
        self.lock = thread.allocate_lock()
        self.locked = False

    def acquire(self):
        self.lock.acquire()
        self.locked = True

    def release(self):
        self.lock.release()
        self.locked = False

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, exc_type, exc_inst, exc_tb):
        self.release()

printer_lock = Lock()

# How to use locks -- TheOldWay(TM)

printer_lock.acquire()
try:
    print 'inside your critical region'
finally:
    printer_lock.release()

# How to use locks -- TheNewWay(TM)

with printer_lock:
    print 'inside your critical region'



















