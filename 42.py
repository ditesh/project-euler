import euler
import csv

i=1
itemsum = {}
maxitem = 0
numbers=[]
fp = open("42.txt", "r")
reader = csv.reader(fp)

for row in reader:
	items = row

for item in items:

	runsum = 0

	for x in item:
		runsum += ord(x) - 64

	if runsum > maxitem: maxitem = runsum
	itemsum[item] = runsum

while True:
	number = euler.getTriangleNumber(i)
	if number > maxitem: break
	numbers.append(number)
	i+=1

numbers=frozenset(numbers)
result = 0

for item in itemsum:

	if itemsum[item] in numbers:
		result += 1

print result
