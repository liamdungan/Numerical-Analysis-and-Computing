import math
import numpy as np

# Problem 1
# Using single precision (np.float32)
pi32 = np.float32(math.pi)

absErr = np.float32(abs(pi32-3.))
print("a 	abs err: %.7f	rel err: %.7fpercent" % (absErr, (absErr/pi32)*100))

absErr = np.float32(abs(pi32-3.14))
print("b 	abs err: %.7f	rel err: %.7fperent" % (absErr, (absErr/pi32)*100))

absErr = np.float32(abs(pi32-(22./7)))
print("c 	abs err: %.7f	rel err: %.7fpercent" % (absErr, (absErr/pi32)*100))
