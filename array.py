#numpy
import numpy as np

a = np.arange(20)
print(a)
b =  np.arange(1, 20, 3)
print(b)
c = np.array([])
print(c)
d = np.array([10, 20, 30, 40,50])
print(d)
e = np.array([[1, 2, 3],
              [4, 5, 6]])
print(e)
print(type(e))
print(type(e[0][0]))
print(e.dtype)
g = np.array(['1', '2', '3'])
print(type(g[0]))
print(g.dtype)
f = np.array(['1', '2', '3'], dtype=np.int32)
print(type(f[0]))
h = d.astype(np.str)
print(type(h[0]))
print(h.dtype)

print(e.shape)
print(d.shape)

i = np.array([
    [np.arange(1, 5), np.arange(5, 9), np.arange(9, 13)],
     [np.arange(13, 17), np.arange(17, 21), np.arange(21, 25)]])
print(i.shape)
print(i)

print(f[2])
print(e[1,1])
