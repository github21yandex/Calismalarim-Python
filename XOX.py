

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

tahta = [ ["___", "___", "___"],
          ["___", "___", "___"],
          ["___", "___", "___"],]

print("\n"*15)

kazanma =  [[[0,0],[1,0],[2,0]],
            [[0,1],[1,1],[2,1]],
            [[0,2],[1,2],[2,2]],
            [[0,0],[0,1],[0,2]],
            [[1,0],[1,1],[1,2]],
            [[2,0],[2,1],[2,2]],
            [[0,0],[1,1],[2,2]],
            [[0,2],[1,1],[2,0]]]

xDurumu = []

oDurumu = []

sıra = 1

while True:

    for i in tahta:
        print("\t".expandtabs(30), *i, end = "\n"*2)

    if sıra % 2 == 0:
        isaret = "X".center(3)
    else:
        isaret = "O".center(3)
    print()

    print("İŞARET: {}\n".format(isaret))



    x = input("yukarıdan aşağıya  [1, 2, 3]:".ljust(30))
    if x == "q":
        break

    y = input("yukarıdan aşağıya: [1, 2, 3]".ljust(30))
    if y == "q":
        break

    x = int(x)-1
    y = int(y)-1

    print("\n"*15)

    if tahta[x][y] == "___":
        tahta[x][y] = isaret
        if isaret == "X".center(3):
            xDurumu += [[x,y]]

        elif isaret == "O".center(3):
            oDurumu += [[x,y]]

        sıra += 1

    else:
        print("\nORASI DOLU! TEKRAR DENEYİN\n")

    for i in kazanma:
        o = [z for z in i if z in oDurumu]
        x = [z for z in i if z in xDurumu]

        if len(o) == len(i):
            print("O KAZANDI!")
            quit()

        if len(x) == len(i):
            print("X KAZANDI!")
            quit()

