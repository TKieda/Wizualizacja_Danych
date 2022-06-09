import sys
import numpy as np
import math
import random
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


##########Zestaw 1##############

#######ZAD 1########
###Wykres kolumnowy jeden na drugim###
# e=np.arange(0,5)
#
# x=[0,1,2,3,4]
# y=[101, 70, 75, 25, 50]
# y1=[20, 10, 30, 10, 0]
#
# l = np.arange(0, 6)
# w = np.full(6, 120)
#
# plt.title('Tytuł')
# plt.bar(x=e, height=y, color=['teal', 'darkgreen', 'darkkhaki', 'pink', 'lawngreen'])
# plt.bar(x=e, height=y1, color=['indigo', 'cyan', 'olive', 'blue', 'blue'])
# plt.plot(l, w, 'g')
#
# plt.axis([-0.60, 5.25, 0, 150])
# plt.savefig('1.pdf', format='pdf')
# plt.show()


#######ZAD 2########

# xlsx=pd.ExcelFile('mieszkania1.xlsx')
# df1=pd.read_excel(xlsx, header=0)
# print(df1)
#
# ind = df1[df1['Formy budownictwa'] == 'indywidualne']
# spo = df1[df1['Formy budownictwa'] == 'spółdzielcze']
# kom = df1[df1['Formy budownictwa'] == 'komunalne']
#
# lata = df1.groupby('Rok').groups.keys()
#
# plt.axis([2014, 2019, 0, 90000])
# plt.bar(x = lata, height = ind['Wartość'], color = 'blue', label = 'indywidualne')
# plt.bar(x = lata, height = spo['Wartość'], color = 'gray', label = 'spółdzielcze')
# plt.bar(x = lata, height = kom['Wartość'], color = 'green', label = 'komunalne')
# plt.title('Wykres wartości mieszkań w latach w zależności od formy budownictwa')
# plt.ylabel('Wartość')
# plt.xlabel('Lata')
# plt.text(2014.1, 85000, '166184') # umieszczenie tekstu w odpowiednim miejscu
# plt.legend()
# plt.savefig('mieszkania.pdf', format='pdf')
# plt.show()

##########Zestaw 2##############

#######ZAD 1########
###Wykres liniowy na trzy linie###

# fig, (ax) = plt.subplots(figsize=(8,5.8))
# x = np.arange(-7,7,0.1)
# y= 20*np.sin(x)
# y1=(2*x/5)-2
# y2=7-x
# ax.plot(x, y, 'r--',x,y1,'y--',x,y2,'g-')
# ax.set(xticks=np.arange(-6,7, 2), yticks=np.arange(-30,31,10))
# ax.legend(labels=['y=20*sin(x)', 'y=(2x/5)-2','y=7-x'], loc='lower left')
# ax.set_title('Tytuł ABCD')
# plt.show()


#######ZAD 2########

# xlsx=pd.ExcelFile('mieszkania2.xlsx')
# df=pd.read_excel(xlsx, header=0)
# print(df)
#
# roczniki = df['Rok'].unique()
# grupa = df[df['Rok'] == 2015].groupby(['Formy budownictwa']).agg('Wartość').sum()
# print(grupa)
# def func(pct, allvals):
#     absolute = int(np.round(pct/100.*np.sum(allvals)))
#     return "{:.1f}%\n({:d})".format(pct, absolute)
# grupa.plot(kind='pie', subplots=True, fontsize=9, figsize=(8,8),explode=(0.2,0.2,0.2),autopct=lambda pct: func(pct, grupa),textprops=dict(color="black"))
# plt.title('Wykres',loc="center")
# plt.legend(title="Legenda", loc="upper left", bbox_to_anchor=(0.8, 0.10, 0, 1))
# plt.text(-1,1,166184)
# plt.ylabel(None)
# plt.show()



##########Zestaw 11##############

#######ZAD 1########
### Wykres liniowy na dwie linie###
# labels=['Styczeń','Luty','Marzec','Kwiecień','Maj','Czerwiec']
# values=[21,32,43,77,66,50]
# values1=[50,42,38,22,24,30]
#
# plt.plot(labels,values1,'b--',label="Filmy")
# plt.plot(labels,values,"g",label="Gry")
#
# plt.xlabel('Miesiąc')
# plt.ylabel('Zyski')
# plt.title('Zyski z filmów i gier')
#
# plt.legend(loc='upper left')
# plt.ylim([0,100])
# plt.grid()
# plt.show()

#######ZAD 2########

# xlsx=pd.ExcelFile('lasy11.xlsx')
# df=pd.read_excel(xlsx, header=0)
# print(df)
# grupa = df.groupby(['Rok']).agg({'Wartość':['sum']})
# print(grupa)
# wykres = grupa.plot.bar(ylabel='Wartość', xlabel='Rok',alpha=0.5, figsize=(8,8))
# wykres.legend().remove()
# plt.xticks(rotation=30)
# plt.title("Jednostka w ha")
# plt.figure(figsize=(20,10)) # wielkość wykresu
# plt.show()

##########Zestaw 12##############

#######ZAD 1########
###Podwójny wykres kolumnowy###
# n_groups = 3
# wartosci_nb=[6,33,1]
# wartosci_pm=[8,28,3]
#
# labels=['Hiper markety','Super markety','Domy handolwe']
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
#
# index = np.linspace(1,n_groups*1.2,n_groups)
#
# bar_width = 0.5
# opacity = 0.4
# plt.bar(index - bar_width/2, wartosci_nb, bar_width, label='Rok 2016')
# plt.bar(index + bar_width/2 , wartosci_pm, bar_width, label='Rok 2017')
# plt.xticks(index,labels)
#
# plt.legend(loc='upper right')
#
# plt.title("Informacje o sklepach")
# plt.tight_layout()
# plt.show()


#######ZAD 2########


# xlsx=pd.ExcelFile('lasy12.xlsx')
# df=pd.read_excel(xlsx, header=0)
# print(df)
# grupa = df.groupby(['Rok']).agg({'Wartość':['sum']})
# print(grupa)
# wykres = grupa.plot()
# wykres.set_ylabel('Wartość')
# wykres.tick_params(axis='x', labelrotation=50) # labelrotation,axis - ułożenie opisów na zaznaczonym wektorze
# wykres.legend().remove()
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
# plt.title("W jednostkach ha")
# plt.show()


##########Zestaw 21##############

#######ZAD 1########

###Podwójny wykres kolumnowy###
# n_groups = 3
# wartosci_ryz=[3.75,3.85,3.9]
# wartosci_marchew=[3.55,3.75,3.7]
#
# labels=['Maj','Maj','Czerwiec']
# fig, ax = plt.subplots()
# # index = np.arange(n_groups)
#
# index = np.linspace(1,n_groups*1.2,n_groups)
#
# bar_width = 0.5
# opacity = 0.4
#
# plt.bar(index - bar_width/2, wartosci_ryz, bar_width, label='Ryż')
# plt.bar(index + bar_width/2 , wartosci_marchew, bar_width, label='Marchew')
# plt.xticks(index,labels,)
#
# plt.legend(loc='upper left')
#
# plt.title("Ceny wybranych produktów w 2019 roku")
# plt.tight_layout()
# plt.ylim([3.0,4.0])
# plt.show()

#######ZAD 2########

xlsx=pd.ExcelFile('ceny21.xlsx')
df=pd.read_excel(xlsx, header=0)
print(df)
grupa = df.groupby(['Rok']).agg({'Wartość':['sum']})
print(grupa)
wykres = grupa.plot()
wykres.set_ylabel('Wartość')
wykres.tick_params(axis='x', labelrotation=50) # labelrotation,axis - ułożenie opisów na zaznaczonym wektorze
wykres.legend().remove()
plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
plt.title("W jednostkach zł")
plt.show()


##########Zestaw 22##############

#######ZAD 1########
###Wykres kolumnowy###
# names=['Piłka nożna','Koszykówka','Siatkówka','Golf','Lekkoatletyka','Inne']
# percentages= [40, 29, 16, 1, 6,8]
# plt.pie(percentages,labels=names,explode=(0.1,0,0,0,0,0),autopct='%.f%%')
# plt.title("Wykres popularności sportów")
# plt.show()

##########Zestaw 24##############

#######ZAD 1########
###Wykres liniowy przerywany###
# x=[1,5,6,7,8,9,12,14,16,19,20,21,22,23,26,28,30]
# y=[0.167,0.1675,0.1675,0.1678,0.1677,0.1674,0.1673,0.1683,0.1688,0.1689,0.1693,0.1687,0.1692,0.1691,0.1692,0.1697,0.1695]
# fig, ax = plt.subplots(figsize=(7.2,5.4))
# ax.plot(x,y,'r--')
# ax.set(xticks=np.arange(0,35, 5),yticks=np.arange(0.165,0.170,0.001), title='Wykres w sierpniu 2019')
# plt.text(29, 0.1685 ,'CZK',verticalalignment='baseline',horizontalalignment='right')
# ax.grid()
# plt.show()

#######ZAD 2########

# xlsx = pd.ExcelFile('odpady24.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# grupa = df.groupby('Rodzaje odpadów')['Wartość'].sum()
# grupa.plot(kind='pie', fontsize=15, figsize=(10,10), legend=(5,5), explode=(0.2,0.2,0.2,0.2,0.2), label='')
# plt.title('Info', fontsize=20)
# plt.legend(loc='upper left')
# plt.savefig('zad2.jpg')
# plt.show()