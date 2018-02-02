import numpy as np


# Forward substitution for lower triangular system
def Forward_Substitution(A,b,x):
    m=A.shape[0]
    n=A.shape[1]
    if(m!=n):
        print 'Matrix is not square!'
        return
    for j in range(0,n):
        if A[j,j] == 0:
            print 'Matrix is singular!'
            return          # matrix is singular
        x[j] = b[j] / A[j,j]
        for i in range(j+1,n):
            b[i] = b[i] - A[i,j]*x[j]

# Back substitution for upper triangular system
def Back_Substitution(A,b,x):
    m=A.shape[0]
    n=A.shape[1]
    if(m!=n):
        print 'Matrix is not square!'
        return
    for j in range(n-1,-1,-1):
        if A[j,j] == 0:
            print 'Matrix is singular!'
            return          # matrix is singular
        x[j] = b[j] / A[j,j]
        for i in range(0,j):
            b[i] = b[i] - A[i,j] * x[j]

def gaussian_elimination(A, b, x):
    m=A.shape[0]
    n=A.shape[1]

    U = deepcopy(A)
    L = np.identity(n)
    if(m!=n):
        print 'Matrix is not square!'
        return
    for k in range(0,n-1):
        if A[k,k] == 0:
            return #need pivoting for this problem, but not for problem #5
        for i in range(k+1,n):
            L[i,k] = A[i,k] / A[k,k]
            A[i,k] = A[i,k] / A[k,k]
            U[i,k] = 0.
        for j in range(k+1,n):
            for i in range(k+1,n):
                A[i,j] -= A[i,k] * A[k,j]
                U[i,j] = A[i,j]
    y=np.zeros(n)
    Forward_Substitution(L, b, y)
    Back_Substitution(U, y, x)


A = np.matrix([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]])
b = np.array([0.1, 0.3, 0.5])
x = np.zeros(3)

print('\nEstimated condition number for A is ')
print(np.linalg.cond(A, np.inf))

print('\nSolution to Ax=b\n')
gaussian_elimination(A, b, x)
print x