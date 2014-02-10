import math
import euler

highestPrimeCount = 0

for a in range(-999, 1000):

	for b in range(-999, 1000):

		n = -1
		primeCount = 0

		while True:

			n += 1
			prime = int(math.pow(n, 2) + a*n + b)

			if not euler.isPrime(prime):
				break

			primeCount += 1

		if primeCount > highestPrimeCount:
			highestPrimeCount = primeCount
			highestA = a
			highestB = b
		

print highestA, highestB, highestPrimeCount
