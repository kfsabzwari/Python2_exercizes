""" Write the famous Fibonacci function.

        F(0) -> 1
        F(1) -> 1
        F(n) -> F(n-1) + F(n-2), n > 1

"""

from decorator_school import add_caching

# @add_caching
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_fast(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

# import threading
import multiprocessing

# lock = threading.Lock()
lock = multiprocessing.Lock()

def show_fib(n):
    result = fib(n)
    with lock:
        print n, '-->', result

if __name__ == '__main__':
    # print fib(10)  # 177 calls
    # print fib(20)  # 21,891 calls
    # print fib(30)  # 2,692,537 calls
    # print fib(40)

##    for n in range(40):
##        thread = threading.Thread(target=show_fib, args=(n,))
##        thread.start()

    processes = []

    for n in range(40):
        process = multiprocessing.Process(target=show_fib, args=(n,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

