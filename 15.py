#!/usr/bin/env python

import sys
import time
import cProfile

def f1(start):

	global graph, end
	return sum(map(f1, graph[start]))

def f2(start):
	if start == end:
		return 1

	stack = []
	pathCount = 0
	data = {}

	nodes = graph[start]
	data["nodes"] = nodes
	data["currentNode"] = -1
	data["length"] = len(nodes)
	stack.append(data)
	append = stack.append
	pop = stack.pop

	while True:

		try:
			sp = pop()
		except:
			break

		nodes = sp["nodes"]
		currentNode = sp["currentNode"]
		length = sp["length"]

		if currentNode == length - 1:
			continue

		if nodes[currentNode] == end:
			pathCount += 1
			continue

		sp["currentNode"] += 1
		append(sp)

		nodes = graph[nodes[sp["currentNode"]]]

		data = {}
		data["nodes"] = nodes
		data["currentNode"] = -1
		data["length"] = len(nodes)
		append(data)

		
	return pathCount

def creategraph(x, y):

	maze = {}

	for i in range(x):

		for j in range(y):
			
			connections = []

			if i < x-1:
				connections.append(str(i+1)+str(j))

			if j < y-1:
				connections.append(str(i)+str(j+1))


			maze[str(i)+str(j)] = connections

	return maze

x = int(sys.argv[1])
y = int(sys.argv[2])
end = str(x-1)+str(y-1)
graph = creategraph(x, y)
print cProfile.run("f1('00')")
print cProfile.run("f2('00')")
