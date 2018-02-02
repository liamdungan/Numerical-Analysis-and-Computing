# L iam Dungan - CS 323 Homework 2
# Oct. 17,2017

import numpy as np
np.set_printoptions(precision=2)
np.set_printoptions(suppress=True)


def LU(A, b):
	s = A.shape[0]
	t = A.shape[1]
	if s != t:
		print "Invalid: Matrix is not square"
		return

	p = A.shape[0]
	M = np.ndarray(shape=(p, p, p))
	L = np.ndarray(shape=(p, p, p))

	Lfinal = np.identity(p)
	Ufinal = np.identity(p)

	for i in range(0, p - 1):
		M[i] = np.identity(p)
		M[i][i, i] = np.float(1) / A[i, i]

		for j in range(i + 1, p):
			M[i][j, i] = (np.float(-1) * A[j, i]) / A[i, i]

		A = M[i].dot(A)
		L[i] = np.linalg.inv(M[i])
		Lfinal = Lfinal.dot(L[i])

	Lfinal = np.linalg.inv(Lfinal)
	Ufinal = np.linalg.inv(A)

	print "\nx = ", Ufinal.dot(Lfinal.dot(b))
	print "\n L = \n", Lfinal
	print "\n U = \n", Ufinal


def main():
	A = np.matrix([[21. ,32. ,14. ,8. ,6. ,9. ,11. ,3. ,5 ],
		[17. ,2. ,8. ,14. ,55. ,23. ,19. ,1. ,6 ],
		[41. ,23. ,13. ,5. ,11. ,22. ,26. ,7. ,9 ],
		[12. ,11. ,5. ,8. ,3. ,15. ,7. ,25. ,19 ],
		[14. ,7. ,3. ,5. ,11. ,23. ,8. ,7. ,9 ],
		[2. ,8. ,5. ,7. ,1. ,13. ,23. ,11. ,17 ],
		[11. ,7. ,9. ,5. ,3. ,8. ,26. ,13. ,17 ],
		[23. ,1. ,5. ,19. ,11. ,7. ,9. ,4. ,16 ],
		[31. ,5. ,12. ,7. ,13. ,17. ,24. ,3. ,11]])
	b = np.array([2. ,5. ,7. ,1. ,6. ,9. ,4. ,8. ,3.])
	LU(A, b)


if __name__ == "__main__":
	main()
