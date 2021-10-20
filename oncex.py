
liste = []
list1 = []
list2 = []

while True:
    temp = input("kelime gir:")

    liste.append(temp)

    if temp == "":
        break


for i in liste:

    if "x" in i:
        list1.append(i)
    else:
        list2.append(i)

list1.sort()
list2.sort()

print(*list1, sep="\n")
print("\n\n")
print(*list2, sep = "\n")    