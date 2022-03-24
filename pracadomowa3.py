import random
import math
import sys
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
print("\nZadanie 2\n")

lista1 = []
for x in range(0,10):
     r = random.randint(1, 100)
     lista1.append(r)
lista2 = [i for i in lista1 if i % 2 == 0]
print(lista1)
print(lista2)

#### Zad3 #####
print("\nZadanie 3\n")

slownik1 = {"czekolada":"szt", "pomidory":"kg", "woda":"l", "ziemniaki":"kg", "bułki":"szt", "jajka":"szt"}
print(slownik1)
slownik2 = {value: key for key, value in slownik1.items() if value == "szt" }
print(slownik2)

##### Zad4 #####
print("\nZadanie 4\n")

def trojkat(a,b,c):
     if pow(a,2)+pow(b,2)==pow(c,2):
          print("Trójkąt jest prostokątny")
     else:
          print("Trójkąt nie jest prostokątny")
print(trojkat(3,4,5))
print(trojkat(1,2,3))

##### Zad5 #####
print("\nZadanie 5\n")

def trapez(a=2,b=1,h=3):
     p=((a + b) * h) / 2
     return p
print(trapez())

##### Zad6 #####
print("\nZadanie 6\n")
def ciag_a(a1=1, b=4, ile=10):
    ciag = []
    for wynik in range(0, ile, 1):
        wynik = a1 * b
        a1 += 1
        ciag.append(wynik)
    return ciag
print(ciag_a())

##### Zad7 #####
print("\nZadanie 7\n")

def ciag2(* ile):
     ciag2 = []
     b = 4
     for i in ile:
          wynik = i * b
          ciag2.append(wynik)
          i += 1
     return ciag2
print(ciag2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

##### Zad8 #####
print("\nZadanie 8\n")

def zakupy(** lista):
     wartosc = 0
     for i in lista:
          wartosc += lista[i]
     print("W koszyku znajdują się",len(lista),"przedmioty o łącznej wartości", wartosc,end=".")
zakupy(karta_graficzna=3500, procesor=1500, plyta_glowna=600, pamiec_ram=400)

##### Zad9 #####
print("\n\nZadanie 9\n")

import ciagi.ciag_g

##### Zad10 #####
print("\n\nZadanie 10\n")


lista = []
for x in range(0, 100, 1):
    if x % 4 == 0 and x!=0:
        lista.append(x)

txt = open("generator.txt", "w")
txt.writelines(str(lista))
txt.close()


##### Zad11 #####
print("\n\nZadanie 11\n")
txt = open("generator.txt","r")
print(txt.read())
txt.close()