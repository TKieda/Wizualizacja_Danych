import sys
import numpy as np
import math
import random
import pandas as pd
import matplotlib.pyplot as plt

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



###Zad 2

# a=math.log(3,27)+math.pow(8/26+math.sin(50),1/3)
# print(a.__round__(3))
#
# ###Zad 3
# lista=[4,3,5,2,1,2,4,6,3,2,7,7]
# lista2=[]
#
# for x in lista[1::2]:
#     if x%2==0:
#         lista2.append(x)
# print(lista2)
# print(len(lista2))

####Zad 1
# def slownik(s={1.1:1,3:4.1,5:6,7:0}):
#     list=[]
#     for key, value in s.items():
#             if key%1==0 and value%1==0:
#                 list.append(key)
#                 list.append(value)
#     return list
# print(slownik())
# print("\n")

# s = {2 : 12, 'a' : 'b', 'c' : 2.3, 4 : 10}
# def slownik(s):
#     lista =[]
#     for x in s:
#         if (type(x) == int):
#             if (type(s[x] == int)):
#                 lista.append(x)
#                 lista.append(s[x])
#     return lista
# print(slownik(s))



####Zad 4


# try:
#     a = int(input("Podaj liczbę a "))
#     b = int(input("Podaj liczbę b "))
#     lista = []
#     for i in range(a, b, 2):
#         lista.append(i ** 2)
#     print(lista)
# except:
#     print("Podany niepoprawny typ danych")

############################### POPRAWKA 22.05 ##########################################

######## Zestaw A #######

# ###Zad.1
# print("Zadanie 1")
# wyr = math.pow(5/9,2)+math.pow(math.log(23+math.sin(45)),1/4)
# print(wyr.__round__(2))
#
# ###Zad.2
# print("\nZadanie 2\n")
# lista=[3,2,3,4,5,4,4,2,2]
# listamin=[]
# for i in lista:
#     if min(lista)==i:
#         listamin.append(i)
# print("Najmniejsza liczba z listy to:",min(lista))
# print("Najmniejszych liczb listy jest:",len(listamin))
#
# ###Zad.3
# print("\nZadanie 3\n")
#
# def fun(lista2=[1,2,3,'a','b',1.2]):
#     znaki = []
#     for i in lista2:
#         if type(i)==str:
#             znaki.append(i)
#     return znaki
# print(fun())
#
#
# ### Zad.4
# print("Zadanie 4\n")
# try:
#     a = int(input("Podaj a:"))
#     lista3 = [1, 2, 3, 4, 5]
#     lista4 = []
#     for i in lista3:
#         if a>i:
#             lista4.append(i)
#     print("Liczb mniejszych od a jest:", len(lista4))
# except ValueError:
#     print("To nie jest liczba")

######## Zestaw A1 #######

###Zad.1
# print("Zadanie 1")
#
# wyr = math.pow(5/36,1/5)+math.pow(math.e,5)+math.pow(math.cos(15),2)
# print(wyr.__round__(2))
#
# ###Zad.2
# print("Zadanie 2")
#
# lista = [1,2,3.4,5.6,3.47,8,9]
# zp = []
# c = []
# for x in lista:
#     if type(x)==int:
#         c.append(x)
#     elif type(x)==float:
#         zp.append(x)
# print(len(c))
# print(len(zp))
#
# ###Zad.3
# print("Zadanie 3")

# lista = [1,2,3,4,'s','d','r']
# l = []
# def fun(lista):
#     l = []
#     for x in lista:
#         if type(x)==int:
#             l.append(x)
#     return sum(l)
# print(fun(lista))
#
# ###Zad.4
# print("Zadanie 4")
#
# try:
#     d = int(input("Podaj liczbę w systemie dziesiętnym:"))
#     print(oct(d))
# except ValueError:
#     print("To nie jest liczba.")

######## Zestaw A2 #######

###Zad.1
# print("Zadanie 1")
#
# s={1.1:1,3:4.1,5:6,7:0,'a':2,9:8}
#
# def slownik(s):
#     list=[]
#     for key, value in s.items():
#             if type(key)==int and type(value)==int:
#                 list.append(key)
#                 list.append(value)
#     return list
# print(slownik(s))
# print("\n")
#
# ###Zad.2
# print("Zadanie 2")
#
# wyr = math.log(27,3)+math.pow(8/26+math.sin(50),1/3)
# print(wyr.__round__(3))
#
# ###Zad.3
# print("Zadanie 3")
#
# l = [1,2,2,4,5,6]
# parz = []
# for x in l[1::2]:
#     if x%2==0:
#         parz.append(x)
# print(len(parz))
#
# ###Zad.4
# print("Zadanie 4")
#
# try:
#     l = []
#     a=int(input("Podaj a:"))
#     b=int(input("Podaj b:"))
#     for x in range(a,b,2):
#         l.append(x**2)
#     print(l)
# except ValueError:
#     print("To nie jest liczba całkowita.")


######## Zestaw B #######

###Zad.1
# print("Zadanie 1")
#
# wyr = math.pow(math.sin(65)+math.pow(4/5,2),1/4)
# print(wyr.__round__(2))
#
# ###Zad.2
# print("Zadanie 2")


# def fun(lista = [1,2,3,'a','s','g',1.2,4.5]):
#
#     for x in lista:
#         if type(x)==int or type(x)==float:
#             l.append(x)
#         elif type(x)==str:
#             z.append(x)
#     return len(z) and len(l)
# print(fun())

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

# a= np.array([20,30,40,50])
# b= np.arange(4)
#
# c=a+b
# print(c)
# d=np.sqrt(b)
# print(d)
#
# e= d + c
# print(e)

# a=np.arange(12).reshape((3,4))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))
# print(a.cumsum(axis=1))
# a=np.arange(3)
# b=np.arange(3)
# print(np.dot(a,b))
# print(a.dot(b))
#
# c=np.arange(3)
# d=np.array([[0],[1],[2]])
# print(c.dot(d))
# e = np.array([[2,4,5],[5,1,7]])
# f=np.array([[2,3],[4,2],[6,1]])
# print(np.dot(e,f))


# a=np.arange(6).reshape((3,2))
# print(a)
# print(a.flat)
# for b in a:
#     print(b)
#     #for c in b:
#    #     print(c)

# a = np.arange(12).reshape((3,4)) # iloczyn w reshape musi być równy arange
# print(a)
# b = a.reshape((4,3))
# print(b)
#
# c = b.ravel() # zmiana do jednowymiarowej
# print(c)
# print(b.T)


###############Pandas########################

# s = pd.Series([1,3,5,'a',5.5])
# print(s)
# s = pd.Series([10,12,14,8], index=['a','b','c','d']) #index - sami tworzymy etykiety
# print(s)
#
# data = {'Kraj':['Belgia', 'Indie','Brazylia'],'Stolica':['Bruksela','New Delphi','Brasilia'],'Populacja':[1234534,12314454,1232345]}
# df = pd.DataFrame(data)
# print(df)

# daty = pd.date_range('20220507', periods=5)
# print(daty)
# df2 = pd.DataFrame(np.random.randn(5,4), index=daty,columns=list('ABCD'))
# print(df2)
#
# df3 = pd.read_csv('dane.csv', header=0, sep=';',decimal='.') # wczytuje plik csv, wczyta 5 pierwszych i 5 ostatnich, header określa gdzie jest nagłówek i gdzie zaczynają się dane
# print(df3)
# xlsx = pd.ExcelFile('imiona.xlsx') # wczytule plik excel
# df = pd.read_excel(xlsx, header=0)
# print(df)
# print(df.head(10)) # czyta pierwsze 10 danych
# print(df.tail(10)) # czyta ostatnie 10 danych
#
# df3.to_csv('dane2.csv', index=False) # zapis do pliku csv
# df.to_excel('imiona2.xlsx', sheet_name='dane') # zapis do pliku excel

# s = pd.Series([10,12,14,8], index=['a','b','c','d']) #index - sami tworzymy etykiety
# print(s)
#
# data = {'Kraj':['Belgia', 'Indie','Brazylia'],'Stolica':['Bruksela','New Delphi','Brasilia'],'Populacja':[1234534,12314454,1232345]}
# df = pd.DataFrame(data)
# print(df)
#
# xlsx =pd.ExcelFile('imiona.xlsx')
# df4 = pd.read_excel(xlsx, header=0)
# print(df4)
# print(df4.head(10))
# print(df4.tail(10))
# print(df.sample())
# print(df.sample(10, replace=True))


# print(s['a'])
# print(s.a)
#
# print(df[0:1])
#
# print(df['Kraj'])
# print(df.Kraj)
# print(df.iloc[[0],[0]])
# print(df.loc[[0],['Kraj']])
# print(df.at[0,'Kraj'])

# print(s['a']) # indeksy
# print(s.a)
# print(df['Kraj'])
# print(df.Kraj)
# ##odwołania do odpowiednich wierszy i kolumn
# print(df[0:1])
# print(df.iloc[[0],[0]])
# print(df.loc[[0],['Kraj']])
# print(df.at[0,'Kraj'])
#
# print(s[s>9])
# print(s.where(s>10, 'warunek niespełniony'))
# seria = s.copy()
# seria.where(s>10, 'warunek niespełniony', inplace=True)
# print(seria)
# print(s[(s>13) & (s > 8)])
#
# print(df[df["Populacja"]>12000000])
# print(df[(df['Populacja']>1000000) & (df.index.isin([0,2]))])

# s['e'] = 14
# print(s)
# df.loc[3] = 'nowy element'
# print(df)
# df.loc[4] = ['Polska', 'Warszawa', 38000000]
# print(df)
#
# new_df = df.drop([3])
# print(new_df)
# df.drop([3], inplace=True)
# print(df)
#
# df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'] # nowa kolumna
# print(df)
#
# df.sort_values('Stolica', inplace=True) # sortowanie bez indeksów
# print(df)

#grupa = df.groupby('Kontynent').agg({'Populacja':[sum]})
# print(grupa.get_group('Europa'))
#
# print(df.groupby('Kontynent').agg({'Populacja':[sum]}))

#matplotlib 3.5.1

# grupa = df.groupby('Kontynent').agg({'Populacja':[sum]})
# grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Populacja w mld', rot=0, title='Populacja na kontynentach', legend=True)

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

#########Wykresy podstawy ############

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum() # funkcja biblioteki pandas generująca skumulowaną sumę kolejnych elementów
# print(ts)
# ts.plot()
# plt.show()


########DataFrame###########

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'], 'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'], 'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'], 'Populacja': [11190846, 1303171035, 207847528, 38675467]}
df = pd.DataFrame(data)
print(df)
grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
print(grupa) #
# grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Mld', rot=0, legend=True, title='Populacja z podzałem na kontynenty')
wykres = grupa.plot.bar()
wykres.set_ylabel("Mld")
wykres.set_xlabel('Kontynent')
wykres.tick_params(axis='x', labelrotation=0)
wykres.legend()
wykres.set_title('Populacja z podzałem na kontynenty')
#plt.xticks(rotation=0)  #zmiana kierunku tekstu etykiet słupków #
plt.savefig('wykres.png')
plt.show()