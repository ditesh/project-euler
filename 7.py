import sys

primes = [2, 3, 5, 7, 11, 13]
i = 15

while True:

	for j in primes:
		if i % j == 0:
			break

		if j == primes[-1:].pop():
			primes.append(i)

	if len(primes) == 10001:
		print primes[-1:]
		sys.exit(0)

	i += 2
