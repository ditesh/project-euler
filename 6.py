sum_of_squares = 0
sum = 0

for i in range(1,101):

	print i
	sum_of_squares += (i * i)
	sum += i

print sum, sum_of_squares, sum*sum

print (sum*sum) - sum_of_squares
