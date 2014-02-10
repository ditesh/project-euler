import euler
import sys

sys.setrecursionlimit(1000000)

def simplify(i, j):

	istr = str(i)
	jstr = str(j)

	if istr[0] == jstr[0]:
		return (int(istr[1]), int(jstr[1]))

	if istr[1] == jstr[0]:
		return (int(istr[0]), int(jstr[1]))

	if istr[0] == jstr[1]:
		return (int(istr[1]), int(jstr[0]))

	if istr[1] == jstr[1]:
		return (int(istr[0]), int(jstr[0]))

	return (i, j)

num = 1
denom = 1

for i in range(11, 100):

	for j in range(11, 100):

		if i%10 == 0 and j%10 == 0:
			continue

		gcd = euler.gcd(i,j)

		if gcd == 1: continue

		a = i / gcd
		b = j / gcd

		x, y = simplify(i, j)

		# no cancellations
		if x == i and y == j: continue

		gcd = euler.gcd(x, y)
		x = x / gcd
		y = y / gcd

		if x == a and y == b and a < b:
			num *= x
			denom *= y

gcd = euler.gcd(num, denom)

print denom/gcd
