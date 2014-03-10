# Project euler -- Problem 25
from itertools import dropwhile, izip, count

def fib():
    ''' Generator for fibonacci sequence '''
    a, b = 1, 1
    yield a; yield b;
    while True:
        a, b = a+b, a
        yield a



if __name__ == "__main__":
    it = izip(count(1), fib())
    print dropwhile(lambda tup: len(str(tup[1])) < 1000, it).next()[0]


