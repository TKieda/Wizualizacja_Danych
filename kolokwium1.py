import math
######Zestaw A######

######Zad 1######

print("Zadanie 1")
wynik=math.pow(math.sqrt(5/36),1/5)+math.e**5+math.cos(15)**2
print(round(wynik,2))
print("\n")
######Zad 2######
print("Zadanie 2")
lista1=[1,2,3,4,5,5.5,6.5,7.5]
lista2=[]
lista3=[]
for i in lista1:
    if i % 1==0:
        lista2.append(i)
    else:
        lista3.append(i)

print(len(lista2))
print(len(lista3))
print("\n")

######Zad 3######
print("Zadanie 3")

def lista(lista4=[1,2,3,4,"a","b","c","d"]):
    lista5=[]
    for i in lista4:
        try:
            int(i)
            lista5.append(i)
        except:
            str(i)
    return lista5
print(sum(lista()))
print("\n")

######Zad 4######
print("Zadanie 4")
l=int(input("Podaj liczbę w systemie dziesiętnym: "))
try:
    print("Convert...:",oct(l))
except ValueError:
    print("To nie jest liczba w systemie dziesiętnym")