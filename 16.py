result = 1
sum = 0

for i in range(1,1001):
	result = 2 * result

result = str(result)

for i in result:
	sum += int(i)

print sum
