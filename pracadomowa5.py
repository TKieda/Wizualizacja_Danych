import numpy as np
import  math

# #### Zad 1 ####
# print("\nZadanie 1\n")
#
# a = np.array([2,3,4])
# b = np.array([5,1,7])
# c = a * b
# print(c)
# print(a*2)
# print(b*3)
#
# #### Zad 2 ####
# print("\nZadanie 2\n")
#
# c = np.array([2,3,4,7,5,3,2,1,3]).reshape((3,3))
# d = np.array([6,4,2,6,7,9,0,2,3,7,3,5,8,4,2,4]).reshape((4,4))
# print("\nMacierz 3x3\n")
# print(c)
# print('')
# print(d)
# print("Najmniejsze z kolumn:",c.min(axis=0))
# print("Najmniejsze z wierszy:",c.min(axis=1))
# print("Najmniejsze z kolumn:",d.min(axis=0))
# print("Najmniejsze z wierszy:",d.min(axis=1))

#
# #### Zad 3 ####
# print("\nZadanie 3\n")
#
# a = np.array([2,3,4])
# b = np.array([5,1,7])
# c = np.dot(a, b)
# print(c)
#
# #### Zad 4 ####
# print("\nZadanie 4\n")
#
# a = np.array([1, 2, 3]) # macierz z liczb całkowitych
# b = np.linspace(0, 10, 3) # (początek, zakres, ilość liczb) macierz z liczb rzeczywistych
# c = a * b
# print(c)


#
# #### Zad 5 ####
# print("\nZadanie 5\n")
#
# g = np.array([2,3,4,7,5,8]).reshape((2,3))
# a=[]
# for x in g.flat:
#     a.append(math.sin(x))
# print(a)
# ###lub###
# a = np.sin(g)
# print(a)

#
# #### Zad 6 ####
# print("\nZadanie 6\n")
#
# h = np.array([10,12,9,5,34,2]).reshape((2,3))
# b=[]
# for x in h.flat:
#     b.append(math.cos(x))
# print(b)
###lub###
# b = np.cos(h)
# print(b)
#
# #### Zad 7 ####
# print("\nZadanie 7\n")
#
# print(a+b)
###lub###
# dodawanie = np.add(a,b)
# print(dodawanie)
#
#### Zad 8 ####
# print("\nZadanie 8\n")
#
# i = np.array([[3,4,63], [24,5,16], [27,58,69]])
# for x in i:
#     print(x)

#### Zad 9 ####
# print("\nZadanie 9\n")
#
# j = np.array([[3,4,63], [24,5,16], [27,58,69]])
#
# for x in j.flat:
#     print("Element tablicy: ", x)

#### Zad 10 ####
# print("\nZadanie 10\n")
#
# k = np.random.randint(0,99,81).reshape((9,9))
# print(k)
# print(k.reshape((27,3)))

#### Zad 11 ####
# print("\nZadanie 11\n")
#
# a = np.random.randint(0,99,12)
# print(a)
# macierz_1 = a.reshape(3, 4)
# print(macierz_1)
# print(macierz_1.ravel()) # ravel - spłaszczenie macirzy
# macierz_2 = macierz_1.reshape(4,3)
# print(macierz_2)
# print(macierz_2.ravel())
# macierz_3 = macierz_1.reshape(2,6)
# print(macierz_3)
# print(macierz_3.ravel())