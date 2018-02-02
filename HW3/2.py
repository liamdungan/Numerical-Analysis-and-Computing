#Liam Dungan
#CS 323 
#problem 2 of HW3

import matplotlib.pyplot as plt
from matplotlib import pylab
import numpy as np

points = np.array([(0.0, 1.), (1., 2.7), (2., 5.8), (3, 6.6), (4.,7.5), (5.,9.9)])
x = points[:,0]
y = points[:,1]

# calculate polynomials
z0 = np.polyfit(x, y, 0)
z1 = np.polyfit(x, y, 1)
z2 = np.polyfit(x, y, 2)
z3 = np.polyfit(x, y, 3)
z4 = np.polyfit(x, y, 4)
z5 = np.polyfit(x, y, 5)
f0 = np.poly1d(z0)
f1 = np.poly1d(z1)
f2 = np.poly1d(z2)
f3 = np.poly1d(z3)
f4 = np.poly1d(z4)
f5 = np.poly1d(z5)

#print polynomials
print f0, "\n\n", f1, "\n\n", f2, "\n\n", f3, "\n\n", f4, "\n\n", f5, "\n"

#new x's and y's
x1_new = np.linspace(x[0], x[-1], 50)
y0_new = f0(x1_new)
plt.plot(x,y,'o', x1_new, y0_new)

y1_new = f1(x1_new)
plt.plot(x,y,'o', x1_new, y1_new)

y2_new = f2(x1_new)
plt.plot(x,y,'o', x1_new, y2_new)

y3_new = f3(x1_new)
plt.plot(x,y,'o', x1_new, y3_new)

y4_new = f4(x1_new)
plt.plot(x,y,'o', x1_new, y4_new)

y5_new = f5(x1_new)
plt.plot(x,y,'o', x1_new, y5_new)

plt.show()
