import numpy as np

A = np.array([[0.16,0.1],[0.17,0.11],[2.02,1.29]])
b = np.array([0.26,0.28,3.31])
b2 = np.array([0.27,0.25,3.33])

#newA = At*A
# ??? ValueError: operands could not be broadcast together with shapes (2,3) (3,1)

newA = np.dot(np.transpose(A) , A)
print "\nL1 cond(A^T*A): ",np.linalg.cond(newA,1)
print "L2 cond(A^T*A): ", np.linalg.cond(newA)

print ""
newb = np.dot(np.transpose(A) , b)
x = np.linalg.solve(newA,newb)
print "For b = ",b,"\t x = ", x

newb2 = np.dot(np.transpose(A) , b2)
x2 = np.linalg.solve(newA,newb2)
print "For b = ",b2,"\t x = ", x2
