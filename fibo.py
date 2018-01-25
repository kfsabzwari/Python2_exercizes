""" Write the famous Fibonacci function.

        F(0) -> 1
        F(1) -> 1
        F(n) -> F(n-1) + F(n-2), n > 1

"""

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    print fib(10)
