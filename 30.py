import math

i = 2

while True:

	sum = 0
	istr = str(i)

	for d in istr:
		sum += math.pow(int(d), 5)

	if sum == i:
		print i

	i += 1
