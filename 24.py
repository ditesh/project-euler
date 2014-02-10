import sys
import euler

o = '0123456789'
perms = ['0']

for i in o[1:]:

	tmpperms = []

	for perm in perms:

		tmpperms.append(i + perm)

		for j in range(len(perm)-1):

			prefix = perm[0:j+1]
			suffix = perm[j+1:]
			tmpperms.append(prefix + i + suffix)

		tmpperms.append(perm + i)

	perms = tmpperms

perms.sort()
print len(perms)
print perms[1000000-1]
