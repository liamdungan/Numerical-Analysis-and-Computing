# Liam Dungan - CS323 Numerical Analysis - Nov. 14, 2017
# HW4 problem 3
import math


# Example equations
def a(x):
	return (x**3) - (2 * x) - 5


def b(x):
	return (math.e**(-x)) - x


def c(x):
	return x * math.sin(x) - 1


def d(x):
	return (x**3) - (3 * (x**2)) + (3 * x) - 1


# Derivatives of each Equation
def da(x):
	return (3 * (x**2)) - 2


def db(x):
	return -(math.e**(-x)) - 1


def dc(x):
	return x * math.cos(x) + math.sin(x)


def dd(x):
	return (3 * (x**2)) - (6 * x) + 3


# An implimentation of the Newton's method for finding roots of a function
# param f : the function
# param df : the derivative of the fucntion
# param x : int, the intial guess
# param maxep : float, the max epsilon allowed before iteration stops i.e 10e-5
def newtons(f, df, x, maxep):
	temp = x
	x = x - (f(x) / df(x))
	e = abs(x - temp)
	while e > maxep:
		temp = x
		x = x - (f(x) / df(x))
		e = abs(x - temp)
	print x
	return x


# An implimentation of the bisection method for finding roots of a function
# param f : the function
# param a : int, start of the interval containing root
# param b : int, end of the interval containing root
# param maxep : float, the max epsilon allowed before iteration stops i.e 10e-5
def bisection(f, a, b, maxep):
	mid = (a + b) / 2.
	while (b - a) > maxep:
		if f(mid) == 0:
			return mid
		elif f(a) * f(mid) < 0:
			b = mid
		else:
			a = mid
		mid = (a + b) / 2.
	print mid
	return mid


# An implimentation of the Secant method for finding roots of a function
# param f : the function
# param x : int, the first initial guess
# param x2 : int, the second intial guess
# param maxep : float, the max epsilon allowed before iteration stops i.e 10e-5
def secant(f, x, x2, maxep):
	while abs(f(x2) - f(x)) > maxep:
		temp = x2 - (f(x2) * (x2 - x) * 1.0) / (f(x2) - f(x))
		x = x2
		x2 = temp
	print x2
	return x2


def main():
	print "\nNewton's Method: "
	newtons(a, da, 2., 10e-5)
	newtons(b, db, 2., 10e-5)
	newtons(c, dc, 1., 10e-5)
	newtons(d, dd, 2., 10e-5)
	print "\nBisection Method: "
	bisection(a, 0, 5, 10e-5)
	bisection(b, 0, 5, 10e-5)
	bisection(c, 0, 5, 10e-5)
	bisection(d, 0, 5, 10e-5)
	print "\nSecant Method: "
	secant(a, 0, 3, 10e-5)
	secant(b, 0, 3, 10e-5)
	secant(c, 0, 2, 10e-5)
	secant(d, 0, 3, 10e-5)


if __name__ == "__main__":
	main()
