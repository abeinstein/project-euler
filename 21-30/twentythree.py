# Project Euler Problem 23
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

def is_abundant(num):
    return sum_proper_factors(num) > num

def abundant_numbers(limit):
    nums = []
    for i in xrange(12, limit):
        if is_abundant(i):
            nums.append(i)

    return nums



14061
def find_answer():
    ''' Finds the sum of all positive integers
    that cannot be written as the sum of two abundant numbers 
    '''
    candidates = list(range(28124))
    ab_nums = abundant_numbers(28124) 
    for i in range(len(ab_nums)):
        for j in range(i, len(ab_nums)):
            try:
                candidates[ab_nums[i]+ab_nums[j]] = 0
            except IndexError:
                pass

    print candidates
    return sum(candidates)

