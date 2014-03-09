## Project Euler, Problem 17


counts = {
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6
}

def count_base(num):
    if num in counts.keys():
        return counts[num]
    else:
        raise Exception(num + " is not a base number")

def count_1_digit(num):
    assert len(str(num)) == 1
    return count_base(num)

def count_2_digit(num):
    assert len(str(num)) == 2
    if num % 10 == 0 or (11 <= num <= 19):
        return count_base(num)
    else:
        t, o = map(int, str(num))
        return count_2_digit(t*10) + count_1_digit(o)

def count_3_digit(num):
    assert len(str(num)) == 3

    h = int(str(num)[0])
    rest = int(str(num)[1:])

    if rest == 0:
        count_rest = 0
    else:
        count_rest = len("and") + count(rest)

    return count_1_digit(h) + len("hundred") + count_rest

def count_4_digit(num):
    assert num == 1000
    return len("onethousand")

def count(num):
    num_digits = len(str(num))
    if num_digits == 1:
        return count_1_digit(num)
    elif num_digits == 2:
        return count_2_digit(num)
    elif num_digits == 3:
        return count_3_digit(num)
    elif num_digits == 4:
        return count_4_digit(num)


if __name__ == "__main__":
    print sum(map(count, range(1, 6)))
    print sum(map(count, range(1, 1001)))

