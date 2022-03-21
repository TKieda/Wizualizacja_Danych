import random
import math

#########LAB 3##########



##### Zad1 #####
print("\nZadanie 1\n")
# A = {1-x: x∈<1,10>}
# B = {1,4,16,…,4^7}
# C = {x: x∈B i x jest liczbą podzielną przez 2}

a = [1-x for x in range(1,11)]
b = [4**i for i in range(8)]
c = [x for x in b if x % 2 == 0]
print(a)
print(b)
print(c)


##### Zad2 #####
# print("\nZadanie 2\n")
#
# lista1 = []
# for x in range(0,10):
#      r = random.randint(1, 100)
#      lista1.append(r)
# lista2 = [i for i in lista1 if i % 2 == 0]
# print(lista1)
# print(lista2)
#
# ##### Zad3 #####
# print("\nZadanie 3\n")
#
# slownik1 = {"czekolada":"szt", "pomidory":"kg", "truskawki":"kg", "ziemniaki":"kg", "bułki":"szt", "jajka":"szt"}
# print(slownik1)
# slownik2 = {value: 'szt' for value, value in slownik1.items()}
# print(slownik2)