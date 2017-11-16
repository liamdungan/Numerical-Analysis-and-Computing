#Liam Dungan
#Nov. 5, 2017
#CS 323 - midterm 1 programming assignment

import numpy as np
from scipy.linalg import lu

#Custom forward substitution for lower triangular system
def Forward_Substitution(A,b,x):
    m=A.shape[0]
    n=A.shape[1]
    if(m!=n):
        print 'Invalid: Matrix is not square'
        return
    for j in range(0,n):
        if A[j,j] == 0:
            print 'Invalid: Matrix is singular'
            return          # matrix is singular

        x[j] = b[j]/A[j,j]
        for i in range(j+1,n):
			if( abs(-1. - A[i,j]*x[j]) >= abs(b[i] - A[i,j]*x[j]) ):
				b[i]=-1.
			b[i] = b[i] - A[i,j]*x[j]


#this routine calculates and prints the condition number
def getCond(A1):
#------METHOD-A-------

	#LU Decomposition 
	P,L,U = lu(A1,permute_l = False)

	#transpose the triangular matrices
	Lt = np.transpose(L)
	Ut = np.transpose(U)
	
	#Solve for Y using method A (forward Sub)
	c=np.array([1.,1.,1.])
	v=np.zeros(3)
	Forward_Substitution(Ut,c,v)
	y_a = np.linalg.solve(Lt,v)

	#Find Ratio ||A^-1||
	z_a = np.linalg.solve(A1,y_a)
	ratio_a = np.linalg.norm(z_a)/np.linalg.norm(y_a)


#------METHOD-B-------

	#5 ranodmly generated Ys
	Y = np.array([np.random.rand(3,1),
		np.random.rand(3,1),
		np.random.rand(3,1),
		np.random.rand(3,1),
		np.random.rand(3,1)])
	ratio_b = ( np.linalg.norm(np.linalg.solve(A1,Y[0]) ) / np.linalg.norm(Y[0]) )

	for i in range(5):
		z_norm = np.linalg.norm( np.linalg.solve(A1,Y[i]) )
		y_norm = np.linalg.norm(Y[i])
		if( (z_norm/y_norm) > ratio_b):
			ratio_b = (z_norm/y_norm)

#------Results--------

	#Find l1 norm of matrix A
	n=A1.shape[1]
	normA = 0
	for i in range(0,n):
		vectorNorm = np.linalg.norm(A1[:,i],1)
		if(vectorNorm > normA):
			normA = vectorNorm

	#Actual conition number for comparison
	actualCond = np.linalg.cond(A1,1)
	print "\n \t cond(A):", actualCond

	#Estimate condition number 
	cond_methodA = normA * ratio_a
	cond_methodB = normA * ratio_b

	errorA = (abs(cond_methodA - actualCond)/actualCond )*100
	errorB = (abs(cond_methodB - actualCond)/actualCond )*100
	print "cond(A) method a:\t",cond_methodA,"\t error: ", errorA,"%"
	print "cond(A) method b:\t",cond_methodB,"\t error: ", errorB,"%"




def main():
	#test matrices
	#A1 = np.array([[-10.,7.,0.],[5.,-1.,5.],[-3.,2.,6.]]) 
	A2 = np.array([[92.,66.,25.],[-73.,78.,24.],[-80.,37.,10.]])
	getCond(A2)
 

if __name__ == "__main__":
    main()


