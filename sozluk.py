sozluk = {  "book"      :"kitap",
            "computer"  :"bilgisayar",
            "mouse"     :"fare",
            "tree"      :"agac"}

def ara(kelime):
    hata = "{} kelimesi sozlukte yok"
    return sozluk.get(kelime, hata.format(kelime))
