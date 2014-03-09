# Project Euler -- 22

def score(name):
    name = list(name)
    return reduce(lambda x, y: x + to_n(y), name, 0)

def to_n(letter):
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(letter) + 1


if __name__ == "__main__":
    names_f = open("names.txt", 'rb')
    names = [n.strip("\"") for n in names_f.read().split(",")]
    
    names.sort()

    print sum([score(name) * (names.index(name) + 1) for name in names])



