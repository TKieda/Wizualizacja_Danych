import pandas as pd
import numpy as np

#### Zad 1 ####
# print("\nZadanie 1\n")

# xlsx = pd.ExcelFile('imiona.xlsx') # wczytanie xlsx
# df = pd.read_excel(xlsx, header=0)
# print(df)
#
# #### Zad 2 ####
# print("\nZadanie 2\n")
#
# print(df[df['Liczba']>1000]) # rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
# print(df[df['Imie']=='TOMASZ']) # rekordy gdzie nadane imię to TOMASZ
# print(df.Liczba.sum()) # suma wszystkich urodzonych dzieci w całym danym okresie

# grupa = df[df.Rok < 2006].groupby('Rok').agg({'Liczba': ['sum']}) # suma dzieci urodzonych w latach 2000-2005
# print(grupa)
# grupa = df[df.Rok < 2006] # suma dzieci urodzonych w latach 2000-2005
# print(grupa.Liczba.sum())


# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0)) #??
# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first()) #??

# print(df.groupby(['Plec']).agg({'Liczba':['sum']})) # suma urodzonych chłopców i dziewczynek

# print("M")
# print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'), ascending=False).iloc[0]) # najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok)
# print("K")
# print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'), ascending=False).iloc[0]) # najbardziej popularne imię dziewczynki i chłopca w całym danym okresie ???


#### Zad 3 ####
# print("\nZadanie 3\n")

# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.') # wczytanie csv

# print(df['Sprzedawca'].unique()) # lista unikalnych nazwisk sprzedawców

# print(df.sort_values('Utarg', ascending=False).head(5)) # 5 najwyższych wartości zamówień

# print(df.groupby('Sprzedawca').size()) # ilość zamówień złożonych przez każdego sprzedawcę

# print(df.groupby('Kraj').agg({'Utarg': ['sum']})) # suma utargu każdego kraju
# print(df.groupby('Kraj').size()) # suma zamówień każdego kraju

# print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')].agg({'Utarg': ['sum']})) # sumę zamówień dla roku 2005, dla sprzedawców z Polski

# print(df[df['Data zamowienia'].str[:4] == '2004'].agg({'Utarg': ['mean']}))

# rok_2004 = df[((df[ 'Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))] # średnią kwotę zamówienia w 2004 roku,
# rok_2004.to_csv("zamowienia_2004.csv", index=False) # zapisane dane za 2004 rok do pliku zamówienia_2004.csv
# rok_2005 = df[((df[ 'Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31'))] # średnią kwotę zamówienia w 2004 roku
# rok_2005.to_csv("zamowienia_2005.csv", index=False) # zapisane dane za 2005 do pliku zamówienia_2005.csv