import math

i=2
number = 2520
remainder = number
primes = []

while True:

	if remainder % i == 0:
		primes.append(i)
		remainder = remainder / i

		total = 1

		for j in primes:
			total = total * j

		print "Found prime: ", i, ", with total: ", total, ", and remainder: ", remainder

		if remainder == 1:
			break

		i=2

	i += 1
