import euler

sum = 0L
lines = open("13.txt").readlines()

for line in lines:

	sum += long(line.strip())

print str(sum)[:10]
