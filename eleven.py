# Number eleven
import numpy as np
from operator import mul
NUM_ROWS = 20
NUM_COLS = 20

mat = np.genfromtxt(open("eleven_input.txt", 'r'))


def horizontal_search(matrix):
	"""Searches whole matrix horizontally"""
	max_prod = 1
	for i in range(NUM_ROWS):
		for j in range(NUM_COLS - 3):
			prod = reduce(mul, matrix[i][j:j+4], 1)
			if prod > max_prod:
				max_prod = prod
	return max_prod

def vertical_search(matrix):
	'''Searches whole matrix vertically'''
	return horizontal_search(matrix.T)

def diagonal_search_left(m):
	''' Searches all left-diagonals'''
	max_prod = 1
	for i in range(NUM_ROWS - 3):
		for j in range(NUM_COLS - 3):
			prod = 1
			for k in range(4):
				prod *= m[i+k][j+k]
			if prod > max_prod:
				max_prod = prod
	return max_prod

def diagonal_search_right(m):
	'''Searches all right-diagonals'''
	max_prod = 1
	for i in xrange(3, NUM_ROWS):
		for j in xrange(3, NUM_ROWS-3):
			prod = 1
			for k in range(4):
				prod *= m[i-k][j+k]
			if prod > max_prod:
				max_prod = prod
	return max_prod
	

print horizontal_search(mat)
print vertical_search(mat)
print diagonal_search_left(mat)
print diagonal_search_right(mat)




