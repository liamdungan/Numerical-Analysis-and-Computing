# Liam Dungan - CS323 Numerical Analysis - Nov. 14, 2017
# HW4 problem 2
import math

# For f(x) = x^2 - 3x + 2 = 0
# Each of the following represents an equivalent fixed point problem


# diverges - cannot use
def g1(x):
	return ((math.pow(x, 2.) + 2.) / 3.)


# converges
def g2(x):
	return math.sqrt((3. * x) - 2.)


# converges
def g3(x):
	return (3. - (2. / x))


# converges
def g4(x):
	return ((math.pow(x, 2.) - 2.) / ((2. * x) - 3.))


# fpi() impliments fixed point iteration to return the root of a given problem
# param g : the g(x) to be used in the iteration (choose one defined above)
# param x : int, the intial guess
# param maxep : float, the max epsilon allowed before iteration stops
# param maxit : int, the max iterations allowed before iteration stops
def fpi(g, x, maxep, maxit):
	print "\nInitial guess: ", x
	i = 0
	e = abs(g(x) - x)
	while e > maxep and i < maxit:
		i += 1
		e = abs(g(x) - x)
		x = g(x)
		print i, "\tx: ", x, "\te: ", e
	print "The root is: ", x
	return x


def main():
	# fpi(g1, 5, 10e-5, 50)
	fpi(g2, 5, 10e-5, 50)
	# fpi(g3, 5, 10e-5, 50)
	# fpi(g4, 5, 10e-5, 50)


if __name__ == "__main__":
	main()
