
girdi = input("")

frekans = []

for i in girdi:
   flag = False
   k = -1   
   for j in frekans:
      k += 1

      if i == j[0][0]:
         frekans[k][1] += 1
         flag = True
         break
   
   if flag == False:
      temp = ["",0]
      temp[0] = i
      temp[1] = 1
      frekans.append(temp)

frekans.sort()

for i in range(0, len(frekans)-1):

   for j in range(0, len(frekans)-1):

      if frekans[j][1] < frekans[j+1][1]:
         temp = frekans[j]
         frekans[j] = frekans[j+1]
         frekans[j+1] = temp 


