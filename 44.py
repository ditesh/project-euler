import euler
import sys

n = 2
sums = {}
minuses = {}
pentagonal = [0, 1, 5]
inverse = {1: 1, 2: 5}


for i in range(3, 10000):
    pentagonal.append(euler.getPentagonalNumber(i))

for k,v in enumerate(pentagonal):

    if k is 0: continue

    for a,b in enumerate(pentagonal[k:]):

        if a is 0: continue

        if (euler.isPentagonalNumber(b-v) is True and euler.isPentagonalNumber(b+v) is True):
            print k, a+k, v+b, b-v
            sys.exit(0)

