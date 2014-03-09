def factorial(n):
    return reduce(lambda x, y: x*y, xrange(1, n+1))

print sum(map(lambda c: int(c), list(str(factorial(100)))))