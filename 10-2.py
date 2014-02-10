j=0
max = 1000
sieve = range(2,max)

for i in sieve:

	j += 1

	for i in sieve[j:]:

		if i % p == 0:
			sieve.remove(i)

print sieve
