

komutlar = ["ekle", "sonaekle", "yazdır", "sil", "sırala", "çek", "tersçevir"]

girdi = input("")

liste = []

while girdi != "" :

   girdi = girdi.split()

   komut = girdi[0]

   if komut == "ekle" :

      konum  = int ( girdi[1] )
      eleman = int ( girdi[2] )

      liste.insert(konum, eleman)

   elif komut == "sonaekle":

      eleman = int (girdi[1] )

      liste.append(eleman)

   elif komut == "yazdır":

      print(liste)

   elif komut == "sil":

      eleman = int ( girdi[1] )
      liste.remove(eleman)

   elif komut == "sırala":
      liste.sort()

   elif komut == "çek":
      liste.pop(-1)

   elif komut == "tersçevir":

      temp =[]

      for i in range(len(liste)-1, -1, -1):
         temp.append(liste[i])
   
      liste = temp

   else:
      print("geçersiz komut")
      exit()

   print("liste = " + str(liste))
   
   girdi = input("")
