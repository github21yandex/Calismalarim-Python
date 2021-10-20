

k1 = input("birinci kelime:")
k2 = input("ikinci kelime:")

temp1 = k1[0:2]

temp2 = k2[0:2]

for i in k2[2:]:
    temp1 += i

for i in k1[2:]:
    temp2 += i

print(temp2)
print(temp1)