# Project Euler -- Problem 31

PENNY = 1
TWOPENNY = 2
NICKEL = 5
DIME = 10
TWODIME = 20
HALFPOUND = 50
POUND = 100
TWOPOUND = 200

COINS = [PENNY, TWOPENNY, NICKEL, DIME, TWODIME, HALFPOUND, POUND, TWOPOUND]

class Combination():
    coins = COINS
    def __init__(self):
        self.counts = [0 for _ in range(8)]

    def __init__(self, amts):
        self.counts = amts

    def total(self):
        return sum([val*amount for val, amount in zip(self.coins, self.counts)])

    def num_left(self):
        return 200 - self.total()

    def generate_combinations():
        total_sum = 200
        current_sum = 0
        start = [200, 0, 0, 0, 0, 0, 0, 0]
        yield start
        while current_sum < 200:
            start 

    def __str__(self):
        print str(self.counts)

(200, Coins[0]) = (199, perm(1, Coins[1])
= (198, perm())
[200, 0, 0, 0, 0, 0, 0, 0] (200, 0)
[198, 1, 0, 0, 0, 0, 0, 0] (198 + perm(2), Coins[1:])
[196, 2, 0, 0, 0, 0, 0, 0] (196 + perm(4, Coins[1:]))
[195, 0, 1, 0, 0, 0, 0, 0] 
[194, 3, 0, 0, 0, 0, 0, 0]
[193, 1, 1, 0, 0, 0, 0, 0]
[192, 4, 0, 0, 0, 0, 0, 0]
[192, 1, 1, ]

[200, 0, 0, 0, 0, 0, 0, 0]
[199, 1]


def perm(total_val, coin_vals):
    ''' Returns a list, corresponding to the 
    amount of each coin value '''
    


def generate_permutations(total, amounts):
    ''' Generates permutations from left to right'''
    curr = Combination([200, 0, 0, 0, 0, 0, 0, 0])
    yield curr
    while curr.counts != [0, 0, 0, 0, 0, 0, 0, 1]:
        curr.counts[0] -= 1
        curr_index = 1
        while curr_index > 0 and curr_index < 8:
            while curr.total() < 200:
                curr.counts[curr_index] += 1
            if curr.total() == 200:
                yield curr

            while curr.counts[curr_index] > 0:
                curr.counts[curr_index] -= 1

                if curr.num_left() >= Combination.coins[curr_index+1]:
                    curr_index += 1
                    # recur(curr_index+1, )
                
            curr_index -= 1
            


            # if curr.total() == 200:
            #     yield curr
            #     curr.counts[curr_index] -= 1
            #     curr_index -= 1
            # else:
            #     curr.counts[curr_index] -= 1
            #     if curr.counts[curr_index] == 0:
            #         curr_index -= 1





