# Project Euler -- Problem 28

def sum_diagonals(size):
    diagonal_sum = 1
    current_diagonal = 1
    increment = 2 # Size is always increment + 1

    while increment <= size:
        for _ in range(4):
            current_diagonal += increment
            diagonal_sum += current_diagonal
        increment += 2

    return diagonal_sum

if __name__ == "__main__":
    print sum_diagonals(5)
    print sum_diagonals(1001)

