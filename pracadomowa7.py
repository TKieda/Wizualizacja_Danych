import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#### Zad 1 rozszerzone ####
# print("\nZadanie 1\n")

###Wykres liniowy####
# xlsx = pd.ExcelFile('imiona.xlsx') # wczytanie xlsx
# df = pd.read_excel(xlsx, header=0)
# roczniki = df['Rok'].unique()
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(grupa)

# wykres = grupa.plot()
# wykres.set_ylabel('Liczba urodzonych dzieci')
# wykres.set_xticks(roczniki)
# wykres.tick_params(axis='x', labelrotation=40)
# wykres.legend()
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
# plt.title("Liczba urodzonych dzieci dla każdego roku")
# plt.show()

###Wykres kolumnowy###

# xlsx = pd.ExcelFile('imiona.xlsx') # wczytanie xlsx
# df = pd.read_excel(xlsx, header=0)
# roczniki = df['Rok'].unique()
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(grupa)
# wykres = grupa.plot.bar(ylabel='Liczba urodzeń', xlabel='Lata',alpha=0.5) # alpha-przezroczystość wykresu, plt.barh()-odwrócenie wykresu
# wykres.legend().remove() # remove - wyłącza legendę
# # plt.xticks(rotation=0)
# plt.title("Liczba urodzeń w latach 2000-2017")
# # plt.figure(figsize=(20,10)) # wielkość wykresu
# plt.show()


###Histogram - tylko brzydki...###

# xlsx = pd.ExcelFile('imiona.xlsx') # wczytanie xlsx
# df = pd.read_excel(xlsx, header=0)
# roczniki = df['Rok'].unique()
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(grupa)

# plt.hist(grupa,bins=50, facecolor='g', alpha=0.75, density=True)
# plt.xlabel('Lata')
# plt.ylabel('Liczba urodzeń')
# plt.title('Histogram')
# plt.show()

###Wykres kołowy###

# xlsx = pd.ExcelFile('imiona.xlsx') # wczytanie xlsx
# df = pd.read_excel(xlsx, header=0)
# roczniki = df['Rok'].unique()
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# print(grupa)

# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=10, figsize=(10,10), legend=(3,0))
# plt.legend().remove()
# plt.show()


#### Zad 2 ####
# print("\nZadanie 2\n")
#
# xlsx = pd.ExcelFile('imiona.xlsx') # wczytanie xlsx
# df = pd.read_excel(xlsx, header=0)
# grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
# print(grupa)
# wykres = grupa.plot.bar(ylabel='Liczba urodzeń w mln', xlabel='Płeć',alpha=0.5, color=['green','red']) # alpha-przezroczystość wykresu, plt.barh()-odwrócenie wykresu
# wykres.legend().remove() # remove - wyłącza legendę
# plt.xticks(rotation=0)
# plt.title("Liczba urodzeń w latach 2000-2017")
# plt.show()

#### Zad 3 ####
# print("\nZadanie 3\n")
#
# xlsx = pd.ExcelFile('imiona.xlsx') # wczytanie xlsx
# df = pd.read_excel(xlsx, header=0)
# roczniki = df['Rok'].unique()
# grupa = df[df['Rok'] > 2012].groupby(['Plec']).agg({'Liczba':['sum']})
# print(grupa)
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(10,10), legend=(3,0))
# plt.legend()
# plt.show()

#### Zad 4 ####
# print("\nZadanie 4\n")
#
# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
# grupa = df.groupby('Sprzedawca').size()
# print(grupa)
#
# wykres = grupa.plot.bar(ylabel='Ilość zamówień', xlabel='Sprzedawca',alpha=0.5) # alpha-przezroczystość wykresu, plt.barh()-odwrócenie wykresu
# wykres.legend().remove() # remove - wyłącza legendę
# #plt.xticks(rotation=0)
# plt.title("Ilość złożonych zamówień przez poszczególnych sprzedawców")
# #plt.figure(figsize=(5,4)) # wielkość wykresu ??
# plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9)
plt.show()
