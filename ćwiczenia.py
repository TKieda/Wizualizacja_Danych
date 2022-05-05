import sys
import numpy as np
import math
import random

# print(sys.version)
#
# a=15123
# b='Tomek'
# print(b)
# c =15.5
# print(c)
# d=3+2j
# print(d)
#
# e = 7
# f = 3
# print(e // f) # // dzielenie calkowite
# print(e ** f) # ** potęgowanie
# print((2/3) ** f)
# print(math.pow(2/3, f)) # math.pow(e, f) - e-liczba potegowana, f - wykladnik
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# x = 6
# y = 5
#
# if x > y:
#     print('liczba x jest wieksza od liczby y')
# elif x < y:
#     print('liczba y jest wieksza od liczby x')
# else:
#     print('liczby są równe')

# if warunek1:
# --instrukcja lub blok instrukcji dla warunek1
# elif warunek2:
# --instrukcja lub blok instrukcji dla warunek2
# elif warunekN:
# --instrukcja lub blok instrukcji dla warunekN
# else:
# --instrukcja lub blok instrukcji gdy warunki sa niespelnione

# nazwa_zmiennej = wartosc
# ctrl+/ - wstawianie komentarzy

# a=input("wprowadź pierwszą liczbę: ")
# print(a)
# print(type(a))
# a = int(a)
# print(type(a))

# PĘTLE:

# for licznik in sekwencja:
# --instrukcja lub blok instrukcji
# else:
# --instrukcja lub blok instrukcji po pętli
# range(start, stop, step)
#   for(int i=0;i<10;i++) - przykład z c++

# for a in range(0, 7, 1):
#     print (a)

# lista =['a', 3, 4, 5.6]
# for element in lista:
#     print(element)
# else:
#     print("wszystkie elementy wyświetlone")
# print(lista)

# while warunek:
# --instrukcja lub blok instrukcji
# else:
# --instrukcja lub blok instrukcji po zakończeniu pętli

# licznik = 0
# while licznik != 11:
#     print(licznik)
#     licznik +=1
# else:
#     print('zostało wyświetlonych ' + str(licznik) + ' liczb')

# break - zakończenie pętli
#
#len - długość

# lista = [4,6,2,5,9,7,3,1]
# liczba = input('wpisz liczbę: ')
# licznik = 0
#
# while licznik != len(lista):
#     if int(liczba) - lista[licznik] == 0:
#         print('liczba ' + str(liczba) + ' - ' + str(lista[licznik]) + ' = 0')
#         break
#     else:
#         licznik +=1
# else:
#     print('żaden z elementów nie dał odpowiedniego wyniku')
#
# lista1 = [4,6,2,5,6,7,8]
# lista2 = [7,3,5,6]
# suma =  []
# for a in lista1:
#     for b in lista2:
#         wynik = a + b
#         suma.append(wynik)
#     print(suma)

# try:
# --instrukcje, które mogą zawierać błąd
# except nazwa_błędu:
# --instrukcja lub blok instrukcji po wychwyceniu błedu
# except nazwa_błędu
# --instrukcje
# else:
# --blok wynikowy gdy nie było błędu

# liczba1 = input('pierwsza liczba: ')
# liczba2 = input('druga liczba: ')
# try:
#     liczba1 = int(liczba1)
#     liczba2 = int(liczba2)
#     wynik = liczba1 / liczba2
#     print(wynik)
# except ZeroDivisionError:
#     print('nie dzieli się przez zero')
# except ValueError:
#     print('to nie jest liczba')

# lista=[], metody do listy
# słownik = {}, metody do słownika
# klucz:wartość - element ze słownika
# {1:10 , 'klucz':'wartość',1:20}
# https://docs.python.org/pl/3/tutorial/datastructures.html
# https://oprojektowaniu.pl/python-dla-inzynierow-listy/


# Metody listy
# lista = [4,3,1,5,4,2] # lista
# print(len(lista)) # długość listy
# lista.append(0) # dodanie argumentu na końcu listy
# print(lista)
# print(len(lista))
# lista.insert(3, 'abc') # dodanie argumentu do konkretnego miejsca listy
# print(lista)
# print(len(lista))

#Przykład pierwszy

# A = {x^2: x∈<0,9>}
# B = {1,3,9,27,…,3^5}
# C = {x: x∈𝐴 i x jest liczbą nieparzystą}
# a = []
# for x in range(10):
#     a.append(x**2)
# print(a)
# b = []
# for y in range(6):
#     b.append(3**y)
# print(b)
# c = []
# for z in a:
#     if z % 2 == 1:
#         c.append(z)
# print(c)
#
#
# a = [x**2 for x in range(10)]
# b = [3**i for i in range(6)]
# c = [x for x in a if x % 2 == 1]
# print(a)
# print(b)
# print(c)

#Przykład drugi

# liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista = []
# for i in liczby:
#     if i % 2 == 0:
#         lista.append(i)
# print("Liczby parzyste uzyskane z wykorzystaniem pętli")
# print(lista)
# print()
#
# lista2 = [i for i in liczby if i % 2 == 0]
# print(lista2)
#
# liczby2=[0]*10
# liczbyParzyste=[]
# n=0
#
# while n<10:
#     liczby2[n]=int(input("Podaj " +str(n+1)+ " liczbę:"))
#     n+=1
# print("Tablica ze wszystkimi liczbami", liczby2)
#
# x=0
# while x<10:
#     if liczby2[x]%2==0:
#         liczbyParzyste.append(liczby2[x])
#     x+=1
# print("Tablica tylko z parzystymi liczbami:", liczbyParzyste)
#
# lista2 = [i for i in liczby2 if i % 2 == 0]
# print(lista2)

# Przykład czwarty związany ze zamianą klucza z wartością w słowniku
#wersja z pętlą
# skroty = {"PZU": "Państwowy zakład ubezpieczeń",
# "ZUS": "Zaklad ubezpieczeń społecznych",
# "PKO": "Państwowa kasa oszczędności"}
# print(skroty)
# odwrocone = {}
# for key,value in skroty.items():
#     odwrocone[value] = key
# print(odwrocone)
# #wersja z python comprehension
# odwrocone2 = {value: key for key, value in skroty.items()}
# print(odwrocone2)

# Symbol * oznacza dowolną ilość argumentów przechowywanych w krotce
# def ciag(* liczby):
# # jeżeli nie ma argumentów to
#     if len(liczby) == 0:
#         return 0
#     else:
#         suma = 0
# #sumujemy elementy ciągu
#     for i in liczby:
#         suma += i
# #zwracamy wartość sumy
#     return suma
#
# #wywołanie gdy nie ma argumentów
# print(ciag())
# #podajemy argumenty
# print(ciag(1, 2, 3.5, 4, 5, 6, 7, 8))

# def to_lubie(** rzeczy):
#     for cos in rzeczy:
#         print("To jest ")
#         print(cos)
#         print(" co lubie ")
#         print(rzeczy[cos])
# to_lubie(slodycze="czekolada", rozrywka=['gry', 'filmy'])


# print("Sortowanie")
# tab = [0]*3
# for t in range(0,3,1):
#     tab[t]=int(input("Podaj " +str(t+1)+ " liczbę:"))
# print(tab)
#
# for i in range(0,2,1):
#     for j in range(0,2,1):
#         if tab[j]>tab[j+1]:
#             pom=tab[j+1]
#             tab[j+1]=tab[j]
#             tab[j]=pom
# print(tab)

###########Numpy, tablice itd.###################

# a=np.array([1,2,3], dtype='float64')
# print("Typ float", a)
# b=np.array([1,2,3], dtype='int32')
# print("Typ int", b)
# a=np.arange(1,5,0.5)
# print("Tablica zaczynająca się od 1, mająca 5 elementów i zmieniająca się o 0.5",a)
# print("Wypisanie typu tablicy:", a.dtype) # typ tablicy
# #print(type(a))
# print("Rozmiar tablicy:", a.shape) # rozmiar tablicy
# print("Iluwymiarowa tablica:", a.ndim) # ilowymiarowa
#
# print("\nTablica 2x2:")
# b = np.array([np.arange(2), np.arange(2)])
# print(b)
# print("Rozmiar:", b.shape)
# print("Wymiar:", b.ndim)
#
#
# print("\nTablica z samymi zerami:")
# z = np.zeros((5,5), dtype='int32') # tablica z samymi zerami
# print(z)
# print("\nTablica z samymi jedynkami:")
# j = np.ones((5,5)) # tablica z samymi jedynkami
# print(j)
# print("\nTablica z przypadkowymi wartościami:")
# p = np.empty((2,2), dtype='int32')
# print(p)
#
# print("\nTablica 2x2 gdzie we wskazanym miejscu na tablicy wstawiono cyfrę 2:")
# p[1][0] = 2
# print(p)
#
# print("\nPięcioelementowa tablica z pominięciem wartości 2")
# a = np.linspace(1, 2, 5, endpoint=False) # pięcioelementowa tablica z pominięciem wartości 2
# print(a)

# print("\nTablica 5x3 (5 wierszy, 3 kolumny)")
# b, c = np.indices((5,3)) # wartość po kolumnach
# print(b)
# print(c)
# print("Wartość wybrana po indeksie:",b[3][2])
# print("Wartość wybrana po indeksie:",c[3][2])

# print("\nTablica 5x5 (2 wiersze(0:2), 5 kolumn(0:5))")
# d,e = np.mgrid[1:2, 1:5] # watrość po wierszach
# print(d)
# print(e)

# print("\nWektor po przekątnej 4x4, wartość k zmienia wektor tworząc przy tym nowy wiersz.")
# f= np.diag([x for x in range(4)],k=0) #
# print(f)

# print("\nTablica pięcioelementowa.")
# g=np.fromiter(range(5), dtype='int')
# print(g)

# marcin = 'Marcin'
# marcin = b'Marcin'
# mar = np.frombuffer(marcin, dtype='S6')
# print(mar)
#
# mar_1 = np.array(list(marcin))
# print(mar_1)
# mar_2 = np.array(list(b'Marcin')) # kod ASCI
# print(mar_2)
# mar_3 = np.fromiter(marcin, dtype='S1')
# mar_4 = np.fromiter(marcin, dtype='U1')
# print(mar_3)
# print(mar_4)

# a = np.ones((2,2))
# b = np.ones((2,2))
# c = a + b
# print(a)
# print(b)
# print(c)
#
# a = np.arange(10)
# print(a)
# s = slice(2,7,2)
# print(a[s])
# s = range(2,7,2)
# print(a[s])
#
# print(a[2:7:2])
# print(a[1:5])
#
# a = np.arange(25)
# mat = a.reshape((5,5))
# print(a)
# print(mat)
# print(mat[1:, 1:])
# print(mat[:, 1:2])
# print(mat[2:5, 1:3])
#
# a = np.array([[1,2,3], [4,5,6], [7,8,9],[10,11,12]])
# print(a)
#
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0, 2]])
# b=a[rows, cols]
# print(b)

# #Kolos 1#
# print("\n")
# a = math.pow(5/35,1/5)+pow(math.e,5)+pow(math.cos(15),2)
# print(a.__round__(2))
#
# #Kolos 2#
# print("\n")
# b=[1,2,3,4,0.5,1.5,2.5]
# c=[]
# d=[]
# print(b)
# for n in b:
#     if n % 1 == 0:
#         c.append(n)
#     if n % 1 != 0:
#         d.append(n)
# print(len(c))
# print(len(d))
#
# #Kolos 3#
# print("\n")
#
# def lista(lista4=[1,2,3,4,"a","b","c","d"]):
#     lista5=[]
#     for i in lista4:
#         try:
#             int(i)
#             lista5.append(i)
#         except:
#             str(i)
#     print(lista5)
#     return lista5
# print("Suma cyfr z listy wynosi:",sum(lista()))
# print("\n")
#
# #Kolos 4#
# print("\n")
#
# try:
#      l = int(input("Podaj liczbę w systemie dziesiętnym: "))
#      print("Convert...:", oct(l))
# except ValueError:
#      print("To nie jest liczba w systemie dziesiętnym")

# nowa_lista = [1,2,3,4,5]
# moja_lista[:3] – elementy od pierwszego (domyślnie jeśli nie podano) do trzeciego: [1,2,3]
# moja_lista[2:] – od trzeciego do ostatniego [3,4,5]
# moja_lista[:] – wszystkie elementy listy [1,2,3,4,5]
# moja_lista[-2:] – dwa ostatnie elementy [4,5]
# moja_lista[:-1] – od pierwszego do przedostatniego [1,2,3,4]
# moja_lista[3:-3] – od czwartego do czwartego od końca [3]
# moja_lista[::2] – Wyświetl wszystko, ale co drugi element listy [1,3,5]
# moja_list[::-1] – odwrócenie kolejności listy – wyświetlenie elementów od końca do początku [5, 4, 3, 2, 1]

###Zad 2

a=math.log(3,27)+math.pow(8/26+math.sin(50),1/3)
print(a.__round__(3))

###Zad 3
lista=[4,3,5,2,1,2,4,6,3,2,7,7]
lista2=[]

for x in lista[1::2]:
    if x%2==0:
        lista2.append(x)
print(lista2)
print(len(lista2))

####Zad 1
def slownik(s={1.1:1,3:4.1,5:6,7:0}):
    list=[]
    for key, value in s.items():
         if key%1==0 and value%1==0:
            list.append(key)
            list.append(value)
    return list
print(slownik())
print("\n")



