import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#### Zad 1 rozszerzone ####
print("\nZadanie 1\n")

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
# wykres = grupa.plot.barh(ylabel='Liczba urodzeń', xlabel='Lata',alpha=0.5) # alpha-przezroczystość wykresu, plt.barh()-odwrócenie wykresu
# wykres.legend().remove() # remove - wyłącza legendę
# # plt.xticks(rotation=0)
# plt.title("Liczba urodzeń w latach 2000-2017")
# plt.show()


###Histogram - tylko brzydki...###

xlsx = pd.ExcelFile('imiona.xlsx') # wczytanie xlsx
df = pd.read_excel(xlsx, header=0)
roczniki = df['Rok'].unique()
grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
print(grupa)

plt.hist(grupa,bins=50, facecolor='g', alpha=0.75, density=True)
plt.xlabel('Lata')
plt.ylabel('Liczba urodzeń')
plt.title('Histogram')
plt.show()