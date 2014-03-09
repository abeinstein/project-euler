# Project Euler -- Problem 21
import math

def sum_proper_factors(n):
    factor_count = 0
    sqrt = math.sqrt(n)
    for i in xrange(1, int(sqrt)+1):
        if n % i == 0:
            if i == sqrt:
                factor_count += sqrt 
            elif i == 1:
                factor_count += 1 # Don't add self
            else:
                factor_count += i + (n / i)

    return factor_count

def all_proper_factor_sums():
    proper_factors = {}
    for i in xrange(1, 10001):
        proper_factors[i] = sum_proper_factors(i)

    return proper_factors

def amicable_numbers(max):
    ''' Returns all the amicable numbers under max '''
    sums = all_proper_factor_sums()
    amicable_nums = []
    for i in xrange(1, max+1):
        for j in xrange(i+1, max+1):
            if sums[i] == j and sums[j] == i:
                amicable_nums.extend([i, j])

    return amicable_nums

if __name__ == "__main__":
    print sum(amicable_numbers(10000))

