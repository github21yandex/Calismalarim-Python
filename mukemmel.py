

def mukemmel(sayi):
    liste = [   i for i in range(2, sayi) if sayi%i == 0  ]
    toplam = 0

    for i in liste:
        toplam = toplam+i

    if (toplam == sayi):
        return True
    else: 
        return False


print(  mukemmel(7)  )