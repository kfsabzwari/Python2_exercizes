""" Goal: Create a new dictionary-like class based on the file
    system so that the data can be examined externally and shared
    across processes. Also, we want the dictionary to be
    persistant on disk.

"""

import os
from collections import MutableMapping

class FileDict(MutableMapping):

    def __init__(self, dirname):
        self.dirname = dirname
        try:
            os.mkdir(dirname)
        except OSError:
            pass

    def __getitem__(self, key):
        # join directory name with key
        fullname = os.path.join(self.dirname, key)
        try:
            with open(fullname) as f:
                return f.read()
        except IOError:
            raise KeyError(key)

    def __setitem__(self, key, value):
        fullname = os.path.join(self.dirname, key)
        with open(fullname, 'w') as writer:
            writer.write(value)

    def __delitem__(self, key):
        fullname = os.path.join(self.dirname, key)
        try:
            os.remove(fullname)
        except OSError:
            raise KeyError(key)

    def __len__(self):
        return len(os.listdir(self.dirname))

    def __iter__(self):
        return iter(os.listdir(self.dirname))

    def __repr__(self):
        return '%s(dirname=%r)' % (self.__class__.__name__, self.dirname)

if __name__ == '__main__':
    d = FileDict('jenks')
    print repr(d)
    d['grant'] = 'orange'
    d['shannon'] = 'green'
    d['bethany'] = 'pink'
    print d['grant']
    try:
        print d['mark']
    except KeyError:
        print 'no mark key'
    del d['shannon']
    print len(d)
    print sorted(d)

    # Mixin methods inherited from MutableMapping

    d.update({'bethany': 'pink', 'mark': ''})
    print d.pop('mark')
    print 'grant' in d
    print d.get('susan', 'white')

        
