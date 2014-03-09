def is_pyth_triplet(x, y, z):
	return x**2 + y**2 == z**2


for a in range(1000):
	for b in range(1000):
		for c in range(1000):
			if a + b + c == 1000 and is_pyth_triplet(a,b,c):
				print a, b, c
				print a * b * c



