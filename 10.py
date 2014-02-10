import sys
import math
import time

i = 5
total = 5
primes = [2, 3]
sixTime = 0
primeTime = 0

while True:

	aPrime = True

	if i % 3 != 0:

		sq = math.sqrt(i)

		for k in range(1, i):

			if ((6*k -1) <= sq) or ((6*k + 1) <= sq):
				if (i % (6*k+1) == 0) or (i % (6*k-1) == 0):
					aPrime = False
					break
			else:
				break

		if aPrime is True:
			primes.append(i)

	i += 2

	if i > 100000:
		break

print "Total: ", sum(primes)
