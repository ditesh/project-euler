import euler

i = 0

for triangleNumber in euler.getTriangleNumber():
	count = euler.getDivisorCount(triangleNumber)

	if count > 500:
		break

print "Triangle number: ", triangleNumber
