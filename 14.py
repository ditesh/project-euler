longest = 0
starting = 0
results = {}

def collatz(chain):

	n = chain[-1:].pop()

	if n == 1:
		return chain

	# run the chain
	if n % 2 == 0:
		n = n/2
	else:
		n = 3*n + 1

	chain.append(n)
	return collatz(chain)

for i in range(2,1000001):
	results = collatz([i])

	if len(results) > longest:
		starting = i
		longest = len(results)
		print "Found longest: ", starting, longest

print "starting: ", starting
print "longest: ", longest
