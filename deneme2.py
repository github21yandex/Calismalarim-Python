
import locale
import sys
locale.setlocale(locale.LC_ALL, "tr_TR.utf-8")
a = ["ali", "veli", "ahmet", "cengiz"]
e = ["ayse", "vefa", "asli", "ceren"]
b = ""
c = "MERHABA İZNİNİZLE ISPARTA VE iskata"
d = 13

dosya = open("yeni", "r+")

dosya.truncate(19)