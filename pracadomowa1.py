import math

#### Zad1. ####
print("\n Zadanie 1 \n")

a=10
b=3
c=2.71
d=3.14
e=1+3j
f=2+4j
g="Tomasz"
h="Kieda"

print(a, b, c, d, e, f, g, h)
print(type(a),type(b),type(c),type(d),type(e), type(f), type(g), type(h))

#### Zad2. ####
print("\n Zadanie 2 \n")

i=input("wprowadź pierwszą liczbę: ")
j=input("wprowadź drugą liczbę: ")
i=int(i)
j=int(j)
print("Dodawanie:", i+j)
print("Odejmowanie:", i-j)
print("Dzielenie:", i/j)
print("Dzielenie całkowite:", i//j)
print("Mnożenie:", i*j)
print("Reszta z dzielenia:", i%j)
print("Potęgowanie:", i**j)
print("Potęgowanie:", pow(i,j))

#### Zad3. ####
print("\n Zadanie 3 \n")

k=10
print("Pierwsza wartosć:", k)
k+=3
print("Dodawanie:", k)
k-=5
print("Odejmowanie:", k)
k*=2
print("Mnożenie:", k)
k/=2
print("Dzielenie:", k)
k**=2
print("Potęgowanie:", k)
k%=3
print("Reszta:", k)

#### Zad4. ####
print("\n Zadanie 4 \n")

print("Wartość e:", math.e)
print("e do potęgi 10:", math.e**10)
print("Obliczenie:", math.pow(math.log(5+pow(math.sin(8),2)), 1/6))
print("Zaorkąglenie w dół:", math.floor(3.55))
print("Zaokrąglenie w górę:", math.ceil(4.80))

#### Zad5. ####
print("\n Zadanie 5 \n")

l1="TOMASZ"
m1="KIEDA"
l2=l1.capitalize()
m2=m1.capitalize()
print(l2, m2)

#### Zad6. ####
print("\n Zadanie 6 \n")

n="na na na na na na na"
m=n.count("na")
print("Słowo 'na' występuje",m, "razy.")

#### Zad7. ####
print("\n Zadanie 7 \n")

imie="Zmienna łańcuchowa"
print("Drugi znak:", imie[1],"\n","Ostatni znak:", imie[-1])

#### Zad8. ####
print("\n Zadanie 8 \n")

n1=n.split(" ")
print(n1)

#### Zad9. ####
print("\n Zadanie 9 \n")

o="jakiś string"
p=1.5
r=0xF44

print('Zmienna o: {0:s} \n Zmienna p: {1:.3f} \n Zmienna r: {2:X}'.format(o,p,r))