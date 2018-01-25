""" Learn to walk like a duck, talk like a duck, and swim like a duck.

Duck Typing:
    If it looks like a duck,
    walks like a duck,
    and quacks like a duck,
    then you can treat it as a duck.

"""

def get_file_size1(f):
    """ Get file size.

    Worst way: exact type checking
    Problem: precludes subclasses

    """
    if type(f) != file:
        raise TypeError('expected a file')
    s = f.read()
    f.close()
    return len(s)

def get_file_size2(f):
    """ Get file size.

    Less egregious: isinstance
    Good: allows subclasses
    Problem: precludes file-like objects

    """
    if not isinstance(f, file):
        raise TypeError('expected a file')
    s = f.read()
    f.close()
    return len(s)

def get_file_size3(f):
    """ Get file size.

    Best: duck typing
    Solution: check based on what you have not who you are

    """
    s = f.read()
    f.close()
    return len(s)

class FakeFile(object):

    def __init__(self):
        print 'fake file initialized'

    def read(self):
        print 'fake file read'
        return 'this is fake data'

    def close(self):
        print 'fake file closed'

if __name__ == '__main__':
    f = open('notes/hamlet.txt')
    print get_file_size3(f)

    fake_file = FakeFile()
    print get_file_size3(fake_file)

    from StringIO import StringIO
    s = StringIO('this is a test')
    print get_file_size3(s)



