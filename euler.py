import math
from math import log10
from sets import Set

def int2bin(x):

    retval = []

    while x is not 0:

        retval.append(str(x%2))
        x=x/2

    retval.reverse()
    return "".join(retval)

def isPalindromic(x):

    xlen = len(x)-1
    midpoint = xlen/2

    for k,v in enumerate(x):

        if v != x[xlen-k]:
            return False

        if k == midpoint: break 

    return True

# needs to be tested
def getPerms(o):

	perms = o[0]

	for i in o[1:]:

		tmpperms = []

		for perm in perms:

			tmpperms.append(i + perm)

			for j in range(len(perm)-1):

				prefix = perm[0:j+1]
				suffix = perm[j+1:]
				tmpperms.append(prefix + i + suffix)

			tmpperms.append(perm + i)

		perms = tmpperms

	return perms 


# returns all factors for number x
def getAllFactors(x):

	returnValue = []

	if x < 2: return returnValue

	for i in range(1, x/2+1):

		remainder = x % i

		if remainder == 0: returnValue.append(i)

	returnValue.append(x)

	return returnValue

# returns number of divisors for number x
def getDivisorCount(x):

	count = {}
	returnValue = 1
	primeFactors = getPrimeFactors(x)

	for i in primeFactors:
		if i not in count:
			count[i] = 1

		count[i] += 1

	for k,v in count.iteritems():
		returnValue *= v

	return returnValue


# returns true/false
def isPrime(x):

	x = int(x)

	if x < 2: return False

	if x == 2 or x == 3 or x == 5: return True

	if x % 2 == 0 or x % 3 == 0 or x % 5 == 0: return False

	aPrime = True
	sq = math.sqrt(x)

    # From http://en.wikipedia.org/wiki/Primality_test#Naive_methods
	for k in range(1, x):

		if ((6*k -1) <= sq) or ((6*k + 1) <= sq):
			if (x % (6*k+1) == 0) or (x % (6*k-1) == 0):
				aPrime = False
				break

		else: break

	return aPrime

# returns prime factorization for number x
def getPrimeFactors(x):

    # base cases
    if x is 1: return []
    if x is 2: return [2]
    if x is 3: return [3]

    def a(y):
        for prime in primes:
            if y % prime is 0: return prime
   
        return None

    returnValue = []
    maxi = math.sqrt(x)
    primes = getPrimes(int(maxi))

    while True:

        prime = a(x)
        if prime is None: prime = x
        returnValue.append(prime)

        x = x/prime
        if x <= 1: break

    return returnValue

# returns all primes <= number x
def getPrimes(x):

	returnValue = [2]

	for i in range(3, x+1, 2):
		if isPrime(i): returnValue.append(i)

	return returnValue


# returns the next triangle number 
def getTriangleNumber2():

	i =0 
	total=0 

	while True:
		i += 1
		total += i
		yield total


def getPermutations(data):

	l = len(data)

	while True:

		perm = swapChars(data, x ,x+1)

		if perm not in returnValue:
			returnValue.append(perm)
	


def swapChars(data, x, y):

	l = len(data)

	if x < 0:
		x = 0

	if y < 0:
		y = 0

	if x > l:
		x = l-1

	if y > l:
		x = l-1

	if x == y:
		return data

	if x > y:
		a = x
		x = y
		y = a

	a = data[:x]
	b = data[y]
	c = data[x+1:y]
	d = data[x]
	e = data[y+1:]

	return a+b+c+d+e

def getTriangleNumber(n):
	return n*(n+1)/2


def getPentagonalNumber(n):
	return n*(3*n-1)/2

def isPentagonalNumber(n):
    x = (math.sqrt(24*n + 1) + 1) / 6
    return (int(x) == x)

def getHexagonalNumber(n):
	return n*(2*n-1)

# Binary GCD algorithm
def gcd(i, j):

	if i == j:
		return i

	elif i == 0 and j == 0:
		return 0

	elif i == 0:
		return j

	elif j == 0:
		return i

	x = i % 2 == 0
	y = j % 2 == 0

	if x is True and y is True:
		return 2*gcd(i/2, j/2)
	elif x is True and y is False:
		return gcd(i/2, j)
	elif x is False and y is True:
		return gcd(i, j/2)
	elif x is False and y is False:

		if j > i:
			return gcd((j-i)/2, i)
		else:
			return gcd((i-j)/2, j)


digits = lambda i: ((i==0) and 1) or int(log10(abs(i)))+1
