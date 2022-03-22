import sys
import math
import random

print(sys.version)
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
def ciag(* liczby):
# jeżeli nie ma argumentów to
    if len(liczby) == 0:
        return 0
    else:
        suma = 0
#sumujemy elementy ciągu
    for i in liczby:
        suma += i
#zwracamy wartość sumy
    return suma

#wywołanie gdy nie ma argumentów
print(ciag())
#podajemy argumenty
print(ciag(1, 2, 3.5, 4, 5, 6, 7, 8))

