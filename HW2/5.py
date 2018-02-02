
# Liam Dungan - CS 323 Homework 2
# Oct. 17,2017
# Gaussian elimination without pivoting
# Problem 5

import numpy as np
import math


# Forward substitution of lower triangular matrix
def forward(A, b, n):
    for r in range(0, n - 1):
        for i in range(r + 1, n):
            temp = A[i, r] / A[r, r]
            for j in range(r, n):
                A[i, j] = A[i, j] - temp * A[r, j]

            b[i] = b[i] - temp * b[r]
    return A, b


# Back sub of upper triangular matrix
def back(a, b, n):
    x = np.zeros((n, 1))
    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for r in range(n - 2, -1, -1):
        sums = b[r]
        for j in range(r + 1, n):
            sums = sums - a[r, j] * x[j]

        x[r] = sums / a[r, r]
    return x


def gaussian(A, b):
    n = A.shape[0]
    if any(np.diag(A) == 0):
        print "Error: diagnol elements zero"
        return
    A, b = forward(A, b, n)
    return back(A, b, n)


def main():
    for k in range(1, 11):
        epsilon = math.pow(10, -2 * k)
        A = np.array([[epsilon, 1, ], [1, 1, ], ])
        b = np.array([1 + epsilon, 2, ])
        x = gaussian(A, b)
        print "k:", k, ",\tx = \n", x
        print ""


if __name__ == '__main__':
    main()
