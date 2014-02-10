import math
import euler
from sets import Set

squares = {}
matches = {}

for i in range(1000):
	squares[i*i] = i


for p in range(3, 1001):

	print p
	matchCount = []

	for a in range(1, 998):

		if a >= p-2:
			break

		for b in range(1, 998):

			if a+b >= p-1:
				break

			c = a*a + b*b

			if c not in squares:
				continue

			c = int(math.sqrt(c))

			if (a + b + c) != p:
				continue

			results = [a, b, c]
			results.sort()

			x = results.pop()
			resultstr = str(x)

			x = results.pop()
			resultstr += "+"+str(x)

			x = results.pop()
			resultstr += "+"+str(x)

			if resultstr not in matchCount:
				matchCount.append(resultstr)

	matches[p] = len(matchCount)

biggestVal = 0

for key, val in matches.items():
	if val > biggestVal:
		print key, val
		biggestVal = val
