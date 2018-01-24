""" Learn that functions are just objects like everything else.

Functions are objects like anything else.
    They have methods:
        __call__            Which is basically the code shown below.
    They have attributes:
        __class__           This points to the <function class>
                            where __call__ is defined.
        __name__            String with name given at birth.
        __doc__             String with docstring given at birth or None.
        __code__            Has co_code attribute which is a string
                            with all the operations in binary.

"""

class Function(object):

    def __init__(self, opcodes, name, doc=None):
        self.opcodes = opcodes
        self.__name__ = name
        self.__doc__ = doc

    def __call__(self, *args):
        opcodes = self.opcodes
        i = 0
        stack = []
        while True:
            operation = opcodes[i]
            if operation == 124:            # LOAD_FAST
                index = opcodes[i+1] + opcodes[i+2] * 256
                value = args[index]
                stack.append(value)
                i += 3
            elif operation == 20:           # BINARY_MULTIPLY
                value = stack.pop() * stack.pop()
                stack.append(value)
                i += 1
            elif operation == 83:           # RETURN_VALUE
                return stack[0]
            # ...

def square(x):
    "Return a value times itself."
    return x * x

pow2 = Function([124, 0, 0, 124, 0, 0, 20, 83], 'pow2', 'num times itself')
#                ^-- map(ord, square.__code__.co_code

if __name__ == '__main__':
    print square(5)
    print pow2(5)
