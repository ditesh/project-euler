import euler

result = 0
abundant = []
runsum = 0
sums = []

for i in range(12, 28112):

	factors = euler.getAllFactors(i)

	if sum(factors[:-1]) > i:
		abundant.append(i)

print len(abundant)

for idx, i in enumerate(abundant):
	for j in abundant[idx:]:
		sums.append(i+j)

print len(sums)
sums = frozenset(sums)

for i in range(1,28123):

	if i not in sums:
		runsum += i

print runsum
