""" Application of context manager and monkey-patching to redirection.

    It is very easy to code with global variables, write and test
    one line at a time and use "print" to see the results. Further
    it is easy to later move those lines into a function.

"""

import os
import sys
import dis

class RedirectStdout(object):

    def __init__(self, target):
        self.target = target

    def __enter__(self):
        self.orig_stdout = sys.stdout
        sys.stdout = self.target

    def __exit__(self, exc_type, exc_inst, exc_tb):
        sys.stdout = self.orig_stdout

def show_family(lastname, first_names):
    "Display the family members in a nice tabular format."
    print 'The %s Family' % lastname
    print '=' * (11 + len(lastname))
    for name in first_names:
        print '* %s' % name

################################################################

with RedirectStdout(sys.stderr):
    show_family('Simpsons', ['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie'])

orig_stdout = sys.stdout
sys.stdout = sys.stderr
try:
    show_family('Simpsons', ['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie'])
finally:
    sys.stdout = orig_stdout

f = open('show_family.help.txt', 'w')
try:
    orig_stdout = sys.stdout
    sys.stdout = f
    try:
        help(show_family)
    finally:
        sys.stdout = orig_stdout
finally:
    f.close()
f = open('show_family.help.txt')
try:
    s = f.read()
    print s.upper()
finally:
    f.close()
try:
    os.remove('show_family.help.txt')
except OSError:
    pass

f = open('dis.txt', 'w')
try:
    orig_stdout = sys.stdout
    sys.stdout = f
    try:
        dis.dis(show_family)
    finally:
        sys.stdout = orig_stdout
finally:
    f.close()

print 'DONE'

################################################################

orig_stdout = sys.stdout
sys.stdout = sys.stderr
try:
    show_family('Simpsons', ['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie'])
finally:
    sys.stdout = orig_stdout

f = open('show_family.help.txt', 'w')
try:
    orig_stdout = sys.stdout
    sys.stdout = f
    try:
        help(show_family)
    finally:
        sys.stdout = orig_stdout
finally:
    f.close()
f = open('show_family.help.txt')
try:
    s = f.read()
    print s.upper()
finally:
    f.close()
try:
    os.remove('show_family.help.txt')
except OSError:
    pass

f = open('dis.txt', 'w')
try:
    orig_stdout = sys.stdout
    sys.stdout = f
    try:
        dis.dis(show_family)
    finally:
        sys.stdout = orig_stdout
finally:
    f.close()

print 'DONE'
