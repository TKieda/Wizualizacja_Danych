def ciag(a1=1, b=4, ile=10):
    ciag = []
    for wynik in range(0, ile, 1):
        wynik = a1 * b
        a1 += 1
        ciag.append(wynik)
    print(ciag)


print(ciag())