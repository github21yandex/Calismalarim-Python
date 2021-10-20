



kelime = input("kelime:")
temp = ""

for i in kelime[1:]:
    
    if i == kelime[0]:
        temp += "*"
    else:
        temp += i


kelime = kelime[0]+temp

print(kelime)
print("ali")