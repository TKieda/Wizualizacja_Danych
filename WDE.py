import sys
import numpy as np
import math
import random
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
##########Zestaw 24##############

#######ZAD 1########

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


#######ZAD 3######## ???????????????

# df = pd.read_csv('apteki24.csv', header=0, sep=";", decimal=".")
# grupa = df('Nazwa').groupby(['Rok']==2017)
# print(grupa)
# grupa.plot(kind='bar', ylabel='Wartosc',xlabel='Nazwa', title='Wartosc aptek w 2017', legend=True)
# plt.show()

##########Zestaw 1##############

#######ZAD 1########

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

plt.axis([-0.60, 5.25, 0, 150])
# plt.savefig('1.pdf', format='pdf')
plt.show()


##########Zestaw 2##############

#######ZAD 1########