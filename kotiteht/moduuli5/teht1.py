import random
maara = int(input("Anna arpakuutioiden lukumäärän: "))
summa = 0

for i in range(maara):
    silmukaluku = random.randint(1,6)
    summa += silmukaluku
print(summa)