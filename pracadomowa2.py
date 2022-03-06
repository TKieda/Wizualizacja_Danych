import sys as system
import math

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

system.stdout.write("Podaj trzy liczby: ")
liczby = system.stdin.readline().split(' ')
if (len(liczby)==3):
    dzialanie=math.pow(int(liczby[0]),int(liczby[1]))+int(liczby[2])
    print("Wynik: ", end="")
    system.stdout.write(str(dzialanie))
else:
    print("Wprowadzono za mało bądź za dużo liczb")

