i = 100
biggest = 0

while i < 1000:

	print "Testing i: ", i
	j = 100

	while j < 1000:

		x = str(i * j)

		if len(x) % 2 == 0:
			for y in range(0,3):
				if x[y] != x[len(x)-y-1]:
					break

				if y == 2:
					if int(x) > biggest:
						biggest = int(x)

					print "Found palindrome: ", x, "for i=", i, " and j=", j

		else:
			for y in range(0,2):
				if x[y] != x[len(x)-y-1]:
					break

				if y == 1:
					if int(x) > biggest:
						biggest = int(x)

					print "Found palindrome: ", x, "for i=", i, " and j=", j
		j += 1

	i += 1

print "Biggest is ", biggest
