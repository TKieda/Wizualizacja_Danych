import numpy as np


#### Zad 1 ####
print("\nZadanie 1\n")
a = np.arange(3,48,3)
print(a)

#### Zad 2 ####
print("\nZadanie 2\n")
a = np.array([1.2, 4.332, 7.4])
print("Typ tablicy a to:", a.dtype)
print(a,"\n")
b=np.array(a, dtype='int64')
print("Typ tablicy a po przekonwertowaniu to:",b.dtype)
print(b)
#### Zad 3 ####
print("\nZadanie 3\n")

def tab(n):
    n= input("Podaj wielkosc tablicy: ")
    tab = np.array()