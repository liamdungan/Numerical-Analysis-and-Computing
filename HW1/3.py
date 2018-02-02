import math


# problem 3
def stirling(temp):
    return math.sqrt(2 * math.pi * temp) * (temp / math.e)**temp


print "n", "\t", "Stirling", "\tFactorial", "\tAbs Err", "\t\tRel Err"
n = 1
for x in range(1, 11):
    n *= x
    absErr = abs(stirling(x) - n)
    relErr = (absErr / stirling(x)) * 100
    print x, "\t", stirling(x), "\t", n, "\t\t", absErr, "\t\t", relErr
