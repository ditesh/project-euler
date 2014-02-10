import euler
from collections import defaultdict

n = 1
triangles = []
pentagonals = []
hexagonals = []
numbers = defaultdict(int)

while True:

	n += 1

	if n % 1000 == 0:
		print "n =", n

	t = euler.getTriangleNumber(n)

	if t > 50000 and numbers[t] == 2:
		print t
		break

	p = euler.getPentagonalNumber(n)
	numbers[p] += 1

	h = euler.getHexagonalNumber(n)
	numbers[h] += 1
