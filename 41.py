import euler

maxi = 0

for i in range(4, 10):

	perms = euler.getPerms(''.join(map(str, range(1,i))))
	newperms = []

	for perm in perms:
		newperms.append(int(perm))

	perms = newperms
	perms.sort()

	for perm in reversed(perms):

		if euler.isPrime(perm):
			print perm
			break
			
print maxi
