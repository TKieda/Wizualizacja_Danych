import sys
import numpy as np
import math
import random
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd

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
# del lista['key3']   # usunięcie elementu za pomocą 'del'
# lista.pop('key4')
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

# nowa_lista = [1,2,3,4,5]
# moja_lista[:3] – elementy od pierwszego (domyślnie jeśli nie podano) do trzeciego: [1,2,3]
# moja_lista[2:] – od trzeciego do ostatniego [3,4,5]
# moja_lista[:] – wszystkie elementy listy [1,2,3,4,5]
# moja_lista[-2:] – dwa ostatnie elementy [4,5]
# moja_lista[:-1] – od pierwszego do przedostatniego [1,2,3,4]
# moja_lista[3:-3] – od czwartego do czwartego od końca [3]
# moja_lista[::2] – Wyświetl wszystko, ale co drugi element listy [1,3,5]
# moja_list[::-1] – odwrócenie kolejności listy – wyświetlenie elementów od końca do początku [5, 4, 3, 2, 1]

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

# d= math.pow(math.log(5+math.pow(math.sin(8),2)),1/6)

# lista10=[1,2,3,'a','b','c']
# lista11=[]
# lista12=[]
#
# for z in lista10:
#     if type(z)== int:
#         lista11.append(z)
#     else:
#         lista12.append(z)
# print(lista11)
# print(lista12)
#
# print("Liczb jest:", len(lista11))
# print("Liczb jest:", len(lista12))

#######matplotlib 3.5.1

# grupa = df.groupby('Kontynent').agg({'Populacja':[sum]})
# grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Populacja w mld', rot=0, title='Populacja na kontynentach', legend=True)
#
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynenty')
# wykres.set_ylabel('Populacja w mld')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.set_title('Populacja na kontynentach')
# plt.show()

# grupa = df3.groupby('Imię i nazwisko').agg({'Wartość zamówienia':['sum']})
# print(grupa)
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(8,6), colors=['red','green'], legend=(3,0))
# plt.legend(loc='upper left')
# plt.savefig('plot.png')
# plt.show()

# seria = pd.Series(np.random.randn(1000))
# seria = seria.cumsum()
# print(seria)
#
# seria.plot()
# plt.show()

# plt.plot([1,2,3,4],[1,4,9,16],'ro:',label='linia')
# plt.ylabel('wartości z wektora')
# plt.show()
#
# plt.plot([1,2,3,4],[1,4,9,16],'r:')
# plt.plot([1,2,3,4],[1,4,9,16],'bo')
# plt.axis([0,6,0,20]) #ustawienie max i min na osiach
# plt.show()


# t = np.arange(0,5,0.1)
# plt.plot(t,t,'r-',t,t**2,'b:',t,t**3,'g^')
# plt.legend(labels=['liniowa','kwadratowa','szescienna'],loc='center left')
# plt.show()
# x = np.linspace(0,2,100)
#
# plt.plot(x,x, label='liniowa')
# plt.plot(x,x**2,label='kwadratowa')
# plt.plot(x,x**3,label='sześcienna')
# plt.xlabel('etykieta na osi x')
# plt.ylabel('etykieta na osi y')
# plt.title('tytuł wykresu')
# plt.savefig('plot.png')
# plt.savefig('plot.jpg')
# plt.show()
# im1 = Image.Open('plot.png')
# im1 = im1.convert('RGB')
# im1.save('plot.jpg')

## Zadanie 1 ##

# x = np.arange(1,21,1)
# plt.plot(x,(1/x))
# plt.xlabel('Od 1 do 20')
# plt.ylabel('1/x')
# plt.title('Wykres')
# plt.show()

# x = np.arange(1,10,0.1)
# y = np.sin(x)
# plt.plot(x,y)
# plt.xlabel('etykieta na osi x')
# plt.ylabel('etykieta na osi y')
# plt.title('Wykres')
# plt.legend(labels=['Wahania nastroju kobiety przed okresem'], loc='upper center')
# plt.show()

# x1 = np.arange(0,2,0.02) # od 0 do 2 z krokiem 0.02
# x2 = np.arange(0,2,0.02)
#
# y1=np.sin(2*np.pi*x1)
# y2=np.cos(2*np.pi*x2)
#
# plt.subplot(2,1,1)
# plt.plot(x1, y1)
# plt.ylabel('sin(x)')
# plt.xlabel('x')
# plt.title('Wykres sin(x)')
# plt.subplot(2,1,2)
# plt.plot(x2,y2,'r-')
# plt.ylabel('cos(x)')
# plt.xlabel('x')
# plt.title('Wykres cos(x)')
#
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# x1 = np.arange(0,2,0.02) # od 0 do 2 z krokiem 0.02
# x2 = np.arange(0,2,0.02)
# y1=np.sin(2*np.pi*x1)
# y2=np.cos(2*np.pi*x2)
# fig, axs = plt.subplots(3,2) # trzy wiersze, dwie kolumny
# print(type(fig))
# print(type(axs))
#
# axs[0,0].plot(x1,y1, 'g-')
# axs[0,0].set_xlabel('x')
# axs[0,0].set_ylabel('sin(x)')
# axs[0,0].set_title('Wykres sin(x)')
#
# axs[1,1].plot(x2,y2,'r-')
# axs[1,1].set_xlabel('x')
# axs[1,1].set_ylabel('cos(x)')
# axs[1,1].set_title('Wykres cos(x)')
#
# axs[2,0].plot(x2,y2,'r-')
# axs[2,0].set_xlabel('x')
# axs[2,0].set_ylabel('cos(x)')
# axs[2,0].set_title('Wykres cos(x)')
# fig.delaxes(axs[0,1])
# fig.delaxes(axs[1,0])
# fig.delaxes(axs[2,1])
# plt.show()

# data = {'a':np.arange(50),'c':np.random.randint(0,51,50),'d':np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter(data=data,x='a', y='b',c='c', s='d') #tworzy wykres punktowy
# plt.xlabel('Wartości z klucza a')
# plt.ylabel('Wartości z klucza b')
# plt.show()

###Wykres kolumnowy#####

# dane={'Kraj':['Belgia','Indie','Brazylia','Polska'],'Stolica': ['Bruksela', 'New Delhi','Brasilia','Warszawa'], 'Populacja':[131244234,1233432535,34234232534,12342342342], 'Kontynent':['Europa','Azja', 'Ameryka','Europa']}
# df = pd.DataFrame(dane)
# print(df)
# grupa = df.groupby('Kontynent')
# etykiety = list(grupa.groups.keys())
# wartosci = list(grupa.agg('Populacja').sum())
# print(etykiety)
# print(wartosci)
# plt.bar(x=etykiety,height=wartosci,color=['red','green','yellow'])
# plt.xlabel('Kontynent')
# plt.ylabel('Populacja na kontynentach')
# plt.show()

###Histogram#####

# x = np.random.randn(10000)
#
# plt.hist(x,bins=50, facecolor='g', alpha=0.75, density=True)
#
# plt.xlabel('Wartości')
# plt.ylabel('Prawdopodobieństwa')
# plt.title('Histogram')
# plt.show()

####Zadanie 1####

# x = np.linspace(1,20,75) # od-do i ilość wartości
# x1 = np.arange(1,21,1) # od-do+1 oraz krok
# plt.plot(x,(1/x))
# plt.xlabel('Od 1 do 20')
# plt.ylabel('f(x)=1/x')
# plt.title('Wykres')
# plt.show()
# print(x1)

####Zadanie 2####
####Pandas####

###Wykres liniowy####

# xlsx = pd.ExcelFile('imiona.xlsx') # wczytanie xlsx
# df = pd.read_excel(xlsx, header=0)
# roczniki = df['Rok'].unique()
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(grupa)
# wykres = grupa.plot()
# wykres.set_ylabel('Liczba urodzonych dzieci')
# wykres.set_xticks(roczniki)
# wykres.tick_params(axis='x', labelrotation=50) # labelrotation,axis - ułożenie opisów na zaznaczonym wektorze
# wykres.legend()
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
# plt.title("Liczba urodzonych dzieci dla każdego roku")
# plt.show()

###Wykres kolumnowy###

# xlsx = pd.ExcelFile('imiona.xlsx') # wczytanie xlsx
# df = pd.read_excel(xlsx, header=0)
# roczniki = df['Rok'].unique() # obsługuje przypadki, w których nie jest posortowane lub ma zduplikowane wartości
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(grupa)
# wykres = grupa.plot.bar(ylabel='Liczba urodzeń', xlabel='Lata',alpha=0.5, figsize=(8,8) # alpha-przezroczystość wykresu, plt.barh()-odwrócenie wykresu
# wykres.legend().remove() # remove - wyłącza legendę
# plt.xticks(rotation=30)
# plt.title("Liczba urodzeń w latach 2000-2017")
# plt.figure(figsize=(20,10)) # wielkość wykresu
# plt.show()

###Wykres kołowy###
# xlsx = pd.ExcelFile('imiona.xlsx') # wczytanie xlsx
# df = pd.read_excel(xlsx, header=0)
# roczniki = df['Rok'].unique()
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(grupa)
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=15, figsize=(10,10), legend=(3,0)) ## kind - rodzaj wykresu(bar:kolumnowy,barh:kolmnowy obrocony,pie:kołowy, plot:liniowy, scatter:rozproszony)
# plt.legend().remove()
# plt.show()