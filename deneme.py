

import sys
import locale

locale.setlocale(locale.LC_ALL, "tr_TR.utf-8")

cumle = "merhaba\tiyi\tmisiN?"
sesli="ıouieaüöIOUİEAÜÖ"
sesliler =""
sessizler=""
gecici=""

tur = "ğıüşöçĞİÜŞÖÇ"
ing = "giusocGIUSOC"

liste = ["ali", "veli", "samet"]

liste = [[1,2,3],[4,5,6],[7,8,9,10]]
liste2 = [1, 2, 3, "mehmed"]


w = open("deneme.txt", "w")
print("ali","ayşe","fatma","veli",sep="\n", file =w)
w.close()
f = open("deneme.txt","r")
dosya = f.readlines()


tc ="12434"

print("tc = %s" %tc)

print("tc = {isim}".format(isim="onur"))

