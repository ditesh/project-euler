import math

i = 3

while True:

	sum = 0
	istr = str(i)

	for d in istr:
		sum += math.factorial(int(d))

	if sum == i:
		print i

	i += 1
