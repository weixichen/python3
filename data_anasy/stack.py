import numpy as np
a = np.arange(11, 20).reshape(3, 3)
print(a)
b = np.arange(21, 30).reshape(3, 3)
print(b)

c = np.vstack((a, b))
print(c)
