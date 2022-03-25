import sys as system
import math
#########LAB 2##########
#### Zad1. ####
print("\n Zadanie 1 \n")

ulubione_sporty=['siatkówka','piłka ręczna', 'hokej']
print(ulubione_sporty)
ulubione_sporty.reverse()
ulubione_sporty.append('koszykówka')
ulubione_sporty.append('piłka nożna')
print(ulubione_sporty)

#### Zad2. ####
print("\n Zadanie 2 \n")

slownik1={"gg":"goodgame", "wp":"wellplay", "hf":"havefun"}
print(slownik1["gg"])
print(slownik1["wp"])
print(slownik1["hf"])

#### Zad3. ####
print("\n Zadanie 3 \n")

slownik2={"W3":"Witcher 3","OW":"Overwatch","PVR":"Pavlov VR","CIV6":"Civilization 6"}
print("Liczba elementów w słowniku:", len(slownik2))

#### Zad4. ####
print("\n Zadanie 4 \n")

l=input("Napisz zdanie:")
print("Ilość liter 'a' wynosi:", l.count("a")+l.count("A"))

#### Zad5. ####
print("\n Zadanie 5 \n")

system.stdout.write("Podaj trzy liczby oddzielając je spacjami: ")
liczby1 = system.stdin.readline().split(' ')
if (len(liczby1)==3):
    dzialanie=math.pow(int(liczby1[0]),int(liczby1[1]))+int(liczby1[2])
    print("Wynik: ", end="")
    system.stdout.write(str(dzialanie))
else:
    print("Wprowadzono za mało bądź za dużo liczb")

#### Zad6. ####
print("\n Zadanie 6 \n")

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))
lista1 = [a,b,c]
for liczba in lista1:
    if a < b:
        a=b
        for liczba in lista1:
           if b<c:
                a=c
print("\nNajwiększą liczbą jest:", a)

#### Zad7. ####
print("\n Zadanie 7 \n")

lista2 = [1,2,3,3.5,4.5,5.6]
for element in lista2:
    print(math.pow(element, 2))

#### Zad8. ####
print("\n Zadanie 8 \n")

liczby2=[0]*10
liczbyParzyste=[]
n=0

while n<10:
    liczby2[n]=int(input("Podaj " +str(n+1)+ " liczbę:"))
    n+=1
print("Tablica ze wszystkimi liczbami", liczby2)

x=0
while x<10:
    if liczby2[x]%2==0:
        liczbyParzyste.append(liczby2[x])
    x+=1
print("Tablica tylko z parzystymi liczbami:", liczbyParzyste)

#### Zad9. ####
print("\n Zadanie 9 \n")

k=int(input("Podaj liczbę: "))
try:
    print("wynik: ", math.sqrt(k))
except:
    if k<0:
        print("Liczba nie może być ujemna.")
