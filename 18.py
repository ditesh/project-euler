#!/usr/bin/env python
import node
import graph

matrix = {}
lines = []
fp = open("18.txt", "r")
row=-1

for line in fp:

	i = -1
	row += 1

	elements = line.split()
	matrix[row] = []

	for element in elements:

		i += 1
		nodeobj = node.Node(int(element), str(row) + " " + str(i))
		matrix[row].append(nodeobj)

while row > 0:

	child = matrix[row][0]
	parent = matrix[row-1][0]
	child.setParent(parent)
	parent.setChild(child)

	i = 0
	children = matrix[row]

	for child in children[1:-1]:

		parent = matrix[row-1][i]
		child.setParent(parent)
		parent.setChild(child)

		parent = matrix[row-1][i+1]
		child.setParent(parent)
		parent.setChild(child)

		i += 1
		
	child = matrix[row][len(children)-1]
	parent = matrix[row-1][i]
	child.setParent(parent)
	parent.setChild(child)

	row -= 1

row = len(matrix)-2

while True:

	if row < 0: break

	for child in matrix[row]:

		maxval = 0
		for n in child.children:
			if n.value > maxval: maxval = n.value

		child.value = maxval + child.value

	row -= 1

print matrix[0][0].value
