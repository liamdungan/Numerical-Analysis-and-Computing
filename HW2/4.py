
# Liam Dungan - CS 323 Homework 2
# Oct. 17,2017


# Problem 4

import numpy as np
from copy import deepcopy
np.set_printoptions(precision=7)


def forward(A, b, x):
    m = A.shape[0]
    n = A.shape[1]
    if(m != n):
        print "Invalid: Matrix is not square"
        return
    for j in range(0, n):
        if A[j, j] == 0:
            print "Matrix is singular"
            return
        x[j] = np.float32(b[j]) / np.float32(A[j, j])
        for i in range(j + 1, n):
            b[i] = np.float32(b[i]) - np.float32(A[i, j]) * np.float32(x[j])


def back(A, b, x):
    m = A.shape[0]
    n = A.shape[1]
    if(m != n):
        print "Invalid: Matrix is not square"
        return
    for j in range(n - 1, - 1, - 1):
        if A[j, j] == 0:
            print "Matrix is singular"
            return
        x[j] = np.float32(b[j]) / np.float32(A[j, j])
        for i in range(0, j):
            b[i] = np.float32(b[i]) - np.float32(A[i, j]) * np.float32(x[j])


def gaussian(A, b, x):
    m = A.shape[0]
    n = A.shape[1]

    U = np.matrix.copy(A)
    L = np.identity(n)

    if(m != n):
        print "Invalid: Matrix is not square"
        return
    for k in range(0, n - 1):
        if A[k, k] == 0:
            return
        for i in range(k + 1, n):
            L[i, k] = np.float32(A[i, k]) / np.float32(A[k, k])
            A[i, k] = np.float32(A[i, k]) / np.float32(A[k, k])
            U[i, k] = np.float32(0.)
        for j in range(k + 1, n):
            for i in range(k + 1, n):
                A[i, j] -= np.float32(A[i, k]) * np.float32(A[k, j])
                U[i, j] = np.float32(A[i, j])
    y = np.float32(np.zeros(n))
    forward(L, b, y)
    back(U, y, x)


def solution(A, b, x):
    n = A.shape[0]
    bCopy = deepcopy(b)
    gaussian(np.matrix.copy(A), bCopy, x)

    r = np.zeros(n)
    thisX = np.zeros(n)
    newX = np.zeros(n)
    for i in range(0, n):
        thisX[i] = x[i]
    print "x = ", x, "\n\n"

    for temp in range(0, 3):  # no change observed after 3
        aCopy = np.matrix.copy(A)
        Ax = aCopy.dot(thisX)
        for i in range(0, n):
            r[i] = np.float32(b[i] - Ax[0, i])

        print "r = ", r
        z = np.zeros(n)
        gaussian(aCopy, r, z)

        for add in range(0, n):
            newX[add] = thisX[add] + z[add]
        print"Improved: ", newX

        print "\n\n"
        for i in range(0, n):
            thisX[i] = newX[i]


def main():
    A = np.matrix([[21.0, 67.0, 88.0, 73.0],
        [76.0, 63.0, 7.0, 20.0],
        [0.0, 85.0, 56.0, 54.0],
        [19.3, 43.0, 30.2, 29.4]])

    b = np.array([141.0, 109.0, 218.0, 93.7])
    x = np.zeros(4)
    solution(A, b, x)


if __name__ == "__main__":
    main()
