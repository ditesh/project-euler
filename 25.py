import euler

i = 2
x = 1
y = 1

while True:

	i += 1
	z = x + y
	x = y
	y = z

	if euler.digits(z) == 1000:
		break

print i
