def fac(x):
    prod = 1
    for i in range(1, x+1):
        prod *= i
    return prod

def curious(x):
    return x == sum(map(lambda i: fac(int(i)), list(str(x))))


if __name__ == "__main__":
    print sum([x for x in range(10, 1000000) if curious(x)])

