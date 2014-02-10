terms = []

for a in range(2, 101):
	for b in range(2, 101):
		terms.append(pow(a, b))

print len(set(terms))
