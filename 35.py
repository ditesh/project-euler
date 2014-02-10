import euler
import math

count = 1
validprimeset = set([2])
invalidset = set()

for i in range(3, 10000, 2):

	if i not in validprimeset and i not in invalidset:

		notprime = False
		perms = euler.getPerms(str(i))
		perms = set(map(int, perms))

		tmp = []
		for perm in perms:

			for j in range(2, int((math.sqrt(perm)))): tmp.append(j*perm)

			if not euler.isPrime(perm):
				invalidset = invalidset | set([perm])
				notprime = True
				break

#		invalidset = invalidset | set(tmp)

		if notprime is False:
			count += len(perms)
			validprimeset = validprimeset | perms
	

print count, len(validprimeset), len(invalidset)
