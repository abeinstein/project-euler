# Project Euler -- Problem 26
import decimal as d
from itertools import izip

def chunks(it, n):
    ''' Produces an iterator grouped by chunks of size n
    Ex: chunks(count(), 3) -> (0,1,2), (3,4,5), (6,7,8), ...
    '''
    return izip(*[iter(it)]*n)

def recurring_cycle(frac):
    ''' Takes a fraction, returns the length of the recurring cycle '''
    frac = d.Decimal(frac)
    decimal_digts = str(frac % 1)[2:]

    recurring_cycle = 1
    temp_counter = 1

    while not success:
        for _ in chunks:


    # Check for 3 iterations
    num_iterations = 3
    for _ in num_iterations:
