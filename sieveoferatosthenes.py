
from math import sqrt

n = 100

A = [0,0]
L = []

for p in range(2,n):
    A.append(p)

for p in range(2, int(sqrt(n))):
    if A[p] != 0:
        j = p*p
        while j < n :
            A[j] = 0
            j = j + p

for p in range(2,n):
    if A[p] != 0:
        L.append(A[p])


for i in range(2, len(L)  ):
    print(L[i])

