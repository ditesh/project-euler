#!/usr/bin/env python

import csv

fp = open("22.txt", "r")
reader = csv.reader(fp)

for row in reader:
	x = row

x.sort()
rsum = 0
i = 1

for name in x:

	csum = 0

	for alphabet in name:
		csum += ord(alphabet)-64

	rsum += i*csum
	i += 1

print rsum
