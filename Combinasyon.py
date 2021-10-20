import itertools
import os

def tersi(kelime):
    yeni = ""
    for i in kelime:
        yeni = i + yeni
    return yeni

dosya = open("denemeler.txt", "w")
dosya.close
dosya = open("denemeler.txt", "a")

sonuc = list(itertools.permutations(["2991", "EnceScrtys2015", "2017", "2018", "2019", "2020", "7102", "0202"], 4 ))



for j in sonuc:
    flag = False
    for k in j:
        for l in j:
            if tersi(k) == l:
                flag = True
    
    if j[0] == "EnceScrtys2015" or j[0] == "2019":
        flag =True

    if ("EnceScrtys2015" not in j or  "2991" not in j ):
        flag == True
        continue

    try:
        sira = j.index("EnceScrtys2015")+1

        if sira >= 5:
            flag = True


        for i in j[sira:]:
            if i != "7102" or i != "0202":
                try:
                    if int( j[ j.index(i) + 1 ] ) < int(i):
                        flag = True
                except:
                    pass
    except:
        pass


    try:
        indexEnc = j.index("EnceScrtys2015")
        index2991 = j.index("2991")

        if index2991 > indexEnc:
            flag = True

    except:
        pass
    

    
            

    if flag == False:
        sifre = ""
        for i in j:
            sifre += i

    if flag == False:
        dosya.write("##" + sifre + "$$" + "\n")
        print(sifre)

    flag = False

dosya.close