import euler

found = []

for i in range(100, 10001):

	if i in found:
		continue

	divisors = euler.getAllFactors(i)
	sum1 = sum(divisors)-i

	divisors = euler.getAllFactors(sum1)
	suma2 = sum(divisors)-i

	if sum1 == suma2 and i != sum1:
		found.append(i)
		found.append(sum1)

print sum(found)
