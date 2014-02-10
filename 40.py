import sys
import math
import time
import euler

i = 1
j = 1
string = "0"

while i	<= 1000000:

	string = string + str(j)
	j += 1
	i = len(string)

output = 1
vals = [1, 10, 100, 1000, 10000, 100000, 1000000]

for val in vals:
	print string[int(val):int(val)+1]
	output *= int(string[int(val):int(val)+1])

print output
