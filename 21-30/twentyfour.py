# Project Euler 24

from itertools import islice, permutations

if __name__ == "__main__":
    # Solved in one line of code!
    print ''.join(islice(permutations('0123456789'), 999999, 1000000).next())