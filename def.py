
def sum(*args):
    
    toplam = 0
    print("args type =", type(args))
    
    for i in args:
        toplam += i
    
    return toplam


print(sum(2,4,5,7,8,6,3,4,5))

def sozlukYap(**kwargs):
    print(kwargs)
    print(type(kwargs))



sozlukYap(book = "kitap",tree = "ağaç")

import random

def sayiUret(adet, basla, bitir):
    sayilar = set()
    while(len(sayilar) < adet):
        sayilar.add(random.randrange(basla,bitir))

    return sayilar

print( sayiUret(7,10,100) )

liste = [1,2,3]
kume = set([1,2,3])

print(kume)

kume.add(5)

print("kume=",kume)
