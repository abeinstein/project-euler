import math

def triangle_numbers():
	i = 2
	while True:
		yield sum(range(i))
		i += 1

def num_factors(n):
	factor_count = 0
	sqrt = math.sqrt(n)
	for i in xrange(1, int(sqrt)+1):
		if n % i == 0:
			if i == sqrt:
				factor_count += 1 # Don't add sqrt twice
			else:
				factor_count += 2

	return factor_count

def first_tri_number_over_x_divisors(x):
	tris = triangle_numbers()
	candidate = tris.next()
	while num_factors(candidate) <= x:
		candidate = tris.next()

	return candidate

print first_tri_number_over_x_divisors(500)