# I think this question is asking for non-line adjacent

matrix = []
horsum = []
biggest = 0
fp = open("11.txt", "r")

for line in fp:
	elements = line.split()
	newelements = []

	for element in elements:
		element = int(element)
		newelements.append(element)

	matrix.append(newelements)

# horizontal
for i in range(20):

	horsum = []

	for j in range(16):

		if len(horsum) == 4:
			horsum.pop(0)

		horsum.append(matrix[i][j])

		total = 1

		for z in horsum:
			total *= z

		if total > biggest:
			biggest = total

print "horizontal: ", biggest, horsum
biggest=0
biggesthorsum = []

#vertical sum
for i in range(20):

	horsum = []

	for j in range(20):

		if len(horsum) == 4:
			horsum.pop(0)

		horsum.append(matrix[j][i])

		total = 1

		for z in horsum:
			total *= z

		if total > biggest:
			biggest = total
			biggesthorsum = horsum

print "vertical: ", biggest, biggesthorsum
biggest=0
biggesthorsum = []

#diagonal sum slanting right
for i in range(20):
	for j in range(20):

		num = matrix[i][j]

		if i+1 <= 19 and j+1<=19:
			num *= matrix[i+1][j+1]
			
			if i+2 <= 19 and j+2<=19:
				num *= matrix[i+2][j+2]

				if i+3 <= 19 and j+3<=19:
					num *= matrix[i+3][j+3]

		if num > biggest:
			biggest = num
			biggesthorsum = horsum

print "diagonal r: ", biggest, biggesthorsum
biggest=0

#diagonal sum slanting left
for i in range(20):

	for j in range(20):
		
		num = matrix[i][j]

		if i+1 <= 19 and j-1 >= 0:
			num *= matrix[i+1][j-1]
			
			if i+2 <= 19 and j-2 >= 0:
				num *= matrix[i+2][j-2]

				if i+3 <= 19 and j-3 >= 0:
					num *= matrix[i+3][j-3]
		if num > biggest:
			biggest = num

print "diagonal l: ", biggest
biggest=0
