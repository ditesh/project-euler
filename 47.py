import sys
import euler

i=1000
memoized = {}

def getFactors(i):

    if i in memoized: return memoized[i]

    factors = {}
    primes = euler.getUniquePrimeFactors(i)

    for factor in primes: factors[factor] = True

    memoized[i] = factors
    return factors

while True:

    i += 1

    if i % 10000 is 0: print i

    factors1 = factors2 = factors3 = factors4 = {}
    factors1 = getFactors(i)
    factors2 = getFactors(i+1)
    factors3 = getFactors(i+2)
    factors4 = getFactors(i+3)

    if len(factors1) is 4 and len(factors2) is 4 and len(factors3) is 4 and len(factors4) is 4:
        print i, i+1, i+2, i+3
        print factors1, factors2, factors3, factors4
        sys.exit(0)

