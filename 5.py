import sys

i=9699680
primes = [2,3,5,7,11,13,17,19]
numbers = [4,6,8,9,10,12,14,15,16,18,20]

while True:

	i = i + 10

	for p in primes:

		if i % p != 0:
			break

		# Last prime
		if p == 19:

			print "Passed prime test: ", i

			for n in numbers:

				if i % n != 0:
					break

				if n == 20:
					print "Found i", i
					sys.exit(0)
