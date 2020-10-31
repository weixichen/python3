import numpy as np
a = np.arange(1, 13)
print(a)
a.shape = (3, 4)
print(a)
a.shape = (4, 3)
print(a)
b = np.arange(0, 12)
print(b)

b.shape = (3, 4)
print(b)
b.resize(2,4)
print(b)
g = b.transpose()
print(g)

e = np.arange(1,13)
print(e)
print(e.reshape(12, 1))

print(e.reshape(-1, 1))