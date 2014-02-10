import euler
import sys

primeset = set()

for i in range(1001, 10000, 1):

        if euler.isPrime(i) is True: primeset = primeset | {str(i)}

diffdict = {}
primedict= {}

# Get list of permuted numbers that are primes
for prime in primeset:

        tperms=[]
        xperms=euler.getPerms(prime)

        for perm in xperms:
                if perm in primeset: tperms.append(perm)

	tperms.sort()
	tperms = tperms[tperms.index(prime):]
	primedict[prime]=tperms

	for i in range(len(tperms)-1, 0, -1):

		sub = int(tperms[i]) - int(tperms[0])

		if sub in diffdict: diffdict[sub].append({tperms[0], tperms[i]})
		else: diffdict[sub] = [{tperms[0], tperms[i]}]

for diff in diffdict:

	for k,v in enumerate(diffdict[diff]):

		for i,j in enumerate(diffdict[diff]):

			if i <= k: continue

			if len(v.intersection(j)) > 0 and len(v | j) is 3:
				print v | j
