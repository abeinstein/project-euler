import math

def get_primes():
	limit = 2000000
	primes = [2,3,5,7]
	for num in xrange(8,limit):
		if num % 2 == 0 or num % 3 == 0:
			pass
		else:
			r = math.floor(math.sqrt(num))
			div_found = False
			for i in xrange(5, int(r)+1):
				if num % i == 0:
					div_found = True
				elif num % (i+2) == 0:
					div_found = True
			if not div_found:
				primes.append(num)
	print primes
	return primes

print sum(get_primes())





