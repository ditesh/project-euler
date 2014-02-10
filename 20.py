result = 1
sum = 0

for i in range(1,101):
	result *= i

result = str(result)

for i in result:
	sum += int(i)

print sum
