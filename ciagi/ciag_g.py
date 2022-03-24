def ciag_g(a=1, b=4, ile=10):
    ciag = []
    wynik=a
    for i in range(0,ile,1):
        wynik=wynik*b
        ciag.append(wynik)
    return ciag
print("Ciąg geometryczny:", ciag_g())




