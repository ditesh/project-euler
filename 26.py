import euler

ds = []
ds.append(0)

for den in range(11, 1000):

	i = 0
	lastnum = 0

	if den > 10: num = 100
	else: num = 1000

	while True:

		rem = num % den
		div = num / den

		if lastnum == rem:
			i -= 1
			break
		elif div is 0: break
		else:
			i += 1
			lastnum = rem
			num = rem * 10

	print den, i

