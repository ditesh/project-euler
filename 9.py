import sys
import math

a = 1
b = 1
c = 0

for i in range(1, 1001):

	print "Now testing i: ", i

	for j in range(1, 1001):

		a = i
		b = j

		cs = a*a + b*b
		c = math.sqrt(cs)

		if c != round(c):
			continue

		elif a + b + c == 1000:
			print "a: ", a, ", b: ", b, ", c:", c
			print "ans: ", a * b * c
			sys.exit(0)

