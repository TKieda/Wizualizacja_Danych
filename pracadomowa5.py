import numpy as np
import  math

#### Zad 1 ####
print("\nZadanie 1\n")

a = np.array([2,3,4]).reshape((1,3))
b = np.array([5,1,7]).reshape((1,3))
print(a*b)

#### Zad 2 ####
print("\nZadanie 2\n")

c = np.array([2,3,4,7,5,3,2,1,3]).reshape((3,3))
print(c)
d = np.array([6,4,2,6,7,9,0,2,3,7,3,5,8,4,2,4]).reshape((4,4))
print(c)
print(c.min(axis=0))
print(c.min(axis=1))
print(d)
print(d.min(axis=0))
print(d.min(axis=1))