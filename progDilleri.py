

def asalmi(sayi):
    print([sayi % j != 0 for j in range(2, sayi)])

    liste = [sayi % j != 0 for j in range(2, sayi)]
        
    if all(liste):
        return True

asalmi(11)

