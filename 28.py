# ulam spirals

i = 1
increment = 2
maxdepth = 1001
diag = [1]
depth = 1

while True:

	depth += 2
	if depth > maxdepth: break
	for x in range(1, 5):

		i += increment
		diag.append(i)
		
	increment += 2

print diag, sum(diag)
