import pandas as pd
import numpy as np

#### Zad 1 ####
# print("\nZadanie 1\n")
#
# xlsx = pd.ExcelFile('imiona.xlsx') # wczytanie xlsx
# df = pd.read_excel(xlsx, header=0)
# print(df)
#
# #### Zad 2 ####
# print("\nZadanie 2\n")
#
# print(df[df['Liczba']>1000]) # rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
# print(df[df['Imie']=='TOMASZ']) # rekordy gdzie nadane imię to TOMASZ
# print(df.groupby(['Rok']).agg({'Liczba':['sum']})) # suma wszystkich urodzonych dzieci w całym danym okresie
# print(df.groupby(df['Rok']<2006).agg({'Liczba':['sum']})) # suma dzieci urodzonych w latach 2000-2005
# print(df.groupby(['Plec']).agg({'Liczba':['sum']})) # suma urodzonych chłopców i dziewczynek
# print(df.groupby(['Rok','Imie']).agg({'Liczba':['max']}))
# # najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok) ???
# # najbardziej popularne imię dziewczynki i chłopca w całym danym okresie ???


#### Zad 3 ####
print("\nZadanie 3\n")

df = pd.read_csv('zamowienia.csv', header=0, sep=";",decimal=',') # wczytanie csv
print(df)

# listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame) ???
print(df.sort_values(by='Utarg', ascending=True).head(5)) # 5 najwyższych wartości zamówień
