collatz_term_cache = {}

def collatz(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3*n + 1

def num_terms(x):
	orig_x = x
	num_terms = 1
	while x != 1:
		x = collatz(x)
		if x in collatz_term_cache:
			num_terms += collatz_term_cache[x]
			break
		num_terms += 1
	collatz_term_cache[orig_x] = num_terms
	return num_terms

def longest_term(max_num):
	max_term = 0
	max_i = 0
	for i in xrange(10, max_num):
		term = num_terms(i)
		if term > max_term:
			max_term = term
			max_i = i

	return (max_term, max_i)

print longest_term(1000000)
