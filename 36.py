import euler
import sys

runsum = 0

for x in range(1, 1000000):

    if euler.isPalindromic(str(x)):
        if euler.isPalindromic(euler.int2bin(x)): runsum += x

print runsum
