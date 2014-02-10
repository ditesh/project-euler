import random

class Node:

	value = None
	name = None
	parent = None
	children = None

	def __init__(self, value, name=int(random.random()*1000)):

		self.value = value
		self.name = name
		self.children = []

	def setParent(self, parent):
		self.parent = parent
#		print "My name is " + self.name + " (" + self.val() + ") and my parent's name is " + parent.getName() + " (" + parent.val() + ")"

	def getParent(self):
		return self.parent

	def getChildren(self, parent):
		self.parent = parent

	def setChild(self, child):
		self.children.append(child)
#		print "My name is " + self.name + " (" + self.val() + ") and I have " + str(len(self.children)) + " children"

	def getChildren(self):
		return self.children

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

	def val(self, val=None):
		if val is None: return self.value
		else: self.value = val
